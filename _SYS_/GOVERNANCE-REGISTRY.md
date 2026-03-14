# GOVERNANCE-REGISTRY.md

## 📋 GOVERNANCE-REGISTRY_v3.2.2.1.md
## ♾️ WeOwnNet 🌐 — Governance Item Index

| Field | Value |
|-------|-------|
| Document | GOVERNANCE-REGISTRY.md |
| Version | 3.2.2.1 |
| **#masterCCC** | **GTM_2026-W11_541** |
| **Approval** | **GTM_2026-W11_606** |
| **#LLMmodel** | **Qwen3.5-397B-A17B (AI.YonksTEAM.xyz @GTM)** |
| **#LLMmodel** | **Claude Opus 4.6 (meta.WeOwn.tools #MetaAgent)** |
| Lifecycle Stage | ✅ 🔒 APPROVED + 🚀 GH LIVE (D-062) |
| Created | 2026-03-14 (W11 Day 6) |
| Season | #WeOwnSeason003 🚀 |
| Source of Truth | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/GOVERNANCE-REGISTRY.md) |
| Tags | #Governance #Registry #PRJ-037 |
| Audience | **Internal + External** — Core TEAM + #FedArch participants |
| Purpose | Authoritative index of ALL governance items (R/D/L/BP) + current structure |

---

## 📖 Table of Contents

1. [Overview](#-overview)
2. [Current Structure (R-204 Option)](#-current-structure)
3. [Rules Registry (R-XXX)](#-rules-registry)
4. [Definitions Registry (D-XXX)](#-definitions-registry)
5. [Learnings Registry (L-XXX)](#-learnings-registry)
6. [Best Practices Registry (BP-XXX)](#-best-practices-registry)
7. [Individual Files Status](#-individual-files-status)
8. [PRJ-037 Progress](#-prj-037-progress)
9. [Related Documents](#-related-documents)
10. [Version History](#-version-history)

---

## 📋 Overview

GOVERNANCE-REGISTRY.md is the **single source of truth** for all governance items in the ♾️ WeOwnNet 🌐 ecosystem. It indexes:

- **Rules** (R-001 → R-217)
- **Definitions** (D-001 → D-069+)
- **Learnings** (L-001 → L-170+)
- **Best Practices** (BP-001 → BP-078)

### Why This Exists

| Problem | Solution |
|---------|----------|
| Governance spread across 4 #PinnedDocs | Single index links everything |
| PRJ-037 splitting docs into ~295 files | Registry tracks which files exist |
| R-204 needs structure-agnostic language | Registry defines current structure |
| ISC Check #3 needs verification method | Registry + query test = audit |

### Key Principle

> **R-204 says "governance accessible." Registry says "here's how."** Change structure → update registry → R-204 still passes. No rule amendment needed.

---

## 📋 Current Structure (R-204 Option)

| Field | Value |
|-------|-------|
| **R-204 Option** | **Option A** (Consolidated #PinnedDocs) |
| **Status** | Current until PRJ-037 Phase 4 complete |
| **Transition** | W13 D1-2 (after L-171 amendments complete) |

### Option A: Consolidated (CURRENT)

| Doc | Location | PIN? | Size |
|-----|----------|------|------|
| SharedKernel.md | `_SYS_/` | ✅ YES | ~80KB |
| BEST-PRACTICES.md | `_SYS_/` | ✅ YES | ~60KB |
| PROTOCOLS.md | `_SYS_/` | ✅ YES | ~30KB |
| CCC.md | `_SYS_/` | ✅ YES | ~15KB |

### Option B: Split (PRJ-037 — FUTURE)

| Doc | Location | PIN? | Size | ETA |
|-----|----------|------|------|-----|
| SharedKernel-Rules.md | `_SYS_/` | ✅ YES | ~15KB | W13 D1 |
| SharedKernel-Definitions.md | `_SYS_/` | ✅ YES | ~20KB | W13 D1 |
| BEST-PRACTICES-Part1.md | `_SYS_/` | ✅ YES | ~25KB | W13 D1 |
| BEST-PRACTICES-Part2.md | `_SYS_/` | ✅ YES | ~25KB | W13 D1 |
| PROTOCOLS.md | `_SYS_/` | ✅ YES | ~10KB | W13 D1 |
| CCC.md | `_SYS_/` | ✅ YES | ~5KB | W13 D1 |
| **Individual Files** | `_GOVERNANCE_/` | ❌ RAG | ~295 files | W12-W14 |

### Option C: RAG-Embedded (INT-OG8)

| Field | Value |
|-------|-------|
| **Instance** | INT-OG8 (AI.RomanDiD.xyz) |
| **Pinned Docs** | 0 (all un-pinned) |
| **RAG Retrieval** | Semantic on reference |
| **Context Usage** | ~10-15% |
| **Message Retention** | 100+ messages |
| **Approval** | GTM_2026-W11_315 (R-204 Option C) |

---

## 📋 Rules Registry (R-XXX)

| ID | Title | Location | Individual File? | Status |
|----|-------|----------|-----------------|--------|
| R-011 | #OnlyHumanApproves | SharedKernel.md | ⬜ TODO | 🔒 IMMUTABLE |
| R-044 | #ContextDensity | SharedKernel.md | ⬜ TODO | 🔒 IMMUTABLE |
| R-168 | CCC-ID tied to contributor | SharedKernel.md | ⬜ TODO | 🔒 LOCKED |
| R-169 | CCC-ID resets at ISO week | SharedKernel.md | ⬜ TODO | 🔒 LOCKED |
| R-181 | _001 = #WeeklySummary | SharedKernel.md | ⬜ TODO | 🔒 LOCKED |
| R-194 | CCC-ID only in CCC workspace | SharedKernel.md | ⬜ TODO | 🔒 IMMUTABLE |
| R-197 | Doc gen = #MetaAgent ONLY | SharedKernel.md | ⬜ TODO | 🔒 IMMUTABLE |
| R-201 | _002 = #WeeklyPlan | SharedKernel.md | ⬜ TODO | 🔒 LOCKED |
| R-202 | _003 = #WeeklyReflection | SharedKernel.md | ⬜ TODO | 🔒 LOCKED |
| R-204 | #HomeInstance #PinnedDocs | SharedKernel.md | ⬜ TODO (W12 D1) | 🔒 LOCKED (amendment pending) |
| R-205 | #GODx10xMODE IMMUTABLE | SharedKernel.md | ⬜ TODO | 🔒 IMMUTABLE |
| R-206 | ADMIN never generates CCC-ID | SharedKernel.md | ⬜ TODO | 🔒 IMMUTABLE |
| R-212 | Cross-instance CCC-ID deconfliction | SharedKernel.md | ⬜ TODO | 🔒 LOCKED |
| R-215 | VSA Lifecycle Gate | SharedKernel.md | ⬜ TODO | 🔒 LOCKED |
| R-217 | VSA Registry = AUTOMATIC + IMMUTABLE | SharedKernel.md | ⬜ TODO | 🔒 IMMUTABLE |

**Total Rules:** ~20 (R-001 → R-217)
**Individual Files:** 0/~20
**Priority:** 🟢 P3 (after D-XXX + L-XXX)

---

## 📋 Definitions Registry (D-XXX)

| ID | Title | Location | Individual File? | Status |
|----|-------|----------|-----------------|--------|
| D-016 | ADMIN | SharedKernel.md | ⬜ TODO | 🔒 LOCKED |
| D-017 | MANAGER | SharedKernel.md | ⬜ TODO | 🔒 LOCKED |
| D-018 | DEFAULT | SharedKernel.md | ⬜ TODO | 🔒 LOCKED |
| D-019 | Orchestrator Agent | SharedKernel.md | ⬜ TODO | 🔒 LOCKED |
| D-020 | User Agent | SharedKernel.md | ⬜ TODO | 🔒 LOCKED |
| D-038 | MAIT ShortCode | SharedKernel.md | ⬜ TODO | 🔒 LOCKED |
| D-039 | #ContextBroadcast | SharedKernel.md | ⬜ TODO | 🔒 LOCKED |
| D-047 | #threadHEADER | SharedKernel.md | ⬜ TODO | 🔒 LOCKED |
| D-048 | #HomeInstance | SharedKernel.md | ⬜ TODO | 🔒 LOCKED |
| D-049 | #GODx10xMODE | SharedKernel.md | ⬜ TODO | 🔒 LOCKED |
| D-050 | CCC-ID Authority | SharedKernel.md | ⬜ TODO | 🔒 LOCKED |
| D-052 | ISC | SharedKernel.md | ⬜ TODO | 🔒 LOCKED |
| D-062 | Document Lifecycle | SharedKernel.md | ⬜ TODO | 🔒 LOCKED |
| D-063 | DRAFT CHECK | SharedKernel.md | ⬜ TODO | 🔒 LOCKED |
| D-064 | EXPECTED FAIL | SharedKernel.md | ⬜ TODO | 🔒 LOCKED |
| D-065 | #MemeLord | SharedKernel.md | ⬜ TODO | 🔒 LOCKED |
| D-066 | Operational Document | SharedKernel.md | ⬜ TODO | 🔒 LOCKED |
| **D-068** | **Attribution Matrix** | SharedKernel.md | ✅ **W12 D2** | 🔒 **LOCKED (W11_513)** |
| **D-069** | **#masterCCC** | SharedKernel.md | ✅ **W12 D2** | 🔒 **LOCKED (W11_527)** |

**Total Definitions:** ~70 (D-001 → D-069+)
**Individual Files:** 0/~70 (2 scheduled W12 D2)
**Priority:** 🔴 P0 (W12 D2-5)

---

## 📋 Learnings Registry (L-XXX)

### W11 Learnings (L-158 → L-173) — 🔴 P0

| ID | Title | Location | Individual File? | Status |
|----|-------|----------|-----------------|--------|
| L-158 | Pinning vs embedding (R-204 Option C) | SharedKernel.md | ⬜ TODO | 🔒 LOCKED |
| L-159 | agent-memory.txt = hidden RAG hazard | SharedKernel.md | ⬜ TODO | 🔒 LOCKED |
| L-160 | Org resilience (no individual names in ownership) | SharedKernel.md | ⬜ TODO | 🔒 LOCKED |
| L-161 | ⬜ Not in current SharedKernel | SharedKernel.md | ⬜ TODO | 🔒 LOCKED |
| L-162 | R-197 evolved: META reviews, not generates | SharedKernel.md | ⬜ TODO | 🔒 LOCKED |
| L-164 | OpenRouter 402 credit depletion | SharedKernel.md | ⬜ TODO | 🔒 LOCKED |
| L-166 | PRE GH PUSH VSA rigor (#LLMmodel + Related Docs) | SharedKernel.md | ⬜ TODO | 🔒 LOCKED |
| L-167 | Related Docs = part of generation | SharedKernel.md | ⬜ TODO | 🔒 LOCKED |
| L-168 | VSA Registry = automatic + immutable | SharedKernel.md | ⬜ TODO | 🔒 LOCKED |
| L-169 | CCC-ID Increment Per Response | SharedKernel.md | ⬜ TODO | 🔒 LOCKED |
| L-170 | #MetaAgent Attribution Required | SharedKernel.md | ⬜ TODO | 🔒 LOCKED |
| **L-171** | **Amend Before Split** | SharedKernel.md | ✅ **W12 D6** | 🔒 **LOCKED (W11_536)** |
| **L-173** | **#WeOwnVer Iteration Increment** | SharedKernel.md | ⬜ TODO | 🔒 **LOCKED (W11_555)** |

**W11 Total:** 14 learnings (L-158 → L-173)
**Individual Files:** 0/14 (L-171 scheduled W12 D6)
**Priority:** 🔴 P0 (W12 D6)

### W10 Learnings (L-100 → L-157) — 🟠 P1

| Count | Range | Individual Files? | Priority |
|-------|-------|-------------------|----------|
| 58 | L-100 → L-157 | ⬜ TODO | 🟠 P1 (W13 D1-3) |

### Legacy Learnings (L-001 → L-099) — 🟡 P2

| Count | Range | Individual Files? | Priority |
|-------|-------|-------------------|----------|
| ~99 | L-001 → L-099 | ⬜ TODO | 🟡 P2 (W13 D4-7) |

**Total Learnings:** ~171 (L-001 → L-173+)
**Individual Files:** 0/~171
**Priority:** 🔴 P0 (W11 first, then W10, then legacy)

---

## 📋 Best Practices Registry (BP-XXX)

| Range | Count | Individual Files? | Priority |
|-------|-------|-------------------|----------|
| BP-001 → BP-040 | ~40 | ⬜ TODO | 🟠 P1 (W13 D4-5) |
| BP-041 → BP-078 | ~38 | ⬜ TODO | 🟠 P1 (W13 D6-7) |
| **BP-080** | **1** | ❌ **MERGED into L-173** | ❌ **Not created** |

**Total Best Practices:** ~78 (BP-001 → BP-078)
**Individual Files:** 0/~78
**Priority:** 🟠 P1 (W13 D4-7)

---

## 📋 Individual Files Status

| Type | Total | Created | Remaining | % Complete |
|------|-------|---------|-----------|------------|
| **Rules (R-XXX)** | ~20 | 0 | ~20 | 0% |
| **Definitions (D-XXX)** | ~70 | 0 | ~70 | 0% |
| **Learnings (L-XXX)** | ~171 | 0 | ~171 | 0% |
| **Best Practices (BP-XXX)** | ~78 | 0 | ~78 | 0% |
| **TOTAL** | **~347** | **0** | **~347** | **0%** |

### Scheduled Individual Files (W12)

| File | Type | CCC-ID | Status |
|------|------|--------|--------|
| D-068_Attribution-Matrix.md | Definition | W12_XXX | ⬜ W12 D2 |
| D-069_masterCCC.md | Definition | W12_XXX | ⬜ W12 D2 |
| L-171_Amend-Before-Split.md | Learning | W12_XXX | ⬜ W12 D6 |

---

## 📋 PRJ-037 Progress

| Phase | Title | Timeline | Status |
|-------|-------|----------|--------|
| 0: R-204 + ISC Check #3 Amendment | W12 D1 | ⬜ TODO (L-171 blocks Phase 4) |
| 1: GOVERNANCE-REGISTRY.md | W12 D1 | ✅ **GH PUSH READY** |
| 2: Definitions (~70 files) | W12 D2-5 | ⬜ TODO |
| 3: W11 Learnings (14 files) | W12 D6 | ⬜ TODO |
| 4: Split #PinnedDocs | W13 D1-2 | ⬜ FUTURE (L-171 block) |
| 5: Remaining L-XXX + BP-XXX | W13 D3-7 | ⬜ FUTURE |
| 6: Paperless-ngx Upload | W14 | ⬜ FUTURE |

---

## 📋 Related Documents

### #PinnedDocs

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| **SharedKernel** | **v3.2.2.1** | GTM_2026-W11_118 | GTM_2026-W11_139 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/SharedKernel.md) |
| BEST-PRACTICES | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/BEST-PRACTICES.md) |
| PROTOCOLS | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/PROTOCOLS.md) |
| CCC | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/CCC.md) |

### PRJ-037

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| PRJ-037: Governance Individualization | v3.2.2.1 | GTM_2026-W11_529 | GTM_2026-W11_547 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-037_Governance-Individualization.md) |

### Learnings

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| L-171: Amend Before Split | — | GTM_2026-W11_534 | GTM_2026-W11_536 | ⬜ SharedKernel Cascade (W12) |

### Projects

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| PRJ-013: Paperless-ngx | v3.1.4.1 | GTM_2026-W09_065 | GTM_2026-W09_068 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-013_Paperless-ngx.md) |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| **v3.2.2.1** | **2026-W11** | **GTM_2026-W11_541** | **GTM_2026-W11_606** | Initial registry (FIRST PUBLICATION); R-XXX (~20), D-XXX (~70), L-XXX (~171), BP-XXX (~78) indexed; Current structure (Option A); PRJ-037 phases tracked; Individual files status (0/~347); D-068 + D-069 + L-171 scheduled W12; L-166 #LLMmodel headers added; L-167 Related Docs (BP-045); VSA PASS 37/37 (VSA_GTM_W11_558); **Approval corrected W11_547 → W11_606 (post-VSA)** |
| v3.2.2.1 | 2026-W11 | GTM_2026-W11_541 | GTM_2026-W11_547 | ❌ INVALID (pre-VSA approval) |

---

#FlowsBros #FedArch #Governance #Registry #PRJ-037 #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
