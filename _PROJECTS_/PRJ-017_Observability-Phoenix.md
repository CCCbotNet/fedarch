# PRJ-017: Observability — Phoenix Deployment

## 📋 PRJ-017_Observability-Phoenix_v3.1.4.2.md
## ♾️ WeOwnNet 🌐 | jAIMSnet

| Field | Value |
|-------|-------|
| Document | PRJ-017_Observability-Phoenix.md |
| Version | 3.1.4.2 |
| CCC-ID | GTM_2026-W09_121 |
| Created | 2026-02-27 (W09) |
| Season | #WeOwnSeason003 🚀 |
| Status | ✅ APPROVED |
| Lifecycle Stage | ✅ APPROVED (#DocLifecycle) |
| Tags | #Observability #Phoenix #OTEL #jAIMSnet #FOSS #FlowsBros |
| Brand | **jAIMSnet** (AI Management Systems network) |
| Urgency | 🔴 **HIGH — 3 blind incidents W09, $5,249 no visibility** |

---

## 📖 Table of Contents

1. [Project Identity](#-project-identity)
2. [jAIMSnet Brand Identity](#-jaimsnet-brand-identity)
3. [Why Phoenix](#-why-phoenix)
4. [What Gets Traced](#-what-gets-traced)
5. [Phase 0 — DO Infrastructure Observability](#-phase-0--do-infrastructure-observability)
6. [Phase 0 — Deployment Checklist](#-phase-0--deployment-checklist)
7. [Phase 0 — Docker Compose](#-phase-0--docker-compose)
8. [Phase 0 — Verification (#SmokeTest)](#-phase-0--verification-smoketest)
9. [Architecture](#-architecture)
10. [Phase 1 — Local Services (GB10-1)](#-phase-1--local-services-gb10-1)
11. [Phase 2 — LiteLLM Integration](#-phase-2--litellm-integration)
12. [Phase 3 — Full Stack](#-phase-3--full-stack)
13. [OTEL Instrumentation Plan](#-otel-instrumentation-plan)
14. [Dashboard Configuration](#-dashboard-configuration)
15. [Integration with PRJ-016 (LiteLLM)](#-integration-with-prj-016-litellm)
16. [Project Team](#-project-team)
17. [@MAIT:#Observability Setup](#-maitobservability-setup)
18. [Risk Matrix](#-risk-matrix)
19. [Relationship to Other Projects](#-relationship-to-other-projects)
20. [Discovered By](#-discovered-by)
21. [Related Documents](#-related-documents)
22. [Version History](#-version-history)

---

## 📋 Project Identity

| Field | Value |
|-------|-------|
| Project ID | **PRJ-017** |
| Title | **Observability — Phoenix Deployment** |
| Type | Infrastructure — Observability |
| Priority | 🔴 P0 (Phase 0) / 🟠 P1 (Phase 1-3) |
| Owner | @GTM + @RMN |
| Brand | **jAIMSnet** |
| Deployment | Phase 0: DO Droplet NYC1 / Phase 1+: GB10-1 #NoDe |
| Timeline | **Phase 0: W10** / Phase 1: W11 / Phase 2: W12 / Phase 3: W13+ |
| Depends on | Phase 0: None / Phase 1: PRJ-015 / Phase 2: PRJ-016 |
| Feeds into | PRJ-016 (LiteLLM OTEL → Phoenix) |
| #masterCCC | GTM_2026-W09_121 |

---

## 📋 jAIMSnet Brand Identity

### Brand

| Field | Value |
|-------|-------|
| Brand | **jAIMSnet** |
| Meaning | j + **AIMS** (AI Management Systems) + net (network) |
| ISO Reference | **ISO/IEC 42001:2023** — AI Management Systems |
| ISO URL | [iso.org/standard/42001](https://www.iso.org/standard/42001) |
| Positioning | Open-source AI observability & management infrastructure |
| Relationship | Ecosystem brand under YonksTEAM LLC |

### Digital Presence

| Asset | URL | Status |
|-------|-----|--------|
| **Primary Domain** | **[jAIMS.network](https://jAIMS.network)** | ✅ Registered |
| GitHub Org | [github.com/jAIMSnet](https://github.com/jAIMSnet) | ✅ Created |
| X (Twitter) | [x.com/jAIMSnet](https://x.com/jAIMSnet) | ✅ Created |

### All Domains (6 — Porkbun / Web3FreedomClub)

| # | Domain | Purpose |
|---|--------|---------|
| 1 | **jAIMS.network** | **Primary** — infrastructure brand |
| 2 | jAIMS.app | App/tool landing page |
| 3 | jAIMS.xyz | Alternative |
| 4 | jAIMSnet.com | Corporate redirect |
| 5 | jAIMSnet.org | Community/open-source |
| 6 | jAIMSnet.xyz | Alternative |

### ISO/IEC 42001 Alignment

| ISO 42001 Requirement | jAIMSnet Implementation |
|----------------------|------------------------|
| AI system monitoring | Phoenix traces + dashboards |
| Risk management | Observability → incident detection |
| Performance evaluation | Token cost, latency, error rates |
| Continual improvement | Data-driven optimization |
| Documentation | #FedArch governance (SharedKernel, BP, PROTO) |
| Accountability | CCC attribution system |

### Ecosystem Brand Map

| Brand | Audience | Focus |
|-------|----------|-------|
| ♾️ WeOwnNet 🌐 | Real estate cooperatives | Cooperative ownership |
| 🔥 BurnedOut Media 🔀 | Burned out professionals | Retreat + coaching |
| **jAIMSnet** 🆕 | AI practitioners + infrastructure | Observability + AI management |
| CCCbot.Net | CCC governance | Onchain cooperative |

### jAIMSnet × PRJ-017

| PRJ-017 Component | jAIMSnet Role |
|-------------------|---------------|
| Phoenix deployment | jAIMSnet infrastructure |
| OTEL instrumentation | jAIMSnet tooling |
| Dashboards | jAIMSnet monitoring platform |
| @MAIT:#Observability | jAIMSnet knowledge base |
| Phase 0 (DO observability) | **jAIMSnet first deployment** |

### jAIMSnet GH Org — Proposed Repos

| # | Repo | Purpose | Timeline |
|---|------|---------|----------|
| 1 | jAIMSnet/docs | Documentation + ISO 42001 mapping | W14+ |
| 2 | jAIMSnet/phoenix-config | Phoenix deployment configs | W14+ |
| 3 | jAIMSnet/otel-recipes | OTEL instrumentation recipes | W14+ |

> **W10-W13:** PRJ-017 docs stay in CCCbotNet/fedarch. **W14+:** jAIMSnet GH org gets its own repos.

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

## 📋 Phase 0 — DO Infrastructure Observability

### Why Phase 0

| Incident | When | Detected By | With Phoenix |
|----------|------|------------|-------------|
| API key lost (W08) | 2h 18m downtime | User report | ✅ 0 traces → alert in <60s |
| API key restart (W09) | ~18 min | @GTM manual | ✅ Trace failure → alert |
| API key lost (W09) | ~69 min | @LDC report | ✅ 0 traces → alert in <60s |
| $5,249 blind spend | 91 days | Manual counting | ✅ Per-instance cost dashboard |
| ATL1 capacity | Today | @SHD manual | ✅ Health check failure |

> **3 incidents detected by humans. All 3 would have been caught by Phoenix in <60 seconds.**

### Phase 0 Scope

| # | What to Observe | Source | Method |
|---|----------------|--------|--------|
| 1 | **LLM calls** (INT-P01, INT-P02) | AnythingLLM | OTEL SDK → Phoenix |
| 2 | **OpenRouter API health** | LLM provider | Trace success/failure |
| 3 | **Token cost per instance** | OTEL metadata | Phoenix dashboard |
| 4 | **Request latency** | OTEL spans | Phoenix dashboard |
| 5 | **Error rates** | OTEL traces | Phoenix alerting |
| 6 | **Endpoint uptime** | All domains | Uptime Kuma |
| 7 | **SSL certificate expiry** | All domains | Uptime Kuma |
| 8 | **PostgreSQL connectivity** | DO Managed DB | Uptime Kuma |

### Phase 0 Infrastructure

| Field | Value |
|-------|-------|
| Host | **DO Droplet — NYC1** |
| Plan | Basic — 2 vCPU / 2 GB / 50 GB |
| Cost | **$18/mo** |
| Domain | ⬜ TBD (jAIMS.network or IP-only initially) |
| Duration | Until GB10-1 arrives → migrate to #NoDe |
| Services | Phoenix (REQUIRED) + Uptime Kuma (REQUIRED) |

### Resource Utilization

| Service | RAM | Port |
|---------|-----|------|
| Phoenix | ~500 MB | 6006 |
| Uptime Kuma | ~50 MB | 3001 |
| **TOTAL** | **~550 MB / 2 GB (28%)** | |

### Observability Layers

| Layer | Tool | What It Sees |
|-------|------|-------------|
| **AI Layer** | Phoenix | LLM calls, tokens, cost, latency, RAG, traces |
| **Infrastructure Layer** | Uptime Kuma | Endpoint uptime, SSL, DNS, PostgreSQL, OpenRouter |

> **Together = complete observability.** Phoenix sees INSIDE the AI. Uptime Kuma sees the INFRASTRUCTURE.

### Migration Path

```
W10:  Phoenix + Uptime Kuma on DO Droplet (NYC1) — $18/mo
      └── Observes: INT-P01, INT-P02, PostgreSQL, WordPress

W11+: GB10-1 arrives (PRJ-015)
      └── Migrate Phoenix + Kuma to GB10-1 #NoDe ($0/mo)
      └── Destroy DO Droplet (save $18/mo)
      └── Continues observing cloud from edge
```

---

## 📋 Phase 0 — Deployment Checklist

| # | Step | Owner | Depends On | Status |
|---|------|-------|-----------|--------|
| 1 | Create DO Droplet (NYC1, 2 GB) | @GTM | None | ⬜ |
| 2 | Install Docker + Docker Compose | @GTM | Step 1 | ⬜ |
| 3 | Create `observability/` directory | @GTM | Step 2 | ⬜ |
| 4 | Create `docker-compose.yml` | @GTM | Step 3 | ⬜ |
| 5 | `docker compose up -d` | @GTM | Step 4 | ⬜ |
| 6 | Verify Phoenix UI (http://<IP>:6006) | @GTM | Step 5 | ⬜ |
| 7 | Instrument INT-P01 LLM calls (OTEL) | @GTM / @RMN | Step 6 | ⬜ |
| 8 | Instrument INT-P02 LLM calls (OTEL) | @GTM / @RMN | Step 7 | ⬜ |
| 9 | Send test trace from INT-P01 | @GTM | Step 7 | ⬜ |
| 10 | Verify trace in Phoenix dashboard | @GTM | Step 9 | ⬜ |
| 11 | Deploy Uptime Kuma | @GTM | Step 5 | ⬜ |
| 12 | Configure 7 endpoint monitors | @GTM | Step 11 | ⬜ |
| 13 | Phase 0 #SmokeTest (10-point) | @GTM | Step 10 + 12 | ⬜ |
| 14 | FULL:SYNC:META | @GTM | Step 13 | ⬜ |

> **14 steps. @GTM solo (steps 1-6, 9-14). @RMN for OTEL instrumentation (steps 7-8).**

---

## 📋 Phase 0 — Docker Compose

```yaml
# docker-compose.yml — jAIMSnet Observability (DO Droplet — NYC1)
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

  uptime-kuma:
    image: louislam/uptime-kuma:1
    container_name: uptime-kuma
    restart: unless-stopped
    ports:
      - "3001:3001"
    volumes:
      - uptime_data:/app/data

volumes:
  phoenix_data:
  uptime_data:
```

### Uptime Kuma Monitors

| # | Endpoint | Type | Interval |
|---|----------|------|----------|
| 1 | AI.WeOwn.Agency (INT-P01) | HTTPS | 60s |
| 2 | s003.ccc.bot (INT-S003) | HTTPS | 60s |
| 3 | Lite.BurnedOut.xyz (INT-P02) | HTTPS | 60s |
| 4 | BurnedOutAdvisor.com | HTTPS | 60s |
| 5 | OpenRouter API | HTTPS | 60s |
| 6 | DO Managed PostgreSQL | TCP:25060 | 300s |
| 7 | SSL certificates (all) | Certificate | Daily |

---

## 📋 Phase 0 — Verification (#SmokeTest)

### Phase 0 #SmokeTest (10-Point)

| # | Test | Expected | Status |
|---|------|----------|--------|
| 1 | Phoenix running | `curl http://<IP>:6006` → dashboard | ⬜ |
| 2 | OTEL endpoint | `curl http://<IP>:6006/v1/traces` → accepts POST | ⬜ |
| 3 | INT-P01 trace | LLM call from INT-P01 → trace in Phoenix | ⬜ |
| 4 | INT-P02 trace | LLM call from INT-P02 → trace in Phoenix | ⬜ |
| 5 | Cost visible | Token count + cost in Phoenix UI | ⬜ |
| 6 | Latency visible | Request latency in Phoenix UI | ⬜ |
| 7 | Uptime Kuma running | `http://<IP>:3001` → dashboard | ⬜ |
| 8 | Uptime Kuma monitors | 7 endpoints green | ⬜ |
| 9 | Persistence (Phoenix) | Restart → traces still present | ⬜ |
| 10 | Persistence (Kuma) | Restart → monitors still configured | ⬜ |

---

## 📋 Architecture

### Phase 0 Architecture (W10 — DO Droplet)

```
┌──────────────────────────────────────────────────────────┐
│  DigitalOcean — NYC1                                      │
│                                                           │
│  ┌────────────────────────────────────────────────────┐  │
│  │  jAIMSnet Observability Droplet ($18/mo)            │  │
│  │  ┌──────────────┐  ┌──────────────────────────┐   │  │
│  │  │  Phoenix      │  │  Uptime Kuma             │   │  │
│  │  │  Port: 6006   │  │  Port: 3001              │   │  │
│  │  └──────┬───────┘  └──────────┬───────────────┘   │  │
│  │         │ OTEL traces          │ Health checks     │  │
│  └─────────┼──────────────────────┼───────────────────┘  │
│            │                      │                       │
│  ┌─────────┴──────────────────────┴───────────────────┐  │
│  │  DigitalOcean — ATL1 (Production)                   │  │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────────────┐   │  │
│  │  │ INT-P01  │ │ INT-P02  │ │ DO PostgreSQL    │   │  │
│  │  │ OTEL SDK │ │ OTEL SDK │ │ (health check)   │   │  │
│  │  └──────────┘ └──────────┘ └──────────────────┘   │  │
│  └────────────────────────────────────────────────────┘  │
│                                                           │
│  ┌────────────────────────────────────────────────────┐  │
│  │  DigitalOcean — NYC1 (New)                          │  │
│  │  ┌──────────────────┐                              │  │
│  │  │ BurnedOutAdvisor │                              │  │
│  │  │ WordPress        │                              │  │
│  │  └──────────────────┘                              │  │
│  └────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────┘
```

### Full Architecture (W13+ — After GB10)

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
3. OTEL exports trace to Phoenix (http://<phoenix>:6006/v1/traces)
4. Phoenix stores in SQLite
5. Phoenix dashboard visualizes
6. @GTM / @RMN view dashboard
```

---

## 📋 Phase 1 — Local Services (GB10-1)

### Timeline: W11 (After PRJ-015)

| Service | Instrumentation | Method |
|---------|----------------|--------|
| **AnythingLLM (local)** | LLM calls + RAG retrieval | OTEL Python SDK or phoenix.otel |
| **Ollama** | Inference calls | OTEL wrapper |

### Deployment Checklist (Phase 1)

| # | Step | Owner | Depends On | Status |
|---|------|-------|-----------|--------|
| 1 | GB10-1 #NoDe operational | @GTM | PRJ-015 | ⬜ |
| 2 | Migrate Phoenix from DO Droplet to GB10-1 | @GTM | Step 1 | ⬜ |
| 3 | Migrate Uptime Kuma from DO Droplet to GB10-1 | @GTM | Step 1 | ⬜ |
| 4 | Destroy DO Droplet | @GTM | Step 2 + 3 | ⬜ |
| 5 | Install OTEL SDK on AnythingLLM (local) | @RMN | Step 2 | ⬜ |
| 6 | Send test trace | @GTM | Step 5 | ⬜ |
| 7 | Verify trace appears in Phoenix UI | @GTM | Step 6 | ⬜ |
| 8 | Instrument Ollama calls | @RMN | Step 5 | ⬜ |

---

## 📋 Phase 2 — LiteLLM Integration

### Timeline: W12 (After PRJ-016)

| Service | Instrumentation | Method |
|---------|----------------|--------|
| **LiteLLM** | All proxied calls | Built-in OTEL export (config.yaml) |

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

## 📋 Phase 3 — Full Stack

### Timeline: W13+

| Service | Instrumentation | Method |
|---------|----------------|--------|
| **INT-P01, INT-S003, etc.** | LLM calls via LiteLLM | Automatic (LiteLLM traces all) |

---

## 📋 OTEL Instrumentation Plan

### OTEL Configuration (Direct — Phase 0/1)

```python
# For direct AnythingLLM instrumentation
from phoenix.otel import register
from openinference.instrumentation.openai import OpenAIInstrumentor

tracer_provider = register(
    endpoint="http://<phoenix-host>:6006/v1/traces",
    project_name="fedarch"
)

OpenAIInstrumentor().instrument(tracer_provider=tracer_provider)
```

### OTEL Configuration (LiteLLM — Phase 2)

```yaml
# In LiteLLM config.yaml
litellm_settings:
  callbacks: ["otel"]

environment_variables:
  OTEL_EXPORTER: "otlp_http"
  OTEL_ENDPOINT: "http://phoenix:6006/v1/traces"
```

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
W10: Deploy Phoenix Phase 0 (DO Droplet)
  └── Phoenix running on port 6006
  └── OTEL endpoint ready
  └── Observing existing infrastructure immediately

W12: Deploy LiteLLM (PRJ-016)
  └── LiteLLM config: OTEL_ENDPOINT=http://phoenix:6006/v1/traces
  └── ALL LLM traffic automatically traced
  └── Cost, latency, cache, failover = visible immediately
```

> **Phoenix = infrastructure for LiteLLM.** Deploy the observer before the thing being observed.

### Shared Docker Network (Phase 1+ on GB10-1)

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

## 📋 Project Team

| CCC | Role | Focus |
|-----|------|-------|
| **GTM** | **Owner** | Deployment, dashboard config, @MAIT, Phase 0 |
| **RMN** | **Platform** | OTEL instrumentation, LiteLLM integration |

> **Phase 0 = primarily @GTM solo.** @RMN for OTEL instrumentation (steps 7-8).

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
| Scope | Phoenix (primary) + OpenTelemetry + Uptime Kuma + MLflow (reference) |

### RAG Documents

| # | Source | Depth |
|---|--------|-------|
| 1 | docs.arize.com/phoenix | 2 |
| 2 | opentelemetry.io/docs | 1 (Python SDK only) |
| 3 | github.com/louislam/uptime-kuma/wiki | 1 |

---

## 📋 Risk Matrix

| # | Risk | Prob | Impact | Mitigation |
|---|------|------|--------|------------|
| 1 | GB10-1 not ready (PRJ-015) | Medium | High | **Phase 0 covers interim — DO Droplet** |
| 2 | OTEL instrumentation complexity | Low | Medium | Phoenix provides helper library (phoenix.otel) |
| 3 | Storage growth (traces) | Low | Low | SQLite + configurable retention; 2 TB NVMe (Phase 1+) |
| 4 | Phoenix project abandoned | Low | Low | BSD-3 = fork; 10K stars; Arize-backed |
| 5 | Network: cloud → GB10-1 (traces) | Medium | Low | Traces = async, non-blocking; latency irrelevant |
| 6 | Dashboard access (remote) | Low | Low | Tailscale/WireGuard or port forward |
| 7 | **GB10 delayed (PRJ-015)** | **Medium** | **Medium** | **Phase 0 covers indefinitely — DO Droplet provides observability until GB10 arrives; no blind period** |

---

## 📋 Relationship to Other Projects

| PRJ | Relationship |
|-----|-------------|
| **PRJ-014** | INT-P01 + INT-S003 traffic observed by Phoenix (Phase 0) |
| **PRJ-015** | Phoenix migrates TO GB10-1 #NoDe (Phase 1 — hardware dependency) |
| **PRJ-016** | LiteLLM sends OTEL traces TO Phoenix (Phase 2 — Phoenix = endpoint) |
| **PRJ-013** | Paperless-ngx co-located on GB10-1 (Phase 1 — shared Docker host) |
| **PRJ-018** | P.O.P. PostgreSQL monitored by Uptime Kuma (Phase 0) |

### Infrastructure Quad — Revised Execution Order

```
PRJ-014: SEPARATE  (INT-S003 + WeOwn.tools)     W10      ✅ GH LIVE
PRJ-017: OBSERVE   (Phoenix Phase 0 — DO)       W10      🆕 PHASE 0
PRJ-015: COMPUTE   (2× GB10)                    W10-W11  ⬜ @THY
PRJ-016: ROUTE     (LiteLLM)                    W12-W13  ⬜ After GB10

"Separate. Observe. Compute. Route."
```

---

## 📋 Discovered By (BP-047)

| CCC | Contributor | Role | Context |
|-----|-------------|------|---------|
| GTM | [yonks](https://GitHub.com/YonksTEAM) | Co-Founder / Chief Digital Alchemist | ADK Observability Ecosystem analysis — Phoenix selected 33/35 — W09; Phase 0 driven by 3 blind incidents W09 |

---

## 📋 Related Documents

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| PRJ-015_HybridArchitecture-GB10 | v3.1.4.3 | GTM_2026-W09_104 | GTM_2026-W09_108 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-015_HybridArchitecture-GB10.md) |
| PRJ-016_AIGateway-LiteLLM | v3.1.4.1 | GTM_2026-W09_117 | GTM_2026-W09_119 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-016_AIGateway-LiteLLM.md) |
| SharedKernel | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/SharedKernel.md) |
| Phoenix Docs | — | — | — | [docs.arize.com/phoenix](https://docs.arize.com/phoenix) |
| Phoenix GitHub | — | — | — | [github.com/Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) |
| Uptime Kuma | — | — | — | [github.com/louislam/uptime-kuma](https://github.com/louislam/uptime-kuma) |
| ISO/IEC 42001 | — | — | — | [iso.org/standard/42001](https://www.iso.org/standard/42001) |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| 3.1.4.2 | 2026-W09 | GTM_2026-W09_154 | GTM_2026-W09_158 | +Phase 0 (DO Infrastructure Observability — W10, no dependencies); +jAIMSnet brand identity (ISO 42001, 6 domains, GH org, ecosystem map); +Uptime Kuma REQUIRED (endpoint health monitoring); +Phase 0 deployment checklist (14 steps); +Phase 0 Docker Compose (Phoenix + Uptime Kuma); +Phase 0 #SmokeTest (10-point); +Phase 0 architecture diagram; +Phase 1 deployment checklist (migration from DO); +Risk #7 (GB10 delayed → Phase 0 covers); Infrastructure Quad reordered (Observe → position 2); Priority 🟠 P1 → 🔴 P0 (Phase 0); FULL PRESERVE Phase 1-3 content from v3.1.4.1 (L-097) |
| 3.1.4.1 | 2026-W09 | GTM_2026-W09_121 | GTM_2026-W09_122 | Initial project; Phoenix observability on GB10-1 #NoDe; BSD-3 FOSS; ~500 MB RAM; OTEL instrumentation (3 phases); LiteLLM integration (PRJ-016 endpoint); 6 dashboard views; 13-step deployment; Docker Compose; 6-point #SmokeTest; @MAIT:#Observability; 6-risk matrix; deploys BEFORE LiteLLM (infrastructure dependency) |

---

#FlowsBros #FedArch #Observability #Phoenix #OTEL #jAIMSnet #FOSS #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
