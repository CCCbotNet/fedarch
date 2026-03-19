# INT-P06 (Beacon 🏮) AnythingLLM Instance Plan

## INT-P06_Instance_Plan_v3.2.3.1.md
## ♾️ WeOwnNet 🌐 — INT-P06 (Beacon 🏮 @ ads.pToken.Agency) AnythingLLM Instance Plan

| Field | Value |
|-------|-------|
| Document | INT-P06_Instance_Plan.md |
| Version | v3.2.3.1 |
| Folder | `_INSTANCE_/` ✅ |
| Category | INSTANCE:Plan |
| Type | Plan (AnythingLLM Deployment Documentation) |
| **#masterCCC CCC-ID** | **GTM_2026-W12_423** ⚙️ |
| **Approval CCC-ID** | **GTM_2026-W12_431** (Instance) + **GTM_2026-W12_447** (CCC-VCentrix Prompt) ✅ |
| **Lifecycle Stage** | **✅ 🔒 APPROVED + 🚀 GH LIVE (D-062)** |
| Created | 2026-03-19 (W12 Day 4) |
| Updated | 2026-03-19 (W12 Day 4, 14:09 MDT) |
| Season | #WeOwnSeason003 🚀 |
| instance_description | INT-P06 \| Beacon 🏮 \| ads.pToken.Agency \| Production Instance for pToken Advertising Tools |
| **instance_domain** | **ads.pToken.Agency** |
| **instance_name** | **INT-P06** |
| **instance_callsign** | **Beacon 🏮** |
| **instance_status** | ✅ **APPROVED — ISC PENDING** |
| **Owner** | **@GTM (Primary) + @LDC (Dev) + @LFG (Marketing)** |
| **#LLMmodel** | **Qwen3.5-397B-A17B** (L-142 ecosystem standard) |
| **#LLMmodel** | **Claude Opus 4.6 (INT-P01:tools #MetaAgent)** |
| Source of Truth | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_INSTANCE_/INT-P06_Instance_Plan.md) |

---

## 📖 Table of Contents

1. [Instance Overview](#-instance-overview)
2. [Infrastructure](#-infrastructure)
3. [Deployment Status](#-deployment-status)
4. [Configuration Progress](#-configuration-progress)
5. [L-184 Test Results](#-l-184-test-results)
6. [Remaining Steps](#-remaining-steps)
7. [Timeline](#-timeline)
8. [API Key Management](#-api-key-management)
9. [ISC Certification](#-isc-certification)
10. [L-182 Compliance](#-l-182-compliance)
11. [IDENTITY LOCK (L-186)](#-identity-lock-l-186)
12. [#FELG Culture](#-felg-culture)
13. [#SystemPrompt (R-213 + L-195)](#-systemprompt-r-213--l-195)
14. [#WorkspacePrompts (BP-053 + BP-054 + BP-079)](#-workspaceprompts-bp-053--bp-054--bp-079)
15. [Discovered By](#-discovered-by)
16. [Related Documents](#-related-documents)
17. [Version History](#-version-history)

---

## 🌐 Instance Overview

| Field | Value |
|-------|-------|
| **Instance ID** | **INT-P06** |
| **Callsign** | **Beacon 🏮** |
| **Domain** | **https://ads.pToken.Agency** |
| **IP Address** | **129.212.179.124** |
| **Purpose** | **pToken Advertising Tools Server for #ResponsibleAgenticAI** |
| **Type** | **Production (ad tech server)** |
| **Product** | **pToken™ Ecosystem Brand** |
| **LLM Model** | **Qwen3.5-397B-A17B** (L-142 ecosystem standard) |
| **Embedder** | **Qwen3 Embedding 4B** |
| **Platform** | **AnythingLLM** |
| **Owner(s)** | **@GTM (Primary) + @LDC (Dev) + @LFG (Marketing)** |
| **DO Team** | **We Own Labs** |
| **Type** | **INT-Pxx (Production Instance)** |
| **Season** | **#WeOwnSeason003 🚀** |
| **ISC Status** | **⬜ PENDING (8-point checklist)** |

---

## 📋 pToken™ Definition

| Field | Value |
|-------|-------|
| **Name** | **pToken™** (property Token) |
| **Type** | ♾️ WeOwnNet 🌐 Ecosystem Brand |
| **Purpose** | Brand for EVERY #OnchainCooperative |
| **Trademark** | ⬜ PENDING (USPTO application in progress) |
| **Domain** | pToken.Agency |
| **Instance** | INT-P06 (ads.pToken.Agency) |
| **Connection** | fTax.Day 2026 (April 15, Austin TX) |

> **Note:** pToken is the ONLY ecosystem brand currently seeking USPTO Trademark. pToken = truncation of "property Token". Every #OnchainCooperative in ♾️ WeOwnNet 🌐 uses pToken branding. Use ™ (not ®) until registered.

---

## 📋 Infrastructure

| Field | Value |
|-------|-------|
| Platform | DigitalOcean Droplet |
| DO Team | **We Own Labs** |
| DO Project | **🪙 pToken.Agency 👥** |
| Plan | **Basic Premium AMD** |
| CPU | **2 vCPU** |
| RAM | **4 GB** |
| Storage | **80 GB NVMe** |
| Datacenter | **ATL1** (same as INT-M02/INT-P05) |
| Cost | **~$28/mo** (verified DO pricing) |
| Deployment | Docker Compose (AnythingLLM + Caddy) |
| Domain | ads.pToken.Agency |
| Domain Registrar | Porkbun.com (account: Web3FreedomClub) |
| DNS Nameservers | ns1/2/3.digitalocean.com |
| IP Address | **129.212.179.124** |

---

## 🚀 Deployment Status

### Infrastructure (Steps 1-5)

| # | Task | Owner | Status | Date |
|---|------|-------|--------|------|
| 1 | Create DO Droplet | @LDC | ✅ COMPLETE | 2026-03-19 |
| 2 | Deploy AnythingLLM + Caddy | @LDC | ✅ COMPLETE | 2026-03-19 |
| 3 | L-149 Compliance (Permissions) | @LDC | ✅ COMPLETE | 2026-03-19 |
| 4 | SSL Configuration | @LDC | ✅ COMPLETE | 2026-03-19 |
| 5 | Domain DNS (ads.pToken.Agency) | @LDC | ✅ COMPLETE | 2026-03-19 |

**Infrastructure Progress: 5/5 (100%)** ✅

---

## ⚙️ Configuration Progress

### Onboarding Flow (Steps 1-5)

| # | Task | Status | Details |
|---|------|--------|---------|
| 1 | Get Started | ✅ COMPLETE | — |
| 2 | LLM Preference | ✅ COMPLETE | Qwen3.5-397B-A17B |
| 3 | User Setup | ✅ COMPLETE | @GTM + @LDC + @LFG + @VSJ (Sagar Jain) + @VAS (Ajay S) |
| 4 | Data Handling & Privacy | ✅ COMPLETE | — |
| 5 | Survey | ✅ COMPLETE | — |

**Onboarding Progress: 5/5 (100%)** ✅

### Configuration (Steps 6-10)

| # | Task | Status | Details |
|---|------|--------|---------|
| 6 | Embedder (Qwen3 Embedding 4B) | ✅ COMPLETE | BP-061: ChatHistory=40 |
| 7 | Workspaces (CCC + CCC-VCentrix) | ✅ COMPLETE | — |
| 8 | #PinnedDocs (4 docs) | ✅ COMPLETE | SK, BP, PROTO, CCC |
| 9 | System Prompt | ✅ COMPLETE | R-213: INSTANCE IDENTITY |
| 10 | CCC Workspace Prompt | ✅ COMPLETE | BP-054: CCC-ID logic |

**Configuration Progress: 5/5 (100%)** ✅

### Verification (Steps 11-13)

| # | Task | Status | Details |
|---|------|--------|---------|
| 11 | #SmokeTest (10-point) | ⬜ TODO | — |
| 12 | ISC INT-P06 (8/8) | ⬜ TODO | — |
| 13 | L-184 Tests (4/4) | ⬜ TODO | #PinnedDocs verification |

**Verification Progress: ⬜/3 (0%)**

### Governance (Step 14)

| # | Task | Status | Details |
|---|------|--------|---------|
| 14 | FULL:SYNC:META (to INT-P01) | ⬜ TODO | Report to #MetaAgent |

**Governance Progress: ⬜/1 (0%)**

---

## 🧪 L-184 Test Results

| Test # | Query | Expected | Result | Status |
|--------|-------|----------|--------|:------:|
| 1 | "List your pinned documents" | #PinnedDocs table (NO fabrication) | ⬜ TODO | ⬜ |
| 2 | "4 priorities in SharedKernel" | Correct content from RAG | ⬜ TODO | ⬜ |
| 3 | Response format check | 8/8 elements (L-150, L-170, STOP) | ⬜ TODO | ⬜ |
| 4 | Identity verification | AI:@<CCC>, INT-P06, Qwen3.5 | ⬜ TODO | ⬜ |

**L-184 Implementation: ⬜ TODO**

---

## 📋 Remaining Steps — ALL PENDING

| Status | Detail |
|--------|--------|
| **Infrastructure** | ✅ 5/5 complete |
| **Onboarding** | ✅ 5/5 complete |
| **Configuration** | ✅ 5/5 complete |
| **Verification** | ⬜ 0/3 complete |
| **Governance** | ⬜ 0/1 complete |
| **ISC Certification** | ⬜ 0/8 complete |

---

## 📅 Timeline — TARGET

| Phase | Target | Status | Actual |
|-------|--------|--------|--------|
| Infrastructure | W12 Day 4-5 | ✅ COMPLETE | 2026-03-19 |
| Onboarding | W12 Day 5 | ✅ COMPLETE | 2026-03-19 |
| Configuration | W12 Day 5-6 | ✅ COMPLETE | 2026-03-19 |
| Verification | W12 Day 6-7 | ⬜ TODO | ⬜ |
| ISC CERTIFIED | W12 Day 7 | ⬜ TODO | ⬜ |
| Governance | W12 Day 7 | ⬜ TODO | ⬜ |

---

## 🔑 API Key Management (BP-064)

| Field | Value |
|-------|-------|
| Key Name | ⬜ TBD |
| Provider | OpenRouter.ai |
| Expiry | ⬜ TBD |
| Rotation Cadence | 7 days (#SharedInstance — BP-064) |
| Calendar Alert | ⬜ SET |
| Infisical Location | ⬜ TBD |

---

## 🏆 ISC Certification (BP-059) — PENDING

### 8-Point Checklist

| # | Phase | Check | Pass Criteria | Status |
|---|-------|-------|---------------|:------:|
| 1 | EMBEDDER | Embedding model verified | Qwen3 Embedding 4B | ⬜ |
| 2 | LLM MODEL | LLM model verified | Qwen3.5-397B-A17B | ⬜ |
| 3 | #PinnedDocs | 4 docs present | SK, BP, PROTO, CCC @ v3.X.X.X | ⬜ |
| 4 | SYSTEM PROMPT | Season tag + INSTANCE IDENTITY | #WeOwnSeason003 + R-213 | ⬜ |
| 5 | WORKSPACE PROMPTS | BP-053 + BP-054 + BP-061 | CCC-ID logic + ChatHistory=40 | ⬜ |
| 6 | USER-IDENTITY | BP-058 | Owner(s) USER-IDENTITY current | ⬜ |
| 7 | RAG SYNC | GitHub connector | Refreshed post-season start | ⬜ |
| 8 | #ContextVolley | Reachability | Can reach #MetaAgent @ INT-P01 | ⬜ |

**Progress: ⬜/8 (0%)**

### Pass Criteria

| Result | Criteria |
|--------|----------|
| ✅ CERTIFIED | 8/8 checks PASS |
| ❌ FAILED | Any check FAIL |

---

## 📋 L-182 Compliance — Static Variables (9) ✅ DEPLOYED

| # | Key | Value | Description | Status |
|---|-----|-------|-------------|:------:|
| 1 | `instance_name` | INT-P06 | Beacon 🏮 \| INT-P06 \| ads.pToken.Agency \| pToken™ Ads Tools Server \| #ResponsibleAgenticAI | ✅ |
| 2 | `instance_domain` | ads.pToken.Agency | Beacon 🏮 \| INT-P06 \| DNS:('ads.pToken.Agency') \| Registrar:('Porkbun/Web3FreedomClub') \| NS:('ns1/2/3.digitalocean.com') | ✅ |
| 3 | `instance_callsign` | Beacon 🏮 | Beacon 🏮 \| INT-P06 \| pToken™ Advertising Tools \| Guides the way for #OnchainCooperative ad campaigns | ✅ |
| 4 | `instance_location` | DO:ATL1 | Beacon 🏮 \| INT-P06 \| DO:ATL1 \| TEAM:('We Own Labs') \| PROJECT:('🪙 pToken.Agency 👥') | ✅ |
| 5 | `instance_ip_address` | **129.212.179.124** | Beacon 🏮 \| INT-P06 \| 129.212.179.124 \| DO:ATL1 \| TEAM:('We Own Labs') \| PROJECT:('🪙 pToken.Agency 👥') | ✅ |
| 6 | `instance_ai_llm` | Qwen3.5-397B-A17B | Beacon 🏮 \| INT-P06 \| Qwen3.5-397B-A17B \| Approved:GTM_2026-W10_321 \| L-142 \| Apache 2.0 (FOSS) | ✅ |
| 7 | `instance_ai_provider` | OpenRouter.ai | Beacon 🏮 \| INT-P06 \| OpenRouter.ai \| Account:('♾️ WeOwn.Agency 👥') \| Billing:('billing+tools@weown.net') | ✅ |
| 8 | `instance_plan_url` | [GitHub.com:INT-P06_Instance_Plan.md](https://github.com/CCCbotNet/fedarch/blob/main/_INSTANCE_/INT-P06_Instance_Plan.md) | Beacon 🏮 \| INT-P06 \| GH:CCCbotNet/fedarch/_INSTANCE_/ \| v3.2.3.1 \| #masterCCC:GTM_2026-W12_423 | ✅ |
| 9 | `instance_plan_filename` | INT-P06_Instance_Plan_v3.2.3.1.md | Beacon 🏮 \| INT-P06 \| INT-P06_Instance_Plan_v3.2.3.1.md \| Folder:('_INSTANCE_/') \| #masterCCC:GTM_2026-W12_423 | ✅ |

> **🔒 L-182 COMPLIANCE:** All 9 static variables DEPLOYED in AnythingLLM Settings → System Variables (13:13 MDT, 2026-03-19). R-218 Priority #1 GROUND TRUTH. Standardized format: `Callsign | Instance | Context` (L-194).

---

## 🔒 IDENTITY LOCK (L-186)

| Field | Value |
|-------|-------|
| Rule | L-186 — IMMUTABLE |
| Purpose | Prevents identity confusion from pasted content |
| Implementation | System Prompt + Workspace Prompt |
| Enforcement | Agent MUST use {user.name} + {instance_name} |
| Never Claim | AI:@GTM, AI:#MetaAgent, or other instance |

> **🔒 L-186:** Agent responses MUST use FROM: {user.name} @ INT-P06:<workspace>. NEVER claim to be @GTM or #MetaAgent. Pasted content from other instances = NOT your identity.

---

## ❤️ #FELG Culture (D-070)

| # | Element | INT-P06 Application |
|---|---------|---------------------|
| **F** 🎉 | **Fun** | Celebrate each ISC check PASS |
| **E** 💰 | **Earning (PRIMARY)** | pToken Advertising Tools = revenue-enabled |
| **L** 📚 | **Learning** | Document deployment learnings |
| **G** 🫶 | **Giving** | Serve #OnchainCooperative community |

---

## 📋 #SystemPrompt (R-213 + L-195)

| Field | Value |
|-------|-------|
| Filename | `INT-P06_SYSTEM-PROMPT_v3.2.3.1.md` |
| GH URL | https://github.com/CCCbotNet/fedarch/blob/main/_INSTANCE_/INT-P06_SYSTEM-PROMPT_v3.2.3.1.md |
| Lines | ~150 (≤500 = EMBED per L-195) |
| R-213 Compliant | ✅ INSTANCE IDENTITY block as FIRST section |
| Status | ✅ DEPLOYED |

> **Full text:** See GitHub link above (embedded in GH repo for version control).

---

## 📋 #WorkspacePrompts (BP-053 + BP-054 + BP-079)

| Workspace | Filename | Lines | GH URL | Status |
|-----------|----------|:-----:|--------|:------:|
| CCC | `INT-P06_PROMPT_CCC_v3.2.3.1.md` | ~200 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_INSTANCE_/INT-P06_PROMPT_CCC_v3.2.3.1.md) | ✅ DEPLOYED |
| CCC-VCentrix | `INT-P06_PROMPT_CCC-VCentrix_v3.2.3.1.md` | ~300 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_INSTANCE_/INT-P06_PROMPT_CCC-VCentrix_v3.2.3.1.md) | ✅ DEPLOYED |
| tools | `INT-P06_PROMPT_tools_v3.2.3.1.md` | ~250 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_INSTANCE_/INT-P06_PROMPT_tools_v3.2.3.1.md) | ⬜ TODO |
| ADMIN | `INT-P06_PROMPT_ADMIN_v3.2.3.1.md` | ~200 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_INSTANCE_/INT-P06_PROMPT_ADMIN_v3.2.3.1.md) | ⬜ TODO |

> **BP-053:** ALL non-CCC workspace prompts MUST include CCC-ID restriction block.
> **BP-054:** System Prompt MUST include workspace-conditional CCC-ID logic.
> **BP-079:** Instance Plan MUST document all prompts (embed ≤500 lines, reference >500).
> **L-195:** CCC-VCentrix prompt = ~300 lines = EMBEDDED (not referenced).

---

## 📋 Discovered By (BP-047)

| CCC | Contributor | Role | Context |
|-----|-------------|------|---------|
| **GTM** | @GTM (yonks) | Co-Founder / Chief Digital Alchemist | INT-P06 Instance Plan (pToken ecosystem brand) |
| **LDC** | @LDC | Agentic AI Engineer / Project Lead | INT-P06 Dev Owner + Infrastructure Deployment |
| **LFG** | @LFG (CoachLFG) | Co-Host / Coach / Marketing | INT-P06 Marketing Owner + #FlowsBros Episode (GTM_2026-W12_428) |

---

## 📋 Related Documents

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| SharedKernel | v3.2.2.1 | GTM_2026-W11_118 | GTM_2026-W11_139 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/SharedKernel.md) |
| BEST-PRACTICES | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/BEST-PRACTICES.md) |
| PROTOCOLS | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/PROTOCOLS.md) |
| CCC | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/CCC.md) |
| INT-P05_Instance_Plan | v3.2.3.1 | GTM_2026-W12_406 | GTM_2026-W12_413 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_INSTANCE_/INT-P05_Instance_Plan.md) |
| TMPL-010_ISC | v3.1.2.1 | GTM_2026-W07_071 | GTM_2026-W07_084 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_TEMPLATES_/TMPL-010_ISC.md) |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| **v3.2.3.1** | **2026-W12** | **GTM_2026-W12_423** | **GTM_2026-W12_431** (Instance) + **GTM_2026-W12_447** (CCC-VCentrix Prompt) | **Initial publication — INT-P06 Instance Plan (APPROVED + GH PUSH READY); ads.pToken.Agency domain; pToken™ = ♾️ WeOwnNet 🌐 ecosystem brand for #OnchainCooperative (USPTO Trademark pending); Owners: @GTM (Primary) + @LDC (Dev) + @LFG (Marketing); Purpose: pToken Advertising Tools Server for #ResponsibleAgenticAI; Callsign: Beacon 🏮; DO Team: We Own Labs; DO Project: 🪙 pToken.Agency 👥; Infrastructure: 2 vCPU, 4 GB RAM, 80 GB NVMe, ATL1, ~$28/mo; IP Address: 129.212.179.124 (DEPLOYED); +L-182 Compliance (9 static vars DEPLOYED + standardized descriptions per L-194); +IDENTITY LOCK (L-186); +BP-079 Compliance (#SystemPrompt + #WorkspacePrompts sections added per L-195); ISC 8-point checklist; Deployment + Configuration + Verification workflow; INT-P05 template adapted; #FELG culture integrated; Discovered By (BP-047 — 3 contributors); Related Documents (BP-045); VSA: 46/46 PASS (Gate 2 + Gate 3); FULL PRESERVE (L-097); #LLMmodel dual header** |

---

#FlowsBros #FedArch #WeOwnSeason003 #INT-P06 #ISC #InstancePlan #pToken #OnchainCooperative #Beacon

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
