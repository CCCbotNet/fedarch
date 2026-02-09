# TMPL-010: Instance Season Certification (ISC)

## 📋 TMPL-010_ISC_v3.1.2.1.md
## ♾️ WeOwnNet 🌐 — Template

| Field | Value |
|-------|-------|
| Document | TMPL-010_ISC.md |
| Version | 3.1.2.1 |
| CCC-ID | GTM_2026-W07_082 |
| Created | 2026-02-09 (W07) |
| Season | #WeOwnSeason003 🚀 |
| Status | 🔒 LOCKED |
| Tags | #ISC #Templates #FedArch |

---

## 📖 Table of Contents

1. [How To Use This Template](#-how-to-use-this-template)
2. [Instance Identity](#-instance-identity)
3. [Certification Details](#-certification-details)
4. [Ecosystem Approved Models](#-ecosystem-approved-models)
5. [ISC 8-Point Checklist](#-isc-8-point-checklist)
6. [Results Summary](#-results-summary)
7. [Action Items / Recovery](#-action-items--recovery)
8. [Attestation](#-attestation)
9. [Related Documents](#-related-documents)
10. [Version History](#-version-history)

---

## 📋 How To Use This Template

| Step | Action |
|------|--------|
| 1 | Copy this template |
| 2 | Rename to `ISC_<INT-XXx>_v<VERSION>.md` |
| 3 | Fill in Instance Identity section |
| 4 | Fill in Certification Details section |
| 5 | Execute 8-point checklist — fill ⬜ fields |
| 6 | Complete Results Summary |
| 7 | If any FAIL → complete Action Items / Recovery |
| 8 | Generate Attestation |
| 9 | FULL:SYNC:META to #MetaAgent |

### Naming Convention

| Field | Format | Example |
|-------|--------|---------|
| Filename | `ISC_<INT-XXx>_v<VERSION>.md` | `ISC_INT-P02_v3.1.2.1.md` |
| Path | `_INSTANCE_/` | `_INSTANCE_/ISC_INT-P02_v3.1.2.1.md` |

### Pass Criteria

| Result | Criteria |
|--------|----------|
| ✅ CERTIFIED | 8/8 checks PASS |
| ❌ FAILED | Any check FAIL |

---

## 📋 Instance Identity

| Field | Value |
|-------|-------|
| Instance ID | ⬜ `<INT-XXx>` |
| Name | ⬜ `<domain>` |
| Type | ⬜ `<Production / #HomeInstance / Seasonal / META / VSA>` |
| Organization | ⬜ `<org name>` |
| Domain | ⬜ `<domain URL>` |
| Owner(s) | ⬜ `<@CCC, @CCC>` |
| Legacy ID | ⬜ `<INT-00X or N/A>` |
| Platform | AnythingLLM |

---

## 📋 Certification Details

| Field | Value |
|-------|-------|
| Season | ⬜ `<#WeOwnSeason00X 🚀>` |
| Season Start | ⬜ `<W## (date)>` |
| Certification Deadline | ⬜ `<date>` (BP-059 — 2 weeks from season start) |
| Certifier | ⬜ `<@CCC>` |
| Witnessed By | ⬜ `<@CCC>` |
| Date | ⬜ `<YYYY-MM-DD>` |
| REF | ⬜ `<CCC-ID>` |

---

## 📋 Ecosystem Approved Models

| Type | Model | API ID | Approved |
|------|-------|--------|----------|
| Embedder | Qwen3 Embedding 4B | — | GTM_2026-W06_175 |
| LLM | Claude Opus 4.6 | `claude-opus-4-6` | GTM_2026-W06_257 |

---

## 📋 ISC 8-Point Checklist

### Check 1: EMBEDDER

| Field | Value |
|-------|-------|
| Check | Embedding model verified |
| Pass Criteria | Qwen3 Embedding 4B |
| Location | Admin Panel → Settings → Embedding Preference |
| Actual | ⬜ |
| Result | ⬜ |

---

### Check 2: LLM MODEL

| Field | Value |
|-------|-------|
| Check | LLM model verified |
| Pass Criteria | Claude Opus 4.6 (`claude-opus-4-6`) |
| Location | Admin Panel → Settings → LLM Preference |
| Actual | ⬜ |
| Result | ⬜ |

---

### Check 3: #PinnedDocs

| Field | Value |
|-------|-------|
| Check | 4 documents present at current season version |
| Pass Criteria | SharedKernel, BEST-PRACTICES, PROTOCOLS, CCC @ v3.X.X.X |
| Location | Workspace settings → Pinned documents |

| # | Document | Expected | Actual | Result |
|---|----------|----------|--------|--------|
| 1 | SharedKernel | v3.X.X.X | ⬜ | ⬜ |
| 2 | BEST-PRACTICES | v3.X.X.X | ⬜ | ⬜ |
| 3 | PROTOCOLS | v3.X.X.X | ⬜ | ⬜ |
| 4 | CCC | v3.X.X.X | ⬜ | ⬜ |

| Result | ⬜ |
|--------|---|

---

### Check 4: SYSTEM PROMPT

| Field | Value |
|-------|-------|
| Check | Season tag + INSTANCE IDENTITY block present |
| Pass Criteria | `#WeOwnSeason00X 🚀` + INSTANCE IDENTITY as FIRST section (R-213) |
| Location | Admin Panel → System Prompt |

| Sub-Check | Expected | Actual | Result |
|-----------|----------|--------|--------|
| Season tag | `#WeOwnSeason00X 🚀` | ⬜ | ⬜ |
| INSTANCE IDENTITY block (R-213) | Instance ID, Name, Type, Owner(s), Season | ⬜ | ⬜ |
| INSTANCE IDENTITY = FIRST section | Before Ecosystem Identity | ⬜ | ⬜ |

| Result | ⬜ |
|--------|---|

---

### Check 5: WORKSPACE PROMPTS + CONFIG

| Field | Value |
|-------|-------|
| Check | Workspace prompts + config verified |
| Pass Criteria | BP-053 (Non-CCC restriction) + BP-054 (CCC-ID logic) + BP-061 (#WorkspaceChatHistory = 40) |

| Sub-Check | Workspace | Expected | Actual | Result |
|-----------|-----------|----------|--------|--------|
| BP-053 | tools | Restriction block present | ⬜ | ⬜ |
| BP-053 | ADMIN | Restriction block present | ⬜ | ⬜ |
| BP-054 | CCC | CCC-ID logic present | ⬜ | ⬜ |
| BP-061 | CCC | ChatHistory = 40 | ⬜ | ⬜ |
| BP-061 | tools | ChatHistory = 40 | ⬜ | ⬜ |
| BP-061 | ADMIN | ChatHistory = 40 | ⬜ | ⬜ |

| Result | ⬜ |
|--------|---|

---

### Check 6: USER-IDENTITY

| Field | Value |
|-------|-------|
| Check | Owner(s) USER-IDENTITY current for season |
| Pass Criteria | BP-058 — current season field |
| Location | `_USERS_/` in RAG |

| CCC | Document | Version | Season | Result |
|-----|----------|---------|--------|--------|
| ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |

| Result | ⬜ |
|--------|---|

---

### Check 7: RAG SYNC

| Field | Value |
|-------|-------|
| Check | GitHub connector refreshed post-season start |
| Pass Criteria | CCCbotNet/fedarch connected + refreshed |
| Location | Admin Panel → Data Connectors |

| Connector | Repo | Last Refresh | Result |
|-----------|------|-------------|--------|
| GitHub | CCCbotNet/fedarch | ⬜ | ⬜ |

| Result | ⬜ |
|--------|---|

---

### Check 8: #ContextVolley

| Field | Value |
|-------|-------|
| Check | Can reach #MetaAgent @ INT-P01 |
| Pass Criteria | Successful #ContextVolley delivery + ACK |
| Method | Send test volley → receive ACK |

| Sub-Check | Expected | Actual | Result |
|-----------|----------|--------|--------|
| Volley sent | ✅ Delivered | ⬜ | ⬜ |
| ACK received | ✅ From #MetaAgent | ⬜ | ⬜ |

| Result | ⬜ |
|--------|---|

---

## 📋 Results Summary

| # | Check | Result |
|---|-------|--------|
| 1 | EMBEDDER | ⬜ |
| 2 | LLM MODEL | ⬜ |
| 3 | #PinnedDocs | ⬜ |
| 4 | SYSTEM PROMPT | ⬜ |
| 5 | WORKSPACE PROMPTS + CONFIG | ⬜ |
| 6 | USER-IDENTITY | ⬜ |
| 7 | RAG SYNC | ⬜ |
| 8 | #ContextVolley | ⬜ |

| Field | Value |
|-------|-------|
| PASSED | ⬜ /8 |
| FAILED | ⬜ /8 |
| **STATUS** | ⬜ |

---

## 📋 Action Items / Recovery

> Complete this section ONLY if any check FAILS.

| # | Failed Check | Root Cause | Recovery Action | Owner | Status |
|---|-------------|------------|-----------------|-------|--------|
| ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |

### Recovery Reference

| Failed Check | Common Recovery |
|-------------|-----------------|
| #1 EMBEDDER | Change → Qwen3 Embedding 4B → re-embed ALL docs |
| #2 LLM MODEL | Change → Claude Opus 4.6 (`claude-opus-4-6`) |
| #3 #PinnedDocs | Upload v3.X.X.X docs → embed in workspaces |
| #4 SYSTEM PROMPT | Add season tag + INSTANCE IDENTITY block (R-213) |
| #5 WORKSPACE PROMPTS | Add BP-053/BP-054 blocks + set ChatHistory = 40 |
| #6 USER-IDENTITY | Create/update USER-IDENTITY per TMPL-009 + BP-058 |
| #7 RAG SYNC | Connect CCCbotNet/fedarch → refresh |
| #8 #ContextVolley | Verify network + API config + META thread URL |

---

## 📋 Attestation

| Field | Value |
|-------|-------|
| **RESULT** | ⬜ `<✅ CERTIFIED / ❌ FAILED>` |
| Score | ⬜ /8 |
| Certifier | ⬜ `<@CCC>` |
| Witnessed By | ⬜ `<@CCC>` |
| Date | ⬜ `<YYYY-MM-DD>` |
| REF | ⬜ `<CCC-ID>` |
| Instance | ⬜ `<INT-XXx>` |

### Attestation Chain

| Step | Actor | CCC-ID | Action |
|------|-------|--------|--------|
| 1 | ⬜ | ⬜ | ISC initiated |
| 2 | ⬜ | ⬜ | Checks executed |
| 3 | ⬜ | ⬜ | APPROVED / FAILED |
| 4 | ⬜ | ⬜ | FULL:SYNC:META |

---

## 📋 Related Documents

| Document | Version | Relevance |
|----------|---------|-----------|
| SharedKernel | v3.1.1.4 | ISC 8-point checklist (BP-059), R-213, ecosystem models |
| BEST-PRACTICES | v3.1.1.3 | BP-053, BP-054, BP-058, BP-059, BP-061 |
| PROTOCOLS | v3.1.1.2 | #ContextVolley protocol |
| TMPL-009_USER-IDENTITY | v3.1.1.2 | USER-IDENTITY template (Check #6) |
| GUIDE-009_SmokeTest | v3.1.1.1 | Post-restart verification (related) |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| 3.1.2.1 | 2026-W07 | GTM_2026-W07_071 | ⬜ AWAITING | Initial template creation; 8-point checklist; Check #4 enhanced (+R-213 INSTANCE IDENTITY); Check #5 enhanced (+BP-061 #WorkspaceChatHistory = 40); recovery reference table; attestation chain; how-to-use section |

---

#FlowsBros #FedArch #ISC #Templates #WeOwnSeason003

♾️ WeOwnNet 🌐 | 🏡 Real Estate and 🤝 cooperative ownership for everyone. An 🤗 inclusive community, by 👥 invitation only.
