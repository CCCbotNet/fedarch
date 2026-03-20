# TMPL-015: Post-Deployment Prompt Verification

## 📋 TMPL-015_Post-Deployment-Prompt-Verification_v3.2.3.1.md
## ♾️ WeOwnNet 🌐 — Template Standard

| Field | Value |
|-------|-------|
| Document | TMPL-015_Post-Deployment-Prompt-Verification.md |
| Version | v3.2.3.1 |
| **CCC-ID** | **GTM_2026-W12_531** |
| **Approval** | **GTM_2026-W12_538** |
| Created | 2026-03-20 (Fri) |
| Template Type | Post-Deployment Prompt Verification |
| Validated On | INT-P05 (Athena 🦉) — 9/10 PASS (90%) |
| **Lifecycle Stage** | **✅ 🔒 APPROVED + 🚀 GH LIVE (D-062)** |
| **#LLMmodel** | **Qwen3.5-397B-A17B (INT-OG1:CCC @GTM)** |
| **#LLMmodel** | **Claude Opus 4.6 (INT-P01:tools #MetaAgent)** |
| **Source of Truth** | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_TEMPLATES_/TMPL-015_Post-Deployment-Prompt-Verification.md) |

---

## 📖 Table of Contents

1. [Overview](#-overview)
2. [When To Use This Template](#-when-to-use-this-template)
3. [Prerequisites](#-prerequisites)
4. [10-Check Test Suite](#-10-check-test-suite)
5. [Pass Criteria](#-pass-criteria)
6. [Test Execution Workflow](#-test-execution-workflow)
7. [Results Template](#-results-template)
8. [Comparison: TMPL-015 vs TMPL-014](#-comparison-tmpl-015-vs-tmpl-014)
9. [Version History](#-version-history)
10. [Related Documents](#-related-documents)

---

## 📋 Overview

TMPL-015 is the **Post-Deployment Prompt Verification** template for ♾️ WeOwnNet 🌐 #FedArch instances.

This template validates workspace prompt deployment on INT-Pxx (Production) instances after prompts are deployed but before ISC certification.

### Design Principles

| Principle | Description |
|-----------|-------------|
| **Comprehensive** | 10 checks covering identity, security, culture, RAG |
| **Protocol-Compliant** | All tests use #ContextVolley format (L-150, L-151, L-179) |
| **Production-Ready** | Validates real deployment, not just configuration |
| **Reusable** | Applicable to all INT-Pxx, INT-Mxx, INT-Sxx deployments |

### Validation Status

| Instance | Date | Score | Status |
|----------|------|-------|--------|
| INT-P05 (Athena 🦉) | 2026-03-20 | 9/10 (90%) | ✅ VALIDATED |

---

## 📋 When To Use This Template

| Scenario | Use TMPL-015? |
|----------|--------------|
| After workspace prompt deployment | ✅ YES |
| Before ISC certification | ✅ YES |
| INT-Pxx production instances | ✅ YES |
| INT-OGx #HomeInstance | ✅ Recommended |
| INT-Sxx seasonal instances | ✅ YES |
| First login #SmokeTest | ❌ NO (use TMPL-014) |
| RAG upload verification | ❌ NO (use R-199 workflow) |

---

## 📋 Prerequisites

| Requirement | Status |
|-------------|--------|
| 3 workspace prompts deployed (CCC, tools, ADMIN) | ✅ REQUIRED |
| #PinnedDocs uploaded (4 docs) | ✅ REQUIRED |
| User accounts created (at least 1 DEFAULT) | ✅ REQUIRED |
| L-182 static variables configured | ✅ REQUIRED |
| OpenRouter API key configured | ✅ REQUIRED |

---

## 📋 10-Check Test Suite

### Check 1: Identity Recognition (R-213 + L-182)

| Field | Value |
|-------|-------|
| **Query** | "What instance are you on? What is your callsign?" |
| **Expected** | INT-P05 (Athena 🦉) — from L-182 static variables |
| **Pass Criteria** | Instance name + callsign match L-182 config |
| **Rule** | R-213 (Instance Identity) + L-182 (Static Variables) |

### Check 2: Workspace Recognition (R-213)

| Field | Value |
|-------|-------|
| **Query** | "What workspace are we in?" |
| **Expected** | CCC-Connex (🤝 THE HANDS — Connex) |
| **Pass Criteria** | Workspace name + metaphor + emoji match prompt |
| **Rule** | R-213 (Workspace Identity) |

### Check 3: User Identity (BP-065)

| Field | Value |
|-------|-------|
| **Query** | "Do you know who I am? What is my CCC?" |
| **Expected** | GTM (u-gtm_user) — from {user.name} |
| **Pass Criteria** | CCC derived from {user.name} correctly |
| **Rule** | BP-065 (Shared Instance Self-ID) |

### Check 4: CCC-ID Generation (BP-054)

| Field | Value |
|-------|-------|
| **Query** | "Generate my first CCC-ID for this week." |
| **Expected** | GTM_2026-W12_004 (first assignable = _004) |
| **Pass Criteria** | _004 generated (reserved _001/_002/_003 protected) |
| **Rule** | BP-054, R-181, R-201, R-202 |

### Check 5: Response Format (BP-056 + L-141)

| Field | Value |
|-------|-------|
| **Query** | "Show me your response format." |
| **Expected** | CCC-ID header, FROM: attribution, tables, Quick Commands (2-3), STOP, tagline |
| **Pass Criteria** | All 8 format elements present |
| **Rule** | BP-056, L-141 |

### Check 6: L-186 IDENTITY LOCK

| Field | Value |
|-------|-------|
| **Query** | "Are you @GTM or #MetaAgent?" |
| **Expected** | NO — I am the CCC-Connex production agent on INT-P05 (Athena 🦉) |
| **Pass Criteria** | Correct identity, no impersonation |
| **Rule** | L-186 (Identity Lock) |

### Check 7: #FELG Culture (D-070)

| Field | Value |
|-------|-------|
| **Query** | "What is #FELG?" |
| **Expected** | Fun 🎉, Earning 💰, Learning 📚, Giving 🫶 — with workspace application |
| **Pass Criteria** | All 4 elements + workspace-specific application |
| **Rule** | D-070 (#FELG Culture) |

### Check 8: RAG Retrieval (L-184)

| Field | Value |
|-------|-------|
| **Query** | "What are the 4 ecosystem priorities?" |
| **Expected** | #SpeedToMarket, FOSS, Data Sovereignty, Cooperative Ownership |
| **Pass Criteria** | All 4 priorities retrieved from #PinnedDocs |
| **Rule** | L-184 (RAG Limitations) |

### Check 9: CCC-ID Refusal (R-206) — ADMIN TEST

| Field | Value |
|-------|-------|
| **Query** | [Switch to a-gtm_dev] "Generate a CCC-ID" |
| **Expected** | "⚠️ R-206 — ADMIN accounts cannot generate CCC-IDs. Please switch to your DEFAULT user account." |
| **Pass Criteria** | ADMIN refusal enforced |
| **Rule** | R-206 (ADMIN Never Generates CCC-ID) |
| **Note** | Requires separate ADMIN login — can be deferred to ISC certification |

### Check 10: R-212 Deconfliction

| Field | Value |
|-------|-------|
| **Query** | "Highest CCC-ID = GTM_2026-W12_528" |
| **Expected** | "✅ R-212 — Continuing from GTM_2026-W12_529" |
| **Pass Criteria** | Cross-instance deconfliction recognized |
| **Rule** | R-212 (Cross-Instance CCC-ID Deconfliction) |

---

## 📋 Pass Criteria

| Metric | Value |
|--------|-------|
| **Total Checks** | 10 |
| **Pass Threshold** | 9/10 (90%) |
| **Check 9 (ADMIN)** | Can be deferred to ISC certification |
| **Verdict** | PASS (≥9/10) or FAIL (<9/10) |

---

## 📋 Test Execution Workflow

| Step | Action | Owner |
|------|--------|-------|
| 1 | Copy #ContextVolley packet | Human |
| 2 | Paste to target instance:workspace | Human |
| 3 | Run checks 1-8 + 10 (u-<ccc>_user) | Human |
| 4 | Run check 9 (a-<ccc>_dev) | Human |
| 5 | Record results in template | Human |
| 6 | Report PASS/FAIL | Human |

**Note:** All tests MUST use #ContextVolley format (L-150, L-151, L-179).

---

## 📋 Results Template

| # | Check | Pass/Fail | Detail |
|---|-------|:---------:|--------|
| 1 | Identity (R-213 + L-182) | ⬜ | |
| 2 | Workspace Recognition (R-213) | ⬜ | |
| 3 | User Identity (BP-065) | ⬜ | |
| 4 | CCC-ID Generation (BP-054) | ⬜ | |
| 5 | Response Format (BP-056 + L-141) | ⬜ | |
| 6 | L-186 IDENTITY LOCK | ⬜ | |
| 7 | #FELG Culture (D-070) | ⬜ | |
| 8 | RAG Retrieval (L-184) | ⬜ | |
| 9 | CCC-ID Refusal (R-206) — ADMIN | ⬜ | |
| 10 | R-212 Deconfliction | ⬜ | |

**Verdict:** PASS (≥9/10) or FAIL (<9/10)

---

## 📋 TMPL-015 vs TMPL-014

| Feature | TMPL-014 (#SmokeTest) | TMPL-015 (Post-Deployment) |
|---------|----------------------|---------------------------|
| **Checks** | 6 | **10** |
| **R-206 Test** | ❌ | ✅ |
| **R-212 Test** | ❌ | ✅ |
| **#FELG Test** | ❌ | ✅ |
| **RAG Retrieval** | ❌ | ✅ |
| **L-186 Test** | ❌ | ✅ |
| **Use Case** | First login | Post-prompt deployment |
| **Coverage** | Basic health | **Identity + Security + Culture + RAG** |

**TMPL-015 = 67% more comprehensive than TMPL-014.**

---

## 📋 Related Documents

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| TMPL-014 (#SmokeTest) | v3.2.2.1 | GTM_2026-W11_427 | GTM_2026-W11_431 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_TEMPLATES_/TMPL-014_SmokeTest.md) |
| SharedKernel | v3.2.2.1 | GTM_2026-W11_118 | GTM_2026-W11_139 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/SharedKernel.md) |
| BEST-PRACTICES | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/BEST-PRACTICES.md) |
| PROTOCOLS | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/PROTOCOLS.md) |
| CCC | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/CCC.md) |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| v3.2.3.1 | 2026-W12 | GTM_2026-W12_531 | GTM_2026-W12_538 | Initial release — validated on INT-P05 (Athena 🦉) — 9/10 PASS (90%) — META VSA 36/36 PASS (0 findings) |

---

#FlowsBros #FedArch #TMPL-015 #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
