# PRJ-016: AI Gateway — LiteLLM Deployment

## 📋 PRJ-016_AIGateway-LiteLLM_v3.1.4.1.md
## ♾️ WeOwnNet 🌐

| Field | Value |
|-------|-------|
| Document | PRJ-016_AIGateway-LiteLLM.md |
| Version | 3.1.4.1 |
| CCC-ID | GTM_2026-W09_117 |
| Created | 2026-02-27 (W09) |
| Season | #WeOwnSeason003 🚀 |
| Status | 📝 DRAFT |
| Lifecycle Stage | 📝 DRAFT (#DocLifecycle) |
| Tags | #AIGateway #LiteLLM #HybridArchitecture #FOSS #FlowsBros |

---

## 📖 Table of Contents

1. [Project Identity](#-project-identity)
2. [Why LiteLLM](#-why-litellm)
3. [Architecture](#-architecture)
4. [Provider Configuration](#-provider-configuration)
5. [Virtual Key Matrix](#-virtual-key-matrix)
6. [Cost Tracking + Budgets](#-cost-tracking--budgets)
7. [Rate Limiting](#-rate-limiting)
8. [Caching Strategy](#-caching-strategy)
9. [Failover Configuration](#-failover-configuration)
10. [Observability Pipeline](#-observability-pipeline)
11. [AnythingLLM Migration Plan](#-anythingllm-migration-plan)
12. [Deployment Checklist](#-deployment-checklist)
13. [Docker Compose](#-docker-compose)
14. [Verification (#SmokeTest)](#-verification-smoketest)
15. [ROI Impact](#-roi-impact)
16. [Project Team](#-project-team)
17. [@MAIT:#AIGateway Setup](#-maitaigateway-setup)
18. [Risk Matrix](#-risk-matrix)
19. [Relationship to Other Projects](#-relationship-to-other-projects)
20. [Discovered By](#-discovered-by)
21. [Related Documents](#-related-documents)
22. [Version History](#-version-history)

---

## 📋 Project Identity

| Field | Value |
|-------|-------|
| Project ID | **PRJ-016** |
| Title | **AI Gateway — LiteLLM Deployment** |
| Type | Infrastructure — AI Traffic Management |
| Priority | 🟠 P1 |
| Owner | @GTM + @RMN |
| Deployment | GB10-1 #NoDe (Northglenn, CO) |
| Timeline | **W12-W13** (after PRJ-015 GB10 arrives) |
| Depends on | PRJ-015 (GB10 hardware) |
| #masterCCC | GTM_2026-W09_117 |
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
| **No observability** | Blind to usage | ✅ OTEL → Phoenix traces |

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
INT-OG1 ──┼──→ LiteLLM Proxy (GB10-1 #NoDe) ──┼──→ Ollama → Llama 70B (dev)
INT-P02 ──┤    Port: 4000                      │
INT-OG8 ──┘    ├── Virtual Keys (per instance) ├──→ Ollama → Qwen3 4B (embed)
               ├── Redis Cache (semantic)       │
               ├── Cost Tracking (per-token)    └──→ [Future providers]
               ├── Rate Limiting (per-instance)
               ├── Failover (auto)
               └── OTEL → Phoenix (Port: 6006)

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
│  │  LiteLLM     │  │  Phoenix     │  │  Paperless   │  │
│  │  AI Gateway   │  │  Observability│  │  -ngx        │  │
│  │  Port: 4000   │  │  Port: 6006   │  │  Port: 8000  │  │
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

### LiteLLM Config (config.yaml)

```yaml
model_list:
  # Production — Claude Opus 4.6 via OpenRouter
  - model_name: claude-opus-production
    litellm_params:
      model: openrouter/anthropic/claude-opus-4-6
      api_key: os.environ/OPENROUTER_API_KEY
      api_base: https://openrouter.ai/api/v1

  # Development — Llama 3.1 70B via local Ollama
  - model_name: llama-70b-dev
    litellm_params:
      model: ollama/llama3.1:70b
      api_base: http://localhost:11434

  # Embedding — Qwen3 4B via local Ollama
  - model_name: qwen3-embedding
    litellm_params:
      model: ollama/qwen3:4b
      api_base: http://localhost:11434

  # Fallback — Llama via Ollama (if OpenRouter down)
  - model_name: claude-opus-production
    litellm_params:
      model: ollama/llama3.1:70b
      api_base: http://localhost:11434
    model_info:
      fallback: true

router_settings:
  routing_strategy: "least-busy"
  num_retries: 3
  timeout: 120
  fallbacks:
    - claude-opus-production: [llama-70b-dev]
```

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

```
LiteLLM ──→ OpenTelemetry SDK ──→ Phoenix (Port: 6006)
                                    ├── Traces (per request)
                                    ├── Spans (LLM call details)
                                    ├── Metrics (tokens, latency, cost)
                                    └── Dashboard (web UI)
```

### What Gets Traced

| Trace | Data |
|-------|------|
| LLM request | Model, provider, tokens in/out, latency, cost |
| Cache hit/miss | Similarity score, cache key, TTL |
| Failover event | Original provider, fallback provider, reason |
| Rate limit event | Instance, current rate, limit |
| Budget alert | Instance, current spend, budget |

### LiteLLM → Phoenix Config

```yaml
# In LiteLLM config
litellm_settings:
  callbacks: ["otel"]
  
environment_variables:
  OTEL_EXPORTER: "otlp_http"
  OTEL_ENDPOINT: "http://localhost:6006/v1/traces"
  OTEL_HEADERS: ""
```

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
| 7 | Verify: Check Phoenix | Trace visible |
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
| 1 | GB10-1 #NoDe operational | @GTM | PRJ-015 | ⬜ |
| 2 | Docker + Docker Compose installed | @GTM | Step 1 | ⬜ |
| 3 | Ollama installed + Llama 70B downloaded | @GTM | Step 2 | ⬜ |
| 4 | Create `litellm/` directory on GB10-1 | @GTM | Step 2 | ⬜ |
| 5 | Create `config.yaml` (provider routing) | @GTM | Step 4 | ⬜ |
| 6 | Create `docker-compose.yml` (LiteLLM + Redis) | @GTM | Step 4 | ⬜ |
| 7 | Set environment variables (OPENROUTER_API_KEY) | @GTM | Step 5 | ⬜ |
| 8 | `docker compose up -d` | @GTM | Steps 5-7 | ⬜ |
| 9 | Verify LiteLLM dashboard (port 4000) | @GTM | Step 8 | ⬜ |
| 10 | Create 5 virtual keys | @GTM | Step 9 | ⬜ |
| 11 | Configure budgets + rate limits | @GTM | Step 10 | ⬜ |
| 12 | Configure OTEL → Phoenix | @RMN | Step 9 | ⬜ |
| 13 | Test: curl to LiteLLM proxy | @GTM | Step 8 | ⬜ |
| 14 | Test: OpenRouter routing | @GTM | Step 13 | ⬜ |
| 15 | Test: Ollama routing | @GTM | Step 13 | ⬜ |
| 16 | Test: Failover (stop OpenRouter, verify Ollama) | @GTM | Step 14-15 | ⬜ |
| 17 | Test: Cache hit (repeat same request) | @GTM | Step 13 | ⬜ |
| 18 | Migrate INT-OG1 (test) | @GTM | Step 16-17 | ⬜ |
| 19 | Migrate INT-OG8 (test) | @RMN | Step 18 | ⬜ |
| 20 | Migrate INT-P01 (production) | @GTM | Step 19 | ⬜ |
| 21 | Migrate INT-S003 (production) | @GTM | Step 20 | ⬜ |
| 22 | Migrate INT-P02 (production) | @GTM | Step 21 | ⬜ |
| 23 | Verify ALL instances via LiteLLM dashboard | @GTM | Step 22 | ⬜ |
| 24 | Revoke old OpenRouter API keys | @GTM | Step 23 | ⬜ |
| 25 | Create @MAIT:#AIGateway | @GTM | Step 23 | ⬜ |
| 26 | FULL:SYNC:META | @GTM | Step 25 | ⬜ |

---

## 📋 Docker Compose

```yaml
# docker-compose.yml — LiteLLM + Redis on GB10-1 #NoDe
version: '3.8'

services:
  litellm:
    image: ghcr.io/berriai/litellm:main-latest
    container_name: litellm
    restart: unless-stopped
    ports:
      - "4000:4000"
    volumes:
      - ./config.yaml:/app/config.yaml
    environment:
      - LITELLM_MASTER_KEY=${LITELLM_MASTER_KEY}
      - OPENROUTER_API_KEY=${OPENROUTER_API_KEY}
      - LITELLM_LOG=DEBUG
      - REDIS_HOST=redis
      - REDIS_PORT=6379
      - OTEL_EXPORTER=otlp_http
      - OTEL_ENDPOINT=http://phoenix:6006/v1/traces
    command: ["--config", "/app/config.yaml", "--port", "4000"]
    depends_on:
      - redis

  redis:
    image: redis:7-alpine
    container_name: litellm-redis
    restart: unless-stopped
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    command: ["redis-server", "--maxmemory", "10gb", "--maxmemory-policy", "allkeys-lru"]

volumes:
  redis_data:
```

### Environment File (.env)

```bash
# .env — GB10-1 #NoDe
LITELLM_MASTER_KEY=sk-litellm-master-xxxx
OPENROUTER_API_KEY=sk-or-v1-xxxx
```

---

## 📋 Verification (#SmokeTest)

### LiteLLM #SmokeTest (8-Point)

| # | Test | Command | Expected | Status |
|---|------|---------|----------|--------|
| 1 | LiteLLM running | `curl http://localhost:4000/health` | `{"status": "healthy"}` | ⬜ |
| 2 | Redis running | `redis-cli ping` | `PONG` | ⬜ |
| 3 | OpenRouter route | `curl -X POST http://localhost:4000/v1/chat/completions -H "Authorization: Bearer vk-..." -d '{"model":"claude-opus-production",...}'` | Claude response | ⬜ |
| 4 | Ollama route | Same with `model: llama-70b-dev` | Llama response | ⬜ |
| 5 | Failover | Stop OpenRouter env, retry | Falls back to Ollama | ⬜ |
| 6 | Cache hit | Repeat identical request | Faster response + cache header | ⬜ |
| 7 | Cost tracked | Check LiteLLM dashboard | Request logged with cost | ⬜ |
| 8 | Phoenix trace | Check Phoenix UI (port 6006) | Trace visible | ⬜ |

---

## 📋 ROI Impact

### Cost Savings (From AI Gateway Analysis)

| Source | Monthly Savings | Annual Savings |
|--------|----------------|---------------|
| Semantic caching (30%) | $1,000 | $12,000 |
| Local inference (50%) | $1,667 | $20,000 |
| **COMBINED** | **$2,667** | **$32,000** |

### Revised PRJ-015 Payback (With LiteLLM)

| Metric | Without LiteLLM | With LiteLLM |
|--------|-----------------|-------------|
| Monthly savings | $1,667 (local only) | **$2,667** (local + cache) |
| GB10 payback | 4.7 months | **3.0 months** |
| Year 1 NET | +$11,802 | **+$23,802** |

### LiteLLM Cost

| Item | Cost |
|------|------|
| Software | **$0** (MIT — FOSS) |
| Infrastructure | $0 (runs on GB10-1 — already acquired) |
| Redis | $0 (Docker container) |
| **TOTAL LiteLLM cost** | **$0** |

> **$0 cost. $2,667/mo savings. The ROI is infinite.** 🏆

---

## 📋 Project Team

| CCC | Role | Focus |
|-----|------|-------|
| **GTM** | **Owner** | Architecture, config, migration, testing, @MAIT |
| **RMN** | **Platform** | LiteLLM config, Ollama routing, OTEL → Phoenix |

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
| **PRJ-014** | LiteLLM routes traffic for INT-P01 + INT-S003 (deployed in PRJ-014) |
| **PRJ-015** | LiteLLM deploys ON GB10-1 #NoDe (hardware from PRJ-015) |
| **PRJ-013** | Paperless-ngx co-located on GB10-1 (shared Docker host) |

### Project Dependency Chain

```
PRJ-015 (GB10 hardware)
    └── PRJ-016 (LiteLLM on GB10-1) ← THIS PROJECT
    └── PRJ-013 (Paperless-ngx on GB10-1)
    └── Phoenix (Observability on GB10-1)

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
| PRJ-015_HybridArchitecture-GB10 | v3.1.4.3 | GTM_2026-W09_104 | ⬜ @THY | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-015_HybridArchitecture-GB10.md) |
| SharedKernel | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/SharedKernel.md) |
| LiteLLM Docs | — | — | — | [docs.litellm.ai](https://docs.litellm.ai/) |
| Gartner AI Gateway Report | G00839683 | — | — | gartner.com |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| 3.1.4.1 | 2026-W09 | GTM_2026-W09_117 | GTM_2026-W09_119 | Initial project; LiteLLM AI Gateway deployment on GB10-1 #NoDe; 10 deliverables; provider config (OpenRouter + Ollama + Qwen3); virtual key matrix (5 instances); cost tracking + budgets; rate limiting; Redis semantic cache (20-40% savings); failover (OpenRouter → Ollama); OTEL → Phoenix observability; 5-instance migration plan; 26-step deployment checklist; Docker Compose (LiteLLM + Redis); 8-point #SmokeTest; ROI: $2,667/mo savings ($0 software cost); 8-risk matrix; @MAIT:#AIGateway setup |

---

#FlowsBros #FedArch #AIGateway #LiteLLM #HybridArchitecture #FOSS #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
