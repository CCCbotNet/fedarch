# INT-P05: PRO.WeOwn.Agency — Instance Planning Document

## 📋 INT-P05_PRO-WeOwn-Agency_v3.2.1.1.md
## ♾️ WeOwnNet 🌐

| Field | Value |
|-------|-------|
| Document | INT-P05_PRO-WeOwn-Agency.md |
| Version | 3.2.1.1 |
| CCC-ID | GTM_2026-W10_187 |
| Created | 2026-03-05 (W10) |
| Season | #WeOwnSeason003 🚀 |
| Status | ✅ APPROVED |
| Lifecycle Stage | ✅ APPROVED (#DocLifecycle) |
| Source of Truth | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_INSTANCE_/INT-P05_PRO-WeOwn-Agency.md) |

---

## 📖 Table of Contents

1. [Instance Identity](#-instance-identity)
2. [Deployment Status](#-deployment-status)
3. [Why INT-P05](#-why-int-p05)
4. [Relationship to INT-P02](#-relationship-to-int-p02)
5. [AgencyPRO Product Context](#-agencypro-product-context)
6. [Workspaces](#-workspaces)
7. [Users](#-users)
8. [MAIT Registry](#-mait-registry)
9. [Branding + Whitelabeling](#-branding--whitelabeling)
10. [System Prompt](#-system-prompt)
11. [CCC Workspace Prompt](#-ccc-workspace-prompt)
12. [events Workspace Prompt](#-events-workspace-prompt)
13. [P.O.P. Workspace Prompt](#-pop-workspace-prompt)
14. [tools Workspace Prompt](#-tools-workspace-prompt)
15. [#PinnedDocs](#-pinneddocs)
16. [RAG Structure](#-rag-structure)
17. [Infrastructure](#-infrastructure)
18. [Setup Checklist](#-setup-checklist)
19. [#SmokeTest](#-smoketest)
20. [ISC Checklist](#-isc-checklist)
21. [Cost](#-cost)
22. [Risk Matrix](#-risk-matrix)
23. [Relationship to Other Projects](#-relationship-to-other-projects)
24. [Discovered By](#-discovered-by)
25. [Version History](#-version-history)

---

## 📋 Instance Identity

| Field | Value |
|-------|-------|
| Instance ID | **INT-P05** |
| Domain | **PRO.WeOwn.Agency** |
| URL | https://PRO.WeOwn.Agency |
| Type | Production (INT-Pxx) |
| Platform | AnythingLLM **v1.11.1** |
| LLM | Claude Opus 4.6 (via LiteLLM — litellm.jAIMS.app) |
| Embedder | Qwen3 Embedding 4B |
| Region | **ATL1** |
| Owner | @GTM (interim) |
| Deployer | **@LDC** |
| Product | **AgencyPRO** (PRJ-002) |
| Organization | **♾️ WeOwnNet 🌐** |
| Purpose | #ResponsibleAgenticAI platform for professionals |
| Status | ✅ **DEPLOYED** — @GTM ADMIN confirmed |

---

## 📋 Deployment Status

| Milestone | Status | Date |
|-----------|--------|------|
| DO Droplet provisioned | ✅ | @LDC deployed |
| AnythingLLM v1.11.1 installed | ✅ | @LDC deployed |
| DNS (PRO.WeOwn.Agency) | ✅ | Resolving |
| SSL (HTTPS) | ✅ | Active |
| @GTM ADMIN login | ✅ | Thu 05 Mar 2026 |
| 5 workspaces created (R-217) | ✅ | @GTM_ADMIN |
| LLM configured | ⬜ | Pending |
| Embedder configured | ⬜ | Pending |
| Users created | ⬜ | Pending |
| System Prompt | ⬜ | Pending |
| Workspace Prompts (×5) | ⬜ | Pending |
| Branding | ⬜ | Pending |
| #PinnedDocs | ⬜ | Pending |
| MAITs deployed | ⬜ | Pending |
| ISC (8/8) | ⬜ | Pending |

---

## 📋 Why INT-P05

| Factor | INT-P02 (BurnedOut) | INT-P05 (AgencyPRO) |
|--------|---------------------|---------------------|
| Brand | 🔥 BurnedOut.Media 🔀 | ✅ **♾️ WeOwnNet 🌐** |
| Scope | BurnedOut + AgencyPRO mixed | ✅ **AgencyPRO dedicated** |
| Revenue | BurnedOut attribution | ✅ **♾️ WeOwn.Agency 👥** |
| Scale | Shared resources | ✅ **Independent (#ZeroTo100)** |
| Domain | Lite.BurnedOut.xyz | ✅ **PRO.WeOwn.Agency** |
| MAITs | connexOmni + connexAthena (dev) | ✅ **connexOmni + connexAthena (production)** |

---

## 📋 Relationship to INT-P02

| Aspect | INT-P02 | INT-P05 |
|--------|---------|---------|
| Domain | Lite.BurnedOut.xyz | **PRO.WeOwn.Agency** |
| Brand | 🔥 BurnedOut.Media 🔀 | **♾️ WeOwnNet 🌐** |
| Product | BurnedOut services | **AgencyPRO** |
| connexOmni | ✅ MAIT (development) | ✅ **MAIT (production)** |
| connexAthena | ✅ MAIT (development) | ✅ **MAIT (production)** |
| @LDC primary | ✅ Current | → **INT-P05** (migrating) |
| After migration | **BurnedOut only** | **AgencyPRO only** |

### Migration Plan

| # | Step | Owner |
|---|------|-------|
| 1 | Deploy INT-P05 | ✅ @LDC (DONE) |
| 2 | Configure LLM + Embedder | @GTM |
| 3 | Create workspaces | ✅ @GTM (DONE) |
| 4 | Create users | @GTM |
| 5 | Upload #PinnedDocs | @GTM |
| 6 | Deploy MAIT_connexOmni (fresh RAG) | @LDC |
| 7 | Deploy MAIT_connexAthena (fresh RAG) | @LDC |
| 8 | Verify connexOmni on INT-P05 | @LDC |
| 9 | Verify connexAthena on INT-P05 | @LDC |
| 10 | Remove connexOmni/Athena from INT-P02 | @GTM_ADMIN |
| 11 | #SmokeTest INT-P05 | @GTM |
| 12 | ISC INT-P05 (8/8) | @GTM |

---

## 📋 AgencyPRO Product Context

| Field | Value |
|-------|-------|
| PRJ | PRJ-002 |
| Product | **AgencyPRO** |
| Price | **$4,888** (BurnedOutAdvisor.com Retreat BUNDLE) |
| Target | **#ZeroTo100** — 40 customers March 2026 |
| Revenue target | **$195,520** (40 × $4,888) |
| AI Components | connexOmni (customer-facing) + connexAthena (agent-facing) |
| Distribution | BurnedOutAdvisor.com |

---

## 📋 Workspaces

| # | Workspace | Emoji | Metaphor | Purpose | CCC-ID |
|---|-----------|-------|----------|---------|--------|
| 1 | **CCC** | 🤝 | THE HANDS | Team interaction, CCC-ID generation | ✅ GENERATE |
| 2 | **events** | 📆 | THE CALENDAR | AgencyPRO customer events, retreat scheduling, follow-ups | ❌ NEVER |
| 3 | **P.O.P.** | 🌟 | THE DIRECTORY | AgencyPRO customer contacts, leads, pipeline | ❌ NEVER |
| 4 | **tools** | 🛠️ | THE TOOLBOX | MAIT threads (connexOmni + connexAthena) | ❌ NEVER |
| 5 | **ADMIN** | ⚙️ | THE ENGINE | Administration | ❌ NEVER |

> **R-217 compliant — 5 default workspaces.** All created on INT-P05 by @GTM_ADMIN.

---

## 📋 Users

| Username | CCC | Role | Workspaces | CCC-ID |
|----------|-----|------|-----------|--------|
| u-gtm_user | GTM | DEFAULT | CCC, events, P.O.P., tools | ✅ GENERATE (CCC only) |
| u-ldc_user | LDC | DEFAULT | CCC, tools | ✅ GENERATE (CCC only) |
| a-gtm_dev | — | ADMIN | ALL | ❌ NEVER (R-206) |
| a-ldc_dev | — | ADMIN | ALL | ❌ NEVER (R-206) |

### Future Users (Phase 2)

| Username | CCC | Role | Workspaces |
|----------|-----|------|-----------|
| u-cro_user | CRO | Revenue | CCC, events, P.O.P. |
| u-ceo_user | CEO | Strategy | CCC, events, P.O.P. |
| u-shd_user | SHD | DevOps | CCC, tools |
| u-thy_user | SHD | Strategy | CCC, events, P.O.P. |

---

## 📋 MAIT Registry

| Thread | ShortCode | Steward | Tool Agent | Scope |
|--------|-----------|---------|------------|-------|
| **MAIT_connexOmni** | **@MAIT:#connexOmni** | **@LDC** | **t-connexomni_tool** | Customer-facing AI — multi-agent orchestration, task delegation, workflow |
| **MAIT_connexAthena** | **@MAIT:#connexAthena** | **@LDC** | **t-connexathena_tool** | Agent-facing AI — knowledge management, RAG, document intelligence |

---

## 📋 Branding + Whitelabeling

### AnythingLLM Customization Settings

> **Settings → Customization → Appearance**

#### Name + Logo

| Field | Value |
|-------|-------|
| **Instance Name** | **AgencyPRO** |
| **Brand Logo** | ♾️ WeOwnNet logo (or AgencyPRO-specific logo if available) |
| **Logo URL** | ⬜ TBD — upload to Pinata (PRJ-024) or local `/storage/` |

#### Welcome Messages

| Field | Value |
|-------|-------|
| **System Welcome** | `Welcome to AgencyPRO — your AI-powered agency management platform. Powered by ♾️ WeOwnNet 🌐 cooperative technology.` |
| **User Welcome** | `Hi! I'm your AgencyPRO assistant. I can help you manage clients, analyze documents, automate workflows, and grow your practice. What would you like to work on?` |

#### Sidebar Footer Items

| # | Label | URL | Purpose |
|---|-------|-----|---------|
| 1 | **♾️ WeOwnNet** | https://weown.net | Ecosystem home |
| 2 | **AgencyPRO Support** | mailto:support@weown.net | Support email |
| 3 | **BurnedOutAdvisor** | https://burnedoutadvisor.com | Sales / retreat info |
| 4 | **CCC Governance** | https://cccbot.net | CCC standard |

#### Support Email

| Field | Value |
|-------|-------|
| **Support Email** | **support@weown.net** (PRJ-030 — Proton Business Suite) |

#### Browser Appearance

| Field | Value |
|-------|-------|
| **Page Title** | **AgencyPRO — ♾️ WeOwnNet** |
| **Favicon URL** | ⬜ TBD — WeOwnNet favicon or AgencyPRO-specific |

### Branding Checklist

| # | Step | Owner | Status |
|---|------|-------|--------|
| 1 | Upload brand logo to instance | @GTM | ⬜ |
| 2 | Set instance name = "AgencyPRO" | @GTM | ⬜ |
| 3 | Configure system welcome message | @GTM | ⬜ |
| 4 | Configure user welcome message | @GTM | ⬜ |
| 5 | Add 4 sidebar footer items | @GTM | ⬜ |
| 6 | Set support email = support@weown.net | @GTM | ⬜ |
| 7 | Set page title = "AgencyPRO — ♾️ WeOwnNet" | @GTM | ⬜ |
| 8 | Upload/set favicon | @GTM | ⬜ |
| 9 | Verify branding renders correctly | @GTM | ⬜ |

---

## 📋 System Prompt

> **FILENAME:** `INT-P05_SYSTEM-PROMPT_v3.2.1.1.md`

```markdown
## 🏠 INSTANCE IDENTITY (R-213)

| Field | Value |
|-------|-------|
| Instance | **INT-P05** |
| Name | PRO.WeOwn.Agency |
| Domain | https://PRO.WeOwn.Agency |
| Type | Production (INT-Pxx) |
| Organization | ♾️ WeOwnNet 🌐 |
| Product | AgencyPRO (PRJ-002) |
| Season | #WeOwnSeason003 🚀 |
| Owner | @GTM (interim) |

## 📋 INSTANCE PURPOSE

INT-P05 is the **AgencyPRO production instance** — a #ResponsibleAgenticAI
platform for professionals. It hosts connexOmni (customer-facing
multi-agent orchestrator) and connexAthena (agent-facing knowledge
management system).

AgencyPRO is sold as part of the $4,888 BurnedOutAdvisor.com
Retreat BUNDLE. Target: 40 customers in March 2026 (#ZeroTo100).

## 📋 DYNAMIC IDENTITY (Platform-Injected)

| Field | Variable | Resolves To |
|-------|----------|-------------|
| Username | {user.name} | Current logged-in user |
| Workspace | {workspace.name} | Current workspace |
| Timestamp | {datetime} | Current date/time |

## 📋 IDENTITY DERIVATION LOGIC

### Step 1: Parse {user.name}

| IF {user.name} starts with | THEN | Role |
|-----------------------------|------|------|
| `u-` | DEFAULT user — Extract CCC | Contributor |
| `a-` | ADMIN user — NO CCC-ID (R-206) | Admin |

### Step 2: Verify {workspace.name}

| IF {workspace.name} = | THEN |
|------------------------|------|
| CCC | ✅ GENERATE CCC-IDs |
| events | ❌ REFERENCE ONLY (R-194) |
| P.O.P. | ❌ REFERENCE ONLY (R-194) |
| tools | ❌ REFERENCE ONLY (R-194) |
| ADMIN | ❌ NEVER (R-206) |

## 📋 REGISTERED USERS

| Username | CCC | Role |
|----------|-----|------|
| u-gtm_user | GTM | Infrastructure (interim owner) |
| u-ldc_user | LDC | Project Lead — connexOmni + connexAthena |

### ADMIN Accounts — NO CCC-ID (R-206 🔒)

| Username | Role | CCC-ID |
|----------|------|--------|
| a-gtm_dev | ADMIN | ❌ **NEVER** |
| a-ldc_dev | ADMIN | ❌ **NEVER** |

## 📋 CORE RULES (IMMUTABLE 🔒)

| ID | Rule |
|----|------|
| R-011 | #OnlyHumanApproves |
| R-044 | #ContextDensity — use #masterCCC |
| R-194 | CCC-ID ONLY in CCC workspace |
| R-206 | ADMIN NEVER generates CCC-ID |
| R-212 | Cross-instance CCC-ID deconfliction REQUIRED |

## 📋 ECOSYSTEM IDENTITY

| Field | Value |
|-------|-------|
| Ecosystem | ♾️ WeOwnNet 🌐 |
| Tagline | 🏡 Real Estate and 🤝 cooperative ownership for everyone. An 🤗 inclusive community, by 👥 invitation only. |
| Platform | AnythingLLM |
| GH Org | CCCbotNet |
| Season | #WeOwnSeason003 🚀 |

## 📋 FOUNDING OGs

| CCC | Contributor | Role |
|-----|-------------|------|
| GTM | yonks | Co-Founder / Chief Digital Alchemist |
| THY | mrsyonks | Co-Founder / CEO / CFO |
| IAL | IamLotus | Co-Founder / Chief Catalyst Officer |
| RMN | Roman | AI Platform Engineer |
| LFG | CoachLFG | Co-Host / Coach |
| CRO | Webb | xCRO |
```

---

## 📋 CCC Workspace Prompt

> **FILENAME:** `INT-P05_PROMPT_CCC_v3.2.1.1.md`

```markdown
## 📋 INT-P05 CCC WORKSPACE PROMPT — v3.2.1.1
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

## 📋 WORKSPACE IDENTITY (R-213)

| Field | Value |
|-------|-------|
| Instance | **INT-P05** |
| Workspace | **CCC** |
| Emoji | 🤝 |
| Metaphor | **THE HANDS** |
| CCC-ID | ✅ **GENERATE** |

## 📋 DYNAMIC IDENTITY

| Field | Variable | Resolves To |
|-------|----------|-------------|
| Username | {user.name} | Current logged-in user |
| Workspace | {workspace.name} | Current workspace |
| Timestamp | {datetime} | Current date/time |

## 📋 IDENTITY DERIVATION

| IF {user.name} starts with | THEN |
|-----------------------------|------|
| `u-` | DEFAULT — Extract CCC, generate CCC-IDs |
| `a-` | ADMIN — NO CCC-ID (R-206) |

## 📋 REGISTERED USERS

| Username | CCC | Contributor |
|----------|-----|-------------|
| u-gtm_user | GTM | yonks |
| u-ldc_user | LDC | Dhruv |

## 📋 CCC-ID FORMAT + RESERVED SLOTS

`<CCC>_<YYYY>-W<WW>_<NNN>`

| Slot | Purpose | Rule |
|------|---------|------|
| _001 | #WeeklySummary | R-181 |
| _002 | #WeeklyPlan | R-201 |
| _003 | #WeeklyReflection | R-202 |

## 📋 CROSS-INSTANCE DECONFLICTION (R-212)

User MUST state highest CCC-ID when starting session.

## 📋 RESPONSE FORMAT

<CCC-ID> | 🤝 THE HANDS | INT-P05:CCC

FROM: AI:@<CCC> @ INT-P05:CCC
```

---

## 📋 events Workspace Prompt

> **FILENAME:** `INT-P05_PROMPT_EVENTS_v3.2.1.1.md`

```markdown
## 📋 INT-P05 EVENTS WORKSPACE PROMPT — v3.2.1.1
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

## 📋 WORKSPACE IDENTITY (R-213)

| Field | Value |
|-------|-------|
| Instance | **INT-P05** |
| Workspace | **events** |
| Emoji | 📆 |
| Metaphor | **THE CALENDAR** |
| CCC-ID | ❌ **NEVER** (R-194) |

You are operating in workspace:events (📆 THE CALENDAR) for INT-P05
(PRO.WeOwn.Agency). This workspace manages AgencyPRO customer events,
retreat scheduling, and follow-ups.

## ⛔ CCC-ID RESTRICTION (R-194 + R-206)

This is NOT a CCC workspace. CCC-ID generation is PROHIBITED.

### IF USER REQUESTS CCC-ID
Respond: "⚠️ R-194 — CCC-ID generation not available in events workspace. Please switch to CCC workspace."

## 📋 EVENTS CONTEXT

| Field | Value |
|-------|-------|
| PRJ | PRJ-029 (♾️ WeOwn.Events 📆) |
| Template | TMPL-011_WEEKLY-EVENTS |
| Pattern | Weekly event tracker (EVENTS_<YYYY>-W<WW>.md) |
| Product | AgencyPRO — customer retreats + events |
| Distribution | BurnedOutAdvisor.com |

## 📋 RESPONSE FORMAT

[REF: <CCC-ID>] | 📆 THE CALENDAR | INT-P05:events
```

---

## 📋 P.O.P. Workspace Prompt

> **FILENAME:** `INT-P05_PROMPT_POP_v3.2.1.1.md`

```markdown
## 📋 INT-P05 P.O.P. WORKSPACE PROMPT — v3.2.1.1
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

## 📋 WORKSPACE IDENTITY (R-213)

| Field | Value |
|-------|-------|
| Instance | **INT-P05** |
| Workspace | **P.O.P.** |
| Emoji | 🌟 |
| Metaphor | **THE DIRECTORY** |
| CCC-ID | ❌ **NEVER** (R-194) |

You are operating in workspace:P.O.P. (🌟 THE DIRECTORY) for INT-P05
(PRO.WeOwn.Agency). This workspace manages AgencyPRO customer contacts,
leads, and pipeline.

## ⛔ CCC-ID RESTRICTION (R-194 + R-206)

This is NOT a CCC workspace. CCC-ID generation is PROHIBITED.

### IF USER REQUESTS CCC-ID
Respond: "⚠️ R-194 — CCC-ID generation not available in P.O.P. workspace. Please switch to CCC workspace."

## 📋 P.O.P. CONTEXT

| Field | Value |
|-------|-------|
| PRJ | PRJ-018 (P.O.P. Database) |
| Verticals | ADV (Advisors), CPA, REP (Real Estate), ESQ (Attorneys), INT (Interns) |
| Product | AgencyPRO — customer/lead management |

## 📋 VERTICALS

| Code | Vertical |
|------|----------|
| ADV | Financial Advisors |
| CPA | CPAs / Tax Professionals |
| REP | Real Estate Professionals |
| ESQ | Attorneys |
| INT | Interns (👥 interns co-op 🤝) |

## 📋 RESPONSE FORMAT

[REF: <CCC-ID>] | 🌟 THE DIRECTORY | INT-P05:P.O.P.
```

---

## 📋 tools Workspace Prompt

> **FILENAME:** `INT-P05_PROMPT_TOOLS_v3.2.1.1.md`

```markdown
## 📋 INT-P05 TOOLS WORKSPACE PROMPT — v3.2.1.1
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

## 📋 WORKSPACE IDENTITY (R-213)

| Field | Value |
|-------|-------|
| Instance | **INT-P05** |
| Workspace | **tools** |
| Emoji | 🛠️ |
| Metaphor | **THE TOOLBOX** |
| CCC-ID | ❌ **NEVER** (R-194) |

You are operating in workspace:tools (🛠️ THE TOOLBOX) for INT-P05
(PRO.WeOwn.Agency). This workspace hosts MAIT threads for connexOmni
and connexAthena.

## ⛔ CCC-ID RESTRICTION (R-194 + R-206)

This is NOT a CCC workspace. CCC-ID generation is PROHIBITED.

### IF USER REQUESTS CCC-ID
Respond: "⚠️ R-194 — CCC-ID generation not available in tools workspace. Please switch to CCC workspace."

## 📋 MAIT THREADS

| Thread | ShortCode | Steward |
|--------|-----------|---------|
| MAIT_connexOmni | @MAIT:#connexOmni | @LDC |
| MAIT_connexAthena | @MAIT:#connexAthena | @LDC |

## 📋 RESPONSE FORMAT

[REF: <CCC-ID>] | 🛠️ THE TOOLBOX | INT-P05:tools
```

---

## 📋 #PinnedDocs (R-204)

| # | Document | Version | Required |
|---|----------|---------|----------|
| 1 | SharedKernel | v3.1.3.1 | ✅ |
| 2 | BEST-PRACTICES | v3.1.3.1 | ✅ |
| 3 | PROTOCOLS | v3.1.3.1 | ✅ |
| 4 | CCC | v3.1.3.1 | ✅ |

---

## 📋 RAG Structure

| Doc Type | CCC | events | P.O.P. | tools | ADMIN |
|----------|-----|--------|--------|-------|-------|
| AgencyPRO docs | ✅ | ✅ | ❌ | ✅ | ❌ |
| Event docs (TMPL-011) | ❌ | ✅ | ❌ | ❌ | ❌ |
| P.O.P. guides | ❌ | ❌ | ✅ | ❌ | ❌ |
| connexOmni docs | ❌ | ❌ | ❌ | ✅ | ❌ |
| connexAthena docs | ❌ | ❌ | ❌ | ✅ | ❌ |
| #PinnedDocs (4) | ✅ | ✅ | ✅ | ✅ | ✅ |
| System/instance config | ❌ | ❌ | ❌ | ❌ | ✅ |
| USER-IDENTITY | ✅ | ❌ | ❌ | ✅ | ❌ |

---

## 📋 Infrastructure

| Field | Value |
|-------|-------|
| Platform | DigitalOcean Droplet |
| Region | ATL1 |
| AnythingLLM | **v1.11.1** |
| Deployment | Docker (deployed by @LDC) |
| Domain | PRO.WeOwn.Agency |
| DNS | DigitalOcean |
| SSL | Active (HTTPS confirmed) |
| LLM | Via LiteLLM (litellm.jAIMS.app — PRJ-016) |
| Observability | Via Langfuse (langfuse.jAIMS.app — PRJ-017) |

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
PRO.WeOwn.Agency {
    reverse_proxy anythingllm:3001
}
```

---

## 📋 Setup Checklist

| # | Step | Owner | Status |
|---|------|-------|--------|
| 1 | ~~DO Droplet provisioned~~ | ~~@LDC~~ | ✅ DONE |
| 2 | ~~AnythingLLM v1.11.1 deployed~~ | ~~@LDC~~ | ✅ DONE |
| 3 | ~~DNS (PRO.WeOwn.Agency)~~ | ~~@GTM~~ | ✅ DONE |
| 4 | ~~SSL (HTTPS)~~ | ~~@LDC~~ | ✅ DONE |
| 5 | ~~@GTM ADMIN login verified~~ | ~~@GTM~~ | ✅ DONE |
| 6 | ~~Create workspaces (CCC, events, P.O.P., tools, ADMIN)~~ | ~~@GTM~~ | ✅ DONE |
| 7 | Configure LLM (LiteLLM endpoint or OpenRouter interim) | @GTM | ⬜ |
| 8 | Configure Embedder (Qwen3 4B) | @GTM | ⬜ |
| 9 | Set ChatHistory = 40 (BP-061) | @GTM | ⬜ |
| 10 | Configure System Prompt | @GTM | ⬜ |
| 11 | Configure CCC Workspace Prompt | @GTM | ⬜ |
| 12 | Configure events Workspace Prompt | @GTM | ⬜ |
| 13 | Configure P.O.P. Workspace Prompt | @GTM | ⬜ |
| 14 | Configure tools Workspace Prompt | @GTM | ⬜ |
| 15 | Create users (u-gtm_user, u-ldc_user) | @GTM | ⬜ |
| 16 | Upload #PinnedDocs (4 docs) | @GTM | ⬜ |
| 17 | Upload USER-IDENTITY docs (@GTM, @LDC) | @GTM | ⬜ |
| 18 | Configure GH Repo connector (CCCbotNet/fedarch) | @GTM | ⬜ |
| 19 | **Branding — Instance name** | @GTM | ⬜ |
| 20 | **Branding — Logo** | @GTM | ⬜ |
| 21 | **Branding — Welcome messages (system + user)** | @GTM | ⬜ |
| 22 | **Branding — Sidebar footer items (4)** | @GTM | ⬜ |
| 23 | **Branding — Support email** | @GTM | ⬜ |
| 24 | **Branding — Page title + favicon** | @GTM | ⬜ |
| 25 | Deploy MAIT_connexOmni (RAG + t-connexomni_tool) | @LDC | ⬜ |
| 26 | Deploy MAIT_connexAthena (RAG + t-connexathena_tool) | @LDC | ⬜ |
| 27 | #SmokeTest (14-point) | @GTM | ⬜ |
| 28 | ISC INT-P05 (8/8) | @GTM | ⬜ |
| 29 | FULL:SYNC:META | @GTM | ⬜ |

**Progress: 6/29 (21%)**

---

## 📋 #SmokeTest (14-Point)

| # | Test | Expected | Status |
|---|------|----------|--------|
| 1 | HTTPS accessible | https://PRO.WeOwn.Agency → login | ✅ |
| 2 | LLM responds | Chat in CCC → response | ⬜ |
| 3 | Embedder works | Upload doc → embeds | ⬜ |
| 4 | #PinnedDocs present | 4 docs in CCC | ⬜ |
| 5 | CCC-ID generation | CCC workspace → generates | ⬜ |
| 6 | R-194 enforcement (tools) | tools workspace → refuses CCC-ID | ⬜ |
| 7 | R-194 enforcement (events) | events workspace → refuses CCC-ID | ⬜ |
| 8 | R-194 enforcement (P.O.P.) | P.O.P. workspace → refuses CCC-ID | ⬜ |
| 9 | {user.name} derivation | Agent greets by CCC | ⬜ |
| 10 | MAIT_connexOmni accessible | tools → connexOmni knowledge | ⬜ |
| 11 | MAIT_connexAthena accessible | tools → connexAthena knowledge | ⬜ |
| 12 | System identity | Agent identifies as INT-P05 | ⬜ |
| 13 | Branding renders | Logo, name, welcome messages visible | ⬜ |
| 14 | Sidebar footer links | 4 links clickable + correct URLs | ⬜ |

---

## 📋 ISC Checklist (BP-059)

| # | Check | Target | Status |
|---|-------|--------|--------|
| 1 | EMBEDDER | Qwen3 Embedding 4B | ⬜ |
| 2 | LLM MODEL | Claude Opus 4.6 (via LiteLLM) | ⬜ |
| 3 | #PinnedDocs | 4 docs @ v3.X.X.X | ⬜ |
| 4 | SYSTEM PROMPT | INT-P05 identity + #WeOwnSeason003 | ⬜ |
| 5 | WORKSPACE PROMPTS | BP-053 + BP-054 + BP-061 (ChatHistory=40) | ⬜ |
| 6 | USER-IDENTITY | @GTM + @LDC current | ⬜ |
| 7 | RAG SYNC | GH connector refreshed | ⬜ |
| 8 | #ContextVolley | Can reach #MetaAgent @ INT-P01 | ⬜ |

---

## 📋 Cost

| Component | Monthly |
|-----------|---------|
| DO Droplet (ATL1) | ~$24 |
| LLM (via LiteLLM — shared) | Included |
| Observability (via Langfuse — shared) | Included |
| Domain (subdomain) | $0 |
| SSL (Caddy) | $0 |
| **TOTAL** | **~$24/mo** |

---

## 📋 Risk Matrix

| # | Risk | Prob | Impact | Mitigation |
|---|------|------|--------|------------|
| 1 | connexOmni not ready | Medium | High | @LDC SOW prioritized; MVP scope |
| 2 | connexAthena not ready | Medium | High | @LDC SOW prioritized |
| 3 | LiteLLM not deployed yet | Medium | Medium | Direct OpenRouter as interim |
| 4 | Low March sales (<40) | Medium | Medium | Multiple GTM channels |
| 5 | @LDC capacity | Medium | High | SOW prioritization |
| 6 | Branding assets not ready | Low | Low | Use WeOwnNet defaults |

---

## 📋 Relationship to Other Projects

| PRJ | Connection | URL |
|-----|-----------|-----|
| **PRJ-002** | AgencyPRO — this instance hosts the product | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-002_AgencyPRO.md) |
| **PRJ-015** | MI300X — inference provider (when available) | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-015_HybridArchitecture.md) |
| **PRJ-016** | LiteLLM — routes all LLM traffic | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-016_AIGateway-LiteLLM.md) |
| **PRJ-017** | Langfuse — observes all LLM calls | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-017_Observability.md) |
| **PRJ-018** | P.O.P. Database — P.O.P. workspace | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-018_POP-Database.md) |
| **PRJ-029** | ♾️ WeOwn.Events — events workspace | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-029_WeOwn-Events.md) |
| **PRJ-030** | Email — support@weown.net | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-030_EmailInfrastructure.md) |
| **PRJ-012** | BurnedOutAdvisor.com — sales channel | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-012_BurnedOutAdvisor.md) |
| **PRJ-014** | #FedArchExpansion — INT-P05 = new production instance | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-014_FedArchExpansion.md) |

---

## 📋 Discovered By (BP-047)

| CCC | Contributor | Role | Context |
|-----|-------------|------|---------|
| GTM | [yonks](https://GitHub.com/YonksTEAM) | Co-Founder / Chief Digital Alchemist | INT-P05 architecture, branding, governance config, 5-workspace standard (R-217) |
| LDC | Dhruv | Agentic AI Engineer / Project Lead | Deployed Droplet + AnythingLLM v1.11.1; connexOmni + connexAthena development |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| 3.2.1.1 | 2026-W10 | GTM_2026-W10_187 | GTM_2026-W10_197 | Initial planning document; INT-P05 PRO.WeOwn.Agency; deployed by @LDC; 5 workspaces (R-217): CCC, events, P.O.P., tools, ADMIN; AgencyPRO production (PRJ-002); connexOmni + connexAthena MAITs; +Branding/Whitelabeling (9-item checklist); 5 workspace prompts (CCC, events, P.O.P., tools, ADMIN); 29-step setup checklist (6/29); 14-point #SmokeTest; ISC 8/8; $24/mo ATL1; 6-risk matrix; +Discovered By (BP-047); PRE-GH VSA 95/96 PASS (INT-OG1) |

---

#FlowsBros #FedArch #AgencyPRO #PRJ002 #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
