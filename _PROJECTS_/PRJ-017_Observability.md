# PRJ-017: Observability — 3-Layer Stack

## 📋 PRJ-017_Observability_v3.2.1.1.md
## ♾️ WeOwnNet 🌐 | jAIMSnet

| Field | Value |
|-------|-------|
| Document | PRJ-017_Observability.md |
| Version | 3.2.1.1 |
| CCC-ID | GTM_2026-W10_122 |
| Created | 2026-02-27 (W09) |
| Updated | 2026-03-04 (W10) |
| Season | #WeOwnSeason003 🚀 |
| Status | ✅ APPROVED |
| Lifecycle Stage | ✅ APPROVED (#DocLifecycle) |
| Source of Truth | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-017_Observability.md) |
| Tags | #Observability #Langfuse #UptimeKuma #jAIMSnet #FOSS #FlowsBros #Prometheus #Grafana #Loki |
| Brand | **jAIMSnet** (AI Management Systems network) |
| Urgency | 🔴 **HIGH — 5 blind incidents W06-W09, $7,277 no visibility** |

---

## 📖 Table of Contents

1. [Project Identity](#-project-identity)
2. [jAIMSnet Brand Identity](#-jaimsnet-brand-identity)
3. [jAIMSnet Observability Stack — 3 Layers](#-jaimsnet-observability-stack--3-layers)
4. [Incident History](#-incident-history)
5. [Why Langfuse](#-why-langfuse)
6. [What Gets Traced](#-what-gets-traced)
7. [Phase 0 — DO Infrastructure Observability](#-phase-0--do-infrastructure-observability)
8. [Phase 0 — Deployment Checklist](#-phase-0--deployment-checklist)
9. [Phase 0 — Docker Compose](#-phase-0--docker-compose)
10. [Phase 0 — Verification (#SmokeTest)](#-phase-0--verification-smoketest)
11. [Phase 0.5 — Infrastructure Observability](#-phase-05--infrastructure-observability)
12. [Phase 0.5 — Deployment Checklist](#-phase-05--deployment-checklist)
13. [Phase 0.5 — Docker Compose](#-phase-05--docker-compose)
14. [Phase 0.5 — Verification (#SmokeTest)](#-phase-05--verification-smoketest)
15. [Architecture](#-architecture)
16. [Phase 1 — Local Services (GB10-1)](#-phase-1--local-services-gb10-1)
17. [Phase 2 — LiteLLM Integration](#-phase-2--litellm-integration)
18. [Phase 3 — Full Stack](#-phase-3--full-stack)
19. [OTEL Instrumentation Plan](#-otel-instrumentation-plan)
20. [Dashboard Configuration](#-dashboard-configuration)
21. [Integration with PRJ-016 (LiteLLM)](#-integration-with-prj-016-litellm)
22. [Project Team](#-project-team)
23. [MAIT Architecture — 3 MAITs](#-mait-architecture--3-maits)
24. [Risk Matrix](#-risk-matrix)
25. [Relationship to Other Projects](#-relationship-to-other-projects)
26. [Discovered By](#-discovered-by)
27. [Related Documents](#-related-documents)
28. [Version History](#-version-history)

---

## 📋 Project Identity

| Field | Value |
|-------|-------|
| Project ID | **PRJ-017** |
| Title | **Observability — Langfuse Deployment** |
| Type | Infrastructure — Observability |
| Priority | 🔴 P0 (Phase 0 + 0.5) / 🟠 P1 (Phase 1-3) |
| Owner | @GTM (Layers 2+3) + @RMN (Layer 1) |
| Brand | **jAIMSnet** |
| Deployment | Phase 0: DO Droplet ATL1 / Phase 0.5: DO Droplet or GB10-1 / Phase 1+: GB10-1 #NoDe |
| Timeline | **Phase 0: W10** / **Phase 0.5: W10-W11** / Phase 1: W11 / Phase 2: W12 / Phase 3: W13+ |
| Depends on | Phase 0: None / Phase 0.5: Phase 0 / Phase 1: PRJ-015 / Phase 2: PRJ-016 |
| Feeds into | PRJ-016 (LiteLLM OTEL → Langfuse) |
| #masterCCC | GTM_2026-W10_122 |

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
| Relationship | Ecosystem brand under ♾️ WeOwnNet 🌐 |

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
| AI system monitoring | Langfuse traces + dashboards |
| Risk management | Observability → incident detection |
| Performance evaluation | Token cost, latency, error rates |
| Continual improvement | Data-driven optimization |
| Documentation | #FedArch governance (SharedKernel, BP, PROTO) |
| Accountability | CCC attribution system |
| **Infrastructure monitoring** | **Prometheus + Grafana + Loki (Layer 1)** |

### Ecosystem Brand Map

| Brand | Audience | Focus |
|-------|----------|-------|
| ♾️ WeOwnNet 🌐 | Real estate cooperatives | Cooperative ownership |
| 🔥 BurnedOut Media 🔀 | Burned out professionals | Retreat + coaching |
| **jAIMSnet** | AI practitioners + infrastructure | **Full-stack observability + AI management** |
| CCCbot.Net | CCC governance | Onchain cooperative |

### jAIMSnet × PRJ-017

| PRJ-017 Component | jAIMSnet Role |
|-------------------|---------------|
| Langfuse deployment | jAIMSnet Layer 3 (AI observability) |
| Uptime Kuma | jAIMSnet Layer 2 (endpoint monitoring) |
| **Prometheus + Grafana + Loki** | **jAIMSnet Layer 1 (infrastructure)** |
| OTEL instrumentation | jAIMSnet tooling |
| Dashboards | jAIMSnet monitoring platform |
| @MAIT:#Langfuse + @MAIT:#UptimeKuma + @MAIT:#InfraObs | jAIMSnet knowledge base (3 MAITs) |

### jAIMSnet GH Org — Proposed Repos

| # | Repo | Purpose | Timeline |
|---|------|---------|----------|
| 1 | jAIMSnet/docs | Documentation + ISO 42001 mapping | W14+ |
| 2 | jAIMSnet/langfuse-config | Langfuse deployment configs | W14+ |
| 3 | jAIMSnet/otel-recipes | OTEL instrumentation recipes | W14+ |
| 4 | **jAIMSnet/infra-stack** | **Prometheus + Grafana + Loki configs** | **W14+** |

> **W10-W13:** PRJ-017 docs stay in CCCbotNet/fedarch. **W14+:** jAIMSnet GH org gets its own repos.

---

## 📋 jAIMSnet Observability Stack — 3 Layers

```
┌─────────────────────────────────────────────────┐
│  Layer 3: AI OBSERVABILITY                       │
│  Langfuse + OTEL                    → @GTM        │
│  "What is the AI doing?"                         │
│  @MAIT:#Langfuse                                  │
├─────────────────────────────────────────────────┤
│  Layer 2: ENDPOINT MONITORING                    │
│  Uptime Kuma                       → @GTM        │
│  "Is it reachable?"                              │
│  @MAIT:#UptimeKuma                               │
├─────────────────────────────────────────────────┤
│  Layer 1: INFRASTRUCTURE                         │
│  Prometheus + Grafana + Loki       → @RMN        │
│  "What is the machine doing?"                    │
│  @MAIT:#InfraObs                                 │
└─────────────────────────────────────────────────┘
```

| Layer | Name | Tools | Owner | Answers |
|-------|------|-------|-------|---------|
| **3** | AI Observability | Langfuse + OTEL | @GTM | "What is the AI doing?" |
| **2** | Endpoint Monitoring | Uptime Kuma | @GTM | "Is it reachable?" |
| **1** | Infrastructure | Prometheus + Grafana + Loki | @RMN | "What is the machine doing?" |

### Why 3 Layers

| Question | Layer 3 (Langfuse) | Layer 2 (Kuma) | Layer 1 (Prom/Grafana) |
|----------|------------------|----------------|----------------------|
| LLM call latency is high — why? | ✅ Shows latency | ❌ | ✅ **Shows CPU/GPU pressure** |
| Website is down — why? | ❌ | ✅ Shows down | ✅ **Shows container crash** |
| Tokens cost spiked — why? | ✅ Shows per-request cost | ❌ | ❌ |
| Disk is full — what happens? | ❌ | ❌ | ✅ **Shows disk pressure** |
| Container OOM killed — what? | ❌ | ✅ Shows endpoint gone | ✅ **Shows memory + restart** |
| Need to search logs | ❌ | ❌ | ✅ **Loki log search** |

> **No single layer answers all questions. All 3 together = complete observability.**

---

## 📋 Incident History

| # | When | Duration | Root Cause | Detection | Layer That Catches It |
|---|------|----------|-----------|-----------|----------------------|
| 1 | W08 | 2h 18m | API key expired | User report (blind) | Layer 3 (Langfuse) |
| 2 | W06 | ~67 min | Embedder reverted | User report (blind) | Layer 2 (Kuma) + Layer 3 |
| 3 | W09 Tue | ~6.5 hrs | API key expired | @LDC report (blind) | Layer 3 (Langfuse) |
| 4 | W09 Sun AM | ~18 min | API key restart | @GTM manual (blind) | Layer 3 (Langfuse) |
| 5 | W09 Sun PM | ~9 min | API key lost | @GTM manual (blind) | Layer 3 + Layer 2 |
| **TOTAL** | | **~9.5 hrs** | **All blind** | **All human-detected** | **All preventable** |

> **9.5 hours of cumulative downtime. All blind. All same pattern. All preventable with observability.**

---

## 📋 Why Phoenix (Legacy Context)

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

## 📋 Phoenix → Langfuse Decision

### Decision Record

| Field | Value |
|-------|-------|
| Decision | **Langfuse replaces Phoenix as Layer 3** |
| Decided by | @GTM + @RMN consensus |
| @RMN analysis | RMN_2026-W10_043 |
| Approved | GTM_2026-W10_161 |
| Sunk cost | **$0** — Phoenix never deployed |
| Evaluation period | ❌ Not needed — clear winner |

### Comparison

| Factor | Phoenix (ELv2) | Langfuse (MIT) | Winner |
|--------|---------------|----------------|--------|
| **License** | ❌ ELv2 (NOT OSI-approved) | ✅ **MIT** (OSI-approved) | **Langfuse** 🏆 |
| **Priority #2 (FOSS)** | ⚠️ Questionable | ✅ **Aligned** | **Langfuse** 🏆 |
| **LiteLLM integration** | 🟡 Manual OTEL config | ✅ **Native callback (5 min)** | **Langfuse** 🏆 |
| **Multi-tenant** | 🟡 Manual tagging | ✅ **Automatic projects** | **Langfuse** 🏆 |
| **Self-hosted** | ✅ Docker | ✅ Docker | Tie |
| **@RMN recommends** | ❌ | ✅ | **Langfuse** 🏆 |

### Learning

| ID | Learning |
|----|----------|
| L-129 | ELv2 (Elastic License v2) is NOT OSI-approved — conflicts with Priority #2 (FOSS); ecosystem MUST prefer OSI-approved licenses (MIT, Apache 2.0, AGPL) over source-available licenses (ELv2, BSL, SSPL) when FOSS alternatives exist |

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

## 📋 jAIMS.app Domain Family

### All Observability Under One Roof

| Subdomain | Service | Layer | Status |
|-----------|---------|-------|--------|
| **langfuse.jAIMS.app** | **Langfuse** | Layer 3 (LLM) | 🔴 **DEPLOYING** |
| **kuma.jAIMS.app** | Uptime Kuma | Layer 2 (Endpoints) | ⬜ Phase 0 |
| **grafana.jAIMS.app** | Grafana | Layer 2 (Metrics) | ⬜ Phase 2 |
| **litellm.jAIMS.app** | LiteLLM (PRJ-016) | Router | 🔴 **DEPLOYING** |

### Why jAIMS.app

| Factor | Value |
|--------|-------|
| Brand | **jAIMSnet = platform engineering** (PRJ-025) |
| Scope | Observability = core jAIMSnet function |
| Separation | Agents = WeOwn.Agency. Data = WeOwn.tools. **Observability = jAIMS.app** |
| Consensus | @RMN + @GTM agree |

### Domain Family Summary

| Domain | Scope |
|--------|-------|
| **WeOwn.Agency** | AI agent instances (#AnythingLLM) |
| **WeOwn.tools** | Data + infrastructure services |
| **jAIMS.app** | **Observability + platform engineering** |
| **ccc.bot** | CCC governance |

---

## 📋 LiteLLM Integration (PRJ-016)

### How LiteLLM Feeds Langfuse

```
ALL INSTANCES → LiteLLM (PRJ-016)
                    │
                    ├── Routes to: MI300X / OpenRouter / GB10
                    │
                    └── success_callback: ["langfuse"]
                        │
                        └── langfuse.jAIMS.app receives:
                            ├── Every LLM call (automatic)
                            ├── Model, tokens, cost, latency
                            ├── Instance + user metadata
                            └── Full prompt/response (self-hosted)
```

### LiteLLM Configuration

```yaml
litellm_settings:
  success_callback: ["langfuse"]

environment_variables:
  LANGFUSE_PUBLIC_KEY: "pk-lf-..."
  LANGFUSE_SECRET_KEY: "sk-lf-..."
  LANGFUSE_HOST: "https://langfuse.jaims.app"
```

> **5 minutes.** Add 3 environment variables to LiteLLM. Every LLM call across every instance = automatically traced.

### Why Langfuse Deploys WITH LiteLLM (Not Before)

| Previously (Phoenix) | Now (Langfuse) |
|---------------------|----------------|
| Phoenix deploys BEFORE LiteLLM | **Langfuse deploys WITH LiteLLM** |
| Separate OTEL config per instance | **Single LiteLLM callback — all instances** |
| More complex, more steps | **5 minutes, 3 env vars** |

---

## 📋 Multi-Tenant Tracking (#ZeroTo100)

### Why Multi-Tenant Matters

| Scenario | Without Langfuse | With Langfuse |
|----------|-----------------|---------------|
| "How much did @GTM spend today?" | ❌ Unknown | ✅ **$47.23** |
| "Cost per AgencyPRO customer?" | ❌ Unknown | ✅ **$12.50/customer/mo** |
| "Which instance uses most tokens?" | ❌ Unknown | ✅ **INT-P01 (42%)** |
| "Llama vs Claude quality?" | ❌ Unknown | ✅ **Llama 94.2% match** |

### Langfuse Multi-Tenant Architecture

```
Langfuse Projects:
├── weownnet-governance    ← INT-P01 traces
├── burnedout-media        ← INT-P02 traces
├── pop-database           ← INT-P03 traces
├── weown-events           ← INT-P04 traces
├── agencypro-production   ← INT-P05 traces
│   ├── customer-001       ← Per AgencyPRO customer
│   └── ... (40 customers in March)
├── seasonal-shared        ← INT-S003 traces
├── home-gtm               ← INT-OG1 traces
└── home-rmn               ← INT-OG8 traces
```

---

## 📋 Self-Hosted Architecture

### Co-Location Strategy (All Services — 1 Droplet)

```
DO Droplet (ATL1 — "jAIMSnet Observability")
├── LiteLLM (PRJ-016) — port 4000
├── Langfuse — port 3000
├── Uptime Kuma — port 3001
├── Caddy (reverse proxy + SSL)
│   ├── litellm.jaims.app → :4000
│   ├── langfuse.jaims.app → :3000
│   └── kuma.jaims.app → :3001
└── PostgreSQL connection → ATL1 managed cluster
```

### Why Self-Host from Day 1

| Factor | Cloud | Self-Hosted |
|--------|-------|-------------|
| Data sovereignty | 🟡 Third-party | ✅ **Our servers (ATL1)** |
| Prompt logging | ❌ Disabled (PII) | ✅ **ENABLED** |
| Cost | Free → $59/mo | **$0 extra** (co-locate) |
| Priority #3 | ❌ Violates | ✅ **Aligned** |

### Droplet Spec

| Field | Value |
|-------|-------|
| Region | ATL1 |
| Plan | Basic — 2 vCPU / 4 GB / 80 GB |
| Cost | **~$24/mo** (all services) |

---

## 📋 Phase 0 — DO Infrastructure Observability

### Why Phase 0

| Incident | When | Detected By | With Phase 0 |
|----------|------|------------|-------------|
| API key lost (W08) | 2h 18m downtime | User report | ✅ 0 traces → alert in <60s |
| API key restart (W09) | ~18 min | @GTM manual | ✅ Trace failure → alert |
| API key lost (W09 AM) | ~69 min | @LDC report | ✅ 0 traces → alert in <60s |
| API key lost (W09 PM) | ~9 min | @GTM manual | ✅ 0 traces → alert in <60s |
| $5,249 blind spend | 91 days | Manual counting | ✅ Per-instance cost dashboard |

> **5 incidents detected by humans. All 5 would have been caught by Langfuse in <60 seconds.**

### Phase 0 Scope

| # | What to Observe | Source | Method |
|---|----------------|--------|--------|
| 1 | **LLM calls** (INT-P01, INT-P02) | AnythingLLM | OTEL SDK → Langfuse |
| 2 | **OpenRouter API health** | LLM provider | Trace success/failure |
| 3 | **Token cost per instance** | OTEL metadata | Langfuse dashboard |
| 4 | **Request latency** | OTEL spans | Langfuse dashboard |
| 5 | **Error rates** | OTEL traces | Langfuse alerting |
| 6 | **Endpoint uptime** | All domains | Uptime Kuma |
| 7 | **SSL certificate expiry** | All domains | Uptime Kuma |
| 8 | **PostgreSQL connectivity** | DO Managed DB | Uptime Kuma |

### Phase 0 Infrastructure

| Field | Value |
|-------|-------|
| Host | **DO Droplet — ATL1** |
| Plan | Basic — 2 vCPU / 4 GB / 80 GB |
| Cost | **$24/mo** |
| Domain | Langfuse.jAIMS.app |
| Duration | Until GB10-1 arrives → migrate to #NoDe |
| Services | Langfuse (REQUIRED) + Uptime Kuma (REQUIRED) |

### Resource Utilization (Phase 0)

| Service | RAM | Port |
|---------|-----|------|
| Langfuse | ~500 MB | 3000 |
| Uptime Kuma | ~50 MB | 3001 |
| **TOTAL** | **~550 MB / 2 GB (28%)** | |

### Observability Layers — Phase 0

| Layer | Tool | What It Sees |
|-------|------|-------------|
| **Layer 3 (AI)** | Langfuse | LLM calls, tokens, cost, latency, RAG, traces |
| **Layer 2 (Endpoints)** | Uptime Kuma | Endpoint uptime, SSL, DNS, PostgreSQL, OpenRouter |

> **Phase 0 = Layer 3 + Layer 2. Layer 1 = Phase 0.5 (@RMN).**

### Migration Path

```
W10:  Langfuse + Uptime Kuma on DO Droplet (ATL1) — $24/mo
      └── Observes: INT-P01, INT-P02, PostgreSQL, WordPress

W10-W11: @RMN adds Prom/Grafana/Loki (Phase 0.5)
         └── Co-locate on same Droplet ($24/mo upgrade) OR GB10-1

W11+: GB10-1 arrives (PRJ-015)
      └── Migrate ALL observability to GB10-1 #NoDe ($0/mo)
      └── Destroy DO Droplet (save $18-24/mo)
      └── Continues observing cloud from edge
```

---

## 📋 Phase 0 — Deployment Checklist

| # | Step | Owner | Depends On | Status |
|---|------|-------|-----------|--------|
| 1 | Create jAIMSnet DO TEAM | @GTM | None | ⬜ |
| 2 | Create DO Droplet (ATL1, 4 GB) | @RMN | Step 1 | ⬜ |
| 3 | Install Docker + Docker Compose | @RMN | Step 2 | ⬜ |
| 4 | Create langfuse_db on ATL1 PostgreSQL | @RMN | Step 2 | ⬜ |
| 5 | Create langfuse_user (restricted) | @RMN | Step 4 | ⬜ |
| 6 | Create docker-compose.yml (all services) | @RMN | Step 3 | ⬜ |
| 7 | Create Caddyfile (3 subdomains) | @RMN | Step 6 | ⬜ |
| 8 | Configure DNS (langfuse + kuma + litellm → jAIMS.app) | @GTM | Step 2 | ⬜ |
| 9 | docker compose up -d | @RMN | Step 7 | ⬜ |
| 10 | Verify Langfuse UI (https://langfuse.jaims.app) | @GTM | Step 9 | ⬜ |
| 11 | Create Langfuse API keys | @RMN | Step 10 | ⬜ |
| 12 | Add Langfuse callback to LiteLLM (3 env vars) | @RMN | Step 11 | ⬜ |
| 13 | Enable full prompt/response logging | @RMN | Step 12 | ⬜ |
| 14 | Create Langfuse projects (per instance) | @RMN | Step 10 | ⬜ |
| 15 | Configure Uptime Kuma monitors (12 targets) | @GTM | Step 9 | ⬜ |
| 16 | Send test LLM call → verify trace in Langfuse | @GTM | Step 12 | ⬜ |
| 17 | Phase 0 #SmokeTest (12-point) | @GTM | Step 16 | ⬜ |
| 18 | FULL:SYNC:META | @GTM | Step 17 | ⬜ |

---

## 📋 Phase 0 — Docker Compose

```yaml
# docker-compose.yml — jAIMSnet Observability Phase 0 (DO Droplet — ATL1)
version: '3.8'

services:
  litellm:
    image: ghcr.io/berriai/litellm:main-latest
    container_name: litellm
    restart: unless-stopped
    ports:
      - "4000:4000"
    volumes:
      - ./litellm_config.yaml:/app/config.yaml
    environment:
      - LANGFUSE_PUBLIC_KEY=${LANGFUSE_PUBLIC_KEY}
      - LANGFUSE_SECRET_KEY=${LANGFUSE_SECRET_KEY}
      - LANGFUSE_HOST=http://langfuse:3000
      - OPENROUTER_API_KEY=${OPENROUTER_API_KEY}
    command: ["--config", "/app/config.yaml"]

  langfuse:
    image: langfuse/langfuse:latest
    container_name: langfuse
    restart: unless-stopped
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=postgresql://langfuse_user:${DB_PASSWORD}@${DB_HOST}:25060/langfuse_db?sslmode=require
      - NEXTAUTH_SECRET=${NEXTAUTH_SECRET}
      - NEXTAUTH_URL=https://langfuse.jaims.app
      - SALT=${SALT}

  uptime-kuma:
    image: louislam/uptime-kuma:1
    container_name: uptime-kuma
    restart: unless-stopped
    ports:
      - "3001:3001"
    volumes:
      - uptime_data:/app/data

  caddy:
    image: caddy:2-alpine
    container_name: caddy
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./Caddyfile:/etc/caddy/Caddyfile
      - caddy_data:/data
      - caddy_config:/config

volumes:
  uptime_data:
  caddy_data:
  caddy_config:
```

### Caddyfile

```
langfuse.jaims.app {
    reverse_proxy langfuse:3000
}

kuma.jaims.app {
    reverse_proxy uptime-kuma:3001
}

litellm.jaims.app {
    reverse_proxy litellm:4000
}
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

### Phase 0 #SmokeTest (12-Point)

| # | Test | Expected | Status |
|---|------|----------|--------|
| 1 | Langfuse running | https://langfuse.jaims.app → login | ⬜ |
| 2 | LiteLLM running | https://litellm.jaims.app → health | ⬜ |
| 3 | LLM call trace | Make call via LiteLLM → trace in Langfuse | ⬜ |
| 4 | Cost visible | Trace shows $ amount | ⬜ |
| 5 | Latency visible | Trace shows ms | ⬜ |
| 6 | Model tracked | Trace shows model name | ⬜ |
| 7 | Prompt logged | Full prompt visible (self-hosted) | ⬜ |
| 8 | Multi-project | Separate projects per instance | ⬜ |
| 9 | Uptime Kuma running | https://kuma.jaims.app → dashboard | ⬜ |
| 10 | Uptime Kuma monitors | 12 endpoints green | ⬜ |
| 11 | Persistence (Langfuse) | Restart → traces retained | ⬜ |
| 12 | Persistence (Kuma) | Restart → monitors retained | ⬜ |

---

## 📋 Phase 0.5 — Infrastructure Observability

### Why Phase 0.5

> *"Running local LLMs on bare metal is even more of a reason to have node-level observability. Whether it's cloud or bare metal, a full observability stack is absolutely critical to monitor performance and identify any issues at an infra level."* — @RMN (GTM_2026-W09_185)

| What Langfuse sees | What Langfuse DOESN'T see |
|-------------------|-------------------------|
| LLM call latency | ❌ Why latency is high (CPU pressure?) |
| Token cost | ❌ Disk running out |
| Trace failures | ❌ Container OOM kills |
| | ❌ GPU thermal throttling |
| | ❌ Log aggregation / search |
| | ❌ Docker container health |
| | ❌ Network I/O |

### Phase 0.5 Identity

| Field | Value |
|-------|-------|
| Phase | **0.5** |
| Name | Infrastructure Observability |
| Tools | Prometheus + Grafana + Loki + node_exporter + cAdvisor + Promtail |
| Owner | **@RMN** |
| Timeline | W10-W11 (parallel to Phase 0) |
| Dependency | Phase 0 (co-locate on DO Droplet or deploy on GB10-1) |
| Trigger | @RMN Signal feedback (GTM_2026-W09_185) |
| Standard | Industry standard / best practice (Prometheus + Grafana + Loki) |

### Phase 0.5 Scope

| # | What to Monitor | Tool | Source |
|---|----------------|------|--------|
| 1 | CPU utilization | Prometheus + node_exporter | All hosts |
| 2 | GPU utilization | Prometheus + nvidia_exporter | GB10-1 (Phase 1+) |
| 3 | Memory pressure | Prometheus + node_exporter | All hosts |
| 4 | Disk I/O + capacity | Prometheus + node_exporter | All hosts |
| 5 | Container health | Prometheus + cAdvisor | Docker hosts |
| 6 | Container restarts | Prometheus + cAdvisor | Docker hosts |
| 7 | Network I/O | Prometheus + node_exporter | All hosts |
| 8 | Log aggregation | Loki + Promtail | All services |
| 9 | Log search | Grafana (Loki datasource) | All services |
| 10 | Dashboard visualization | Grafana | All metrics |

### Phase 0.5 Resource Requirements

| Service | RAM | Port |
|---------|-----|------|
| Prometheus | ~500 MB - 1 GB | 9090 |
| Grafana | ~200-500 MB | 3000 |
| Loki | ~500 MB - 1 GB | 3100 |
| Promtail | ~50 MB | — |
| node_exporter | ~20 MB | 9100 |
| cAdvisor | ~50 MB | 8080 |
| **TOTAL** | **~1.3 - 3 GB** | |

### Deployment Options

| Option | Where | Cost | When |
|--------|-------|------|------|
| A: Co-locate on DO Droplet | NYC1 (upgrade to 4 GB) | $24/mo | W10 |
| B: Deploy on GB10-1 directly | Northglenn, CO | $0/mo | W11+ (after PRJ-015) |
| C: Separate DO Droplet | NYC1 | +$18/mo | W10 |

> **@RMN decides deployment option.** Phase 0 MUST NOT be blocked on this decision.

---

## 📋 Phase 0.5 — Deployment Checklist

| # | Step | Owner | Depends On | Status |
|---|------|-------|-----------|--------|
| 1 | Choose deployment option (A/B/C) | @RMN | None | ⬜ |
| 2 | Provision host (if new) or upgrade Droplet | @RMN / @GTM | Step 1 | ⬜ |
| 3 | Create `observability-infra/` directory | @RMN | Step 2 | ⬜ |
| 4 | Create `docker-compose.observability-infra.yml` | @RMN | Step 3 | ⬜ |
| 5 | Create `prometheus.yml` config | @RMN | Step 4 | ⬜ |
| 6 | Create `promtail.yml` config | @RMN | Step 4 | ⬜ |
| 7 | `docker compose up -d` | @RMN | Step 6 | ⬜ |
| 8 | Verify Prometheus UI (http://<IP>:9090) | @RMN | Step 7 | ⬜ |
| 9 | Verify Grafana UI (http://<IP>:3000) | @RMN | Step 7 | ⬜ |
| 10 | Add Prometheus datasource in Grafana | @RMN | Step 9 | ⬜ |
| 11 | Add Loki datasource in Grafana | @RMN | Step 9 | ⬜ |
| 12 | Import node_exporter dashboard | @RMN | Step 10 | ⬜ |
| 13 | Import cAdvisor dashboard | @RMN | Step 10 | ⬜ |
| 14 | Phase 0.5 #SmokeTest (10-point) | @RMN | Step 13 | ⬜ |
| 15 | FULL:SYNC:META | @RMN | Step 14 | ⬜ |

> **15 steps. @RMN owns all steps. @GTM assists with Droplet upgrade if Option A.**

---

## 📋 Phase 0.5 — Docker Compose

```yaml
# docker-compose.observability-infra.yml — jAIMSnet Infrastructure (Phase 0.5)
version: '3.8'

services:
  prometheus:
    image: prom/prometheus:latest
    container_name: prometheus
    restart: unless-stopped
    ports:
      - "9090:9090"
    volumes:
      - prometheus_data:/prometheus
      - ./prometheus.yml:/etc/prometheus/prometheus.yml

  grafana:
    image: grafana/grafana:latest
    container_name: grafana
    restart: unless-stopped
    ports:
      - "3000:3000"
    volumes:
      - grafana_data:/var/lib/grafana
    depends_on:
      - prometheus

  loki:
    image: grafana/loki:latest
    container_name: loki
    restart: unless-stopped
    ports:
      - "3100:3100"
    volumes:
      - loki_data:/loki

  promtail:
    image: grafana/promtail:latest
    container_name: promtail
    restart: unless-stopped
    volumes:
      - /var/log:/var/log:ro
      - ./promtail.yml:/etc/promtail/config.yml

  node-exporter:
    image: prom/node-exporter:latest
    container_name: node-exporter
    restart: unless-stopped
    ports:
      - "9100:9100"

  cadvisor:
    image: gcr.io/cadvisor/cadvisor:latest
    container_name: cadvisor
    restart: unless-stopped
    ports:
      - "8080:8080"
    volumes:
      - /:/rootfs:ro
      - /var/run:/var/run:ro
      - /sys:/sys:ro
      - /var/lib/docker/:/var/lib/docker:ro

volumes:
  prometheus_data:
  grafana_data:
  loki_data:
```

---

## 📋 Phase 0.5 — Verification (#SmokeTest)

### Phase 0.5 #SmokeTest (10-Point)

| # | Test | Expected | Status |
|---|------|----------|--------|
| 1 | Prometheus running | `curl http://<IP>:9090` → UI | ⬜ |
| 2 | node_exporter metrics | `curl http://<IP>:9100/metrics` → CPU/memory data | ⬜ |
| 3 | cAdvisor metrics | `curl http://<IP>:8080/metrics` → container data | ⬜ |
| 4 | Grafana running | `http://<IP>:3000` → login page | ⬜ |
| 5 | Prometheus datasource | Grafana → Data Sources → Prometheus → Test → ✅ | ⬜ |
| 6 | Loki datasource | Grafana → Data Sources → Loki → Test → ✅ | ⬜ |
| 7 | Node dashboard | CPU, memory, disk, network visible | ⬜ |
| 8 | Container dashboard | Container health, restarts visible | ⬜ |
| 9 | Log search | Grafana → Explore → Loki → query returns logs | ⬜ |
| 10 | Persistence | Restart all → data retained | ⬜ |

---

## 📋 Architecture

### Phase 0 + 0.5 Architecture (W10 — DO Droplet)

```
┌──────────────────────────────────────────────────────────┐
│  DigitalOcean — NYC1                                      │
│                                                           │
│  ┌────────────────────────────────────────────────────┐  │
│  │  jAIMSnet Observability Droplet ($18-24/mo)         │  │
│  │                                                     │  │
│  │  LAYER 3 (AI):                                     │  │
│  │  ┌──────────────┐                                  │  │
│  │  │  Langfuse      │ OTEL traces from INT-P01/P02    │  │
│  │  │  Port: 3000   │                                  │  │
│  │  └──────────────┘                                  │  │
│  │                                                     │  │
│  │  LAYER 2 (Endpoints):                              │  │
│  │  ┌──────────────┐                                  │  │
│  │  │  Uptime Kuma  │ Health checks → all endpoints   │  │
│  │  │  Port: 3001   │                                  │  │
│  │  └──────────────┘                                  │  │
│  │                                                     │  │
│  │  LAYER 1 (Infrastructure) — Phase 0.5:             │  │
│  │  ┌──────────┐ ┌────────┐ ┌──────┐                │  │
│  │  │Prometheus│ │Grafana │ │ Loki │                │  │
│  │  │  :9090   │ │ :3000  │ │:3100 │                │  │
│  │  └──────────┘ └────────┘ └──────┘                │  │
│  │  ┌────────────┐ ┌──────────┐ ┌─────────┐        │  │
│  │  │node_export │ │ cAdvisor │ │Promtail │        │  │
│  │  │   :9100    │ │  :8080   │ │         │        │  │
│  │  └────────────┘ └──────────┘ └─────────┘        │  │
│  └────────────────────────────────────────────────────┘  │
│                                                           │
│  ┌────────────────────────────────────────────────────┐  │
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
│  LAYER 3 (AI):                                           │
│  ┌──────────────────────────────────────────────────┐   │
│  │  Langfuse (Port: 3000)                             │   │
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
│                                                          │
│  LAYER 2 (Endpoints):                                    │
│  ┌──────────────────────────────────────────────────┐   │
│  │  Uptime Kuma (Port: 3001)                         │   │
│  └──────────────────────────────────────────────────┘   │
│                                                          │
│  LAYER 1 (Infrastructure):                               │
│  ┌──────────────────────────────────────────────────┐   │
│  │  Prometheus :9090 │ Grafana :3000 │ Loki :3100    │   │
│  │  node_exporter :9100 │ cAdvisor :8080 │ Promtail  │   │
│  │  nvidia_exporter (GPU) 🆕                         │   │
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
3. OTEL exports trace to Langfuse (http://<langfuse>:3000/v1/traces)
4. Langfuse stores in SQLite
5. Langfuse dashboard visualizes
6. Prometheus scrapes node_exporter + cAdvisor (Layer 1)
7. Loki ingests logs via Promtail (Layer 1)
8. Grafana visualizes Prometheus + Loki (Layer 1)
9. @GTM / @RMN view dashboards
```

---

## 📋 Phase 1 — Local Services (GB10-1)

### Timeline: W11 (After PRJ-015)

| Service | Instrumentation | Method |
|---------|----------------|--------|
| **AnythingLLM (local)** | LLM calls + RAG retrieval | OTEL Python SDK or langfuse.otel |
| **Ollama** | Inference calls | OTEL wrapper |

### Deployment Checklist (Phase 1)

| # | Step | Owner | Depends On | Status |
|---|------|-------|-----------|--------|
| 1 | GB10-1 #NoDe operational | @GTM | PRJ-015 | ⬜ |
| 2 | Migrate Langfuse from DO Droplet to GB10-1 | @GTM | Step 1 | ⬜ |
| 3 | Migrate Uptime Kuma from DO Droplet to GB10-1 | @GTM | Step 1 | ⬜ |
| 4 | Migrate Prom/Grafana/Loki from DO Droplet to GB10-1 | @RMN | Step 1 | ⬜ |
| 5 | Add nvidia_exporter for GPU monitoring | @RMN | Step 4 | ⬜ |
| 6 | Destroy DO Droplet | @GTM | Step 2 + 3 + 4 | ⬜ |
| 7 | Install OTEL SDK on AnythingLLM (local) | @RMN | Step 2 | ⬜ |
| 8 | Send test trace | @GTM | Step 7 | ⬜ |
| 9 | Verify trace appears in Langfuse UI | @GTM | Step 8 | ⬜ |
| 10 | Instrument Ollama calls | @RMN | Step 7 | ⬜ |

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
  OTEL_ENDPOINT: "http://langfuse:3000/v1/traces"
```

> **When PRJ-016 deploys, ALL LLM traffic automatically traces to Langfuse.** Zero additional instrumentation needed per instance.

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
from langfuse.otel import register
from openinference.instrumentation.openai import OpenAIInstrumentor

tracer_provider = register(
    endpoint="http://<langfuse-host>:3000/v1/traces",
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
  OTEL_ENDPOINT: "http://langfuse:3000/v1/traces"
```

---

## 📋 Dashboard Configuration

### Default Views (Layer 3 — Langfuse)

| Dashboard | Metrics | Purpose |
|-----------|---------|---------|
| **Traces** | Request waterfall, spans, latency | Debug individual requests |
| **LLM Calls** | Model, tokens in/out, cost, latency | Usage patterns |
| **Embeddings** | Embedding latency, batch sizes | Performance monitoring |
| **RAG** | Retrieval relevance, chunks returned | RAG quality |

### Custom Views for #FedArch (Layer 3 — Langfuse)

| View | Metrics | Purpose |
|------|---------|---------|
| **Cost by Instance** | Tokens × cost per instance | Budget tracking |
| **Model Distribution** | % Claude vs % Llama vs % Qwen3 | #HybridArchitecture balance |
| **Cache Effectiveness** | Hit/miss rate (via LiteLLM) | Savings validation |
| **Failover Events** | OpenRouter → Ollama transitions | Reliability monitoring |
| **Error Rate** | Errors by provider, model, instance | Health monitoring |

### Infrastructure Dashboards (Layer 1 — Grafana)

| Dashboard | Metrics | Purpose |
|-----------|---------|---------|
| **Node Overview** | CPU, memory, disk, network | Host health |
| **Container Overview** | Container CPU, memory, restarts | Docker health |
| **GPU Monitoring** | GPU utilization, temperature, memory | GB10-1 inference health |
| **Log Explorer** | Log search, filter, aggregate | Debugging |

---

## 📋 Integration with PRJ-016 (LiteLLM)

### Why Langfuse Deploys BEFORE LiteLLM

```
W10: Deploy Langfuse Phase 0 (DO Droplet)
  └── Langfuse running on port 3000
  └── OTEL endpoint ready
  └── Observing existing infrastructure immediately

W12: Deploy LiteLLM (PRJ-016)
  └── LiteLLM config: OTEL_ENDPOINT=http://langfuse:3000/v1/traces
  └── ALL LLM traffic automatically traced
  └── Cost, latency, cache, failover = visible immediately
```

> **Langfuse = infrastructure for LiteLLM.** Deploy the observer before the thing being observed.

### Shared Docker Network (Phase 1+ on GB10-1)

```yaml
# Both PRJ-016 and PRJ-017 on same Docker network
networks:
  fedarch-edge:
    driver: bridge

# Langfuse joins:
services:
  langfuse:
    networks:
      - fedarch-edge

# LiteLLM joins:
services:
  litellm:
    networks:
      - fedarch-edge
    environment:
      - OTEL_ENDPOINT=http://langfuse:3000/v1/traces

# Prometheus joins:
services:
  prometheus:
    networks:
      - fedarch-edge
```

---

## 📋 Project Team

| CCC | Role | Layers | Focus |
|-----|------|--------|-------|
| **GTM** | **Owner** | Layer 3 + Layer 2 | Langfuse, Uptime Kuma, Phase 0, dashboards, @MAIT |
| **RMN** | **Platform + Infra Observability** | **Layer 1** | **Prometheus, Grafana, Loki, OTEL instrumentation, Phase 0.5** |

> **Phase 0 = primarily @GTM solo.** Phase 0.5 = @RMN. Phase 1+ = both.

---

## 📋 MAIT Architecture — 3 MAITs

> **#MAITlivesInAthread** — "One thread, one tool, one truth."

### @MAIT:#Langfuse

| Field | Value |
|-------|-------|
| Thread | MAIT_Langfuse |
| UUID | ⬜ TBD |
| ShortCode | @MAIT:#Langfuse |
| Steward | @GTM |
| Instance | INT-P01 |
| Protocol | #ContextVolley |
| Tool Agent | t-langfuse_tool |
| Scope | Langfuse LLM observability + LiteLLM callback integration |

#### RAG Documents

| # | Source | Depth |
|---|--------|-------|
| 1 | langfuse.com/docs | 2 |
| 2 | opentelemetry.io/docs (Python SDK) | 1 |
| 3 | github.com/langfuse/langfuse (GH Repo connector) | — |

### @MAIT:#UptimeKuma

| Field | Value |
|-------|-------|
| Thread | MAIT_UptimeKuma |
| UUID | 002676d5-66f8-42fb-aee8-a89f67c63fb3 |
| ShortCode | @MAIT:#UptimeKuma |
| Steward | @GTM |
| Instance | INT-P01 |
| Protocol | #ContextVolley |
| Tool Agent | t-uptimekuma_tool |
| Scope | Uptime Kuma endpoint monitoring + SSL + DNS health |

#### RAG Documents

| # | Source | Depth |
|---|--------|-------|
| 1 | github.com/louislam/uptime-kuma/wiki | 2 |

### @MAIT:#InfraObs

| Field | Value |
|-------|-------|
| Thread | MAIT_InfraObs |
| UUID | ⬜ TBD (created by @RMN) |
| ShortCode | @MAIT:#InfraObs |
| Steward | **@RMN** |
| Instance | INT-P01 |
| Protocol | #ContextVolley |
| Tool Agent | t-infraobs_tool |
| Scope | Prometheus + Grafana + Loki + node_exporter + cAdvisor |

#### RAG Documents

| # | Source | Depth |
|---|--------|-------|
| 1 | prometheus.io/docs | 2 |
| 2 | grafana.com/docs/grafana | 2 |
| 3 | grafana.com/docs/loki | 2 |

---

## 📋 Risk Matrix

| # | Risk | Prob | Impact | Mitigation |
|---|------|------|--------|------------|
| 1 | GB10-1 not ready (PRJ-015) | Medium | High | **Phase 0 covers interim — DO Droplet** |
| 2 | OTEL instrumentation complexity | Low | Medium | Langfuse provides helper library (langfuse.otel) |
| 3 | Storage growth (traces) | Low | Low | SQLite + configurable retention; 2 TB NVMe (Phase 1+) |
| 4 | Langfuse project abandoned | Low | Low | MIT = fork-friendly |
| 5 | Network: cloud → GB10-1 (traces) | Medium | Low | Traces = async, non-blocking; latency irrelevant |
| 6 | Dashboard access (remote) | Low | Low | Tailscale/WireGuard or port forward |
| 7 | GB10 delayed (PRJ-015) | Medium | Medium | Phase 0 covers indefinitely — DO Droplet provides observability until GB10 arrives |
| 8 | **@RMN availability for Layer 1** | **Low** | **Medium** | **Phase 0 (Layer 2+3) deploys independently; Layer 1 = parallel track; no blocking** |

---

## 📋 Relationship to Other Projects

| PRJ | Relationship |
|-----|-------------|
| **PRJ-014** | INT-P01 + INT-S003 traffic observed by Langfuse (Phase 0) |
| **PRJ-015** | All observability migrates TO GB10-1 #NoDe (Phase 1 — hardware dependency) |
| **PRJ-016** | LiteLLM sends OTEL traces TO Langfuse (Phase 2 — Langfuse = endpoint) |
| **PRJ-013** | Paperless-ngx co-located on GB10-1 (Phase 1 — shared Docker host) |
| **PRJ-018** | P.O.P. PostgreSQL monitored by Uptime Kuma (Phase 0) |

### Infrastructure Quad — Execution Order

```
PRJ-014: SEPARATE  (INT-S003 + WeOwn.tools)     W10      ✅ GH LIVE
PRJ-017: OBSERVE   (Langfuse Phase 0 — DO)       W10      🔴 PHASE 0 MONDAY
PRJ-015: COMPUTE   (2× GB10)                    W10-W11  ⬜ @THY
PRJ-016: ROUTE     (LiteLLM)                    W12-W13  ⬜ After GB10

"Separate. Observe. Compute. Route."
```

---

## 📋 Discovered By (BP-047)

| CCC | Contributor | Role | Context |
|-----|-------------|------|---------|
| GTM | [yonks](https://GitHub.com/YonksTEAM) | Co-Founder / Chief Digital Alchemist | ADK Observability Ecosystem analysis — Langfuse selected 33/35 — W09; Phase 0 driven by 5 blind incidents W06-W09 |
| RMN | Roman Di Domizio | AI Platform Engineer | Identified missing Layer 1 (infrastructure observability) — W09; **Langfuse recommendation (RMN_2026-W10_043) — MIT license + native LiteLLM callback — W10** |

---

## 📋 Related Documents

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| PRJ-015_HybridArchitecture | v3.2.1.1 | GTM_2026-W10_122 | GTM_2026-W10_125 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-015_HybridArchitecture.md) |
| PRJ-016_AIGateway-LiteLLM | v3.1.4.1 | GTM_2026-W09_117 | GTM_2026-W09_119 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-016_AIGateway-LiteLLM.md) |
| SharedKernel | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/SharedKernel.md) |
| Langfuse Docs | — | — | — | [langfuse.com/docs](https://langfuse.com/docs) |
| Langfuse GitHub | — | — | — | [github.com/langfuse/langfuse](https://github.com/langfuse/langfuse) |
| Uptime Kuma | — | — | — | [github.com/louislam/uptime-kuma](https://github.com/louislam/uptime-kuma) |
| Prometheus | — | — | — | [prometheus.io](https://prometheus.io) |
| Grafana | — | — | — | [grafana.com](https://grafana.com) |
| Loki | — | — | — | [grafana.com/oss/loki](https://grafana.com/oss/loki) |
| ISO/IEC 42001 | — | — | — | [iso.org/standard/42001](https://www.iso.org/standard/42001) |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| 3.2.1.1 | 2026-W10 | GTM_2026-W10_122 | GTM_2026-W10_161 | **Phoenix → Langfuse** (Layer 3); MIT replaces ELv2 (L-129 — Priority #2); self-host from Day 1 at langfuse.jAIMS.app; co-locate LiteLLM + Langfuse + Uptime Kuma on ATL1 ($24/mo); native LiteLLM callback (5 min — replaces manual OTEL); full prompt logging (self-hosted = safe); +Multi-Tenant Tracking section (#ZeroTo100); +jAIMS.app Domain Family section; +LiteLLM Integration section; +Phoenix → Langfuse Decision section; +Self-Hosted Architecture section; Phase 0 host NYC1 → ATL1 (co-locate); Phase 0 Docker Compose updated (LiteLLM + Langfuse + Kuma + Caddy); Phase 0 checklist updated (14 → 18 steps); Phase 0 #SmokeTest updated (10 → 12 points); @MAIT:#Phoenix → @MAIT:#Langfuse; t-phoenix_tool → t-langfuse_tool; title → "Observability — 3-Layer Stack"; @RMN Discovered By updated (Langfuse recommendation); FULL PRESERVE from v3.1.4.3 (L-097) |
| 3.1.4.3 | 2026-W09 | GTM_2026-W09_185 | GTM_2026-W09_191 | +3-layer jAIMSnet observability stack (AI + Endpoint + Infrastructure); +Phase 0.5 (Prometheus + Grafana + Loki — @RMN owns Layer 1); +Phase 0.5 Docker Compose (6 services); +Phase 0.5 deployment checklist (15 steps); +Phase 0.5 #SmokeTest (10-point); +@MAIT:#InfraObs (Steward: @RMN) + t-infraobs_tool; +Incident history (5 incidents — all blind); @RMN elevated: Platform → Platform + Infra Observability; +@RMN in Discovered By (BP-047); GB10-1 resource allocation 65% → 67%; jAIMSnet scope 2-layer → 3-layer; MAIT section: 1 MAIT → 3 MAITs; +Infrastructure dashboards (Layer 1 — Grafana); +nvidia_exporter for GPU (Phase 1); Phase 1 checklist expanded (8 → 10 steps); Architecture diagrams updated (both); Data flow expanded (6 → 9 steps); +Risk #8 (@RMN availability); +Related Documents (Prometheus, Grafana, Loki); FULL PRESERVE Phase 0-3 from v3.1.4.2 (L-097) |
| 3.1.4.2 | 2026-W09 | GTM_2026-W09_154 | GTM_2026-W09_158 | +Phase 0 (DO Infrastructure Observability — W10, no dependencies); +jAIMSnet brand identity (ISO 42001, 6 domains, GH org, ecosystem map); +Uptime Kuma REQUIRED (endpoint health monitoring); +Phase 0 deployment checklist (14 steps); +Phase 0 Docker Compose (Phoenix + Uptime Kuma); +Phase 0 #SmokeTest (10-point); +Phase 0 architecture diagram; +Phase 1 deployment checklist (migration from DO); +Risk #7 (GB10 delayed → Phase 0 covers); Infrastructure Quad reordered (Observe → position 2); Priority 🟠 P1 → 🔴 P0 (Phase 0); FULL PRESERVE Phase 1-3 content from v3.1.4.1 (L-097) |
| 3.1.4.1 | 2026-W09 | GTM_2026-W09_121 | GTM_2026-W09_122 | Initial project; Phoenix observability on GB10-1 #NoDe; BSD-3 FOSS; ~500 MB RAM; OTEL instrumentation (3 phases); LiteLLM integration (PRJ-016 endpoint); 6 dashboard views; 13-step deployment; Docker Compose; 6-point #SmokeTest; @MAIT:#Observability; 6-risk matrix; deploys BEFORE LiteLLM (infrastructure dependency) |

---

#FlowsBros #FedArch #Observability #Langfuse #OTEL #jAIMSnet #Prometheus #Grafana #Loki #FOSS #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
