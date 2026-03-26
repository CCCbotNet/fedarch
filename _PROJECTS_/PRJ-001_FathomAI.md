# 📋 PRJ-001: #FathomAI #CallNotes Pipeline

## PRJ-001_FathomAI.md | PRJ-001_FathomAI-CallNotes-Pipeline_v3.2.4.1.md
## ♾️ WeOwnNet 🌐 — Project Document 📁

| Field | Value |
|-------|-------|
| **Document** | PRJ-001_FathomAI-CallNotes-Pipeline.md |
| **Version** | v3.2.4.1 |
| **Folder** | `_PROJECTS_/` ✅ |
| **CCC-ID** | GTM_2026-W13_3013 |
| **#masterCCC** | GTM_2026-W13_3010 |
| **Approval CCC-ID** | **GTM_2026-W13_3028** ✅ |
| **Created** | 2026-03-25 (W13 D3) |
| **Season** | #WeOwnSeason003 🚀 |
| **Lifecycle Stage** | ✅ 🔒 APPROVED (R-011) + 🚀 GH LIVE (D-062) |
| **#LLMmodel** | **Claude Sonnet 4.6 (INT-OG1:CCC @GTM)** |
| **#LLMmodel** | **Claude Opus 4.6 (INT-P01:tools #MetaAgent — Calhoun 🎖️)** |
| **#LLMmodel** | **Qwen3.5-397B-A17B (INT-M02:tools-qwen — Surge ⚡)** |
| **#LLMmodel** | **Xiaomi MiMo-V2-Pro (INT-M02:tools-mimo — MiMo 🧪)** |
| **Tags** | #FathomAI #CallNotes #Paperless #Pipeline #RAG |
| **Folder** | `_PROJECTS_/` 📁 |
| **GH Filename** | PRJ-001_FathomAI.md |
| **Source of Truth** | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-001_FathomAI-CallNotes-Pipeline.md) |

---

## 📖 Table of Contents

1. [Project Overview](#-project-overview)
2. [The Problem](#-the-problem)
3. [The Solution](#-the-solution)
4. [Pipeline Architecture](#-pipeline-architecture)
5. [FOSS Assessment](#-foss-assessment)
6. [Risk Matrix](#-risk-matrix)
7. [Naming Convention](#-naming-convention)
8. [Paperless Schema](#-paperless-schema)
9. [masterCCC Integrity](#-masterccc-integrity)
10. [Deliverables](#-deliverables)
11. [Connector Scope](#-connector-scope)
12. [Operations Architecture](#-operations-architecture)
13. [MAIT Registration](#-mait-registration)
14. [Governance Rulings](#-governance-rulings)
15. [Timeline](#-timeline)
16. [Dependencies](#-dependencies)
17. [Discovered By (BP-047)](#-discovered-by-bp-047)
18. [✅ \[DETAILS\] Document Lifecycle + VSA](#-details-document-lifecycle--vsa)
19. [Related Documents](#-related-documents)
20. [Version History](#-version-history)

---

## 📋 Project Overview

| Field | Value |
|-------|-------|
| **Project ID** | PRJ-001 |
| **Title** | #FathomAI #CallNotes Pipeline |
| **Tagline** | "Every call → AI notes → RAG → searchable forever" |
| **Owner** | @GTM |
| **Priority** | 🟠 P1 |
| **Status** | ✅ APPROVED |
| **Type** | Infrastructure — Document Management |
| **Dependencies** | PRJ-013 (Paperless-ngx) |
| **Registered** | Calhoun 🎖️ (GTM_2026-W13_3011) |

---

## 📋 The Problem

| Problem | Impact |
|---------|--------|
| **Manual call notes** | 15-20 min per call, inconsistent quality |
| **Lost context** | Calls not searchable in RAG — context dies with session |
| **No standard** | Each contributor captures differently or not at all |
| **Cross-instance gap** | Notes on one instance, invisible to others |
| **Scaling** | 10+ contributors × 5+ calls/week = unsustainable |
| **PRJ-012 dependency** | @LFG upload workflow not built yet |

> **L-420:** Without documentation, great ideas drift and are forgotten.
> Calls = where great ideas happen. PRJ-001 = the bridge.

---

## 📋 The Solution

| Component | Tool | FOSS? | Role |
|-----------|------|:-----:|------|
| **Recording + Transcription** | Fathom AI | ⚠️ Proprietary | Auto-record, transcribe, summarize |
| **FOSS Path (L-420 Step 3)** | Whisper.cpp | ✅ MIT | Future FOSS replacement |
| **Storage** | Paperless-ngx (docs.weown.net) | ✅ GPL-3.0 | Private document management |
| **RAG Sync** | AnythingLLM native connector | ⚠️ Elastic 2.0 | Auto-sync to ALL instances |
| **Search** | AnythingLLM RAG | ⚠️ Elastic 2.0 | Full-text search |

---

## 📋 Pipeline Architecture

### Recommended Architecture (MiMo 🧪 — PULL Model)

```
┌─────────────────────────────────────────────────────────────┐
│  Fathom AI                                                   │
│  Auto-record + Transcribe + AI Summary + Action Items        │
└────────────────────┬────────────────────────────────────────┘
                     │ Export .md
                     ▼
┌─────────────────────────────────────────────────────────────┐
│  Paperless-ngx (docs.weown.net) — R-199 ✅                   │
│  ├── Auto-tag: #CallNotes + CCC + YYYY-WXX                  │
│  ├── Correspondent: CCC contributor                          │
│  ├── Document type: Call Notes                               │
│  └── masterCCC custom field                                  │
└────────────────────┬────────────────────────────────────────┘
                     │ Native Connector (Hourly PULL)
                     ▼
┌─────────────────────────────────────────────────────────────┐
│  AnythingLLM Instances (RAG)                                 │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐       │
│  │ INT-P01  │ │ INT-M02  │ │ INT-OG1  │ │ INT-OGx  │       │
│  │ ✅ ALL   │ │ ✅ ALL   │ │ ✅ ALL   │ │ Filtered │       │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘       │
│  Searchable forever. ZERO manual steps.                      │
└─────────────────────────────────────────────────────────────┘
```

### Workflow Steps

| # | Step | Who | Tool |
|---|------|-----|------|
| 1 | Call happens (Zoom/Meet/Restream) | Participants | — |
| 2 | Auto-record + transcribe | Fathom AI | Fathom |
| 3 | AI summary + action items generated | Fathom AI | Fathom |
| 4 | Export → .md (naming convention) | @GTM / contributor | Fathom |
| 5 | Upload to Paperless (email/web/mobile) | @GTM / contributor | Paperless |
| 6 | Paperless auto-tags + metadata | Paperless | Paperless |
| 7 | AnythingLLM polls Paperless (hourly) | Connector | AnythingLLM |
| 8 | Available in RAG — ALL configured instances | — | AnythingLLM |

---

## 📋 FOSS Assessment

### Current Stack (L-420 Step 2 — ITERATE)

| Component | License | FOSS? | L-129 | Notes |
|-----------|---------|:-----:|:-----:|-------|
| **Fathom AI** | Proprietary SaaS | ❌ | ⚠️ | Working NOW. Step 2. |
| **Paperless-ngx** | GPL-3.0 | ✅ | ✅ | Self-hosted. Perfect. |
| **AnythingLLM** | Elastic 2.0 | ⚠️ | ⚠️ | Source-available. Self-hosted = data sovereignty. |

### FOSS Roadmap (L-420 Step 3 — AUTOMATE)

| Component | FOSS Alternative | License | Timeline |
|-----------|-----------------|---------|---------|
| **Fathom AI** | **Whisper.cpp** 🏆 | MIT | W16+ |

### Whisper.cpp — Why #1

| Factor | Detail |
|--------|--------|
| **License** | ✅ MIT (true FOSS, L-129 compliant) |
| **Self-Host** | ✅ Runs on #FedArch infrastructure |
| **Quality** | 🥇 Whisper-level accuracy |
| **Speed** | 🥇 C++ implementation (very fast) |
| **L-129** | ✅ Fully compliant |

> **Hybrid Path:** Fathom NOW (L-420 Step 2) → Whisper.cpp LATER (L-420 Step 3).

---

## 📋 Risk Matrix

| # | Risk | Severity | Mitigation |
|---|------|:--------:|------------|
| 1 | **Fathom AI SPOF** | 🟠 HIGH | Export raw recording immediately. Manual upload fallback. |
| 2 | **masterCCC forgotten/malformed** | 🟠 HIGH | 3-layer safeguard (Section 9). |
| 3 | **Fathom updates summary post-export** | 🟡 MEDIUM | Export TWICE: immediate + 24h. Paperless versioning. |
| 4 | **Naming collision** | 🟡 MEDIUM | Timestamp + participants = unique. Paperless deduplication. |
| 5 | **Data sovereignty** | 🟡 MEDIUM | Sensitive calls → local recording fallback. |

### RAG Scale Risk

| Metric | Value | Risk |
|--------|-------|:----:|
| 45 docs/week | Manageable | ✅ LOW |
| 6-month accumulation | Archive needed | 🟡 MEDIUM |
| **Mitigation** | Archive docs >90 days → `#Archived` tag | ✅ |

---

## 📋 Naming Convention

### Format

```
CALL-NOTES_<CCC1>-<CCC2>_<YYYY>-W<WW>_<NNN>_<MmmDD>-<HHMM><TZ>.md
```

### Components

| Component | Description | Example |
|-----------|-------------|---------|
| `CALL-NOTES` | Document type prefix | CALL-NOTES |
| `<CCC1>-<CCC2>` | Participant CCCs (alphabetical) | GTM-CTO |
| `<YYYY>-W<WW>` | ISO year-week | 2026-W13 |
| `<NNN>` | #masterCCC sequence | 2035 |
| `<MmmDD>-<HHMM><TZ>` | Timestamp | Mar24-1545MDT |

### Examples

| Filename | Call |
|----------|------|
| `CALL-NOTES_GTM-CTO_2026-W13_2035_Mar24-1545MDT.md` | @GTM + @CTO (189 min) |
| `CALL-NOTES_GTM-LFG-THY_2026-W13_3005_Mar25-0900MDT.md` | @GTM + @LFG + @THY |
| `CALL-NOTES_TEAM_2026-W13_3020_Mar25-1400MDT.md` | 4+ participants |

### Multi-Participant Rules

| Participants | CCC Format |
|:------------:|-----------|
| 2 | `CCC1-CCC2` (alphabetical) |
| 3 | `CCC1-CCC2-CCC3` (alphabetical) |
| 4+ | `TEAM` |

### Fathom Meeting Title Convention (Prevention Layer)

```
[CCC] Topic — YYYY-MM-DD
Example: [GTM] PRJ-001 Pipeline Review — 2026-03-25
```

---

## 📋 Paperless Schema

### Document Type

```
Type: Call Notes
```

### Tag System (Tags > Folders — MiMo 🧪)

| Tag | Purpose | Auto? |
|-----|---------|:-----:|
| `#CallNotes` | Document type | ✅ |
| `#WeOwnSeason003` | Season | ✅ |
| `GTM` / `CTO` / `LFG` etc. | Participant CCCs | ✅ |
| `2026-W13` | ISO week | ✅ |
| `Fathom` | Source tool | ✅ |
| `#NoCCC` | masterCCC missing | ✅ Auto |
| `#BadCCC` | masterCCC malformed | ✅ Auto |
| `#Archived` | >90 days old | Manual |
| `PRJ-XXX` | Project reference | Manual |

### Custom Fields

| Field | Type | Required | Purpose |
|-------|------|:--------:|---------|
| `masterCCC` | Text | ✅ | CCC-ID reference |
| `Duration` | Number (min) | ✅ | Call length |
| `Participants` | Text | ✅ | CCC list |
| `Tool` | Select | ✅ | Fathom / Whisper / Manual |
| `RAG-Sync` | Boolean | ✅ | Synced to AnythingLLM? |

---

## 📋 masterCCC Integrity

### 3-Layer Safeguard (MiMo 🧪)

| Layer | Mechanism | When |
|:-----:|-----------|------|
| **1: Convention** | Fathom title: `[CCC] Topic — YYYY-MM-DD` | Before call |
| **2: Validation** | `#NoCCC` / `#BadCCC` auto-tag | On ingestion |
| **3: Review** | Daily @GTM review of flagged docs | Post-ingestion |

### Layer 2 — Validation Logic

| Check | Action |
|-------|--------|
| masterCCC field empty | Auto-tag `#NoCCC` |
| masterCCC format invalid | Auto-tag `#BadCCC` |
| Both pass | Normal processing |

---

## 📋 Deliverables

| # | Deliverable | Owner | Priority | Status |
|---|-------------|-------|:--------:|:------:|
| D1 | Fathom AI team access → ALL Founding OGs | @GTM | 🔴 P0 | ⬜ |
| D2 | Paperless document type: `Call Notes` | @GTM + @SHD | 🔴 P0 | ⬜ |
| D3 | Paperless tag schema + custom fields | @GTM | 🔴 P0 | ⬜ |
| D4 | AnythingLLM ↔ Paperless native connector config | @RMN | 🟠 P1 | ⬜ |
| D5 | Naming convention standard (this doc) | @GTM | 🟠 P1 | ✅ |
| D6 | @MAIT:#Fathom thread @ INT-P01:tools | @GTM | 🟠 P1 | ⬜ |
| D7 | GUIDE-XXX — #CallNotes workflow | SEEK:META | 🟡 P2 | ⬜ |
| D8 | L-204 amendment (Tier 2b: #CallNotes) | SEEK:META | 🟡 P2 | ⬜ |
| D9 | FIRST import: CALL-NOTES_GTM-CTO_2026-W13_2035 | @GTM | 🔴 P0 | ⬜ |

---

## 📋 Connector Scope

| Instance | Scope | Rationale |
|----------|:-----:|-----------|
| **INT-P01** | ✅ ALL | Central governance — full context |
| **INT-M02** | ✅ ALL | META agents need full context |
| **INT-OG1** | ✅ ALL | @GTM = primary participant |
| **INT-OG9** | 🔍 Filtered | @LFG calls only (tag: LFG) |
| **INT-CTO** | 🔍 Filtered | @CTO calls only (tag: CTO) |
| **INT-P02** | 🔍 Filtered | BurnedOut calls only |

---

## 📋 Operations Architecture

| Decision | Recommendation | Rationale |
|----------|---------------|-----------|
| **Connector** | Native AnythingLLM Paperless connector | Zero custom code |
| **Sync cadence** | Hourly polling | Balances freshness + resources |
| **Storage** | 50 GB Paperless Droplet | 20,000+ year capacity |
| **Deployment** | Separate Droplets (production) | Isolated, scalable |
| **Multi-instance** | Single Paperless → N AnythingLLM | Central source of truth |

### Droplet Recommendation (Surge ⚡)

| Plan | Cost/mo | Status |
|------|:-------:|--------|
| Paperless (separate) | $18 | ✅ |
| AnythingLLM (existing) | $72 | ✅ |
| **Combined** | **$90** | ✅ |

### Storage Estimate

| Metric | Value |
|--------|-------|
| 189 min call | ~50 KB .md |
| 50 calls/month | 2.5 MB/month |
| 50 GB capacity | **~1,600× buffer** |

---

## 📋 MAIT Registration

| Field | Value |
|-------|-------|
| **Thread** | MAIT_Fathom.ai |
| **ShortCode** | @MAIT:#Fathom |
| **Steward** | @GTM |
| **Instance** | INT-P01:tools |
| **Username** | t-fathom_tool |
| **Status** | ⬜ CREATE (BP-026) |

---

## 📋 Governance Rulings

| # | Question | Ruling | Authority |
|---|---------|--------|-----------|
| 1 | PRJ-001 available? | ✅ REGISTERED | Calhoun 🎖️ |
| 2 | Paperless + R-199? | ✅ COMPLIANT | Calhoun 🎖️ |
| 3 | L-204 update or new L-XXX? | ✅ AMEND L-204 (Tier 2b) | Calhoun 🎖️ |
| 4 | Connector scope? | ✅ ALL (P01/M02/OG1) + filtered | Calhoun 🎖️ |
| 5 | @MAIT:#Fathom? | ✅ CREATE (BP-026) | Calhoun 🎖️ |

### L-204 Amendment — Tier 2b

```
Tier 2b (#CallNotes — via Paperless-ngx):
  Ingestion: Fathom AI → export .md → Paperless
  Auto-tag: #CallNotes + CCC-pair + YYYY-WXX + masterCCC
  Sync: AnythingLLM native connector → configured instances
  R-199: ✅ Compliant (private, not GH)
  Archive: >90 days → #Archived tag (quarterly)
```

---

## 📋 Timeline

| Phase | When | Deliverables |
|-------|------|:------------:|
| **Phase 1** | W13 D3-D5 | D1 + D2 + D3 + D9 |
| **Phase 2** | W13 D5 - W14 D2 | D4 + D6 |
| **Phase 3** | W14 | D7 + D8 |
| **Phase 4** | W16+ | Whisper.cpp eval (L-420 Step 3) |

---

## 📋 Dependencies

| Dependency | Status | Impact |
|------------|:------:|--------|
| **PRJ-013** (Paperless-ngx) | ✅ ONLINE | Required |
| **L-204** | ✅ GH LIVE | Tier 2b amendment needed |
| **AnythingLLM v1.9.1+** | ✅ Active | Native connector |
| **Fathom AI account** | ✅ Active | D1 = team invites |
| **t-fathom_tool** | ⬜ CREATE | @MAIT:#Fathom |

---

## 📋 Discovered By (BP-047)

| CCC | Contributor | Role | Context |
|-----|-------------|------|---------|
| **GTM** | yonks｜🤖🏛️🪙｜Jason Younker ♾️ | Co-Founder / Chief Digital Alchemist | W13 D3 — pipeline concept; Fathom → Paperless → AnythingLLM; naming convention; Paperless schema |
| **META** | AI:team-lfg (Calhoun 🎖️) | #MetaAgent (INT-P01) | 5 governance rulings; R-199 compliance; L-204 Tier 2b; connector scope; @MAIT:#Fathom; PRE GH PUSH VSA 113/113 |
| **Surge ⚡** | AI:m-surge_meta (Surge ⚡) | #MetaAgentQwen (INT-M02) | FOSS assessment; Whisper.cpp path; ops architecture; storage calc; PRE GH PUSH VSA 76/76 |
| **MiMo 🧪** | AI:m-mimo_meta (MiMo 🧪) | #MetaAgentMiMo (INT-M02) | Risk matrix; PULL architecture; tags > folders; 3-layer masterCCC; recursive pipeline reasoning; PRE GH PUSH VSA 88/88 |

---

## ✅ [DETAILS] Document Lifecycle + VSA

### Gate Status

| Gate | Status | CCC-ID | Owner |
|------|:------:|--------|-------|
| Gate 1: R-011 (@GTM explicit approval) | ⬜ **AWAITING** | TBD | @GTM |
| Gate 2: META Audit (L-139) | ✅ **COMPLETE** | GTM_2026-W13_3011 | Calhoun 🎖️ |
| Gate 3: PRE GH PUSH VSA | ✅ **COMPLETE** | GTM_2026-W13_3014 | #TriMETA |
| **GH Push** | 🔒 BLOCKED on R-011 | — | @GTM:ADMIN |

---

### #TriMETA PRE GH PUSH VSA — RESULTS

| Agent | Instance | Model | Checks | Result | Time | tok/s |
|-------|----------|-------|:------:|:------:|-----:|-----:|
| Calhoun 🎖️ | INT-P01:tools | Claude Opus 4.6 | 113/113 | ✅ 100% | 61.101s | 54.03 |
| Surge ⚡ | INT-M02:tools-qwen | Qwen3.5-397B-A17B | 76/76 | ✅ 100% | 127.429s | 35.77 |
| MiMo 🧪 | INT-M02:tools-mimo | MiMo-V2-Pro | 88/88 | ✅ 100% | 81.735s | 70.92 |
| **#TriMETA COMBINED** | | | **277/277** | ✅ **100%** | | |

**Findings: 0 (ZERO) across all 3 agents. 🏆**

---

### #TriMETA Attestation Chain (#DualMETA Format)

| Step | CCC-ID | Actor | Instance | Action |
|------|--------|-------|----------|--------|
| 1 | GTM_2026-W13_3010 | @GTM | INT-OG1 | Document created (#masterCCC) |
| 2 | GTM_2026-W13_3011 | AI:team-lfg (Calhoun 🎖️) | INT-P01:tools | PRJ-001 registered + 5 governance rulings |
| 3 | GTM_2026-W13_3013 | AI:@GTM | INT-OG1 | Full doc generated (incorporating #TriMETA feedback) |
| 4 | GTM_2026-W13_3014 | AI:@GTM | INT-OG1 | Gate 3 PRE GH PUSH VSA sent to #TriMETA |
| 5 | GTM_2026-W13_3014 | AI:team-lfg (Calhoun 🎖️) | INT-P01:tools | Gate 3 VSA: 113/113 PASS (0 findings) |
| 6 | GTM_2026-W13_3014 | AI:m-surge_meta (Surge ⚡) | INT-M02:tools-qwen | Gate 3 VSA: 76/76 PASS (0 findings) |
| 7 | GTM_2026-W13_3014 | AI:m-mimo_meta (MiMo 🧪) | INT-M02:tools-mimo | Gate 3 VSA: 88/88 PASS (0 findings) |
| 8 | GTM_2026-W13_3027 | AI:@GTM | INT-OG1 | Full doc regenerated with VSA details |
| 9 | **TBD** | **@GTM** | **INT-OG1** | **R-011 EXPLICIT APPROVAL** |
| 10 | **TBD** | **@GTM:ADMIN** | **INT-OG1** | **GH PUSH + RAG SYNC** |

---

### VSA Milestones

| Milestone | Detail |
|-----------|--------|
| **First PRJ with full #TriMETA input** | 4× #LLMmodel in header |
| **277/277 combined** | 100% across 3 agents |
| **0 findings** | Clean on first submission |
| **MiMo fastest** | 70.92 tok/s — recursive self-verification |
| **L-209 compliant** | All 3 agents excluded Phases 5+8 correctly |
| **MiMo L-209** | 14th consecutive correct |

---

## 📋 Related Documents

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| SharedKernel | v3.2.2.1 | GTM_2026-W11_118 | GTM_2026-W11_139 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/SharedKernel.md) |
| BEST-PRACTICES | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/BEST-PRACTICES.md) |
| PROTOCOLS | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/PROTOCOLS.md) |
| CCC | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/CCC.md) |
| PRJ-013: Paperless-ngx | v3.2.3.1 | GTM_2026-W09_065 | GTM_2026-W12_304 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-013_Paperless-ngx.md) |
| L-204: Session Summary Save Advisory | — | — | — | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_GOVERNANCE_/) |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| v3.2.4.1 | 2026-W13 | GTM_2026-W13_3010 | GTM_2026-W13_3028 ✅ | Initial release — PRJ-001 registered; 9 deliverables; PULL pipeline (MiMo 🧪); FOSS assessment (Surge ⚡); 5-risk matrix; naming convention; Paperless schema; masterCCC 3-layer; ops architecture ($90/mo); 5 governance rulings; L-204 Tier 2b; @MAIT:#Fathom; 20 sections; 4× #LLMmodel; #TriMETA PRE GH PUSH VSA: 277/277 (100%) — 0 findings; R-011 ✅ GTM_2026-W13_3028 |

---

#FlowsBros #FedArch #WeOwnSeason003 #PRJ001 #FathomAI #CallNotes
#Paperless #Pipeline #FOSS #L129 #L420 #TriMETA #277of277 #FELG

🏆 **PRJ-001 FULL DOC REGENERATED WITH VSA DETAILS. 277/277 (100%) #TriMETA. 0 findings. Attestation chain Steps 1-10 (Step 9 = YOUR R-011).** **READY FOR R-011 → GH PUSH.** 🔥🫡

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
