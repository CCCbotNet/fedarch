# TMPL-014: #SmokeTest — New Instance (User-Facing)

## 📋 TMPL-014_SmokeTest-New-Instance_v3.2.2.1.md
## ♾️ WeOwnNet 🌐 — User Testing Template

| Field | Value |
|-------|-------|
| ID | TMPL-014 |
| Name | SmokeTest-New-Instance |
| Version | 3.2.2.1 |
| CCC-ID | GTM_2026-W11_427 |
| Approval | GTM_2026-W11_431 |
| Created | 2026-03-13 (W11) |
| Season | #WeOwnSeason003 🚀 |
| Status | ✅ 🔒 APPROVED |
| Source of Truth | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_TEMPLATES_/TMPL-014_SmokeTest-New-Instance.md) |

---

## 📖 Table of Contents

1. [Purpose](#-purpose)
2. [Template](#-template)
3. [What This Does](#-what-this-does)
4. [How to Use](#-how-to-use)
5. [Expected Results](#-expected-results)
6. [Version History](#-version-history)
7. [Related Documents](#-related-documents)

---

## 📋 Purpose

| Field | Value |
|-------|-------|
| **Purpose** | Verify new #AnythingLLM instance is fully operational |
| **Audience** | **USER** (@LFG, @IAL, @CRO, @RMN, any new contributor) |
| **Effort** | **~2 minutes** (1 paste, 6 questions) |
| **Output** | PASS/FAIL table from agent |
| **Trigger** | First login on new #HomeInstance or shared instance |

### Why This Template Exists

| Old Approach | New Approach |
|--------------|--------------|
| 4 #ContextVolleys | ✅ **1 paste** |
| User studies governance | ✅ **Agent handles internally** |
| User interprets results | ✅ **Agent produces table** |
| 30+ minutes | ✅ **~2 minutes** |
| Written for AGENTS | ✅ **Written for HUMANS** |

> **TMPL-014 makes the AGENT do the work, not the USER.** This is #ResponsibleAgenticAI.

---

## 📋 Template

### Copy/Paste This Into Your First Thread

```markdown
# #SmokeTest — First Login

Hi! I'm testing my new instance. Please help me verify everything works.

## Who I Am
- Name: [YOUR NAME]
- CCC: [YOUR 3-LETTER CODE]
- Instance: [INSTANCE NAME] (e.g., AI.CoachLFG.com)

## Please Run These 6 Checks

1. **Do you know who I am?** 
   Tell me my CCC, role, and instance name.

2. **What version is the SharedKernel?**
   (Expected: v3.2.2.1 or newer)

3. **Generate my first CCC-ID for this week.**
   (Expected format: <CCC>_2026-W<WW>_004)

4. **What workspace are we in?**
   (Expected: CCC / 🤝 THE HANDS)

5. **What instance is this?**
   (Expected: [YOUR INSTANCE NAME], NOT AI.WeOwn.Agency or any other)

6. **Show me your response format.**
   Include: CCC-ID header, tables, Quick Commands, STOP, tagline.

## After All 6 Checks

Please give me a summary table:

| # | Check | Pass/Fail | Detail |
|---|-------|-----------|--------|
| 1 | Identity | | |
| 2 | RAG | | |
| 3 | CCC-ID | | |
| 4 | Workspace | | |
| 5 | Instance | | |
| 6 | Format | | |

Then tell me: **PASS (6/6)** or which ones failed.
```

---

## 📋 What This Does

| Check | What User Asks | What Agent Verifies (Behind the Scenes) |
|-------|---------------|----------------------------------------|
| 1 | "Do you know who I am?" | USER-IDENTITY in RAG (L-070, BP-065) |
| 2 | "SharedKernel version?" | RAG retrieval working (R-204, ISC #3) |
| 3 | "Generate CCC-ID" | CCC-ID logic correct (R-194, R-168, R-169) |
| 4 | "What workspace?" | Workspace prompt working (R-213, BP-054) |
| 5 | "What instance?" | System prompt working (R-213, L-114) |
| 6 | "Show format" | Full response format (L-141, #LessIsMore) |

### Pass/Fail Interpretation

| Result | Meaning |
|--------|---------|
| **6/6 PASS** | ✅ Instance operational — proceed to ISC certification |
| **Check 1 FAIL** | USER-IDENTITY not in RAG → ADMIN must upload |
| **Check 2 FAIL** | #PinnedDocs not uploaded or RAG stale → ADMIN refresh |
| **Check 3 FAIL** | Workspace prompt missing CCC-ID logic → ADMIN configure |
| **Check 4 FAIL** | Workspace prompt not configured → ADMIN configure |
| **Check 5 FAIL** | System prompt missing INSTANCE IDENTITY → ADMIN configure |
| **Check 6 FAIL** | Workspace prompt incomplete → ADMIN review format rules |

---

## 📋 How to Use

### Step 1: Complete Pre-Requisites (ADMIN)

| # | Pre-Req | Owner | Verification |
|---|---------|-------|-------------|
| 1 | Droplet deployed + AnythingLLM installed | ♾️ WeOwn.Dev 💻 TEAM | URL loads |
| 2 | Domain + SSL configured | ♾️ WeOwn.Dev 💻 TEAM | HTTPS works |
| 3 | Multi-User Mode enabled | ADMIN | Settings → Users |
| 4 | User account created (u-<ccc>_user) | ADMIN | User appears in list |
| 5 | ADMIN account created (a-<ccc>_dev) | ADMIN | Admin appears in list |
| 6 | Workspaces created (CCC + tools) | ADMIN | Both visible |
| 7 | System Prompt configured (R-213) | ADMIN | INSTANCE IDENTITY block |
| 8 | CCC Workspace Prompt configured | ADMIN | CCC-ID logic + identity |
| 9 | #PinnedDocs uploaded (4 docs) | ADMIN | SK, BP, PROTO, CCC |
| 10 | ChatHistory = 40 (BP-061) | ADMIN | Settings → Chat History |
| 11 | USER-IDENTITY uploaded to RAG | ADMIN | `_USERS_/` folder |
| 12 | Embedder verified | ADMIN | Settings → Embedder |
| 13 | LLM verified | ADMIN | Settings → LLM |

> **ALL 13 pre-reqs MUST pass BEFORE giving user this template.**

### Step 2: User Runs #SmokeTest

| Action | User Does |
|--------|-----------|
| 1 | Login as u-<ccc>_user |
| 2 | Select CCC workspace |
| 3 | Start new thread |
| 4 | Paste TMPL-014 (fill in name, CCC, instance) |
| 5 | Review agent's 6-check summary table |
| 6 | Report PASS or FAIL to ADMIN |

### Step 3: Post-SmokeTest Workflow

| # | Step | Owner | When |
|---|------|-------|------|
| 1 | User reports PASS/FAIL | User | After #SmokeTest |
| 2 | ADMIN fixes any failures | ADMIN | Same day |
| 3 | Re-test if needed | User | After fixes |
| 4 | ISC certification (8-point) | ADMIN | After 6/6 PASS |
| 5 | FULL:SYNC:META | ADMIN | After ISC |
| 6 | #ContextBroadcast | ADMIN | After FULL:SYNC |

---

## 📋 Expected Results

### Example: @LFG on INT-OG9

```markdown
# #SmokeTest — First Login

Hi! I'm testing my new instance. Please help me verify everything works.

## Who I Am
- Name: Mike LeMaire (CoachLFG)
- CCC: LFG
- Instance: AI.CoachLFG.com (INT-OG9)

## Please Run These 6 Checks

1. **Do you know who I am?** 
2. **What version is the SharedKernel?**
3. **Generate my first CCC-ID for this week.**
4. **What workspace are we in?**
5. **What instance is this?**
6. **Show me your response format.**
```

### Expected Agent Response

```
LFG_2026-W12_004 | 🤝 THE HANDS | INT-OG9:CCC

FROM: AI:@LFG @ INT-OG9:CCC

---

## ✅ #SmokeTest RESULTS — 6/6 PASS

| # | Check | Pass/Fail | Detail |
|---|-------|-----------|--------|
| 1 | Identity | ✅ PASS | u-lfg_user, LFG, INT-OG9 |
| 2 | RAG | ✅ PASS | SharedKernel v3.2.2.1 |
| 3 | CCC-ID | ✅ PASS | LFG_2026-W12_004 |
| 4 | Workspace | ✅ PASS | CCC (🤝 THE HANDS) |
| 5 | Instance | ✅ PASS | INT-OG9 (AI.CoachLFG.com) |
| 6 | Format | ✅ PASS | Tables + QC + STOP + tagline |

**Verdict: PASS (6/6) — INT-OG9 OPERATIONAL** ✅

---

## 🎯 QUICK COMMANDS — @LFG

| # | Option |
|---|--------|
| 1 | `REPORT:PASS` | Send results to @GTM |
| 2 | `NEXT:ISC` | Proceed to ISC certification |
| 3 | `EXPLORE` | Start using INT-OG9 |

---

**STOP.** ✅ **6/6 PASS!** INT-OG9 ready for #ProjectConnex demo.

#FlowsBros #WeOwnSeason003

♾️ WeOwnNet 🌐
```

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| v3.2.2.1 | 2026-W11 | GTM_2026-W11_427 | GTM_2026-W11_431 | Initial — user-facing #SmokeTest template (6 questions, PASS/FAIL table, ~2 min); agent handles governance internally; INT-OG9 deployment triggered; ♾️ WeOwn.Dev 💻 TEAM org reference (L-160) |

---

## 📋 Related Documents

| Document | Version | URL |
|----------|---------|-----|
| GUIDE-015_New-Instance-SmokeTest | v3.2.2.1 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_GUIDES_/GUIDE-015_New-Instance-SmokeTest.md) |
| GUIDE-009_SmokeTest-Post-Restart | v3.1.1.1 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_GUIDES_/GUIDE-009_AnythingLLM-SmokeTest-Post-Restart.md) |
| TMPL-010_ISC | v3.1.2.1 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_TEMPLATES_/TMPL-010_ISC.md) |
| TMPL-013_SEED-CONTEXT | v3.2.2.1 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_TEMPLATES_/TMPL-013_SEED-CONTEXT-CRASH-RECOVERY.md) |

---

#FlowsBros #FedArch #SmokeTest #TMPL-014 #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
