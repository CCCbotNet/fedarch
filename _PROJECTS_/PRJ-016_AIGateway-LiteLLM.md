# PRJ-016: AI Gateway — LiteLLM Deployment

## 📋 PRJ-016_AIGateway-LiteLLM_v3.2.1.1.md
## ♾️ WeOwnNet 🌐

| Field | Value |
|-------|-------|
| Document | PRJ-016_AIGateway-LiteLLM.md |
| Version | 3.2.1.1 |
| CCC-ID | GTM_2026-W10_122 |
| Created | 2026-02-27 (W09) |
| Updated | 2026-03-04 (W10) |
| Season | #WeOwnSeason003 🚀 |
| Status | ✅ APPROVED |
| Lifecycle Stage | ✅ APPROVED (#DocLifecycle) |
| Source of Truth | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-016_AIGateway-LiteLLM.md) |
| Tags | #LiteLLM #AIGateway #Langfuse #jAIMSnet #FOSS #FlowsBros |

---

## 📖 Table of Contents

1. [Project Identity](#-project-identity)
2. [Why LiteLLM](#-why-litellm)
3. [Timeline Acceleration — W10](#-timeline-acceleration--w10)
4. [Co-Location — jAIMSnet Droplet (ATL1)](#-co-location--jaimsnet-droplet-atl1)
5. [Architecture](#-architecture)
6. [Provider Configuration](#-provider-configuration)
7. [Virtual Key Matrix](#-virtual-key-matrix)
8. [Cost Tracking + Budgets](#-cost-tracking--budgets)
9. [Cost Impact](#-cost-impact)
10. [Rate Limiting](#-rate-limiting)
11. [Caching Strategy](#-caching-strategy)
12. [Failover Configuration](#-failover-configuration)
13. [Langfuse Integration (PRJ-017)](#-langfuse-integration-prj-017)
14. [AnythingLLM Migration Plan](#-anythingllm-migration-plan)
15. [Deployment Checklist](#-deployment-checklist)
16. [Docker Compose](#-docker-compose)
17. [Verification (#SmokeTest)](#-verification-smoketest)
18. [Project Team](#-project-team)
19. [@MAIT:#AIGateway Setup](#-maitaigateway-setup)
20. [Risk Matrix](#-risk-matrix)
21. [Relationship to Other Projects](#-relationship-to-other-projects)
22. [Discovered By](#-discovered-by)
23. [Related Documents](#-related-documents)
24. [Version History](#-version-history)

---

## 📋 Project Identity

| Field | Value |
|-------|-------|
| Project ID | **PRJ-016** |
| Title | **AI Gateway — LiteLLM** |
| Type | Infrastructure — AI Gateway |
| Priority | 🔴 **P0** (accelerated — cost emergency) |
| Owner | @RMN (platform) + @GTM (governance) |
| Deployment | **Phase 0: DO Droplet ATL1 (co-locate with Langfuse + Uptime Kuma)** |
| Domain | **litellm.jAIMS.app** |
| Timeline | **Phase 0: W10 (NOW — @RMN deploying)** |
| Depends on | None (Phase 0 = no dependencies) |
| Feeds into | PRJ-017 (Langfuse — via success_callback) |
| #masterCCC | GTM_2026-W10_122 |
| Selection | LiteLLM 🏆 (56/60 — AI Gateway Analysis GTM_2026-W09_115) |

---

## 📋 Why LiteLLM

### Selection Summary

| Field | Value |
|-------|-------|
| Product | [LiteLLM](https://docs.litellm.ai/) |
| License | **MIT** ✅ (FOSS — most permissive) |
| GitHub | [BerriAI/litellm](https://github.com/BerriAI/litellm) — **15K+ stars** |
| Language | Python |
| Score | **56/60** (vs Portkey 53, Traefik 38, TrueFoundry 37) |
| Key feature | **OpenAI-compatible proxy — drop-in for AnythingLLM** |
| Gartner category | Purpose-Built Open-Source AI Gateway (Table 4) |

### What LiteLLM Solves (Actual Problems)

| Problem | Current Pain | LiteLLM Solution |
|---------|-------------|------------------|
| **$5,249 in 91 days — no visibility** | Manual top-up tracking | ✅ Real-time cost dashboard |
| **API key incidents (×2 W09)** | Manual rotation (BP-064) | ✅ Centralized key vault |
| **Single provider dependency** | OpenRouter only | ✅ Multi-provider failover |
| **No caching** | Every request = API call | ✅ Semantic cache (20-40% reduction) |
| **No rate limiting** | Any instance burns unlimited | ✅ Per-instance budgets |
| **Cloud-only inference** | 100% OpenRouter | ✅ Route dev/test to local Ollama |
| **No observability** | Blind to usage | ✅ OTEL → Langfuse traces |

---

## 📋 Timeline Acceleration — W10

### Original Plan (v3.1.4.1)

| Phase | Timeline | Dependency |
|-------|----------|-----------|
| Deploy LiteLLM | W12-W13 | After GB10-1 (PRJ-015) |
| Connect to Phoenix | W12-W13 | After Phoenix deployed (PRJ-017) |

### Accelerated Plan (v3.2.1.1)

| Phase | Timeline | Dependency | Trigger |
|-------|----------|-----------|---------|
| **Deploy LiteLLM** | **W10 (NOW)** | **None** | **$372/day cost emergency** |
| **Connect to Langfuse** | **W10 (same deploy)** | **Co-located** | **Native callback** |

### What Changed

| Factor | v3.1.4.1 | v3.2.1.1 |
|--------|----------|----------|
| Deploy timeline | W12-W13 | **W10 (NOW)** |
| Dependency | GB10-1 (PRJ-015) | **None** |
| Observability | Phoenix (OTEL) | **Langfuse (native callback)** |
| Location | GB10-1 #NoDe | **ATL1 jAIMSnet Droplet** |
| Domain | N/A | **litellm.jAIMS.app** |
| Trigger | Planned | **$372/day cost emergency** |
| @RMN status | Planned | **DEPLOYING NOW** |

### Why Accelerated

| Fact | Value |
|------|-------|
| OpenRouter daily burn | **$372/day** |
| LiteLLM caching savings | **50-65% (~$130-185/day)** |
| MI300X approved but out of stock | LiteLLM = immediate savings |
| @THY directive | "Drop everything and do that right now" |
| @RMN status | "I'm ready to tackle this project" |

---

## 📋 Co-Location — jAIMSnet Droplet (ATL1)

### Architecture

```
DO Droplet (ATL1 — "jAIMSnet Observability")
├── LiteLLM (PRJ-016) — port 4000      ← THIS PROJECT
├── Langfuse (PRJ-017) — port 3000
├── Uptime Kuma (PRJ-017) — port 3001
├── Caddy (reverse proxy + SSL)
│   ├── litellm.jaims.app → :4000
│   ├── langfuse.jaims.app → :3000
│   └── kuma.jaims.app → :3001
└── PostgreSQL connection → ATL1 managed cluster
```

### Why Co-Locate

| Factor | Separate Droplets | Co-Located |
|--------|------------------|-----------|
| Cost | $18 + $18 = $36/mo | **$24/mo (1 Droplet)** |
| Latency (LiteLLM → Langfuse) | Network hop | **localhost (~0ms)** |
| Docker networking | Cross-host | **Same compose network** |
| Management | 2 Droplets | **1 Droplet** |

### Droplet Spec

| Field | Value |
|-------|-------|
| Region | ATL1 |
| Plan | Basic — 2 vCPU / 4 GB / 80 GB |
| Cost | **$24/mo** (shared with PRJ-017) |
| Services | LiteLLM + Langfuse + Uptime Kuma + Caddy |

---

## 📋 Architecture

### Before (Current)

```
INT-P01 ──→ OpenRouter API Key #1 ──→ Claude Opus 4.6
INT-S003──→ OpenRouter API Key #1 ──→ Claude Opus 4.6
INT-OG1 ──→ OpenRouter API Key #2 ──→ Claude Opus 4.6
INT-P02 ──→ OpenRouter API Key #3 ──→ Claude Opus 4.6
INT-OG8 ──→ OpenRouter API Key #4 ──→ Claude Opus 4.6

❌ Multiple API keys
❌ No visibility
❌ No caching
❌ No failover
❌ No rate limiting
```

### After (With LiteLLM)

```
INT-P01 ──┐                                    ┌──→ OpenRouter → Claude (prod)
INT-S003──┤                                    │
INT-OG1 ──┼──→ LiteLLM Proxy (ATL1) ──┼──→ Ollama → Llama 70B (dev)
INT-P02 ──┤    Port: 4000                      │
INT-OG8 ──┘    ├── Virtual Keys (per instance) ├──→ Ollama → Qwen3 4B (embed)
               ├── Redis Cache (semantic)       │
               ├── Cost Tracking (per-token)    └──→ [Future providers]
               ├── Rate Limiting (per-instance)
               ├── Failover (auto)
               └── OTEL → Langfuse (Port: 3000)

✅ Single control point
✅ One real API key (LiteLLM manages)
✅ Full visibility
✅ Caching
✅ Failover
✅ Rate limiting
✅ Observability
```

### GB10-1 #NoDe — Full Service Stack

```
GB10-1: #NoDe (Northglenn, CO)
┌─────────────────────────────────────────────────────────┐
│                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │  LiteLLM     │  │  Langfuse     │  │  Paperless   │  │
│  │  AI Gateway   │  │  Observability│  │  -ngx        │  │
│  │  Port: 4000   │  │  Port: 3000   │  │  Port: 8000  │  │
│  └──────┬───────┘  └──────────────┘  └──────────────┘  │
│         │                                                │
│  ┌──────┴───────┐  ┌──────────────┐  ┌──────────────┐  │
│  │  Ollama      │  │  Redis       │  │  AnythingLLM │  │
│  │  Local LLM    │  │  Cache       │  │  Local Dev    │  │
│  │  Llama 70B    │  │  Port: 6379   │  │  Port: 3001   │  │
│  │  Qwen3 4B     │  │              │  │              │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
│                                                          │
│  128 GB Unified | 2 TB NVMe | Ubuntu | Docker Compose   │
│  ~83 GB utilized (~65%) | Always-on | UPS protected     │
│  Services: 6 | Cost: ~$15/mo (power)                   │
└─────────────────────────────────────────────────────────┘
```

---

## 📋 Provider Configuration

### Routing Targets (3-Layer — PRJ-015)

| Layer | Provider | Model | Endpoint | Priority |
|-------|----------|-------|----------|----------|
| **1** | **MI300X (ATL1)** | Llama 3.1 70B | `http://mi300x.internal:8000` | 🔴 Primary (when available) |
| **2** | **GB10-1 (Ollama)** | Llama 3.1 70B | `http://gb10-1:11434` | Dev/test + backup |
| **3** | **OpenRouter** | Claude Opus 4.6 | `https://openrouter.ai/api/v1` | Fallback |

### LiteLLM config.yaml (Updated)

```yaml
model_list:
  # Layer 1: MI300X — Primary Production (ATL1)
  - model_name: llama-70b-production
    litellm_params:
      model: vllm/meta-llama/Llama-3.1-70B-Instruct
      api_base: http://mi300x.internal:8000

  # Layer 1: MI300X — Embedder
  - model_name: qwen3-embedding
    litellm_params:
      model: vllm/Qwen/Qwen3-Embedding-4B
      api_base: http://mi300x.internal:8000

  # Layer 2: GB10-1 — Dev/Test
  - model_name: llama-70b-dev
    litellm_params:
      model: ollama/llama3.1:70b
      api_base: http://gb10-1:11434

  # Layer 3: OpenRouter — Fallback
  - model_name: claude-opus-fallback
    litellm_params:
      model: openrouter/anthropic/claude-opus-4-6
      api_key: os.environ/OPENROUTER_API_KEY

router_settings:
  fallbacks:
    - llama-70b-production: [claude-opus-fallback]

litellm_settings:
  success_callback: ["langfuse"]
  cache: true
  cache_params:
    type: "redis"
    host: "redis"
    port: 6379

general_settings:
  master_key: os.environ/LITELLM_MASTER_KEY
```

### Interim Config (W10 — Before MI300X Available)

```yaml
model_list:
  # OpenRouter — Primary (interim)
  - model_name: claude-opus
    litellm_params:
      model: openrouter/anthropic/claude-opus-4-6
      api_key: os.environ/OPENROUTER_API_KEY

litellm_settings:
  success_callback: ["langfuse"]
  cache: true
  cache_params:
    type: "redis"
    host: "redis"
    port: 6379
```

> **Interim: LiteLLM → OpenRouter with caching + Langfuse tracing. Saves 50-65%.**
> **Full: LiteLLM → MI300X (primary) + OpenRouter (fallback) + Langfuse tracing. Saves 87%.**

### Provider Matrix

| Provider | Model | Use | Route |
|----------|-------|-----|-------|
| **OpenRouter** | Claude Opus 4.6 | Production (user-facing) | Cloud |
| **Ollama (local)** | Llama 3.1 70B | Development + fallback | GB10-1 |
| **Ollama (local)** | Qwen3 Embedding 4B | Embedding (all instances) | GB10-1 |
| **[Future]** | Any LiteLLM-supported | Expansion | Configurable |

---

## 📋 Virtual Key Matrix

### Per-Instance Keys

| Instance | Virtual Key Name | Model Access | Budget | Rate Limit |
|----------|-----------------|-------------|--------|------------|
| INT-P01 | `vk-int-p01` | claude-opus-production, llama-70b-dev | $50/day | 100 req/min |
| INT-S003 | `vk-int-s003` | claude-opus-production | $30/day | 60 req/min |
| INT-OG1 | `vk-int-og1` | claude-opus-production, llama-70b-dev | $40/day | 80 req/min |
| INT-P02 | `vk-int-p02` | claude-opus-production | $20/day | 40 req/min |
| INT-OG8 | `vk-int-og8` | claude-opus-production, llama-70b-dev | $20/day | 40 req/min |

### Key Management

| Aspect | Before | After |
|--------|--------|-------|
| Real API keys | 4+ (one per instance) | **1** (LiteLLM manages) |
| Key rotation | Manual per instance (BP-064) | **Rotate once in LiteLLM** |
| Key exposure | Each instance has real key | **Instances have virtual keys only** |
| Revocation | Per-instance | **Instant — revoke virtual key** |

---

## 📋 Cost Tracking + Budgets

### Dashboard Metrics

| Metric | Granularity | Purpose |
|--------|------------|---------|
| Token usage | Per-instance, per-model, per-day | Track consumption |
| Cost ($) | Per-instance, per-model, per-day | Budget enforcement |
| Cache hit rate | Global + per-instance | Measure savings |
| Request count | Per-instance, per-model | Usage patterns |

### Budget Configuration

| Level | Limit | Action When Exceeded |
|-------|-------|---------------------|
| Per-instance daily | $20-50/day | ⚠️ Alert → rate limit |
| Per-instance monthly | $600-1,500/mo | 🔴 Hard stop |
| Global daily | $150/day | ⚠️ Alert to @GTM |
| Global monthly | $3,500/mo | 🔴 Alert + review |

### Cost Alerts

| Alert | Threshold | Action |
|-------|-----------|--------|
| Instance approaching daily limit | 80% | Notify @GTM |
| Instance hit daily limit | 100% | Rate limit (not block) |
| Global approaching monthly | 80% | Notify @GTM + @THY |
| Unusual spike (2× normal) | Anomaly | Immediate alert |

---

## 📋 Rate Limiting

| Instance | Requests/min | Tokens/min | Rationale |
|----------|-------------|-----------|-----------|
| INT-P01 | 100 | 50,000 | Governance hub — high priority |
| INT-S003 | 60 | 30,000 | 6 contributors — moderate |
| INT-OG1 | 80 | 40,000 | @GTM + @THY — high usage |
| INT-P02 | 40 | 20,000 | BurnedOut — lower priority |
| INT-OG8 | 40 | 20,000 | @RMN — development |

> Rate limits = **soft limits** — requests queue, not reject. Prevents runaway costs without breaking user experience.

---

## 📋 Caching Strategy

### Redis Semantic Cache

| Field | Value |
|-------|-------|
| Engine | Redis |
| Type | Semantic caching (similarity-based) |
| Similarity threshold | 0.95 (high — only cache near-identical requests) |
| TTL | 24 hours (default) |
| Max cache size | 10 GB (on GB10-1 — 2 TB NVMe available) |
| Sensitive data | ❌ Do NOT cache PII or CCC-ID generation requests |

### Cache Rules

| Request Type | Cache? | Rationale |
|-------------|--------|-----------|
| RAG retrieval queries | ✅ YES | Same docs = same embeddings |
| General knowledge | ✅ YES | Repeated questions |
| CCC-ID generation | ❌ NO | Must be unique every time |
| #ContextVolley | ❌ NO | Unique context |
| VSA checks | ❌ NO | Must verify against current docs |
| SEEK:META | ❌ NO | Unique governance requests |

### Expected Impact

| Metric | Estimate |
|--------|----------|
| Cache hit rate (steady state) | 20-40% |
| Monthly savings (at $3,333/mo) | **$667-$1,333/mo** |
| Annual savings (cache alone) | **$8,000-$16,000/yr** |

---

## 📋 Failover Configuration

```yaml
# LiteLLM failover config
fallbacks:
  - claude-opus-production: [llama-70b-dev]

# Behavior:
# 1. Request → OpenRouter (Claude)
# 2. IF OpenRouter fails (timeout, 401, 429, 500)
# 3. THEN → Ollama (Llama 70B) on GB10-1 local
# 4. Response includes header: X-LiteLLM-Fallback: true
```

### Failover Matrix

| Trigger | Action | User Impact |
|---------|--------|-------------|
| OpenRouter timeout (>120s) | → Ollama Llama 70B | Slight quality difference |
| OpenRouter 401 (key expired) | → Ollama Llama 70B | ⚠️ Alert @GTM to rotate |
| OpenRouter 429 (rate limit) | → Ollama Llama 70B | Transparent |
| OpenRouter 500 (server error) | → Ollama Llama 70B | Transparent |
| Ollama down | → Error (no further fallback) | ❌ Manual intervention |

> **Incident #3 (W08) and #4 (W09) = would have been ZERO DOWNTIME with LiteLLM failover.**

---

## 📋 Observability Pipeline

### Langfuse Integration (PRJ-017)

| Field | Value |
|-------|-------|
| Tool | **Langfuse** (MIT) |
| Integration | **Native success_callback** |
| Setup time | **5 minutes** |
| Domain | **langfuse.jAIMS.app** |
| Co-located | ✅ Same Docker compose |

### Configuration

```yaml
litellm_settings:
  success_callback: ["langfuse"]

environment_variables:
  LANGFUSE_PUBLIC_KEY: "pk-lf-..."
  LANGFUSE_SECRET_KEY: "sk-lf-..."
  LANGFUSE_HOST: "http://langfuse:3000"  # Internal Docker network
```

### What Gets Traced (Automatically)

| Data | Source |
|------|--------|
| Model used | LiteLLM routing decision |
| Tokens (in/out) | LiteLLM |
| Cost ($) | LiteLLM cost tracking |
| Latency (ms) | LiteLLM |
| Cache hit/miss | LiteLLM cache |
| Failover events | LiteLLM routing |
| Instance | LiteLLM metadata |
| User | LiteLLM metadata |
| Full prompt/response | LiteLLM (self-hosted = safe) |

---

## 📋 AnythingLLM Migration Plan

### Per-Instance Migration

| # | Step | Detail |
|---|------|--------|
| 1 | Record current OpenRouter config | API key, model, base URL |
| 2 | Create virtual key in LiteLLM | `vk-int-<id>` |
| 3 | Update AnythingLLM LLM settings | Base URL → `http://<GB10-1-IP>:4000/v1` |
| 4 | Update AnythingLLM API key | → LiteLLM virtual key |
| 5 | Test: Send message in CCC workspace | Verify response |
| 6 | Verify: Check LiteLLM dashboard | Request logged + cost tracked |
| 7 | Verify: Check Langfuse | Trace visible |
| 8 | Done | Instance migrated ✅ |

### Migration Order

| Order | Instance | Priority | Rationale |
|-------|----------|----------|-----------|
| 1 | **INT-OG1** | 🟡 Test | @GTM's instance — test first |
| 2 | **INT-OG8** | 🟡 Test | @RMN's instance — verify |
| 3 | **INT-P01** | 🔴 Production | Governance hub — after testing |
| 4 | **INT-S003** | 🔴 Production | 6 contributors |
| 5 | **INT-P02** | 🟠 Production | BurnedOut |

> **Test on #HomeInstances first (INT-OG1, INT-OG8). Production after verified.**

### AnythingLLM Config Change

```
BEFORE:
  LLM Provider: OpenRouter
  API Base: https://openrouter.ai/api/v1
  API Key: sk-or-v1-xxxx (real OpenRouter key)
  Model: anthropic/claude-opus-4-6

AFTER:
  LLM Provider: OpenAI (compatible)
  API Base: http://<GB10-1-IP>:4000/v1
  API Key: sk-litellm-vk-int-p01 (virtual key)
  Model: claude-opus-production (LiteLLM model alias)
```

> **AnythingLLM thinks it's talking to OpenAI.** LiteLLM handles the routing. Zero AnythingLLM code changes.

---

## 📋 Deployment Checklist

| # | Step | Owner | Depends On | Status |
|---|------|-------|-----------|--------|
| 1 | 🤖 jAIMS Network 🌐 Project on DO We Own Labs TEAM created | @GTM | None | ⬜ |
| 2 | jAIMSnet Droplet provisioned (ATL1, 4 GB) | @RMN | Step 1 | ⬜ |
| 3 | Docker + Docker Compose installed | @RMN | Step 2 | ⬜ |
| 4 | Create litellm_config.yaml (interim — OpenRouter only) | @RMN | Step 3 | ⬜ |
| 5 | Deploy LiteLLM + Redis containers | @RMN | Step 4 | ⬜ |
| 6 | Configure DNS (litellm.jAIMS.app → Droplet) | @GTM | Step 2 | ⬜ |
| 7 | Configure Caddy entry for litellm.jAIMS.app | @RMN | Step 6 | ⬜ |
| 8 | Add Langfuse callback (3 env vars) | @RMN | PRJ-017 Langfuse running | ⬜ |
| 9 | Point INT-OG1 → litellm.jAIMS.app (test) | @RMN | Step 5 | ⬜ |
| 10 | Verify caching working (Redis) | @RMN | Step 9 | ⬜ |
| 11 | Verify Langfuse traces appearing | @GTM | Step 8 | ⬜ |
| 12 | Point ALL instances → litellm.jAIMS.app | @RMN | Step 10 + 11 | ⬜ |
| 13 | Monitor cost reduction (target: 50-65%) | @GTM | Step 12 | ⬜ |
| 14 | Add MI300X provider (when available) | @RMN | DO Sales + provisioning | ⬜ |
| 15 | #SmokeTest (10-point) | @GTM | Step 12 | ⬜ |
| 16 | FULL:SYNC:META | @GTM | Step 15 | ⬜ |

---

## 📋 Docker Compose

```yaml
# docker-compose.yml — LiteLLM (PRJ-016) on jAIMSnet Droplet
# Co-located with Langfuse + Uptime Kuma (PRJ-017)
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
      - LITELLM_MASTER_KEY=${LITELLM_MASTER_KEY}
      - REDIS_HOST=redis
      - REDIS_PORT=6379
    command: ["--config", "/app/config.yaml", "--port", "4000"]
    depends_on:
      - redis

  redis:
    image: redis:7-alpine
    container_name: redis
    restart: unless-stopped
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data

volumes:
  redis_data:
```

### Caddyfile Entry (Added to PRJ-017 Caddyfile)

```
litellm.jaims.app {
    reverse_proxy litellm:4000
}
```

> **LiteLLM + Redis = PRJ-016 services. Langfuse + Uptime Kuma + Caddy = PRJ-017 services. All in one Docker compose on jAIMSnet Droplet.**

---

## 📋 Verification (#SmokeTest)

## 📋 #SmokeTest (10-Point)

| # | Test | Expected | Status |
|---|------|----------|--------|
| 1 | LiteLLM running | https://litellm.jaims.app/health → 200 | ⬜ |
| 2 | LLM call via LiteLLM | Chat request → response | ⬜ |
| 3 | Caching working | Same prompt twice → 2nd = cache hit | ⬜ |
| 4 | Cost tracked | Langfuse shows $ per request | ⬜ |
| 5 | Langfuse trace | LLM call → trace in langfuse.jAIMS.app | ⬜ |
| 6 | Model routing | Request routes to correct provider | ⬜ |
| 7 | Failover | Block primary → falls back to secondary | ⬜ |
| 8 | Redis persistence | Restart Redis → cache retained | ⬜ |
| 9 | Master key auth | Request without key → 401 | ⬜ |
| 10 | Multi-instance | INT-OG1 + INT-P01 both route through LiteLLM | ⬜ |

---

## 📋 Cost Impact

### Interim (LiteLLM + OpenRouter — W10)

| Metric | Before LiteLLM | After LiteLLM |
|--------|---------------|--------------|
| Daily cost | $372/day | **~$130-185/day** |
| Monthly cost | $11,167/mo | **~$4,000-5,500/mo** |
| Savings | — | **50-65%** |
| Method | Direct API calls | **Caching + cost tracking** |

### Full (LiteLLM + MI300X — When Available)

| Metric | Before | After |
|--------|--------|-------|
| Daily cost | $372/day | **~$47/day** |
| Monthly cost | $11,167/mo | **~$1,433/mo** |
| Savings | — | **87%** |
| Method | OpenRouter only | **MI300X primary + OpenRouter fallback** |

### How LiteLLM Saves Money (Without GPU)

| Technique | Savings Est. |
|-----------|-------------|
| Prompt caching (Redis) | 20-40% |
| Response caching | 10-20% |
| Cost tracking → optimization | 5-10% |
| Rate limiting | 5-10% |
| **TOTAL** | **50-65%** |

---

## 📋 Project Team

| CCC | Role | Focus |
|-----|------|-------|
| **GTM** | **Owner** | Architecture, config, migration, testing, @MAIT |
| **RMN** | **Platform** | LiteLLM config, Ollama routing, OTEL → Langfuse |

> **2-person project.** No @SHD needed (GB10-1 is local, not cloud). No @LDC needed (no custom code).

---

## 📋 @MAIT:#AIGateway Setup

| Field | Value |
|-------|-------|
| Thread | MAIT_AIGateway |
| ShortCode | @MAIT:#AIGateway |
| Steward | @GTM |
| Instance | INT-P01 |
| Protocol | #ContextVolley |
| Tool Agent | t-aigateway_tool |
| Scope | LiteLLM (primary) + AI Gateway patterns + Portkey (reference) |

### RAG Documents

| # | Source | Depth |
|---|--------|-------|
| 1 | docs.litellm.ai | 2 |
| 2 | github.com/BerriAI/litellm (README) | 1 |

---

## 📋 Risk Matrix

| # | Risk | Prob | Impact | Mitigation |
|---|------|------|--------|------------|
| 1 | GB10-1 not ready (PRJ-015 delay) | Medium | High | Deploy on DO Droplet as interim |
| 2 | LiteLLM latency (proxy overhead) | Low | Medium | Benchmark; co-located = minimal |
| 3 | Redis cache corruption | Low | Low | Cache = optimization, not critical path |
| 4 | AnythingLLM incompatible with proxy | Low | High | OpenAI-compatible = well-tested |
| 5 | Ollama model quality < Claude | Known | Medium | Fallback only — production stays Claude |
| 6 | Virtual key management complexity | Low | Low | 5 instances = manageable |
| 7 | Network: cloud instances → GB10-1 | Medium | Medium | Benchmark latency; DO Droplet fallback |
| 8 | LiteLLM project abandoned | Low | Medium | MIT = fork; 15K stars = healthy |

---

## 📋 Relationship to Other Projects

| PRJ | Relationship |
|-----|-------------|
| **PRJ-015** | **3-Layer #HybridArchitecture — LiteLLM routes to MI300X (Layer 1) + GB10 (Layer 2) + OpenRouter (Layer 3)** |
| **PRJ-017** | **Langfuse — LiteLLM success_callback feeds ALL traces to langfuse.jAIMS.app; co-located on same Droplet** |
| **PRJ-002** | AgencyPRO — connexOmni/Athena inference routed through LiteLLM |
| PRJ-014 | All instances route through LiteLLM |
| PRJ-024 | Infisical manages LiteLLM API keys + secrets |

### Project Dependency Chain

```
PRJ-015 (GB10 hardware)
    └── PRJ-016 (LiteLLM on GB10-1) ← THIS PROJECT
    └── PRJ-013 (Paperless-ngx on GB10-1)
    └── Langfuse (Observability on GB10-1)

PRJ-014 (INT-S003 + INT-P01 evolution)
    └── PRJ-016 (LiteLLM routes traffic for both)
```

---

## 📋 Discovered By (BP-047)

| CCC | Contributor | Role | Context |
|-----|-------------|------|---------|
| GTM | [yonks](https://GitHub.com/YonksTEAM) | Co-Founder / Chief Digital Alchemist | Gartner AI Gateway Market Guide analysis + LiteLLM selection (56/60) — W09 |

---

## 📋 Related Documents

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| PRJ-015_HybridArchitecture | v3.2.1.1 | GTM_2026-W10_122 | GTM_2026-W10_125 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-015_HybridArchitecture.md) |
| PRJ-017_Observability | v3.2.1.1 | GTM_2026-W10_122 | GTM_2026-W10_161 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-017_Observability.md) |
| SharedKernel | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/SharedKernel.md) |
| LiteLLM Docs | — | — | — | [docs.litellm.ai](https://docs.litellm.ai) |
| LiteLLM GitHub | — | — | — | [github.com/BerriAI/litellm](https://github.com/BerriAI/litellm) |
| Gartner AI Gateway Report | G00839683 | — | — | gartner.com |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| 3.2.1.1 | 2026-W10 | GTM_2026-W10_122 | GTM_2026-W10_173 | Timeline accelerated W12-W13 → **W10** ($372/day cost emergency); deployment ATL1 jAIMSnet Droplet (co-locate with Langfuse + Uptime Kuma — PRJ-017); domain = litellm.jAIMS.app; Phoenix → **Langfuse** (native success_callback — replaces OTEL); +MI300X as routing target (PRJ-015 Layer 1); +Interim config (OpenRouter + caching — 50-65% savings); +Full config (MI300X primary + OpenRouter fallback — 87% savings); +Co-Location Architecture section; +Timeline Acceleration section; +Cost Impact section; Docker Compose updated (co-located + Redis); #SmokeTest updated (10-point); deployment checklist updated (16 steps); @RMN deploying NOW; FULL PRESERVE from v3.1.4.1 (L-097) |
| 3.1.4.1 | 2026-W09 | GTM_2026-W09_117 | GTM_2026-W09_119 | Initial project; LiteLLM AI Gateway on GB10-1; routing (OpenRouter + Ollama); caching (Redis); cost tracking; OTEL → Phoenix; Docker Compose; deployment checklist; #SmokeTest; risk matrix |

---

#FlowsBros #FedArch #AIGateway #LiteLLM #HybridArchitecture #FOSS #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
