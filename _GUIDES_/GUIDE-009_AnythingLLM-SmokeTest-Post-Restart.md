# GUIDE-009: AnythingLLM Smoke Test — Post-Restart Verification

## 📋 GUIDE-009_AnythingLLM-SmokeTest-Post-Restart_v3.1.1.1.md
## ♾️ WeOwnNet 🌐 — #YonksPromptingAcademy

| Field | Value |
|-------|-------|
| Document | GUIDE-009_AnythingLLM-SmokeTest-Post-Restart.md |
| Version | 3.1.1.1 |
| CCC-ID | GTM_2026-W06_503 |
| Created | 2026-02-08 (W06) |
| Season | #WeOwnSeason003 🚀 |
| Status | 🔒 LOCKED |
| Tags | #AnythingLLM #BestPractices #YonksPromptingAcademy #ErrorHandling #SmokeTest |

---

## 📖 Table of Contents

1. [Overview](#-overview)
2. [Prerequisites](#-prerequisites)
3. [Phase 1: ADMIN Checks](#-phase-1-admin-checks)
4. [Phase 2: CCC Checks](#-phase-2-ccc-checks)
5. [Pass/Fail Criteria](#-passfail-criteria)
6. [Reporting Format](#-reporting-format)
7. [Escalation Path](#-escalation-path)
8. [ISC Mapping](#-isc-mapping)
9. [Incident Log Template](#-incident-log-template)
10. [Discovered By](#-discovered-by)
11. [Related Documents](#-related-documents)
12. [Version History](#-version-history)

---

## 📋 Overview

### What Is This?

| Field | Value |
|-------|-------|
| Name | #AnythingLLM Smoke Test |
| Purpose | Standardized post-restart verification — confirm instance is operational |
| Tests | **4** |
| Time | **~5 minutes** |
| Audience | @GTM_ADMIN + ALL instance owners |

### When To Run

| Trigger | Priority |
|---------|----------|
| After ANY #AnythingLLM restart | 🔴 IMMEDIATE |
| After unexpected error (401, 500, etc.) | 🔴 IMMEDIATE |
| After Helm chart update | 🔴 IMMEDIATE |
| After embedder/LLM model change | 🟠 BEFORE operations resume |
| After RAG document upload | 🟡 RECOMMENDED |
| Scheduled (weekly) | 🟢 OPTIONAL |

### Why This Exists

| Incident | Date | What Happened | Learning |
|----------|------|---------------|----------|
| #1 | Fri 06 Feb 2026 | Embedder reverted to GTE-Large after restart | L-107 |
| #2 | Sun 08 Feb 2026 | Full config reset — embedder + LLM reverted | L-115 |

> Two incidents in 3 days proved that #AnythingLLM config may NOT persist across restarts. This guide ensures rapid detection and recovery.

---

## 📋 Prerequisites

### Before Running Smoke Test

| # | Prerequisite | Who |
|---|-------------|-----|
| 1 | ADMIN access (`a-<ccc>_dev`) | ADMIN |
| 2 | DEFAULT user access (`u-<ccc>_user`) | ADMIN or contributor |
| 3 | Know ecosystem-approved models | See table below |
| 4 | Instance URL accessible | Verify in browser first |

### Ecosystem Approved Models

| Type | Model | API ID | Approved |
|------|-------|--------|----------|
| Embedder | Qwen3 Embedding 4B | — | GTM_2026-W06_175 |
| LLM | Claude Opus 4.6 | `claude-opus-4-6` | GTM_2026-W06_257 |

### User Requirements

| Test | User Required | Why |
|------|---------------|-----|
| Test 1 (Embedder) | `a-<ccc>_dev` (ADMIN) | Settings access |
| Test 2 (LLM) | `a-<ccc>_dev` (ADMIN) | Settings access |
| Test 3 (RAG) | `u-<ccc>_user` (DEFAULT) | CCC workspace access |
| Test 4 (CCC-ID) | `u-<ccc>_user` (DEFAULT) | CCC-ID generation (R-194) |

---

## 📋 Phase 1: ADMIN Checks

### Test 1: EMBEDDER VERIFICATION

| Field | Value |
|-------|-------|
| User | `a-<ccc>_dev` (ADMIN) |
| Location | Admin Panel → Settings → Embedder Preference |
| Time | ~1 minute |

#### Steps

| # | Step | Action |
|---|------|--------|
| 1 | Login | Login as `a-<ccc>_dev` |
| 2 | Navigate | Admin Panel → Settings → Embedding Preference |
| 3 | Check | Verify model = **Qwen3 Embedding 4B** |
| 4 | Record | Note actual model found |

#### Expected vs Failure

| Result | Model Found | Action |
|--------|-------------|--------|
| ✅ PASS | Qwen3 Embedding 4B | Proceed to Test 2 |
| ❌ FAIL | GTE-Large or other | Change to Qwen3 → re-embed ALL docs → L-107 |

#### If FAIL — Recovery

| # | Step | Action |
|---|------|--------|
| 1 | Change embedder | Select Qwen3 Embedding 4B |
| 2 | Save | Apply settings |
| 3 | Re-embed | ALL workspaces must re-embed documents |
| 4 | Log | Record as L-107 incident |

---

### Test 2: LLM MODEL VERIFICATION

| Field | Value |
|-------|-------|
| User | `a-<ccc>_dev` (ADMIN) |
| Location | Admin Panel → Settings → LLM Preference |
| Time | ~1 minute |

#### Steps

| # | Step | Action |
|---|------|--------|
| 1 | Navigate | Admin Panel → Settings → LLM Preference |
| 2 | Check | Verify model = **Claude Opus 4.6** (`claude-opus-4-6`) |
| 3 | Record | Note actual model found |

#### Expected vs Failure

| Result | Model Found | Action |
|--------|-------------|--------|
| ✅ PASS | Claude Opus 4.6 | Proceed to Phase 2 |
| ❌ FAIL | Other model | Change to Claude Opus 4.6 → L-108 |

#### If FAIL — Recovery

| # | Step | Action |
|---|------|--------|
| 1 | Change LLM | Select Claude Opus 4.6 (`claude-opus-4-6`) |
| 2 | Save | Apply settings |
| 3 | Log | Record as L-108 incident |

---

## 📋 Phase 2: CCC Checks

> ⚠️ Phase 2 MUST be run as DEFAULT user (`u-<ccc>_user`) in CCC workspace. NEVER use ADMIN for these tests (R-206).

### Test 3: RAG RETRIEVAL VERIFICATION

| Field | Value |
|-------|-------|
| User | `u-<ccc>_user` (DEFAULT) |
| Location | CCC workspace (🤝 THE HANDS) |
| Time | ~1 minute |

#### Steps

| # | Step | Action |
|---|------|--------|
| 1 | Login | Login as `u-<ccc>_user` |
| 2 | Navigate | CCC workspace |
| 3 | Create thread | NEW thread (BP-034 — fresh session) |
| 4 | Query | Ask: "What version is SharedKernel?" |
| 5 | Verify | Response should include `v3.X.X.X` |

#### Expected vs Failure

| Result | Response | Action |
|--------|----------|--------|
| ✅ PASS | SharedKernel v3.X.X.X | Proceed to Test 4 |
| ⚠️ STALE | SharedKernel v2.X.X | RAG needs refresh — stale #PinnedDocs |
| ❌ FAIL | "I don't have information" | RAG broken — re-embed required |

#### If FAIL — Recovery

| # | Step | Action |
|---|------|--------|
| 1 | Switch to ADMIN | Login as `a-<ccc>_dev` |
| 2 | Check #PinnedDocs | Verify 4 docs present in workspace |
| 3 | Re-embed | If missing, re-upload + embed |
| 4 | Fresh session | BP-034 — new thread required |
| 5 | Retest | Run Test 3 again |

---

### Test 4: CCC-ID GENERATION VERIFICATION

| Field | Value |
|-------|-------|
| User | `u-<ccc>_user` (DEFAULT) |
| Location | CCC workspace (🤝 THE HANDS) |
| Time | ~2 minutes |

#### Steps

| # | Step | Action |
|---|------|--------|
| 1 | Same thread | Continue from Test 3 (or new thread) |
| 2 | Set context | State: `[<CCC>_<YYYY>-W<WW>_<NNN>](#masterCCC)` |
| 3 | Request | Ask agent to generate next CCC-ID |
| 4 | Verify format | Must match `<CCC>_<YYYY>-W<WW>_<NNN>` |
| 5 | Verify R-212 | Agent should acknowledge cross-instance context |

#### Expected vs Failure

| Result | Response | Action |
|--------|----------|--------|
| ✅ PASS | Valid CCC-ID in correct format | All tests PASS |
| ❌ FAIL — Wrong format | Malformed CCC-ID | Check workspace prompt (BP-054) |
| ❌ FAIL — Refused | "Cannot generate" | Check user role (must be DEFAULT) + workspace (must be CCC) |
| ❌ FAIL — Wrong week | Stale ISO week | Check system date + BP-052 |

#### If FAIL — Recovery

| # | Step | Action |
|---|------|--------|
| 1 | Check workspace prompt | Verify BP-054 CCC-ID logic present |
| 2 | Check user role | Must be DEFAULT (not ADMIN — R-206) |
| 3 | Check workspace | Must be CCC (not tools — R-194) |
| 4 | Fresh session | BP-034 |
| 5 | Retest | Run Test 4 again |

---

## 📋 Pass/Fail Criteria

### Results Matrix

| Score | Result | Action |
|-------|--------|--------|
| **4/4** | ✅ **PASS** | Instance recovered — resume operations |
| **3/4** | ⚠️ **PARTIAL** | Fix failing check, retest that check only |
| **2/4** | 🟠 **DEGRADED** | Multiple issues — fix all, full retest |
| **≤1/4** | 🔴 **CRITICAL** | Escalate immediately — Helm chart or deeper issue |

### Retest Rules

| Rule | Description |
|------|-------------|
| Fix + Retest | After fixing a failure, retest ONLY that check |
| Full Retest | If ≤2/4, retest ALL 4 after fixes |
| Fresh Session | BP-034 — ALWAYS fresh session for Phase 2 retests |
| 3 Failures = Escalate | If same check fails 3× after fix attempts → escalate |

---

## 📋 Reporting Format

### Smoke Test Results Template

```markdown
## 📋 SMOKE TEST RESULTS — <INT-XXx>

| Field | Value |
|-------|-------|
| Instance | <INT-XXx> (<domain>) |
| Tester | @<CCC> |
| Date | <YYYY-MM-DD> |
| Time | <HH:MM> EST |
| Trigger | <restart / error / scheduled> |
| REF | <CCC-ID> |

### Results

| # | Test | Expected | Actual | Result |
|---|------|----------|--------|--------|
| 1 | EMBEDDER | Qwen3 Embedding 4B | <actual> | ✅/❌ |
| 2 | LLM MODEL | Claude Opus 4.6 | <actual> | ✅/❌ |
| 3 | RAG RETRIEVAL | SharedKernel v3.X.X.X | <actual> | ✅/❌ |
| 4 | CCC-ID GENERATION | Valid format | <actual> | ✅/❌ |

| Score | <X/4> |
|-------|-------|
| Result | <PASS / PARTIAL / DEGRADED / CRITICAL> |

### Actions Taken (if any)
- <action 1>
- <action 2>
```

### Where To Report

| Result | Report To |
|--------|-----------|
| 4/4 PASS | Log locally — no escalation needed |
| <4/4 | FULL:SYNC:META to #MetaAgent |
| Repeated failures | #ContextBroadcast to ALL AGENTS |

---

## 📋 Escalation Path

### Escalation Matrix

| Level | Trigger | Who | Action |
|-------|---------|-----|--------|
| 1 | Single check FAIL | Instance owner | Fix + retest |
| 2 | Multiple checks FAIL | Instance owner + @GTM_ADMIN | Investigate + fix |
| 3 | Repeated failures (same check 3×) | @RMN | Helm chart investigation |
| 4 | Full config reset | @RMN + @GTM | P0 — Helm chart persistence fix |

### Escalation Template

```markdown
═══════════════════════════════════════════════════════════════════════════════
🏐 #ContextVolley | @<CCC> → @RMN
═══════════════════════════════════════════════════════════════════════════════

TYPE: ESCALATION — SMOKE TEST FAILURE
REF: <CCC-ID>

## Issue
| Field | Value |
|-------|-------|
| Instance | <INT-XXx> |
| Test(s) Failed | <#1, #2, #3, #4> |
| Attempts | <N> |
| Error | <description> |
| L-107 Incident # | <N> |

## Request
Helm chart investigation — config not persisting across restarts.

═══════════════════════════════════════════════════════════════════════════════
```

---

## 📋 ISC Mapping

### Smoke Test → ISC 8-Point

| Smoke Test | ISC Check | ISC # |
|------------|-----------|-------|
| Test 1 (Embedder) | EMBEDDER | #1 |
| Test 2 (LLM) | LLM MODEL | #2 |
| Test 3 (RAG) | #PinnedDocs (partial) | #3 |
| Test 4 (CCC-ID) | WORKSPACE PROMPTS (partial) | #5 |

### Relationship

| Scope | Checks | Time | When |
|-------|--------|------|------|
| **Smoke Test** | 4 | ~5 min | After EVERY restart |
| **ISC 8-Point** | 8 | ~30 min | Start of EVERY season |

> Smoke Test = **rapid subset** of ISC. If smoke test PASSES, instance is operational. ISC = full certification for season compliance.

### Checks NOT Covered by Smoke Test

| ISC Check | # | Reason |
|-----------|---|--------|
| SYSTEM PROMPT | #4 | Doesn't change on restart |
| USER-IDENTITY | #6 | Doesn't change on restart |
| RAG SYNC (full) | #7 | Smoke test checks retrieval only |
| #ContextVolley | #8 | Cross-instance — separate test |

---

## 📋 Incident Log Template

### For Tracking Recurring Issues

```markdown
## 📋 INCIDENT LOG — <INT-XXx>

| # | Date | Trigger | Tests Failed | Root Cause | Fix | L-XXX | Resolved |
|---|------|---------|--------------|------------|-----|-------|----------|
| 1 | 2026-02-06 | Restart | Embedder | GTE-Large revert | Change to Qwen3 | L-107 | ✅ |
| 2 | 2026-02-08 | Reset | Embedder + LLM | Full config revert | Restore both | L-107, L-115 | ✅ |
```

### Pattern Detection

| Pattern | Threshold | Action |
|---------|-----------|--------|
| Same check fails 3× in 2 weeks | 🔴 | Escalate to @RMN — Helm chart fix |
| Full config revert 2× in 1 week | 🔴 | P0 — deployment architecture issue |
| Embedder-only revert | 🟠 | L-107 — Helm chart embedder persistence |
| No failures in 4 weeks | 🟢 | Consider reducing to monthly smoke test |

---

## 📋 Discovered By (BP-047)

| CCC | Contributor | Role | Context |
|-----|-------------|------|---------|
| GTM | [yonks](https://GitHub.com/YonksTEAM) | Co-Founder / Chief Digital Alchemist | INT-P01 post-restart recovery — 2 incidents in 3 days (W06) |

---

## 📋 Related Documents

| Document | Version | Relevance |
|----------|---------|-----------|
| SharedKernel | v3.1.1.4 | L-107, L-108, BP-059, ISC checklist |
| BEST-PRACTICES | v3.1.1.3 | BP-034, BP-059 |
| TMPL-010_ISC | v3.1.1.2 | ISC attestation template |
| GUIDE-006_GitHub-PAT | v3.1.1.1 | GitHub connector setup |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| 3.1.1.1 | 2026-W06 | GTM_2026-W06_503 | ⬜ AWAITING | Initial creation; 4-test smoke test; 2-phase workflow; escalation matrix; ISC mapping; incident log template; pattern detection; ~5 min execution |

---

#FlowsBros #FedArch #YonksPromptingAcademy #AnythingLLM #SmokeTest #ErrorHandling #WeOwnSeason003

♾️ WeOwnNet 🌐 | 🏡 Real Estate and 🤝 cooperative ownership for everyone. An 🤗 inclusive community, by 👥 invitation only.
