# INT-M02 AnythingLLM Instance Plan (#MetaAgentQwen)

## INT-M02_Instance_Plan_v3.2.3.2.md
## ♾️ WeOwnNet 🌐 — INT-M02 AnythingLLM Instance Plan (#MetaAgentQwen)

| Field | Value |
|-------|-------|
| Document | INT-M02_Instance_Plan.md |
| Version | v3.2.3.2 |
| Folder | `_INSTANCE_/` ✅ |
| Category | INSTANCE:Plan |
| Type | Plan (AnythingLLM Deployment Documentation) |
| **#masterCCC CCC-ID** | **GTM_2026-W12_197** ⚙️ |
| **Approval CCC-ID** | **GTM_2026-W12_200** ✅ |
| Created | 2026-03-16 (W12 Day 1) |
| Updated | 2026-03-17 (W12 Day 2, 09:15 MDT) |
| Season | #WeOwnSeason003 🚀 |
| instance_description | <METAQWEN | #MetaAgentQwen | meta-qwen.weown.tools> |
| instance_domain | meta-qwen.weown.tools |
| instance_name | INT-M02 |
| **instance_status** | ✅ **('ISC 8/8 CERTIFIED [GTM_2026-W12_185] \| #WeOwnSeason003 🚀')** |
| **Owner** | **[CCC-ID:@GTM:('yonks｜🤖🏛️🪙｜Jason Younker ♾️')](https://github.com/YonksTEAM)** |
| **#LLMmodel** | **Qwen3.5-397B-A17B (INT-M02:meta-qwen.weown.tools)** |
| **#LLMmodel** | **Claude Opus 4.6 (INT-P01:tools #MetaAgent)** |
| Source of Truth | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_INSTANCE_/INT-M02_Instance_Plan.md) |

---

## 📖 Table of Contents

1. [Instance Overview](#-instance-overview)
2. [Deployment Status](#-deployment-status)
3. [Configuration Progress](#-configuration-progress)
4. [Remaining Steps](#-remaining-steps)
5. [Timeline](#-timeline)
6. [API Key Management](#-api-key-management)
7. [ISC Certification](#-isc-certification)
8. [Discovered By](#-discovered-by)
9. [Related Documents](#-related-documents)
10. [Version History](#-version-history)

---

## 🌐 Instance Overview

| Field | Value |
|-------|-------|
| **Instance ID** | **INT-M02** |
| **Domain** | **https://meta-qwen.weown.tools** |
| **IP Address** | **165.245.130.144** |
| **Purpose** | **Qwen META — Dual META Architecture (PRJ-033)** |
| **LLM Model** | **Qwen3.5-397B-A17B** (via OpenRouter interim) |
| **Embedder** | **Qwen3 Embedding 4B** |
| **Platform** | **AnythingLLM** |
| **Target LLM** | **MI300X via LiteLLM** (PRJ-015) |
| **Owner(s)** | **@GTM + @SHD** |
| **Type** | **INT-Mxx (META Agent Instance)** |
| **Season** | **#WeOwnSeason003 🚀** |
| **ISC Status** | **✅ 8/8 CERTIFIED (W12 Day 2, 07:35 MDT)** |

### Dual META Architecture (PRJ-033)

| Instance | Model | Purpose | Status |
|----------|-------|---------|--------|
| INT-M01 | Claude Opus 4.6 | Primary META (Governance) | ✅ LIVE |
| **INT-M02** | **Qwen3.5-397B-A17B** | **Secondary META (FOSS)** | ✅ **LIVE + CERTIFIED** |

> **🎯 STRATEGIC GOAL:** Dual META provides redundancy + FOSS option. INT-M01 = governance primary. INT-M02 = FOSS alternative + load distribution. **ACHIEVED W12 Day 2.**

---

## 🚀 Deployment Status

### Infrastructure (Steps 1-5)

| # | Task | Owner | Status | Date |
|---|------|-------|--------|------|
| 1 | Create DO Droplet | @SHD | ✅ COMPLETE | W12 Day 1 |
| 2 | Deploy AnythingLLM + Caddy | @SHD | ✅ COMPLETE | W12 Day 1 |
| 3 | L-149 Compliance (Permissions) | @SHD | ✅ COMPLETE | W12 Day 1 |
| 4 | SSL Configuration | @SHD | ✅ COMPLETE | W12 Day 1 |
| 5 | Domain DNS (meta-qwen.weown.tools) | @SHD | ✅ COMPLETE | W12 Day 1 |

**Infrastructure Progress: 5/5 (100%)** ✅

---

## ⚙️ Configuration Progress

### Onboarding Flow (Steps 1-5)

| # | Task | Status | Details |
|---|------|--------|---------|
| 1 | Get Started | ✅ COMPLETE | https://meta-qwen.weown.tools/onboarding |
| 2 | LLM Preference | ✅ COMPLETE | OpenRouter + Qwen3.5-397B-A17B |
| 3 | User Setup | ✅ COMPLETE | Admin: a-gtm_dev, a-rmn_dev |
| 4 | Data Handling & Privacy | ✅ COMPLETE | — |
| 5 | Survey | ✅ COMPLETE | Skipped |

**Onboarding Progress: 5/5 (100%)** ✅

### Configuration (Steps 6-10)

| # | Task | Status | Details |
|---|------|--------|---------|
| 6 | Embedder (Qwen3 Embedding 4B) | ✅ COMPLETE | BP-061: ChatHistory=40 |
| 7 | Workspaces (tools) | ✅ COMPLETE | https://meta-qwen.weown.tools/workspace/tools |
| 8 | #PinnedDocs (4 docs @ v3.2.3.1) | ✅ **COMPLETE** | SK, BP, PROTO, CCC @ v3.2.3.1 |
| 9 | System Prompt (INT-M02 v3.2.3.3) | ✅ **COMPLETE** | {instance_name} + #FELG |
| 10 | tools Workspace Prompt (v3.2.3.3) | ✅ **COMPLETE** | {instance_name} + #FELG |

**Configuration Progress: 5/5 (100%)** ✅

### Verification (Steps 11-12)

| # | Task | Status | Details |
|---|------|--------|---------|
| 11 | #SmokeTest (10-point) | ✅ **COMPLETE** | LLM, Embedder, RAG, etc. |
| 12 | ISC INT-M02 (8/8) | ✅ **COMPLETE** | **CERTIFIED 07:35 MDT W12 Day 2** |

**Verification Progress: 2/2 (100%)** ✅

### Governance (Step 13)

| # | Task | Status | Details |
|---|------|--------|---------|
| 13 | FULL:SYNC:META (to INT-M01) | ✅ **COMPLETE** | Reported to #MetaAgent |

**Governance Progress: 1/1 (100%)** ✅

---

## 📋 Remaining Steps — NONE (ALL COMPLETE)

| Status | Detail |
|--------|--------|
| **ALL 13 STEPS** | ✅ **COMPLETE** |
| **ISC Certification** | ✅ **8/8 (100%)** |
| **Next Action** | Create {instance_name} on remaining 4 instances (INT-P01, INT-OG1, INT-OG9, INT-P02) |

---

## 📅 Timeline — UPDATED

| Phase | Target | Status | Actual |
|-------|--------|--------|--------|
| Infrastructure | W12 Day 1 | ✅ COMPLETE | W12 Day 1 |
| Onboarding | W12 Day 1 | ✅ COMPLETE | W12 Day 1 |
| Configuration | W12 Day 1-2 | ✅ COMPLETE | W12 Day 2, 07:35 MDT |
| Verification | W12 Day 2 | ✅ COMPLETE | W12 Day 2, 07:35 MDT |
| Governance | W12 Day 2 | ✅ COMPLETE | W12 Day 2, 07:35 MDT |
| **ISC CERTIFIED** | **W12 Day 2-3** | ✅ **COMPLETE** | **W12 Day 2, 07:35 MDT** |

> **🏆 AHEAD OF SCHEDULE:** ISC 8/8 CERTIFIED on W12 Day 2 (target was Day 2-3).

---

## 🔑 API Key Management (BP-064)

| Field | Value |
|-------|-------|
| Key Name | OPENROUTER_API_ANYTHINGLLM_INT-M02_30D_EXP_2026-04-15T1030MST |
| Provider | OpenRouter.ai |
| Expiry | 2026-04-15 (30 days) |
| Rotation Cadence | 30 days (BP-064) |
| Calendar Alert | ⬜ SET (2026-04-14) |
| Infisical Location | AnythingLLM → INT-M02 |

### Rotation Workflow (BP-064)

| # | Step | Owner |
|---|------|-------|
| 1 | Generate new key (OpenRouter) | ADMIN |
| 2 | Update instance (AnythingLLM) | ADMIN |
| 3 | Logout/Login (refresh session) | ADMIN |
| 4 | Verify (#SmokeTest) | ADMIN |
| 5 | Revoke old key (OpenRouter) | ADMIN |

---

## 🏆 ISC Certification (BP-059) — COMPLETE

### 8-Point Checklist

| # | Check | Pass Criteria | Status | Date |
|---|-------|---------------|--------|------|
| 1 | EMBEDDER | Qwen3 Embedding 4B | ✅ PASS | W12 Day 2 |
| 2 | LLM MODEL | Qwen3.5-397B-A17B | ✅ PASS | W12 Day 2 |
| 3 | #PinnedDocs | 4 docs @ v3.2.3.1 | ✅ PASS | W12 Day 2 |
| 4 | SYSTEM PROMPT | Season tag + INSTANCE IDENTITY + {instance_name} + #FELG | ✅ PASS | W12 Day 2, 07:35 MDT |
| 5 | WORKSPACE PROMPTS + CONFIG | BP-053 + BP-054 + BP-061 + {instance_name} + #FELG | ✅ PASS | W12 Day 2, 07:35 MDT |
| 6 | USER-IDENTITY | Owner(s) current | ✅ PASS | W12 Day 2 |
| 7 | RAG SYNC | GitHub connector | ✅ PASS | W12 Day 2 |
| 8 | #ContextVolley | Reach INT-M01 | ✅ PASS | W12 Day 2 |

**ISC Progress: 8/8 (100%)** ✅ **CERTIFIED**

### ISC Attestation

| Field | Value |
|-------|-------|
| **RESULT** | ✅ **CERTIFIED — 8/8** |
| Score | **100%** |
| Certifier | @GTM |
| Date | 2026-03-17 (W12 Day 2, 07:35 MDT) |
| REF | GTM_2026-W12_185 |
| Instance | INT-M02 |

---

## 📋 L-182 COMPLIANCE — {instance_name}

| Field | Value |
|-------|-------|
| **Static Variable** | `{instance_name}` |
| **Value** | `INT-M02` |
| **Description** | `METAQWEN \| #MetaAgentQwen \| meta-qwen.weown.tools` |
| **Created** | 23:38 MDT · Mon 16 Mar 2026 (W12 Day 1) |
| **Created By** | @GTM (a-gtm_dev) |
| **R-218 Priority** | **#1 GROUND TRUTH** |
| **System Prompt** | ✅ Updated (v3.2.3.3) |
| **Workspace Prompt** | ✅ Updated (v3.2.3.3) |

> **🔒 L-182 COMPLIANT:** {instance_name} created + integrated into both prompts. R-218 Priority #1 GROUND TRUTH.

---

## 📋 #FELG CULTURE — INTEGRATED

| Field | Value |
|-------|-------|
| **Culture** | **#FELG (Fun 🎉 + Earning 💰 + Learning 📚 + Giving 🫶)** |
| **D-070 Status** | ✅ GH LIVE (v3.2.3.1) |
| **System Prompt** | ✅ Updated (v3.2.3.3) |
| **Workspace Prompt** | ✅ Updated (v3.2.3.3) |
| **#FELG Check** | ✅ **4/4** |

> **🏆 #FELG INTEGRATED:** Culture-first agent behavior enabled in both prompts.

---

## 📋 Discovered By (BP-047)

| CCC | Contributor | Role | Context |
|-----|-------------|------|---------|
| GTM | @GTM | Co-Founder / Chief Digital Alchemist | INT-M02 deployment planning + governance |
| SHD | @SHD | Sr. Full-Stack DevOps Engineer | INT-M02 infrastructure deployment (DO + Caddy) |

---

## 📋 Related Documents

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| SharedKernel | v3.2.3.1 | GTM_2026-W11_118 | GTM_2026-W11_139 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/SharedKernel.md) |
| BEST-PRACTICES | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/BEST-PRACTICES.md) |
| PROTOCOLS | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/PROTOCOLS.md) |
| CCC | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/CCC.md) |
| TMPL-010_ISC | v3.1.2.1 | GTM_2026-W07_071 | GTM_2026-W07_084 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_TEMPLATES_/TMPL-010_ISC.md) |
| L-182_Instance_Name_Static_Variable | v3.2.3.1 | GTM_2026-W12_164 | GTM_2026-W12_188 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_GOVERNANCE_/L-182_Instance_Name_Static_Variable.md) |
| D-070_FELG_Culture | v3.2.3.1 | GTM_2026-W12_153 | GTM_2026-W12_156 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_GOVERNANCE_/D-070_FELG_Culture.md) |

---

## 📜 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| **v3.2.3.2** | **2026-W12** | **GTM_2026-W12_197** | **GTM_2026-W12_200** | W12 Day 2 UPDATES — ALL 13 steps COMPLETE; **ISC 8/8 CERTIFIED (07:35 MDT) [GTM_2026-W12_185]**; {instance_name} created (L-182); **#FELG integrated (D-070)**; System Prompt v3.2.3.3 deployed; Workspace Prompt v3.2.3.3 deployed; L-182 GH LIVE; **Cross-instance VSA 231/231 PASS**; Timeline updated (ahead of schedule); Metadata enhancements (instance_description, instance_domain, instance_name, instance_status, Owner CCC-ID link) |
| v3.2.3.1 | 2026-W12 | GTM_2026-W12_053 | GTM_2026-W12_065 | INT-M02 deployment plan DRAFT (NEVER UPLOADED); Infrastructure + Onboarding complete (10/24 steps); Configuration in progress (12/24); Target ISC: W12 Day 2-3; Gate 2 findings fixed (version, BP-047, #LLMmodel) |

---

#FlowsBros #FedArch #INT-M02 #DualMETA #PRJ-033 #WeOwnSeason003 #ISC88

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
