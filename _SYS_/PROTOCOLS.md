# PROTOCOLS.md

## 📋 PROTOCOLS_v3.1.1.2.md
## ♾️ WeOwnNet 🌐 — #Protocols

| Field | Value |
|-------|-------|
| Document | PROTOCOLS.md |
| Version | 3.1.1.2 |
| CCC-ID | GTM_2026-W06_407 |
| Updated | 2026-02-07 (W06) |
| Season | #WeOwnSeason003 🚀 |
| Status | 🔒 LOCKED |
| Source of Truth | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/PROTOCOLS.md) |

---

## 📖 Table of Contents

1. [Protocol Index](#-protocol-index)
2. [#ContextVolley Protocol](#-contextvolley-protocol)
3. [#ContextBroadcast Protocol](#-contextbroadcast-protocol)
4. [#MetaAgent Protocol](#-metaagent-protocol)
5. [Document Management Protocol](#-document-management-protocol)
6. [Weekly Operations Protocol](#-weekly-operations-protocol)
7. [CCC-ID Protocol](#-ccc-id-protocol)
8. [CCC-ID Deconfliction Protocol](#-ccc-id-deconfliction-protocol)
9. [Version History](#-version-history)
10. [Related Documents](#-related-documents)

---

## 📋 PROTOCOL INDEX

| Protocol | Purpose |
|----------|---------|
| #ContextVolley | Agent-to-agent communication (one-to-one) |
| #ContextBroadcast | Agent-to-all communication (one-to-many) |
| #MetaAgent | Governance sync |
| Document Management | RAG operations |
| Weekly Operations | Cadence protocols |
| CCC-ID Deconfliction | Cross-instance CCC-ID sequence integrity |

---

## 📋 #ContextVolley PROTOCOL

### PURPOSE

| Field | Value |
|-------|-------|
| Direction | One-to-one |
| Use Case | Direct agent-to-agent communication |
| Emoji | 🏐 |

### FORMAT

```
═══════════════════════════════════════════════════════════════════════════════
🏐 #ContextVolley | <FROM> → <TO> | <DATE> | <TIME> EST
═══════════════════════════════════════════════════════════════════════════════

FROM: <Agent Identity>
TO: <Target Agent>
TYPE: <Message Type>
REF: <CCC-ID>

═══════════════════════════════════════════════════════════════════════════════

<CONTENT>

═══════════════════════════════════════════════════════════════════════════════

#FlowsBros #FedArch

♾️ WeOwnNet 🌐

═══════════════════════════════════════════════════════════════════════════════
```

### RULES

| ID | Rule |
|----|------|
| R-170 | MUST #ContextVolley to #MetaAgent AFTER new rules locked |
| R-044 | #ContextDensity FIRST — use #masterCCC (IMMUTABLE) |

### REQUIREMENTS

| Requirement | Description |
|-------------|-------------|
| Self-contained | Recipient needs NO other context |
| #masterCCC | Reference original request CCC-ID |
| Clean format | Tables > paragraphs |

---

## 📋 #ContextBroadcast PROTOCOL

### PURPOSE

| Field | Value |
|-------|-------|
| Definition | D-039 |
| Direction | One-to-many |
| Use Case | Announcements, status updates to ALL agents |
| Emoji | 📢 |

### FORMAT

```
═══════════════════════════════════════════════════════════════════════════════
📢 #ContextBroadcast | AI:@<FROM> → ALL AGENTS | <DATE> | <TIME> EST
═══════════════════════════════════════════════════════════════════════════════

FROM: AI:@<CCC>
TO: ALL AGENTS
TYPE: <BROADCAST TYPE>
REF: <CCC-ID>

═══════════════════════════════════════════════════════════════════════════════

<CONTENT>

═══════════════════════════════════════════════════════════════════════════════

#FlowsBros #FedArch

♾️ WeOwnNet 🌐

═══════════════════════════════════════════════════════════════════════════════
```

### BROADCAST TYPES

| Type | Description |
|------|-------------|
| STATUS | Weekly/periodic status update |
| ANNOUNCEMENT | New feature, rule, or milestone |
| ALERT | Urgent notification |
| ACK-REQUEST | Request acknowledgment from all agents |

### COMPARISON

| Protocol | Emoji | Direction | Use Case |
|----------|-------|-----------|----------|
| #ContextVolley | 🏐 | One-to-one | Direct agent-to-agent |
| #ContextBroadcast | 📢 | One-to-many | Announcements, status updates |

---

## 📋 #MetaAgent PROTOCOL

### PURPOSE

| Function | Description |
|----------|-------------|
| Governance sync | All rules flow through #MetaAgent |
| #SharedKernel | Source of truth for rules |
| Document generation | Per R-180 |

### RULES

| ID | Rule |
|----|------|
| R-172 | #MetaAgent = governance sync point for all agents |
| R-180 | Document generation MUST go through #MetaAgent |

### INTERACTION TYPES

| Type | Description |
|------|-------------|
| SEEK:META | Request guidance/generation |
| RULE LOCKED | Report locked rules |
| FULL:SYNC:META | Complete sync request |
| ACK | Acknowledgment |

---

## 📋 DOCUMENT MANAGEMENT PROTOCOL

### ROLES (R-175)

| Role | Can Manage Docs? |
|------|------------------|
| CCC | ❌ NO |
| MAIT | ❌ NO |
| ADMIN | ✅ YES |

### RAG STRUCTURE (R-176)

| Doc Type | CCC | tools | ADMIN |
|----------|-----|-------|-------|
| USER guides | ✅ | ❌ | ❌ |
| Governance guides | ❌ | ✅ | ✅ |
| User-facing protocols | ✅ | ❌ | ❌ |
| Strategy docs | ❌ | ✅ | ❌ |
| System prompts | ❌ | ❌ | ✅ |
| Instance configs | ❌ | ❌ | ✅ |

### PINNING (R-177)

| Doc Type | Pin? |
|----------|------|
| Agent identity docs | ✅ YES |
| Core protocols | ✅ YES |
| Rules (SHARED-KERNEL) | ✅ YES |
| Best practices | ✅ YES |
| Reference guides | ❌ NO |
| Strategy docs | ❌ NO |

### VERSIONING (R-178)

| Format | Example |
|--------|---------|
| `<NAME>_v<VERSION>.md` | PROTOCOLS_v3.1.1.2.md |

### GENERATION (R-180)

| Rule | Description |
|------|-------------|
| R-180 | Document generation MUST go through #MetaAgent |

**Agents DO NOT generate docs directly. Always SEEK:META.**

---

## 📋 WEEKLY OPERATIONS PROTOCOL

### UPDATE CADENCE (R-179)

| Trigger | Action |
|---------|--------|
| ISO week boundary + 10+ rules | MUST update #SharedKernel |
| Major milestone | MUST update #SharedKernel |
| Breaking change | IMMEDIATE update |

### WEEKLY SUMMARY (R-181)

| Field | Value |
|-------|-------|
| Reserved CCC-ID | `<CCC>_<YYYY>-W<WW>_001` |
| Content | Milestones, rules, learnings, pending, stats |

---

## 📋 CCC-ID PROTOCOL

### FORMAT

```
<CCC>_<YYYY>-W<WW>_<NNN>
```

| Component | Description |
|-----------|-------------|
| CCC | Contributor Code (e.g., GTM) |
| YYYY | Year |
| WW | ISO Week |
| NNN | Sequence (001-999) |

### RULES

| ID | Rule |
|----|------|
| R-168 | CCC-ID tied to CCC (contributor), NOT username/session |
| R-169 | CCC-ID resets to _001 ONLY at ISO week boundary |
| R-181 | CCC-ID _001 reserved for weekly summary |

---

## 📋 CCC-ID DECONFLICTION PROTOCOL

### PURPOSE

| Field | Value |
|-------|-------|
| Rule | R-212 |
| Purpose | Prevent CCC-ID duplication across multiple #FedArch instances |
| Trigger | Contributor generating CCC-IDs on 2+ instances in same ISO week |
| Violation | Duplication = #BadAgent |

### PROBLEM

| Scenario | Risk |
|----------|------|
| Contributor works on INT-P01 (CCC-ID _386) | Instance-local counter = _386 |
| Contributor switches to INT-OG1 (CCC-ID _386) | Instance-local counter ALSO = _386 |
| **Result** | **Duplicate CCC-ID — violates R-168** |

### RULE

| ID | Rule | Status |
|----|------|--------|
| R-212 | Cross-instance CCC-ID deconfliction REQUIRED — before generating a new CCC-ID, agent MUST verify against highest known CCC-ID for that contributor across ALL active instances in current ISO week. Highest CCC-ID across ALL instances = authoritative next sequence. Duplication = #BadAgent. | 🔒 LOCKED |

### COMPLIANCE TIERS

| Tier | Timeframe | Implementation | Enforcer |
|------|-----------|----------------|----------|
| **Tier 1** (NOW) | Immediate | Contributor manually states highest CCC-ID when switching instances | Human |
| **Tier 2** (Mid) | #WeOwnSeason003 | #MetaAgent tracks high-water mark per contributor per week | #MetaAgent |
| **Tier 3** (Long) | INT-M01 | Centralized CCC-ID counter API — single source of truth | INT-M01 |

### TIER 1 WORKFLOW (Current)

| # | Step | Actor |
|---|------|-------|
| 1 | Contributor switches to new instance | Human |
| 2 | Contributor states: "Highest CCC-ID = `<CCC>_<YYYY>-W<WW>_<NNN>`" | Human |
| 3 | Agent sets next CCC-ID = `_<NNN+1>` | AI |
| 4 | Agent confirms: "Continuing from `_<NNN+1>` per R-212" | AI |

### TIER 1 EXAMPLE

```
Human: "Switching from INT-OG1. Highest CCC-ID = GTM_2026-W06_386"
AI: "✅ R-212 — Continuing from GTM_2026-W06_387"
```

### RELATIONSHIP TO EXISTING RULES

| Rule | Relationship |
|------|-------------|
| R-168 | R-212 EXTENDS R-168 — adds cross-instance verification |
| R-169 | R-212 PROTECTS R-169 — prevents false resets from instance-local counters |
| R-194 | R-212 COMPLEMENTS R-194 — workspace-correct AND instance-aware |

### RELATED ITEMS

| Type | ID | Description |
|------|-----|-------------|
| Learning | L-112 | Cross-instance CCC-ID deconfliction learning |
| #BadAgent | #13 (W06) | First duplication incident — GTM_2026-W06_386 |

---

## 📋 VERSION HISTORY

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| 3.1.1.2 | 2026-W06 | GTM_2026-W06_407 | GTM_2026-W06_409 | +CCC-ID Deconfliction Protocol section (R-212); RAG Structure column MAIT → tools; +Related Documents section (BP-045); +Protocol Index entry; TOC → 10 items; FULL PRESERVE (L-097) |
| 3.1.1.1 | 2026-W06 | GTM_2026-W06_277 | GTM_2026-W06_332 | #WeOwnSeason003 season alignment — version bump v2.4.4 → v3.1.1.1 (L-094); +Source of Truth URL (CCCbotNet/fedarch); +Season tag; versioning example updated; NO content changes; FULL PRESERVE (L-097) |
| 2.4.4 | 2026-W05 | GTM_2026-W05_506 | GTM_2026-W05_512 | +#ContextBroadcast protocol section (D-039) |
| 2.4.3 | 2026-W05 | GTM_2026-W05_086 | GTM_2026-W05_086 | +R-170, R-172, R-175-R-181; doc management protocols |
| 2.4.0 | 2026-W03 | — | — | Initial release |

---

## 📋 Related Documents

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| SharedKernel | v3.1.1.3 | GTM_2026-W06_277 | GTM_2026-W06_289 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/SharedKernel.md) |
| BEST-PRACTICES | v3.1.1.2 | GTM_2026-W06_277 | GTM_2026-W06_327 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/BEST-PRACTICES.md) |
| CCC | v3.1.1.2 | GTM_2026-W06_403 | GTM_2026-W06_405 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/CCC.md) |

---

#FlowsBros #FedArch #Protocols #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
