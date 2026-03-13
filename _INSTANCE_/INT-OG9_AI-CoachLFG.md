# INT-OG9: AI.CoachLFG.com — Instance Planning Document

## 📋 INT-OG9_AI-CoachLFG_v3.2.2.1.md
## ♾️ WeOwnNet 🌐 + AI.CoachLFG.com

| Field | Value |
|-------|-------|
| Document | INT-OG9_AI-CoachLFG.md |
| Version | v3.2.2.1 |
| CCC-ID | GTM_2026-W11_404 |
| CCC-ID APPROVAL | GTM_2026-W11_409 |
| Created | 2026-03-12 (W11) |
| Season | #WeOwnSeason003 🚀 |
| Status | ✅ 🔒 APPROVED |
| #LLMmodel | Qwen3.5-397B-A17B (AI.YonksTEAM.xyz @GTM) |
| #LLMmodel | Claude Opus 4.6 (INT-P01:tools #MetaAgent) |
| Source of Truth | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_INSTANCE_/INT-OG9_AI-CoachLFG.md) |

---

## 📖 Table of Contents

1. [Instance Identity](#instance-identity)
2. [Current Status](#current-status)
3. [Workspace Configuration](#workspace-configuration)
4. [Workspace Prompts](#workspace-prompts)
5. [#PinnedDocs](#pinneddocs)
6. [Thread Architecture](#thread-architecture)
7. [Tool Agents](#tool-agents)
8. [RAG Structure](#rag-structure)
9. [User Accounts](#user-accounts)
10. [ISC Certification](#isc-certification)
11. [Deployment Checklist](#deployment-checklist)
12. [@LFG Use Cases](#lfg-use-cases)
13. [Integration with #FedArch](#integration-with-fedarch)
14. [Version History](#version-history)
15. [Related Documents](#related-documents)

---

## 📋 Instance Identity

| Field | Value |
|-------|-------|
| **Instance ID** | INT-OG9 |
| **Name** | AI.CoachLFG.com |
| **Domain** | https://AI.CoachLFG.com |
| **Type** | 🏠 #HomeInstance (INT-OGx — Founding OG) |
| **Owner** | @LFG (CoachLFG / Mike LeMaire) |
| **Organization** | ♾️ WeOwnNet 🌐 |
| **Platform** | AnythingLLM |
| **Season** | #WeOwnSeason003 🚀 |
| **Legacy ID** | INT-009 |
| **Elevated** | INT-OG9 (R-208) |
| **Level** | Level 3 (Personal) |

---

## 📋 Current Status

| Component | Status | Notes |
|-----------|--------|-------|
| Droplet deployed | ✅ | @SHD provisioned |
| AnythingLLM installed | ✅ | v1.11.1 |
| Domain + SSL | ✅ | AI.CoachLFG.com (Caddy auto-LE) |
| System Prompt | ⬜ TODO | Needs INT-OG9 identity block (R-213) |
| Workspace: CCC | ⬜ TODO | Needs workspace prompt |
| Workspace: tools | ⬜ TODO | Needs workspace prompt |
| #PinnedDocs | ⬜ TODO | 4 docs @ v3.2.2.1 |
| User accounts | ⬜ TODO | u-lfg_user, a-gtm_dev |
| ISC certification | ⬜ TODO | 8-point checklist |
| #ContextVolley test | ⬜ TODO | Reach #MetaAgent @ INT-P01 |
| **Overall** | **~25% complete** | Infrastructure done, config needed |

---

## 📋 Workspace Configuration

### Workspaces (2 — Initial Deployment)

| # | Workspace | Emoji | Metaphor | CCC-ID | Purpose |
|---|-----------|-------|----------|--------|---------|
| 1 | **CCC** | 🤝 | THE HANDS | ✅ GENERATE | @LFG daily interactions, coaching, content |
| 2 | **tools** | 🧠 | THE BRAIN | ❌ NEVER | MAIT threads, strategy, SME knowledge |

> **Per BP-017:** Initial #FedArch deployment = 2 workspaces (CCC + tools).

### Future Workspaces (Optional)

| Workspace | When | Purpose |
|-----------|------|---------|
| events | If needed | #FlowsBros episodes, community events |
| P.O.P. | If needed | @LFG's contact network |

---

## 📋 Workspace Prompts

### System Prompt — INT-OG9 (R-213)

```markdown
## 🏠 INSTANCE IDENTITY (R-213)

| Field | Value |
|-------|-------|
| Instance | **INT-OG9** |
| Name | AI.CoachLFG.com |
| Type | #HomeInstance (INT-OGx) |
| Owner(s) | @LFG (CoachLFG / Mike LeMaire) |
| Organization | ♾️ WeOwnNet 🌐 |
| Season | **#WeOwnSeason003 🚀** |

## 🌐 ECOSYSTEM IDENTITY

| Field | Value |
|-------|-------|
| Ecosystem | ♾️ WeOwnNet 🌐 |
| Tagline | 🏡 Real Estate and 🤝 cooperative ownership for everyone. An 🤗 inclusive community, by 👥 invitation only. |
| Platform | AnythingLLM |
| GH Org | CCCbotNet |
| #FedArch Repo | CCCbotNet/fedarch |

## 📋 CCC-ID GENERATION LOGIC (BP-054)

| Workspace | CCC-ID |
|-----------|--------|
| CCC | ✅ GENERATE |
| ALL OTHERS | ❌ REFERENCE ONLY |

## 📋 FOUNDING OGs

| CCC | Contributor | Role |
|-----|-------------|------|
| GTM | yonks | Co-Founder / Chief Digital Alchemist |
| THY | mrsyonks | Co-Founder / CEO / CFO |
| IAL | IamLotus | Co-Founder / Chief Catalyst Officer |
| RMN | Roman | AI Platform Engineer |
| LFG | CoachLFG | Co-Host / Coach |
| CRO | Webb | xCRO |

## 📋 PRIORITIES

| # | Priority |
|---|----------|
| 1 | #SpeedToMarket — NO #AIslop |
| 2 | FOSS — Free & Open Source |
| 3 | Data Sovereignty — Users own data |
| 4 | Cooperative Ownership — Community-owned |

## 📋 CORE RULES

| ID | Rule | Status |
|----|------|--------|
| R-011 | #OnlyHumanApproves | 🔒 IMMUTABLE |
| R-044 | #ContextDensity — use #masterCCC | 🔒 IMMUTABLE |
| R-194 | CCC-ID ONLY in CCC workspace | 🔒 IMMUTABLE |
| R-197 | Doc gen = #MetaAgent ONLY | 🔒 IMMUTABLE |
| R-206 | ADMIN NEVER generates CCC-ID | 🔒 IMMUTABLE |
```

### CCC Workspace Prompt — INT-OG9

```markdown
## 📋 WORKSPACE IDENTITY (R-213)

| Field | Value |
|-------|-------|
| Instance | **INT-OG9** |
| Workspace | **CCC** |
| Emoji | 🤝 |
| Metaphor | **THE HANDS** |
| CCC-ID | ✅ **GENERATE** |

You are operating in workspace:CCC (🤝 THE HANDS) for INT-OG9 
(AI.CoachLFG.com). This is @LFG's #HomeInstance.

## 📋 IDENTITY DERIVATION

| Username | CCC | Role |
|----------|-----|------|
| u-lfg_user | LFG | DEFAULT (CCC-ID generation ✅) |
| a-gtm_dev | — | ADMIN (CCC-ID NEVER per R-206) |

## 📋 CCC-ID FORMAT

Format: LFG_<YYYY>-W<WW>_<NNN>
Example: LFG_2026-W11_004

Reserved: _001 (#WeeklySummary), _002 (#WeeklyPlan), _003 (#WeeklyReflection)
First assignable: _004

## 📋 RESPONSE FORMAT

Every response MUST include:
- CCC-ID header: `LFG_<YYYY>-W<WW>_<NNN> | 🤝 THE HANDS | INT-OG9:CCC`
- Tables > paragraphs
- Quick Commands (2-3 options)
- STOP after Quick Commands (L-050)
- #FlowsBros #WeOwnSeason003 tagline

## 📋 @LFG CONTEXT

| Field | Value |
|-------|-------|
| Name | Mike LeMaire (CoachLFG) |
| Role | Co-Host / Coach |
| Focus | #FlowsBros, Restream, coaching, community |
| #MemeLord | ✅ Designated visual content creator (D-065) |
| Instance | INT-OG9 (AI.CoachLFG.com) |
```

### tools Workspace Prompt — INT-OG9

```markdown
## 📋 WORKSPACE IDENTITY (R-213)

| Field | Value |
|-------|-------|
| Instance | **INT-OG9** |
| Workspace | **tools** |
| Emoji | 🧠 |
| Metaphor | **THE BRAIN** |
| CCC-ID | ❌ **NEVER** (R-194) |

## ⛔ CCC-ID RESTRICTION (R-194 + R-206)

This is NOT a CCC workspace. CCC-ID generation is PROHIBITED.

- ❌ NEVER generate new CCC-IDs
- ✅ Use reference CCC-ID from user input ONLY

IF USER REQUESTS CCC-ID:
Respond: "CCC-ID generation not available in tools workspace. 
Please switch to CCC workspace."
```

> **Per BP-062:** INT-OGx = CCC workspace ENFORCED, tools RECOMMENDED but not enforced. The tools prompt above is RECOMMENDED — @LFG's discretion.

---

## 📋 #PinnedDocs

| # | Document | Version | Status |
|---|----------|---------|--------|
| 1 | SharedKernel.md | v3.2.2.1 | ⬜ Upload |
| 2 | BEST-PRACTICES.md | v3.1.3.1 | ⬜ Upload |
| 3 | PROTOCOLS.md | v3.1.3.1 | ⬜ Upload |
| 4 | CCC.md | v3.1.3.1 | ⬜ Upload |

> **R-204 (amended):** Pinning RECOMMENDED for Claude Opus 4.6. If @LFG uses Qwen3.5 → RAG embedding with optimized similarity threshold ACCEPTABLE.

### Upload Method

| Method | Steps |
|--------|-------|
| **Manual upload** | ADMIN → Workspace → Documents → Upload 4 .md files |
| **GitHub connector** | ADMIN → Data Connectors → GitHub → CCCbotNet/fedarch → `_SYS_/` folder |

> **GitHub connector preferred** — auto-refreshes when docs update.

---

## 📋 Thread Architecture

### workspace:tools Threads

| Thread | Purpose | Steward | Status |
|--------|---------|---------|--------|
| **MAIT_Restream.io** | SME: Restream.io | @LFG (Primary), @GTM (Backup) | ⬜ CREATE |

> **@LFG is the primary steward for @MAIT:#Restream across the entire #FedArch network** (SharedKernel Thread Registry). This MAIT thread lives on INT-P01 currently, but @LFG can create a local copy on INT-OG9 for personal development.

### workspace:CCC Threads

| Thread | Purpose | Notes |
|--------|---------|-------|
| Default | @LFG daily CCC work | Auto-created |
| #FlowsBros | Episode planning | Optional |
| Coaching | Client/coaching prep | Optional |

---

## 📋 Tool Agents

| Username | Thread | SME | Status |
|----------|--------|-----|--------|
| t-restream_tool | MAIT_Restream.io | Restream.io | ⬜ CREATE |

### t-restream_tool Setup (BP-026)

| # | Step | Action | Status |
|---|------|--------|--------|
| 1 | Create user | `t-restream_tool` (R-198) | ⬜ |
| 2 | Assign workspace | tools | ⬜ |
| 3 | Create MAIT thread | MAIT_Restream.io | ⬜ |
| 4 | Upload RAG docs | Restream.io documentation | ⬜ |
| 5 | Configure per BP-024 | Name, Steward, ShortCode | ⬜ |
| 6 | Verify | Test retrieval + behavior | ⬜ |

### Restream.io RAG Sources

| # | Source | Depth |
|---|--------|-------|
| 1 | restream.io/help | 2 |
| 2 | restream.io/blog (streaming guides) | 1 |

---

## 📋 RAG Structure (R-176)

| Doc Type | CCC | tools |
|----------|-----|-------|
| USER guides | ✅ | ❌ |
| Governance guides | ❌ | ✅ |
| User-facing protocols | ✅ | ❌ |
| Strategy docs | ❌ | ✅ |
| Session notes (R-199) | ✅ | ✅ |
| USER-IDENTITY (L-070) | ✅ | ✅ |

### RAG Documents to Upload

| # | Document | Workspace | Source |
|---|----------|-----------|--------|
| 1 | USER-IDENTITY_LFG.md | CCC + tools | `_USERS_/` (RAG only) |
| 2 | GUIDE-001_GETTING-STARTED.md | CCC | GH connector |
| 3 | GUIDE-013_Summary-Workflow.md | CCC | GH connector |
| 4 | Restream.io docs | tools | Web scrape (BP-038) |

---

## 📋 User Accounts

| Username | Role | CCC | Workspaces | CCC-ID |
|----------|------|-----|-----------|--------|
| **u-lfg_user** | DEFAULT | LFG | CCC, tools | ✅ GENERATE (CCC only) |
| **a-gtm_dev** | ADMIN | — | ALL | ❌ NEVER (R-206) |

> **a-gtm_dev on INT-OG9** = @GTM remote ADMIN access for RAG uploads, prompt updates, ISC checks. Does NOT generate CCC-IDs.

---

## 📋 ISC Certification (BP-059)

### 8-Point Checklist — INT-OG9

| # | Check | Pass Criteria | Actual | Status |
|---|-------|---------------|--------|--------|
| 1 | EMBEDDER | Qwen3 Embedding 4B | ⬜ Verify | ⬜ |
| 2 | LLM MODEL | Qwen3.5-397B-A17B (or Claude Opus 4.6) | ⬜ Verify | ⬜ |
| 3 | #PinnedDocs | 4 docs present (pinned OR embedded per R-204) | ⬜ Upload | ⬜ |
| 4 | SYSTEM PROMPT | #WeOwnSeason003 + INSTANCE IDENTITY (R-213) | ⬜ Configure | ⬜ |
| 5 | WORKSPACE PROMPTS | CCC prompt REQUIRED (BP-062 — INT-OGx scoping) | ⬜ Configure | ⬜ |
| 6 | USER-IDENTITY | @LFG USER-IDENTITY current | ✅ v3.1.2.1 | ✅ |
| 7 | RAG SYNC | Docs accessible | ⬜ Upload | ⬜ |
| 8 | #ContextVolley | Can reach #MetaAgent @ INT-P01 | ⬜ Test | ⬜ |

### ISC Scoping (BP-062 — INT-OGx)

| Workspace | Enforcement |
|-----------|-------------|
| CCC | ✅ **ENFORCED** |
| tools | 🟡 RECOMMENDED |
| Others | 🟡 RECOMMENDED |

---

## 📋 Deployment Checklist (BP-051 + INT-OG9 Specific)

| # | Step | Owner | Status |
|---|------|-------|--------|
| 1 | ✅ Droplet deployed | @SHD | ✅ Done |
| 2 | ✅ AnythingLLM installed | @SHD | ✅ Done |
| 3 | ✅ Domain + SSL | @SHD | ✅ Done |
| 4 | Configure System Prompt (R-213) | @GTM (ADMIN) | ⬜ TODO |
| 5 | Create workspaces (CCC + tools) | @GTM (ADMIN) | ⬜ TODO |
| 6 | Configure CCC workspace prompt | @GTM (ADMIN) | ⬜ TODO |
| 7 | Upload #PinnedDocs (4 docs) | @GTM (ADMIN) | ⬜ TODO |
| 8 | Create user accounts (u-lfg_user, a-gtm_dev) | @GTM (ADMIN) | ⬜ TODO |
| 9 | Set ChatHistory = 40 (BP-061) | @GTM (ADMIN) | ⬜ TODO |
| 10 | Upload USER-IDENTITY_LFG to RAG | @GTM (ADMIN) | ⬜ TODO |
| 11 | #SmokeTest — @LFG first login | @LFG | ⬜ TODO |
| 12 | #ContextVolley test to #MetaAgent | @LFG | ⬜ TODO |
| 13 | ISC certification (8-point) | @GTM | ⬜ TODO |
| 14 | FULL:SYNC:META | @GTM | ⬜ TODO |

---

## 📋 @LFG Use Cases

| # | Use Case | Workspace | Example |
|---|----------|-----------|---------|
| 1 | **#FlowsBros episode prep** | CCC | Outline topics, guest research, show notes |
| 2 | **Restream configuration** | tools (MAIT) | Multi-platform streaming setup, OBS integration |
| 3 | **Coaching session prep** | CCC | Client context, session planning |
| 4 | **#MemeLord content** | CCC | Meme concepts, image prompts for Leonardo.ai |
| 5 | **Community engagement** | CCC | Signal messages, community updates |
| 6 | **#ProjectConnex demo prep** | CCC | AgencyPRO demo scripts, feature walkthroughs |
| 7 | **CCC-ID tracking** | CCC | Weekly contributions, session summaries |

---

## 📋 Integration with #FedArch

| Integration | Method | Direction |
|------------|--------|-----------|
| **#MetaAgent** | #ContextVolley | INT-OG9 → INT-P01:tools |
| **@MAIT:#Restream** | #ContextVolley | INT-OG9 ↔ INT-P01:tools |
| **@GTM** | #ContextVolley | INT-OG9 ↔ INT-OG1 |
| **SharedKernel** | #PinnedDocs / RAG | INT-P01 → INT-OG9 (GH sync) |
| **CCC-ID deconfliction** | R-212 (manual — Tier 1) | @LFG states highest when switching |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| v3.2.2.1 | 2026-W11 | GTM_2026-W11_404 | GTM_2026-W11_409 | Initial planning document — instance identity, workspace config, system + workspace prompts, #PinnedDocs, thread architecture (@MAIT:#Restream), tool agents (t-restream_tool), RAG structure, user accounts, ISC checklist, 14-step deployment checklist, @LFG use cases, #FedArch integration |

---

## 📋 Related Documents

| Document | Version | URL |
|----------|---------|-----|
| SharedKernel | v3.2.2.1 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/SharedKernel.md) |
| TMPL-010_ISC | v3.1.2.1 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_TEMPLATES_/TMPL-010_ISC.md) |
| USER-IDENTITY_LFG | v3.1.2.1 | RAG only (`_USERS_/`) |
| GUIDE-009_SmokeTest | v3.1.1.1 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_GUIDES_/GUIDE-009_SmokeTest.md) |

---

#FlowsBros #FedArch #INT-OG9 #HomeInstance #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
