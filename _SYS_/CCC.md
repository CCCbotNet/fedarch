# 📐 Contributor Code Convention (CCC) Standard

## CCC_v3.1.1.1.md
## ♾️ WeOwnNet 🌐 — Ecosystem Official Documentation

| Field | Value |
|-------|-------|
| Document | CCC.md |
| Version | 3.1.1.1 |
| CCC-ID | GTM_2026-W06_277 |
| Established | 2026-W02 |
| Updated | 2026-02-07 (W06) |
| Season | #WeOwnSeason003 🚀 |
| Status | 🔒 LOCKED |
| Source of Truth | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/CCC.md) |
| Repository | [github.com/CCCbotNet/fedarch](https://github.com/CCCbotNet/fedarch) |
| Domain | [CCCbot.Net](https://CCCbot.Net) *(coming soon)* |

---

## 📖 Table of Contents

1. [Overview](#-overview)
2. [Governance & Adoption](#-governance--adoption)
3. [CCC-ID Format Specification](#-ccc-id-format-specification)
4. [CCC-ID Rules](#-ccc-id-rules)
5. [Registered Contributor Codes](#-registered-contributor-codes)
6. [Agent Identity Format](#-agent-identity-format)
7. [Timestamp Format Standards](#-timestamp-format-standards)
8. [Priority Matrix](#-priority-matrix)
9. [Status Icons](#-status-icons)
10. [Category Emojis](#-category-emojis)
11. [CCC Template](#-ccc-template)
12. [Quick Reference Card](#-quick-reference-card)
13. [Contribution Workflow](#-contribution-workflow)
14. [Version History](#-version-history)

---

## 📖 Overview

The **Contributor Code Convention (CCC)** is the official standard for tracking, organizing, and attributing contributions across the ♾️ WeOwnNet 🌐 ecosystem. This convention ensures:

- **Consistent Attribution** — Every contribution is properly credited
- **Traceability** — All entries can be traced back to their source
- **Collaboration** — Team members can easily reference and build upon each other's work
- **Automation-Ready** — Structured format enables tooling and automation

### Design Principles

| Principle | Description |
|-----------|-------------|
| **Human-Readable** | Entry IDs should be immediately understandable |
| **Machine-Parseable** | Format supports automated processing |
| **Chronologically Sortable** | Entries sort correctly by date |
| **Uniquely Identifiable** | No two entries share the same ID |
| **Context-Rich** | Each entry carries meaningful metadata |

### AI Collaboration

CCC entries may be created in collaboration with AI assistants. The primary AI collaboration environment for ♾️ WeOwnNet 🌐 is:

| Resource | Value |
|----------|-------|
| **AI Instance** | [AI.WeOwn.Agency](https://AI.WeOwn.Agency) |
| **AI Username** | AI:team-lfg |
| **Platform** | AnythingLLM |

### Onchain Cooperative

The CCC standard will be governed by an onchain cooperative at [CCCbot.Net](https://CCCbot.Net).

| Resource | Value |
|----------|-------|
| **Domain** | [CCCbot.Net](https://CCCbot.Net) |
| **Registrar** | Porkbun.com (Web3FreedomClub) |
| **Purpose** | Onchain cooperative for CCC governance |
| **Status** | 🔄 In Development |

---

## 🏛️ Governance & Adoption

### Formal Adoption Process

The CCC standard will be formally adopted through on-chain governance to ensure transparent, community-driven decision making.

#### Governance Proposal

| Field | Value |
|-------|-------|
| **Platform** | [snapshot.box/#/s:cccbot.eth](https://snapshot.box/#/s:cccbot.eth) |
| **Proposer** | yonks (GTM) |
| **Proposal** | CCC v2.4.0 Adoption |
| **Status** | 📋 Pending |

#### Voting Eligibility

| Team | Participation |
|------|---------------|
| ♾️ WeOwnNet 🌐 Core TEAM | ✅ Eligible |
| ♾️ WeOwn.Dev 💻 TEAM | ✅ Eligible |

### AMA / Q&A Event

An **Ask Me Anything (AMA)** session will be hosted to discuss the CCC standard, answer questions, and gather feedback before the governance vote.

| Field | Value |
|-------|-------|
| **Event** | CCC v2.4.0 AMA / Q&A |
| **Hosts** | yonks (GTM) + CoachLFG (LFG) |
| **Audience** | ♾️ WeOwnNet 🌐 Community |
| **Purpose** | Discuss CCC, answer questions, gather feedback |
| **Status** | 📋 Scheduled (TBD) |

#### AMA Agenda (Proposed)

| # | Topic | Duration |
|---|-------|----------|
| 1 | Introduction to CCC | 10 min |
| 2 | Entry ID Format Walkthrough | 10 min |
| 3 | Contributor Codes & Attribution | 10 min |
| 4 | Standards Overview (timestamps, priorities, statuses) | 10 min |
| 5 | Live Q&A | 20 min |
| 6 | Next Steps & Governance Vote | 10 min |

### Adoption Timeline

| Phase | Activity | Status |
|-------|----------|--------|
| 1 | CCC v2.4.0 Published to GitHub | ✅ Complete |
| 2 | CCCbot.Net Domain Registered | ✅ Complete |
| 3 | Share with Core TEAM (Signal) | 📋 Pending |
| 4 | AMA / Q&A Event | 📋 Scheduled |
| 5 | Governance Proposal on snapshot.box | 📋 Pending |
| 6 | Voting Period | ⬜ TBD |
| 7 | Formal Adoption (if approved) | ⬜ TBD |
| 8 | CCCbot.Net Cooperative Launch | ⬜ TBD |

---

## 🆔 CCC-ID Format Specification

### Format Structure

```
<CCC>_<YYYY>-W<WW>_<NNN>
```

### Component Breakdown

| Component | Description | Format | Example |
|-----------|-------------|--------|---------|
| `<CCC>` | Contributor Code Convention identifier | 3 uppercase letters | `GTM` |
| `_` | Primary delimiter | Underscore | `_` |
| `<YYYY>` | 4-digit year | ISO 8601 | `2026` |
| `-` | Date separator | Hyphen | `-` |
| `W` | Week indicator | Literal "W" | `W` |
| `<WW>` | ISO week number | 01-53, zero-padded | `05` |
| `_` | Secondary delimiter | Underscore | `_` |
| `<NNN>` | Sequential number | 001-999, zero-padded | `796` |

### Complete Example

```
GTM_2026-W05_796
│   │    │   │
│   │    │   └── Sequential entry #796
│   │    └────── ISO Week 05
│   └─────────── Year 2026
└─────────────── Contributor: yonks (GTM)
```

### Validation Rules

| Rule | Requirement |
|------|-------------|
| CCC Length | Exactly 3 characters |
| CCC Characters | A-Z uppercase only |
| Year Range | 2024-2099 (current era) |
| Week Range | 01-53 (ISO 8601 compliant) |
| Sequence Range | 001-999 per contributor per week |
| Delimiters | Underscores and hyphens as specified |

### RegEx Pattern

```regex
^[A-Z]{3}_[0-9]{4}-W(0[1-9]|[1-4][0-9]|5[0-3])_[0-9]{3}$
```

---

## 📋 CCC-ID Rules

### Core Rules

| ID | Rule | Description |
|----|------|-------------|
| R-168 | CCC-ID sequence tied to CCC (contributor), NOT username/session | Each contributor maintains their own sequence |
| R-169 | CCC-ID resets to _001 ONLY at ISO week boundary | Sequence resets weekly |
| R-181 | CCC-ID _001 reserved for weekly summary | First entry = weekly summary |

### Workspace Rules

| ID | Rule | Description |
|----|------|-------------|
| R-194 | CCC-ID generation ONLY in CCC workspace — tools + ADMIN = NEVER | 🔒 IMMUTABLE |

### Weekly Summary Format

| Field | Value |
|-------|-------|
| Reserved CCC-ID | `<CCC>_<YYYY>-W<WW>_001` |
| Content | Milestones, rules, learnings, pending, stats |
| Example | GTM_2026-W05_001 = @GTM Week 5 Summary |

---

## 👥 Registered Contributor Codes

### 🏛️ Founding OG ♾️ WeOwn.Agency Owners

**Established:** 2026-W02 (GTM_2026-W02_015)

> *"Forever OG"* 🫡

| CCC | Contributor | Handle | Role | Status |
|-----|-------------|--------|------|--------|
| `GTM` | yonks | yonks.box｜🤖🏛️🪙｜Jason Younker ♾️ | Co-Founder / Chief Digital Alchemist | 🏛️ Founding OG |
| `THY` | mrsyonks | Tyler Younker (mrsyonks) | Co-Founder / CEO / CFO | 🏛️ Founding OG |
| `IAL` | IamLotus | IamLotus.eth | Co-Founder / Chief Catalyst Officer | 🏛️ Founding OG |
| `RMN` | Roman | Roman Di Domizio (@LLMfeed) | AI Platform Engineer | 🏛️ Founding OG |
| `LFG` | CoachLFG | Mike LeMaire (Coach) | Co-Host / Coach | 🏛️ Founding OG |

### Contributors (2026-W02+)

| CCC | Contributor | Handle | Role | Status | CCC Join Date |
|-----|-------------|--------|------|--------|---------------|
| `LDC` | Dhruv | — | Agentic AI Engineer / Project Lead | ✅ Active | 2026-W02 |
| `SHD` | Shahid | — | Sr. Full-Stack DevOps Engineer | ✅ Active | 2026-W02 |
| `JRW` | Webb | — | xCRO (fractional Chief Revenue Officer) | ✅ Active | 2026-W05 |

### System Codes

| CCC | Purpose | Description |
|-----|---------|-------------|
| `ORG` | Organization-wide | Shared entries not attributed to individuals |
| `SYS` | System | Automated or system-generated entries |
| `TMP` | Temporary | Draft or temporary entries pending assignment |

### Code Assignment Rules

1. **Uniqueness** — Each CCC must be unique across the organization
2. **Permanence** — Once assigned, a CCC is never reassigned to another contributor
3. **Individual Attribution** — Each CCC represents an individual contributor
4. **AI Collaboration** — Entries created with AI assistance are still attributed to the human contributor's CCC

### Requesting a New CCC

New contributor codes are assigned by:
1. Request via Core TEAM channel (Signal: ♾️ WeOwn.Agency 👥)
2. Approval by existing Founding OG member
3. Registration in this document
4. Announcement in community channels

---

## 🤖 Agent Identity Format

### Overview

Each contributor has a corresponding AI agent in the #FedArch network.

> **#MAITlivesInAthread** — MAIT = thread within workspace:tools, NOT a separate workspace

### Agent Naming Convention

| Format | Example | Description |
|--------|---------|-------------|
| `AI:@<CCC>` | AI:@GTM | User Agent for contributor |
| `AI:team-lfg` | AI:team-lfg | #MetaAgent (Orchestrator) |

### MAIT ShortCode (D-038)

| Field | Value |
|-------|-------|
| Definition | Unique identifier for MAIT thread |
| Format | `@MAIT:#<SME>` |
| Example | `@MAIT:#Deepnote` |
| Note | SME-centric identifier |

### Agent Identity Table

| CCC | Human | Agent | Example MAIT ShortCode |
|-----|-------|-------|------------------------|
| GTM | @GTM | AI:@GTM | @MAIT:#Deepnote (Steward: @GTM) |
| THY | @THY | AI:@THY | — |
| IAL | @IAL | AI:@IAL | — |
| RMN | @RMN | AI:@RMN | — |
| LFG | @LFG | AI:@LFG | — |

### Related Rules

| ID | Rule |
|----|------|
| R-171 | Agent identity format: AI:@<CCC> |
| D-038 | MAIT ShortCode: @MAIT:#<SME> |

---

## ⏰ Timestamp Format Standards

### Primary Format

| Scenario | Pattern | Example |
|----------|---------|---------|
| Time known | `Dd HH:MM TZ` | `Tu 17:58 EST` |
| Time unknown | `Fullday` | `Tuesday` |

### Day Abbreviations

| Day | Abbreviation | ISO Number |
|-----|--------------|------------|
| Monday | `Mo` | 1 |
| Tuesday | `Tu` | 2 |
| Wednesday | `We` | 3 |
| Thursday | `Th` | 4 |
| Friday | `Fr` | 5 |
| Saturday | `Sa` | 6 |
| Sunday | `Su` | 7 |

### Time Zone Reference

| Abbreviation | Full Name | UTC Offset |
|--------------|-----------|------------|
| `EST` | Eastern Standard Time | UTC-5 |
| `EDT` | Eastern Daylight Time | UTC-4 |
| `CST` | Central Standard Time | UTC-6 |
| `CDT` | Central Daylight Time | UTC-5 |
| `MST` | Mountain Standard Time | UTC-7 |
| `MDT` | Mountain Daylight Time | UTC-6 |
| `PST` | Pacific Standard Time | UTC-8 |
| `PDT` | Pacific Daylight Time | UTC-7 |
| `UTC` | Coordinated Universal Time | UTC±0 |

### Examples

```
Tu 17:58 EST    → Tuesday at 5:58 PM Eastern Standard Time
Mo 09:00 UTC    → Monday at 9:00 AM UTC
Friday          → Friday (time not specified)
We 23:45 PST    → Wednesday at 11:45 PM Pacific Standard Time
```

---

## 🎯 Priority Matrix

| Priority | Label | SLA | Emoji | Description |
|----------|-------|-----|-------|-------------|
| **P0** | Critical | Today | 🔴 | Blocking issues requiring immediate attention |
| **P1** | High | This Week | 🟠 | Important items for current sprint/week |
| **P2** | Medium | Next Week | 🟡 | Planned items for near-term completion |
| **P3** | Low | Backlog | 🟢 | Nice-to-have or future consideration |

### Priority Selection Guide

| Choose P0 When... | Choose P1 When... |
|-------------------|-------------------|
| Production is down | Feature deadline this week |
| Security vulnerability | Important client request |
| Data loss risk | Team blocked on this |
| Revenue impact | Sprint commitment |

| Choose P2 When... | Choose P3 When... |
|-------------------|-------------------|
| Planned improvement | Future enhancement |
| Non-urgent bug | Research/exploration |
| Documentation update | Nice-to-have feature |
| Scheduled maintenance | Technical debt |
## 📊 Status Icons

### Primary Status Set

| Icon | Status | Description |
|------|--------|-------------|
| ✅ | Complete | Work finished and verified |
| 🔄 | In Progress | Actively being worked on |
| 📋 | Pending | Queued, not yet started |
| ⏳ | Blocked | Cannot proceed due to dependency |
| ⬜ | TBD | To Be Determined |

### Extended Status Set

| Icon | Status | Description |
|------|--------|-------------|
| 🚀 | Launched | Deployed to production |
| 🧪 | Testing | In QA/testing phase |
| 👀 | Review | Awaiting review/approval |
| 🔙 | Reverted | Rolled back |
| ❌ | Cancelled | Will not be completed |
| 💤 | On Hold | Paused intentionally |
| 🔁 | Recurring | Repeating task |

### Status Transitions

```
📋 Pending → 🔄 In Progress → 👀 Review → ✅ Complete → 🚀 Launched
                    ↓
                  ⏳ Blocked
                    ↓
              (resolve blocker)
                    ↓
              🔄 In Progress
```

---

## 🏷️ Category Emojis

### Core Categories

| Emoji | Category | Use Case |
|-------|----------|----------|
| 🔧 | Tools Decision | Tool selection, integration decisions |
| 🚨 | Error Resolution | Bug fixes, incident response |
| 📖 | Documentation | Docs, guides, READMEs |
| 🏗️ | Architecture | System design, infrastructure |
| 🎪 | Event Planning | Meetings, launches, community events |
| 📐 | Standards | Conventions, processes, guidelines |

### Development Categories

| Emoji | Category | Use Case |
|-------|----------|----------|
| 🐛 | Bug Fix | Bug identification and resolution |
| ✨ | Enhancement | Feature improvements |
| ♻️ | Refactor | Code restructuring |
| 🧪 | Testing | Test creation, QA activities |
| 🔐 | Security | Security-related work |
| ⚡ | Performance | Optimization work |

### Operations Categories

| Emoji | Category | Use Case |
|-------|----------|----------|
| ⚙️ | Operations | DevOps, maintenance |
| 🔍 | Health Check | Monitoring, audits |
| 📦 | Product | Product management |
| 🚀 | Launch | Deployments, releases |
| 💰 | Finance | Budget, payments, revenue |

### Creative & Growth Categories

| Emoji | Category | Use Case |
|-------|----------|----------|
| 🎨 | Creative | Design, branding, content |
| 💡 | Ideation | Brainstorming, proposals |
| 📣 | Marketing | Campaigns, outreach |
| 🎓 | Learning | Training, education |
| 📊 | Analytics | Data analysis, metrics |

### Collaboration Categories

| Emoji | Category | Use Case |
|-------|----------|----------|
| 🤝 | Collaboration | Team activities, partnerships |
| 🏛️ | Milestone | Major achievements, milestones |

---

## 📝 CCC Template

### Standard CCC Format

```markdown
> **<CCC>_<YYYY>-W<WW>_<NNN>** | <EMOJI> <Category>: <Title>
>
> | Field | Value |
> |-------|-------|
> | **Timestamp** | <Dd HH:MM TZ or Fullday> |
> | **Status** | <STATUS_ICON> <STATUS_TEXT> |
> | **Category** | <EMOJI> <Category> |
> | **Priority** | <PRIORITY_EMOJI> <PRIORITY_LABEL> |
>
> ### Description
> <Brief description of the entry>
>
> ### Details
> <Extended details, context, or notes>
>
> ### Related Entries
> - <ENTRY_ID>: <Description>
```

### Minimal CCC Format

```markdown
> **<CCC>_<YYYY>-W<WW>_<NNN>** | <EMOJI> <Category>: <Title>
> **Status:** <STATUS_ICON> <STATUS_TEXT> | **Timestamp:** <Dd HH:MM TZ>
```

### Example CCC Entry

```markdown
> **GTM_2026-W05_796** | 📐 Standards: CCC v2.4.3 Update
>
> | Field | Value |
> |-------|-------|
> | **Timestamp** | Th 17:50 EST |
> | **Status** | ✅ Complete |
> | **Category** | 📐 Standards |
> | **Priority** | 🔴 P0 - Critical |
>
> ### Description
> Added new contributor JRW (Webb) + applied #ContextSwaps.
>
> ### Details
> - +JRW: xCRO (fractional Chief Revenue Officer)
> - #ContextSwap: ccc.bot → cccid.info
> - #ContextSwap: D-038 @MAIT:#<SME> format
>
> ### Related Entries
> - GTM_2026-W05_777: @JRW onboarding #masterCCC
> - GTM_2026-W05_789: BP-050 locked
```

---

## 📇 Quick Reference Card

### CCC-ID Format
```
<CCC>_<YYYY>-W<WW>_<NNN>
Example: GTM_2026-W05_796
```

### Founding OG CCCs
| `GTM` | `THY` | `IAL` | `RMN` | `LFG` |
|-------|-------|-------|-------|-------|
| yonks | mrsyonks | IamLotus | Roman | Coach |

### Day Codes
| Mo | Tu | We | Th | Fr | Sa | Su |
|----|----|----|----|----|----|----|

### Priorities
| 🔴 P0 | 🟠 P1 | 🟡 P2 | 🟢 P3 |
|-------|-------|-------|-------|
| Today | Week | Next | Backlog |

### Status Icons
| ✅ Done | 🔄 Progress | 📋 Pending | ⏳ Blocked | ⬜ TBD |
|---------|-------------|------------|------------|--------|

### Common Categories
| 🔧 Tools | 🚨 Error | 📖 Docs | 🏗️ Arch | 📐 Standards |
|----------|----------|---------|---------|--------------|
| 🐛 Bug | ✨ Feature | 🤝 Collab | 🚀 Launch | 🏛️ Milestone |

---

## 🔄 Contribution Workflow

### Step 1: Create Entry ID

1. Identify your CCC (e.g., `GTM`, `THY`, `IAL`)
2. Note current ISO week (e.g., `2026-W06`)
3. Get next sequential number for your CCC this week
4. Assemble: `GTM_2026-W06_341`

### Step 2: Select Metadata

1. Choose appropriate **Category** emoji
2. Set **Priority** level
3. Initialize **Status** (usually `📋 Pending` or `🔄 In Progress`)
4. Add **Timestamp**

### Step 3: Document Entry

1. Use the Entry Template
2. Write clear **Title** and **Description**
3. Link **Related Entries** if applicable
4. Add relevant details

### Step 4: Track Progress

1. Update **Status** as work progresses
2. Add notes for significant updates
3. Mark ✅ **Complete** when finished
4. Archive or reference as needed

### AI-Assisted Contributions

When creating entries with AI assistance:
1. Use your personal CCC (not a system code)
2. Reference the AI collaboration in the entry details
3. Include thread link when applicable

Example:
```markdown
### Details
- AI collaboration via AI:team-lfg at AI.WeOwn.Agency
- Thread: https://ai.weown.agency/workspace/tools/t/[thread-id]
```

---

## 📜 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| 3.1.1.1 | 2026-W06 | GTM_2026-W06_277 | GTM_2026-W06_346 | #WeOwnSeason003 season alignment — version bump v2.4.3 → v3.1.1.1 (L-094); +Source of Truth URL (CCCbotNet/fedarch); +Season tag; Repository → CCCbotNet/fedarch; Document ID → CCC.md; #ContextSwap cccid.info → CCCbot.Net (×6); #ContextSwap snapshot.box → cccbot.eth (×2); -Adoption Signatures section; NO content changes; FULL PRESERVE (L-097) |
| 2.4.3 | 2026-W05 | GTM_2026-W05_793 | GTM_2026-W05_795 | +JRW (Webb) — xCRO; #ContextSwap: ccc.bot → cccid.info; #ContextSwap: D-038 @MAIT:#<SME> format |
| 2.4.2 | 2026-W05 | GTM_2026-W05_270 | — | +CCC-ID Rules section; +Agent Identity Format section; +Contributors (LDC, SHD); TOC → 15 items; fixes applied |
| 2.4.1 | 2026-W05 | GTM_2026-W05_262 | — | #ContextSwap: ILO → IAL; roles aligned with SharedKernel_v2.4.7 |
| 2.4.0 | 2026-W02 | GTM_2026-W02_017 | — | Initial public release; Governance & AMA process; ccc.bot domain; ♾️ WeOwnNet 🌐 branding |

---

## 🔗 Links

| Resource | URL |
|----------|-----|
| **♾️ WeOwnNet 🌐** | [weown.net](https://weown.net) |
| **CCC Cooperative** | [CCCbot.Net](https://CCCbot.Net) *(coming soon)* |
| **AI Instance** | [AI.WeOwn.Agency](https://AI.WeOwn.Agency) |
| **GitHub Org** | [github.com/CCCbotNet](https://github.com/CCCbotNet) |
| **#FedArch Repository** | [github.com/CCCbotNet/fedarch](https://github.com/CCCbotNet/fedarch) |
| **Governance** | [snapshot.box/#/s:cccbot.eth](https://snapshot.box/#/s:cccbot.eth) |

---

<div align="center">

**Document ID:** `CCC.md`
**Maintained By:** Core TEAM
**Repository:** [github.com/CCCbotNet/fedarch](https://github.com/CCCbotNet/fedarch)
**Cooperative:** [CCCbot.Net](https://CCCbot.Net)

---

*♾️ WeOwnNet 🌐 | 🏡 Real Estate and 🤝 cooperative ownership for everyone. An 🤗 inclusive community, by 👥 invitation only.*
