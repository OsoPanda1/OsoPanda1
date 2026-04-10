# 🜂 RDM‑TOS  
## Sovereign Territorial Operating System  

<div align="center">
  <img src="branding/cover.svg" width="100%" alt="RDM-TOS Sovereign Territorial OS Cover"/>
</div>

---

## 📦 ESTRUCTURA DEL PROYECTO

```text
rdm-tos/
├── README.md
├── assets/
│   ├── hero.svg
│   ├── grid.svg
│   └── pulse.svg
├── web/
│   └── index.html
└── branding/
    └── cover.svg
```

Todo lo visual es **propio y autocontenido**: sin servicios externos, sin dependencias de terceros para el look & feel, pensado para funcionar offline y en entornos aislados (edge / air‑gapped).

---

<div align="center">

## 🧬 IDENTIDAD DEL SISTEMA

# RDM‑TOS  
### Sovereign Territorial Operating System  

<img src="assets/hero.svg" width="100%" alt="RDM-TOS Hero"/>

**NODE ZERO:** Real del Monte, México  
**ARCHITECT:** Anubis Villaseñor (Edwin Oswaldo Castillo Trejo)  

---

</div>

## 🧠 DEFINICIÓN

RDM‑TOS es un **sistema operativo territorial** diseñado para restituir control computacional, cognitivo y económico a un territorio físico.

No se limita a ser “software” en sentido convencional:  
es una **infraestructura soberana** que:

- Orquesta datos, modelos y decisiones desde el territorio hacia el territorio.  
- Encapsula una arquitectura heptafederada antifrágil.  
- Ancla la gobernanza en un bucle **human‑in‑the‑loop** explícito.

---

## ⚙️ ARQUITECTURA MACRO

<div align="center">
  <img src="assets/grid.svg" width="100%" alt="RDM-TOS Architecture Grid"/>
</div>

### Núcleo conceptual

- **Kernel MD‑X4** (Isabella Protocol)  
- **Heptafederación** (7 dominios funcionales: DATA, INTEL, SEC, GOV, ECON, VIS, TERRITORY)  
- **Edge‑First Computing** (operación prioritaria en el borde, nube como complemento opcional)  
- **Human‑In‑The‑Loop** innegociable en decisiones estratégicas  

---

## 🌍 PRINCIPIO CIVILIZATORIO

> “El territorio no es contenido.  
> Es el sistema.”

RDM‑TOS asume que un municipio, ciudad o región debe ser tratado con el mismo rigor que un **sistema crítico de misión**: modelado, monitoreado, defendido y optimizado con herramientas de clase mundial, pero bajo control local.

---

## 📡 CAPACIDADES ESTRATÉGICAS

- **Modelado geoespacial real**  
  - Integración de DEMs, GSHHG, y capas vectoriales territoriales.  
- **Telemetría territorial en tiempo real**  
  - WebSockets, buses de eventos y streams de sensores/POIs locales.  
- **Simulación dinámica de escenarios**  
  - Flujos turísticos, logística, rutas, saturación y resiliencia.  
- **Economía local integrada**  
  - Comercio, servicios, cadenas de valor y métricas de impacto en un grafo vivo.

---

## 🔒 SEGURIDAD Y RESILIENCIA

- **Post‑Quantum Ready** (familia de esquemas tipo Kyber / Lattice‑based)  
- **Modelo Zero‑Trust contextualizado al territorio**  
- **Autodestrucción lógica en Q‑Cells** para evitar persistencia de compromisos  
- **Operación degradada** (modo isla / edge‑only) ante fallas de backbone o nube global  

---

## 🧱 BOOTSTRAP MÍNIMO

```bash
git clone https://github.com/tu-org/rdm-tos.git
cd rdm-tos
docker-compose up
```

A partir de aquí:

- Levantas base de datos + servicios básicos.  
- Sirves la landing `web/index.html` desde cualquier servidor estático.  
- Usas los SVGs de `assets/` y `branding/` para GitHub, docs y presentaciones.

---

## 🧬 ARQUITECTO

**Nombre:** Anubis Villaseñor (Edwin Oswaldo Castillo Trejo)  
**Origen:** Real del Monte, Hidalgo, México  

> Soberanía no es discurso.  
> Es ejecución, versión y despliegue.

---

# 🌐 WEB LANDING ( `web/index.html` )

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>RDM-TOS :: Sovereign Territorial OS</title>
  <style>
    :root {
      --bg: #000000;
      --fg: #00F7FF;
      --accent: #FF1717;
      --muted: #777777;
      --font-main: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      --font-mono: "Fira Code", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace;
    }
    * {
      box-sizing: border-box;
    }
    body {
      margin: 0;
      background: radial-gradient(circle at top, #050811 0, #000000 50%, #000000 100%);
      color: var(--fg);
      font-family: var(--font-main);
      -webkit-font-smoothing: antialiased;
    }
    main {
      max-width: 1100px;
      margin: 0 auto;
      padding-bottom: 80px;
    }
    .hero {
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      padding: 40px 24px 0 24px;
    }
    .hero-title {
      font-size: clamp(2.8rem, 5vw, 4.2rem);
      letter-spacing: 0.18em;
      text-transform: uppercase;
      margin: 0 0 12px 0;
      font-family: var(--font-mono);
      animation: glow 2.4s ease-in-out infinite alternate;
    }
    .hero-subtitle {
      font-size: 1.1rem;
      text-transform: uppercase;
      letter-spacing: 0.28em;
      color: var(--muted);
      margin-bottom: 32px;
    }
    .hero-badge {
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.2em;
      border: 1px solid rgba(0, 247, 255, 0.35);
      padding: 8px 16px;
      border-radius: 999px;
      margin-bottom: 24px;
      color: var(--fg);
    }
    .hero-pulse {
      margin-top: 32px;
    }
    .grid-section {
      padding: 60px 24px 0 24px;
    }
    .section {
      padding: 60px 24px 0 24px;
      border-top: 1px solid #111111;
    }
    .section h2 {
      font-family: var(--font-mono);
      font-size: 1.2rem;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      margin: 0 0 12px 0;
      color: var(--accent);
    }
    .section h3 {
      font-family: var(--font-mono);
      font-size: 1rem;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      margin: 24px 0 8px 0;
      color: var(--fg);
    }
    .section p {
      margin: 0 0 10px 0;
      color: #cccccc;
      line-height: 1.6;
      font-size: 0.98rem;
    }
    .columns {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 32px;
      margin-top: 20px;
    }
    .card {
      border: 1px solid #111111;
      border-radius: 16px;
      padding: 18px 20px;
      background: radial-gradient(circle at top, #050811 0, #020409 40%, #020202 100%);
    }
    .card h4 {
      font-family: var(--font-mono);
      font-size: 0.9rem;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      margin: 0 0 8px 0;
      color: var(--fg);
    }
    .card p {
      font-size: 0.9rem;
      color: #bbbbbb;
      margin: 0;
      line-height: 1.5;
    }
    code, pre {
      font-family: var(--font-mono);
      font-size: 0.85rem;
    }
    pre {
      background: #050608;
      border-radius: 10px;
      padding: 14px 16px;
      border: 1px solid #111111;
      overflow-x: auto;
      color: #c5c8c6;
    }
    .footer {
      padding: 40px 24px 20px 24px;
      border-top: 1px solid #111111;
      text-align: center;
      color: #888888;
      font-size: 0.85rem;
    }
    .footer span {
      display: block;
      margin-bottom: 4px;
    }
    @keyframes glow {
      0% { text-shadow: 0 0 10px #00F7FF, 0 0 20px #00F7FF; }
      100% { text-shadow: 0 0 16px #FF1717, 0 0 32px #FF1717; }
    }
    @media (max-width: 768px) {
      .section, .grid-section {
        padding-left: 16px;
        padding-right: 16px;
      }
    }
  </style>
</head>
<body>

<main>
  <section class="hero">
    <div class="hero-badge">NODE ZERO · REAL DEL MONTE · MÉXICO</div>
    <h1 class="hero-title">RDM‑TOS</h1>
    <div class="hero-subtitle">SOVEREIGN TERRITORIAL OPERATING SYSTEM</div>
    <img src="../assets/pulse.svg" width="320" alt="RDM-TOS Pulse" class="hero-pulse"/>
  </section>

  <section class="grid-section">
    <h2>Architecture</h2>
    <p>
      RDM‑TOS modela el territorio como un sistema operativo: datos, inteligencia, seguridad, economía y geoespacio
      convergen en un kernel heptafederado, diseñado para operar en el borde bajo condiciones adversas.
    </p>
    <img src="../assets/grid.svg" width="100%" alt="RDM-TOS Heptafederated Architecture"/>
  </section>

  <section class="section">
    <h2>Principle</h2>
    <p>
      El territorio no es un conjunto de puntos en un mapa ni una colección de “usuarios”.
      Es un sistema vivo que merece la misma ingeniería que un datacenter crítico.
    </p>
  </section>

  <section class="section">
    <h2>Capabilities</h2>
    <div class="columns">
      <div class="card">
        <h4>Geospatial Modeling</h4>
        <p>Integración de DEMs, GSHHG y vectores propios para representar el territorio con precisión científica.</p>
      </div>
      <div class="card">
        <h4>Telemetry</h4>
        <p>Bus de eventos en tiempo real para flujos de personas, comercio, movilidad y riesgo.</p>
      </div>
      <div class="card">
        <h4>Simulation</h4>
        <p>Escenarios dinámicos de rutas, congestión, resiliencia y operación en modo isla.</p>
      </div>
      <div class="card">
        <h4>Local Economy</h4>
        <p>Comercio y servicios locales integrados como nodos económicos trazables, no como anexos.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <h2>Bootstrap</h2>
    <p>Inicialización mínima del entorno para pruebas y exploración.</p>
    <pre><code># Clonar el kernel territorial
git clone https://github.com/tu-org/rdm-tos.git
cd rdm-tos

# Levantar servicios base (ejemplo)
docker-compose up</code></pre>
  </section>

  <footer class="footer">
    <span>RDM‑TOS · Sovereign Territorial Operating System</span>
    <span>Arquitecto: Anubis Villaseñor · Real del Monte, México</span>
    <span>Soberanía no es discurso. Es ejecución.</span>
  </footer>
</main>

</body>
</html>
```

---

## 🎨 SVG HERO ( `assets/hero.svg` )

```svg
<svg viewBox="0 0 800 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="bg" cx="50%" cy="0%" r="100%">
      <stop offset="0%" stop-color="#050811"/>
      <stop offset="45%" stop-color="#020309"/>
      <stop offset="100%" stop-color="#000000"/>
    </radialGradient>
  </defs>
  <rect width="800" height="400" fill="url(#bg)"/>
  <rect x="80" y="80" width="640" height="240" fill="none" stroke="#111111" stroke-width="1.2"/>
  <text x="50%" y="48%" fill="#00F7FF" font-size="46" text-anchor="middle" font-family="Fira Code, monospace" letter-spacing="0.25em">
    RDM-TOS
  </text>
  <text x="50%" y="62%" fill="#FF1717" font-size="18" text-anchor="middle" font-family="Fira Code, monospace" letter-spacing="0.18em">
    SOVEREIGN TERRITORIAL OPERATING SYSTEM
  </text>
</svg>
```

---

## 🧠 SVG GRID ( `assets/grid.svg` )

```svg
<svg viewBox="0 0 800 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="gridbg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#020308"/>
      <stop offset="100%" stop-color="#000000"/>
    </linearGradient>
  </defs>
  <rect width="800" height="400" fill="url(#gridbg)"/>
  <g stroke="#111111" stroke-width="0.6">
    <!-- vertical grid -->
    <line x1="100" y1="40" x2="100" y2="360"/>
    <line x1="200" y1="40" x2="200" y2="360"/>
    <line x1="300" y1="40" x2="300" y2="360"/>
    <line x1="400" y1="40" x2="400" y2="360"/>
    <line x1="500" y1="40" x2="500" y2="360"/>
    <line x1="600" y1="40" x2="600" y2="360"/>
    <line x1="700" y1="40" x2="700" y2="360"/>
    <!-- horizontal grid -->
    <line x1="80" y1="80" x2="720" y2="80"/>
    <line x1="80" y1="140" x2="720" y2="140"/>
    <line x1="80" y1="200" x2="720" y2="200"/>
    <line x1="80" y1="260" x2="720" y2="260"/>
    <line x1="80" y1="320" x2="720" y2="320"/>
  </g>
  <circle cx="400" cy="200" r="46" stroke="#FF1717" stroke-width="2" fill="none"/>
  <circle cx="400" cy="200" r="4" fill="#00F7FF"/>

  <text x="400" y="195" fill="#00F7FF" font-size="11" text-anchor="middle" font-family="Fira Code, monospace">
    KERNEL MD-X4
  </text>
  <text x="400" y="212" fill="#777777" font-size="9" text-anchor="middle" font-family="Fira Code, monospace">
    HEPTAFEDERATED CORE
  </text>
</svg>
```

---

## ⚡ SVG PULSE ( `assets/pulse.svg` )

```svg
<svg viewBox="0 0 300 100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="pulseGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F7FF"/>
      <stop offset="100%" stop-color="#FF1717"/>
    </linearGradient>
  </defs>
  <rect width="300" height="100" fill="none"/>
  <polyline
    points="0,50 40,50 60,20 80,80 100,45 130,45 150,15 170,85 190,50 220,50 240,30 260,70 280,50 300,50"
    fill="none"
    stroke="url(#pulseGradient)"
    stroke-width="3"
    stroke-linejoin="round"
    stroke-linecap="round">
    <animate attributeName="stroke-dasharray"
      values="0,400;400,0"
      dur="2.2s"
      repeatCount="indefinite"/>
  </polyline>
</svg>
```

---

## 🧿 PORTADA PRINCIPAL ( `branding/cover.svg` )

```svg
<svg viewBox="0 0 1200 600" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="coverBg" cx="50%" cy="0%" r="100%">
      <stop offset="0%" stop-color="#050811"/>
      <stop offset="40%" stop-color="#020309"/>
      <stop offset="100%" stop-color="#000000"/>
    </radialGradient>
  </defs>
  <rect width="1200" height="600" fill="url(#coverBg)"/>

  <rect x="160" y="140" width="880" height="320"
        fill="none" stroke="#111111" stroke-width="1.4"/>

  <text x="50%" y="45%" fill="#00F7FF" font-size="60"
        text-anchor="middle" font-family="Fira Code, monospace"
        letter-spacing="0.32em">
    RDM-TOS
  </text>

  <text x="50%" y="58%" fill="#FF1717" font-size="22"
        text-anchor="middle" font-family="Fira Code, monospace"
        letter-spacing="0.28em">
    SOVEREIGN TERRITORIAL OPERATING SYSTEM
  </text>

  <text x="50%" y="72%" fill="#777777" font-size="16"
        text-anchor="middle" font-family="Fira Code, monospace"
        letter-spacing="0.22em">
    NODE ZERO · REAL DEL MONTE · MEXICO
  </text>
</svg>
```

---

