# TMPL-009_USER-IDENTITY.md

## 📋 TMPL-009_USER-IDENTITY_v3.1.1.2.md
## ♾️ WeOwnNet 🌐 — User Identity Template

| Field | Value |
|-------|-------|
| Template | TMPL-009_USER-IDENTITY |
| Version | 3.1.1.2 |
| CCC-ID | GTM_2026-W06_353 |
| Created | 2026-01-30 (W05) |
| Updated | 2026-02-07 (W06) |
| Season | #WeOwnSeason003 🚀 |
| Status | 🔒 LOCKED |
| Source of Truth | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_TEMPLATES_/TMPL-009_USER-IDENTITY.md) |

---

## 📖 Table of Contents

1. [Overview](#-overview)
2. [User Identity Schema](#-user-identity-schema)
3. [Username Format Standard](#-username-format-standard)
4. [User Identity Template](#-user-identity-template)
5. [Relationship to #threadHEADER](#-relationship-to-threadheader)
6. [Usage Examples](#-usage-examples)
7. [Version History](#-version-history)

---

## 📋 Overview

### Purpose

| Use Case | Description |
|----------|-------------|
| Onboarding | Standard format for new user setup |
| Permissions | Document user role and access |
| Attribution | Static identity for #threadHEADER inheritance |
| Audit | Traceability of user assignments |
| Season Compliance | BP-058 requires Season field |
| #HomeInstance | R-209 requires #HomeInstance for ALL contributors |

### Lifecycle

| Aspect | Value |
|--------|-------|
| Created | Once per user |
| Updated | Rarely (role change, instance assignment) |
| Refreshed | Each #WeOwnSeason (BP-058) |
| Storage | RAG (persistent) |
| Type | Static |

### Related Items

| Type | ID | Description |
|------|-----|-------------|
| Definition | D-047 | #threadHEADER (dynamic attribution) |
| Definition | D-048 | #HomeInstance |
| Definition | D-058 | INT-S0x — Seasonal Shared Instance |
| Definition | D-059 | #PersonalBrand Instance |
| Learning | L-069 | VSA MUST include #threadHEADER |
| Learning | L-070 | USER-IDENTITY storage in `_USERS_/` |
| Best Practice | BP-049 | #threadHEADER required for attribution |
| Best Practice | BP-050 | Onboarding Workflow |
| Best Practice | BP-058 | USER-IDENTITY Season refresh |
| Rule | R-160 | Username format standard |
| Rule | R-209 | #HomeInstance REQUIRED for ALL contributors |
| Rule | R-210 | INT-S0x = Seasonal Shared Instance |
| Rule | R-211 | Interim assignment until INT-S0x deployed |

---

## 📋 User Identity Schema

### Required Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| CCC | String (3 chars) | Contributor Code Convention | `GTM` |
| Contributor | String | Full name | `yonks (Jason Younker)` |
| Username | String | #AnythingLLM username (per R-160) | `u-gtm_user` |
| Role | Enum | ADMIN / DEFAULT | `DEFAULT` |
| Instance(s) | Array | Assigned instances | `INT-P01, INT-OG1` |
| **#HomeInstance** | **String** | **Primary instance — REQUIRED (R-209)** | **`INT-OG1` or `INT-S03`** |
| Workspace(s) | Array | Assigned workspaces | `CCC` |
| Created | Date | Creation date (ISO) | `2026-01-30` |
| **Season** | String | Current #WeOwnSeason | `#WeOwnSeason003 🚀` |

### Optional Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| Updated | Date | Last update date (ISO) | `2026-02-07` |
| Notes | String | Additional context | `Founding OG` |
| Status | Enum | ACTIVE / INACTIVE | `ACTIVE` |
| Mode Unlocked | String | Achievement tier | `#GODx10xMODE 🔒` |

### #HomeInstance Types (R-209)

| Type | Prefix | Description | Example |
|------|--------|-------------|---------|
| #PersonalBrand | INT-OGx | Own domain, personal instance | INT-OG1 (AI.YonksTEAM.xyz) |
| Seasonal Shared | INT-S0x | Default for new contributors (R-210) | INT-S03 (#WeOwnSeason003) |
| Interim | INT-P0x | Temporary until INT-S0x deployed (R-211) | INT-P01 (AI.WeOwn.Agency) |

### Schema Change Log

| Version | Change |
|---------|--------|
| v2.4.0 | Initial schema |
| v3.1.1.1 | +Season field (REQUIRED) — BP-058 compliance |
| v3.1.1.2 | #HomeInstance → REQUIRED (R-209); +#HomeInstance Types table; +Seasonal Shared / Interim |

---

## 📋 Username Format Standard (R-160)

### Format Rules

| Role | Prefix | Suffix | Format | Example |
|------|--------|--------|--------|---------|
| ADMIN | `a-` | `_dev` | `a-<ccc>_dev` | `a-gtm_dev` |
| DEFAULT | `u-` | `_user` | `u-<ccc>_user` | `u-ldc_user` |
| Tool Agent | `t-` | `_tool` | `t-<tool>_tool` | `t-anythingllm_tool` |

### Username Components

| Component | Description | Constraint |
|-----------|-------------|------------|
| Prefix | Role indicator | `a-` / `u-` / `t-` |
| Identifier | CCC or tool name | lowercase |
| Suffix | Type indicator | `_dev` / `_user` / `_tool` |

### Validation RegEx

```regex
^(a-[a-z]{3}_dev|u-[a-z]{3}_user|t-[a-z]+_tool)$
```

---

## 📋 User Identity Template

### Template Format

```markdown
# User Identity: <CCC>

## 📋 USER-IDENTITY_<CCC>_v3.1.1.2.md
## ♾️ WeOwnNet 🌐 — User Identity Document

| Field | Value |
|-------|-------|
| Document | USER-IDENTITY_<CCC>.md |
| Version | 3.1.1.2 |
| CCC-ID | <CCC-ID> |
| Created | <YYYY-MM-DD> (W<WW>) |
| Updated | <YYYY-MM-DD> (W<WW>) |
| Season | #WeOwnSeason00X 🚀 |
| Status | 🔒 LOCKED |

---

## 📋 User Identity

| Field | Value |
|-------|-------|
| CCC | <CCC> |
| Contributor | <Full Name> |
| Username | u-<ccc>_user |
| Role | DEFAULT |
| Instance(s) | <INT-XXX, INT-XXX> |
| #HomeInstance | <INT-OGx or INT-S0x> |
| Workspace(s) | CCC |
| Created | <YYYY-MM-DD> |
| Updated | <YYYY-MM-DD> |
| Season | #WeOwnSeason00X 🚀 |
| Status | ACTIVE |

---

## 📋 Admin Identity

> ⚠️ Include ONLY if contributor has ADMIN access. Delete for DEFAULT-only users.

| Field | Value |
|-------|-------|
| Username | a-<ccc>_dev |
| Role | ADMIN |
| Instance(s) | <INT-XXX, INT-XXX> |
| Workspace(s) | CCC, tools, ADMIN |

---

## 📋 Profile

| Field | Value |
|-------|-------|
| Handle | <Display Name> |
| GitHub | [<username>](https://GitHub.com/<username>) |
| Role | <Organizational Role> |
| Status | <Status> |
| Mode Unlocked | <Achievement> |

---

## 📋 #HomeInstance

> **R-209:** Every contributor MUST have a #HomeInstance.
> - **#PersonalBrand:** INT-OGx — use this section
> - **Seasonal Shared:** INT-S0x — use Seasonal Instance section instead
> **ONE of these two sections is ALWAYS required.**

| Field | Value |
|-------|-------|
| Instance | <INT-OGx> |
| Name | <domain> |
| Type | #PersonalBrand |
| Owner(s) | @<CCC> |
| Status | ✅ ACTIVE / ⬜ PLANNED / 🔄 SETUP |

---

## 📋 Seasonal Instance

> **R-210:** INT-S0x = Seasonal Shared Instance — default for new contributors.
> Include this section instead of #HomeInstance for Seasonal Shared users.
> **ONE of these two sections is ALWAYS required (R-209).**

| Field | Value |
|-------|-------|
| Instance | <INT-S0x> |
| Season | <#WeOwnSeasonXXX> |
| Type | Seasonal Shared |
| Status | ✅ ACTIVE / ⬜ PLANNED |
| Interim | <INT-P01 or INT-P02> *(only if INT-S0x not yet deployed — R-211)* |

---

## 📋 Instance Access

| Instance | Name | Role | Status |
|----------|------|------|--------|
| <INT-XXX> | <domain> | User / User + Admin / User (#HomeInstance) | ✅ ACTIVE / ⬜ PLANNED |

---

## 📋 #FedArch Participation

| Field | Value |
|-------|-------|
| Reports To | #MetaAgent (INT-P01) |
| Protocol | #ContextVolley |
| Authority | <Role / Achievement>, SEEK:META for governance |
| #HomeInstance | <INT-OGx or INT-S0x> |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| 3.1.1.2 | 2026-W06 | <CCC-ID> | <CCC-ID> | Initial creation |

---

#FlowsBros #FedArch #UserIdentity #WeOwnSeason00X

♾️ WeOwnNet 🌐 | 🏡 Real Estate and 🤝 cooperative ownership for everyone. An 🤗 inclusive community, by 👥 invitation only.
```

### Blank Template

```markdown
# User Identity: ___

## 📋 User Identity

| Field | Value |
|-------|-------|
| CCC | ___ |
| Contributor | ___ |
| Username | ___ |
| Role | ___ |
| Instance(s) | ___ |
| #HomeInstance | ___ |
| Workspace(s) | ___ |
| Created | ___ |
| Season | #WeOwnSeason00X 🚀 |
| Updated | ___ |
| Status | ACTIVE |

## 📋 #HomeInstance / Seasonal Instance

> Choose ONE (R-209):

| Field | Value |
|-------|-------|
| Instance | ___ |
| Type | #PersonalBrand / Seasonal Shared |
| Status | ___ |

## 📋 Notes

___

---

#FlowsBros #FedArch #UserIdentity

♾️ WeOwnNet 🌐 | 🏡 Real Estate and 🤝 cooperative ownership for everyone. An 🤗 inclusive community, by 👥 invitation only.
```

---

## 📋 Relationship to #threadHEADER

### Static vs Dynamic

| Aspect | TMPL-009 (Static) | D-047 (Dynamic) |
|--------|-------------------|-----------------|
| Purpose | WHO is the user | WHERE is the action |
| Lifecycle | Long-lived | Per-operation |
| Storage | RAG | Inline |
| Changes | Rarely (+ each Season) | Every thread |

### Inheritance Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    TMPL-009_USER-IDENTITY                       │
│                    (Static — WHO)                               │
│                                                                 │
│   CCC: GTM ─────────────────────────────────┐                  │
│   Username: u-gtm_user ─────────────────────┤                  │
│   Role: DEFAULT                             │                  │
│   Instances: INT-P01, INT-OG1               │ inherits         │
│   #HomeInstance: INT-OG1                    │                  │
│   Workspaces: CCC                           │                  │
│   Season: #WeOwnSeason003 🚀                │                  │
│                                             ↓                  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                    D-047: #threadHEADER                         │
│                    (Dynamic — WHERE)                            │
│                                                                 │
│   CCC: GTM ←────────────────── inherited                       │
│   Username: u-gtm_user ←────── inherited                       │
│   Instance: INT-P01 ←───────── current session                 │
│   Workspace: CCC ←──────────── current session                 │
│   Thread UUID: 62b10159-... ←─ current thread                  │
│   Timestamp: Sa 12:45 EST ←─── now                             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### #threadHEADER Format (D-047)

```markdown
## 📋 Thread Context

| Field | Value |
|-------|-------|
| CCC | <CCC> |
| Username | <username> |
| Instance | <INT-XXX> |
| Workspace | <workspace> |
| Thread UUID | <UUID> |
| Thread URL | <URL> |
| Timestamp | <Dd HH:MM TZ> |
```

### Shorthand Format

```
<CCC>:<username>@<INT-XXX>:<workspace>:<UUID>
```

---

## 📋 Usage Examples

### Example 1: Founding OG with #PersonalBrand (#HomeInstance)

```markdown
# User Identity: GTM

## 📋 USER-IDENTITY_GTM_v3.1.1.2.md
## ♾️ WeOwnNet 🌐 — User Identity Document

| Field | Value |
|-------|-------|
| Document | USER-IDENTITY_GTM.md |
| Version | 3.1.1.2 |
| CCC-ID | GTM_2026-W06_353 |
| Created | 2026-01-30 (W05) |
| Updated | 2026-02-07 (W06) |
| Season | #WeOwnSeason003 🚀 |
| Status | 🔒 LOCKED |

---

## 📋 User Identity

| Field | Value |
|-------|-------|
| CCC | GTM |
| Contributor | yonks (Jason Younker) |
| Username | u-gtm_user |
| Role | DEFAULT |
| Instance(s) | INT-P01, INT-OG1 |
| #HomeInstance | INT-OG1 |
| Workspace(s) | CCC |
| Created | 2026-01-30 |
| Updated | 2026-02-07 |
| Season | #WeOwnSeason003 🚀 |
| Status | ACTIVE |

---

## 📋 Admin Identity

| Field | Value |
|-------|-------|
| Username | a-gtm_dev |
| Role | ADMIN |
| Instance(s) | INT-P01, INT-OG1 |
| Workspace(s) | CCC, tools, ADMIN |

---

## 📋 Profile

| Field | Value |
|-------|-------|
| Handle | yonks.box｜🤖🏛️🪙｜Jason Younker ♾️ |
| GitHub | [YonksTEAM](https://GitHub.com/YonksTEAM) |
| Role | Co-Founder / Chief Digital Alchemist & Architect for #ResponsibleAgenticAI |
| Status | 🏛️ Founding OG |
| Mode Unlocked | **#GODx10xMODE** 🔒 |

---

## 📋 #HomeInstance

| Field | Value |
|-------|-------|
| Instance | INT-OG1 |
| Name | AI.YonksTEAM.xyz |
| Type | #PersonalBrand |
| Owners | @GTM + @THY |
| Status | ✅ ACTIVE |

---

## 📋 Instance Access

| Instance | Name | Role | Status |
|----------|------|------|--------|
| INT-P01 | AI.WeOwn.Agency | User + Admin | ✅ ACTIVE |
| INT-OG1 | AI.YonksTEAM.xyz | User + Admin (#HomeInstance) | ✅ ACTIVE |

---

## 📋 #FedArch Participation

| Field | Value |
|-------|-------|
| Reports To | #MetaAgent (INT-P01) |
| Protocol | #ContextVolley |
| Authority | Founding OG, #GODx10xMODE |
| #HomeInstance | INT-OG1 |

---

#FlowsBros #FedArch #UserIdentity #HomeInstance #GODx10xMODE #WeOwnSeason003

♾️ WeOwnNet 🌐
```

### Example 2: Contributor on Seasonal Shared Instance

```markdown
# User Identity: NEW

## 📋 USER-IDENTITY_NEW_v3.1.1.2.md
## ♾️ WeOwnNet 🌐 — User Identity Document

| Field | Value |
|-------|-------|
| Document | USER-IDENTITY_NEW.md |
| Version | 3.1.1.2 |
| CCC-ID | NEW_2026-W06_001 |
| Created | 2026-02-07 (W06) |
| Season | #WeOwnSeason003 🚀 |
| Status | 🔒 LOCKED |

---

## 📋 User Identity

| Field | Value |
|-------|-------|
| CCC | NEW |
| Contributor | New Contributor |
| Username | u-new_user |
| Role | DEFAULT |
| Instance(s) | INT-S03 |
| #HomeInstance | INT-S03 |
| Workspace(s) | CCC |
| Created | 2026-02-07 |
| Season | #WeOwnSeason003 🚀 |
| Status | ACTIVE |

---

## 📋 Profile

| Field | Value |
|-------|-------|
| Handle | New Contributor |
| Role | Community Member |
| Status | ✅ Active |

---

## 📋 Seasonal Instance

| Field | Value |
|-------|-------|
| Instance | INT-S03 |
| Season | #WeOwnSeason003 |
| Type | Seasonal Shared |
| Status | ✅ ACTIVE |

---

## 📋 Instance Access

| Instance | Name | Role | Status |
|----------|------|------|--------|
| INT-S03 | Seasonal Shared | User (#HomeInstance) | ✅ ACTIVE |

---

## 📋 #FedArch Participation

| Field | Value |
|-------|-------|
| Reports To | #MetaAgent (INT-P01) |
| Protocol | #ContextVolley |
| Authority | User, SEEK:META for governance |
| #HomeInstance | INT-S03 |

---

#FlowsBros #FedArch #UserIdentity #WeOwnSeason003

♾️ WeOwnNet 🌐
```

### Example 3: Contributor with Interim Assignment (R-211)

```markdown
# User Identity: LDC

## 📋 User Identity

| Field | Value |
|-------|-------|
| CCC | LDC |
| Contributor | Dhruv Malik |
| Username | u-ldc_user |
| Role | DEFAULT |
| Instance(s) | INT-P01, INT-P02 |
| #HomeInstance | INT-S03 |
| Workspace(s) | CCC |
| Created | 2026-02-04 |
| Season | #WeOwnSeason003 🚀 |
| Status | ACTIVE |

---

## 📋 Profile

| Field | Value |
|-------|-------|
| Handle | Dhruv Malik (@LDC) |
| Role | Agentic AI Engineer / Project Lead |
| Status | ✅ Active |

---

## 📋 Seasonal Instance

| Field | Value |
|-------|-------|
| Instance | INT-S03 |
| Season | #WeOwnSeason003 |
| Type | Seasonal Shared |
| Status | ⬜ PLANNED |
| Interim | INT-P01 (R-211) |

---

## 📋 Instance Access

| Instance | Name | Role | Status |
|----------|------|------|--------|
| INT-P01 | AI.WeOwn.Agency | User (Interim — R-211) | ✅ ACTIVE |
| INT-P02 | Lite.BurnedOut.xyz | User | ✅ ACTIVE |
| INT-S03 | Seasonal Shared | User (#HomeInstance) | ⬜ PLANNED |

---

## 📋 #FedArch Participation

| Field | Value |
|-------|-------|
| Reports To | #MetaAgent (INT-P01) |
| Protocol | #ContextVolley |
| Authority | User, SEEK:META for governance |
| #HomeInstance | INT-S03 (Interim: INT-P01) |

---

## 📋 Notes

Agentic AI Platform Engineer. #ProjectConnex.

---

#FlowsBros #FedArch #UserIdentity

♾️ WeOwnNet 🌐
```

### Example 4: Tool Agent

```markdown
# User Identity: t-pinata_tool

## 📋 User Identity

| Field | Value |
|-------|-------|
| CCC | — |
| Contributor | Tool Agent |
| Username | t-pinata_tool |
| Role | DEFAULT |
| Instance(s) | INT-P01 |
| Workspace(s) | tools |
| Created | 2026-02-03 |
| Season | #WeOwnSeason003 🚀 |
| Status | ACTIVE |

## 📋 Notes

Pinata.cloud Tool Agent. Steward: @GTM. ShortCode: @MAIT:#Pinata.

---

#FlowsBros #FedArch #UserIdentity

♾️ WeOwnNet 🌐
```

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| 3.1.1.2 | 2026-W06 | GTM_2026-W06_353 | GTM_2026-W06_370 | #HomeInstance → REQUIRED (R-209); +#HomeInstance Types table; +Seasonal Instance section (R-210); +Interim field (R-211); +D-058, D-059 refs; conditional logic (ONE always required); +Seasonal example; +Interim example (LDC); Elevated naming throughout; Source of Truth → CCCbotNet/fedarch; Blank template updated; FULL PRESERVE from v3.1.1.1 (L-097) |
| 3.1.1.1 | 2026-W06 | GTM_2026-W06_241 | GTM_2026-W06_247 | +Season field (REQUIRED); +#HomeInstance; +Profile section; +Admin Identity section; BP-058 compliance; #WeOwnVer L-094; FULL PRESERVE from v2.4.0 (L-097) |
| 2.4.0 | 2026-W05 | GTM_2026-W05_763 | GTM_2026-W05_772 | Initial release; +R-160 username format; +D-047 relationship; +inheritance diagram |

---

#FlowsBros #FedArch #UserIdentity #TMPL009 #WeOwnSeason003

♾️ WeOwnNet 🌐 | 🏡 Real Estate and 🤝 cooperative ownership for everyone. An 🤗 inclusive community, by 👥 invitation only.
