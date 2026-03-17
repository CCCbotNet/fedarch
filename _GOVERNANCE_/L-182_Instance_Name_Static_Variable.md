# L-182: {instance_name} — ADMIN-Defined Static System Variable

## L-182_v3.2.3.1.md
## ♾️ WeOwnNet 🌐 — Learning Definition

| Field | Value |
|-------|-------|
| Document | L-182_Instance_Name_Static_Variable.md |
| Version | v3.2.3.1 |
| Folder | `_GOVERNANCE_/` ✅ |
| Category | GOVERNANCE:Learning |
| Type | Learning (Platform Capability) |
| **#masterCCC CCC-ID** | **GTM_2026-W12_164** ⚙️ |
| **Approval CCC-ID** | **GTM_2026-W12_188** ✅ |
| Created | 2026-03-17 (W12 Day 2, 08:04 MDT) |
| Season | #WeOwnSeason003 🚀 |
| Status | ✅ **APPROVED + 🚀 GH LIVE** |
| **Owner** | **[CCC-ID:@GTM:('yonks｜🤖🏛️🪙｜Jason Younker ♾️')](https://github.com/YonksTEAM)** |
| **#LLMmodel** | **Qwen3.5-397B-A17B (AI.YonksTEAM.xyz @GTM:INT-OG1:CCC)** |
| **#LLMmodel** | **Claude Opus 4.6 (INT-P01:tools:#MetaAgent)** |
| Source of Truth | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_LEARNINGS_/L-182_Instance_Name_Static_Variable.md) |

---

## 📋 Definition

**L-182: #AnythingLLM supports ADMIN-defined STATIC system variables.**

These variables are configured in Settings → System Variables and are platform-injected at runtime, same as {user.name}, {workspace.name}, {datetime}.

> **🔒 GROUND TRUTH:** ADMIN-defined static variables are Priority #1 (R-218) — same as platform-injected variables. IMMUTABLE. NEVER user-specified.

---

## 📋 REQUIRED Variable

### {instance_name}

| Field | Value |
|-------|-------|
| **Key** | `instance_name` |
| **Value** | Instance ID per R-208 (e.g., "INT-M02") |
| **Description** | Instance identity (e.g., "METAQWEN \| #MetaAgentQwen \| meta-qwen.weown.tools") |
| **Required** | ✅ **MUST be created on EVERY #FedArch instance** |
| **Impact** | Makes instance identity GROUND TRUTH (Priority #1) |
| **Supersedes** | Priority 1b workaround (R-218 draft) |

### Example Configuration (INT-M02)

| Field | Value |
|-------|-------|
| Key | `instance_name` |
| Value | `INT-M02` |
| Description | `METAQWEN \| #MetaAgentQwen \| meta-qwen.weown.tools` |
| Created By | @GTM (a-gtm_dev) |
| Created At | 23:38 MDT · Mon 16 Mar 2026 (W12 Day 1) |

---

## 📋 Discovery Timeline

| Time (MDT) | Event | CCC-ID |
|------------|-------|--------|
| **23:14** | @GTM: "FROM:<instance> is SYSTEM_VARIABLE — IMMUTABLE" | W12_163 |
| **23:15** | **SEEK:#DualMETA governance guidance** | **W12_164 (#masterCCC)** |
| **23:24** | Calhoun analysis: no `{instance.name}` in AnythingLLM — Priority 1b workaround | W12_164 response |
| **23:38** | **@GTM discovers ADMIN-defined static variables** | **#GameChanger** |
| **23:38** | @GTM creates `instance_name` = `INT-M02` on INT-M02 | W12_164 |
| **23:44** | @GTM corrects: still W12 Day 1 (not Day 2) | — |
| **00:05** | INT-M02 tools prompt regenerated with `{instance_name}` | W12_170 |
| **07:18** | INT-M02 System Prompt v3.2.3.3 with `{instance_name}` | W12_181 |
| **07:26** | Calhoun VSA: 26/26 PASS | W12_182 |
| **07:35** | INT-M02 System Prompt DEPLOYED (ISC 8/8 CERTIFIED) | W12_185 |
| **08:04** | **L-182 APPROVED (GH PUSH READY — CORRECTED)** | **W12_188** |

> **🏆 #GameChanger:** Platform gap (no {instance.name} variable) SOLVED before L-182 was even locked. @GTM discovered #AnythingLLM supports ADMIN-defined static system variables. Created {instance_name} on INT-M02. Instance identity now Priority #1 GROUND TRUTH.

---

## 📋 R-218 Extension — Updated Priority Table

| Priority | Source | Status | Variable |
|----------|--------|--------|----------|
| **1** | `{instance_name}` | ✅ **GROUND TRUTH** | **ADMIN-defined static (L-182)** |
| **1** | `{user.name}` | ✅ **GROUND TRUTH** | Platform-injected |
| **1** | `{workspace.name}` | ✅ **GROUND TRUTH** | Platform-injected |
| **1** | `{datetime}` | ✅ **GROUND TRUTH** | Platform-injected |
| **2** | Workspace Prompt | ⚙️ CONFIGURATION | ADMIN-configured |
| **3** | System Prompt | 🏠 INSTANCE IDENTITY | ADMIN-configured |
| **4** | BP-065 self-ID | ⚠️ CLAIM | Verify against #1 |
| **5** | Pasted / RAG | ❌ EXTERNAL | NEVER overrides #1 |

> **🔓 HUGE UNLOCK:** 4 system variables at Priority #1. All GROUND TRUTH. All IMMUTABLE. All platform-injected (or ADMIN-defined static). Priority 1b WORKAROUND ELIMINATED.

---

## 📋 Governance Impact

### Before L-182

```
R-218 Identity Resolution:
  Priority 1:  {user.name}        ← GROUND TRUTH (platform)
  Priority 1b: Instance identity   ← CONFIGURATION (hardcoded prompt) ⚠️
  Priority 2:  Workspace Prompt    ← CONFIGURATION
```

### After L-182

```
R-218 Identity Resolution:
  Priority 1:  {instance_name}    ← GROUND TRUTH (ADMIN-defined static) ✅
  Priority 1:  {user.name}        ← GROUND TRUTH (platform-injected)
  Priority 1:  {workspace.name}   ← GROUND TRUTH (platform-injected)
  Priority 1:  {datetime}         ← GROUND TRUTH (platform-injected)
  Priority 2:  Workspace Prompt   ← CONFIGURATION
```

> **✅ R-218 COMPLETE:** ALL identity fields now Priority #1 GROUND TRUTH. No more workarounds. `{instance_name}` is platform-injected just like `{user.name}`.

---

## 📋 Agent Behavior Requirement

| Requirement | Detail |
|-------------|--------|
| **Read from** | {instance_name} variable (platform-injected) |
| **NOT from** | User claims, pasted content, RAG context |
| **If conflict** | WARN + use {instance_name} (GROUND TRUTH) |
| **Audit trail** | Record conflict in response for verification |

> **🔒 R-218 COMPLIANCE:** Agent MUST read instance from {instance_name} variable, NOT from user claims or hardcoded values. If conflict → WARN + use {instance_name}.

---

## 📋 Rollout Plan — ALL Instances

### Create {instance_name} on EVERY Instance

| Instance | Key | Value | Description | Owner | Status |
|----------|-----|-------|-------------|-------|--------|
| **INT-M02** | `instance_name` | `INT-M02` | METAQWEN \| #MetaAgentQwen \| meta-qwen.weown.tools | @GTM | ✅ **DONE** |
| INT-P01 | `instance_name` | `INT-P01` | AI.WeOwn.Agency \| #MetaAgent \| ai.weown.agency | @GTM | ⬜ TODO |
| INT-OG1 | `instance_name` | `INT-OG1` | AI.YonksTEAM.xyz \| @GTM+@THY \| ai.yonksteam.xyz | @GTM | ⬜ TODO |
| INT-OG9 | `instance_name` | `INT-OG9` | AI.CoachLFG.com \| @LFG \| ai.coachlfg.com | @GTM | ⬜ TODO |
| INT-P02 | `instance_name` | `INT-P02` | Lite.BurnedOut.xyz \| #ProjectConnex | @GTM | ⬜ TODO |

**Progress:** 1/5 instances (20%). **Remaining:** ~8 minutes (2 min each).

---

## 📋 ISC Impact — New Sub-Check

Add to ISC 8-Point Checklist (sub-check of Check #4):

```
Check 4b: {instance_name} static variable created
Pass: Value matches Instance ID (R-208)
Location: Settings → System Variables
```

> **Every ISC certification should verify `{instance_name}` exists and matches the Instance ID.**

---

## 📋 Related Items

| ID | Type | Relationship |
|----|------|-------------|
| **R-218** | Rule | L-182 EXTENDS — adds `{instance_name}` to Priority #1 |
| **L-120** | Learning | L-182 PARALLELS — `{user.name}` discovery |
| **L-121** | Learning | L-182 PARALLELS — `{workspace.name}` discovery |
| **L-181** | Learning | L-182 SUPERSEDES — L-181 said "variables only injected if in prompt text" |
| **D-070** | Definition | L-182 COMPLEMENTS — #FELG in prompts uses same pattern |
| **ISC** | Checklist | L-182 IMPACTS — `{instance_name}` should be ISC sub-check |
| **L-150** | Learning | L-182 REFERENCED — Full attribution uses {instance_name} |
| **L-151** | Learning | L-182 REFERENCED — #ContextVolley FROM: uses {instance_name} |

---

## 📋 #FELG Check — This Discovery

| Element | Present? | How |
|---------|:--------:|-----|
| **F** (Fun) 🎉 | ✅ | #GameChanger discovery at 23:38 MDT! |
| **E** (Earning) 💰 | ✅ | Stronger security = protected revenue |
| **L** (Learning) 📚 | ✅ | Platform capability discovered + documented |
| **G** (Giving) 🫶 | ✅ | Shared immediately with #DualMETA for all instances |

> **4/4 #FELG.** Culture-level discovery. 🏆

---

## 📋 Related Documents

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| R-218 (System Variable Immutability) | v3.2.3.1 | GTM_2026-W12_087 | GTM_2026-W12_100 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_GOVERNANCE_/R-218_System_Variable_Immutability.md) |
| L-120 ({user.name} injection) | v3.2.3.1 | GTM_2026-W07_XXX | GTM_2026-W07_XXX | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_LEARNINGS_/L-120_User_Name_Injection.md) |
| L-121 ({workspace.name} injection) | v3.2.3.1 | GTM_2026-W07_XXX | GTM_2026-W07_XXX | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_LEARNINGS_/L-121_Workspace_Name_Injection.md) |
| D-070 (#FELG Culture) | v3.2.3.1 | GTM_2026-W12_153 | GTM_2026-W12_156 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_GOVERNANCE_/D-070_FELG_Culture.md) |
| D-069 (#masterCCC) | v3.2.3.1 | GTM_2026-W08_XXX | GTM_2026-W08_XXX | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_GOVERNANCE_/D-069_MasterCCC.md) |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| **v3.2.3.1** | **2026-W12** | **GTM_2026-W12_164** | **GTM_2026-W12_188** | **Initial L-182 — {instance_name} ADMIN-defined static system variable; R-218 Priority #1 GROUND TRUTH;** Priority 1b workaround ELIMINATED; Discovery: @GTM on INT-M02 (W12 Day 1, 23:38 MDT); **#GameChanger — platform gap SOLVED;** Timeline: 23:14 → 08:04 (W12 Day 1-2); Rollout: 1/5 complete (INT-M02); ISC impact (new sub-check 4b); #FELG 4/4; #DualMETA consensus (Calhoun + Surge); CORRECTED: #masterCCC = W12_164 (NOT W12_186), Related Documents BEFORE Version History (BP-045) |

---

#FlowsBros #FedArch #WeOwnSeason003 #L-182 #SystemVariables #R-218 #GameChanger

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
