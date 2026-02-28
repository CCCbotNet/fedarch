# PRJ-017: Observability — Phoenix Deployment

## 📋 PRJ-017_Observability-Phoenix_v3.1.4.1.md
## ♾️ WeOwnNet 🌐

| Field | Value |
|-------|-------|
| Document | PRJ-017_Observability-Phoenix.md |
| Version | 3.1.4.1 |
| CCC-ID | GTM_2026-W09_121 |
| Created | 2026-02-27 (W09) |
| Season | #WeOwnSeason003 🚀 |
| Status | 📝 DRAFT |
| Lifecycle Stage | 📝 DRAFT (#DocLifecycle) |
| Tags | #Observability #Phoenix #OTEL #FOSS #FlowsBros |

---

## 📖 Table of Contents

1. [Project Identity](#-project-identity)
2. [Why Phoenix](#-why-phoenix)
3. [What Gets Traced](#-what-gets-traced)
4. [Architecture](#-architecture)
5. [Deployment Checklist](#-deployment-checklist)
6. [Docker Compose](#-docker-compose)
7. [OTEL Instrumentation Plan](#-otel-instrumentation-plan)
8. [Dashboard Configuration](#-dashboard-configuration)
9. [Integration with PRJ-016 (LiteLLM)](#-integration-with-prj-016-litellm)
10. [Verification (#SmokeTest)](#-verification-smoketest)
11. [Project Team](#-project-team)
12. [@MAIT:#Observability Setup](#-maitobservability-setup)
13. [Risk Matrix](#-risk-matrix)
14. [Relationship to Other Projects](#-relationship-to-other-projects)
15. [Discovered By](#-discovered-by)
16. [Related Documents](#-related-documents)
17. [Version History](#-version-history)

---

## 📋 Project Identity

| Field | Value |
|-------|-------|
| Project ID | **PRJ-017** |
| Title | **Observability — Phoenix Deployment** |
| Type | Infrastructure — Observability |
| Priority | 🟠 P1 |
| Owner | @GTM + @RMN |
| Deployment | GB10-1 #NoDe (Northglenn, CO) |
| Timeline | **W11-W12** |
| Depends on | PRJ-015 (GB10 hardware) |
| Feeds into | PRJ-016 (LiteLLM OTEL → Phoenix) |
| #masterCCC | GTM_2026-W09_121 |

---

## 📋 Why Phoenix

| Field | Value |
|-------|-------|
| Product | [Arize Phoenix](https://github.com/Arize-ai/phoenix) |
| License | **BSD-3-Clause** ✅ (FOSS — permissive) |
| Stars | 10K+ |
| Score | **33/35** (GTM_2026-W09_114) |
| Setup | `pip install arize-phoenix` + `phoenix serve` = **2 minutes** |
| Footprint | **~500 MB RAM** |
| Storage | SQLite (default) or PostgreSQL |
| UI | Self-hosted web dashboard |
| OTEL | ✅ Native OpenTelemetry support |

### What We Have Now vs With Phoenix

| Metric | Now | With Phoenix |
|--------|-----|-------------|
| LLM call visibility | ❌ None | ✅ Every call traced |
| Token cost tracking | ❌ Manual top-up counting | ✅ Per-request cost |
| Latency monitoring | ❌ None | ✅ Per-request latency |
| RAG quality | ❌ Blind | ✅ Retrieval relevance scores |
| Agent flows | ❌ Invisible | ✅ #ContextVolley visualization |
| Embedding performance | ❌ Unknown | ✅ Embedding latency + quality |
| Cache effectiveness | ❌ N/A (no cache yet) | ✅ Hit/miss tracking (PRJ-016) |
| Error debugging | ❌ Log diving | ✅ Trace waterfall |

---

## 📋 What Gets Traced

| Trace Type | Source | #FedArch Value |
|-----------|--------|---------------|
| **LLM calls** | AnythingLLM → LLM provider | Token usage, cost, latency per request |
| **Embedding ops** | AnythingLLM → Qwen3 4B | Embedding latency, batch sizes |
| **RAG retrieval** | AnythingLLM vector search | Retrieval relevance, doc chunks returned |
| **Tool calls** | MAIT thread interactions | MAIT response quality |
| **Agent spans** | Parent → child request chains | #ContextVolley flow visualization |
| **Cache events** | LiteLLM Redis (PRJ-016) | Hit/miss rate, savings |
| **Failover events** | LiteLLM provider switching | OpenRouter → Ollama transitions |
| **Errors** | Any failure in pipeline | Root cause analysis |

---

## 📋 Architecture

### Phoenix on GB10-1 #NoDe

```
┌─────────────────────────────────────────────────────────┐
│  GB10-1: #NoDe (Northglenn, CO)                          │
│                                                          │
│  ┌──────────────────────────────────────────────────┐   │
│  │  Phoenix (Port: 6006)                             │   │
│  │  ┌──────────────┐  ┌──────────────────────────┐  │   │
│  │  │  OTEL Collector│  │  Web Dashboard           │  │   │
│  │  │  (traces in)  │  │  (visualization out)     │  │   │
│  │  └──────┬───────┘  └──────────────────────────┘  │   │
│  │         │                                         │   │
│  │  ┌──────┴───────┐                                │   │
│  │  │  SQLite DB    │                                │   │
│  │  │  (trace store)│                                │   │
│  │  └──────────────┘                                │   │
│  └──────────────────────────────────────────────────┘   │
│         ▲         ▲         ▲                            │
│         │         │         │                            │
│  ┌──────┴──┐ ┌───┴────┐ ┌──┴──────┐                   │
│  │ Ollama  │ │LiteLLM │ │ ALLM    │                   │
│  │ (local) │ │(gateway)│ │ (local) │                   │
│  └─────────┘ └────────┘ └─────────┘                   │
│                    ▲                                     │
│                    │ OTEL traces                         │
│         ┌──────────┴──────────┐                         │
│         │ Cloud AnythingLLM    │                         │
│         │ INT-P01, INT-S003,   │                         │
│         │ INT-OG1, INT-P02     │                         │
│         └─────────────────────┘                         │
└─────────────────────────────────────────────────────────┘
```

### Data Flow

```
1. AnythingLLM makes LLM call
2. OTEL SDK captures: model, tokens, latency, cost
3. OTEL exports trace to Phoenix (http://gb10-1:6006/v1/traces)
4. Phoenix stores in SQLite
5. Phoenix dashboard visualizes
6. @GTM / @RMN view dashboard
```

---

## 📋 Deployment Checklist

| # | Step | Owner | Depends On | Status |
|---|------|-------|-----------|--------|
| 1 | GB10-1 #NoDe operational | @GTM | PRJ-015 | ⬜ |
| 2 | Docker installed | @GTM | Step 1 | ⬜ |
| 3 | Create `phoenix/` directory | @GTM | Step 2 | ⬜ |
| 4 | Create `docker-compose.yml` | @GTM | Step 3 | ⬜ |
| 5 | `docker compose up -d` | @GTM | Step 4 | ⬜ |
| 6 | Verify Phoenix UI (http://gb10-1:6006) | @GTM | Step 5 | ⬜ |
| 7 | Install OTEL SDK on AnythingLLM (local) | @RMN | Step 6 | ⬜ |
| 8 | Send test trace | @GTM | Step 7 | ⬜ |
| 9 | Verify trace appears in Phoenix UI | @GTM | Step 8 | ⬜ |
| 10 | Instrument Ollama calls | @RMN | Step 7 | ⬜ |
| 11 | Configure LiteLLM → Phoenix (PRJ-016) | @RMN | PRJ-016 | ⬜ |
| 12 | Create @MAIT:#Observability | @GTM | Step 9 | ⬜ |
| 13 | FULL:SYNC:META | @GTM | Step 12 | ⬜ |

> **13 steps. Lightweight.** Phoenix = `pip install + serve` or Docker. No complex config.

---

## 📋 Docker Compose

```yaml
# docker-compose.yml — Phoenix on GB10-1 #NoDe
version: '3.8'

services:
  phoenix:
    image: arizephoenix/phoenix:latest
    container_name: phoenix
    restart: unless-stopped
    ports:
      - "6006:6006"
    volumes:
      - phoenix_data:/data
    environment:
      - PHOENIX_PORT=6006
      - PHOENIX_STORAGE_DIR=/data

volumes:
  phoenix_data:
```

### Alternative: pip install (even simpler)

```bash
# On GB10-1 directly (no Docker needed)
pip install arize-phoenix
phoenix serve --port 6006
```

> **Docker = recommended** (consistent with GB10-1 stack). pip = fastest for testing.

---

## 📋 OTEL Instrumentation Plan

### Phase 1: Local Services (W11)

| Service | Instrumentation | Method |
|---------|----------------|--------|
| **AnythingLLM (local)** | LLM calls + RAG retrieval | OTEL Python SDK or phoenix.otel |
| **Ollama** | Inference calls | OTEL wrapper |

### Phase 2: LiteLLM Integration (W12 — PRJ-016)

| Service | Instrumentation | Method |
|---------|----------------|--------|
| **LiteLLM** | All proxied calls | Built-in OTEL export (config.yaml) |

### Phase 3: Cloud Instances (W13+)

| Service | Instrumentation | Method |
|---------|----------------|--------|
| **INT-P01, INT-S003, etc.** | LLM calls via LiteLLM | Automatic (LiteLLM traces all) |

### OTEL Configuration

```python
# For direct AnythingLLM instrumentation
from phoenix.otel import register
from openinference.instrumentation.openai import OpenAIInstrumentor

tracer_provider = register(
    endpoint="http://localhost:6006/v1/traces",
    project_name="fedarch"
)

OpenAIInstrumentor().instrument(tracer_provider=tracer_provider)
```

### For LiteLLM (PRJ-016 — automatic)

```yaml
# In LiteLLM config.yaml
litellm_settings:
  callbacks: ["otel"]

environment_variables:
  OTEL_EXPORTER: "otlp_http"
  OTEL_ENDPOINT: "http://phoenix:6006/v1/traces"
```

> **When PRJ-016 deploys, ALL LLM traffic automatically traces to Phoenix.** Zero additional instrumentation needed per instance.

---

## 📋 Dashboard Configuration

### Default Views

| Dashboard | Metrics | Purpose |
|-----------|---------|---------|
| **Traces** | Request waterfall, spans, latency | Debug individual requests |
| **LLM Calls** | Model, tokens in/out, cost, latency | Usage patterns |
| **Embeddings** | Embedding latency, batch sizes | Performance monitoring |
| **RAG** | Retrieval relevance, chunks returned | RAG quality |

### Custom Views for #FedArch

| View | Metrics | Purpose |
|------|---------|---------|
| **Cost by Instance** | Tokens × cost per instance | Budget tracking |
| **Model Distribution** | % Claude vs % Llama vs % Qwen3 | #HybridArchitecture balance |
| **Cache Effectiveness** | Hit/miss rate (via LiteLLM) | Savings validation |
| **Failover Events** | OpenRouter → Ollama transitions | Reliability monitoring |
| **Error Rate** | Errors by provider, model, instance | Health monitoring |

---

## 📋 Integration with PRJ-016 (LiteLLM)

### Why Phoenix Deploys BEFORE LiteLLM

```
W11: Deploy Phoenix (PRJ-017)
  └── Phoenix running on port 6006
  └── OTEL endpoint ready

W12: Deploy LiteLLM (PRJ-016)
  └── LiteLLM config: OTEL_ENDPOINT=http://phoenix:6006/v1/traces
  └── ALL LLM traffic automatically traced
  └── Cost, latency, cache, failover = visible immediately
```

> **Phoenix = infrastructure for LiteLLM.** Deploy the observer before the thing being observed.

### Shared Docker Network

```yaml
# Both PRJ-016 and PRJ-017 on same Docker network
networks:
  fedarch-edge:
    driver: bridge

# Phoenix joins:
services:
  phoenix:
    networks:
      - fedarch-edge

# LiteLLM joins:
services:
  litellm:
    networks:
      - fedarch-edge
    environment:
      - OTEL_ENDPOINT=http://phoenix:6006/v1/traces
```

---

## 📋 Verification (#SmokeTest)

### Phoenix #SmokeTest (6-Point)

| # | Test | Expected | Status |
|---|------|----------|--------|
| 1 | Phoenix running | `curl http://localhost:6006` → dashboard loads | ⬜ |
| 2 | OTEL endpoint | `curl http://localhost:6006/v1/traces` → accepts POST | ⬜ |
| 3 | Send test trace | Python OTEL SDK → Phoenix | ⬜ |
| 4 | Trace visible in UI | Dashboard shows test trace | ⬜ |
| 5 | Ollama trace | Local LLM call → trace in Phoenix | ⬜ |
| 6 | Persistence | Restart Phoenix → traces still present | ⬜ |

---

## 📋 Project Team

| CCC | Role | Focus |
|-----|------|-------|
| **GTM** | **Owner** | Deployment, dashboard config, @MAIT |
| **RMN** | **Platform** | OTEL instrumentation, LiteLLM integration |

> **2-person project.** Phoenix is lightweight — deploy + instrument + done.

---

## 📋 @MAIT:#Observability Setup

| Field | Value |
|-------|-------|
| Thread | MAIT_Observability |
| ShortCode | @MAIT:#Observability |
| Steward | @GTM |
| Instance | INT-P01 |
| Protocol | #ContextVolley |
| Tool Agent | t-observability_tool |
| Scope | Phoenix (primary) + OpenTelemetry + MLflow (reference) |

### RAG Documents

| # | Source | Depth |
|---|--------|-------|
| 1 | docs.arize.com/phoenix | 2 |
| 2 | opentelemetry.io/docs | 1 (Python SDK only) |

---

## 📋 Risk Matrix

| # | Risk | Prob | Impact | Mitigation |
|---|------|------|--------|------------|
| 1 | GB10-1 not ready (PRJ-015) | Medium | High | Deploy Phoenix on DO Droplet interim |
| 2 | OTEL instrumentation complexity | Low | Medium | Phoenix provides helper library (phoenix.otel) |
| 3 | Storage growth (traces) | Low | Low | SQLite + configurable retention; 2 TB NVMe |
| 4 | Phoenix project abandoned | Low | Low | BSD-3 = fork; 10K stars; Arize-backed |
| 5 | Network: cloud → GB10-1 (traces) | Medium | Low | Traces = async, non-blocking; latency irrelevant |
| 6 | Dashboard access (remote) | Low | Low | Tailscale/WireGuard or port forward |

---

## 📋 Relationship to Other Projects

| PRJ | Relationship |
|-----|-------------|
| **PRJ-015** | Phoenix deploys ON GB10-1 #NoDe (hardware dependency) |
| **PRJ-016** | LiteLLM sends OTEL traces TO Phoenix (Phoenix = endpoint) |
| **PRJ-013** | Paperless-ngx co-located on GB10-1 (shared Docker host) |
| **PRJ-014** | INT-P01 + INT-S003 traffic traced through LiteLLM → Phoenix |

### Infrastructure Quad — Execution Order

```
PRJ-014: SEPARATE  (INT-S003 + WeOwn.tools)     W10      ✅ GH LIVE
PRJ-015: COMPUTE   (2× GB10)                    W10-W11  🚀 GH LIVE
PRJ-017: OBSERVE   (Phoenix)                    W11-W12  📝 THIS
PRJ-016: ROUTE     (LiteLLM)                    W12-W13  🚀 GH LIVE

"Separate. Compute. Observe. Route."
```

---

## 📋 Discovered By (BP-047)

| CCC | Contributor | Role | Context |
|-----|-------------|------|---------|
| GTM | [yonks](https://GitHub.com/YonksTEAM) | Co-Founder / Chief Digital Alchemist | ADK Observability Ecosystem analysis — Phoenix selected 33/35 — W09 |

---

## 📋 Related Documents

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| PRJ-015_HybridArchitecture-GB10 | v3.1.4.3 | GTM_2026-W09_104 | ⬜ @THY | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-015_HybridArchitecture-GB10.md) |
| PRJ-016_AIGateway-LiteLLM | v3.1.4.1 | GTM_2026-W09_117 | ⬜ AWAITING | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-016_AIGateway-LiteLLM.md) |
| SharedKernel | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/SharedKernel.md) |
| Phoenix Docs | — | — | — | [docs.arize.com/phoenix](https://docs.arize.com/phoenix) |
| Phoenix GitHub | — | — | — | [github.com/Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| 3.1.4.1 | 2026-W09 | GTM_2026-W09_121 | GTM_2026-W09_122 | Initial project; Phoenix observability on GB10-1 #NoDe; BSD-3 FOSS; ~500 MB RAM; OTEL instrumentation (3 phases); LiteLLM integration (PRJ-016 endpoint); 6 dashboard views; 13-step deployment; Docker Compose; 6-point #SmokeTest; @MAIT:#Observability; 6-risk matrix; deploys BEFORE LiteLLM (infrastructure dependency) |

---

#FlowsBros #FedArch #Observability #Phoenix #OTEL #FOSS #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
