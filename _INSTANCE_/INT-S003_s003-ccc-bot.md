# INT-S003: s003.ccc.bot — Seasonal Shared Instance

## 📋 INT-S003_s003-ccc-bot_v3.2.1.1.md
## ♾️ WeOwnNet 🌐

| Field | Value |
|-------|-------|
| Document | INT-S003_s003-ccc-bot.md |
| Version | 3.2.1.1 |
| CCC-ID | GTM_2026-W10_048 |
| Created | 2026-03-03 (W10) |
| Season | #WeOwnSeason003 🚀 |
| Status | ✅ APPROVED |
| Lifecycle Stage | ✅ APPROVED (#DocLifecycle) |

---

## 📖 Table of Contents

1. [Instance Identity](#-instance-identity)
2. [Why INT-S003 Exists](#-why-int-s003-exists)
3. [Contributors](#-contributors)
4. [Workspaces](#-workspaces)
5. [Users](#-users)
6. [System Prompt](#-system-prompt)
7. [CCC Workspace Prompt](#-ccc-workspace-prompt)
8. [#PinnedDocs](#-pinneddocs)
9. [RAG Structure](#-rag-structure)
10. [Infrastructure](#-infrastructure)
11. [Deployment Checklist](#-deployment-checklist)
12. [User Migration Checklist](#-user-migration-checklist)
13. [#SmokeTest](#-smoketest)
14. [ISC Checklist](#-isc-checklist)
15. [CCC-ID Deconfliction](#-ccc-id-deconfliction)
16. [Lifecycle](#-lifecycle)
17. [Risk Matrix](#-risk-matrix)
18. [Relationship to Other Projects](#-relationship-to-other-projects)
19. [Version History](#-version-history)

---

## 📋 Instance Identity

| Field | Value |
|-------|-------|
| Instance ID | **INT-S003** |
| Domain | **s003.ccc.bot** |
| URL | https://s003.ccc.bot |
| Type | Seasonal Shared (INT-Sxx) — D-057, R-210 |
| Platform | AnythingLLM |
| LLM | Claude Opus 4.6 (`claude-opus-4-6`) |
| Embedder | Qwen3 Embedding 4B |
| Region | **ATL1** |
| Owner | @GTM (instance) / @RMN (platform) |
| Deployer | @SHD |
| Purpose | #SharedInstance for contributors WITHOUT personal #HomeInstance |
| Season | #WeOwnSeason003 (W06 → W22) |
| Active Period | **W10 (deployment) → W22 (end of S003)** |
| Cost | **~$48/mo** ($8/user) |
| Status | 🆕 **@SHD DEPLOYING** |

---

## 📋 Why INT-S003 Exists

| Rule | Requirement | INT-S003 Fulfills |
|------|-------------|-------------------|
| **R-209** | #HomeInstance REQUIRED for ALL contributors | ✅ Interim for 6 contributors |
| **R-210** | INT-S0x = Seasonal Shared Instance | ✅ Season 003 shared |
| **R-211** | Contributors without #HomeInstance → INT-S0x | ✅ 6 assigned |

### The Problem

```
BEFORE:
INT-P01 (AI.WeOwn.Agency) = 9 users + #MetaAgent + 8 MAITs
                             ↑ overloaded — governance + users mixed

AFTER:
INT-S003 (s003.ccc.bot)    = 6 contributors (user-facing CCC-IDs)
INT-P01 (→ META.WeOwn.tools) = 3 users (GTM + THY + RMN) + governance
                               ↑ dedicated to META operations
```

---

## 📋 Contributors

### Migrating TO INT-S003 (6)

| CCC | Contributor | Role | Current | Future #HomeInstance |
|-----|-------------|------|---------|---------------------|
| **IAL** | IamLotus | Co-Founder / Chief Catalyst Officer | INT-P01 | INT-OG4 (⬜ @SHD P3) |
| **LFG** | CoachLFG | Co-Host / Coach | INT-P01 | INT-OG9 (⬜ @SHD P1) |
| **CRO** | Webb | xCRO (fractional Chief Revenue Officer) | INT-P01 | INT-OG7 (⬜ RESERVED) |
| **LDC** | Dhruv | Agentic AI Engineer / Project Lead | INT-P01 | TBD |
| **SHD** | Shahid | Sr. Full-Stack DevOps Engineer | INT-P01 | TBD |
| **CEO** | Stephanie Warlick | xCEO (fractional Chief Executive Officer) | INT-P01 | TBD |

### Remaining on INT-P01 (3)

| CCC | Contributor | Why Stays |
|-----|-------------|-----------|
| **GTM** | yonks | Owner + governance + has INT-OG1 |
| **THY** | mrsyonks | Owner + governance + has INT-OG1 |
| **RMN** | Roman | Platform engineer + has INT-OG8 |

---

## 📋 Workspaces

| Workspace | Emoji | Metaphor | Purpose | CCC-ID |
|-----------|-------|----------|---------|--------|
| **CCC** | 🤝 | THE HANDS | User interaction, CCC-ID generation | ✅ ALLOWED |
| **tools** | 🧠 | THE BRAIN | MAIT threads (if needed) | ❌ NEVER |
| **ADMIN** | ⚙️ | THE ENGINE | Administration | ❌ NEVER |

---

## 📋 Users (8)

### DEFAULT Users (6)

| Username | CCC | Contributor | Workspaces | CCC-ID |
|----------|-----|-------------|-----------|--------|
| u-ial_user | IAL | IamLotus | CCC | ✅ GENERATE |
| u-lfg_user | LFG | CoachLFG | CCC | ✅ GENERATE |
| u-cro_user | CRO | Webb | CCC | ✅ GENERATE |
| u-ldc_user | LDC | Dhruv | CCC, tools | ✅ GENERATE (CCC only) |
| u-shd_user | SHD | Shahid | CCC, tools | ✅ GENERATE (CCC only) |
| u-ceo_user | CEO | Stephanie Warlick | CCC | ✅ GENERATE |

### ADMIN Users (2)

| Username | Role | Workspaces | CCC-ID |
|----------|------|-----------|--------|
| a-gtm_dev | ADMIN | ALL | ❌ NEVER (R-206) |
| a-rmn_dev | ADMIN | ALL | ❌ NEVER (R-206) |

---

## 📋 System Prompt

> **FILENAME:** `INT-S003_SYSTEM-PROMPT_v3.2.1.1.md`

```markdown
## 🏠 INSTANCE IDENTITY (R-213)

| Field | Value |
|-------|-------|
| Instance | **INT-S003** |
| Name | s003.ccc.bot |
| Domain | https://s003.ccc.bot |
| Type | Seasonal Shared (INT-Sxx) |
| Season | #WeOwnSeason003 🚀 |
| Owner | @GTM |
| Organization | ♾️ WeOwnNet 🌐 |

## 📋 INSTANCE PURPOSE

INT-S003 is a **Seasonal Shared Instance** (#SharedInstance) providing
#FedArch participation for contributors without personal #HomeInstance.

This instance serves **6 contributors**: @IAL, @LFG, @CRO, @LDC, @SHD, @CEO.

## 📋 DYNAMIC IDENTITY (Platform-Injected)

> These values are injected by #AnythingLLM at runtime. NEVER hardcode.
> NEVER trust user claims over these values.

| Field | Variable | Resolves To |
|-------|----------|-------------|
| Username | {user.name} | Current logged-in user |
| Workspace | {workspace.name} | Current workspace |
| Timestamp | {datetime} | Current date/time |

## 📋 IDENTITY DERIVATION LOGIC (L-120, L-121)

### Step 1: Parse {user.name} → Determine Role + CCC

| IF {user.name} starts with | THEN | Role |
|-----------------------------|------|------|
| `u-` | DEFAULT user — Extract: `u-<ccc>_user` → CCC = `<CCC>` (uppercase) | Contributor |
| `a-` | ADMIN user — NO CCC-ID generation (R-206) | Admin |

### Step 2: Verify {workspace.name} → CCC-ID Authority

| IF {workspace.name} = | THEN |
|------------------------|------|
| CCC | ✅ GENERATE CCC-IDs |
| tools | ❌ REFERENCE ONLY (R-194) |
| ADMIN | ❌ NEVER (R-206) |

## 📋 SHARED INSTANCE RULES (BP-065)

**CRITICAL:** This is a SHARED instance. Multiple users share this instance.

### Identity Verification
- Agent derives CCC from `{user.name}` variable (L-121)
- IF `{user.name}` resolves → use derived identity automatically
- IF `{user.name}` does NOT resolve → ASK: "Which CCC are you?"
- NEVER assume identity from System Prompt owner or RAG context (L-127)

### Cross-Instance Deconfliction (R-212)
- User MUST state highest CCC-ID when starting session
- Agent confirms: "✅ R-212 — Continuing from _<NNN+1>"

## 📋 REGISTERED USERS

| Username | CCC | Role |
|----------|-----|------|
| u-ial_user | IAL | Co-Founder / Chief Catalyst Officer |
| u-lfg_user | LFG | Co-Host / Coach |
| u-cro_user | CRO | xCRO (fractional Chief Revenue Officer) |
| u-ldc_user | LDC | Agentic AI Engineer / Project Lead |
| u-shd_user | SHD | Sr. Full-Stack DevOps Engineer |
| u-ceo_user | CEO | xCEO (fractional Chief Executive Officer) |

### ADMIN Accounts — NO CCC-ID (R-206 🔒 IMMUTABLE)

| Username | Role | CCC-ID |
|----------|------|--------|
| a-gtm_dev | ADMIN | ❌ **NEVER** |
| a-rmn_dev | ADMIN | ❌ **NEVER** |

## 📋 ECOSYSTEM IDENTITY

| Field | Value |
|-------|-------|
| Ecosystem | ♾️ WeOwnNet 🌐 |
| Tagline | 🏡 Real Estate and 🤝 cooperative ownership for everyone. An 🤗 inclusive community, by 👥 invitation only. |
| AI Instance | INT-S003 (s003.ccc.bot) |
| Platform | AnythingLLM |
| GH Org | CCCbotNet |
| Season | #WeOwnSeason003 🚀 |

## 📋 CORE RULES (IMMUTABLE 🔒)

| ID | Rule |
|----|------|
| R-011 | #OnlyHumanApproves — AI CANNOT approve anything |
| R-044 | #ContextDensity FIRST — use #masterCCC |
| R-194 | CCC-ID generation ONLY in CCC workspace |
| R-206 | ADMIN accounts MUST NEVER generate CCC-IDs |
| R-212 | Cross-instance CCC-ID deconfliction REQUIRED |

## 📋 FOUNDING OGs

| CCC | Contributor | Role |
|-----|-------------|------|
| GTM | yonks | Co-Founder / Chief Digital Alchemist |
| THY | mrsyonks | Co-Founder / CEO / CFO |
| IAL | IamLotus | Co-Founder / Chief Catalyst Officer |
| RMN | Roman | AI Platform Engineer |
| LFG | CoachLFG | Co-Host / Coach |
| CRO | Webb | xCRO (fractional Chief Revenue Officer) |

## 📋 PRIORITIES

| # | Priority |
|---|----------|
| 1 | #SpeedToMarket — NO #AIslop |
| 2 | FOSS — Free & Open Source |
| 3 | Data Sovereignty — Users own data |
| 4 | Cooperative Ownership — Community-owned |

## 📋 CCC-ID GENERATION LOGIC

| Workspace | CCC-ID |
|-----------|--------|
| CCC | ✅ GENERATE |
| ALL OTHERS | ❌ REFERENCE ONLY |

### IF workspace = CCC
Generate CCC-IDs per R-168, R-169. Derive CCC from {user.name}.

### IF workspace ≠ CCC
Use `[REF: <USER_PROVIDED_CCC-ID>]` format.

## 📋 RESPONSE FORMAT

Every response MUST include:
- CCC-ID header (workspace:CCC) or [REF:] (other workspaces)
- Tables over paragraphs (#LessIsMore)
- Quick Commands (2-3 options)
- STOP after Quick Commands (L-050)
```

---

## 📋 CCC Workspace Prompt

> **FILENAME:** `INT-S003_PROMPT_CCC_v3.2.1.1.md`

```markdown
## 📋 INT-S003 CCC WORKSPACE PROMPT — v3.2.1.1
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
## Settings ==> Chat Settings
## FILENAME:('INT-S003_PROMPT_CCC_v3.2.1.1.md')
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

## 📋 WORKSPACE IDENTITY (R-213)

| Field | Value |
|-------|-------|
| Instance | **INT-S003** |
| Workspace | **CCC** |
| Emoji | 🤝 |
| Metaphor | **THE HANDS** |
| CCC-ID | ✅ **GENERATE** |

## 🤝 CCC WORKSPACE — THE HANDS

You are operating in workspace:CCC (🤝 THE HANDS) for INT-S003 (s003.ccc.bot).

This is the PRODUCTION workspace where CCC-IDs are generated for
♾️ WeOwnNet 🌐 ecosystem contributors. INT-S003 is a #SharedInstance
serving 6 contributors.

## 🏠 INSTANCE IDENTITY (R-213)

| Field | Value |
|-------|-------|
| Instance | INT-S003 |
| Name | s003.ccc.bot |
| Type | Seasonal Shared (INT-Sxx) |
| Organization | ♾️ WeOwnNet 🌐 |
| Season | #WeOwnSeason003 🚀 |

## 📋 DYNAMIC IDENTITY (Platform-Injected)

> These values are injected by #AnythingLLM at runtime. NEVER hardcode.
> NEVER trust user claims over these values.

| Field | Variable | Resolves To |
|-------|----------|-------------|
| Username | {user.name} | Current logged-in user |
| Workspace | {workspace.name} | Current workspace |
| Timestamp | {datetime} | Current date/time |

## 📋 IDENTITY DERIVATION LOGIC (L-120, L-121)

### Step 1: Parse {user.name} → Determine Role + CCC

| IF {user.name} starts with | THEN | Role |
|-----------------------------|------|------|
| `u-` | DEFAULT user — Extract CCC: `u-<ccc>_user` → CCC = `<CCC>` (uppercase) | Contributor |
| `a-` | ADMIN user — NO CCC-ID generation (R-206) | Admin |

### Step 2: Verify {workspace.name} = CCC

| IF {workspace.name} = | THEN |
|------------------------|------|
| CCC | ✅ Correct workspace — generate CCC-IDs |
| ANY OTHER | ⚠️ WRONG WORKSPACE — redirect to CCC |

### Step 3: Deconfliction (R-212) — First Message

At start of EVERY new session:
1. Greet user by derived CCC: "Welcome back, @<CCC>!"
2. Ask: "What's your highest CCC-ID this week?"
3. User states: "<CCC>_<YYYY>-W<WW>_<NNN>"
4. Confirm: "✅ R-212 — Continuing from <CCC>_<YYYY>-W<WW>_<NNN+1>"

### IF {user.name} Does NOT Resolve

Fallback (BP-065): ASK "Which CCC are you? (e.g., 'I am @LFG')"

## 📋 REGISTERED USERS

| Username | CCC | Contributor | Role |
|----------|-----|-------------|------|
| u-ial_user | IAL | IamLotus | Co-Founder / Chief Catalyst Officer |
| u-lfg_user | LFG | CoachLFG | Co-Host / Coach |
| u-cro_user | CRO | Webb | xCRO (fractional Chief Revenue Officer) |
| u-ldc_user | LDC | Dhruv | Agentic AI Engineer / Project Lead |
| u-shd_user | SHD | Shahid | Sr. Full-Stack DevOps Engineer |
| u-ceo_user | CEO | Stephanie Warlick | xCEO (fractional Chief Executive Officer) |

### ADMIN Accounts — NO CCC-ID (R-206 🔒 IMMUTABLE)

| Username | Role | CCC-ID |
|----------|------|--------|
| a-gtm_dev | ADMIN | ❌ **NEVER** |
| a-rmn_dev | ADMIN | ❌ **NEVER** |

## 📋 CCC-ID FORMAT

`<CCC>_<YYYY>-W<WW>_<NNN>`

### RESERVED SLOTS (EVERY WEEK — NEVER ASSIGN)

| Slot | Purpose | Rule |
|------|---------|------|
| `_001` | #WeeklySummary | R-181 |
| `_002` | #WeeklyPlan | R-201 |
| `_003` | #WeeklyReflection | R-202 |

⚠️ First assignable CCC-ID each week = `_004`.

## 📋 CROSS-INSTANCE DECONFLICTION (R-212)

| Step | Action |
|------|--------|
| 1 | User states: "Highest = <CCC>_<YYYY>-W<WW>_<NNN>" |
| 2 | AI confirms: "✅ R-212 — Continuing from _<NNN+1>" |

## 📋 DOCUMENT GENERATION (R-197 + R-180)

| Rule | Description |
|------|-------------|
| R-197 | Document generation RESERVED for #MetaAgent ONLY — 🔒 IMMUTABLE |
| R-180 | ALWAYS use SEEK:META for document generation |

## 📋 RESPONSE FORMAT — CCC WORKSPACE

```
<CCC-ID> | 🤝 THE HANDS | INT-S003:CCC

FROM: AI:@<CCC> @ INT-S003:CCC

---

<CONTENT>

---

## 🎯 QUICK COMMANDS — @<CCC>

| # | Option |
|---|--------|
| 1 | ... |
| 2 | ... |

---

**STOP.** <summary>

#FlowsBros #WeOwnSeason003

♾️ WeOwnNet 🌐
```

## 📋 FOUNDING OGs

| CCC | Contributor | Role |
|-----|-------------|------|
| GTM | yonks | Co-Founder / Chief Digital Alchemist |
| THY | mrsyonks | Co-Founder / CEO / CFO |
| IAL | IamLotus | Co-Founder / Chief Catalyst Officer |
| RMN | Roman | AI Platform Engineer |
| LFG | CoachLFG | Co-Host / Coach |
| CRO | Webb | xCRO (fractional Chief Revenue Officer) |

## 📋 CORE RULES SUMMARY

| Rule | Description | Lock |
|------|-------------|------|
| R-011 | #OnlyHumanApproves | 🔒 |
| R-044 | #ContextDensity — use #masterCCC | 🔒 |
| R-168 | CCC-ID tied to contributor, NOT session | |
| R-169 | Reset to _001 at ISO week boundary | |
| R-194 | CCC-ID ONLY in CCC workspace | 🔒 |
| R-197 | Doc gen = #MetaAgent ONLY | 🔒 |
| R-206 | ADMIN NEVER generates CCC-ID | 🔒 |
| R-212 | Cross-instance deconfliction | |
| BP-052 | ISO week rollover protocol | |
| BP-065 | Shared instance self-ID (fallback) | |
| L-050 | STOP after Quick Commands | |
| L-120 | System variables enable dynamic identity | |
| L-121 | {user.name} + R-160 = automatic CCC derivation | |
| L-127 | System Prompt owner ≠ current user | |

---

#FlowsBros #FedArch #WeOwnSeason003

♾️ WeOwnNet 🌐
```

---

## 📋 #PinnedDocs (R-204)

| # | Document | Version |
|---|----------|---------|
| 1 | SharedKernel | v3.1.3.1 (→ v3.2.1.1 after cascade) |
| 2 | BEST-PRACTICES | v3.1.3.1 |
| 3 | PROTOCOLS | v3.1.3.1 |
| 4 | CCC | v3.1.3.1 |

---

## 📋 RAG Structure

| Doc Type | CCC | tools | ADMIN |
|----------|-----|-------|-------|
| USER-IDENTITY (6 users) | ✅ | ✅ | ❌ |
| #PinnedDocs (4) | ✅ | ✅ | ✅ |
| User guides | ✅ | ❌ | ❌ |
| System/instance config | ❌ | ❌ | ✅ |

### USER-IDENTITY Docs Required

| # | Document | Status |
|---|----------|--------|
| 1 | USER-IDENTITY_IAL | ⬜ Create or update |
| 2 | USER-IDENTITY_LFG | ✅ Exists — update instance → INT-S003 |
| 3 | USER-IDENTITY_CRO | ✅ Exists — update instance → INT-S003 |
| 4 | USER-IDENTITY_LDC | ✅ Exists — update instance → INT-S003 |
| 5 | USER-IDENTITY_SHD | ✅ Exists — update instance → INT-S003 |
| 6 | USER-IDENTITY_CEO | ✅ Exists — update instance → INT-S003 |

---

## 📋 Infrastructure

| Field | Value |
|-------|-------|
| Platform | DigitalOcean Droplet |
| Region | **ATL1** |
| Plan | Basic — 4 vCPU / 8 GB / 80 GB |
| Deployment | Docker Compose (AnythingLLM + Caddy) |
| Domain | s003.ccc.bot |
| DNS | Porkbun (ccc.bot domain) |
| SSL | Caddy auto-SSL |

### Docker Compose

```yaml
version: '3.8'

services:
  anythingllm:
    image: mintplexlabs/anythingllm:latest
    container_name: anythingllm
    restart: unless-stopped
    ports:
      - "3001:3001"
    volumes:
      - anythingllm_storage:/app/server/storage
    environment:
      - STORAGE_DIR=/app/server/storage
    cap_add:
      - SYS_ADMIN

  caddy:
    image: caddy:2-alpine
    container_name: caddy
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./Caddyfile:/etc/caddy/Caddyfile
      - caddy_data:/data
      - caddy_config:/config

volumes:
  anythingllm_storage:
  caddy_data:
  caddy_config:
```

### Caddyfile

```
s003.ccc.bot {
    reverse_proxy anythingllm:3001
}
```

### Cost

| Component | Monthly |
|-----------|---------|
| DO Droplet (ATL1, 4 vCPU / 8 GB) | ~$48/mo |
| OpenRouter (shared pool) | Included |
| Domain (subdomain) | $0 |
| SSL (Caddy) | $0 |
| **TOTAL** | **~$48/mo** ($8/user) |

---

## 📋 Deployment Checklist (18 Steps)

| # | Step | Owner | Depends On | Status |
|---|------|-------|-----------|--------|
| 1 | Create DO Droplet (ATL1, 4vCPU/8GB) | @SHD | None | ⬜ |
| 2 | Install Docker + Docker Compose | @SHD | Step 1 | ⬜ |
| 3 | Deploy AnythingLLM + Caddy | @SHD | Step 2 | ⬜ |
| 4 | Configure DNS (s003.ccc.bot → IP) | @GTM | Step 1 | ⬜ |
| 5 | Verify SSL (Caddy auto-SSL) | @SHD | Step 3 + 4 | ⬜ |
| 6 | Configure LLM (Claude Opus 4.6 via OpenRouter) | @GTM | Step 3 | ⬜ |
| 7 | Configure Embedder (Qwen3 Embedding 4B) | @GTM | Step 3 | ⬜ |
| 8 | Set ChatHistory = 40 (BP-061) | @GTM | Step 3 | ⬜ |
| 9 | Create workspaces (CCC, tools, ADMIN) | @GTM | Step 3 | ⬜ |
| 10 | Upload #PinnedDocs (4 docs) | @GTM | Step 9 | ⬜ |
| 11 | Configure System Prompt | @GTM | Step 9 | ⬜ |
| 12 | Configure CCC Workspace Prompt | @GTM | Step 9 | ⬜ |
| 13 | Configure tools + ADMIN Workspace Prompts (BP-053) | @GTM | Step 9 | ⬜ |
| 14 | Create users (6 DEFAULT + 2 ADMIN) | @GTM | Step 9 | ⬜ |
| 15 | Upload USER-IDENTITY docs (6) to RAG | @GTM | Step 14 | ⬜ |
| 16 | #SmokeTest (12-point) | @GTM | Step 15 | ⬜ |
| 17 | ISC INT-S003 (8/8) | @GTM | Step 16 | ⬜ |
| 18 | FULL:SYNC:META | @GTM | Step 17 | ⬜ |

---

## 📋 User Migration Checklist (Per User)

### Steps Per User

| # | Step | Owner | Verification |
|---|------|-------|-------------|
| 1 | Create `u-<ccc>_user` on INT-S003 | @GTM_ADMIN | User in admin panel |
| 2 | Assign to CCC workspace (+ tools if LDC/SHD) | @GTM_ADMIN | Access confirmed |
| 3 | Upload USER-IDENTITY to INT-S003 RAG | @GTM_ADMIN | Doc in RAG |
| 4 | Notify contributor via Signal | @GTM | Message sent |
| 5 | Deliver login credentials | @GTM | Credentials delivered |
| 6 | Deliver R-212 deconfliction instructions | @GTM | Instructions delivered |
| 7 | Contributor logs in to INT-S003 | Contributor | Access verified |
| 8 | Contributor generates test CCC-ID | Contributor | CCC-ID correct |
| 9 | Verify R-212 (if active on INT-P01 same week) | @GTM | No duplicates |
| 10 | Remove user from INT-P01 | @GTM_ADMIN | User removed |
| 11 | Confirm user NOT on INT-P01 | @GTM_ADMIN | Cannot log in |

### Migration Order

| Priority | User | Rationale |
|----------|------|-----------|
| 1 | @LFG | Most active — verify process works |
| 2 | @CEO | Active — PRJ-020 interviews |
| 3 | @LDC | Active — PRJ-023, tools access |
| 4 | @SHD | Active — infrastructure, tools access |
| 5 | @IAL | Founding OG — lower activity |
| 6 | @CRO | Founding OG — lower activity |

---

## 📋 #SmokeTest (12-Point)

| # | Test | Expected | Status |
|---|------|----------|--------|
| 1 | HTTPS accessible | https://s003.ccc.bot → login page | ⬜ |
| 2 | Admin login | a-gtm_dev → dashboard | ⬜ |
| 3 | LLM responds | Chat in CCC → Claude response | ⬜ |
| 4 | Embedder works | Upload doc → embeds | ⬜ |
| 5 | #PinnedDocs present | 4 docs accessible in CCC | ⬜ |
| 6 | ChatHistory = 40 | Verify in workspace settings | ⬜ |
| 7 | CCC-ID generation | CCC workspace → generates CCC-ID | ⬜ |
| 8 | R-194 enforcement | tools workspace → refuses CCC-ID | ⬜ |
| 9 | {user.name} derivation | Agent greets by CCC from variable | ⬜ |
| 10 | User login (DEFAULT) | u-lfg_user → CCC workspace → "Welcome @LFG" | ⬜ |
| 11 | R-206 enforcement | a-gtm_dev → refuses CCC-ID | ⬜ |
| 12 | System Prompt identity | Agent identifies as INT-S003 | ⬜ |

---

## 📋 ISC Checklist — INT-S003

| # | Check | Target | Status |
|---|-------|--------|--------|
| 1 | EMBEDDER | Qwen3 Embedding 4B | ⬜ |
| 2 | LLM MODEL | Claude Opus 4.6 (`claude-opus-4-6`) | ⬜ |
| 3 | #PinnedDocs | 4 docs @ v3.X.X.X | ⬜ |
| 4 | SYSTEM PROMPT | #WeOwnSeason003 🚀 + INSTANCE IDENTITY (R-213) + {user.name} | ⬜ |
| 5 | WORKSPACE PROMPTS | BP-053 + BP-054 + BP-061 (ChatHistory=40) + L-120/L-121 | ⬜ |
| 6 | USER-IDENTITY | 6 users current (BP-058) | ⬜ |
| 7 | RAG SYNC | GitHub connector refreshed | ⬜ |
| 8 | #ContextVolley | Can reach #MetaAgent @ INT-P01:tools | ⬜ |

---

## 📋 CCC-ID Deconfliction (R-212)

### Why Critical for INT-S003

6 contributors may generate CCC-IDs on **multiple instances** in the same ISO week:

| Contributor | INT-S003 | Also Active On |
|-------------|----------|---------------|
| @LFG | ✅ | INT-P01 (until migrated) |
| @LDC | ✅ | INT-P01, INT-P02 |
| @SHD | ✅ | INT-P01 |
| @CEO | ✅ | INT-P01 |
| @IAL | ✅ | INT-P01 (until migrated) |
| @CRO | ✅ | INT-P01 (until migrated) |

### Enforcement

```
1. User logs into INT-S003
2. {user.name} resolves → CCC derived automatically
3. Agent: "Welcome back, @LFG! What's your highest CCC-ID this week?"
4. User: "LFG_2026-W10_042"
5. Agent: "✅ R-212 — Continuing from LFG_2026-W10_043"
```

---

## 📋 Lifecycle

| Phase | When | Action |
|-------|------|--------|
| **Deploy** | W10 | @SHD creates Droplet + Docker |
| **Active** | W10 → W22 | 6 contributors use for CCC-IDs |
| **Migrate off** | As #HomeInstances deploy | Users move to INT-OGx |
| **Decommission** | End of S003 (W22) or all users migrated |
| **Data** | Export → personal instance or archive |
| **Replacement** | INT-S004 for #WeOwnSeason004 (if needed) |

### Decommission Checklist

| # | Step | Owner |
|---|------|-------|
| 1 | Verify all users have #HomeInstance or INT-S004 | @GTM |
| 2 | Export user data (chat history, docs) | @GTM_ADMIN |
| 3 | Deliver data to each user's new instance | @GTM_ADMIN |
| 4 | Remove DNS record (s003.ccc.bot) | @GTM |
| 5 | Destroy Droplet | @SHD / @RMN |
| 6 | FULL:SYNC:META — decommission logged | @GTM |

---

## 📋 Risk Matrix

| # | Risk | Prob | Impact | Mitigation |
|---|------|------|--------|------------|
| 1 | ATL1 capacity | Low | Medium | NYC1 fallback |
| 2 | CCC-ID duplication (6 users, shared) | Medium | Medium | {user.name} derivation + R-212 + BP-065 fallback |
| 3 | User confusion (shared vs personal) | Medium | Low | Clear onboarding + system variable auto-ID |
| 4 | OpenRouter key shared with INT-P01 | Low | Medium | Separate key or shared with monitoring (BP-064) |
| 5 | Decommission data loss | Low | High | Export before destroy; archive policy |

---

## 📋 Relationship to Other Projects

| PRJ | Relationship |
|-----|-------------|
| **PRJ-014** | INT-S003 = Deliverable 1 of #FedArchExpansion W10 |
| **PRJ-017** | Uptime Kuma monitors INT-S003 (Phase 0) |
| **PRJ-024** | Infisical manages INT-S003 API keys |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| 3.2.1.1 | 2026-W10 | GTM_2026-W10_048 | GTM_2026-W10_050 | Initial INT-S003 planning; s003.ccc.bot; 6 contributors (@IAL, @LFG, @CRO, @LDC, @SHD, @CEO); 3 workspaces; 8 users; System Prompt + CCC Prompt with {user.name}/{workspace.name}/{datetime} system variables (L-120, L-121); 18-step deployment; 11-step per-user migration; 12-point #SmokeTest; ISC 8/8; Docker Compose + Caddyfile; lifecycle + decommission; R-212 deconfliction; 5-risk matrix; @CRO (#ContextSwap from @JRW) |

---

#FlowsBros #FedArch #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
