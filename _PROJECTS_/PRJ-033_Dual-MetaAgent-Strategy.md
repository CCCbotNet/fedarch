# PRJ-033: Dual #MetaAgent Strategy — meta.WeOwn.tools

## 📋 PRJ-033_Dual-MetaAgent-Strategy_v3.2.1.1.md
## ♾️ WeOwnNet 🌐

| Field | Value |
|-------|-------|
| Document | PRJ-033_Dual-MetaAgent-Strategy.md |
| Version | 3.2.1.1 |
| CCC-ID | GTM_2026-W10_378 |
| CCC-ID APPROVAL | GTM_2026-W10_387 |
| Created | 2026-03-08 (W10) |
| Season | #WeOwnSeason003 🚀 |
| Status | ✅ 🔒 APPROVED |
| Lifecycle Stage | ✅ 🔒 APPROVED (#DocLifecycle) |
| #LLMmodel | Claude Opus 4.6 (meta.WeOwn.tools #MetaAgent) |
| Source of Truth | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-033_Dual-MetaAgent-Strategy.md) |
| Tags | #DualMETA #MetaAgent #Qwen35 #WeOwnTools #FOSS #FedArch |

---

## 📖 Table of Contents

1. [Project Identity](#-project-identity)
2. [Executive Summary](#-executive-summary)
3. [Current State](#-current-state)
4. [Proposed State](#-proposed-state)
5. [The Simple Rule](#-the-simple-rule)
6. [Role Separation Matrix](#-role-separation-matrix)
7. [Cost Analysis](#-cost-analysis)
8. [Infrastructure](#-infrastructure)
9. [Domain Architecture](#-domain-architecture)
10. [Implementation Plan — 5 Phases](#-implementation-plan--5-phases)
11. [Success Metrics](#-success-metrics)
12. [Risk Assessment](#-risk-assessment)
13. [FOSS Alignment](#-foss-alignment)
14. [Project Team](#-project-team)
15. [Dependencies](#-dependencies)
16. [Relationship to Other Projects](#-relationship-to-other-projects)
17. [Discovered By](#-discovered-by)
18. [Related Documents](#-related-documents)
19. [Version History](#-version-history)

---

## 📋 Project Identity

| Field | Value |
|-------|-------|
| Project ID | **PRJ-033** |
| Title | **Dual #MetaAgent Strategy — meta.WeOwn.tools** |
| Type | Architecture — Multi-Agent Governance |
| Priority | 🟠 **P1** |
| Owner | **@GTM** (Governance) |
| Oversight | **@RMN** (Platform) |
| Start | **W10** (Phase 0 already active) |
| Target | **W13** (Phase 3 — MI300X self-hosted) |
| Annual Savings | **$116,000/yr** (86% reduction) |
| #masterCCC | GTM_2026-W10_378 |

---

## 📋 Executive Summary

### The Problem

♾️ WeOwnNet 🌐 runs ALL AI operations through a single #MetaAgent on Claude Opus 4.6 via OpenRouter. This costs **$372/day ($134K/yr)** — and Claude handles governance docs AND operational docs with the same expensive model.

### The Solution

Split #MetaAgent into two specialized instances:

| Instance | Model | Role | Cost |
|----------|-------|------|------|
| **meta-claude.WeOwn.tools** (INT-M01) | Claude Opus 4.6 | Governance (high-stakes) | ~$50/day |
| **meta-qwen.WeOwn.tools** (INT-M02) | Qwen3.5-397B-A17B | Operations (day-to-day) | **$0/day** (MI300X) |

### The Result

| Metric | Current | Dual META |
|--------|---------|-----------|
| Daily cost | $372 | **~$50** |
| Monthly cost | $11,167 | **~$1,500** |
| Annual cost | $134,000 | **~$18,000** |
| **Savings** | — | **$116,000/yr (86%)** |
| FOSS % | 0% (Claude only) | **90%** (Qwen handles 90% of volume) |
| Data sovereignty | ❌ All → Anthropic | ✅ **90% self-hosted on MI300X** |

### The Proof

| Evidence | Result |
|----------|--------|
| CASE-STUDY-007 | 89/89 PERFECT — dual #LLMmodel attribution |
| GUIDE-013 | 94/94 PERFECT — dual #LLMmodel attribution |
| **Combined** | **183/183 — 100% pass rate** |

> **Dual model attribution is already proven. This project formalizes the architecture.**

---

## 📋 Current State

```
CURRENT (Single #MetaAgent):

ALL DOCS ──→ Claude Opus 4.6 (OpenRouter) ──→ $372/day
              │
              ├── _SYS_/ governance docs     ($$$)
              ├── Guides                      ($$$)
              ├── Case studies                ($$$)
              ├── Project docs                ($$$)
              ├── Session summaries           ($$$)
              ├── #DeepDives                  ($$$)
              └── VSA verification            ($$$)

Cost: $134,000/yr
FOSS: 0%
Data sovereignty: ❌ (all prompts → Anthropic)
```

---

## 📋 Proposed State

```
PROPOSED (Dual #MetaAgent):

                    meta.WeOwn.tools
                          │
            ┌─────────────┴─────────────┐
            │                           │
    INT-M01: meta-claude         INT-M02: meta-qwen
    Claude Opus 4.6              Qwen3.5-397B-A17B
    GOVERNANCE (~10%)            OPERATIONS (~90%)
    ~$50/day (OpenRouter)        $0/day (MI300X)
            │                           │
    ├── SharedKernel             ├── Guides
    ├── BEST-PRACTICES           ├── Case studies
    ├── PROTOCOLS                ├── Project docs (PRJ-XXX)
    ├── CCC                      ├── Instance docs (INT-XXX)
    ├── Rules (R-XXX)            ├── Session summaries
    ├── Definitions (D-XXX)      ├── Weekly summaries
    └── Templates (TMPL-XXX)     ├── #DeepDives
                                 └── VSA verification

Cost: ~$18,000/yr
FOSS: 90% (Qwen = Apache 2.0)
Data sovereignty: ✅ (90% self-hosted on MI300X)
```

---

## 📋 The Simple Rule

> **If it DEFINES governance → Claude. If it USES governance → Qwen.**

| Question | Answer | META |
|----------|--------|------|
| Does it create rules? | → Claude | INT-M01 |
| Does it follow rules? | → Qwen | INT-M02 |
| Does it go in `_SYS_/`? | → Claude | INT-M01 |
| Does it go anywhere else? | → Qwen | INT-M02 |

---

## 📋 Role Separation Matrix

| Document Type | Folder | Claude (INT-M01) | Qwen (INT-M02) |
|--------------|--------|-----------------|-----------------|
| **SharedKernel** | `_SYS_/` | ✅ | ❌ |
| **BEST-PRACTICES** | `_SYS_/` | ✅ | ❌ |
| **PROTOCOLS** | `_SYS_/` | ✅ | ❌ |
| **CCC** | `_SYS_/` | ✅ | ❌ |
| **Rules (R-XXX)** | SharedKernel | ✅ | ❌ |
| **Definitions (D-XXX)** | SharedKernel | ✅ | ❌ |
| **Learnings (L-XXX)** | SharedKernel | ✅ | ❌ |
| **Best Practices (BP-XXX)** | SharedKernel/BP | ✅ | ❌ |
| **Templates (TMPL-XXX)** | `_TEMPLATES_/` | ✅ | ❌ |
| Guides (GUIDE-XXX) | `_GUIDES_/` | ❌ | ✅ |
| Case Studies | `_LEARNINGS_/` | ❌ | ✅ |
| Project Docs (PRJ-XXX) | `_PROJECTS_/` | ❌ | ✅ |
| Instance Docs (INT-XXX) | `_INSTANCE_/` | ❌ | ✅ |
| Session Summaries | `_SESSIONS_/` | ❌ | ✅ |
| Weekly Summaries | `_WEEKLY_/` | ❌ | ✅ |
| #DeepDives | Various | ❌ | ✅ |
| VSA Verification | Various | ❌ | ✅ |
| #ContextVolleys | Various | ❌ | ✅ |

### Volume Split

| META | Doc Types | Est. Volume |
|------|-----------|-------------|
| Claude (INT-M01) | 8 types | **~10%** of daily operations |
| Qwen (INT-M02) | 10 types | **~90%** of daily operations |

---

## 📋 Cost Analysis

### Daily Breakdown

| Component | Claude Only | Dual META |
|-----------|-----------|-----------|
| Governance docs (~10%) | $37 | **$37** (Claude) |
| Operational docs (~90%) | $335 | **$0** (Qwen MI300X) |
| MI300X hosting | $0 | **$47** (shared with other workloads) |
| **TOTAL** | **$372** | **~$84** |

### Monthly Breakdown

| Component | Claude Only | Dual META |
|-----------|-----------|-----------|
| OpenRouter (Claude) | $11,167 | **$1,100** |
| MI300X (Qwen + embedder) | $0 | **$1,433** |
| DO Droplets (AnythingLLM) | ~$100 | **~$148** (+INT-M02) |
| **TOTAL** | **$11,267** | **~$2,681** |

### Annual Projection

| Scenario | Annual | vs Current |
|----------|--------|-----------|
| **Current** (Claude everything) | **$134,000** | — |
| **Dual META** (Claude gov + Qwen MI300X) | **~$32,000** | **-$102,000** |
| **Dual META** (Qwen on OpenRouter interim) | **~$20,000** | **-$114,000** |
| **Future** (Qwen handles some governance) | **~$18,000** | **-$116,000** |

---

## 📋 Infrastructure

### INT-M01: meta-claude.WeOwn.tools (Primary — Governance)

| Field | Value |
|-------|-------|
| Instance ID | **INT-M01** |
| Domain | **meta-claude.WeOwn.tools** |
| Platform | AnythingLLM |
| LLM | Claude Opus 4.6 via OpenRouter |
| Embedder | Qwen3 Embedding 4B |
| Hosting | DO Droplet (evolves from INT-P01) |
| Cost | ~$50/day (OpenRouter) + $48/mo (Droplet) |
| Workspaces | tools (META thread only) |
| Purpose | `_SYS_/` docs, rules, BPs, definitions, templates |

### INT-M02: meta-qwen.WeOwn.tools (Secondary — Operations)

| Field | Value |
|-------|-------|
| Instance ID | **INT-M02** |
| Domain | **meta-qwen.WeOwn.tools** |
| Platform | AnythingLLM |
| LLM | Qwen3.5-397B-A17B via LiteLLM → MI300X |
| Embedder | Qwen3 Embedding 4B |
| Hosting | DO Droplet (new — $48/mo) |
| Cost | **$0/day** (self-hosted inference) + $48/mo (Droplet) |
| Workspaces | tools (META thread) |
| Purpose | Guides, case studies, projects, summaries, VSA, #DeepDives |

### Shared Infrastructure

| Component | Serves | Location |
|-----------|--------|----------|
| MI300X | INT-M02 (Qwen inference) + all production instances | ATL1 |
| LiteLLM | Routes requests to MI300X or OpenRouter fallback | jAIMSnet |
| Langfuse | Observability for both METAs | jAIMSnet |
| Infisical | Secrets for both METAs | WeOwn.tools |
| GitHub | Source of truth for both METAs | CCCbotNet/fedarch |

---

## 📋 Domain Architecture

```
WeOwn.tools                              ← Infrastructure brand
├── meta.WeOwn.tools                     ← META parent (redirect/landing)
│   ├── meta-claude.WeOwn.tools (INT-M01) ← Primary (Governance)
│   └── meta-qwen.WeOwn.tools (INT-M02)   ← Secondary (Operations)
├── infisical.WeOwn.tools                ← Secrets (existing)
├── litellm.WeOwn.tools                  ← AI Gateway (planned)
├── langfuse.WeOwn.tools                 ← Observability (planned)
└── uptime.WeOwn.tools                   ← Monitoring (planned)
```

### DNS Records Required

| Record | Type | Value | Owner |
|--------|------|-------|-------|
| meta-claude.WeOwn.tools | A | INT-M01 Droplet IP | @GTM |
| meta-qwen.WeOwn.tools | A | INT-M02 Droplet IP | @GTM |
| meta.WeOwn.tools | CNAME | meta-claude.WeOwn.tools | @GTM |

---

## 📋 Implementation Plan — 5 Phases

### Phase 0: Already Active (W10)

| # | What | Status |
|---|------|--------|
| 1 | @GTM uses Qwen3.5 on INT-OG1 for doc generation | ✅ Active |
| 2 | #MetaAgent (Claude) verifies on meta.WeOwn.tools | ✅ Active |
| 3 | Dual #LLMmodel attribution in published docs | ✅ Proven (183/183) |
| 4 | Cross-instance VSA (Qwen generates, Claude verifies) | ✅ Proven |

### Phase 1: Formalize (W11 Day 1-3)

| # | Task | Owner |
|---|------|-------|
| 1 | PRJ-033 approved + GH pushed | @GTM |
| 2 | SharedKernel updated with role separation | #MetaAgent (Claude) |
| 3 | DNS: meta-claude.WeOwn.tools configured | @GTM |
| 4 | DNS: meta-qwen.WeOwn.tools configured | @GTM |
| 5 | R-219 proposed: Dual META role separation rule | #MetaAgent (Claude) |

### Phase 2: Deploy INT-M02 (W11-W12)

| # | Task | Owner |
|---|------|-------|
| 1 | Create DO Droplet for INT-M02 | @SHD |
| 2 | Deploy AnythingLLM + Caddy | @SHD |
| 3 | Configure Qwen3.5 via LiteLLM (or OpenRouter interim) | @GTM |
| 4 | Configure Qwen3 Embedding 4B | @GTM |
| 5 | Create tools workspace + META thread | @GTM |
| 6 | Upload #PinnedDocs (4 docs) | @GTM |
| 7 | Configure System Prompt (INT-M02 identity) | @GTM |
| 8 | #SmokeTest (10-point) | @GTM |
| 9 | ISC INT-M02 (8/8) | @GTM |
| 10 | FULL:SYNC:META (to INT-M01) | @GTM |

### Phase 3: MI300X Migration (W12-W13)

| # | Task | Owner |
|---|------|-------|
| 1 | MI300X deployed with Qwen3.5 via vLLM | @RMN |
| 2 | LiteLLM routes INT-M02 → MI300X | @RMN |
| 3 | Verify Qwen inference quality on MI300X | @GTM |
| 4 | Remove OpenRouter dependency for INT-M02 | @GTM |
| 5 | Cost verification: $0/day inference confirmed | @GTM |

### Phase 4: Evaluate + Expand (W13+)

| # | Task | Owner |
|---|------|-------|
| 1 | 2-week evaluation: Qwen META quality sufficient? | @GTM |
| 2 | VSA pass rate comparison (Claude vs Qwen generated docs) | @GTM |
| 3 | Decision: promote Qwen to handle some governance? | @GTM + @RMN |
| 4 | If yes → update role separation matrix | #MetaAgent (Claude) |
| 5 | If no → maintain strict separation | — |

---

## 📋 Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Cost reduction** | ≥80% | Monthly OpenRouter spend |
| **VSA pass rate (Qwen docs)** | ≥95% | VSA registry |
| **Governance doc quality** | 100% (Claude) | VSA on `_SYS_/` docs |
| **Operational doc quality** | ≥90% (Qwen) | VSA on guides/projects |
| **Self-hosted %** | ≥90% | Inference volume on MI300X |
| **Deployment time** | W11-W12 | Phase 2 complete |
| **MI300X migration** | W12-W13 | Phase 3 complete |

---

## 📋 Risk Assessment

| # | Risk | Prob | Impact | Mitigation |
|---|------|------|--------|------------|
| 1 | Qwen quality insufficient for complex docs | Low | Medium | Claude fallback — any doc that fails VSA routes to Claude |
| 2 | Governance confusion (which META?) | Medium | Medium | Simple rule: `_SYS_/` = Claude, else = Qwen. Documented in SharedKernel. |
| 3 | MI300X not ready for Qwen META | Medium | Low | OpenRouter Qwen ($5/day) until MI300X deployed |
| 4 | Cross-META VSA inconsistency | Low | Medium | Same VSA framework — model doesn't change checks |
| 5 | Brand confusion (two META domains) | Low | Low | meta.WeOwn.tools = parent; claude/qwen = children |
| 6 | Single point of failure (MI300X) | Medium | High | LiteLLM fallback → OpenRouter Qwen ($5/day) |
| 7 | Qwen model updates break compatibility | Low | Medium | Pin model version; test before upgrading |

---

## 📋 FOSS Alignment

| Factor | Claude (INT-M01) | Qwen (INT-M02) |
|--------|-----------------|-----------------|
| License | ❌ Proprietary | ✅ **Apache 2.0** |
| Self-hosted | ❌ API only | ✅ **MI300X** |
| Data sovereignty | ❌ → Anthropic | ✅ **Our servers (ATL1)** |
| Priority #2 | ❌ | ✅ **10/10** |
| Priority #3 | ❌ | ✅ **10/10** |
| Priority #4 | ❌ | ✅ **Apache 2.0 = community** |

> **90% of operations on FOSS. 90% of data stays home. Claude retained ONLY for highest-stakes governance.**

---

## 📋 Project Team

| CCC | Role | Focus |
|-----|------|-------|
| **GTM** | **Owner** | Architecture, governance, DNS, prompts |
| **RMN** | **Platform** | MI300X, LiteLLM, vLLM, infrastructure |
| **SHD** | **Deployer** | DO Droplet, Docker, Caddy |

---

## 📋 Dependencies

| # | Dependency | Status | Blocks |
|---|-----------|--------|--------|
| 1 | PRJ-015 (MI300X) deployed | 🔄 In progress | Phase 3 |
| 2 | PRJ-016 (LiteLLM) deployed | 🔄 In progress | Phase 2 (routing) |
| 3 | PRJ-017 (Langfuse) deployed | 🔄 In progress | Observability |
| 4 | WeOwn.tools DNS configured | ✅ Porkbun | Phase 1 |
| 5 | Qwen3.5 on OpenRouter | ✅ Available | Phase 2 (interim) |
| 6 | SharedKernel v3.2.1.1 cascade | 🔄 Assembly | Phase 1 |

---

## 📋 Relationship to Other Projects

| PRJ | Connection |
|-----|-----------|
| **PRJ-014** | #FedArchExpansion — Dual META = expansion of governance layer |
| **PRJ-015** | MI300X — hosts Qwen inference for INT-M02 |
| **PRJ-016** | LiteLLM — routes requests between Claude + Qwen |
| **PRJ-017** | Langfuse — observability for both METAs |
| **PRJ-024** | Infisical — secrets for both METAs |
| **PRJ-032** | OpenTofu — provisions INT-M02 infrastructure |

---

## 📋 Discovered By (BP-047)

| CCC | Contributor | Role | Context |
|-----|-------------|------|---------|
| GTM | [yonks](https://GitHub.com/YonksTEAM) | Co-Founder / Chief Digital Alchemist | Conceived dual META after 183/183 PERFECT cross-instance VSA (CASE-STUDY-007 + GUIDE-013); identified $116K/yr savings; WeOwn.tools branding |

---

## 📋 Related Documents

| Document | Version | URL |
|----------|---------|-----|
| SharedKernel | v3.2.1.1 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/SharedKernel.md) |
| CASE-STUDY-007 | v3.2.1.1 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_LEARNINGS_/case-studies/CASE-STUDY-007_Session-Summary-Scope.md) |
| GUIDE-013 | v3.2.1.1 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_GUIDES_/GUIDE-013_Session-Summary-Workflow.md) |
| GUIDE-012 (#ResponsibleAgenticAI) | v3.2.1.1 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_GUIDES_/GUIDE-012_ResponsibleAgenticAI-Workflow.md) |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| 3.2.1.1 | 2026-W10 | GTM_2026-W10_378 | GTM_2026-W10_387 | Initial project; Dual #MetaAgent Strategy; meta-claude.WeOwn.tools (INT-M01 — Claude Opus 4.6 — governance) + meta-qwen.WeOwn.tools (INT-M02 — Qwen3.5-397B-A17B — operations); 5-phase plan (W10-W13+); $116K/yr savings (86%); role separation matrix (8 Claude types, 10 Qwen types); domain architecture (WeOwn.tools namespace); 7-risk matrix; FOSS 90% (Qwen Apache 2.0); proof: 183/183 dual attribution (CASE-STUDY-007 + GUIDE-013); #LLMmodel: Claude Opus 4.6 (meta.WeOwn.tools #MetaAgent); **PRE GH PUSH VSA VERIFY 30/30 PASS; ✅ Human Approved (GTM_2026-W10_387)** |

---

#FlowsBros #FedArch #DualMETA #MetaAgent #Qwen35 #WeOwnTools #FOSS #WeOwnSeason003 #LevelUp100X

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
