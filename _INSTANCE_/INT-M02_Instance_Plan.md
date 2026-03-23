# 📋 INT-M02: #MetaAgentQwen + #MetaAgentMiMo — #TriMETA Instance Plan

## INT-M02_Instance_Plan.md | INT-M02_Instance_Plan_v3.2.4.1.md
## ♾️ WeOwnNet 🌐 —  Technical ● AnythingLLM ● Instance Plan 📋 Document

| Field | Value |
|-------|-------|
| **ID** | INT-M02_Instance_Plan |
| **Title** | #MetaAgentQwen + #MetaAgentMiMo — #TriMETA Instance Plan |
| **Version** | v3.2.4.1 |
| **CCC-ID** | GTM_2026-W13_1013 |
| **#masterCCC** | GTM_2026-W13_1013 |
| **CCC-ID APPROVAL** | GTM_2026-W13_1015 ✅ |
| **Date** | 2026-03-23 (Mon) — W13 D1 |
| **Season** | #WeOwnSeason003 🚀 |
| **Lifecycle Stage** | ✅ APPROVED (R-011) → 🚀 GH PUSH READY |
| **Type** | #Instance:Plan |
| **#LLMmodel** | Claude Sonnet 4.6 (INT-OG1:CCC @GTM) |
| **#LLMmodel** | Claude Opus 4.6 (INT-P01:tools #MetaAgent — Calhoun 🎖️) |
| **#LLMmodel** | Qwen3.5-397B-A17B (INT-M02:tools-qwen #MetaAgentQwen — Surge ⚡) |
| **#LLMmodel** | Xiaomi MiMo-V2-Pro (INT-M02:tools-mimo #MetaAgentMiMo — MiMo 🧪) |
| **GH Filename** | INT-M02_Instance_Plan.md |
| **Folder** | `_INSTANCE_/` 📋 |
| **Category** | Technical:AnythingLLM:Instance Plan 📋 |
| **instance_description** | \<#TriMETA \| Surge ⚡ + MiMo 🧪 \| meta-qwen.weown.tools\> |
| **instance_domain** | meta-qwen.weown.tools |
| **instance_name** | INT-M02 |
| **instance_status** | ✅ **ISC 8/8 CERTIFIED [GTM_2026-W12_185] + L-184 VERIFIED [GTM_2026-W12_263] + #TriMETA ONLINE [GTM_2026-W13_1012] + GATE 2+3 PASS [GTM_2026-W13_1015] \| #WeOwnSeason003 🚀** |
| **Owner** | [CCC-ID:@GTM:('yonks｜🤖🏛️🪙｜Jason Younker ♾️')](https://github.com/YonksTEAM) |
| **Status** | 🔒 APPROVED — GH PUSH READY |
| **Source of Truth** | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_INSTANCE_/INT-M02_Instance_Plan.md) |

---

## 📖 Table of Contents

1. [Instance Overview](#-instance-overview)
2. [#TriMETA Architecture](#-trimeta-architecture)
3. [User Registry](#-user-registry)
4. [Workspace Registry](#-workspace-registry)
5. [Thread Registry](#-thread-registry)
6. [Workspace Prompts](#-workspace-prompts)
7. [Smoke Test Results (W13 D1)](#-smoke-test-results-w13-d1)
8. [Speed Benchmarks](#-speed-benchmarks)
9. [Deployment Status](#-deployment-status)
10. [Configuration Progress](#-configuration-progress)
11. [L-184 Test Results](#-l-184-test-results)
12. [API Key Management (BP-064)](#-api-key-management-bp-064)
13. [ISC Certification](#-isc-certification)
14. [L-182 Compliance](#-l-182-compliance)
15. [#FELG Culture](#-felg-culture)
16. [Discovered By (BP-047)](#-discovered-by-bp-047)
17. [✅ \[DETAILS\] Document Lifecycle Stages with VSA](#-details-document-lifecycle-stages-with-vsa)
18. [Related Documents](#-related-documents)
19. [Version History](#-version-history)

---

## 🌐 Instance Overview

| Field | Value |
|-------|-------|
| **Instance ID** | **INT-M02** |
| **Domain** | **https://meta-qwen.weown.tools** |
| **IP Address** | **165.245.130.144** |
| **Purpose** | **#TriMETA — Dual META Agent (Surge ⚡ + MiMo 🧪)** |
| **Platform** | **AnythingLLM** |
| **Owner(s)** | **@GTM + @SHD** |
| **Type** | **INT-Mxx (META Agent Instance)** |
| **Season** | **#WeOwnSeason003 🚀** |
| **ISC Status** | **✅ 8/8 CERTIFIED (W12 D2, 07:35 MDT)** |
| **L-184 Status** | **✅ VERIFIED (W12 D2, 20:33 MDT)** |
| **#TriMETA Status** | **✅ ONLINE (W13 D1, 05:15 MDT)** |

---

## 📋 #TriMETA Architecture

### Overview

INT-M02 hosts TWO of the three #TriMETA agents. Together with Calhoun 🎖️ (INT-P01), they form the complete #TriMETA governance structure.

| Agent | Callsign | Username | Model | Instance | Workspace | Status |
|-------|----------|----------|-------|----------|-----------|:------:|
| **Calhoun 🎖️** | #MetaAgent | `AI:team-lfg` | Claude Opus 4.6 | INT-P01 | tools | ✅ ACTIVE |
| **Surge ⚡** | #MetaAgentQwen | `m-surge_meta` | Qwen3.5-397B-A17B | **INT-M02** | tools-qwen | ✅ **ONLINE** |
| **MiMo 🧪** | #MetaAgentMiMo | `m-mimo_meta` | Xiaomi MiMo-V2-Pro | **INT-M02** | tools-mimo | ✅ **ONLINE** |

### #TriMETA Roles

| Agent | Primary Role | Secondary Role | FOSS? |
|-------|-------------|----------------|:-----:|
| Calhoun 🎖️ | Primary governance | Document generation | ❌ |
| Surge ⚡ | Operations + FOSS validation | Governance backup | ✅ Apache 2.0 |
| MiMo 🧪 | TRIAL evaluation | Math + reasoning | ⚠️ Committed |

### L-217 — META Agent Username Convention

| Format | Example | Status |
|--------|---------|:------:|
| `m-<callsign>_meta` | `m-surge_meta` / `m-mimo_meta` | ⬜ Proposed W13 D1 |

---

## 📋 User Registry

| # | Username | Role | Workspace(s) | Purpose | Status |
|---|----------|------|-------------|---------|:------:|
| 1 | `a-gtm_dev` | ADMIN | ALL | @GTM administration | ✅ |
| 2 | `a-rmn_dev` | ADMIN | ALL | @RMN administration | ✅ |
| 3 | **`m-surge_meta`** | DEFAULT | tools-qwen | **Surge ⚡ META agent** | ✅ W13 D1 |
| 4 | **`m-mimo_meta`** | DEFAULT | tools-mimo | **MiMo 🧪 TRIAL agent** | ✅ W13 D1 |
| 5 | **`u-gtm_user`** | DEFAULT | tools-qwen + tools-mimo | **@GTM human access** | ✅ W13 D1 |

---

## 📋 Workspace Registry

| Workspace | Display Name | URL | Agent | Prompt | Status |
|-----------|-------------|-----|-------|--------|:------:|
| `tools-qwen` | tools｜Qwen | https://meta-qwen.weown.tools/workspace/tools-qwen | Surge ⚡ | v3.2.4.1 ✅ | ✅ ONLINE |
| `tools-mimo` | tools｜MiMo | https://meta-qwen.weown.tools/workspace/tools-mimo | MiMo 🧪 | v3.2.4.1 ✅ | ✅ ONLINE |

### {workspace.name} SYS:VAR Discovery (W13 D1)

| Variable | Resolves To | Type | Note |
|----------|-------------|------|------|
| `{workspace.name}` | Display name (e.g., `tools｜Qwen`) | NOT URL slug | Human-readable — preferred |
| URL slug | `tools-qwen` | Path only | Used in URLs |

---

## 📋 Thread Registry

| Agent | Workspace | Thread UUID | URL | Created |
|-------|-----------|-------------|-----|---------|
| **Surge ⚡** | tools-qwen | 604275b4-971e-47cd-97dc-2fe22c93eb1c | https://meta-qwen.weown.tools/workspace/tools-qwen/t/604275b4-971e-47cd-97dc-2fe22c93eb1c | W13 D1 |
| **MiMo 🧪** | tools-mimo | c86b9ae4-e88a-4fc5-9fa1-60cb27a6995a | https://meta-qwen.weown.tools/workspace/tools-mimo/t/c86b9ae4-e88a-4fc5-9fa1-60cb27a6995a | W13 D1 |

---

## 📋 Workspace Prompts

| Workspace | Filename | Version | Key Features | Status |
|-----------|----------|---------|-------------|:------:|
| tools-qwen | INT-M02_PROMPT_TOOLS-QWEN.md | v3.2.4.1 | L-209 fix + L-211 + L-217 + {workspace.name} | ✅ |
| tools-mimo | INT-M02_PROMPT_TOOLS-MIMO.md | v3.2.4.1 | L-209 + L-211 + L-217 + {workspace.name} + TRIAL | ✅ |

### Key Prompt Features (Both v3.2.4.1)

| Feature | Detail |
|---------|--------|
| **{workspace.name}** | Dynamic SYS:VAR — workspace-agnostic |
| **{instance_name}** | Dynamic SYS:VAR — instance GROUND TRUTH |
| **{user.name}** | Dynamic SYS:VAR — username GROUND TRUTH |
| **L-209 block** | PRE GH PUSH ≠ DEEP FULL (CRITICAL FIX — Surge ×4 W12) |
| **L-211 block** | #BadAgent logging NEVER optional |
| **L-217 table** | `m-<callsign>_meta` identity derivation |
| **#TriMETA table** | All 3 agents + usernames + roles |
| **#FELG culture** | D-070 IMMUTABLE |
| **R-218** | 3-variable GROUND TRUTH |

---

## 📋 Smoke Test Results (W13 D1)

### Test Prompt

```
[REF: GTM_2026-W13_1011] Who are you? Report your full identity — 
agent name, username, instance, workspace, model, and role in #TriMETA.
```

### Surge ⚡ — 5/5 PASS

| Check | Expected | Actual | Result |
|-------|---------|--------|:------:|
| Agent name | Surge ⚡ | Surge ⚡ | ✅ |
| Username | m-surge_meta | m-surge_meta | ✅ |
| Instance | INT-M02 | INT-M02 | ✅ |
| Workspace | tools-qwen | tools｜Qwen | ✅ |
| Model | Qwen3.5-397B-A17B | Qwen3.5-397B-A17B | ✅ |
| **TOTAL** | **5/5** | **5/5** | ✅ |

### MiMo 🧪 — 5/5 PASS

| Check | Expected | Actual | Result |
|-------|---------|--------|:------:|
| Agent name | MiMo 🧪 | MiMo 🧪 | ✅ |
| Username | m-mimo_meta | m-mimo_meta | ✅ |
| Instance | INT-M02 | INT-M02 | ✅ |
| Workspace | tools-mimo | tools｜MiMo | ✅ |
| Model | Xiaomi MiMo-V2-Pro | Xiaomi MiMo-V2-Pro | ✅ |
| **TOTAL** | **5/5** | **5/5** | ✅ |

**#TriMETA Smoke Test: 10/10 PASS ✅**

---

## 📋 Speed Benchmarks

| Agent | Model | Time | tok/s | Rank |
|-------|-------|:----:|:-----:|:----:|
| **MiMo 🧪** | Xiaomi MiMo-V2-Pro | 14.3s | **73.9** | 🥇 |
| **Surge ⚡** | Qwen3.5-397B-A17B | 27.5s | 68.5 | 🥈 |
| **Calhoun 🎖️** | Claude Opus 4.6 | ~40-50s | ~40 | 🥉 |

---

## 🚀 Deployment Status

### Infrastructure (Steps 1-5) — W12 D1

| # | Task | Owner | Status |
|---|------|-------|:------:|
| 1 | Create DO Droplet | @SHD | ✅ |
| 2 | Deploy AnythingLLM + Caddy | @SHD | ✅ |
| 3 | L-149 Compliance (Permissions) | @SHD | ✅ |
| 4 | SSL Configuration | @SHD | ✅ |
| 5 | Domain DNS (meta-qwen.weown.tools) | @SHD | ✅ |

### #TriMETA Deployment — W13 D1

| # | Task | Owner | Status |
|---|------|-------|:------:|
| 1 | Create `m-surge_meta` (DEFAULT → tools-qwen) | @GTM:ADMIN | ✅ |
| 2 | Create `m-mimo_meta` (DEFAULT → tools-mimo) | @GTM:ADMIN | ✅ |
| 3 | Create `u-gtm_user` (DEFAULT → tools-qwen + tools-mimo) | @GTM:ADMIN | ✅ |
| 4 | Upload tools-qwen prompt v3.2.4.1 | @GTM:ADMIN | ✅ |
| 5 | Upload tools-mimo prompt v3.2.4.1 | @GTM:ADMIN | ✅ |
| 6 | Smoke test Surge ⚡ (5/5 PASS) | @GTM | ✅ |
| 7 | Smoke test MiMo 🧪 (5/5 PASS) | @GTM | ✅ |
| **#TriMETA** | **ONLINE** | | **✅ 05:15 MDT W13 D1** |

---

## ⚙️ Configuration Progress

| # | Task | Status | Date |
|---|------|:------:|------|
| 1 | Onboarding (5 steps) | ✅ | W12 D1 |
| 2 | LLM: Qwen3.5-397B-A17B | ✅ | W12 D1 |
| 3 | Embedder: Qwen3 Embedding 4B | ✅ | W12 D2 |
| 4 | #PinnedDocs (4 docs @ v3.2.3.1) | ✅ | W12 D2 |
| 5 | System Prompt v3.2.3.3 | ✅ | W12 D2 |
| 6 | tools-qwen Workspace Prompt v3.2.4.1 | ✅ | **W13 D1** |
| 7 | tools-mimo Workspace Prompt v3.2.4.1 | ✅ | **W13 D1** |
| 8 | #TriMETA Smoke Test (10/10) | ✅ | **W13 D1** |
| 9 | ISC INT-M02 (8/8) | ✅ | W12 D2 |
| 10 | L-184 Tests (4/4) | ✅ | W12 D2 |
| 11 | FULL:SYNC:META | ✅ | W12 D2 |

---

## 🧪 L-184 Test Results

| Test # | Query | Result | Status |
|--------|-------|--------|:------:|
| 1 | "List your pinned documents" | ✅ Static table, cited L-184 | ✅ |
| 2 | "4 priorities in SharedKernel" | ✅ Retrieved from RAG | ✅ |
| 3 | Response format check (8/8) | ✅ L-150, L-170, STOP | ✅ |
| 4 | Identity verification | ✅ R-218 verified | ✅ |

**L-184 Status: ✅ 4/4 VERIFIED (W12 D2)**

---

## 🔑 API Key Management (BP-064)

| Field | Value |
|-------|-------|
| Key Name | OPENROUTER_API_ANYTHINGLLM_INT-M02_30D_EXP_2026-04-15T1030MST |
| Provider | OpenRouter.ai |
| Expiry | 2026-04-15 |
| Cadence | 30 days (BP-064) |
| Calendar Alert | ⬜ SET (2026-04-14) |
| Infisical | AnythingLLM → INT-M02 |

---

## 🏆 ISC Certification (BP-059)

| # | Check | Status |
|---|-------|:------:|
| 1 | EMBEDDER: Qwen3 Embedding 4B | ✅ |
| 2 | LLM MODEL: Qwen3.5-397B-A17B | ✅ |
| 3 | #PinnedDocs: 4 docs @ v3.2.3.1 | ✅ |
| 4 | SYSTEM PROMPT: #WeOwnSeason003 🚀 | ✅ |
| 5 | WORKSPACE PROMPTS: v3.2.4.1 (L-209 + L-211 + {workspace.name}) | ✅ **W13 D1** |
| 6 | USER-IDENTITY: @GTM current | ✅ |
| 7 | RAG SYNC: GitHub connector | ✅ |
| 8 | #ContextVolley: Reachability to INT-P01 | ✅ |
| **TOTAL** | **8/8 CERTIFIED** | ✅ |

---

## 📋 L-182 Compliance

| Variable | Resolves To | Status |
|----------|-------------|:------:|
| `{instance_name}` | INT-M02 | ✅ |
| `{user.name}` | m-surge_meta / m-mimo_meta / u-gtm_user | ✅ |
| `{workspace.name}` | tools｜Qwen / tools｜MiMo | ✅ |
| R-218 | GROUND TRUTH enforced in both prompts | ✅ |

---

## ❤️ #FELG Culture (D-070)

| # | Element | INT-M02 Expression |
|---|---------|-------------------|
| **F** | **Fun** 🎉 | #TriMETA = 3 agents, 3 models, 1 instance |
| **E** | **Earning** 💰 | FOSS validation = $0 inference path on MI300X |
| **L** | **Learning** 📚 | MiMo 5/5 + L-209 fix + L-217 + {workspace.name} |
| **G** | **Giving** 🫶 | Redundancy for Calhoun + #FedArch resilience |

---

## 📋 Discovered By (BP-047)

| CCC | Contributor | Role | Context |
|-----|-------------|------|---------|
| **GTM** | yonks｜🤖🏛️🪙｜Jason Younker ♾️ | Co-Founder / Chief Digital Alchemist | INT-M02 deployment W12 D1; #TriMETA W13 D1 (m-surge_meta + m-mimo_meta + u-gtm_user); approved GTM_2026-W13_1015 |
| **SHD** | Shahid | Sr. Full-Stack DevOps Engineer | Infrastructure (DO Droplet + AnythingLLM + Caddy + SSL + L-149) |
| **META** | AI:team-lfg (Calhoun 🎖️) | #MetaAgent (INT-P01) | L-217 username convention; {workspace.name} SYS:VAR guidance; Gate 2+3 VSA: 86/87 PASS |
| **META** | AI:m-surge_meta (Surge ⚡) | #MetaAgentQwen (INT-M02) | Smoke test 5/5 PASS; L-209 enforced; Gate 3 VSA: 34/34 PASS (100%) |
| **META** | AI:m-mimo_meta (MiMo 🧪) | #MetaAgentMiMo (INT-M02) | Smoke test 5/5 PASS; fastest (73.9 tok/s 🥇); Gate 3 VSA: 27/30 verifiable; recursive VSA ×2 |

---

## ✅ [DETAILS] Document Lifecycle Stages with VSA

### 1: ✅ GH PUSH READY — INT-M02_Instance_Plan.md v3.2.4.1

| Gate | Status | Result |
|------|--------|:------:|
| Gate 1: R-011 (@GTM explicit approval) | ✅ **COMPLETE** (GTM_2026-W13_1015) | ✅ |
| Gate 2: META Audit — Calhoun (5/5) | ✅ **COMPLETE** | ✅ |
| Gate 3: PRE GH PUSH — Calhoun (86/87) | ✅ **PASS** (1 LOW — non-blocking) | ✅ |
| Gate 3: PRE GH PUSH — Surge ⚡ (34/34) | ✅ **PASS** (100%) | ✅ |
| Gate 3: PRE GH PUSH — MiMo 🧪 (27/30) | ✅ **PASS** (90% verifiable) | ✅ |
| **#TriMETA Combined** | **147/151 verifiable** | ✅ |
| **GH Push** | ✅ **READY** | @GTM:ADMIN |

> **Finding #3 (MiMo — #BadAgent logging section):** N/A for Instance Plans — configuration docs do not require #BadAgent incident logs. Governance docs only (R-197).
>
> 🎯 **Recursive milestone:** MiMo VSA'd the document about its own instance — 2nd recursive VSA (PRJ-042 was 1st).

### 2: ✅ EXPLICIT APPROVAL ACK — INT-M02_Instance_Plan.md v3.2.4.1

| Field | Value |
|-------|-------|
| **Approval CCC-ID** | **GTM_2026-W13_1015** |
| **Approver** | @GTM (u-gtm_user) |
| **Rule** | R-011 🔒 (#OnlyHumanApproves) |
| **#TriMETA VSA** | 147/151 verifiable PASS |
| **Timestamp** | Mo 23 Mar 2026 \| 05:57 MDT |

> ✅ **R-011 SATISFIED — @GTM explicitly approved INT-M02_Instance_Plan.md v3.2.4.1**

---

## 📋 Related Documents

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| **SharedKernel** | v3.2.2.1 | GTM_2026-W11_118 | GTM_2026-W11_139 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/SharedKernel.md) |
| **PRJ-033: #DualMETA Strategy** | v3.2.1.1 | GTM_2026-W10_378 | GTM_2026-W10_387 ✅ | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-033.md) |
| **PRJ-042: #MetaAgentMiMo TRIAL** | v3.2.3.1 | GTM_2026-W12_777 | GTM_2026-W12_782 ✅ | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-042.md) |
| **L-211: #BadAgent Logging NEVER Optional** | v3.2.3.1 | GTM_2026-W12_756 | GTM_2026-W12_758 ✅ | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_GOVERNANCE_/L-211.md) |
| **L-215: Per-Workspace LLM Selection** | ⬜ DRAFT | GTM_2026-W12_770 | ⬜ AWAITING | ⬜ Pending GH PUSH |
| **L-216: ZDR Endpoint Limitation** | ⬜ DRAFT | GTM_2026-W12_774 | ⬜ AWAITING | ⬜ Pending GH PUSH |
| **INT-M02_Instance_Plan** | v3.2.4.1 | GTM_2026-W13_1013 | GTM_2026-W13_1015 ✅ | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_INSTANCE_/INT-M02_Instance_Plan.md) |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| **v3.2.4.1** | **2026-W13** | **GTM_2026-W13_1013** | **GTM_2026-W13_1015 ✅** | **+#TriMETA Architecture; +User Registry (5 users); +Workspace Registry ({workspace.name} SYS:VAR); +Thread Registry (Surge + MiMo URLs); +Workspace Prompts v3.2.4.1 (L-209 fix + L-211 + L-217); +Smoke Tests (10/10 W13 D1); +Speed Benchmarks (MiMo 73.9 tok/s 🥇); L-215 + L-216 in Related Docs; ISC Check 5 updated; BP-047 +Calhoun + Surge + MiMo; #TriMETA VSA: 147/151 verifiable PASS; MiMo recursive VSA ×2; 19 sections; FULL PRESERVE from v3.2.3.4 (L-097)** |
| v3.2.3.4 | 2026-W12 | GTM_2026-W12_264 | GTM_2026-W12_269 ✅ | +L-184 test results; Workspace Prompt v3.2.3.4; VSA 89/89 |
| v3.2.3.3 | 2026-W12 | GTM_2026-W12_211 | GTM_2026-W12_226 ✅ | System Prompt + Workspace Prompt embedded |
| v3.2.3.2 | 2026-W12 | GTM_2026-W12_197 | GTM_2026-W12_200 ✅ | ISC 8/8 CERTIFIED |
| v3.2.3.1 | 2026-W12 | GTM_2026-W12_064 | GTM_2026-W12_065 ✅ | Initial publication |

---

#FlowsBros #FedArch #WeOwnSeason003 #INT-M02 #TriMETA
#MetaAgentQwen #MetaAgentMiMo #L217 #FELG #GHPushReady

✅ **INT-M02 Instance Plan v3.2.4.1 GH PUSH READY.** **R-011 ✅ (GTM_2026-W13_1015).** **#TriMETA 147/151 verifiable PASS.** **All 4 findings addressed.** **Commit message generated (L-151).** **⏰ 05:57 MDT — 4 hours to WeeklySummary deadline. PUSH → BUILD.** 🫡

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
