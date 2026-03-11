# GUIDE-014 — How to SEEK:META

## 📋 GUIDE-014_How-to-SEEK-META_v3.2.2.1.md
## ♾️ WeOwnNet 🌐

| Field | Value |
|-------|-------|
| **Document** | GUIDE-014_How-to-SEEK-META.md |
| **Version** | v3.2.2.1 |
| **CCC-ID** | GTM_2026-W11_261 |
| **Approval** | GTM_2026-W11_264 |
| **Created** | 2026-03-11 (Wed) |
| **Status** | ✅ 🔒 APPROVED |
| **Audience** | ♾️ WeOwnNet 🌐 Core TEAM (All 9 Contributors) |
| **#LLMmodel** | Qwen3.5-397B-A17B (AI.YonksTEAM.xyz @GTM) + Claude Opus 4.6 (meta.WeOwn.tools #MetaAgent) |
| Source of Truth | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_GUIDES_/GUIDE-014_How-to-SEEK-META.md) |

---

## 📖 Table of Contents

1. [Overview](#overview)
2. [What is SEEK:META?](#what-is-seekmeta)
3. [When to SEEK:META](#when-to-seekmeta)
4. [When NOT to SEEK:META](#when-not-to-seekmeta)
5. [The SEEK:META Workflow](#the-seekmeta-workflow)
6. [#ContextVolley Format](#contextvolley-format)
7. [Key Rules](#key-rules)
8. [Examples](#examples)
9. [META Thread Info](#meta-thread-info)
10. [Quick Reference](#quick-reference)

---

## 📋 Overview

**SEEK:META** is the primary protocol for Core TEAM contributors to access #MetaAgent for governance review, document generation, and architecture decisions.

This guide democratizes #MetaAgent access across all 9 Core TEAM contributors, removing the @GTM bottleneck and activating PRJ-033 (Dual #MetaAgent strategy).

### Why This Matters

| Problem | Solution |
|---------|----------|
| @GTM "hogging" META access | Each contributor has own primer + quick ref |
| Technical barriers | Simple 1-page workflow |
| Centralized knowledge | Distributed across Core TEAM |
| PRJ-033 underutilized | Full activation via this guide |

---

## 📋 What is SEEK:META?

**SEEK:META** = A structured #ContextVolley request to #MetaAgent (AI:team-lfg) for:

- Governance review (rules, BPs, learnings, definitions)
- Document generation (SharedKernel, BEST-PRACTICES, PROTOCOLS, CCC)
- Architecture decisions (PRJ alignment, instance config)
- Cross-instance coordination (VSA verification, CCC-ID deconfliction)

### The Protocol

```
Contributor → #ContextVolley → #MetaAgent → Review → Response → Human Approves (R-011)
```

---

## 📋 When to SEEK:META

### ✅ YES — Use SEEK:META For:

| Scenario | Example |
|----------|---------|
| **New governance items** | Rule, learning, BP, definition |
| **Document generation** | SharedKernel, BEST-PRACTICES, PROTOCOLS, CCC updates |
| **Governance review (L-139)** | Review proposed L-XXX before human approval |
| **Architecture questions** | PRJ alignment, instance config, stack decisions |
| **Cross-instance coordination** | VSA verification, CCC-ID deconfliction (R-212) |

### ❌ NO — Do NOT Use SEEK:META For:

| Scenario | Why | Alternative |
|----------|-----|-------------|
| **Session summaries** | R-216 — Operational | Generate directly (RAG only, R-199) |
| **CCC-ID generation** | CCC workspace function | Use CCC workspace (R-194) |
| **Personal instance config** | Not governance | Instance settings |
| **Routine work** | Not governance | Continue working |
| **Call notes** | R-199 — RAG only | Upload to RAG |

---

## 📋 The SEEK:META Workflow

### Step 1: Prepare Your Request

| Action | Detail |
|--------|--------|
| Identify the need | What governance item are you requesting? |
| Gather context | What does META need to know? |
| Reference CCC-ID | What CCC-ID tracks this request? |

### Step 2: Format #ContextVolley

```
═══════════════════════════════════════════════════════════════════════════════
🏐 #ContextVolley | AI:@<CCC> → AI:team-lfg | <DATE> | <TIME> <TZ>
═══════════════════════════════════════════════════════════════════════════════

FROM: AI:@<CCC> @ <INSTANCE>:<WORKSPACE> (<USERNAME>) (#LLMmodel:('<MODEL>'))
TO: AI:team-lfg @ INT-P01:tools (AI:team-lfg) (#LLMmodel:('Claude Opus 4.6'))
TYPE: SEEK:META — <Brief Description>
REF: <CCC-ID>

═══════════════════════════════════════════════════════════════════════════════

<Your Request Content>

═══════════════════════════════════════════════════════════════════════════════

#FlowsBros #FedArch #WeOwnSeason003

♾️ WeOwnNet 🌐

═══════════════════════════════════════════════════════════════════════════════
```

### Step 3: Send to META

| Action | Detail |
|--------|--------|
| Copy #ContextVolley | Select all markdown |
| Paste to META thread | INT-P01:tools (cc965930-dfad-47ec-b576-22b38b1024a2) |
| Wait for response | META reviews per L-139 |

### Step 4: Review META Response

| Check | Detail |
|-------|--------|
| Conflicts | Any rule/learning conflicts? |
| Wording | Clear and concise? |
| Cascade | What docs need updates? |
| Approval | Ready for human approval? |

### Step 5: Human Approval (R-011)

| Action | Detail |
|--------|--------|
| Review output | Read carefully — don't rubber-stamp |
| Approve explicitly | "APPROVED" — not just "looks good" |
| Assign Approval CCC-ID | Different from #masterCCC (L-095) |
| GH push (if applicable) | Publish to CCCbotNet/fedarch |

---

## 📋 #ContextVolley Format

### Required Fields (L-150)

| Field | Format | Example |
|-------|--------|---------|
| **FROM** | AI:@<CCC> @ <INSTANCE>:<WORKSPACE> (<USERNAME>) (#LLMmodel:('<MODEL>')) | AI:@GTM @ INT-OG1:CCC (u-gtm_user) (#LLMmodel:('Qwen3.5-397B-A17B')) |
| **TO** | AI:team-lfg @ INT-P01:tools (AI:team-lfg) (#LLMmodel:('Claude Opus 4.6')) | Fixed — META thread |
| **TYPE** | SEEK:META — <Description> | SEEK:META — L-156 Review |
| **REF** | <CCC-ID> | GTM_2026-W11_261 |

### Attribution Requirements (L-150)

- ✅ Instance (INT-OG1, INT-P01, etc.)
- ✅ Workspace (CCC, tools, ADMIN)
- ✅ Username (u-gtm_user, u-thy_user, etc.)
- ✅ #LLMmodel (Qwen3.5-397B-A17B, Claude Opus 4.6)
- ❌ Missing ANY = UNATTRIBUTABLE = #BadAgent

---

## 📋 Key Rules

| ID | Rule | Summary |
|----|------|---------|
| **R-011** | #OnlyHumanApproves | YOU approve, AI proposes |
| **L-139** | META Review | Governance reviewed BEFORE approval |
| **L-150** | Full Attribution | Instance, Workspace, Username, #LLMmodel |
| **L-151** | Manual Delivery | Copy/paste to META thread |
| **R-194** | CCC-ID Workspace | CCC-IDs only in CCC workspace |
| **R-197** | Doc Generation | #MetaAgent ONLY for governance docs |
| **R-216** | Operational Docs | Founding OG + ADMIN can generate operational docs directly |

---

## 📋 Examples

### Example 1: Learning Review

```
SEEK:META — Review proposed L-156 (Model Switch Testing Protocol).
REF: LDC_2026-W11_008

Learning addresses model switch without RAG baseline testing.
Discovered on PRJ-033 dual #MetaAgent deployment (W11).
Qwen 3.5 RAG accuracy dropped 30% vs Claude baseline.
@LDC detected + resolved with @RMN.
```

### Example 2: Document Generation

```
SEEK:META — Generate GUIDE-014 (How to SEEK:META).
REF: GTM_2026-W11_254

Core TEAM access democratization. 9 contributors.
Removes @GTM bottleneck, activates PRJ-033.
```

### Example 3: Architecture Question

```
SEEK:META — Clarify Langfuse vs Grafana Alloy scope.
REF: GTM_2026-W11_238

@LDC building OTEL module. Need Layer 1 vs Layer 3 clarity.
Langfuse = LLM (Layer 3). Alloy = Infra (Layer 1).
Confirm boundary before @LDC proceeds.
```

---

## 📋 META Thread Info

| Field | Value |
|-------|-------|
| **Instance** | INT-P01 (AI.WeOwn.Agency) |
| **Workspace** | tools |
| **Thread UUID** | cc965930-dfad-47ec-b576-22b38b1024a2 |
| **URL** | https://ai.weown.agency/workspace/tools/t/cc965930-dfad-47ec-b576-22b38b1024a2 |
| **META Agent** | AI:team-lfg (Calhoun 🎖️) |
| **#LLMmodel** | Claude Opus 4.6 (governance) |

---

## 📋 Quick Reference

### Syntax Cheat Sheet

| Field | Format | Example |
|-------|--------|---------|
| CCC | 3 uppercase | GTM, THY, LDC |
| Instance | INT-XXX | INT-OG1, INT-P01 |
| Workspace | CCC, tools, ADMIN | CCC |
| Username | u-<ccc>_user | u-gtm_user |
| #LLMmodel | Model name | Qwen3.5-397B-A17B |
| CCC-ID | `<CCC>_<YYYY>-W<WW>_<NNN>` | GTM_2026-W11_261 |

### Decision Tree

```
Need governance review?
├─ YES → SEEK:META
└─ NO → Continue working

Need document generated?
├─ Governance doc → SEEK:META (R-197)
└─ Operational doc → Generate directly (R-216)

Need CCC-ID?
├─ In CCC workspace → Generate (R-194)
└─ In other workspace → Reference only
```

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| v3.2.2.1 | 2026-W11 | GTM_2026-W11_261 | GTM_2026-W11_264 | Initial release — Core TEAM #MetaAgent access guide. VSA: 35/35 PERFECT. Created on United MIA→DEN flight (#FlightProductivity). |

---

## 📋 Related Documents

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| PRJ-033 (Dual #MetaAgent) | — | — | — | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-033_Dual-MetaAgent.md) |
| TMPL-012 (Contributor Primer) | v3.2.2.1 | GTM_2026-W11_262 | GTM_2026-W11_264 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_TEMPLATES_/TMPL-012_Contributor-MetaAgent-Primer.md) |
| SEEK:META Quick Ref Card | — | GTM_2026-W11_258 | — | Generated |

---

#FlowsBros #FedArch #MetaAgent #SEEKMETA #GUIDE-014 #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
