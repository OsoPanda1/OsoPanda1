use anyhow::{Context, Result};
use chrono::Utc;
use hmac::{Hmac, Mac};
use rand::{seq::IteratorRandom, thread_rng};
use serde::{Deserialize, Serialize};
use sha2::Sha256;
use std::{collections::HashMap, fs, path::PathBuf};
use tokio::time::{interval, Duration};

type HmacSha256 = Hmac<Sha256>;

#[derive(Debug, Deserialize)]
struct Config {
    node: Node,
    mesh: Mesh,
    agent: Agent,
}

#[derive(Debug, Deserialize)]
struct Node { id: u16, next_id: u16, prev_id: u16 }

#[derive(Debug, Deserialize)]
struct Mesh { interface: String, gossip_interval_ms: u64, secret_key: String }

#[derive(Debug, Deserialize)]
struct Agent { retry_limit: u8, chain_timeout_ms: u64 }

#[derive(Debug, Serialize, Deserialize, Clone)]
struct RegistryEntry {
    status: String,
    last_seen: Option<String>,
    chain_seen: Option<String>,
    break_meta: Option<String>,
}

#[derive(Debug, Serialize, Deserialize)]
struct State {
    local_id: u16,
    current_round: Option<String>,
    registry: HashMap<u16, RegistryEntry>,
}

#[derive(Debug, Serialize)]
struct WireMessage<'a, T: Serialize> {
    kind: &'a str,
    from_id: u16,
    timestamp: String,
    nonce: u64,
    payload: T,
    signature: String,
}

#[tokio::main]
async fn main() -> Result<()> {
    let cfg = load_config("config.toml")?;
    let mut state = load_or_init_state("state.json", cfg.node.id)?;

    println!("tamv-agent iniciado en nodo {} sobre {}", cfg.node.id, cfg.mesh.interface);

    let mut ticker = interval(Duration::from_millis(cfg.mesh.gossip_interval_ms));
    loop {
        tokio::select! {
            _ = ticker.tick() => {
                let partial = select_partial_registry(&state.registry, 8);
                let msg = signed_message("STATE_SYNC", cfg.node.id, &partial, &cfg.mesh.secret_key)?;
                println!("gossip -> next={} prev={} entries={} sig={}..", cfg.node.next_id, cfg.node.prev_id, partial.len(), &msg.signature[..8]);
                state.current_round = Some(Utc::now().to_rfc3339());
                persist_state_atomic("state.json", &state)?;
            }
            _ = tokio::signal::ctrl_c() => {
                println!("tamv-agent detenido");
                break;
            }
        }
    }
    Ok(())
}

fn load_config(path: &str) -> Result<Config> {
    let raw = fs::read_to_string(path).with_context(|| format!("no se pudo leer {path}"))?;
    Ok(toml::from_str(&raw).context("config.toml inválido")?)
}

fn load_or_init_state(path: &str, local_id: u16) -> Result<State> {
    if PathBuf::from(path).exists() {
        let raw = fs::read_to_string(path)?;
        return Ok(serde_json::from_str(&raw)?);
    }

    let state = State { local_id, current_round: None, registry: HashMap::new() };
    persist_state_atomic(path, &state)?;
    Ok(state)
}

fn persist_state_atomic(path: &str, state: &State) -> Result<()> {
    let temp = format!("{path}.tmp");
    fs::write(&temp, serde_json::to_vec_pretty(state)?)?;
    fs::rename(temp, path)?;
    Ok(())
}

fn signed_message<T: Serialize>(kind: &str, from_id: u16, payload: &T, secret: &str) -> Result<WireMessage<'_, T>> {
    let nonce = rand::random::<u64>();
    let timestamp = Utc::now().to_rfc3339();
    let body = serde_json::json!({"kind": kind, "from_id": from_id, "timestamp": timestamp, "nonce": nonce, "payload": payload});
    let mut mac = HmacSha256::new_from_slice(secret.as_bytes()).context("secret_key inválida")?;
    mac.update(serde_json::to_string(&body)?.as_bytes());
    let signature = base64::encode(mac.finalize().into_bytes());

    Ok(WireMessage { kind, from_id, timestamp: body["timestamp"].as_str().unwrap().to_string(), nonce, payload, signature })
}

fn select_partial_registry(registry: &HashMap<u16, RegistryEntry>, k: usize) -> HashMap<u16, RegistryEntry> {
    let mut rng = thread_rng();
    registry.iter().choose_multiple(&mut rng, k).into_iter().map(|(id, e)| (*id, e.clone())).collect()
}
