# PRJ-015: #HybridArchitecture — 3-Layer AI Compute

## 📋 PRJ-015_HybridArchitecture_v3.2.1.1.md
## YonksTEAM LLC - Ventures - Series 4

| Field | Value |
|-------|-------|
| Document | PRJ-015_HybridArchitecture.md |
| Version | 3.2.1.1 |
| CCC-ID | GTM_2026-W10_122 |
| Created | 2026-02-27 (W09) |
| Updated | 2026-03-04 (W10) |
| Season | #WeOwnSeason003 🚀 |
| Status | ✅ APPROVED |
| Proposer | @GTM (Chief Digital Alchemist) |
| Approver | **@THY (CEO / CFO — YonksTEAM LLC)** |
| Entity | **YonksTEAM LLC - Ventures - Series 4** |
| Urgency | 🔴 **CRITICAL — $372/day burn, $134K/yr trajectory** |

---

## 📖 Table of Contents

1. [Executive Summary](#-executive-summary)
2. [The Cost Emergency — Actual Data](#-the-cost-emergency--actual-data)
3. [3-Layer Architecture](#-3-layer-architecture)
4. [Layer 1: Cloud GPU — DO MI300X](#-layer-1-cloud-gpu--do-mi300x)
5. [Layer 2: Edge GPU — Dell GB10](#-layer-2-edge-gpu--dell-gb10)
6. [Layer 3: Cloud LLM — OpenRouter (Fallback)](#-layer-3-cloud-llm--openrouter-fallback)
7. [Router: LiteLLM AI Gateway (PRJ-016)](#-router-litellm-ai-gateway-prj-016)
8. [3-Phase Migration Plan](#-3-phase-migration-plan)
9. [Model Evaluation Matrix](#-model-evaluation-matrix)
10. [MI300X Deployment Checklist](#-mi300x-deployment-checklist)
11. [GB10 2-Unit Strategy](#-gb10-2-unit-strategy)
12. [GB10 Use Cases](#-gb10-use-cases)
13. [ROI Analysis — Actual Data](#-roi-analysis--actual-data)
14. [Budget](#-budget)
15. [GB10 Implementation Plan](#-gb10-implementation-plan)
16. [Risk Analysis](#-risk-analysis)
17. [Approvals](#-approvals)
18. [Recommendation](#-recommendation)
19. [Related Documents](#-related-documents)
20. [Version History](#-version-history)

---

## 📋 Executive Summary

### The Problem

We have spent **$7,277 on OpenRouter API** since November 2025. March 2026 burn rate = **$372/day ($11,167/mo projected)**. This is **3.5× February** and still accelerating. At current trajectory: **$134,000+/year** on cloud AI inference.

### The Solution

**3-Layer #HybridArchitecture** — move the majority of AI inference off OpenRouter using a combination of cloud GPU (DigitalOcean MI300X) and edge GPU (Dell GB10).

### The 3 Layers

| Layer | Component | Cost | Role |
|-------|-----------|------|------|
| **1** | **DO MI300X (ATL1)** | **$1,433/mo** | **Primary production inference** |
| **2** | **Dell GB10 ×2** | **$7,898 (one-time)** | Dev/test + demos + backup |
| **3** | **OpenRouter (reduced)** | **$0-3,350/mo** | Fallback + quality benchmark |
| **—** | **LiteLLM (PRJ-016)** | **$0** | Routes all traffic |

### The Math

| Scenario | Monthly | Annual | vs Current |
|----------|---------|--------|-----------|
| **Current (OpenRouter only)** | **$11,167** | **$134,000** | — |
| **A: MI300X + OpenRouter** | $4,783 | $57,396 | **-$76,604** |
| **B: MI300X + GB10 + OpenRouter** | $3,995 | $51,894 | **-$82,106** |
| **C: MI300X + GB10 only** | $1,762 | $25,094 | **-$108,906** |

### The Approval

| Field | Value |
|-------|-------|
| MI300X approved by | **@THY (CEO / CFO)** |
| Date | **Wed 04 Mar 2026, ~10:33 MST** |
| Quote | **"Drop everything and do that right now plz"** |
| CCC-ID | GTM_2026-W10_125 |

---

## 📋 The Cost Emergency — Actual Data

### OpenRouter Credit History (All-Time)

| # | Date | Amount | Running Total |
|---|------|--------|---------------|
| 1 | Nov 26, 2025 | $500 | $500 |
| 2 | Jan 9, 2026 | $1,000 | $1,500 |
| 3 | Jan 18, 2026 | $777 | $2,277 |
| 4 | Feb 1, 2026 | $500 | $2,777 |
| 5 | Feb 7, 2026 | $500 | $3,277 |
| 6 | Feb 10, 2026 | $500 | $3,777 |
| 7 | Feb 15, 2026 | $500 | $4,277 |
| 8 | Feb 17, 2026 | $500 | $4,777 |
| 9 | Feb 24, 2026 | $500 | $5,277 |
| 10 | Feb 27, 2026 | $500 | $5,777 |
| 11 | Mar 01, 2026 | $500 | $6,277 |
| 12 | Mar 03, 2026 | $500 | $6,777 |
| 13 | Mar 04, 2026 | $500 | $7,277 |
| | **TOTAL PURCHASED** | **$7,277** | |
| | **TOTAL CONSUMED** | **~$6,766** | |

### Burn Rate Acceleration

| Period | Spend | Daily Rate | Monthly Rate | vs Baseline |
|--------|-------|-----------|-------------|-------------|
| Nov-Dec 2025 | ~$500 | ~$8/day | ~$250/mo | Baseline |
| Jan 2026 | ~$1,777 | ~$57/day | ~$1,777/mo | **7×** |
| Feb 2026 | ~$3,000 | ~$107/day | ~$3,333/mo | **13×** |
| **Mar 1-4 (4 days)** | **~$1,489** | **$372/day** | **$11,167/mo** | **46×** |

```
DAILY BURN RATE:

Nov:  $8      █
Jan:  $57     ███████
Feb:  $107    █████████████
Mar:  $372    █████████████████████████████████████████████████
```

### What's Driving the Acceleration

| Driver | Impact |
|--------|--------|
| More instances | INT-E01, INT-OG8, INT-S003 (deploying) |
| More contributors | @CEO, @LFG, @SHD active |
| More MAIT threads | 5+ active MAITs |
| ChatHistory = 40 | 2× context per request (BP-061) |
| More governance | VSAs, cascades, doc generation — token-heavy |
| Claude Opus 4.6 | Premium model — highest cost per token |
| W10 Day 2 | 82 CCC-IDs, 1,077 VSA checks, 8 docs, 16 SEEK:METAs |

### The Absurdity

| Action | Cost | Lasts |
|--------|------|-------|
| OpenRouter $500 top-up | $500 | ~1.3 days |
| OpenRouter $500 top-up | $500 | ~1.3 days |
| OpenRouter $500 top-up | $500 | ~1.3 days |
| **MI300X (entire month)** | **$1,433** | **30 days** |

> **3 top-ups ($1,500) = 4 days. MI300X ($1,433) = 30 days.** We pay more for 4 days of OpenRouter than an entire month of dedicated GPU.

---

## 📋 3-Layer Architecture

```
┌──────────────────────────────────────────────────────────┐
│  LAYER 1: CLOUD GPU — DO MI300X (ATL1)          🆕 NEW   │
│  $1,433/mo | 192 GB VRAM | <2ms to all instances         │
│  ├── Llama 3.1 70B (production)                          │
│  ├── Qwen3 Embedding 4B (all instances)                  │
│  └── Qwen3 72B (alternative — Phase 2)                   │
│  Role: PRIMARY PRODUCTION INFERENCE                       │
├──────────────────────────────────────────────────────────┤
│  LAYER 2: EDGE GPU — Dell GB10 ×2 ($7,898)    EXISTING   │
│  ├── GB10-1 #NoDe (Northglenn, 24/7)                    │
│  │   └── Paperless-ngx, embedding, local LLM, backup    │
│  └── GB10-2 Portable (demos, travel)                     │
│      └── Live demos, FL ops, offline inference           │
│  Role: DEV/TEST + DEMOS + BACKUP                         │
├──────────────────────────────────────────────────────────┤
│  LAYER 3: CLOUD LLM — OpenRouter (REDUCED)    CHANGED    │
│  ├── Claude Opus 4.6 (fallback only)                     │
│  └── $0-3,350/mo (down from $11,167)                    │
│  Role: FALLBACK + QUALITY BENCHMARK                      │
├──────────────────────────────────────────────────────────┤
│  ROUTER: LiteLLM AI Gateway (PRJ-016)         EXISTING   │
│  Routes ALL traffic → Layer 1/2/3 based on rules          │
│  Cost tracking, caching, failover                         │
└──────────────────────────────────────────────────────────┘

         ▲              ▲              ▲
         │              │              │
┌────────┴──┐  ┌───────┴────┐  ┌─────┴──────┐
│  INT-P01  │  │  INT-P05   │  │  INT-S003  │
│  INT-P02  │  │  INT-P03   │  │  INT-OG1   │
│  INT-P04  │  │  INT-VSA   │  │  INT-OG8   │
└───────────┘  └────────────┘  └────────────┘
```

### Layer Roles — When to Use What

| Workload | Layer | Model | Why |
|----------|-------|-------|-----|
| **Production CCC-IDs** | Layer 1 (MI300X) | Llama 70B | Low latency, <2ms |
| **SEEK:META** | Layer 1 (MI300X) | Llama 70B | Standard governance |
| **VSA** | Layer 1 (MI300X) | Llama 70B | Batch verification |
| **Embedding** | Layer 1 (MI300X) | Qwen3 4B | All instances |
| **Dev/test** | Layer 2 (GB10) | Llama 70B | Free inference |
| **Live demos** | Layer 2 (GB10-2) | Llama 70B | Offline capable |
| **Quality benchmark** | Layer 3 (OpenRouter) | Claude Opus 4.6 | Comparison only |
| **Fallback** | Layer 3 (OpenRouter) | Claude Opus 4.6 | If MI300X down |

---

## 📋 Layer 1: Cloud GPU — DO MI300X

### Specifications

| Field | Value |
|-------|-------|
| GPU | **AMD MI300X** |
| VRAM | **192 GB** |
| Provider | DigitalOcean |
| Region | **ATL1** (same DC as all instances) |
| Cost | **$1.99/hr = $1,433/mo** |
| Latency | **<2ms** (same VPC) |
| Bandwidth | **FREE** (internal DO network) |
| Billing | Unified DO billing |
| Cancel | Anytime (hourly billing) |

### Why MI300X (vs Alternatives)

| Provider | GPU | VRAM | Cost/mo | Verdict |
|----------|-----|------|---------|---------|
| **DO MI300X** | MI300X | **192 GB** | **$1,433** | ✅ **Best value + same DC** |
| DO H100 (1x) | H100 | 80 GB | $1,483 | 🟡 Less VRAM, similar price |
| DO H100 (2x) | H100 ×2 | 160 GB | $2,966 | ❌ 2× price for less VRAM |
| Latitude H100 VM | H100 | 80 GB | $1,195 | 🟡 Cheaper but separate network |
| Latitude H100 ×2 | H100 ×2 | 160 GB | $2,390 | ❌ More expensive, separate network |

> **MI300X wins on VRAM/$ AND same-datacenter advantage.** 192 GB fits 3-4 models. Same VPC = <2ms latency + free bandwidth.

### @RMN Analysis (24 Feb 2026 — Signal)

> *"MI300X on DO was the recommendation because we can deploy on ATL1 and it has the best value of DO's GPU options. It has 192GB for $1.99/hr ($1,433/mo), which fits 3-4 of our target models plus the embedder on a single GPU. That lets the gateway route different questions to different models all on one machine."*

### Models on MI300X

| Model | Parameters | VRAM (est.) | Purpose | Priority |
|-------|-----------|-------------|---------|----------|
| **Llama 3.1 70B** | 70B | ~80 GB | Primary production LLM | 🔴 P0 |
| **Qwen3 Embedding 4B** | 4B | ~8 GB | Embedder (all instances) | 🔴 P0 |
| **Qwen3 72B** | 72B | ~85 GB | Alternative LLM (Phase 2) | 🟠 P1 |
| DeepSeek V3 | 671B MoE | ~120 GB | Evaluation (quantized) | 🟡 P2 |

**Day 1 deployment:**

| Model | VRAM | Cumulative | Remaining |
|-------|------|-----------|-----------|
| Llama 3.1 70B | ~80 GB | 80 GB | 112 GB |
| Qwen3 Embedding 4B | ~8 GB | 88 GB | **104 GB free** |

### LiteLLM Config (Layer 1)

```yaml
model_list:
  # MI300X — Primary Production (ATL1)
  - model_name: llama-70b-production
    litellm_params:
      model: vllm/meta-llama/Llama-3.1-70B-Instruct
      api_base: http://mi300x.internal:8000

  # MI300X — Embedder
  - model_name: qwen3-embedding
    litellm_params:
      model: vllm/Qwen/Qwen3-Embedding-4B
      api_base: http://mi300x.internal:8000

router_settings:
  fallbacks:
    - llama-70b-production: [claude-opus-fallback]
```

---

## 📋 Layer 2: Edge GPU — Dell GB10

### Product Specification

| Field | Value |
|-------|-------|
| Manufacturer | Dell |
| Model | FCM1253 |
| Form Factor | **Micro** (smaller than a shoebox) |
| Chip | **NVIDIA GB10 Grace Blackwell Superchip** |
| GPU | Blackwell-class (integrated — 1 PFLOPS AI) |
| CPU | ARM Cortex-A725 (efficiency) + Cortex-X925 (performance) |
| Memory | **128 GB unified** (CPU + GPU shared) |
| Storage | **2 TB NVMe SSD** |
| Connectivity | WiFi 7, Bluetooth 5.4, USB-C, HDMI, Ethernet |
| OS | Ubuntu Linux (pre-installed) |
| Power | ~150W TDP |
| Vendor | [CDW.com](https://www.cdw.com/product/dell-pro-max-with-gb10-fcm1253-micro-gb10-grace-blackwell-superchip-corte/9063421) |

### What 128 GB Unified Memory Runs

| Model | Parameters | Memory | Fits? |
|-------|-----------|--------|-------|
| Llama 3.1 8B | 8B | ~16 GB | ✅ |
| Llama 3.1 70B | 70B | ~80 GB | ✅ |
| Mixtral 8x7B | 47B | ~48 GB | ✅ |
| Qwen3 72B | 72B | ~85 GB | ✅ |
| DeepSeek V3 | 671B (MoE) | ~120 GB | ⚠️ Tight |

---

## 📋 Layer 3: Cloud LLM — OpenRouter (Fallback)

### Reduced Role

| Aspect | Before (v3.1.4.3) | After (v3.2.1.1) |
|--------|-------------------|-------------------|
| Role | **PRIMARY** — all inference | **FALLBACK** — if MI300X down |
| Cost | $11,167/mo | **$0-3,350/mo** |
| Model | Claude Opus 4.6 | Claude Opus 4.6 (unchanged) |
| Usage | 100% of traffic | **0-30% of traffic** |

### When OpenRouter Is Used

| Scenario | Use OpenRouter? |
|----------|----------------|
| MI300X operational | ❌ No — MI300X handles all |
| MI300X down | ✅ Yes — automatic failover via LiteLLM |
| Quality benchmark | ✅ Yes — periodic Claude vs Llama comparison |
| Phase 1 (W10-W11) | ✅ Yes — production while MI300X evaluated |

---

## 📋 Router: LiteLLM AI Gateway (PRJ-016)

### How LiteLLM Routes Traffic

```
ALL INSTANCES → LiteLLM (PRJ-016) → Routes to:
  ├── MI300X (ATL1) → Llama 70B (primary)        ← Layer 1
  ├── MI300X (ATL1) → Qwen3 4B (embedding)       ← Layer 1
  ├── GB10-1 → Ollama → Llama 70B (dev/test)     ← Layer 2
  ├── GB10-2 → Ollama → Llama 70B (demos)        ← Layer 2
  └── OpenRouter → Claude Opus 4.6 (fallback)    ← Layer 3
```

### Routing Rules

| Rule | Condition | Route To |
|------|-----------|----------|
| Default | All production traffic | Layer 1 (MI300X) |
| Embedding | All embedding requests | Layer 1 (MI300X — Qwen3 4B) |
| Dev/test | INT-OG1 dev workspace | Layer 2 (GB10-1) |
| Demo | INT-E0x event instances | Layer 2 (GB10-2) |
| Fallback | MI300X unavailable | Layer 3 (OpenRouter) |
| Benchmark | Periodic quality test | Layer 3 (OpenRouter) |

---

## 📋 3-Phase Migration Plan

| Phase | OpenRouter Role | MI300X Role | GB10 Role | Timeline |
|-------|----------------|-------------|-----------|----------|
| **1: Hybrid** | Production (Claude) | Dev/test (Llama) | Not yet deployed | **W10-W11** |
| **2: Evaluate** | Reduced (30%) | Production (Llama evaluated) | Dev/test | **W12-W13** |
| **3: Decide** | Fallback or eliminated | Primary production | Dev/test + demos + backup | **W14+** |

### Phase 1: Hybrid (W10-W11)

| Action | Owner | Status |
|--------|-------|--------|
| Provision MI300X (ATL1) | @RMN | ⬜ **THIS WEEK** |
| Install vLLM | @RMN | ⬜ |
| Download Llama 70B + Qwen3 4B | @RMN | ⬜ |
| Route dev/test to MI300X | @RMN | ⬜ |
| Production stays on OpenRouter | — | ✅ |
| Benchmark Llama vs Claude | @GTM | ⬜ |

### Phase 2: Evaluate (W12-W13)

| Action | Owner |
|--------|-------|
| Route 70% production to MI300X | @RMN |
| Keep 30% on OpenRouter (comparison) | @RMN |
| Run evaluation matrix (see below) | @GTM |
| GB10 arrives — deploy Layer 2 | @GTM |

### Phase 3: Decide (W14+)

| Outcome | Action |
|---------|--------|
| Llama quality ≥ 95% of Claude | Eliminate OpenRouter (Option C) |
| Llama quality 80-95% | Keep OpenRouter for critical ops (Option A/B) |
| Llama quality < 80% | Keep OpenRouter as primary, MI300X for dev/embed (recalculate) |

---

## 📋 Model Evaluation Matrix

### Phase 2 Testing Protocol

| Test | Pass Criteria | Method |
|------|--------------|--------|
| CCC-ID format compliance | 100% (R-168, R-169) | Generate 50 CCC-IDs, verify format |
| VSA accuracy (DEEP FULL) | ≥ 95% match with Claude | Run same VSA on both, compare |
| Governance doc generation | Quality comparable | SEEK:META on both, blind compare |
| #ContextVolley format | 100% compliance | Generate 10 volleys, verify format |
| Response quality | No #AIslop degradation | Blind review by @GTM + @THY |
| Context retention | ChatHistory 40 = functional | Test 40-message context |
| Table formatting | Tables render correctly | Verify markdown tables |
| Rule compliance | All immutable rules followed | Spot-check R-011, R-194, R-197, R-206 |

### Scoring

| Score | Meaning | Action |
|-------|---------|--------|
| ≥ 95% | Excellent | ✅ Eliminate OpenRouter |
| 80-95% | Good | 🟡 Keep OpenRouter for critical ops |
| < 80% | Insufficient | 🔴 Recalculate — MI300X for dev/embed only |

---

## 📋 MI300X Deployment Checklist

| # | Step | Owner | Timeline | Status |
|---|------|-------|----------|--------|
| 1 | @THY approves MI300X ($1,433/mo) | @THY | ✅ **DONE** (GTM_2026-W10_125) | ✅ |
| 2 | Provision MI300X Droplet (ATL1) | @RMN | **W10 (Thu-Fri)** | ⬜ |
| 3 | Install vLLM (or Ollama) | @RMN | W10 | ⬜ |
| 4 | Download Llama 3.1 70B (~40 GB) | @RMN | W10 | ⬜ |
| 5 | Download Qwen3 Embedding 4B (~8 GB) | @RMN | W10 | ⬜ |
| 6 | Benchmark inference (tokens/sec) | @RMN | W10 | ⬜ |
| 7 | Configure LiteLLM routing (PRJ-016) | @RMN | W10-W11 | ⬜ |
| 8 | Route dev/test traffic to MI300X | @RMN | W11 | ⬜ |
| 9 | Route production traffic (gradual) | @RMN | W11 | ⬜ |
| 10 | Reduce OpenRouter to fallback | @GTM | W11 | ⬜ |
| 11 | Begin Phase 2 evaluation | @GTM | W12 | ⬜ |

---

## 📋 GB10 2-Unit Strategy

### Unit Profiles

| Unit | Name | Location | Mode | Role |
|------|------|----------|------|------|
| **GB10-1** | **#NoDe** | Northglenn, CO | Always-on (24/7) | Infrastructure services |
| **GB10-2** | **Portable** | Roams with YonksTEAM | On-demand | Demos, travel, FL ops |

### GB10-1: #NoDe (Northglenn, CO)

| Service | Detail |
|---------|--------|
| **Paperless-ngx** | PRJ-013 — always-on document management |
| **Embedding server** | Qwen3 4B — backup to MI300X |
| **Local LLM** | Llama 70B / Qwen3 72B — dev/test inference |
| **AnythingLLM (local)** | Local dev/test instance |
| **Docker host** | Multiple containers simultaneously |
| **Backup inference** | Failover if MI300X + OpenRouter both down |

### GB10-2: Portable (Roams)

| Service | Detail |
|---------|--------|
| **Live demos** | Local AI inference at events — no internet needed |
| **Central Florida ops** | @GTM mobile office — full AI capability |
| **Event deployments** | Power instances locally |
| **Client presentations** | Demo #FedArch + CCC to partners |
| **@GTM mobile lab** | Development anywhere |
| **Offline inference** | Full AI with zero internet |

---

## 📋 GB10 Use Cases

### GB10-1: #NoDe (6 Use Cases)

| # | Use Case | Priority | Value |
|---|----------|----------|-------|
| 1 | Embedding server (backup) | 🟠 P1 | Redundancy for MI300X |
| 2 | Paperless-ngx (PRJ-013) | 🔴 P0 | Saves $18/mo Droplet |
| 3 | Local LLM (dev/test) | 🟠 P1 | Free dev inference |
| 4 | @RMN dev environment | 🟠 P1 | Free dev inference |
| 5 | Backup inference | 🟡 P2 | Resilience (Layer 2 backup) |
| 6 | Fine-tuning | 🟡 P2 | New capability |

### GB10-2: Portable (6 Use Cases)

| # | Use Case | Priority | Value |
|---|----------|----------|-------|
| 7 | Live demos (events) | 🔴 P0 | No venue WiFi dependency |
| 8 | Central Florida ops | 🔴 P0 | Full AI on the road |
| 9 | Event deployments | 🟠 P1 | Local event instances |
| 10 | Client presentations | 🟠 P1 | Demo capability |
| 11 | @GTM mobile lab | 🟠 P1 | Dev anywhere |
| 12 | Offline inference | 🟡 P2 | Zero-internet AI |

---

## 📋 ROI Analysis — Actual Data

### Cost Comparison — All Scenarios

| Scenario | Monthly | Annual | vs Current |
|----------|---------|--------|-----------|
| **Current (OpenRouter only)** | **$11,167** | **$134,000** | — |
| **A: MI300X + OpenRouter (30%)** | $4,783 | $57,396 | **-$76,604** |
| **B: MI300X + GB10 + OpenRouter (20%)** | $3,995 | $51,894 | **-$82,106** |
| **C: MI300X + GB10 (no OpenRouter)** | $1,762 | $25,094 | **-$108,906** |

### Scenario A: MI300X + OpenRouter (Hybrid)

| Component | Monthly | Annual |
|-----------|---------|--------|
| MI300X (ATL1) | $1,433 | $17,196 |
| OpenRouter (30% — production fallback) | $3,350 | $40,200 |
| **TOTAL** | **$4,783** | **$57,396** |
| **SAVINGS** | **$6,384/mo** | **$76,604/yr** |

### Scenario B: MI300X + GB10 + OpenRouter (Full Hybrid)

| Component | Monthly | Annual |
|-----------|---------|--------|
| MI300X (ATL1) | $1,433 | $17,196 |
| GB10 ×2 (amortized 24mo) | $329 | $7,898 |
| OpenRouter (20%) | $2,233 | $26,800 |
| **TOTAL** | **$3,995** | **$51,894** |
| **SAVINGS** | **$7,172/mo** | **$82,106/yr** |

### Scenario C: MI300X + GB10 Only (No OpenRouter)

| Component | Monthly | Annual |
|-----------|---------|--------|
| MI300X (ATL1) | $1,433 | $17,196 |
| GB10 ×2 (amortized 24mo) | $329 | $7,898 |
| OpenRouter | $0 | $0 |
| **TOTAL** | **$1,762** | **$25,094** |
| **SAVINGS** | **$9,405/mo** | **$108,906/yr** |

### Payback Periods

| Investment | Cost | Payback (at $372/day savings) |
|-----------|------|-------------------------------|
| MI300X (first month) | $1,433 | **3.9 days** |
| GB10 ×2 | $7,898 | **21 days** |
| **Combined** | $9,331 | **25 days** |

### 2-Year Financial Impact

| Scenario | Year 1 | Year 2 | 2-Year Total Savings |
|----------|--------|--------|---------------------|
| A (MI300X + OR) | $76,604 | $76,604 | **$153,208** |
| B (MI300X + GB10 + OR) | $74,208 | $82,106 | **$156,314** |
| **C (MI300X + GB10)** | **$101,008** | **$108,906** | **$209,914** |

---

## 📋 Budget

### Hardware (One-Time)

| Item | Qty | Unit Cost | Total |
|------|-----|-----------|-------|
| Dell Pro Max GB10 (FCM1253) | 2 | ~$3,799 | ~$7,598 |
| UPS — #NoDe (APC 600VA) | 1 | ~$100 | ~$100 |
| Travel case — Portable | 1 | ~$100 | ~$100 |
| **TOTAL HARDWARE** | | | **~$7,898** |

### Monthly (Ongoing)

| Item | Monthly |
|------|---------|
| **MI300X (ATL1)** | **$1,433** |
| Electricity — #NoDe (24/7) | ~$10-15 |
| Electricity — Portable (on-demand) | ~$5-10 |
| OpenRouter (fallback — Scenario B) | ~$2,233 |
| **TOTAL MONTHLY (Scenario B)** | **~$3,681-3,691** |

### Purchasing Entity

| Field | Value |
|-------|-------|
| Entity | **YonksTEAM LLC - Ventures - Series 4** |
| GB10 tax treatment | **Section 179 — deduct full ~$7,898 in Year 1** |
| MI300X tax treatment | Operating expense (monthly) |

---

## 📋 GB10 Implementation Plan

### Phase 1: Acquire + Setup #NoDe (After MI300X — W11-W12)

| # | Step | Owner |
|---|------|-------|
| 1 | Order 2 units from CDW | @GTM |
| 2 | Receive + unbox #NoDe | @GTM |
| 3 | Ubuntu verified | @GTM |
| 4 | Install Docker + Ollama | @GTM / @RMN |
| 5 | Download Llama 3.1 70B + Qwen3 4B | @GTM |
| 6 | Deploy Paperless-ngx on #NoDe | @GTM |
| 7 | Configure as Layer 2 backup in LiteLLM | @RMN |
| 8 | Connect UPS | @GTM |
| 9 | #SmokeTest #NoDe | @GTM |

### Phase 2: Setup Portable (W12-W13)

| # | Step | Owner |
|---|------|-------|
| 10 | Unbox Portable | @GTM |
| 11 | Mirror #NoDe config | @GTM |
| 12 | Test WiFi 7 + hotspot | @GTM |
| 13 | Travel case + accessories | @GTM |
| 14 | #SmokeTest Portable | @GTM |

---

## 📋 Risk Analysis

| # | Risk | Prob | Impact | Mitigation |
|---|------|------|--------|------------|
| 1 | MI300X availability (ATL1) | Low | High | @RMN confirmed available; hourly cancel |
| 2 | Llama quality < Claude | Medium | Medium | Phase 2 evaluation; OpenRouter fallback |
| 3 | MI300X latency issues | Low | Medium | Same VPC (<2ms); benchmark before production |
| 4 | GB10 shipping delay | Medium | Low | MI300X = primary; GB10 = Layer 2 (not urgent) |
| 5 | OpenRouter elimination premature | Low | Medium | Phase 3 = data-driven decision |
| 6 | vLLM compatibility | Low | Medium | @RMN experienced; Ollama as alternative |
| 7 | DO billing surprise | Low | Medium | Hourly billing = predictable; set alerts |
| 8 | Model quality degradation | Low | Medium | Periodic benchmark vs Claude (Phase 2+) |

---

## 📋 Approvals

| # | Item | Approver | Date | CCC-ID |
|---|------|---------|------|--------|
| 1 | GB10 ×2 ($7,898) | @THY | W09 | GTM_2026-W09_104 |
| 2 | **MI300X ($1,433/mo)** | **@THY** | **Wed 04 Mar 2026** | **GTM_2026-W10_125** |

> **@THY quote:** *"Drop everything and do that right now plz"*

---

## 📋 Recommendation

**Deploy MI300X THIS WEEK (W10). GB10 follows (W11-W12). Evaluate Llama quality (W12-W13). Decide on OpenRouter elimination (W14+).**

| Priority | Action | Timeline |
|----------|--------|----------|
| 🔴 **#1** | **MI300X provisioned + Llama running** | **W10 (Thu-Fri)** |
| 🔴 #2 | LiteLLM routes dev/test to MI300X | W11 |
| 🟠 #3 | GB10 ordered + shipped | W10-W11 |
| 🟠 #4 | Production traffic migrated to MI300X | W11-W12 |
| 🟡 #5 | Phase 2 evaluation (Llama vs Claude) | W12-W13 |
| 🟡 #6 | Phase 3 decision (eliminate OpenRouter?) | W14+ |

---

## 📋 Related Documents

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| SharedKernel | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/SharedKernel.md) |
| PRJ-016 (LiteLLM) | v3.1.4.1 | GTM_2026-W09_117 | GTM_2026-W09_119 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-016_AIGateway-LiteLLM.md) |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| 3.2.1.1 | 2026-W10 | GTM_2026-W10_122 | GTM_2026-W10_125 | +MI300X Layer 1 Cloud GPU ($1,433/mo — @THY approved "Drop everything"); 3-layer architecture (Cloud GPU + Edge GPU + Cloud LLM); title → "3-Layer AI Compute"; +MI300X deployment checklist (11 steps); +Cost emergency catalyst ($372/day burn, $7,277 total, 13 top-ups); +3-phase migration plan (Hybrid → Evaluate → Decide); +Model evaluation matrix (8 tests, 3 score tiers); +LiteLLM integration config; +@RMN analysis (24 Feb Signal); +OpenRouter credit history (13 top-ups); +Layer routing rules; GB10 relabeled Layer 2 (content preserved L-097); OpenRouter relabeled Layer 3 (fallback); ROI updated for 3-layer scenarios ($76K-$109K/yr savings); payback = 3.9 days (MI300X) / 25 days (combined); 2-year savings $153K-$210K; FULL PRESERVE existing content |
| 3.1.4.3 | 2026-W09 | GTM_2026-W09_104 | ⬜ @THY | Initial proposal; 2× Dell GB10 ($7,898); #HybridArchitecture vision; 12 use cases; ROI analysis; implementation plan |

---

#FlowsBros #FedArch #HybridArchitecture #MI300X #CostEmergency #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
