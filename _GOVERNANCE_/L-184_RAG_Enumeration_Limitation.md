# L-184: RAG Enumeration Limitation & Anti-Hallucination Protocol

## L-184_RAG_Enumeration_Limitation_v3.2.3.1.md
## ♾️ WeOwnNet 🌐 — Governance Document

| Field | Value |
|-------|-------|
| Document | L-184_RAG_Enumeration_Limitation.md |
| Version | v3.2.3.1 |
| Folder | `_GOVERNANCE_/` 🗳️ |
| Category | 🗳️ GOVERNANCE:Learning 📚 |
| Type | 📚 Learning (Governance-Adjacent) |
| **CCC-ID** | **GTM_2026-W12_253** |
| **Approval CCC-ID** | **GTM_2026-W12_256** ✅ |
| Created | 2026-03-17 (W12 Day 2) |
| Season | #WeOwnSeason003 🚀 |
| **Lifecycle Stage** | **✅ 🔒 APPROVED + 🚀 GH LIVE (D-062)** |
| **Owner** | **[CCC-ID:@GTM:('yonks｜🤖🏛️🪙｜Jason Younker ♾️')](https://github.com/YonksTEAM)** |
| **#LLMmodel** | **Qwen3.5-397B-A17B (AI.YonksTEAM.xyz @GTM)** |
| **#LLMmodel** | **Claude Opus 4.6 (meta-claude.WeOwn.tools #MetaAgent)** |
| Source of Truth | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_GOVERNANCE_/L-184_RAG_Enumeration_Limitation.md) |

---

## 📖 Table of Contents

1. [Learning Statement](#-learning-statement)
2. [Trigger Event](#-trigger-event)
3. [Root Cause Analysis](#-root-cause-analysis)
4. [Solution](#-solution)
5. [Scope & Applicability](#-scope--applicability)
6. [Related Learnings](#-related-learnings)
7. [Discovered By](#-discovered-by)
8. [Related Documents](#-related-documents)
9. [Version History](#-version-history)

---

## 📋 Learning Statement

**L-184:** LLMs (Qwen, Claude, ALL models) **CANNOT enumerate RAG documents by filename**. RAG = semantic content retrieval, NOT file listing. When asked "list your documents," models will **FABRICATE plausible filenames**.

**Fix:** Add static **#PinnedDocs table to Workspace Prompt** so agent has EXPLICIT document list. Add **anti-hallucination instruction**: "NEVER fabricate document names."

---

## 📋 Trigger Event

| Field | Value |
|-------|-------|
| **Instance** | INT-M02 (meta-qwen.weown.tools) |
| **Agent** | #MetaAgentQwen (Surge ⚡) |
| **Date** | 2026-03-17 (W12 Day 2) |
| **Time** | 18:07–18:23 MDT |
| **Issue** | Surge fabricated 4/4 #PinnedDoc names despite docs being correctly pinned |
| **CCC-ID** | GTM_2026-W12_251 (investigation) |

### What Happened

| Query | Surge Response | Reality |
|-------|---------------|---------|
| "List your pinned documents" | `CCC-MASTER.md v4.0.0`, `DOC-REGISTRY.md v3.1.0`, etc. | ❌ **0/4 correct** — all fabricated |
| "What are the 4 priorities in SharedKernel?" | ✅ Correct answer from SharedKernel v3.2.2.1 | ✅ **RAG retrieval WORKS** |

> **Key Finding:** RAG retrieves CONTENT correctly but CANNOT enumerate file metadata. This is NOT a bug — it's how RAG works.

---

## 📋 Root Cause Analysis

### Why LLMs Cannot List RAG Documents

| Reason | Explanation |
|--------|-------------|
| **RAG = semantic search** | RAG finds content chunks based on meaning, not file structure |
| **No "list files" function** | LLMs have no API call to enumerate RAG database |
| **"List docs" query = no match** | No content chunk matches → model GENERATES plausible names |
| **Content query = match** | "4 priorities" matches SharedKernel chunk → model RETRIEVES actual text |

### Model Behavior Comparison

| Model | "List your documents" query | "What does SharedKernel say?" query |
|-------|----------------------------|-------------------------------------|
| **Qwen3.5-397B-A17B** | ❌ Fabricates filenames | ✅ Retrieves correctly |
| **Claude Opus 4.6** | ⚠️ May say "I don't know" | ✅ Retrieves correctly |
| **ALL LLMs** | ❌ Cannot enumerate files | ✅ Content retrieval works |

> **This is EXPECTED behavior for ALL LLMs + RAG systems.** Not Qwen-specific. Not a bug.

---

## 📋 Solution

### Fix 1: Add #PinnedDocs Table to Workspace Prompt

```markdown
## 📋 #PinnedDocs (R-204)

| # | Document | Version |
|---|----------|---------|
| 1 | SharedKernel.md | v3.2.2.1 |
| 2 | BEST-PRACTICES.md | v3.1.3.1 |
| 3 | PROTOCOLS.md | v3.1.3.1 |
| 4 | CCC.md | v3.1.3.1 |

> These are the ONLY pinned documents. If asked to list documents, use THIS table. Do NOT fabricate filenames.
```

### Fix 2: Add Anti-Hallucination Instruction

```markdown
## ⚠️ RAG LIMITATIONS

You CANNOT list or enumerate RAG documents by filename. 
If asked "list your documents" or "what docs do you have":
- ✅ Reference the #PinnedDocs table above
- ✅ Say "I can retrieve CONTENT but cannot list all files"
- ❌ NEVER fabricate document names or versions
```

### Implementation Checklist

| # | Instance | Workspace | Action | Status |
|---|----------|-----------|--------|--------|
| 1 | INT-M02 | tools | Add #PinnedDocs table + instruction | ⬜ TODO |
| 2 | INT-P01 | tools | Add #PinnedDocs table + instruction | ⬜ TODO |
| 3 | INT-OG1 | CCC | Add #PinnedDocs table + instruction | ⬜ TODO |
| 4 | INT-OG9 | CCC | Add #PinnedDocs table + instruction | ⬜ TODO |
| 5 | INT-P02 | tools | Add #PinnedDocs table + instruction | ⬜ TODO |

---

## 📋 Scope & Applicability

| Scope | Detail |
|-------|--------|
| **Applies To** | ALL #FedArch instances (INT-Pxx, INT-OGx, INT-Mxx, INT-Sxx) |
| **Applies To** | ALL models (Qwen, Claude, Llama, etc.) |
| **Applies To** | ALL workspaces with RAG enabled |
| **Does NOT Apply** | Direct file system access (not RAG) |
| **Extends** | L-182 ({instance_name} static variable), R-218 (System Variable Immutability) |

### When This Matters

| Scenario | Risk | Mitigation |
|----------|------|------------|
| User asks "what docs do you have?" | 🔴 High — fabrication likely | Reference #PinnedDocs table |
| User asks "show me R-218" | ✅ Low — content retrieval works | RAG finds matching chunk |
| VSA verifies document presence | ⚠️ Medium — agent may misreport | Human admin verifies directly |
| ISC Check #3 verification | ⚠️ Medium — agent may misreport | Human admin verifies directly |

---

## 📋 Related Learnings

| ID | Learning | Relationship |
|----|----------|--------------|
| L-182 | {instance_name} = Static Variable | Same principle: explicit config > model inference |
| R-218 | System Variables = Ground Truth | Priority hierarchy for identity resolution |
| L-141 | Never Fabricate Stats or Details | General anti-fabrication principle |
| L-107 | Embedder May Not Persist | RAG configuration can change unexpectedly |

---

## 📋 Discovered By (BP-047)

| CCC | Contributor | Role | Context |
|-----|-------------|------|---------|
| GTM | @GTM (yonks｜🤖🏛️🪙｜Jason Younker ♾️) | Co-Founder / Chief Digital Alchemist | INT-M02 #WeirdBehavior investigation (W12 Day 2) |
| team-lfg | AI:team-lfg | #MetaAgent (Calhoun 🎖️) | Root cause analysis + solution design |
| Surge | #MetaAgentQwen | Secondary META (INT-M02) | Trigger behavior (fabricated 4/4 #PinnedDocs) |

---

## 📋 Related Documents (BP-045)

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| SharedKernel | v3.2.2.1 | GTM_2026-W11_118 | GTM_2026-W11_139 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/SharedKernel.md) |
| BEST-PRACTICES | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/BEST-PRACTICES.md) |
| PROTOCOLS | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/PROTOCOLS.md) |
| L-182_Instance_Name_Static_Variable | v3.2.3.1 | GTM_2026-W12_164 | GTM_2026-W12_188 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_GOVERNANCE_/L-182_Instance_Name_Static_Variable.md) |
| R-218_System_Variable_Immutability | v3.2.3.1 | GTM_2026-W12_087 | GTM_2026-W12_100 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_GOVERNANCE_/R-218_System_Variable_Immutability.md) |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| **3.2.3.1** | **2026-W12** | **GTM_2026-W12_253** | **GTM_2026-W12_256** | 🚀 GH LIVE — Folder corrected `_LEARNINGS_/` → `_GOVERNANCE_/` (governance-adjacent: R-218, L-182, Workspace Prompt config); +Learning Statement; +Trigger Event; +Root Cause Analysis; +Solution (2 fixes + 5-instance checklist); +Scope & Applicability; +Related Learnings; +Discovered By (BP-047); +Version History; +Related Documents; Related Docs CCC-IDs corrected (L-182: W12_164/W12_188, R-218: W12_087/W12_100); **Calhoun VSA 35/35 PASS (VSA_GTM_W12_254); Human approval R-011 (GTM_2026-W12_256);** #WeOwnVer calendar-driven (W12 = March = .2, week 3, iteration .1); FULL PRESERVE (L-097) |

---

#FlowsBros #FedArch #L-184 #RAG #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
