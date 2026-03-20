# LLM Infrastructure Implementation Guide: Gateway + Self-Hosted Inference
## The HOW — Technical Evaluation, Stack Options & Deployment Guide

### ♾️ WeOwnNet 🌐

| Field | Value |
|-------|-------|
| Document | P-010_Doc2_Gateway-Inference-Implementation-Guide.md |
| Version | v3.1.3.2 |
| CCC-ID | RMN_2026-W09_035 |
| #masterCCC | RMN_2026-W09_035 |
| Created | February 24, 2026 (W09) |
| Submitted | February XX, 2026 |
| Season | #WeOwnSeason003 🚀 |
| Status | 👀 REVIEW |
| Reviewers | @RMN, @SHD (Shahid), @LDC (Dhruv), @GTM (yonks) |
| Approval | ⬜ AWAITING @GTM |
| Author | @RMN (with AI research assistance) |
| Audience | All — @RMN, @SHD, @LDC, @CEO, @THY, @GTM, engineering team, interns |
| Purpose | Technical evaluation of all stack options + step-by-step deployment guide |
| Companion | P-010_Doc1_LLM-Infrastructure-Evaluation.md (The WHAT) |
| Tags | #LLM #Infrastructure #Implementation #Gateway #Inference #P-010 |

---

## Table of Contents

1. [Introduction & Context](#1-introduction--context)
2. [Phased Deployment Strategy](#2-phased-deployment-strategy)
3. [Architecture Overview](#3-architecture-overview)
4. [AI Gateway Evaluation](#4-ai-gateway-evaluation)
5. [Observability Evaluation](#5-observability-evaluation)
6. [Inference Framework Evaluation](#6-inference-framework-evaluation)
7. [GPU Infrastructure Options](#7-gpu-infrastructure-options)
8. [Target Model Matrix](#8-target-model-matrix)
9. [Recommended Stack Configurations](#9-recommended-stack-configurations)
10. [Phase 1A Deployment — Gateway Quick Win (Days 1-3)](#10-phase-1a-deployment--gateway-quick-win-days-1-3)
11. [Phase 1B Deployment — Add Self-Hosted Inference (Days 7-14)](#11-phase-1b-deployment--add-self-hosted-inference-days-7-14)
12. [Phase 2+ Scaling Guide](#12-phase-2-scaling-guide)
13. [Operations & Maintenance Playbook](#13-operations--maintenance-playbook)
14. [Automation (OpenTofu + n8n)](#14-automation-opentofu--n8n)
15. [Migration Plan — OpenRouter to Self-Hosted](#15-migration-plan--openrouter-to-self-hosted)
16. [Appendix: Configuration Reference](#16-appendix-configuration-reference)

---

## 1. Introduction & Context

### What This Document Is

This is the technical companion to Doc 1 (Cost + Privacy + Architecture
Evaluation). Doc 1 answers "WHAT should we do?" — this document answers
"HOW do we do it?"

This document evaluates all viable options for each component of our
LLM infrastructure stack, provides recommendations, and includes
complete step-by-step deployment guides for each phase.

### Current State

| Component | Current | Phase 1A Target | Phase 1B Target |
|-----------|---------|----------------|----------------|
| LLM Provider | OpenRouter (Opus for everything) | Cloud APIs via gateway (Anthropic direct + Together AI) | Self-hosted primary + cloud fallback |
| Gateway | None | LiteLLM, TensorZero, or Portkey | Same gateway |
| Observability | Braintrust (free tier) | Braintrust (keep) + optionally add Langfuse | Same |
| Inference | None (cloud-only) | None (still cloud) | vLLM or SGLang on GPU |
| GPU | None | None needed | DigitalOcean MI300X |
| Embedder | Qwen3 Embedding 4B (via OpenRouter) | Same (via Together AI or local) | Self-hosted on GPU |
| Infrastructure | DO DOKS + Droplets (ATL1) | Same + gateway pods | Same + GPU Droplet(s) |

### Decisions Still Open

This document presents options for management and engineering to finalize:

| Component | Options | Current Leaning |
|-----------|---------|----------------|
| **Gateway** | LiteLLM (FOSS) / TensorZero (FOSS) / Portkey (paid) | LiteLLM |
| **Observability** | Keep Braintrust / Add Langfuse / Both | Keep Braintrust + evaluate Langfuse |
| **Inference** | vLLM / SGLang | vLLM |
| **GPU** | Multiple options per model — see Section 7 | DO MI300X |
| **Models** | Multiple frontier open-weight — see Section 8 | Llama 4 Maverick + Scout |

---

## 2. Phased Deployment Strategy

### Why Phased?

Doc 1 recommends deploying in phases to minimize risk and deliver
immediate savings. Each phase builds on the previous one and can be
paused or reversed if issues arise.

### Phase Overview

```
Phase 1A: GATEWAY QUICK WIN (Days 1-3)
├── Deploy LiteLLM gateway on existing DOKS cluster
├── Route to cloud APIs: Anthropic direct + Together AI
├── Smart routing: simple tasks → cheap models, complex → Opus
├── NO GPU needed, NO new hardware
├── Immediate savings: 76-81% ($3,400-3,700/mo)
├── Risk: VERY LOW (same cloud models, just smarter routing)
│
▼
Phase 1B: ADD SELF-HOSTED INFERENCE (Days 7-14)
├── Provision MI300X GPU Droplet
├── Deploy vLLM with open-weight models
├── Gateway routes most traffic to self-hosted
├── Cloud API becomes fallback only (~10% of traffic)
├── Additional savings: fixed cost replaces per-token cost
├── Risk: LOW-MEDIUM (new GPU ops, but cloud fallback if issues)
│
▼
Phase 2+: SCALE (Month 2-12)
├── Onboard customers through self-hosted stack
├── Add GPU servers as customer count grows
├── Add bare metal for internal/dev use
├── Full scale: 1000 customers on 6-8 GPUs
└── Risk: LOW (proven stack, just adding capacity)
```

### Cost at Each Phase

| Phase | Monthly Cost | vs Current ($4,500) | What Changes |
|-------|:-----------:|:-------------------:|-------------|
| **Current** | $4,500 | — | All Opus via OpenRouter |
| **Phase 1A** | ~$845-1,070 | **76-81% savings** | Gateway + smart routing to cloud APIs |
| **Phase 1B** | ~$1,716-2,058 | **54-62% savings** | Add MI300X + self-hosted (fixed cost) |
| **Phase 2 (100 customers)** | ~$3,976 | **93-97% vs OpenRouter at scale** | 2 GPUs + customers |
| **Phase 3 (1000 customers)** | ~$13,478 | **97-99% vs OpenRouter at scale** | 7 GPUs + full scale |

### Why Phase 1A First?

| Reason | Detail |
|--------|--------|
| **Immediate ROI** | Saves $3,400+/mo from day 1 — gateway pays for itself 40× over |
| **Zero new skills needed** | Gateway runs on existing DOKS cluster — no GPU knowledge required |
| **Validates the gateway** | Confirm routing, budgeting, logging work before adding GPU complexity |
| **De-risks Phase 1B** | If gateway works, adding GPU is just connecting a new backend |
| **Provides baseline data** | See real traffic patterns before deciding which models to self-host |
| **Eliminates OpenRouter** | Moves to Anthropic direct API (cheaper, more private, SOC2 certified) |

---

## 3. Architecture Overview

### Phase 1A Architecture (Gateway + Cloud APIs)

```
┌─────────────────────────────────────────────────────────────────┐
│                 ANYTHINGLLM INSTANCES (DO DOKS)                  │
│         4 instances now → 100+ customer instances later          │
└─────────────────────────┬───────────────────────────────────────┘
                          │
                          │ POST /v1/chat/completions
                          │ Authorization: Bearer sk-tenant-XXX
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│              AI GATEWAY — LiteLLM (DO DOKS — ATL1)              │
│                                                                 │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐          │
│  │ Tenant   │ │ Budget   │ │ Semantic │ │ Routing  │          │
│  │ Auth     │ │ Check    │ │ Cache    │ │ Engine   │          │
│  └────┬─────┘ └────┬─────┘ │ (Redis)  │ └────┬─────┘          │
│       └─────────────┴───────┴──────────┴──────┘                │
│                          │                                      │
│  Logging ──→  Braintrust (current)                              │
│          ──→  Langfuse (optional FOSS addition)                 │
│                          │                                      │
│       ┌──────────────────┼──────────────────┐                  │
│       ▼                  ▼                  ▼                  │
│  Simple Tasks      Moderate Tasks     Complex Tasks            │
│  (60% of traffic)  (25% of traffic)  (15% of traffic)          │
└───────┼──────────────────┼──────────────────┼──────────────────┘
        │                  │                  │
        ▼                  ▼                  ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ Together AI  │  │ Anthropic    │  │ Anthropic    │
│              │  │ Claude       │  │ Claude       │
│ Llama 4      │  │ Sonnet 4.5   │  │ Opus 4.6     │
│ Maverick     │  │              │  │              │
│              │  │ $3/$15 per M │  │ $15/$75 per M│
│ $0.27/$0.85  │  │              │  │              │
│ per M tokens │  │              │  │              │
└──────────────┘  └──────────────┘  └──────────────┘

Estimated monthly cost: ~$845-1,070
(vs $4,500 current = 76-81% savings)
```

### Phase 1B Architecture (Add Self-Hosted Inference)

```
┌─────────────────────────────────────────────────────────────────┐
│                 ANYTHINGLLM INSTANCES (DO DOKS)                  │
└─────────────────────────┬───────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│              AI GATEWAY — LiteLLM (DO DOKS — ATL1)              │
│                                                                 │
│  Same gateway as Phase 1A — just add self-hosted backends       │
│                                                                 │
│  Routing changes:                                               │
│  ├── Simple tasks → Self-hosted Scout (was: Together AI)        │
│  ├── Standard tasks → Self-hosted Maverick (was: Together AI)   │
│  ├── Code tasks → Self-hosted DeepSeek V3.2 (new)              │
│  └── Complex tasks → Cloud Claude Opus (unchanged, ~10%)       │
│                                                                 │
│       ┌──────────────────┼──────────────┐                      │
│       ▼                  ▼              ▼                      │
│  Self-Hosted         Self-Hosted    Cloud Fallback              │
│  (90% traffic)       (if 2nd GPU)   (10% traffic)              │
└───────┼──────────────────┼──────────────┼──────────────────────┘
        │                  │              │
        ▼                  ▼              ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ vLLM/SGLang  │  │ vLLM/SGLang  │  │ Anthropic    │
│ on MI300X #1 │  │ on MI300X #2 │  │ Claude API   │
│ (DO ATL1)    │  │ (Phase 2+)   │  │ (Direct)     │
│              │  │              │  │              │
│ Models:      │  │ Models:      │  │ Opus 4.6     │
│ - Maverick   │  │ - DeepSeek   │  │ Sonnet 4.5   │
│ - Scout      │  │ - Qwen 3.5   │  │              │
│ - Embed 4B   │  │ - GLM-5      │  │ ~$200-500/mo │
│              │  │              │  │              │
│ $1,433/mo    │  │ $1,433/mo    │  │              │
└──────────────┘  └──────────────┘  └──────────────┘
```

### Connection Map

| # | From | To | Method | Latency | Bandwidth Cost |
|---|------|-----|--------|---------|---------------|
| 1 | AnythingLLM (DOKS) | Gateway (DOKS) | K8s service | <1ms | Free (same cluster) |
| 2 | Gateway (DOKS) | Together AI | HTTPS (public) | 50-150ms | Standard egress |
| 3 | Gateway (DOKS) | Anthropic API | HTTPS (public) | 50-200ms | Standard egress |
| 4 | Gateway (DOKS) | vLLM (GPU Droplet) | VPC private IP | <2ms | **Free** (same VPC) |
| 5 | Gateway (DOKS) | Braintrust | HTTPS (public) | 50-100ms | Minimal |
| 6 | Gateway (DOKS) | Langfuse (DOKS) | K8s service | <1ms | Free (if self-hosted) |
| 7 | Gateway (DOKS) | Redis (DOKS/Managed) | VPC/K8s | <1ms | Free |
| 8 | Gateway (DOKS) | PostgreSQL (Managed) | VPC private | <1ms | Free |

---

## 4. AI Gateway Evaluation

### Why We Need a Gateway

A gateway sits between AnythingLLM and the AI models. It provides:
- **Smart routing** — send questions to the right model based on complexity
- **Per-customer budgets** — limit how much each customer can spend
- **Per-customer API keys** — each customer gets their own key
- **Caching** — avoid re-processing identical or similar questions
- **Logging** — track every request for monitoring and billing
- **Fallback** — if one model/provider is down, automatically use another
- **Load balancing** — spread requests across multiple backends

### Gateway Options Evaluated

#### Option 1: LiteLLM (FOSS — MIT License) ⭐ PRIMARY RECOMMENDATION

| Aspect | Detail |
|--------|--------|
| **License** | MIT — fully free and open-source |
| **Deployment** | Docker, Kubernetes (Helm chart available) |
| **FOSS Features (all free)** | Multi-model routing, 100+ provider support, per-key budgets, per-key rate limits, per-key model access, spend tracking, semantic caching (Redis), fallback routing, load balancing, OpenAI-compatible API, PostgreSQL backend |
| **Enterprise Features (paid)** | SSO, premium support, advanced analytics UI |
| **Multi-tenant** | ✅ Best-in-class — purpose-built for per-key budget/access control |
| **Semantic routing** | ⚠️ Not native — add RouteLLM library for complexity-based routing |
| **Guardrails** | ⚠️ Via callbacks — add NeMo Guardrails or custom middleware |
| **Observability** | ✅ Logs to Braintrust, Langfuse, and 10+ other backends natively |
| **AnythingLLM integration** | ✅ Generic OpenAI endpoint — no code changes needed |
| **Community** | 3K+ GitHub stars, active development, large community |
| **Our score** | 13/18 desired features natively, 17/18 with Langfuse + RouteLLM |
| **Monthly cost** | $0 (software) + ~$50-80 (DO compute for pods) |

**Best for:** Teams that want maximum control, full FOSS alignment, and the
strongest multi-tenant budgeting — all for free.

#### Option 2: TensorZero (FOSS — Apache 2.0) ⭐ FOSS ALTERNATIVE

| Aspect | Detail |
|--------|--------|
| **License** | Apache 2.0 — fully free and open-source |
| **Deployment** | Docker, Kubernetes (self-hosted only — no cloud option) |
| **Key Differentiator** | All-in-one: gateway + observability + evaluation + A/B testing + fine-tuning workflows. Written in Rust (very lightweight). |
| **FOSS Features** | Multi-model routing, variant-based routing (A/B tests), built-in evaluation, structured inference, feedback collection, ClickHouse observability, Prometheus metrics |
| **Multi-tenant** | ✅ Via API key mapping + ClickHouse per-tenant queries |
| **Semantic routing** | ⚠️ Variant-based (not semantic) — add RouteLLM |
| **Budgeting** | ⚠️ Not native — must build on ClickHouse usage data |
| **Observability** | ✅ Built-in (ClickHouse) — could potentially replace both Braintrust and Langfuse |
| **AnythingLLM integration** | ✅ OpenAI-compatible API |
| **Our score** | 11/18 desired features |
| **Monthly cost** | $0 (software) + ~$30-50 (DO compute — Rust binary is very lightweight) |

**Best for:** Teams that want an all-in-one FOSS solution with built-in
experimentation and don't need per-tenant budgeting out of the box.

#### Option 3: Portkey (Paid — Proprietary) ⭐ PAID OPTION

| Aspect | Detail |
|--------|--------|
| **License** | Proprietary (open-source gateway core, paid features) |
| **Deployment** | Cloud (primary), self-hosted (enterprise plan) |
| **Key Differentiator** | Most complete feature set in a single product. Rich UI dashboard. |
| **Paid Features** | Native semantic routing, PII detection, prompt injection defense, advanced guardrails, advanced caching, rich analytics dashboard, built-in evaluation |
| **Multi-tenant** | ✅ Full per-tenant everything via UI |
| **Semantic routing** | ✅ Native |
| **Guardrails** | ✅ Native (PII, content filtering, prompt injection) |
| **Observability** | ✅ Built-in — could replace Braintrust |
| **AnythingLLM integration** | ✅ OpenAI-compatible API |
| **Our score** | 16/18 desired features in single product |
| **Monthly cost** | $499-2,000/mo (enterprise pricing varies) |

**Best for:** Teams that want maximum features with minimum engineering effort
and are willing to pay for it.

### Gateway Comparison Matrix

| Feature | LiteLLM (FOSS) | TensorZero (FOSS) | Portkey (Paid) |
|---------|:-:|:-:|:-:|
| **Free to use** | ✅ MIT | ✅ Apache 2.0 | ❌ $499+/mo |
| **Self-hosted on VPC** | ✅ | ✅ | ✅ (enterprise) |
| **Multi-model routing** | ✅ | ✅ | ✅ |
| **Semantic routing** | ⚠️ Add RouteLLM | ⚠️ Add RouteLLM | ✅ Native |
| **Fallback routing** | ✅ | ✅ | ✅ |
| **Load balancing** | ✅ | ✅ | ✅ |
| **Per-tenant budgets** | ✅ Native | ⚠️ Custom | ✅ Native |
| **Per-tenant API keys** | ✅ Native | ✅ | ✅ |
| **Per-tenant model access** | ✅ Native | ✅ | ✅ |
| **Semantic caching** | ✅ Redis | ✅ Built-in | ✅ |
| **Guardrails / PII** | ⚠️ Callbacks | ⚠️ Middleware | ✅ Native |
| **OpenAI-compatible API** | ✅ | ✅ | ✅ |
| **Logs to Braintrust** | ✅ Native | ⚠️ Custom | ⚠️ Custom |
| **Logs to Langfuse** | ✅ Native | ⚠️ Custom | ⚠️ Custom |
| **Built-in eval/experiments** | ❌ | ✅ | ✅ |
| **UI Dashboard** | ✅ Basic admin UI | ⚠️ ClickHouse queries | ✅ Rich dashboard |
| **100+ provider support** | ✅ | ⚠️ Limited | ✅ |
| **Community size** | Large (3K+ stars) | Growing | Medium |
| **Production proven** | ✅ Widely used | ⚠️ Newer | ✅ |

### Gateway Recommendation

| Scenario | Pick | Why |
|----------|------|-----|
| **FOSS-first, best multi-tenant** | **LiteLLM** | Free, per-tenant budgets/keys/access built-in, logs to Braintrust natively |
| **FOSS-first, all-in-one** | **TensorZero** | Free, built-in evals/experiments, lightest resource usage |
| **Boss wants to pay for simplicity** | **Portkey** | Most features in one product, best dashboard, native guardrails |

---

## 5. Observability Evaluation

### Current State: Braintrust (Free Tier)

| Aspect | Detail |
|--------|--------|
| **What we use** | Braintrust free tier |
| **Current usage** | Light — haven't fully utilized features |
| **Features available** | Logging, tracing, evaluation, datasets, experiments, prompt management |
| **Self-hosted** | ❌ No — cloud only |
| **License** | Proprietary (free tier available) |
| **Integration with LiteLLM** | ✅ Native callback — `success_callback: ["braintrust"]` |

### Option A: Keep Braintrust Only (Current — Default) ⭐ STARTING POINT

| Pro | Con |
|-----|-----|
| ✅ Already set up — no migration needed | ❌ Cloud-only — data goes to Braintrust servers |
| ✅ Strong evaluation features | ❌ Not self-hosted (privacy consideration for observability data) |
| ✅ LiteLLM integrates natively | ❌ Free tier has limits that may be reached at scale |
| ✅ No additional deployment work | ❌ Not FOSS |

**LiteLLM config:**
```yaml
litellm_settings:
  success_callback: ["braintrust"]
  failure_callback: ["braintrust"]

environment_variables:
  BRAINTRUST_API_KEY: "os.environ/BRAINTRUST_API_KEY"
```

### Option B: Add Langfuse Alongside Braintrust ⭐ RECOMMENDED APPROACH

| Aspect | Detail |
|--------|--------|
| **License** | MIT (core) — fully free and open-source |
| **Deployment** | Self-hosted on DOKS (Docker, Helm) or Langfuse Cloud |
| **Features** | Logging, tracing, evaluation, datasets, experiments, prompt management, user feedback, cost tracking |
| **Self-hosted** | ✅ Yes — all observability data stays on our infrastructure |
| **Monthly cost (self-hosted)** | ~$20-30 (compute on DOKS) |

**Approach:** Run BOTH during evaluation period. Braintrust stays as primary.
Langfuse runs alongside for comparison. Decide later whether to fully migrate.

**LiteLLM config for both (dual-logging):**
```yaml
litellm_settings:
  success_callback: ["braintrust", "langfuse"]
  failure_callback: ["braintrust", "langfuse"]

environment_variables:
  BRAINTRUST_API_KEY: "os.environ/BRAINTRUST_API_KEY"
  LANGFUSE_PUBLIC_KEY: "os.environ/LANGFUSE_PUBLIC_KEY"
  LANGFUSE_SECRET_KEY: "os.environ/LANGFUSE_SECRET_KEY"
  LANGFUSE_HOST: "http://langfuse-svc.observability:3000"
```

### Option C: Replace Braintrust with Langfuse (Full FOSS)

Only consider this after evaluating Langfuse alongside Braintrust during Phase 1.

| Pro | Con |
|-----|-----|
| ✅ Fully self-hosted — all data on our infrastructure | ❌ Lose Braintrust features we may be using |
| ✅ MIT license — fully FOSS | ❌ Migration effort |
| ✅ Bette

<note>Content truncated. Call the fetch tool with a start_index of 20000 to get more content.</note>