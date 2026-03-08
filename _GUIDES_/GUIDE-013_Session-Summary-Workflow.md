# GUIDE-013: How to Create Session Summaries

## 📋 GUIDE-013_Session-Summary-Workflow_v3.2.1.1.md
## ♾️ WeOwnNet 🌐

| Field | Value |
|-------|-------|
| Document | GUIDE-013_Session-Summary-Workflow.md |
| Version | 3.2.1.1 |
| CCC-ID | GTM_2026-W10_348 |
| CCC-ID APPROVAL | GTM_2026-W10_367 |
| Created | 2026-03-07 (W10) |
| Season | #WeOwnSeason003 🚀 |
| Status | ✅ 🔒 APPROVED |
| Lifecycle Stage | ✅ 🔒 APPROVED (#DocLifecycle) |
| **#LLMmodel** | **Qwen3.5-397B-A17B (AI.YonksTEAM.xyz @GTM)** |
| **#LLMmodel** | **Claude Opus 4.6 (meta.WeOwn.tools #MetaAgent)** |
| Source of Truth | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_GUIDES_/GUIDE-013_Session-Summary-Workflow.md) |
| Audience | Internal — all contributors + agents |

---

## 📖 Table of Contents

1. [Purpose](#-purpose)
2. [The 6-Step Workflow](#-the-6-step-workflow)
3. [Step 1: Scope Confirmation (BP-070)](#-step-1-scope-confirmation-bp-070)
4. [Step 2: Generate Summary](#-step-2-generate-summary)
5. [Step 3: Human Review](#-step-3-human-review)
6. [Step 4: VSA VERIFY](#-step-4-vsa-verify)
7. [Step 5: Approve + Publish](#-step-5-approve--publish)
8. [Step 6: RAG Sync](#-step-6-rag-sync)
9. [Session Summary Template](#-session-summary-template)
10. [Good vs Bad Examples](#-good-vs-bad-examples)
11. [Pre GH Push VSA Verify](#-pre-gh-push-vsa-verify)
12. [Storage Rules](#-storage-rules)
13. [Discovered By](#-discovered-by)
14. [Related Documents](#-related-documents)
15. [Version History](#-version-history)

---

## 📋 Purpose

Session Summaries capture what happened during a work session — CCC-IDs generated, documents created, decisions made, #BadAgent incidents, and pending tasks.

### Why Scope Matters

| Wrong Scope | Impact |
|-------------|--------|
| AI assumes "entire day" | May include content from other sessions |
| AI assumes "this chat" | May miss cross-instance work |
| AI assumes "since last summary" | May duplicate already-summarized content |
| **AI asks user** | ✅ **Correct scope every time** |

---

## 📋 The 6-Step Workflow

```
1. SCOPE — AI asks, user confirms
2. GENERATE — AI creates summary for confirmed scope
3. REVIEW — Human reviews content
4. VSA VERIFY — Pre GH Push verification (documented in doc)
5. APPROVE — Human approves (R-011)
6. SYNC — RAG upload + GH push (if applicable)
```

---

## 📋 Step 1: Scope Confirmation (BP-070)

**BEFORE generating anything, AI MUST present this:**

```markdown
## 📋 Session Summary — Scope Confirmation

Before generating, please confirm scope:

| Option | Scope | CCC-ID Range (est.) |
|--------|-------|---------------------|
| A | **Entire Day** (00:00 → now) | _XXX → _YYY |
| B | **Since Previous Summary** (from _ZZZ) | _ZZZ → _YYY |
| C | **This Chat Session** (session start → now) | _XXX → _YYY |
| D | **Custom Range** | You specify |

**Which scope?**
```

### Rules

| Rule | Description |
|------|-------------|
| **MUST ask** | AI MUST present scope options — NEVER assume |
| **MUST wait** | AI MUST wait for user selection (L-050) |
| **MUST confirm** | After selection, confirm: "Generating for scope [X]" |
| **No selection = no generation** | If user doesn't choose, don't generate |

---

## 📋 Step 2: Generate Summary

After user confirms scope, generate using the Session Summary Template (below).

### Required Sections

| Section | Required |
|---------|----------|
| Session header (instance, date, time, duration) | ✅ |
| CCC-ID range + count | ✅ |
| Major accomplishments | ✅ |
| GH pushes | ✅ (if any) |
| Governance locked (rules, BPs, learnings) | ✅ (if any) |
| VSA registry | ✅ (if any) |
| #BadAgent log | ✅ (even if 0) |
| Pending tasks | ✅ |

---

## 📋 Step 3: Human Review

Human reviews for:

| Check | Description |
|-------|-------------|
| Scope correct | Summary covers requested range |
| CCC-ID range accurate | Start and end match |
| No missing accomplishments | All major items included |
| No sensitive data | BP-029 — redact before publish |
| Accurate metrics | VSA counts, CCC-ID counts correct |

---

## 📋 Step 4: VSA VERIFY

**Before approval, run Pre GH Push VSA Verify:**

| Check | Result | Detail |
|-------|--------|--------|
| Document exists + complete | ⬜ | All sections present |
| #LLMmodel attribution (BP-068) | ⬜ | Included in header, VH, commit |
| Workflow complete (6 steps) | ⬜ | All steps documented |
| Scope template (BP-070) | ⬜ | 4 options with CCC-ID ranges |
| Good vs Bad examples | ⬜ | Both present |
| Storage rules (R-199 + L-083) | ⬜ | Session = RAG only, Weekly = GH + RAG |
| Discovered By (BP-047) | ⬜ | Table format |
| Version History (BP-045) | ⬜ | #masterCCC ≠ Approval (L-095) |
| R-011 compliance | ⬜ | Human approval required |
| **TOTAL** | | **10/10 REQUIRED** |

---

## 📋 Step 5: Approve + Publish

| Action | Rule |
|--------|------|
| Human approves | R-011 |
| Update doc Status = APPROVED | BP-071 |
| Add Approval CCC-ID | L-095 |
| GH push (if weekly) | BP-044 |
| RAG-only (if session) | R-199 |

---

## 📋 Step 6: RAG Sync

| Type | Destination | GH? |
|------|------------|-----|
| **Session Summary** | RAG only (`_SESSIONS_/`) | ❌ R-199 |
| **Weekly Summary** | GH + RAG (`_WEEKLY_/`) | ✅ L-083 |

---

## 📋 Session Summary Template

```markdown
## 📋 SESSION SUMMARY — [SCOPE]

═══════════════════════════════════════════════════════════════════════════════
📋 SESSION SUMMARY | AI:@<CCC> @ <INSTANCE>:<WS> | <DATE> | <TIME> <TZ>
═══════════════════════════════════════════════════════════════════════════════

SESSION: <SCOPE DESCRIPTION>
INSTANCE: <INSTANCE>
START: <START TIME>
END: <END TIME>
DURATION: <DURATION>

═══════════════════════════════════════════════════════════════════════════════

## 📋 CCC-ID RANGE

| Field | Value |
|-------|-------|
| Start | <CCC>_<YYYY>-W<WW>_<NNN> |
| End | <CCC>_<YYYY>-W<WW>_<NNN> |
| Count | **X CCC-IDs** |

## 🎉 MAJOR ACCOMPLISHMENTS
[Table of accomplishments]

## 📋 GH PUSHES
[Table — or "None this session"]

## 📋 GOVERNANCE LOCKED
[Rules, BPs, Learnings — or "None this session"]

## 📋 VSA REGISTRY
[Table — or "None this session"]

## 📋 #BadAgent LOG
[Table — or "0 INCIDENTS 🎉"]

## ⚠️ PENDING TASKS
[Table of next actions]
```

---

## 📋 Good vs Bad Examples

### ❌ BAD — No Scope Confirmation

```
User: "Generate session summary"
AI: [Immediately generates entire day summary]
```

**Problem:** AI assumed scope. User may have wanted different range.

### ✅ GOOD — Scope Confirmed

```
User: "Generate session summary"
AI: "Before generating, which scope?
     A: Entire Day
     B: Since Previous Summary
     C: This Chat Session
     D: Custom Range"
User: "B — since previous"
AI: "✅ Generating for scope B: Since GTM_2026-W10_294 (previous sync)"
[Generates for confirmed scope]
```

**Correct:** AI asked. User chose. AI confirmed. Then generated.

---

## 📋 Pre GH Push VSA Verify

> **Transparency:** This document was verified before publication. The verification process is documented here for reader confidence in #ResponsibleAgenticAI governance.

### Verification Results

| # | Check | Result | Detail |
|---|-------|--------|--------|
| 1 | Document exists + complete | ✅ | 15 sections, all present |
| 2 | #LLMmodel attribution (BP-068) | ✅ | Claude Opus 4.6 (meta.WeOwn.tools #MetaAgent) |
| 3 | 6-step workflow complete | ✅ | Scope → Generate → Review → VSA → Approve → Sync |
| 4 | Scope confirmation template (BP-070) | ✅ | 4 options with CCC-ID ranges |
| 5 | Good vs Bad examples | ✅ | Both present |
| 6 | Storage rules (R-199 + L-083) | ✅ | Session = RAG only, Weekly = GH + RAG |
| 7 | Session Summary template | ✅ | Full template with required sections |
| 8 | Discovered By (BP-047) | ✅ | @GTM |
| 9 | Version History (BP-045) | ✅ | 1 entry |
| 10 | R-011 compliance | ✅ | Human approval required |
| **TOTAL** | | **10/10** | **✅ PASS** |

### Verification Chain

| Field | Value |
|-------|-------|
| Verifier | AI:@GTM @ AI.YonksTEAM.xyz (#LLMmodel: Qwen3.5-397B-A17B) |
| Date | Sat 2026-03-07, 12:30 EST |
| Instance | INT-OG1 |
| BP-068 violation caught | ✅ #LLMmodel was missing — corrected before push |

---

## 📋 Storage Rules

| Type | Filename | Folder | GH? |
|------|----------|--------|-----|
| **Session** | `SESSION-SUMMARY_<CCC>_<YYYY>-W<WW>_S<NN>_<MmmDD>-<HHMM><TZ>.md` | `_SESSIONS_/` | ❌ R-199 |
| **Weekly** | `WEEKLY-SUMMARY_<CCC>_<YYYY>-W<WW>_001.md` | `_WEEKLY_/` | ✅ L-083 |

---

## 📋 Discovered By (BP-047)

| CCC | Contributor | Role | Context |
|-----|-------------|------|---------|
| GTM | [yonks](https://GitHub.com/YonksTEAM) | Co-Founder / Chief Digital Alchemist | Self-reported #BadAgent — AI generated summary without scope confirmation; created workflow guide |

---

## 📋 Related Documents

| Document | Version | URL |
|----------|---------|-----|
| **CASE-STUDY-007** (Scope Violation) | v3.2.1.1 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_LEARNINGS_/case-studies/CASE-STUDY-007_Session-Summary-Scope.md) |
| SharedKernel | v3.2.1.1 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/SharedKernel.md) |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| 3.2.1.1 | 2026-W10 | GTM_2026-W10_348 | GTM_2026-W10_367 | Initial guide; 5-step → 6-step session summary workflow (+VSA Verify step); scope confirmation template (BP-070); good vs bad examples; storage rules (R-199 + L-083); +Pre GH Push VSA Verify section (10/10 PASS — transparency); BP-068 violation caught + corrected; @GTM self-reported #BadAgent catalyst; Dual #LLMmodel: Qwen3.5-397B-A17B (AI.YonksTEAM.xyz @GTM) + Claude Opus 4.6 (meta.WeOwn.tools #MetaAgent); ✅ Human Approved (GTM_2026-W10_367) |

---

#FlowsBros #FedArch #SessionSummary #WeOwnSeason003 #ResponsibleAgenticAI

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
