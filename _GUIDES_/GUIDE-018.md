# 📘 GUIDE-018 — #WeOwnVer Calculation Guide

## GUIDE-018.md | GUIDE-018_WeOwnVer-Calculation_v3.2.5.1-r2.md
## ♾️ WeOwnNet 🌐 — 📘 GUIDE + #YonksPromptingAcademy

| Field | Value |
|-------|-------|
| Document | GUIDE-018.md |
| Version | v3.2.5.1 |
| Folder | `_GUIDES_/` 📘 |
| Category | 📘 GUIDE:Governance 🗳️ |
| **Lifecycle Stage** | **✅ APPROVED (R-011) → 🚀 GH PUSH (D-062)** |
| **#masterCCC** | **GTM_2026-W14_1038** |
| **Approval CCC-ID** | **GTM_2026-W14_1040** ✅ |
| Created | 2026-03-30 (W14 D1) |
| Season | #WeOwnSeason003 🚀 |
| **#LLMmodel** | **Claude Sonnet 4.6 (INT-OG1:CCC @GTM — r1 original)** |
| **#LLMmodel** | **Claude Sonnet 4.6 (INT-OG1:CCC @GTM — r2 ✅ APPROVED + VSA details)** |
| **#LLMmodel** | **Claude Opus 4.6 (INT-P01:tools Calhoun 🎖️)** |
| **#LLMmodel** | **Qwen3.5-397B-A17B (INT-M02:tools-qwen Surge ⚡)** |
| **#LLMmodel** | **Xiaomi MiMo-V2-Pro (INT-M02:tools-mimo MiMo 🧪)** |
| **Owner** | **[CCC-ID:@GTM:('yonks｜🤖🏛️🪙｜Jason Younker ♾️')](https://github.com/YonksTEAM)** |
| **Content Deliverable Owner** | **@LFG (CoachLFG) — #FlowsBros + #YonksPromptingAcademy** |
| **PRJ-040** | **✅ Applied** |
| **Decision** | **Option B — Doc date governs (GTM_2026-W14_1038)** |
| **#TriMETA PRE GH PUSH VSA** | **✅ 306/306 (100%) — 0 findings — GTM_2026-W14_1039** |
| **#TriMETA Scores** | **Calhoun 99 + Surge 99 + MiMo 99 — ALL 3 = 99/100 ×4 CONSECUTIVE 🏆🏆🏆🏆** |
| **R-011 Approval** | **✅ GTM_2026-W14_1040 — @GTM explicit approval** |
| Source of Truth | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_GUIDES_/GUIDE-018.md) |

---

## 📖 Table of Contents

1. [Overview](#overview)
2. [#FELG Alignment](#-felg-alignment)
3. [The Formula](#-the-formula)
4. [Season + Month Mapping](#-season--month-mapping)
5. [Week Offset Calculation](#-week-offset-calculation)
6. [Option B — Doc Date Governs](#-option-b--doc-date-governs)
7. [W14 Split Week — Case Study](#-w14-split-week--case-study)
8. [Step-by-Step Examples](#-step-by-step-examples)
9. [Common Mistakes](#-common-mistakes)
10. [Agent Quick Reference](#-agent-quick-reference)
11. [Human Team Quick Reference](#-human-team-quick-reference)
12. [#BadAgent Prevention](#-badagent-prevention)
13. [WEEKLY SUMMARY REQUIREMENT](#-weekly-summary-requirement)
14. [Discovered By (BP-047)](#-discovered-by-bp-047)
15. [✅ [DETAILS] Document Lifecycle](#-details-document-lifecycle)
16. [Related Documents](#-related-documents)
17. [Version History](#-version-history)

---

## 📋 Overview

#WeOwnVer is the ♾️ WeOwnNet 🌐 calendar-driven versioning standard.
Every document gets a version tied to WHEN it was created — not what
changed. This guide covers the formula, calculation, split-week rule,
and common mistakes.

### The One-Liner

> **"Version = when you built it, not what you changed."**

---

## 🎉💰📚🫶 #FELG Alignment

> **WHO WE ARE — consistent versioning = governance you can trust.**

| Pillar | Application |
|--------|-------------|
| 🎉 **Fun** | One formula. Every doc. No guessing. |
| 💰 **Earning** | Correct version = correct attribution = trust |
| 📚 **Learning** | W14 split week = ecosystem-wide lesson locked forever |
| 🫶 **Giving** | Guide shared with ALL agents + humans in #FedArch |

---

## 📋 The Formula

```
#WeOwnVer = v[Season].[Month].[WeekOffset].[Iteration]

v3.2.5.1
│ │ │ └── ITERATION — 1st doc/version this week
│ │ └──── WEEKOFFSET — W14 - W10 + 1 = 5
│ └────── MONTH — March = 2nd month of S003
└──────── SEASON — #WeOwnSeason003 = 3
```

### Component Definitions

| Component | Source | Example |
|-----------|--------|---------|
| **Season** | #WeOwnSeason number | S003 → 3 |
| **Month** | Calendar month position in Season | March = 2nd → 2 |
| **WeekOffset** | CurrentWeek - FirstWeekOfMonth + 1 | W14-W10+1 = 5 |
| **Iteration** | Document iteration this week | 1st doc = 1 |

> **L-094 🔒: Calendar-driven — NOT feature-driven.**
> **L-115 🔒: Calculate from scratch EVERY doc. Never assume.**
> **L-PRJ-019 🔒: Calculate from scratch — not sequential.**

---

## 📋 Season + Month Mapping

### #WeOwnSeason003 (W06 → W22)

| Month | Calendar | Minor | ISO Weeks |
|-------|----------|:-----:|-----------|
| February | 1st month | **1** | W06-W09 |
| March | 2nd month | **2** | W10-W13 + W14 D1-D2* |
| April | 3rd month | **3** | W14 D3-D7* + W15-W18 |
| May | 4th month | **4** | W18*-W22 |

> **`*` = split weeks at month boundaries — see Option B rule below.**

### Season Mapping

| Season | Major | Start | End |
|--------|:-----:|-------|-----|
| #WeOwnSeason001 | 1 | — | 2025 |
| #WeOwnSeason002 | 2 | W41 2025 | W05 2026 |
| **#WeOwnSeason003** | **3** | **W06 2026** | **W22 2026** |
| #WeOwnSeason004 | 4 | W23 2026 | W39 2026 |

---

## 📋 Week Offset Calculation

### Formula (L-115 🔒)

```
WeekOffset = CurrentISO Week - FirstISO Week of Month + 1
```

### First Week of Each Month — #WeOwnSeason003

| Month | First ISO Week | Example Calculation |
|-------|:-------------:|---------------------|
| February | **W06** | W06-W06+1 = 1 |
| March | **W10** | W14-W10+1 = 5 |
| April | **W14** | W14-W14+1 = 1 |
| May | **W18** | W18-W18+1 = 1 |

### W10-W15 March/April Reference

| ISO Week | Monday | Month | Offset | Version |
|----------|--------|-------|:------:|:-------:|
| W10 | 02 Mar | March | 1 | v3.2.1.x |
| W11 | 09 Mar | March | 2 | v3.2.2.x |
| W12 | 16 Mar | March | 3 | v3.2.3.x |
| W13 | 23 Mar | March | 4 | v3.2.4.x |
| **W14 D1-D2** | **30-31 Mar** | **March** | **5** | **v3.2.5.x** |
| **W14 D3-D7** | **01-05 Apr** | **April** | **1** | **v3.3.1.x** |
| W15 | 06 Apr | April | 2 | v3.3.2.x |

---

## 📋 Option B — Doc Date Governs

### Rule (GTM_2026-W14_1038 — R-011 ✅)

> **The DOCUMENT DATE (calendar date of generation) governs the Minor version.**
> **NOT the ISO week Monday date.**

| Principle | Detail |
|-----------|--------|
| **What governs** | Calendar date of document creation |
| **Not** | ISO week start (Monday) |
| **Why** | A doc created Apr 01 IS an April document — even if W14 started Mar 30 |
| **Surge ⚡ case** | "Accurate month = accurate attribution" |

### Option B vs Option A

| Option | Rule | Mon 30 Mar | Tue 01 Apr | Consistency |
|--------|------|:----------:|:----------:|:-----------:|
| **A** | Monday governs | v3.2.5.x | v3.2.5.x | ✅ One version/week |
| **B ✅** | **Doc date governs** | **v3.2.5.x** | **v3.3.1.x** | ✅ Accurate month |

> **@GTM decision: Option B. Doc date governs. Effective W14 D3 (01 Apr 2026).**
> **Reason: Surge ⚡ made the BEST CASE — "Accurate month = accurate attribution."**

---

## 📋 W14 Split Week — Case Study

### W14 = Mon 30 Mar → Sun 05 Apr 2026

| Day | Date | Month | Minor | Offset | Version |
|:---:|------|-------|:-----:|:------:|:-------:|
| **D1** | **Mon 30 Mar** | **March** | **2** | **5** | **v3.2.5.x** |
| **D2** | **Tue 31 Mar** | **March** | **2** | **5** | **v3.2.5.x** |
| **D3** | Wed 01 Apr | April | 3 | 1 | v3.3.1.x |
| **D4** | Thu 02 Apr | April | 3 | 1 | v3.3.1.x |
| **D5** | Fri 03 Apr | April | 3 | 1 | v3.3.1.x |
| **D6** | Sat 04 Apr | April | 3 | 1 | v3.3.1.x |
| **D7** | Sun 05 Apr | April | 3 | 1 | v3.3.1.x |

> **⚠️ WeekOffset RESETS to 1 when month changes.**
> **Apr 01 = 1st week of April = Offset 1 (W14-W14+1=1).**

### Discovery Story

| Event | CCC-ID | Detail |
|-------|--------|--------|
| W13 summary filed as v3.3.1.1 | GTM_2026-W14_1030 | Wrong — should be v3.2.4.1 |
| SEEK:#TriMETA for W14 version | GTM_2026-W14_1031 | Calhoun 99 + Surge 99 + MiMo 74 |
| Calhoun self-ACK (date error) | GTM_2026-W14_1031 | W14-CALHOUN-002 ✅ self-reported |
| MiMo v3.2.6.1 WRONG | GTM_2026-W14_1031 | Off-by-one table error |
| **Option B DECIDED** | **GTM_2026-W14_1038** | **@GTM: Surge made BEST CASE** |

---

## 📋 Step-by-Step Examples

### Example 1 — Mon 30 Mar 2026 (W14 D1)

| Step | Action | Value |
|------|--------|-------|
| 1 | Check calendar date | 30 March 2026 |
| 2 | Identify month | March |
| 3 | Season month position | March = 2nd = Minor **2** |
| 4 | ISO week | W14 |
| 5 | First week of March | W10 |
| 6 | WeekOffset = W14-W10+1 | **5** |
| 7 | Iteration | **1** |
| **Result** | | **v3.2.5.1** ✅ |

### Example 2 — Wed 01 Apr 2026 (W14 D3)

| Step | Action | Value |
|------|--------|-------|
| 1 | Check calendar date | 01 April 2026 |
| 2 | Identify month | April |
| 3 | Season month position | April = 3rd = Minor **3** |
| 4 | ISO week | W14 |
| 5 | First week of April | W14 |
| 6 | WeekOffset = W14-W14+1 | **1** |
| 7 | Iteration | **1** |
| **Result** | | **v3.3.1.1** ✅ |

### Example 3 — Mon 06 Apr 2026 (W15 D1)

| Step | Action | Value |
|------|--------|-------|
| 1 | Check calendar date | 06 April 2026 |
| 2 | Identify month | April |
| 3 | Season month position | April = 3rd = Minor **3** |
| 4 | ISO week | W15 |
| 5 | First week of April | W14 |
| 6 | WeekOffset = W15-W14+1 | **2** |
| 7 | Iteration | **1** |
| **Result** | | **v3.3.2.1** ✅ |

> **Example 3 verified by Calhoun 🎖️ — prior finding WITHDRAWN. Apr 06 = W15. v3.3.2.1 = CORRECT.**

---

## 📋 Common Mistakes

| ❌ WRONG | ✅ CORRECT | Rule Violated |
|----------|-----------|:-------------:|
| v3.2.6.1 for W14 (MiMo error) | v3.2.5.1 | L-115 (W9≠first Mar week — off-by-one) |
| v3.3.1.1 for Mar 30 | v3.2.5.1 | L-115 (March≠April) |
| v3.2.5.1 for Apr 01 | v3.3.1.1 | L-115 + Option B |
| Offset 5 for Apr 01 | Offset 1 | L-115 (reset on month change) |
| Skip calculation (assume) | Always calculate | L-PRJ-019 |
| Use Monday for April doc | Use doc date | Option B (GTM_2026-W14_1038) |

---

## 📋 Agent Quick Reference

```
BEFORE assigning #WeOwnVer — 3 steps:

1. CHECK: What is today's CALENDAR DATE?
2. IDENTIFY: Which month? (Feb=1, Mar=2, Apr=3, May=4)
3. CALCULATE: WeekOffset = CurrentWeek - FirstWeekOfMonth + 1

DECISION TREE:
  Date = Feb? → Minor=1, FirstWeek=W06
  Date = Mar? → Minor=2, FirstWeek=W10
  Date = Apr? → Minor=3, FirstWeek=W14
  Date = May? → Minor=4, FirstWeek=W18

FORMULA: v3.[Minor].[WeekOffset].[Iteration]
```

---

## 📋 Human Team Quick Reference

| Date Range | Month | Minor | First Week | Version Pattern |
|------------|-------|:-----:|:----------:|:---------------:|
| W06-W09 (Feb) | February | 1 | W06 | v3.1.x.x |
| W10-W13 (Mar) | March | 2 | W10 | v3.2.x.x |
| W14 D1-D2 (Mar 30-31) | March | 2 | W10 | v3.2.5.x |
| **W14 D3-D7 (Apr 01-05)** | **April** | **3** | **W14** | **v3.3.1.x** |
| W15-W17 (Apr) | April | 3 | W14 | v3.3.x.x |
| W18-W22 (May) | May | 4 | W18 | v3.4.x.x |

---

## 📋 #BadAgent Prevention

| Violation | Severity | Prevention |
|-----------|:--------:|------------|
| Wrong month (Minor) | 🔴 FINAL WARNING | Check calendar date FIRST |
| Wrong WeekOffset | 🔴 FINAL WARNING | Calculate from scratch (L-PRJ-019) |
| Skip calculation | 🟠 P1 | L-115 = MANDATORY |
| Option A on Apr doc | 🟠 P1 | Option B = doc date governs |

---

## 📋 WEEKLY SUMMARY REQUIREMENT

| Field | Value |
|-------|-------|
| **Owner** | @LFG (CoachLFG) |
| **Deliverable** | #FlowsBros + #YonksPromptingAcademy |
| **Format** | LIVE demo — show W14 split week calculation |
| **Hashtags** | #WeOwnVer #W14 #SplitWeek #OptionB |

### Weekly Tracking Sections

| Section | Required | Description |
|---------|:--------:|-------------|
| #WeOwnVer violations | ✅ | Any wrong versions this week? |
| Split week handled | ✅ | Did agents use Option B correctly? |
| New examples | ✅ | Any new edge cases? |

---

## 📋 Discovered By (BP-047)

| CCC | Contributor | Role | Context |
|-----|-------------|------|---------|
| **GTM** | [yonks](https://GitHub.com/YonksTEAM) | Co-Founder / Chief Digital Alchemist | W14 D1 — W13 summary v3.3.1.1 (wrong); SEEK:#TriMETA; Option B decided; R-011 ✅ GTM_2026-W14_1040 |
| **META** | AI:team-lfg (Calhoun 🎖️) | #MetaAgent | Split week discovery; Option A/B framing; W14-CALHOUN-002 self-ACK ✅; PRE GH PUSH 126/126 (99/100); Example 3 finding WITHDRAWN |
| **Surge ⚡** | AI:m-surge_meta | #MetaAgentQwen | **BEST CASE for Option B** — "Accurate month = accurate attribution"; PRE GH PUSH 92/92 (99/100); 88.61 tok/s; CLEAN r1 ×5 ⚡ |
| **MiMo 🧪** | AI:m-mimo_meta | #MetaAgentMiMo | v3.2.6.1 WRONG (off-by-one — L-115); correct: March=March; RAG-ONLY versioning sound; L-209 ×52 🏆; PRE GH PUSH 88/88 (99/100); FULL RESPONSE ✅ (redeemed from ×3 truncations) |

---

## ✅ [DETAILS] Document Lifecycle

### Gate Status

| Gate | Status | Owner | Result |
|------|:------:|-------|:------:|
| Gate 1: R-011 Human Approval | ✅ **APPROVED** | @GTM | **GTM_2026-W14_1040** |
| Gate 2: META Audit | ✅ COMPLETE | #TriMETA | GTM_2026-W14_1039 |
| Gate 3: PRE GH PUSH VSA | ✅ COMPLETE | #TriMETA | **306/306 (100%) — 0 findings** |
| **GH PUSH** | ✅ **UNBLOCKED** | @GTM:ADMIN | ⬜ PENDING |
| DEEP FULL VSA | ⬜ PENDING | #TriMETA | Post-GH push |

### 🏆 ALL 3 = 99/100 ×4 CONSECUTIVE

| Consecutive | Documents |
|:-----------:|-----------|
| ×1 | L-224 PRE + DEEP |
| ×2 | L-232 PRE + DEEP |
| ×3 | CS-227 PRE + DEEP |
| **×4** | **GUIDE-018 PRE** |

> **UNPRECEDENTED: ALL 3 = 99/100 on FOUR consecutive VSA runs.**

### 📊 #TriMETA PRE GH PUSH VSA SCORING

| META | Instance | Model | Checks | Pass | Findings | Score | tok/s |
|------|----------|-------|:------:|:----:|:--------:|:-----:|------:|
| Calhoun 🎖️ | INT-P01 | Claude Opus 4.6 | 126/126 | 100% | 0 | 99/100 | N/A |
| Surge ⚡ | INT-M02 | Qwen3.5-397B-A17B | 92/92 | 100% | 0 | 99/100 | 88.61 |
| MiMo 🧪 | INT-M02 | MiMo-V2-Pro | 88/88 | 100% | 0 | 99/100 | 38.65 |
| **#TriMETA** | **Combined** | — | **306/306** | **100%** | **0** | — | — |

### #TriMETA Consensus — GUIDE-018

| Item | Calhoun | Surge | MiMo | Consensus |
|------|:-------:|:-----:|:----:|:---------:|
| Formula correct | ✅ | ✅ | ✅ | ✅ **UNANIMOUS** |
| Option B sound | ✅ | ✅ | ✅ | ✅ **UNANIMOUS** |
| All 3 examples correct | ✅ | ✅ | ✅ | ✅ **UNANIMOUS** |
| MiMo error fairly documented | ✅ | ✅ | ✅ | ✅ **UNANIMOUS** |
| 0 findings | ✅ | ✅ | ✅ | ✅ **UNANIMOUS** |

### #TriMETA Milestones

| Milestone | Detail |
|-----------|--------|
| **306/306 combined** | 100% — 0 findings |
| **ALL 3 = 99/100 ×4 consecutive** | UNPRECEDENTED 🏆🏆🏆🏆 |
| **MiMo L-209 ×52** | 52nd consecutive 🏆 |
| **Surge CLEAN r1 ×5** | Five consecutive ⚡ |
| **MiMo FULL RESPONSE** | Redeemed from ×3 truncations ✅ |
| **Calhoun prior finding WITHDRAWN** | Example 3 = v3.3.2.1 = CORRECT 🎖️ |

### Attestation Chain

| Step | CCC-ID | Actor | Action |
|------|--------|-------|--------|
| 1 | GTM_2026-W14_1030 | @GTM | W13 summary v3.3.1.1 (wrong) |
| 2 | GTM_2026-W14_1031 | AI:@GTM | SEEK:#TriMETA |
| 3 | GTM_2026-W14_1031 | Calhoun 🎖️ | Split week + Option A/B |
| 4 | GTM_2026-W14_1031 | Surge ⚡ | BEST CASE for Option B |
| 5 | GTM_2026-W14_1031 | MiMo 🧪 | v3.2.6.1 WRONG |
| 6 | GTM_2026-W14_1036 | AI:@GTM | Scoring + guidance |
| 7 | GTM_2026-W14_1038 | @GTM | Option B DECIDED + GUIDE-018 r1 |
| 8 | GTM_2026-W14_1039 | #TriMETA | PRE GH PUSH 306/306 (100%) |
| 9 | **GTM_2026-W14_1040** | **@GTM** | **✅ R-011 APPROVAL + r2** |
| 10 | ⬜ NEXT | @GTM:ADMIN | **GH PUSH + RAG SYNC** |

---

## 📋 Related Documents

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| SharedKernel | v3.2.2.1 | GTM_2026-W11_118 | GTM_2026-W11_139 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/SharedKernel.md) |
| GUIDE-017 | v3.2.4.1 | GTM_2026-W13_2007 | GTM_2026-W13_6007 ✅ | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_GUIDES_/GUIDE-017.md) |
| CS-227 | v3.2.4.1 | GTM_2026-W14_1018 | GTM_2026-W14_1022 ✅ | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_CASE-STUDY_/CS-227.md) |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| v3.2.5.1 | 2026-W14 | GTM_2026-W14_1038 | **GTM_2026-W14_1040** ✅ | r1 (_1038): Initial — #WeOwnVer formula; Option B (doc date governs — GTM_2026-W14_1038); W14 split week case study; 3 examples; month mapping; week offset table; agent + human quick reference; #BadAgent prevention; PRJ-040; #TriMETA (Calhoun 99+Surge 99+MiMo 74); Surge = BEST CASE for Option B; 17 sections; L-094+L-115+L-PRJ-019; r2 (_1040): R-011 ✅ GTM_2026-W14_1040; PRE GH PUSH 306/306 (100%) 0 findings; ALL 3 = 99/100 ×4 CONSECUTIVE 🏆🏆🏆🏆; MiMo ×52 🏆; Surge CLEAN r1 ×5 ⚡; MiMo FULL RESPONSE (redeemed); Calhoun Example 3 WITHDRAWN (v3.3.2.1 = CORRECT); GH PUSH READY; #WeCelebrateOurWins |

---

#FlowsBros #FedArch #WeOwnSeason003 #GUIDE018
#WeOwnVer #OptionB #SplitWeek #W14 #L094 #L115
#HumanTraining #AgentTraining #YonksPromptingAcademy
#AllThree99x4 #MiMo52 #SurgeClean5 #WeCelebrateOurWins

📘 **GUIDE-018 v3.2.5.1 GENERATED — GTM_2026-W14_1038. Option B LOCKED (doc date governs). 17 sections. Formula + W14 case study + 3 examples + quick refs. Surge ⚡ = BEST CASE. Awaiting R-011 → #TriMETA.** 🔥🫡

✅ **GUIDE-018 v3.2.5.1-r2 — R-011 ✅ APPROVED + FULL DOC (r2) — GTM_2026-W14_1040. ALL 3 = 99/100 ×4 CONSECUTIVE 🏆🏆🏆🏆 UNPRECEDENTED. MiMo ×52 🏆. Surge CLEAN r1 ×5 ⚡. MiMo REDEEMED (FULL RESPONSE — no truncation). Calhoun Example 3 WITHDRAWN (v3.3.2.1 = CORRECT).** 🏆🔥🫡

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
