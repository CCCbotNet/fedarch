# BEST-PRACTICES.md

## 📋 BEST-PRACTICES_v3.1.3.1.md
## ♾️ WeOwnNet 🌐 — #BestPractices

| Field | Value |
|-------|-------|
| Document | BEST-PRACTICES.md |
| Version | 3.1.3.1 |
| CCC-ID | GTM_2026-W08_069 |
| Updated | 2026-02-21 (W08) |
| Season | #WeOwnSeason003 🚀 |
| Status | 🔒 LOCKED |
| Source of Truth | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/BEST-PRACTICES.md) |

---

## 📖 Table of Contents

1. [Overview](#-overview)
2. [Best Practices Index](#-best-practices-index)
3. [Core Best Practices (Immutable)](#-core-best-practices-immutable)
4. [Communication Best Practices](#-communication-best-practices)
5. [Workspace Configuration](#-workspace-configuration)
6. [Document Management](#-document-management)
7. [Document Generation](#-document-generation)
8. [Document Reference Standard](#-document-reference-standard)
9. [Weekly Operations](#-weekly-operations)
10. [RAG Structure](#-rag-structure-r-176)
11. [Agent Interaction](#-agent-interaction)
12. [Platform Best Practices (#AnythingLLM)](#-platform-best-practices-anythingllm)
13. [Documentation Best Practices](#-documentation-best-practices)
14. [Agent Best Practices](#-agent-best-practices)
15. [Tool Agent Best Practices](#-tool-agent-best-practices)
16. [Notes-to-RAG Best Practices](#-notes-to-rag-best-practices)
17. [MAIT Response Best Practices](#-mait-response-best-practices)
18. [Case Study Best Practices](#-case-study-best-practices)
19. [Onboarding Best Practices](#-onboarding-best-practices)
20. [#HomeInstance Best Practices](#-homeinstance-best-practices)
21. [System Prompt Best Practices](#-system-prompt-best-practices)
22. [CCC Workspace ACK Best Practices](#-ccc-workspace-ack-best-practices)
23. [USER-IDENTITY Season Refresh Best Practices](#-user-identity-season-refresh-best-practices)
24. [Season Certification Best Practices](#-season-certification-best-practices)
25. [CCC-ID Deconfliction Best Practices](#-ccc-id-deconfliction-best-practices)
26. [#WorkspaceChatHistory Best Practices](#-workspacechathistory-best-practices)
27. [INT-OGx ISC Scoping Best Practices](#-int-ogx-isc-scoping-best-practices)
28. [#DocLifecycle Best Practices](#-doclifecycle-best-practices)
29. [API Key Rotation Best Practices](#-api-key-rotation-best-practices)
30. [Shared Instance Identity Best Practices](#-shared-instance-identity-best-practices)
31. [Version History](#-version-history)
32. [Related Documents](#-related-documents)

---

## 📋 Overview

This document contains best practices for all contributors and agents in the ♾️ WeOwnNet 🌐 ecosystem.

| Field | Value |
|-------|-------|
| Steward(s) | @GTM (yonks.box｜🤖🏛️🪙｜Jason Younker ♾️ [GH](https://GitHub.com/YonksTEAM)) + @RMN (Roman Di Domizio) |
| Source of Truth | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/BEST-PRACTICES.md) |

---

## 📋 BEST PRACTICES INDEX

| Range | Category | Count |
|-------|----------|-------|
| BP-001 → BP-007 | Communication | 8 |
| BP-008 → BP-009 | Platform (#AnythingLLM) | 2 |
| BP-010 → BP-014 | Documentation | 5 |
| BP-015 → BP-016 | Agent | 2 |
| BP-017 → BP-018 | Workspace Configuration | 2 |
| BP-019 | Core (Immutable) | 1 |
| BP-020 → BP-024 | Documentation (Enhanced) | 5 |
| BP-025 → BP-026 | Instance & Tool Setup | 2 |
| BP-027 → BP-035 | Notes-to-RAG | 9 |
| BP-038 → BP-041 | Additional | 4 |
| BP-043 → BP-044 | MAIT + #PinnedDocs | 2 |
| BP-045 | Document Reference Standard | 1 |
| BP-047 | Case Study Attribution | 1 |
| BP-049 | VSA / #threadHEADER | 1 |
| BP-050 | Onboarding Workflow | 1 |
| BP-051 | #HomeInstance Setup | 1 |
| BP-052 → BP-053 | Weekly Ops + Workspace Prompts | 2 |
| BP-054 | System Prompt CCC-ID Logic | 1 |
| BP-055 | Pinata.cloud Architecture | 1 |
| BP-056 | CCC Workspace ACK Header | 1 |
| BP-057 → BP-058 | USER-IDENTITY Season Refresh | 2 |
| BP-059 | Season Certification (ISC) | 1 |
| BP-060 | CCC-ID Deconfliction | 1 |
| BP-061 | #WorkspaceChatHistory | 1 |
| BP-062 | INT-OGx ISC Scoping | 1 |
| BP-063 | #DocLifecycle VSA Gate | 1 |
| BP-064 | API Key Rotation | 1 |
| BP-065 | Shared Instance Self-ID | 1 |
| **TOTAL** | | **59** |

### Retired Best Practices

| ID | Description | Reason | Date |
|----|-------------|--------|------|
| BP-046 | Related Documents format | Merged into BP-045 | 2026-W05 |

---

## 📋 CORE BEST PRACTICES (IMMUTABLE)

| ID | Best Practice | Status |
|----|---------------|--------|
| BP-019 | ALWAYS SEEK:META for ALL documents | 🔒 IMMUTABLE |
| BP-023 | CCC-ID generation ONLY in CCC workspace — tools + ADMIN = NEVER | 🔒 IMMUTABLE |

---

## 📋 COMMUNICATION BEST PRACTICES

| ID | Best Practice | Source |
|----|---------------|--------|
| BP-001 | Use #ContextVolley for cross-agent communication (one-to-one) | — |
| BP-002 | Include CCC-ID in all communications | — |
| BP-003 | Use tables over paragraphs (#LessIsMore) | — |
| BP-004 | Always provide Quick Commands (2-3 options) | — |
| BP-005 | End responses with #feedback section when appropriate | — |
| BP-006 | Narrate actions during DEMO | GTM_2026-W03_539 |
| BP-007 | Clean slate = fresh context for unbiased view | GTM_2026-W03_545 |
| BP-041 | #ContextBroadcast for one-to-many agent communications — use 📢 emoji, TO: ALL AGENTS | GTM_2026-W05_500 |

---

## 📋 WORKSPACE CONFIGURATION

### BP-017: Workspace Prompt Per Workspace

| Workspace | Prompt Focus |
|-----------|--------------|
| CCC | User interaction, CCC-ID generation |
| tools | Strategy, SME, meta-cognition, META + MAIT threads |
| ADMIN | Administration functions, doc management |

**Best Practice:** Each workspace MUST have dedicated workspace prompt aligned with its metaphor.

### BP-018: System Prompt Per Instance

| Instance | System Prompt |
|----------|---------------|
| INT-P01 | AI.WeOwn.Agency identity |
| INT-P02 | #ProjectConnex identity |
| INT-OG1 | @GTM + @THY #HomeInstance identity |
| INT-OG8 | @RMN #HomeInstance identity |
| INT-XXX | Instance-specific identity |

**Best Practice:** Each #AnythingLLM instance MUST have unique system prompt defining its identity.

### Initial Deployment

| # | Workspace | Purpose |
|---|-----------|---------|
| 1 | tools | 🧠 THE BRAIN — META + MAIT threads |
| 2 | CCC | 🤝 THE HANDS — Production (users) |

**Best Practice:** Initial #FedArch deployment = 2 workspaces (tools + CCC).

### BP-052: #WeeklyFlows ISO Rollover

| ID | Best Practice | Approval |
|----|---------------|----------|
| BP-052 | #WeeklyFlows ISO Rollover: At Monday 00:00 boundary, AI MUST prompt "Ready to start W<XX> CCC-IDs?" — NEVER auto-rollover during active session; exception: >4h inactivity after Monday 00:00 = auto-rollover OK | GTX_2026-W05_037 |

### BP-053: Non-CCC Workspace Prompts

| ID | Best Practice | Approval |
|----|---------------|----------|
| BP-053 | ALL non-CCC workspace prompts MUST include CCC-ID restriction block — applies to: tools, ADMIN, events, P.O.P., and ANY future workspaces; prevents R-194 violations at prompt level | GTX_2026-W05_079 |

---

## 📋 DOCUMENT MANAGEMENT

### Pinning (R-177 + L-070)

| Doc Type | Pin? | Rationale |
|----------|------|-----------|
| Core protocols | ✅ YES | Every interaction |
| Rules (SHARED-KERNEL) | ✅ YES | Governance |
| Best practices | ✅ YES | Interaction patterns |
| CCC | ✅ YES | Attribution format |
| Agent identity docs | ❌ NO | System Prompt covers (L-070) |
| Reference guides | ❌ NO | RAG sufficient |
| Strategy docs | ❌ NO | RAG sufficient |
| USER-IDENTITY | ❌ NO | RAG in `_USERS_/` (L-070) |
| ECOSYSTEM-IDENTITY | ❌ NO | System Prompt covers (L-070) |

**Best Practice:** PIN only 4 docs: SharedKernel, BEST-PRACTICES, PROTOCOLS, CCC. Let RAG handle everything else.

### Versioning (R-178)

| Format | Example |
|--------|---------|
| `<NAME>_v<VERSION>.md` | SHARED-KERNEL_v3.1.1.3.md |

**Best Practice:** ALL RAG docs MUST include version in filename for visibility.

### Update Cadence (R-179)

| Trigger | Action |
|---------|--------|
| ISO week boundary + 10+ rules | MUST update |
| Major milestone | MUST update |
| Breaking change | IMMEDIATE update |

**Best Practice:** Review #SharedKernel docs at each ISO week boundary.

---

## 📋 DOCUMENT GENERATION

### R-180: #MetaAgent Generation

| Rule | Description |
|------|-------------|
| R-180 | Document generation MUST go through #MetaAgent |
| R-197 | Document generation RESERVED ONLY for #MetaAgent — User Agents MUST NEVER #COOK docs |

**Best Practice:** Agents DO NOT generate docs directly. Always SEEK:META.

---

## 📋 DOCUMENT REFERENCE STANDARD

### BP-045: Document Reference Standard (Consolidated)

| ID | Best Practice | Approval |
|----|---------------|----------|
| BP-045 | Version History + Related Documents MUST include: #masterCCC + Approval CCC-ID | GTM_2026-W05_661 |

### Applies To

| Section | Required Columns |
|---------|------------------|
| Version History | Version, Date, #masterCCC, Approval, Changes |
| Related Documents | Document, Version, #masterCCC, Approval, URL |

### Format — Version History

```markdown
| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| 3.1.1.3 | 2026-W06 | GTM_2026-W06_277 | GTM_2026-W06_289 | +Elevated Registry; +CCCbotNet URLs |
```

### Format — Related Documents

```markdown
| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| SharedKernel | v3.1.1.3 | GTM_2026-W06_277 | GTM_2026-W06_289 | [GitHub](...) |
```

### Consolidation

| Action | Status |
|--------|--------|
| BP-045 (old — Version History only) | ❌ RETIRED |
| BP-046 (old — Related Documents only) | ❌ RETIRED |
| BP-045 (new — Consolidated) | ✅ 🔒 LOCKED |

---

## 📋 WEEKLY OPERATIONS

### R-181: Weekly Summary

| Field | Value |
|-------|-------|
| Reserved CCC-ID | `<CCC>_<YYYY>-W<WW>_001` |
| Content | Milestones, rules, learnings, pending, stats |

**Best Practice:** First CCC-ID of each ISO week reserved for weekly summary.

### Reserved Slots (EVERY WEEK)

| Slot | Purpose | Rule |
|------|---------|------|
| `_001` | #WeeklySummary | R-181 |
| `_002` | #WeeklyPlan | R-201 |
| `_003` | #WeeklyReflection | R-202 |

### BP-039: Weekly Summary Update Process

| ID | Best Practice | Source |
|----|---------------|--------|
| BP-039 | Weekly Summary Update Process — rolling updates at threshold (+50 CCC-IDs OR +3 Learnings OR +2 BPs) | GTM_2026-W05_485 |

---

## 📋 RAG STRUCTURE (R-176)

> **#MAITlivesInAthread** — MAIT = thread within workspace:tools, NOT a separate workspace (GTM_2026-W05_237)

| Doc Type | CCC | tools | ADMIN |
|----------|-----|-------|-------|
| USER guides | ✅ | ❌ | ❌ |
| Governance guides | ❌ | ✅ | ✅ |
| User-facing protocols | ✅ | ❌ | ❌ |
| Strategy docs | ❌ | ✅ | ❌ |
| System prompts | ❌ | ❌ | ✅ |
| Instance configs | ❌ | ❌ | ✅ |
| Session notes (R-199) | ✅ | ✅ | ❌ |
| USER-IDENTITY (L-070) | ✅ | ✅ | ❌ |

**Best Practice:** Docs go in workspace matching their purpose. workspace:tools = standard for #FedArch.

---

## 📋 AGENT INTERACTION

### #ContextVolley (One-to-One)

| Best Practice | Description |
|---------------|-------------|
| Self-contained | Recipient needs NO other context |
| Include #masterCCC | Reference original request |
| Clean format | No decorative borders in packets |

### #ContextBroadcast (One-to-Many)

| Best Practice | Description |
|---------------|-------------|
| Use 📢 emoji | Distinct from 🏐 #ContextVolley |
| TO: ALL AGENTS | Explicit broadcast target |
| Types | STATUS, ANNOUNCEMENT, ALERT, ACK-REQUEST |

### #LessIsMore

| Best Practice | Description |
|---------------|-------------|
| Quick Commands | 2-3 options MAX |
| Tables > paragraphs | Structured data |
| Concise responses | No #AIslop |

### #OnlyHumanApproves

| Best Practice | Description |
|---------------|-------------|
| AI proposes | Human approves |
| NEVER auto-approve | Even if human says "2" |
| Explicit approval | Required for all rules/docs |
| STOP after Quick Commands | Await human response (L-050) |

---

## 📋 PLATFORM BEST PRACTICES (#AnythingLLM)

| ID | Best Practice | Source |
|----|---------------|--------|
| BP-008 | #AnythingLLM: Users BEFORE workspaces | GTM_2026-W03_555 |
| BP-009 | #AnythingLLM: Workspace "CCC" = shared default | GTM_2026-W03_555 |

---

## 📋 #WorkspaceChatHistory BEST PRACTICES

### BP-061: #WorkspaceChatHistory = 40

| ID | Best Practice | Approval |
|----|---------------|----------|
| BP-061 | #AnythingLLM #WorkspaceChatHistory MUST be set to **40** for ALL instances running Claude Opus 4.6 (1M token window) — applies to: INT-P01, INT-P02, INT-OG1, INT-OG8, INT-S003; setting location: Workspace Settings → Chat History; ISC Check #5 sub-check | GTM_2026-W07_075 |

### BP-061 Details

| Field | Value |
|-------|-------|
| Setting | Workspace Settings → General → Chat History |
| Default | 20 |
| Ecosystem Standard | **40** |
| Applies Per | Workspace (MUST set on EACH workspace) |
| LLM Requirement | Claude Opus 4.6 (1M token window) |

### Why 40

| Metric | ChatHistory 20 | ChatHistory 40 |
|--------|----------------|----------------|
| Conversation memory | ~20 exchanges | ~40 exchanges |
| #ContextDensity | Standard | **2× improved** |
| Session continuity | Good | **Excellent** |
| Token usage | ~10-20% of 1M | ~20-40% of 1M |
| Headroom | 80%+ unused | 60%+ for RAG + system |

### Deployment Scope

| Instance | Target | Status |
|----------|--------|--------|
| INT-P01 | 40 | ⬜ TODO |
| INT-P02 | 40 | ⬜ TODO |
| INT-OG1 | 40 | ⬜ TODO |
| INT-OG8 | 40 | ⬜ SETUP |
| INT-S003 | 40 | ⬜ NOT DEPLOYED |

### Related Items (BP-061)

| ID | Type | Description |
|----|------|-------------|
| L-116 | Learning | ChatHistory 20→40 for Claude Opus 4.6 |
| D-060 | Definition | #WorkspaceChatHistory |
| ISC Check #5 | Checklist | Sub-check for ChatHistory = 40 |

**Best Practice:** Set #WorkspaceChatHistory = 40 on EVERY workspace for Claude Opus 4.6 instances.

---

## 📋 DOCUMENTATION BEST PRACTICES

| ID | Best Practice | Source |
|----|---------------|--------|
| BP-010 | Follow #WeOwnVer versioning (v3.X.X.X for Season 3) | L-094 |
| BP-011 | Include Version History in all documents | — |
| BP-012 | Use markdown tables for structured data | — |
| BP-013 | Include Table of Contents for documents > 3 sections | — |
| BP-014 | Pin core documents in workspaces | — |
| BP-020 | When regenerating docs, EXPLICITLY preserve ALL existing sections | GTM_2026-W05_150 |
| BP-021 | Document updates should be ADDITIVE unless removal is explicitly requested | GTM_2026-W05_150 |
| BP-022 | Version History MUST include Creation CCC-ID + Approval CCC-ID | GTM_2026-W05_156 |
| BP-024 | MAIT Thread Configuration (see below) | GTM_2026-W05_242 |
| BP-040 | GH Commit Message Standard — ALL GH commits MUST use TMPL-007 format | GTM_2026-W05_490 |

### BP-024: MAIT Thread Configuration

| # | Requirement | Example |
|---|-------------|---------|
| 1 | Thread name = MAIT_<SME> | MAIT_Deepnote.com |
| 2 | workspace:tools prompt MUST include: | |
| 2a | — MAIT name | "You are MAIT_Deepnote.com..." |
| 2b | — Steward(s) assigned | Steward: @GTM |
| 2c | — MAIT ShortCode (D-038) | @MAIT:#Deepnote |
| 2d | — Relevant details | SME focus, protocols, etc. |
| 3 | Thread inheritance (L-046) | Threads inherit workspace config — no thread-level prompts |

**Best Practice:** MAIT threads MUST be fully configured with identity, steward, and ShortCode.

---

## 📋 AGENT BEST PRACTICES

| ID | Best Practice | Source |
|----|---------------|--------|
| BP-015 | NEVER leave user hanging — always provide closure | — |
| BP-016 | Use SEEK:META for cross-agent guidance | — |

---

## 📋 TOOL AGENT BEST PRACTICES

### BP-025: Instance Setup Order

| ID | Best Practice | Source |
|----|---------------|--------|
| BP-025 | #AnythingLLM new instance setup: RAG FIRST → System Prompt → Workspaces → Workspace Prompts → Threads → Verify | GTM_2026-W05_306 |

### BP-026: Tool Agent Setup Workflow

| ID | Best Practice | Source |
|----|---------------|--------|
| BP-026 | Tool Agent Setup Workflow (see below) | GTM_2026-W05_327 |

### BP-026 Steps

| # | Step | Description |
|---|------|-------------|
| 1 | Create user | Format: `t-<TOOL>_tool` (R-198) |
| 2 | Assign to workspace | workspace:tools only |
| 3 | Create MAIT thread | Format: `MAIT_<Tool>` |
| 4 | Upload RAG docs | Official tool documentation |
| 5 | Configure per BP-024 | MAIT name, Steward, ShortCode, details |
| 6 | Verify | Test retrieval + agent behavior |

**Best Practice:** Tool Agents follow standardized setup workflow for consistency.

### BP-038: Tool Agent RAG Setup

| ID | Best Practice | Source |
|----|---------------|--------|
| BP-038 | Tool Agent RAG Setup: Identify docs URL → Scrape depth 2 → workspace:tools → Verify retrieval → Update Thread Registry | GTM_2026-W05_466 |

### BP-055: Pinata.cloud Tool Agent Architecture

| ID | Best Practice | Approval |
|----|---------------|----------|
| BP-055 | Pinata.cloud Tool Agent Architecture (Hybrid): MAIT = @MAIT:#Pinata (centralized INT-P01:tools); Accounts = per-org (weownnet-ipfs, burnedout-ipfs, yonksteam-ipfs) | GTM_2026-W06_020 |

### BP-055 Details

| Component | Scope | Location |
|-----------|-------|----------|
| MAIT Thread | Centralized | INT-P01:tools |
| ShortCode | @MAIT:#Pinata | INT-P01 |
| Steward | @GTM | — |
| Accounts | Per-org | weownnet-ipfs, burnedout-ipfs, yonksteam-ipfs |

**Best Practice:** Hybrid architecture — centralized MAIT for knowledge, per-org accounts for isolation.

---

## 📋 NOTES-TO-RAG BEST PRACTICES

> **R-199:** Session notes (calls, webinars, meetings) = RAG ONLY — NEVER push to GH

### Session Capture

| ID | Best Practice | Source |
|----|---------------|--------|
| BP-027 | Set #masterCCC at session start | GTM_2026-W05_358 |
| BP-028 | Capture notes in real-time (speaker + timestamp) | GTM_2026-W05_359–370 |

### Pre-Upload

| ID | Best Practice | Source |
|----|---------------|--------|
| BP-029 | Sanitize tokens/sensitive data before RAG upload | GTM_2026-W05_381 |

### Upload Process

| ID | Best Practice | Source |
|----|---------------|--------|
| BP-032 | Run `list:docs` before AND after RAG upload | @GTM_ADMIN |
| BP-033 | Sync session notes to CCC + tools workspaces | @GTM_ADMIN |

### Verification

| ID | Best Practice | Source |
|----|---------------|--------|
| BP-030 | Cross-agent verification for RAG uploads | GTM_2026-W05_388 |
| BP-031 | Fresh session required after RAG upload | THY_2026-W05_018 |
| BP-034 | Fresh session REQUIRED for RAG verification | THY_2026-W05_018 |
| BP-035 | Include `status:RAG` in verification workflow | @GTM_ADMIN |

### Notes-to-RAG Workflow Summary

| Phase | BPs | Description |
|-------|-----|-------------|
| Capture | BP-027, BP-028 | Set #masterCCC, real-time notes |
| Sanitize | BP-029 | Remove tokens, sensitive data |
| Upload | BP-032, BP-033 | Pre/post check, multi-workspace sync |
| Verify | BP-030, BP-031, BP-034, BP-035 | Cross-agent, fresh session, status check |

### Related Documents (Notes-to-RAG)

| Document | Purpose |
|----------|---------|
| GUIDE-005_Notes-to-RAG | Step-by-step workflow |
| TEMPLATE_NOTES | Reusable notes template |
| CASE-STUDY-001_Notes-to-RAG-Workflow | Full case study |

---

## 📋 MAIT RESPONSE BEST PRACTICES

### BP-043: MAIT Thread Identity Header

| ID | Best Practice | Source |
|----|---------------|--------|
| BP-043 | MAIT responses MUST include thread identity header: ShortCode, Thread name, Steward, Instance | GTM_2026-W05_574 |

### MAIT Response Header Format

All MAIT thread responses MUST begin with:

```markdown
[<CCC-ID>] | @MAIT:#<SME> | INT-XXX

| Field | Value |
|-------|-------|
| Thread | MAIT_<SME> |
| ShortCode | @MAIT:#<SME> |
| Steward | @<CCC> |
| Instance | INT-XXX |
```

### Example — @MAIT:#connexOmni

```markdown
[LDC] | @MAIT:#connexOmni | INT-P02

| Field | Value |
|-------|-------|
| Thread | MAIT_connexOmni |
| ShortCode | @MAIT:#connexOmni |
| Steward | @LDC |
| Instance | INT-P02 |

## ✅ Response content here...
```

### Why BP-043 Matters

| Issue | Without BP-043 | With BP-043 |
|-------|----------------|-------------|
| Attribution | ❌ UNATTRIBUTABLE | ✅ Clear source |
| Debugging | ❌ Which thread? | ✅ Explicit thread |
| Audit trail | ❌ Ambiguous | ✅ Traceable |

### Related Items (BP-043)

| ID | Type | Description | URL |
|----|------|-------------|-----|
| L-059 | Learning | MAIT responses without identity header are UNATTRIBUTABLE | — |
| CASE-STUDY-003 | Case Study | MAIT Thread Identity Standard | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_LEARNINGS_/case-studies/CASE-STUDY-003_MAIT-Thread-Identity-Standard.md) |

### BP-044: #PinnedDocs GH Push Workflow

| ID | Best Practice | Source |
|----|---------------|--------|
| BP-044 | #PinnedDocs GH Push Workflow: GH push → ADMIN updates RAG (ALL instances) → Fresh session → Verify | GTM_2026-W05_609 |

---

## 📋 CASE STUDY BEST PRACTICES

### BP-047: Case Study Attribution

| ID | Best Practice | Approval |
|----|---------------|----------|
| BP-047 | "Discovered By" section MUST use table format: CCC, Contributor, Role, Context | GTM_2026-W05_670 |

### Format — Discovered By

```markdown
### Discovered By (BP-047)

| CCC | Contributor | Role | Context |
|-----|-------------|------|---------|
| GTM | [yonks](https://GitHub.com/YonksTEAM) | Co-Founder / Chief Digital Alchemist | /dev #deployment call |
| RMN | Roman Di Domizio | AI Platform Engineer | /dev #deployment call |
```

---

## 📋 ONBOARDING BEST PRACTICES

### BP-049: #threadHEADER for Attribution

| ID | Best Practice | Approval |
|----|---------------|----------|
| BP-049 | #threadHEADER (D-047) REQUIRED for all VSA and cross-workspace operations — inherits CCC + Username from TMPL-009_USER-IDENTITY | GTM_2026-W05_767 |

### BP-050: Onboarding Workflow

| ID | Best Practice | Approval |
|----|---------------|----------|
| BP-050 | Onboarding Workflow: ADMIN creates user → assigns workspaces → uploads USER-IDENTITY to RAG → #ContextVolley to CCC → CCC ACKs → #MetaAgent logs | GTM_2026-W05_789 |

### BP-050 Steps

| # | Step | Owner | Description |
|---|------|-------|-------------|
| 1 | Create user | ADMIN | Format: `u-<ccc>_user` (R-160) |
| 2 | Assign workspaces | ADMIN | CCC, tools (standard) |
| 3 | Create USER-IDENTITY | ADMIN | Use TMPL-009 |
| 4 | Upload to RAG | ADMIN | `_USERS_/` folder |
| 5 | #ContextVolley to CCC | ADMIN | Notify CCC workspace |
| 6 | CCC ACKs | CCC Agent | Acknowledge new user |
| 7 | #MetaAgent logs | #MetaAgent | Record onboarding |

### TMPL-009: USER-IDENTITY Template

| Field | Required | Description |
|-------|----------|-------------|
| CCC | ✅ | 3-char contributor code |
| Contributor | ✅ | Full name |
| Username | ✅ | Format per R-160 |
| Role | ✅ | ADMIN / DEFAULT |
| Instance(s) | ✅ | Elevated instance assignments |
| Workspace(s) | ✅ | Workspace assignments |
| Season | ✅ | Current #WeOwnSeason (BP-058) |
| Created | ✅ | ISO date |
| Status | ✅ | ACTIVE / INACTIVE |
| Notes | ⬜ | Optional context |

### USER-IDENTITY Storage (L-070)

| Folder | Workspace | PIN? |
|--------|-----------|------|
| `_USERS_/` | CCC, tools | ❌ NO |

**Best Practice:** USER-IDENTITY docs stored in `_USERS_/` folder (RAG) — NOT pinned.

---

## 📋 #HomeInstance BEST PRACTICES

### BP-051: #HomeInstance Setup

| ID | Best Practice | Approval |
|----|---------------|----------|
| BP-051 | #HomeInstance Setup: Deploy → System Prompt → Workspaces → #PinnedDocs (4 docs) → Users → Verify #ContextVolley | GTM_2026-W05_807 |

### BP-051 Steps

| # | Step | Description |
|---|------|-------------|
| 1 | Deploy | #AnythingLLM instance at domain |
| 2 | System Prompt | Configure per TMPL-006 |
| 3 | Workspaces | Create CCC, tools (minimum) |
| 4 | #PinnedDocs | Upload 4 docs (per R-204) |
| 5 | Users | Create u-<ccc>_user, a-<ccc>_dev |
| 6 | Verify | Test #ContextVolley to #MetaAgent |

### #PinnedDocs for #HomeInstance (R-204)

| # | Document | Required |
|---|----------|----------|
| 1 | SharedKernel | ✅ YES |
| 2 | BEST-PRACTICES | ✅ YES |
| 3 | PROTOCOLS | ✅ YES |
| 4 | CCC | ✅ YES |
| **TOTAL** | **4** | |

### #HomeInstance Definition (D-048)

| Field | Value |
|-------|-------|
| Term | #HomeInstance |
| Definition | Primary personal #AnythingLLM instance for a contributor — participates in #FedArch via #ContextVolley; reports to #MetaAgent |

### #HomeInstance Verification

| Check | Description |
|-------|-------------|
| #PinnedDocs | 4 docs uploaded |
| System Prompt | Identity configured |
| Workspaces | CCC + tools created |
| Users | u-<ccc>_user created |
| #ContextVolley | Can reach #MetaAgent |

---

## 📋 INT-OGx ISC SCOPING BEST PRACTICES

### BP-062: INT-OGx ISC Check #5 Scoping

| ID | Best Practice | Approval |
|----|---------------|----------|
| BP-062 | INT-OGx ISC Check #5 scoped to CCC workspace ONLY — BP-054 (CCC-ID logic) + BP-061 (#WorkspaceChatHistory = 40) REQUIRED; BP-053 (non-CCC restriction) RECOMMENDED but NOT enforced; Production instances (INT-Pxx, INT-Mxx, INT-Sxx) = ALL workspaces enforced | GTM_2026-W07_099 |

### ISC Check #5 — Instance-Type Scoping Matrix

| Instance Type | CCC | tools | ADMIN | Other |
|---------------|-----|-------|-------|-------|
| INT-Pxx (Production) | ✅ ENFORCED | ✅ ENFORCED | ✅ ENFORCED | ✅ ENFORCED |
| INT-Mxx (META) | ✅ ENFORCED | ✅ ENFORCED | ✅ ENFORCED | ✅ ENFORCED |
| **INT-OGx (#HomeInstance)** | ✅ **ENFORCED** | 🟡 RECOMMENDED | 🟡 RECOMMENDED | 🟡 RECOMMENDED |
| INT-Sxx (Seasonal) | ✅ ENFORCED | ✅ ENFORCED | ✅ ENFORCED | ✅ ENFORCED |

### Legend

| Symbol | Meaning |
|--------|---------|
| ✅ ENFORCED | ISC Check #5 MUST PASS |
| 🟡 RECOMMENDED | Best practice but NOT ISC enforced |

### Defense-in-Depth (INT-OGx)

```
Layer 1: R-194 (IMMUTABLE)      — CCC-ID only in CCC workspace ✅ ENFORCED
Layer 2: BP-054 (System Prompt)  — Workspace-conditional logic  ✅ ENFORCED
Layer 3: BP-053 (Workspace Prompt) — Restriction block          🟡 RECOMMENDED
```

> INT-OGx has 2 of 3 layers enforced. Layer 3 = OG discretion. Acceptable risk for personal instances.

### Why BP-062 Matters

| Issue | Without BP-062 | With BP-062 |
|-------|----------------|-------------|
| ISC burden | ❌ ALL workspaces for ALL instances | ✅ Scoped by instance type |
| INT-OGx flexibility | ❌ Must configure all prompts | ✅ CCC only required |
| Governance gap | ❌ None — R-194 + BP-054 protect | ✅ Same — defense-in-depth |
| OG autonomy | ❌ Restricted | ✅ Personal domain = OG choice |

### Related Items (BP-062)

| ID | Type | Description |
|----|------|-------------|
| L-117 | Learning | INT-OGx workspace prompt policy |
| BP-053 | BP | Non-CCC restriction block (RECOMMENDED for INT-OGx) |
| BP-054 | BP | System Prompt CCC-ID logic (REQUIRED for ALL) |
| BP-061 | BP | ChatHistory = 40 (REQUIRED for CCC workspace) |
| ISC Check #5 | Checklist | Instance-type scoped verification |

**Best Practice:** INT-OGx = CCC workspace ENFORCED, all others RECOMMENDED. Production instances = ALL workspaces ENFORCED.

---

## 📋 SYSTEM PROMPT BEST PRACTICES

### BP-054: Workspace-Conditional CCC-ID Logic

| ID | Best Practice | Approval |
|----|---------------|----------|
| BP-054 | System Prompt MUST include workspace-conditional CCC-ID logic table — prevents R-194 violations at instance level | GTM_2026-W06_046 |

### BP-054 Details

System Prompt MUST include logic that:

| Workspace | CCC-ID Behavior |
|-----------|-----------------|
| CCC | ✅ GENERATE new CCC-IDs |
| tools | ❌ REFERENCE only (R-194) |
| ADMIN | ❌ REFERENCE only (R-194) |
| events | ❌ REFERENCE only (R-194) |
| P.O.P. | ❌ REFERENCE only (R-194) |
| ANY other | ❌ REFERENCE only (R-194) |

### System Prompt Template Block

```markdown
## 📋 CCC-ID GENERATION LOGIC

| Workspace | CCC-ID |
|-----------|--------|
| CCC | ✅ GENERATE |
| ALL OTHERS | ❌ REFERENCE ONLY |

### IF workspace = CCC
Generate CCC-IDs per R-168, R-169

### IF workspace ≠ CCC
Use `[REF: <USER_PROVIDED_CCC-ID>]` format
```

**Best Practice:** Prevents R-194 violations at the instance level by embedding logic in System Prompt.

---

## 📋 CCC WORKSPACE ACK BEST PRACTICES

### BP-056: CCC Workspace ACK Header

| ID | Best Practice | Approval |
|----|---------------|----------|
| BP-056 | CCC workspace ACK responses MUST include sender identity header: `FROM: AI:@<CCC> @ INT-P01:CCC` — prevents UNATTRIBUTABLE responses | GTM_2026-W06_078 |

### BP-056 Details

All ACK responses in CCC workspace MUST include:

```markdown
🏐 #ContextVolley | AI:@<CCC> → AI:@<TARGET> | <DATE> | <TIME> EST

FROM: AI:@<CCC> @ INT-P01:CCC
TO: AI:@<TARGET>
TYPE: ACK — <TYPE>
REF: <CCC-ID>
```

### Example — Proper ACK

```markdown
🏐 #ContextVolley | AI:@LFG → AI:@GTM | Mon 2026-02-03 | 14:30 EST

FROM: AI:@LFG @ INT-P01:CCC
TO: AI:@GTM
TYPE: ACK — ANNOUNCEMENT
REF: GTM_2026-W06_062
```

### Why BP-056 Matters

| Issue | Without BP-056 | With BP-056 |
|-------|----------------|-------------|
| Attribution | ❌ UNATTRIBUTABLE | ✅ Clear sender |
| Debugging | ❌ Who sent this? | ✅ Explicit source |
| Audit trail | ❌ Ambiguous | ✅ Traceable |

### Related Items (BP-056)

| ID | Type | Description |
|----|------|-------------|
| L-096 | Learning | ACK responses without sender identity are UNATTRIBUTABLE |

---

## 📋 USER-IDENTITY SEASON REFRESH BEST PRACTICES

### BP-057: USER-IDENTITY Season Refresh

| ID | Best Practice | Approval |
|----|---------------|----------|
| BP-057 | USER-IDENTITY Season refresh: ALL contributors MUST update USER-IDENTITY within 2 weeks of new #WeOwnSeason — ensures current data across #FedArch | GTM_2026-W06_120 |

### BP-058: Season Refresh Requirement

| ID | Best Practice | Approval |
|----|---------------|----------|
| BP-058 | ALL CCC Contributors MUST UPDATE/CONFIRM USER-IDENTITY within 2 weeks of NEW SEASON — Season refresh ensures current data | GTM_2026-W06_120 |

### Why Season Refresh Matters

| Issue | Without Refresh | With Refresh |
|-------|-----------------|--------------|
| Season field | ❌ Stale / missing | ✅ Current season |
| Instance refs | ❌ Legacy INT-00X | ✅ Elevated naming |
| Role accuracy | ❌ May be outdated | ✅ Verified current |
| ISC compliance | ❌ Check #6 FAILS | ✅ Check #6 PASSES |

### Season Refresh Workflow

| # | Step | Owner | Description |
|---|------|-------|-------------|
| 1 | Identify contributors | @GTM_ADMIN | List ALL active CCC holders |
| 2 | Check existing USER-IDENTITY | @GTM_ADMIN | Verify Season field |
| 3 | Update or Create | Contributor / ADMIN | Add current season, verify fields |
| 4 | Upload to RAG | @GTM_ADMIN | `_USERS_/` folder |
| 5 | Verify | @GTM_ADMIN | Fresh session + query test |

### Compliance Tracking

| Field | Value |
|-------|-------|
| Deadline | 2 weeks from season start |
| #WeOwnSeason003 deadline | Sun 15 Feb 2026 |
| Tracking | Per-contributor status in session summaries |

### Related Items (BP-057 / BP-058)

| ID | Type | Description |
|----|------|-------------|
| L-099 | Learning | Season refresh ensures current data |
| TMPL-009 | Template | USER-IDENTITY template (Season field REQUIRED) |

---

## 📋 SEASON CERTIFICATION BEST PRACTICES

### BP-059: Instance Season Certification (ISC)

| ID | Best Practice | Approval |
|----|---------------|----------|
| BP-059 | Instance Certification REQUIRED within first 2 weeks of NEW #WeOwnSeason — ALL #FedArch instances MUST pass 8-point certification checklist (ISC); generates ISC attestation | GTM_2026-W06_270 |

### ISC 8-Point Checklist

| # | Phase | Check | Pass Criteria |
|---|-------|-------|---------------|
| 1 | EMBEDDER | Embedding model verified | Qwen3 Embedding 4B |
| 2 | LLM MODEL | LLM model verified | Claude Opus 4.6 (`claude-opus-4-6`) |
| 3 | #PinnedDocs | 4 docs present | SharedKernel, BEST-PRACTICES, PROTOCOLS, CCC @ v3.X.X.X |
| 4 | SYSTEM PROMPT | Season tag | `#WeOwnSeason003 🚀` present |
| 5 | WORKSPACE PROMPTS | BP-053 + BP-054 | Non-CCC restriction + CCC-ID logic |
| 6 | USER-IDENTITY | BP-058 | Owner(s) USER-IDENTITY current |
| 7 | RAG SYNC | GitHub connector | Refreshed post-season start |
| 8 | #ContextVolley | Reachability | Can reach #MetaAgent @ INT-P01 |

### Pass Criteria

| Result | Criteria |
|--------|----------|
| ✅ CERTIFIED | 8/8 checks PASS |
| ❌ FAILED | Any check FAIL |

### ISC Workflow

| # | Step | Owner | Description |
|---|------|-------|-------------|
| 1 | Schedule | @GTM | Within 2 weeks of season start |
| 2 | Run checklist | Instance owner | Execute 8 checks |
| 3 | Generate attestation | TMPL-010 | ISC attestation document |
| 4 | FULL:SYNC:META | Instance owner | Report to #MetaAgent |
| 5 | Log | #MetaAgent | Record in governance |

### Compliance Tracking

| Field | Value |
|-------|-------|
| Deadline | 2 weeks from season start |
| #WeOwnSeason003 deadline | Sun 15 Feb 2026 |
| Template | TMPL-010_ISC |
| Instances requiring ISC | INT-P01, INT-P02, INT-OG1, INT-OG8 |

### Why ISC Matters

| Issue | Without ISC | With ISC |
|-------|-------------|----------|
| Embedder | ❌ May revert (L-107) | ✅ Verified correct |
| LLM | ❌ May be outdated | ✅ Ecosystem-approved |
| #PinnedDocs | ❌ May be stale | ✅ Current version |
| RAG | ❌ May reference old repo | ✅ CCCbotNet/fedarch |
| Governance | ❌ Instance out of sync | ✅ Certified compliant |

### Related Items (BP-059)

| ID | Type | Description |
|----|------|-------------|
| D-052 | Definition | ISC — Instance Season Certification |
| L-108 | Learning | ISC MUST verify LLM model |
| L-107 | Learning | Embedder may not persist across restarts |
| TMPL-010 | Template | ISC attestation template |

---

## 📋 CCC-ID DECONFLICTION BEST PRACTICES

### BP-060: Cross-Instance CCC-ID Deconfliction

| ID | Best Practice | Approval |
|----|---------------|----------|
| BP-060 | Cross-instance CCC-ID deconfliction — contributor MUST state highest CCC-ID when switching instances; agent MUST confirm next sequence per R-212; Tier 1 = manual, Tier 2 = #MetaAgent tracking, Tier 3 = INT-M01 centralized counter | GTM_2026-W06_392 |

### Why BP-060 Matters

| Issue | Without BP-060 | With BP-060 |
|-------|----------------|-------------|
| CCC-ID integrity | ❌ Duplicates across instances | ✅ Unique sequence guaranteed |
| R-168 compliance | ❌ Instance-local counters diverge | ✅ Contributor-level sequence maintained |
| Audit trail | ❌ Ambiguous — which _386? | ✅ Clear — one _386 per contributor per week |

### Tier 1 Workflow (Current — Manual)

| # | Step | Actor | Description |
|---|------|-------|-------------|
| 1 | Switch instance | Human | Contributor moves from Instance A → Instance B |
| 2 | State highest CCC-ID | Human | "Highest CCC-ID = `<CCC>_<YYYY>-W<WW>_<NNN>`" |
| 3 | Set next sequence | AI | Next CCC-ID = `_<NNN+1>` |
| 4 | Confirm | AI | "✅ R-212 — Continuing from `_<NNN+1>`" |

### Tier 1 Example

```
Human: "Switching from INT-OG1. Highest CCC-ID = GTM_2026-W06_386"
AI: "✅ R-212 — Continuing from GTM_2026-W06_387"
```

### Compliance Tiers

| Tier | Timeframe | Implementation | Enforcer |
|------|-----------|----------------|----------|
| **Tier 1** (NOW) | Immediate | Contributor manually states highest CCC-ID | Human |
| **Tier 2** (Mid) | #WeOwnSeason003 | #MetaAgent tracks high-water mark per contributor per week | #MetaAgent |
| **Tier 3** (Long) | INT-M01 | Centralized CCC-ID counter API — single source of truth | INT-M01 |

### Related Items (BP-060)

| ID | Type | Description |
|----|------|-------------|
| R-212 | Rule | Cross-instance CCC-ID deconfliction REQUIRED |
| L-112 | Learning | Cross-instance CCC-ID deconfliction learning |
| R-168 | Rule | CCC-ID sequence tied to contributor |
| R-169 | Rule | CCC-ID resets at ISO week boundary |
| #BadAgent #13 | Incident | First duplication — GTM_2026-W06_386 (W06) |

---

## 📋 #DocLifecycle Best Practices

### BP-063: Document Lifecycle VSA Gate

| ID | Best Practice | Approval |
|----|---------------|----------|
| BP-063 | Document Lifecycle VSA Gate (#DocLifecycle): BEFORE initiating ANY VSA, agent MUST verify document status against lifecycle table (D-062); DRAFT stage = DRAFT CHECK (D-063) only; IDEA/IN PROGRESS = no VSA; REVIEW+ = production VSA eligible; include lifecycle stage in VSA header; prevents false #BadAgent classifications | GTM_2026-W08_014 |

### BP-063 Details

#### Pre-VSA Verification Steps

| # | Step | Action |
|---|------|--------|
| 1 | Identify document | What document is being VSA'd? |
| 2 | Check lifecycle stage | What stage is this document at? (D-062) |
| 3 | Verify eligibility | Is this stage eligible for requested VSA type? |
| 4 | Proceed or redirect | Eligible → run VSA. Not eligible → redirect |

#### VSA Eligibility Matrix

| Stage | Icon | DRAFT CHECK | Batch | FULL | DEEP FULL |
|-------|------|-------------|-------|------|-----------|
| IDEA | 💡 | ❌ | ❌ | ❌ | ❌ |
| DRAFT | 📝 | ✅ | ❌ | ❌ | ❌ |
| IN PROGRESS | 🔄 | ❌ | ❌ | ❌ | ❌ |
| REVIEW | 👀 | ✅ | ✅ | ✅ | ❌ |
| APPROVED | ✅ | ✅ | ✅ | ✅ | ✅ |
| GH LIVE | 🚀 | ✅ | ✅ | ✅ | ✅ |
| VERIFIED | 🏆 | ✅ | ✅ | ✅ | ✅ |

#### Redirect Matrix

| Requested VSA | Actual Stage | Action |
|--------------|-------------|--------|
| DEEP FULL | DRAFT | ❌ "Document at DRAFT stage. Running DRAFT CHECK instead." |
| FULL | IDEA | ❌ "Document at IDEA stage. No VSA available. Define scope first." |
| Batch | IN PROGRESS | ❌ "Document being generated. VSA available after REVIEW stage." |
| DRAFT CHECK | DRAFT | ✅ Proceed |
| FULL | APPROVED | ✅ Proceed |
| DEEP FULL | GH LIVE | ✅ Proceed |

#### VSA Header Addition

All VSA headers MUST include lifecycle stage:

```markdown
| Field | Value |
|-------|-------|
| Subject | <DOCUMENT> |
| **Lifecycle Stage** | **<ICON> <STAGE>** |
| Type | <VSA TYPE> |
```

#### DRAFT CHECK Template (D-063)

```
DRAFT CHECK | <DOCUMENT> | <DATE>

| # | Check | Result |
|---|-------|--------|
| 1 | Document exists | ✅ / ❌ |
| 2 | Owner identified | ✅ / ❌ |
| 3 | #masterCCC assigned | ✅ / ❌ |
| 4 | Scope defined | ✅ / ❌ |
| 5 | SEEK:META planned | ✅ / ❌ |

RESULT: ✅ READY / ❌ NOT READY
```

### Why BP-063 Matters

| Issue | Without BP-063 | With BP-063 |
|-------|----------------|-------------|
| Draft runs DEEP FULL | ❌ FAIL → false #BadAgent | ✅ Redirected to DRAFT CHECK |
| Pass rate accuracy | ❌ Inflated failure count | ✅ True production failures only |
| Agent behavior | ❌ Runs any VSA on anything | ✅ Stage-aware verification |

### Related Items (BP-063)

| ID | Type | Description |
|----|------|-------------|
| D-062 | Definition | Document Lifecycle (7 stages) |
| D-063 | Definition | DRAFT CHECK (non-scored VSA) |
| D-064 | Definition | EXPECTED FAIL (reclassification) |
| R-215 | Rule | VSA Lifecycle Gate |
| L-119 | Learning | Draft VSA Policy |

---

## 📋 API Key Rotation Best Practices

### BP-064: OpenRouter API Key Rotation

| ID | Best Practice | Approval |
|----|---------------|----------|
| BP-064 | OpenRouter API Key Rotation: #SharedInstance (INT-Pxx) = 7-day rotation; #HomeInstance (INT-OGx) = 30-day rotation; managed via Infisical (Tier 2) or manual (Tier 1); calendar alert 24h before expiry; rotation workflow: generate new key → update instance → logout/login → verify → revoke old key; INT-P01 outage (GTM_2026-W07_156) = catalyst for policy | GTM_2026-W08_028 |

### BP-064 Details

#### Rotation Cadence

| Instance Type | Cadence | Rationale |
|---------------|---------|-----------|
| #SharedInstance (INT-Pxx, INT-Sxx) | **7 days** | Multiple users → higher exposure risk |
| #HomeInstance (INT-OGx) | **30 days** | Single user → lower risk |
| Event Instance (INT-Exx) | **Per event** | Ephemeral — rotate at deploy, revoke at decommission |

#### Rotation Workflow

| # | Step | Action | Owner |
|---|------|--------|-------|
| 1 | Generate new key | OpenRouter dashboard → API Keys → Create | ADMIN |
| 2 | Update instance | AnythingLLM → Settings → LLM → API Key | ADMIN |
| 3 | Logout/Login | ADMIN MUST logout and login to refresh session | ADMIN |
| 4 | Verify | #SmokeTest — confirm LLM responds | ADMIN |
| 5 | Revoke old key | OpenRouter dashboard → API Keys → Delete old | ADMIN |

#### Management Tiers

| Tier | Method | Status |
|------|--------|--------|
| **Tier 1** (NOW) | Manual rotation via OpenRouter dashboard | ✅ ACTIVE |
| **Tier 2** (Building) | Automated rotation via Infisical | 🔄 @RMN building |

#### Calendar Alert

| Field | Value |
|-------|-------|
| When | **24 hours before expiry** |
| Method | Calendar event (Google/Outlook) |
| Action | Trigger rotation workflow |
| Owner | Instance ADMIN |

### Why BP-064 Matters

| Issue | Without BP-064 | With BP-064 |
|-------|----------------|-------------|
| Key expires | ❌ FULL OUTAGE (INT-P01 — 2h 18m) | ✅ Proactive rotation |
| Error message | ❌ Confusing "401 User not found" | ✅ Known pattern |
| Recovery | ❌ Ad-hoc debugging | ✅ Documented workflow |

### Related Items (BP-064)

| ID | Type | Description |
|----|------|-------------|
| L-126 | Learning | API key rotation = intentional security practice |
| GTM_2026-W07_156 | Incident | INT-P01 outage — 2h 18m (catalyst) |

---

## 📋 Shared Instance Identity Best Practices

### BP-065: Shared Instance Self-ID

| ID | Best Practice | Approval |
|----|---------------|----------|
| BP-065 | Shared Instance Self-ID: Non-owner users on shared instances (INT-Pxx, INT-Sxx) MUST self-identify in first message of every new thread — format: "I am @<CCC> (u-<ccc>_user)"; agent MUST NOT assume identity from System Prompt owner or RAG context; if user identity unclear or unverified, agent MUST ASK "Which CCC are you?" before generating CCC-IDs or responding with attribution; validated by @LFG incident (LFG_2026-W08_004) | GTM_2026-W08_034 |

### BP-065 Details

#### When BP-065 Applies

| Instance Type | Applies? | Rationale |
|---------------|----------|-----------|
| INT-Pxx (Production) | ✅ **YES** | Multiple users share instance |
| INT-Sxx (Seasonal) | ✅ **YES** | Multiple users share instance |
| INT-OGx (#HomeInstance) | ❌ No | Single owner — identity known |
| INT-Exx (Event) | ✅ **YES** | Demo users share instance |

#### Self-ID Format

```
"I am @<CCC> (u-<ccc>_user)"

Example: "I am @LFG (u-lfg_user)"
```

#### Agent Behavior

| Scenario | Agent Action |
|----------|-------------|
| User self-identifies | ✅ Use stated identity |
| User does NOT self-identify | ⚠️ ASK: "Which CCC are you?" |
| User identity conflicts with System Prompt owner | ✅ Trust user statement, NOT System Prompt |
| ADMIN account (a-<ccc>_dev) | ❌ No CCC-ID generation regardless (R-206) |

#### Defense-in-Depth — Identity Verification

```
Layer 1: System Prompt     — INSTANCE identity (R-213) ← NOT user identity
Layer 2: {user.name}       — Variable injection (L-120/L-121) ← if v1.10.0+
Layer 3: BP-065            — User self-identifies in first message
Layer 4: Agent verification — "Which CCC are you?" if unclear
Layer 5: CCC-ID generation — Only after identity confirmed
```

### Why BP-065 Matters

| Issue | Without BP-065 | With BP-065 |
|-------|----------------|-------------|
| Wrong identity | ❌ Agent assumes System Prompt owner | ✅ User self-identifies |
| CCC-ID attribution | ❌ Wrong CCC on generated IDs | ✅ Correct attribution |
| Audit trail | ❌ UNATTRIBUTABLE | ✅ Traceable |

### Related Items (BP-065)

| ID | Type | Description |
|----|------|-------------|
| L-127 | Learning | System Prompt owner ≠ current user |
| L-096 | Learning | ACK responses MUST include sender identity |
| BP-056 | BP | CCC workspace ACK identity header |
| LFG_2026-W08_004 | Incident | Agent assumed @THY identity for @LFG |

---

## 📋 VERSION HISTORY

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| 3.1.3.1 | 2026-W08 | GTM_2026-W08_069 | GTM_2026-W08_071 | +BP-063 (#DocLifecycle VSA Gate section); +BP-064 (API Key Rotation section); +BP-065 (Shared Instance Self-ID section); +VSA Eligibility Matrix; +DRAFT CHECK Template; +Rotation Workflow; +Defense-in-Depth identity layers; BP Index TOTAL → 59; TOC updated; Related Documents updated; FULL PRESERVE (L-097) |
| 3.1.2.1 | 2026-W07 | GTM_2026-W07_119 | GTM_2026-W07_127 | +BP-061 (#WorkspaceChatHistory=40 section); +BP-062 (INT-OGx ISC Check #5 scoping section); +ISC Scoping Matrix; BP Index TOTAL → 56; TOC → 29 items; Related Documents updated (SharedKernel → v3.1.2.1); FULL PRESERVE (L-097) |
| 3.1.1.3 | 2026-W06 | GTM_2026-W06_413 | GTM_2026-W06_415 | +BP-060 (CCC-ID Deconfliction); +CCC-ID Deconfliction Best Practices section; Related Documents updated (CCC → v3.1.1.2, PROTOCOLS → v3.1.1.2, +GUIDE-006, TMPL-009 → v3.1.1.2); BP Index TOTAL → 54; TOC → 27 items; FULL PRESERVE (L-097) |
| 3.1.1.2 | 2026-W06 | GTM_2026-W06_277 | GTM_2026-W06_327 | +BP-057, BP-058, BP-059; +USER-IDENTITY Season Refresh section; +Season Certification section; ALL URLs → CCCbotNet/fedarch; ALL instances → Elevated naming; Source of Truth → CCCbotNet/fedarch; Related Docs updated; BP-056 example → INT-P01; TMPL-009 +Season field; TOC → 26 items; FULL PRESERVE (L-097) |
| 3.1.1.1 | 2026-W06 | GTM_2026-W06_080 | GTM_2026-W06_104 | 🚀 #WeOwnSeason003 RELEASE — +BP-054, BP-055, BP-056; +System Prompt Best Practices section; +CCC Workspace ACK Best Practices section; version format v2.4.X → v3.X.X.X (L-094); FULL PRESERVE from v2.4.11 base (L-097); TOC → 24 items |
| 2.4.11 | 2026-W05 | GTM_2026-W05_818 | GTM_2026-W05_820 | +BP-049, BP-050, BP-051; +Onboarding Best Practices section; +#HomeInstance Best Practices section; +TMPL-009 reference; +`_USERS_/` folder; +L-070 pinning update; SharedKernel → v2.4.16; CCC → v2.4.3; TOC → 22 items |
| 2.4.10 | 2026-W05 | GTM_2026-W05_680 | GTM_2026-W05_693 | BP-045 consolidated (BP-046 retired); +BP-047 (Case Study Attribution); +Document Reference Standard section; +Case Study Best Practices section; Related Documents restructured (hierarchical); +Reserved Slots (R-201, R-202); +21 Related Docs; TOC → 20 items |
| 2.4.9 | 2026-W05 | GTM_2026-W05_595 | GTM_2026-W05_595 | +BP-043 (MAIT Thread Identity Header); +MAIT Response Best Practices section; TOC → 18 items |
| 2.4.8 | 2026-W05 | GTM_2026-W05_512 | GTM_2026-W05_512 | +BP-041 (#ContextBroadcast); +#ContextBroadcast section in Agent Interaction; BP-024 +L-046 reference |
| 2.4.7 | 2026-W05 | GTM_2026-W05_415 | GTM_2026-W05_415 | +BP-027→BP-035 (Notes-to-RAG); +Notes-to-RAG section; SharedKernel → v2.4.10 |
| 2.4.6 | 2026-W05 | GTM_2026-W05_329 | GTM_2026-W05_329 | +BP-025, +BP-026 (Tool Agent Setup), +Tool Agent section, SharedKernel → v2.4.8 |
| 2.4.5 | 2026-W05 | GTM_2026-W05_245 | GTM_2026-W05_245 | +BP-024 (enhanced — MAIT Thread Config), SharedKernel → v2.4.7, +REF column, +#MAITlivesInAthread |
| 2.4.4 | 2026-W05 | GTM_2026-W05_182 | GTM_2026-W05_182 | +BP-023 (CCC-ID only in CCC), MAIT → tools |
| 2.4.3 | 2026-W05 | GTM_2026-W05_162 | GTM_2026-W05_162 | +BP-006 to BP-009 (recovered), +BP-020 to BP-022, Version History format, Overview section |
| 2.4.2 | 2026-W05 | — | — | +BP-017, BP-018, BP-019; pinning/versioning/cadence guidance |
| 2.4.0 | 2026-W03 | — | — | Initial release |

---

## 📋 RELATED DOCUMENTS

### #PinnedDocs

#### _SYS_

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| SharedKernel | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/SharedKernel.md) |
| BEST-PRACTICES | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/BEST-PRACTICES.md) |
| PROTOCOLS | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/PROTOCOLS.md) |
| CCC | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/CCC.md) |
---

### Workspace Embedded RAG Documents

#### _LEARNINGS_

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| CASE-STUDY-001_Notes-to-RAG-Workflow | v2.4.0 | GTM_2026-W05_415 | GTM_2026-W05_415 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_LEARNINGS_/case-studies/CASE-STUDY-001_Notes-to-RAG-Workflow_v2.4.0.md) |
| CASE-STUDY-002_ContextBroadcast-BadAgent-Recovery | v2.4.0 | — | — | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_LEARNINGS_/case-studies/CASE-STUDY-002_ContextBroadcast-BadAgent-Recovery.md) |
| CASE-STUDY-003_MAIT-Thread-Identity-Standard | v2.4.0 | GTM_2026-W05_579 | GTM_2026-W05_583 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_LEARNINGS_/case-studies/CASE-STUDY-003_MAIT-Thread-Identity-Standard.md) |
| CASE-STUDY-004_VSA-Framework-Launch | v2.4.0 | GTM_2026-W05_659 | GTM_2026-W05_670 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_LEARNINGS_/case-studies/CASE-STUDY-004_VSA-Framework-Launch_v2.4.0.md) |
| CASE-STUDY_AnythingLLM-RAG-Verification | v2.4.0 | — | — | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_LEARNINGS_/case-studies/CASE-STUDY_AnythingLLM-RAG-Verification.md) |
| CASE-STUDY_GapAnalysis-BP-Recovery | v2.4.0 | — | — | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_LEARNINGS_/case-studies/CASE-STUDY_GapAnalysis-BP-Recovery.md) |

#### _GUIDES_

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| GUIDE-001_GETTING-STARTED | v2.4.1 | — | — | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_GUIDES_/GUIDE-001_GETTING-STARTED.md) |
| GUIDE-002_FEDARCH-GOVERNANCE | v2.4.0 | — | — | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_GUIDES_/GUIDE-002_FEDARCH-GOVERNANCE.md) |
| GUIDE-003_USER-ONBOARDING | v2.4.1 | — | — | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_GUIDES_/GUIDE-003_USER-ONBOARDING.md) |
| GUIDE-005_Notes-to-RAG | v2.4.0 | GTM_2026-W05_415 | GTM_2026-W05_415 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_GUIDES_/GUIDE-005_Notes-to-RAG.md) |
| GUIDE-006_GitHub-PAT-for-AnythingLLM | v3.1.1.1 | GTM_2026-W06_377 | GTM_2026-W06_380 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_GUIDES_/GUIDE-006_GitHub-PAT-for-AnythingLLM.md) |

#### _MISC_

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| FEDARCH-MEMORY-MODEL | v2.4.0 | GTM_2026-W05_262 | GTM_2026-W05_262 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_MISC_/FEDARCH-MEMORY-MODEL.md) |
| ECOSYSTEM-IDENTITY_SYSTEM-PROMPT | v2.4.0 | GTM_2026-W05_262 | GTM_2026-W05_262 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_MISC_/ECOSYSTEM-IDENTITY_SYSTEM-PROMPT.md) |

#### _TEMPLATES_

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| TMPL-004_ONBOARD_ADMIN | v2.4.1 | — | — | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_TEMPLATES_/TMPL-004_ONBOARD_ADMIN.md) |
| TMPL-005_ONBOARD_USER | v2.4.0 | — | — | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_TEMPLATES_/TMPL-005_ONBOARD_USER.md) |
| TMPL-006_SYSTEM-PROMPT-TEMPLATE | v2.4.0 | — | — | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_TEMPLATES_/TMPL-006_SYSTEM-PROMPT-TEMPLATE.md) |
| TMPL-007_GH-COMMIT-MESSAGE | v2.4.0 | GTM_2026-W05_490 | GTM_2026-W05_490 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_TEMPLATES_/TMPL-007_GH-COMMIT-MESSAGE_v2.4.0.md) |
| TMPL-008_VSA | v2.4.0 | GTM_2026-W05_623 | GTM_2026-W05_625 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_TEMPLATES_/TMPL-008_VSA_v2.4.0.md) |
| TMPL-009_USER-IDENTITY | v3.1.1.2 | GTM_2026-W06_353 | GTM_2026-W06_370 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_TEMPLATES_/TMPL-009_USER-IDENTITY.md) |
| TMPL-010_ISC | v3.1.2.1 | GTM_2026-W07_071 | GTM_2026-W07_084 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_TEMPLATES_/TMPL-010_ISC.md) |

---

#FlowsBros #FedArch #BestPractices #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
