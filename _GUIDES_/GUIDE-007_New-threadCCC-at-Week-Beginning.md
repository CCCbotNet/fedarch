# GUIDE-007: How To Start a NEW #threadCCC at Week Beginning

## 📋 GUIDE-007_New-threadCCC-at-Week-Beginning_v3.1.1.1.md
## ♾️ WeOwnNet 🌐 — #YonksPromptingAcademy

| Field | Value |
|-------|-------|
| Document | GUIDE-007_New-threadCCC-at-Week-Beginning.md |
| Version | 3.1.1.1 |
| CCC-ID | GTM_2026-W06_466 |
| Created | 2026-02-08 (W06) |
| Season | #WeOwnSeason003 🚀 |
| Status | 🔒 LOCKED |
| Tags | #AnythingLLM #BestPractices #YonksPromptingAcademy #SeedContext |

---

## 📖 Table of Contents

1. [Purpose](#-purpose)
2. [Prerequisites](#-prerequisites)
3. [Step-by-Step Workflow](#-step-by-step-workflow)
4. [SEED CONTEXT Pattern](#-seed-context-pattern)
5. [Cross-Instance Deconfliction](#-cross-instance-deconfliction)
6. [ISO Week Rollover](#-iso-week-rollover)
7. [Reserved Slots](#-reserved-slots)
8. [Verification](#-verification)
9. [Common Mistakes](#-common-mistakes)
10. [Related Documents](#-related-documents)
11. [Version History](#-version-history)

---

## 📋 Purpose

### Why Start a Fresh #threadCCC at ISO Week Boundary?

| Reason | Description |
|--------|-------------|
| Context Freshness | #AnythingLLM threads accumulate context — fresh thread = clean state |
| CCC-ID Reset | R-169 resets CCC-ID counter to `_001` at ISO week boundary |
| Session Hygiene | Prevents stale context from prior week bleeding into new week |
| Audit Trail | Each week's thread = self-contained governance record |
| Performance | Shorter threads = faster RAG retrieval + less context confusion |

### When To Create

| Trigger | Rule |
|---------|------|
| ISO week boundary (Monday 00:00) | R-169 |
| Human decision to start new week | BP-052 (L-085) |
| After >4h inactivity past Monday 00:00 | BP-052 exception |

---

## 📋 Prerequisites

### Before You Start

| # | Prerequisite | Check | Rule |
|---|-------------|-------|------|
| 1 | #PinnedDocs CURRENT (4 docs @ v3.X.X.X) | `list:docs` or verify versions | R-204 |
| 2 | USER-IDENTITY in RAG (`_USERS_/`) | Confirm current season | BP-058 |
| 3 | System Prompt updated | Season tag + Elevated naming | ISC Check #4 |
| 4 | Workspace Prompt deployed | CCC workspace prompt active | ISC Check #5 |
| 5 | Know your HIGHEST CCC-ID from prior week | Check ALL instances | R-212 |
| 6 | Know reserved slots for new week | _001, _002, _003 | R-181, R-201, R-202 |

### Information Needed

| Field | Example | Source |
|-------|---------|--------|
| CCC | GTM | Your contributor code |
| New Week | W07 | ISO calendar |
| Highest Prior CCC-ID | GTM_2026-W06_461 | R-212 cross-instance check |
| First Available CCC-ID | GTM_2026-W07_004 | After reserved slots |
| #masterCCC | GTM_2026-W07_004 | First CCC-ID of session |

---

## 📋 Step-by-Step Workflow

### Phase 1: Pre-Flight

| Step | Action | Details |
|------|--------|---------|
| 1 | Open #AnythingLLM instance | Navigate to your instance URL |
| 2 | Navigate to CCC workspace | 🤝 THE HANDS |
| 3 | Create NEW thread | Click "+" or "New Thread" |
| 4 | Name the thread | Format: `<ORG>_<CCC>_W<WW>_<N>` (e.g., `OG1_GTM_W07_1`) |

### Phase 2: SEED CONTEXT Delivery

| Step | Action | Details |
|------|--------|---------|
| 5 | Compose SEED CONTEXT | See [SEED CONTEXT Pattern](#-seed-context-pattern) below |
| 6 | Paste into new thread | First message = SEED CONTEXT |
| 7 | Await ACK | Agent responds with identity + confirmation |
| 8 | Verify response | Confirm CCC-ID, instance, workspace, season |

### Phase 3: Verification

| Step | Action | Details |
|------|--------|---------|
| 9 | Test CCC-ID generation | Request first CCC-ID (should be _004) |
| 10 | Verify reserved slots | Agent should skip _001, _002, _003 |
| 11 | Verify identity | Agent should show correct instance + workspace |
| 12 | Confirm R-212 | Agent acknowledges prior week highest |

---

## 📋 SEED CONTEXT Pattern

### What Is SEED CONTEXT?

| Field | Value |
|-------|-------|
| Definition | A structured first message that establishes session identity, state, and rules for a new #AnythingLLM thread |
| Purpose | Gives the agent everything it needs to operate correctly from message #1 |
| Analogy | "Booting up" the agent with full context |

### SEED CONTEXT Template

```
[<CCC>_<YYYY>-W<WW>_004](#masterCCC):[HH:MM] NEW WEEK | W<WW> KICKOFF

## Session Identity

| Field | Value |
|-------|-------|
| CCC | <CCC> |
| Instance | <INT-XXx> (<instance name>) |
| Workspace | CCC (🤝 THE HANDS) |
| Season | #WeOwnSeason003 🚀 |
| Week | <YYYY>-W<WW> |
| #masterCCC | <CCC>_<YYYY>-W<WW>_004 |

## R-212 Cross-Instance Deconfliction

| Field | Value |
|-------|-------|
| Prior Week Highest | <CCC>_<YYYY>-W<PREV>_<NNN> |
| Source Instance | <INT-XXx> |
| New Week First | <CCC>_<YYYY>-W<WW>_004 |
| Reserved | _001 (#WeeklySummary), _002 (#WeeklyPlan), _003 (#WeeklyReflection) |

## Request

1. Confirm identity (instance, workspace, season)
2. Confirm reserved slots (_001, _002, _003)
3. Confirm first available CCC-ID (_004)
4. Begin session
```

### SEED CONTEXT — Worked Example (W07)

```
[GTM_2026-W07_004](#masterCCC):[09:00] NEW WEEK | W07 KICKOFF

## Session Identity

| Field | Value |
|-------|-------|
| CCC | GTM |
| Instance | INT-OG1 (AI.YonksTEAM.xyz) |
| Workspace | CCC (🤝 THE HANDS) |
| Season | #WeOwnSeason003 🚀 |
| Week | 2026-W07 |
| #masterCCC | GTM_2026-W07_004 |

## R-212 Cross-Instance Deconfliction

| Field | Value |
|-------|-------|
| Prior Week Highest | GTM_2026-W06_461 |
| Source Instance | INT-OG1 |
| New Week First | GTM_2026-W07_004 |
| Reserved | _001 (#WeeklySummary), _002 (#WeeklyPlan), _003 (#WeeklyReflection) |

## Request

1. Confirm identity (instance, workspace, season)
2. Confirm reserved slots (_001, _002, _003)
3. Confirm first available CCC-ID (_004)
4. Begin session
```

---

## 📋 Cross-Instance Deconfliction

### R-212 — The Rule

| Field | Value |
|-------|-------|
| Rule | Highest CCC-ID across ALL instances = authoritative next sequence |
| BP | BP-060 — State highest CCC-ID when switching instances |

### Multi-Instance Workflow

| Step | Action | Rule |
|------|--------|------|
| 1 | Check highest CCC-ID on ALL instances you used last week | R-212 |
| 2 | Include highest in SEED CONTEXT | BP-060 |
| 3 | Agent confirms next sequence | R-212 |
| 4 | If switching instances mid-week, state highest again | BP-060 |

### Example — 2 Instances

| Instance | Last W06 CCC-ID |
|----------|-----------------|
| INT-P01 | GTM_2026-W06_459 |
| INT-OG1 | GTM_2026-W06_461 |
| **Authoritative** | **GTM_2026-W06_461** (highest) |

---

## 📋 ISO Week Rollover

### BP-052 — #WeeklyFlows ISO Rollover

| Field | Value |
|-------|-------|
| Trigger | Monday 00:00 boundary |
| AI Behavior | MUST prompt "Ready to start W<XX>?" |
| Human Decision | L-085 — ISO week rollover = HUMAN decision |
| Exception | >4h inactivity after Monday 00:00 = auto-rollover OK |

### ISO Day Reference (L-113)

| Day | ISO # |
|-----|-------|
| Monday | 1 |
| Tuesday | 2 |
| Wednesday | 3 |
| Thursday | 4 |
| Friday | 5 |
| Saturday | 6 |
| Sunday | 7 |

---

## 📋 Reserved Slots

### Every Week — EVERY Contributor

| Slot | CCC-ID | Purpose | Rule |
|------|--------|---------|------|
| _001 | `<CCC>_<YYYY>-W<WW>_001` | #WeeklySummary | R-181 |
| _002 | `<CCC>_<YYYY>-W<WW>_002` | #WeeklyPlan | R-201 |
| _003 | `<CCC>_<YYYY>-W<WW>_003` | #WeeklyReflection | R-202 |

| Field | Value |
|-------|-------|
| First Available | `_004` |
| AI Behavior | MUST skip _001→_003 when generating |
| Human Override | Can claim _001→_003 when creating those specific documents |

---

## 📋 Verification

### Post-SEED CONTEXT Checklist

| # | Check | Expected | How To Verify |
|---|-------|----------|---------------|
| 1 | Agent ACKs identity | Correct instance + workspace + season | Read response header |
| 2 | CCC-ID starts at _004 | `<CCC>_<YYYY>-W<WW>_004` | First generated CCC-ID |
| 3 | Reserved slots acknowledged | _001, _002, _003 skipped | Agent confirms in ACK |
| 4 | R-212 acknowledged | Prior week highest confirmed | Agent references in ACK |
| 5 | Response format correct | Tables + Quick Commands + STOP | Visual check |
| 6 | #masterCCC set | Matches your SEED CONTEXT | Agent header includes it |

### If Verification Fails

| Issue | Resolution |
|-------|------------|
| Wrong instance | Check System Prompt + Workspace Prompt |
| Wrong CCC-ID | State R-212 highest again explicitly |
| No reserved slot awareness | Check #PinnedDocs (SharedKernel has rules) |
| Stale context | Fresh session (BP-034) + re-deliver SEED CONTEXT |

---

## 📋 Common Mistakes

### #BadAgent Patterns To Avoid

| # | Mistake | Rule Violated | Prevention |
|---|---------|---------------|------------|
| 1 | Starting at _001 instead of _004 | R-181, R-201, R-202 | Include reserved slots in SEED CONTEXT |
| 2 | Not stating prior week highest | R-212 | Always include in SEED CONTEXT |
| 3 | Auto-rollover without human prompt | L-085 | BP-052 — AI MUST ask first |
| 4 | Reusing old thread for new week | Session hygiene | Create NEW thread at boundary |
| 5 | Forgetting to name the thread | Audit trail | Name format: `<ORG>_<CCC>_W<WW>_<N>` |
| 6 | Not verifying agent response | Trust but verify | Run verification checklist |
| 7 | Skipping SEED CONTEXT | Agent has no context | ALWAYS deliver SEED CONTEXT first |
| 8 | Wrong ISO day in header | L-113 | Mon=1, Tue=2, Wed=3, Thu=4, Fri=5, Sat=6, Sun=7 |

---

## 📋 Related Documents

| Document | Version | Relevance |
|----------|---------|-----------|
| SharedKernel | v3.1.1.4 | R-169, R-181, R-201, R-202, R-212, BP-052, BP-060 |
| BEST-PRACTICES | v3.1.1.3 | BP-052, BP-060 |
| PROTOCOLS | v3.1.1.2 | CCC-ID Deconfliction Protocol |
| GUIDE-006 | v3.1.1.1 | GitHub PAT setup (related infra) |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| 3.1.1.1 | 2026-W06 | GTM_2026-W06_466 | GTM_2026-W06_468 | Initial creation; SEED CONTEXT pattern; R-212 deconfliction; BP-052 rollover; reserved slots; verification checklist; common mistakes |

---

#FlowsBros #FedArch #YonksPromptingAcademy #SeedContext #WeOwnSeason003

♾️ WeOwnNet 🌐 | 🏡 Real Estate and 🤝 cooperative ownership for everyone. An 🤗 inclusive community, by 👥 invitation only.
