# TAMV ONLINE ENTERPRISE
> **Infraestructura Civilizatoria, Soberanía Digital e Inteligencia Territorial**

[![Ecosistema: TAMV](https://img.shields.io/badge/Ecosistema-TAMV_Online_Enterprise-000000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/TAMV-ONLINE)
[![Kernel: MD-X4](https://img.shields.io/badge/Kernel-MD--X4_Federated-00f0ff?style=for-the-badge)](docs/ARCHITECTURE.md)
[![Cognitive: Isabella AI](https://img.shields.io/badge/AI-Isabella_Genesis_Governance-7000ff?style=for-the-badge)](docs/ISABELLA.md)
[![Audit: BookPI](https://img.shields.io/badge/Memory-MSR_%2F_BookPI_Traceable-00ff66?style=for-the-badge)](docs/BOOKPI.md)

---

## Manifiesto Técnico

> **No construyo una marca. Construyo una infraestructura civilizatoria.**

Nacido en **Mineral del Monte (Real del Monte), Hidalgo, México**, TAMV ONLINE ENTERPRISE es un sistema vivo de soberanía digital, memoria territorial, inteligencia aplicada y coordinación comunitaria. 

Si la tecnología no fortalece a la comunidad, solo está decorando dependencia. TAMV opera bajo la convicción de que los datos sin soberanía constituyen extractivismo, la inteligencia sin territorio es ruido automatizado, y los sistemas incapaces de sobrevivir a sus propias fallas nunca fueron realmente sistemas.

```MERMAID

    [ TERRITORIO & COMUNIDAD ]
               │
               ▼
   [ CAPA COGNITIVA: ISABELLA AI ]
               │
               ▼
   [ KERNEL DE SOBERANÍA: MD-X4 ]
               │
               ▼
   [ SISTEMA OPERATIVO: RDM-TOS ]
               │
               ▼
   [ MEMORIA Y AUDITORÍA: MSR / BOOKPI ]

```

---

## Módulos del Ecosistema

| Componente | Capa | Función Arquitectónica | Estado |
| :--- | :--- | :--- | :--- |
| **MD-X4** | *Kernel / Federación* | Coordinación de nodos, políticas de soberanía, orquestación y contratos runtime. | `Active` |
| **RDM-TOS** | *OS Territorial* | Gestión de datos contextuales, expedientes comunitarios, eventos y memoria operacional. | `Active` |
| **Isabella AI** | *Inteligencia / Agentes* | Sistema federado de IA gobernada, verificación, procedencia y resolución de incertidumbre. | `Genesis` |
| **MSR / BookPI** | *Memoria & Auditoría* | Grafo de trazabilidad inmutable: Decisión ↔ Código ↔ Evidencia ↔ Despliegue. | `Active` |
| **TAMV Network** | *Interfaz & Colaboración* | Superficie pública, identidad XR/multimedia, radio comunitaria y nodo de integración. | `Active` |

---

## Principios Operativos Exigibles

1. **Soberanía sobre dependencia:** Ninguna dependencia crítica carecerá de estrategia de reemplazo o plan de degradación sin pérdida de datos.
2. **Defensa por capas:** Todo módulo implementa prevención, detección, contención (circuit breakers), corrección idempotente y aprendizaje automático.
3. **Auditabilidad BookPI:** Todo cambio arquitectónico o de modelo debe registrarse en la cadena causal de decisiones con metadatos verificables.
4. **Criterio Humano:** La automatización expande la capacidad de acción comunitaria; nunca oculta la responsabilidad técnica o ética.

---

## Estructura de Documentación

Para profundizar en la arquitectura, reglas de gobernanza y guías de contribución:

* 🗺️ [**Arquitectura de Sistema (`docs/ARCHITECTURE.md`)**](docs/ARCHITECTURE.md)
* 🏛️ [**Modelo de Gobernanza (`docs/GOVERNANCE.md`)**](docs/GOVERNANCE.md)
* 🤝 [**Guía de Contribución (`docs/CONTRIBUTING.md`)**](docs/CONTRIBUTING.md)
* 🔒 [**Políticas de Seguridad y Soberanía (`docs/SECURITY.md`)**](docs/SECURITY.md)
* 📜 [**Libro de Decisiones BookPI (`docs/BOOKPI.md`)**](docs/BOOKPI.md)

---

**Fundador & Arquitecto:** Edwin Oswaldo Castillo Trejo (*Anubis Villaseñor*)  
**Origen:** Real del Monte, Hidalgo, México 🇲🇽  
**Ámbito:** Latinoamérica hacia el mundo.
Dashboard Interactivo de Arquitectura Ecosistémica TAMVNormas y Código de Gobernanza (docs/GOVERNANCE.md)Markdown# Código de Gobernanza y Gestión de Cambios (TAMV-GOV-01)

## 1. Niveles de Cambios y Versionado
Todo cambio dentro de los repositorios del ecosistema TAMV ONLINE ENTERPRISE se clasifica bajo la especificación SemVer modificada para infraestructuras soberanas:

* **PATCH (x.x.N):** Correcciones internas de código, parches de seguridad sin alteración de esquemas o contratos API.
* **MINOR (x.N.0):** Adición de nuevas capacidades, endpoints o agentes de Isabella AI que mantienen compatibilidad hacia atrás.
* **MAJOR (N.0.0):** Cambios incompatibles en contratos API, reestructuración del Kernel MD-X4, modificaciones en esquemas de datos RDM-TOS o cambios en el protocolo de consenso. Requieren registro BookPI obligatorio.
* **EMERGENCY (HOTFIX):** Despliegue de urgencia por vulnerabilidad de seguridad activa. Exige auditoría post-mortem en menos de 72 horas.

## 2. Reglas de Merge y Aprobación
1. **Verificación Estricta:** Ningún Pull Request será integrado sin superar el pipeline CI/CD (linting, tests unitarios, tests de contrato e inspección de secretos).
2. **Registro BookPI:** Cambios clasificados como MINOR o MAJOR requieren un archivo de decisión en `docs/decisions/` siguiendo el estándar `BPI-YYYY-XXXX`.
3. **Prohibición de Parches Ciegos:** Se rechaza cualquier PR que resuelva un síntoma sin documentar el disparador y la causa raíz en el vector de fallas.

## 3. Gobernanza Algorítmica y Control de IA
1. **Transparencia Cognitiva:** Isabella AI no responderá ni ejecutará herramientas sin registrar la trazabilidad de su contexto y grado de incertidumbre.
2. **Human-in-the-Loop:** Toda acción con impacto económico, borrado de datos o reconfiguración de infraestructura territorial requerirá autorización explícita firmada por un operador humano calificado.
3. **Aislamiento de Prompts:** Separación estricta entre las directivas del sistema y las entradas no confiables del usuario para evitar ataques de inyección.
Manifiesto Técnico de GitHub (docs/TAMV-ONLINE-ENTERPRISE.md)Markdown# MANIFIESTO Y MANUAL DE ARQUITECTURA TÉCNICA
## TAMV ONLINE ENTERPRISE: INFRAESTRUCTURA CIVILIZATORIA SOBERANA

### Preámbulo
TAMV ONLINE ENTERPRISE no es una startup, ni una vitrina tecnológica, ni una marca comercial. Es una infraestructura civilizatoria desarrollada desde Real del Monte, Hidalgo, diseñada para dotar a las comunidades de Latinoamérica de capacidad cibernética autónoma, memoria histórica inalterable e inteligencia territorial gobernada.

---

### Tesis Fundamental
> **Si la tecnología no fortalece a la comunidad, solo está decorando dependencia.**

Frente a la centralización tecnológica extractiva, TAMV contrapone:
1. **Soberanía de Datos:** Los datos pertenecen al territorio que los genera.
2. **Defensa Sistémica:** Diseñar asumiendo la falla continua como estado natural; la resiliencia es el único indicador real de madurez.
3. **Memoria Operacional:** Toda acción técnica o algorítmica debe ser auditable en tiempo y origen mediante BookPI.

---

### Análisis Causal de Fallas (Matriz de Defensa)

TAMV rechaza la ingeniería basada en parches superficiales. Todo error en el ecosistema debe analizarse bajo el vector lineal de propagación:

$$\text{Condición Previa} \rightarrow \text{Disparador} \rightarrow \text{Vulnerabilidad} \rightarrow \text{Error Observable} \rightarrow \text{Impacto} \rightarrow \text{Detección} \rightarrow \text{Corrección} \rightarrow \text{Aprendizaje}$$

#### Capas de Resiliencia Exigidas:
* **Prevención:** Tipado estricto, contratos inmutables, validación de esquemas en frontera.
* **Detección:** Health checks sintéticos, monitoreo de métricas doradas (latencia, tráfico, errores, saturación).
* **Contención:** Isolation boundary, degradación elegante de interfaz, circuit breakers activos.
* **Corrección:** Rollback automatizado, retries con backoff exponencial e idempotencia estricta.

---

### Protocolo de Contribución
Para contribuir a TAMV ONLINE ENTERPRISE, el desarrollador debe aportar **criterio técnico y compromiso territorial**, no solo líneas de código.

1. **Comprensión del Sistema:** Identificar los contratos consumidos y producidos por el módulo a modificar.
2. **Aislamiento:** Trabajar en ramas temáticas (`feature/`, `fix/`, `audit/`).
3. **Verificación de Invariantes:** Garantizar que los tests de no regresión se ejecuten localmente.
4. **Firma de Compromiso:** Documentar el riesgo aceptado y el procedimiento de reversión (*rollback*) en la descripción del Pull Request.

---
*Diseñado, codificado y sostenido desde Real del Monte, Hidalgo, México.*
