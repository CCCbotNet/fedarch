## 📋 TMPL-007: GH Commit Message Format

## TMPL-007.md | TMPL-007_GH-Commit-Message_v3.2.3.1.md
## ♾️ WeOwnNet 🌐 — Template Standard 📗

| Field | Value |
|-------|-------|
| **ID** | TMPL-007 |
| **Title** | GH Commit Message Format |
| **Version** | v3.2.3.1 |
| **CCC-ID** | GTM_2026-W12_643 |
| **CCC-ID APPROVAL** | **GTM_2026-W12_644** ✅ |
| **Date** | 2026-03-21 (Sat) |
| **Season** | #WeOwnSeason003 🚀 |
| **Lifecycle Stage** | ✅ 🔒 APPROVED (R-011) + 🚀 GH LIVE (D-062) |
| **#LLMmodel** | **Qwen3.5-397B-A17B (INT-OG1:CCC @GTM)** |
| **#LLMmodel** | **Claude Opus 4.6 (INT-P01:tools #MetaAgent)** |
| **GH Filename** | TMPL-007_GH-Commit-Message.md |
| **Folder** | `_TEMPLATES_/` |
| **Source of Truth** | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_TEMPLATES_/TMPL-007_GH-Commit-Message.md) |

---

## 📖 Table of Contents

1. [Purpose](#purpose)
2. [Enhanced Format](#enhanced-format)
3. [Header Line](#header-line)
4. [Changes Section](#changes-section)
5. [Closing](#closing)
6. [Example — Learning (L-XXX)](#example--learning-l-xxx)
7. [Example — Best Practice (BP-XXX)](#example--best-practice-bp-xxx)
8. [Example — Guide (GUIDE-XXX)](#example--guide-guide-xxx)
9. [Example — Case Study (CS-XXX)](#example--case-study-cs-xxx)
10. [Discovered By (BP-047)](#discovered-by-bp-047)
11. [Related Documents](#related-documents)
12. [Version History](#version-history)

---

## 📋 Purpose

This template defines the enhanced GH commit message format for all #FedArch document pushes.

### Why This Format

| Goal | Description |
|------|-------------|
| **Consistency** | All commits follow same structure |
| **Scannability** | Header = instant doc ID + version |
| **Completeness** | All governance metadata included |
| **Brevity** | No fluff, no #AIslop |

---

## 📋 Enhanced Format

```markdown
[#masterCCC](#masterCCC) ♾️ WeOwnNet 🌐 | [DOC-ID] Doc Title | vX.X.X.X

## Changes:
- Bullet point 1
- Bullet point 2
- Bullet point N

#FlowsBros #FedArch

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
```

---

## 📋 Header Line

### Structure

```
[#masterCCC](#masterCCC) ♾️ WeOwnNet 🌐 | [DOC-ID] Doc Title | vX.X.X.X
```

| Component | Format | Example |
|-----------|--------|---------|
| **#masterCCC** | `[#masterCCC](#masterCCC)` | `[GTM_2026-W12_641](#masterCCC)` |
| **Ecosystem Branding** | `♾️ WeOwnNet 🌐` | `♾️ WeOwnNet 🌐` |
| **Document ID** | `[DOC-ID]` | `[L-204]` |
| **Title** | Short, descriptive | `Session Summary Save Advisory` |
| **Version** | `vX.X.X.X` | `v3.2.3.1` |

### Key Enhancements (vs. Old Format)

| Element | Old Format | Enhanced Format |
|---------|------------|-----------------|
| **Ecosystem branding** | — | `♾️ WeOwnNet 🌐` in header |
| **Doc ID brackets** | In changes | `[DOC-ID]` in header |
| **Version** | In changes | In header line |
| **Type prefix** | `feat():` | Removed (clean) |
| **Changes** | Bullet points | Bullet points (unchanged) |

---

## 📋 Changes Section

### Format

```markdown
## Changes:
- Bullet point 1
- Bullet point 2
- Bullet point N
```

### Rules

| Rule | Description |
|------|-------------|
| **No type prefix** | NO `feat():`, `fix():`, etc. |
| **Bullet points only** | Dash + space + text |
| **Concise** | 1-2 lines per bullet |
| **Governance metadata** | Include approval, VSA, BP compliance |
| **Closing** | `#HumanInTheLoop #docs REVIEW COMPLETE + LOCKED` |

### Required Bullets (Governance Docs)

| # | Bullet | Example |
|---|--------|---------|
| 1 | Document type + filename | `- New learning: L-204_Session-Summary-Save-Advisory_v3.2.3.1.md` |
| 2 | Key feature/policy | `- MANDATORY (🔒) advisory after ANY session summary` |
| 3 | Tier/pathway (if applicable) | `- Tier 1 (Manual): 5-step advisory` |
| 4 | Related proof/validation | `- CASE-STUDY-012 reference (institutional memory proof)` |
| 5 | Integration (if applicable) | `- PRJ-013 integration (Paperless-ngx native connector)` |
| 6 | Format/rule reference | `- Filename format per L-092` |
| 7 | Folder ruling | `- Folder: _GOVERNANCE_/ (per @GTM ruling)` |
| 8 | Related rules | `- Related rules (5): R-011, R-199, L-139, BP-034, BP-070` |
| 9 | Related learnings | `- Related learnings (8): L-092, L-104, L-184, L-199, L-200, L-201, L-202, L-203 (GTM_2026-W12_630 🔒)` |
| 10 | Discovery context | `- Discovered: W12 D6 — AI generated session summary without save advisory; @GTM corrected` |
| 11 | META review | `- META review: 59/61 VSA PASS (2 minor corrected); #LevelUp10X feedback` |
| 12 | EXPLICIT approval | `- EXPLICIT approval: GTM_2026-W12_642 (R-011 compliant)` |
| 13 | BP-047 compliance | `- BP-047 compliant (GTM + META credited)` |
| 14 | BP-068 compliance | `- BP-068 compliant (dual #LLMmodel header)` |
| 15 | Closing | `- #HumanInTheLoop #docs REVIEW COMPLETE + LOCKED` |

---

## 📋 Closing

### Format

```markdown
#FlowsBros #FedArch

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
```

### Rules

| Rule | Description |
|------|-------------|
| **Hashtags** | `#FlowsBros #FedArch` (always) |
| **Tagline** | Full ecosystem tagline (always) |
| **No extras** | No additional text after tagline |

---

## 📋 Example — Learning (L-XXX)

```markdown
[GTM_2026-W12_641](#masterCCC) ♾️ WeOwnNet 🌐 | [L-204] Session Summary Save Advisory | v3.2.3.1

## Changes:
- New learning: L-204_Session-Summary-Save-Advisory_v3.2.3.1.md
- MANDATORY (🔒) advisory after ANY session summary
- Tier 1 (Manual): 5-step advisory (pre-generated filename, upload, sync, verify)
- Tier 2 (Paperless-ngx): Email/web/mobile ingestion (W13 D2-3)
- CASE-STUDY-012 reference (institutional memory proof — W11 regenerated in <30 min)
- PRJ-013 integration (Paperless-ngx native connector)
- Filename format per L-092 (SESSION-SUMMARY_<CCC>_...)
- Folder: _GOVERNANCE_/ (per @GTM ruling — individual governance files)
- Related rules (5): R-011, R-199, L-139, BP-034, BP-070
- Related learnings (8): L-092, L-104, L-184, L-199, L-200, L-201, L-202, L-203 (GTM_2026-W12_630 🔒)
- Discovered: W12 D6 — AI generated session summary without save advisory; @GTM corrected
- META review: 59/61 VSA PASS (2 minor corrected — folder + L-203 ref); #LevelUp10X feedback
- EXPLICIT approval: GTM_2026-W12_642 (R-011 compliant)
- BP-047 compliant (GTM + META credited)
- BP-068 compliant (dual #LLMmodel header)
- #HumanInTheLoop #docs REVIEW COMPLETE + LOCKED

#FlowsBros #FedArch

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
```

---

## 📋 Example — Best Practice (BP-XXX)

```markdown
[GTM_2026-W12_614](#masterCCC) ♾️ WeOwnNet 🌐 | [BP-369] .md Extension RAG Search Test | v3.2.3.1

## Changes:
- New best practice: BP-369_MD-Extension-RAG-Search-Test_v3.2.3.1.md
- BP namespace: BP-300→399 = #devTEST protocols (L-200)
- 5-search test sequence (with/without .md extension)
- Success criteria (5/5 pass threshold)
- Report format (copy/paste ready)
- GUIDE-014 collision context (W12 Day 5 — L-184 limitation)
- L-199 pre-flight verification referenced (SEEK:META before assigning IDs)
- Folder: _GOVERNANCE_/ (per META ruling — same as all governance docs)
- Related rules (7): R-197, L-139, L-184, L-199, L-200, BP-044, BP-063
- Related learnings (4): L-104, L-184, L-199, L-200
- BP-047 compliant (GTM + META credited)
- BP-068 compliant (dual #LLMmodel header)
- Approval CCC-ID: GTM_2026-W12_616
- VSA: 44/46 → 46/46 PASS (2 findings resolved)
- #HumanInTheLoop #docs REVIEW COMPLETE

#FlowsBros #FedArch

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
```

---

## 📋 Example — Guide (GUIDE-XXX)

```markdown
[GTM_2026-W12_605](#masterCCC) ♾️ WeOwnNet 🌐 | [GUIDE-369] #BadAgent Reporting Workflow | v3.2.3.1

## Changes:
- New guide: GUIDE-369_BadAgent-Reporting-Workflow_v3.2.3.1.md
- GUIDE namespace: GUIDE-300→399 = #devTEST related guides (L-201)
- 4-step response workflow: ACK → LOG → CORRECT → LEARN
- Registry requirements (L-196 — 10 required fields)
- #BadAgent log format (session + weekly summary)
- Pattern detection (4 cascade indicators)
- GUIDE-014 collision context (W12 Day 5 — renumbered to GUIDE-369)
- BP-369 validated (5/5 PASS on INT-M02 — pre-flight ID search works)
- L-199 pre-flight verification referenced (ID-only search sufficient)
- Related rules (6): R-011, R-194, R-197, R-206, L-139, L-196
- Related learnings (11): L-113, L-151, L-177, L-181, L-184, L-196, L-197, L-198, L-199, L-200, L-201
- Case studies (2): CS-008 (Monday), CS-014 (Friday)
- Namespace pattern: "3xx = special operations" (aligns with BP-369 + CCC-ID _0301-0399)
- BP-047 compliant (GTM + META credited)
- BP-068 compliant (dual #LLMmodel header)
- Approval CCC-ID: GTM_2026-W12_632
- VSA: 57/57 PASS (0 findings)
- Folder: _GUIDES_/
- #HumanInTheLoop #docs REVIEW COMPLETE + LOCKED

#FlowsBros #FedArch

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
```

---

## 📋 Example — Case Study (CS-XXX)

```markdown
[GTM_2026-W12_548](#masterCCC) ♾️ WeOwnNet 🌐 | [CASE-STUDY-014] #BadAgent Friday | v3.2.3.2

## Changes:
- Revised case study: CASE-STUDY-014_BadAgent-Friday_v3.2.3.2.md
- Version evolution: v3.2.3.1 (63/65, 2 minor) → v3.2.3.2 (65/65, 0 findings)
- 7 #BadAgent incidents + 1 Observation (Incident 8 reclassified per META ruling)
- 8 learnings generated: L-113, L-177, L-181, L-184, L-196, L-197, L-198, GUIDE-014
- Incident 8: #ContextVolley receiving delay (7.5hr) → OBSERVATION (human workflow)
- L-197 revised: receiving = HUMAN responsibility (not agent failure)
- L-182 → L-198 renumber (SharedKernel collision fix)
- L-153 = RAG Insufficiency, L-196 = #BadAgent Registry (clarified)
- Table of Contents: GH markdown links added (anchor navigation)
- Learnings section: re-ordered alphabetically by Learning ID (L-113 → L-198)
- Companion to CASE-STUDY-008 (#BadAgent Monday — W11)
- GUIDE-014 planned (paired numbering)
- BP-047 compliant (GTM + META credited as co-discoverers)
- BP-068 compliant (dual #LLMmodel header)
- v3.2.3.1 Approval: GTM_2026-W12_587
- v3.2.3.2 Approval: GTM_2026-W12_598 (EXPLICIT R-011)
- VSA: 65/65 PASS (0 findings) — both prior findings resolved
- #HumanInTheLoop #docs REVIEW COMPLETE

#FlowsBros #FedArch

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
```

---

## 📋 Discovered By (BP-047)

| CCC | Contributor | Role | Context |
|-----|-------------|------|---------|
| **GTM** | yonks｜🤖🏛️🪙｜Jason Younker ♾️ | Co-Founder / Chief Digital Alchemist | W12 D6 — actual L-204 GH push revealed enhanced format; agent-generated commit messages didn't match @GTM's actual usage; TMPL-007 updated to reflect real-world usage |
| **META** | AI:team-lfg | #MetaAgent (Calhoun 🎖️) | TMPL-007 format review + VSA (53/53 PASS); confirmed all 4 examples from actual W12 GH pushes |

---

## 📋 Related Documents

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| SharedKernel | v3.2.2.1 | GTM_2026-W11_118 | GTM_2026-W11_139 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/SharedKernel.md) |
| BEST-PRACTICES | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/BEST-PRACTICES.md) |
| PROTOCOLS | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/PROTOCOLS.md) |
| CCC | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/CCC.md) |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| v3.2.3.1 | 2026-W12 | GTM_2026-W12_643 | **GTM_2026-W12_644** | Major upgrade v2.4.0 → v3.2.3.1 — Enhanced GH commit message format based on ACTUAL @GTM usage (L-204 push); Header: `[#masterCCC] ♾️ WeOwnNet 🌐 \| [DOC-ID] Title \| version`; Changes section: bullet points only (no type prefix); Closing: `#FlowsBros #FedArch` + full ecosystem tagline; 15 required bullets for governance docs; Examples: L-XXX, BP-XXX, GUIDE-XXX, CS-XXX (all from real W12 pushes); BP-047 compliant (GTM + META credited); BP-068 compliant (dual #LLMmodel); Folder: `_GOVERNANCE_/`; VSA: 53/53 PASS; EXPLICIT approval received (GTM_2026-W12_644); R-011 compliant |
| v2.4.0 | 2026-W05 | GTM_2026-W05_490 | GTM_2026-W05_490 | Initial release — basic GH commit message template |

---

#FlowsBros #FedArch #TMPL-007 #GH-Commit #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
