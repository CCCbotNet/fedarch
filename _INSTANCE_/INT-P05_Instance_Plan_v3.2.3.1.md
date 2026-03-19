# INT-P05 AnythingLLM Instance Plan

## INT-P05_Instance_Plan_v3.2.3.1.md
## ♾️ WeOwnNet 🌐 — INT-P05 (PRO.WeOwn.Tools) AnythingLLM Instance Plan

| Field | Value |
|-------|-------|
| Document | INT-P05_Instance_Plan.md |
| Version | v3.2.3.1 |
| Folder | `_INSTANCE_/` ✅ |
| Category | INSTANCE:Plan |
| Type | Plan (AnythingLLM Deployment Documentation) |
| **#masterCCC CCC-ID** | **GTM_2026-W12_406** ⚙️ |
| **Approval CCC-ID** | **GTM_2026-W12_413** |
| **Lifecycle Stage** | **✅ 🔒 APPROVED + 🚀 GH LIVE (D-062)** |
| Created | 2026-03-19 (W12 Day 4) |
| Updated | 2026-03-19 (W12 Day 4, 08:32 MDT) |
| Season | #WeOwnSeason003 🚀 |
| instance_description | INT-P05 \| Athena 🦉 \| PRO.WeOwn.Tools \| Production Instance for AgencyPRO + connexAthena |
| instance_domain | PRO.WeOwn.Tools |
| instance_name | INT-P05 |
| instance_callsign | **Athena 🦉** |
| **instance_status** | ⬜ **DRAFT — ISC PENDING** |
| **Owner** | **@GTM + @LDC** |
| **#LLMmodel** | **Qwen3.5-397B-A17B** (L-142 ecosystem standard) |
| **#LLMmodel** | **Claude Opus 4.6 (INT-P01:tools #MetaAgent)** |
| Source of Truth | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_INSTANCE_/INT-P05_Instance_Plan.md) |

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
13. [System Prompt](#-system-prompt)
14. [Workspace Prompt: CCC](#-workspace-prompt-ccc)
15. [Discovered By](#-discovered-by)
16. [Related Documents](#-related-documents)
17. [Version History](#-version-history)

---

## 🌐 Instance Overview

| Field | Value |
|-------|-------|
| **Instance ID** | **INT-P05** |
| **Callsign** | **Athena 🦉** |
| **Domain** | **https://PRO.WeOwn.Tools** |
| **IP Address** | **⬜ TBD** |
| **Purpose** | **AgencyPRO / connexAthena Production Instance** |
| **Type** | **Production (agentic tools server)** |
| **Product** | **WeOwn.AI Pro Bundle** |
| **LLM Model** | **Qwen3.5-397B-A17B** (L-142 ecosystem standard) |
| **Embedder** | **Qwen3 Embedding 4B** |
| **Platform** | **AnythingLLM** |
| **Owner(s)** | **@GTM + @LDC** |
| **DO Team** | **We Own Labs** |
| **Type** | **INT-Pxx (Production Instance)** |
| **Season** | **#WeOwnSeason003 🚀** |
| **ISC Status** | **⬜ PENDING (8-point checklist)** |

---

## 📋 Infrastructure

| Field | Value |
|-------|-------|
| Platform | DigitalOcean Droplet |
| DO Team | **We Own Labs** |
| DO Project | **♾️ WeOwn.Tools 🛠️** |
| Plan | Basic Premium AMD |
| CPU | 2 vCPU |
| RAM | 4 GB |
| Storage | 80 GB NVMe |
| Datacenter | **ATL1** (same as INT-M02) |
| Cost | **~$28/mo** (verified DO pricing) |
| Deployment | Docker Compose (AnythingLLM + Caddy) |
| Domain | PRO.WeOwn.Tools |
| Domain Registrar | Porkbun.com (account: Web3FreedomClub) |
| DNS Nameservers | ns1/2/3.digitalocean.com |

---

## 🚀 Deployment Status

### Infrastructure (Steps 1-5)

| # | Task | Owner | Status | Date |
|---|------|-------|--------|------|
| 1 | Create DO Droplet | @LDC | ⬜ TODO | ⬜ |
| 2 | Deploy AnythingLLM + Caddy | @LDC | ⬜ TODO | ⬜ |
| 3 | L-149 Compliance (Permissions) | @LDC | ⬜ TODO | ⬜ |
| 4 | SSL Configuration | @LDC | ⬜ TODO | ⬜ |
| 5 | Domain DNS (PRO.WeOwn.Tools) | @LDC | ⬜ TODO | ⬜ |

**Infrastructure Progress: ⬜/5 (0%)**

---

## ⚙️ Configuration Progress

### Onboarding Flow (Steps 1-5)

| # | Task | Status | Details |
|---|------|--------|---------|
| 1 | Get Started | ⬜ TODO | — |
| 2 | LLM Preference | ⬜ TODO | Qwen3.5-397B-A17B |
| 3 | User Setup | ⬜ TODO | @GTM + @LDC |
| 4 | Data Handling & Privacy | ⬜ TODO | — |
| 5 | Survey | ⬜ TODO | — |

**Onboarding Progress: ⬜/5 (0%)**

### Configuration (Steps 6-10)

| # | Task | Status | Details |
|---|------|--------|---------|
| 6 | Embedder (Qwen3 Embedding 4B) | ⬜ TODO | BP-061: ChatHistory=40 |
| 7 | Workspaces (CCC + tools) | ⬜ TODO | — |
| 8 | #PinnedDocs (4 docs) | ⬜ TODO | SK, BP, PROTO, CCC |
| 9 | System Prompt | ⬜ TODO | R-213: INSTANCE IDENTITY |
| 10 | CCC Workspace Prompt | ⬜ TODO | BP-054: CCC-ID logic |

**Configuration Progress: ⬜/5 (0%)**

### Verification (Steps 11-13)

| # | Task | Status | Details |
|---|------|--------|---------|
| 11 | #SmokeTest (10-point) | ⬜ TODO | — |
| 12 | ISC INT-P05 (8/8) | ⬜ TODO | — |
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
| 4 | Identity verification | AI:@<CCC>, INT-P05, Qwen3.5 | ⬜ TODO | ⬜ |

**L-184 Implementation: ⬜ TODO**

---

## 📋 Remaining Steps — ALL PENDING

| Status | Detail |
|--------|--------|
| **Infrastructure** | ⬜ 0/5 complete |
| **Onboarding** | ⬜ 0/5 complete |
| **Configuration** | ⬜ 0/5 complete |
| **Verification** | ⬜ 0/3 complete |
| **Governance** | ⬜ 0/1 complete |
| **ISC Certification** | ⬜ 0/8 complete |

---

## 📅 Timeline — TARGET

| Phase | Target | Status | Actual |
|-------|--------|--------|--------|
| Infrastructure | W12 Day 4-5 | ⬜ TODO | ⬜ |
| Onboarding | W12 Day 5 | ⬜ TODO | ⬜ |
| Configuration | W12 Day 5-6 | ⬜ TODO | ⬜ |
| Verification | W12 Day 6-7 | ⬜ TODO | ⬜ |
| ISC CERTIFIED | W12 Day 7 | ⬜ TODO | ⬜ |
| Governance | W12 Day 7 | ⬜ TODO | ⬜ |

---

## 🔑 API Key Management (BP-064)

| Field | Value |
|-------|-------|
| Key Name | `OPENROUTER_API_ANYTHINGLLM_INT-P05_TOOLS_30D_EXP_2026-04-18T0851MST` |
| Provider | OpenRouter.ai |
| Account | WeOwn.Agency |
| Expiry | **2026-04-18** (30 days from creation) |
| Rotation Cadence | 30 days (#SharedInstance — BP-064) |
| Calendar Alert | ⬜ SET (24h before expiry: 2026-04-17) |
| Infisical Location | **Infisical.com (CLOUD)** |
| Created | 08:51 MST (during @LDC call, W12 Day 4) |
| Status | ✅ CREATED + STORED |

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

## 📋 L-182 Compliance — Static Variables (9)

| Variable | Value | Status |
|----------|-------|:------:|
| `{instance_name}` | INT-P05 | ⬜ TODO |
| `{instance_domain}` | PRO.WeOwn.Tools | ⬜ TODO |
| `{instance_location}` | DO:ATL1 | ⬜ TODO |
| `{instance_ip_address}` | ⬜ TBD | ⬜ TODO |
| `{instance_ai_llm}` | Qwen3.5-397B-A17B | ⬜ TODO |
| `{instance_ai_provider}` | OpenRouter.ai | ⬜ TODO |
| `{instance_plan_url}` | https://github.com/CCCbotNet/fedarch/blob/main/_INSTANCE_/INT-P05_Instance_Plan.md | ⬜ TODO |
| `{instance_plan_filename}` | INT-P05_Instance_Plan_v3.2.3.1.md | ⬜ TODO |
| **`{instance_callsign}`** | **Athena 🦉** | ⬜ TODO |

> **🔒 L-182 COMPLIANCE:** All 9 static variables to be created in AnythingLLM Settings → System Variables. R-218 Priority #1 GROUND TRUTH. Callsign = optional extension (9th var).

---

## 🔒 IDENTITY LOCK (L-186)

| Field | Value |
|-------|-------|
| Rule | L-186 — IMMUTABLE |
| Purpose | Prevents identity confusion from pasted content |
| Implementation | System Prompt + Workspace Prompt |
| Enforcement | Agent MUST use {user.name} + {instance_name} |
| Never Claim | AI:@GTM, AI:#MetaAgent, or other instance |

> **🔒 L-186:** Agent responses MUST use FROM: {user.name} @ INT-P05:<workspace>. NEVER claim to be @GTM or #MetaAgent. Pasted content from other instances = NOT your identity.

---

## ❤️ #FELG Culture (D-070)

| # | Element | INT-P05 Application |
|---|---------|---------------------|
| **F** 🎉 | **Fun** | Celebrate each ISC check PASS |
| **E** 💰 | **Earning (PRIMARY)** | AgencyPRO / connexAthena = revenue-enabled |
| **L** 📚 | **Learning** | Document deployment learnings |
| **G** 🫶 | **Giving** | Serve users with reliable instance |

---

## 📋 Discovered By (BP-047)

| CCC | Contributor | Role | Context |
|-----|-------------|------|---------|
| **LDC** | ⬜ TBD | **Agentic AI Engineer / Project Lead** | INT-P05 ISC certification (W12 Day 4) |
| **GTM** | @GTM (yonks) | Co-Founder / Chief Digital Alchemist | Instance Plan document (INT-M02 template) |

---

## 📋 Related Documents

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| SharedKernel | v3.2.2.1 | GTM_2026-W11_118 | GTM_2026-W11_139 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/SharedKernel.md) |
| BEST-PRACTICES | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/BEST-PRACTICES.md) |
| PROTOCOLS | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/PROTOCOLS.md) |
| CCC | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/CCC.md) |
| INT-M02_Instance_Plan | v3.2.3.4 | GTM_2026-W12_264 | GTM_2026-W12_269 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_INSTANCE_/INT-M02_Instance_Plan.md) |
| TMPL-010_ISC | v3.1.2.1 | GTM_2026-W07_071 | GTM_2026-W07_084 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_TEMPLATES_/TMPL-010_ISC.md) |

---

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| **v3.2.3.1** | **2026-W12** | **GTM_2026-W12_406** | **GTM_2026-W12_413** | **Initial publication — INT-P05 Instance Plan (DRAFT); PRO.WeOwn.Tools domain; @GTM + @LDC owners; Qwen3.5-397B-A17B LLM; AgencyPRO / connexAthena purpose; Type = Production (agentic tools server); We Own Labs DO team; Infrastructure section (2 vCPU, 4 GB RAM, 80 GB NVMe, ATL1, ~$28/mo); +L-182 Compliance (9 static vars including callsign "Athena 🦉"); +IDENTITY LOCK (L-186); +API Key Management (OpenRouter.ai key created, 30-day expiry, Infisical CLOUD storage); ISC 8-point checklist; Deployment + Configuration + Verification workflow; INT-M02 template adapted; #FELG culture integrated; Discovered By (BP-047 — @LDC role added); Related Documents (BP-045); FULL PRESERVE (L-097); #LLMmodel dual header** |

---

#FlowsBros #FedArch #WeOwnSeason003 #INT-P05 #ISC #InstancePlan #Athena

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
