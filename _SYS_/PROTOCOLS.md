# PROTOCOLS.md

## 📋 PROTOCOLS_v3.1.3.1.md
## ♾️ WeOwnNet 🌐 — #Protocols

| Field | Value |
|-------|-------|
| Document | PROTOCOLS.md |
| Version | 3.1.3.1 |
| CCC-ID | GTM_2026-W08_069 |
| Updated | 2026-02-21 (W08) |
| Season | #WeOwnSeason003 🚀 |
| Status | 🔒 LOCKED |
| Source of Truth | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/PROTOCOLS.md) |

---

## 📖 Table of Contents

1. [Protocol Index](#-protocol-index)
2. [#ContextVolley Protocol](#-contextvolley-protocol)
3. [#ContextBroadcast Protocol](#-contextbroadcast-protocol)
4. [#MetaAgent Protocol](#-metaagent-protocol)
5. [#DocLifecycle Protocol](#-doclifecycle-protocol)
6. [Document Management Protocol](#-document-management-protocol)
7. [Weekly Operations Protocol](#-weekly-operations-protocol)
8. [CCC-ID Protocol](#-ccc-id-protocol)
9. [CCC-ID Deconfliction Protocol](#-ccc-id-deconfliction-protocol)
10. [Version History](#-version-history)
11. [Related Documents](#-related-documents)

---

## 📋 PROTOCOL INDEX

| Protocol | Purpose |
|----------|---------|
| #ContextVolley | Agent-to-agent communication (one-to-one) |
| #ContextBroadcast | Agent-to-all communication (one-to-many) |
| #MetaAgent | Governance sync |
| #DocLifecycle | Document lifecycle VSA governance |
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

## 📋 #DocLifecycle PROTOCOL

### PURPOSE

| Field | Value |
|-------|-------|
| Definition | D-062 |
| Purpose | Govern document progression and VSA eligibility |
| Hashtag | #DocLifecycle |
| Rule | R-215 |
| Best Practice | BP-063 |

### LIFECYCLE STAGES

| Stage | Icon | VSA Eligible? | VSA Type | Exit Criteria |
|-------|------|---------------|----------|---------------|
| IDEA | 💡 | ❌ | — | Owner + scope defined |
| DRAFT | 📝 | ⚠️ DRAFT CHECK only | DRAFT CHECK (D-063) | 5-item checklist passes |
| IN PROGRESS | 🔄 | ❌ | — | #MetaAgent generating |
| REVIEW | 👀 | ✅ | Batch, FULL | Human reviews |
| APPROVED | ✅ | ✅ | Batch, FULL, DEEP FULL | Human approves (R-011) |
| GH LIVE | 🚀 | ✅ | Batch, FULL, DEEP FULL | Published to GH |
| VERIFIED | 🏆 | ✅ | Any (re-VSA) | VSA PASS attested |

### RULES

| ID | Rule |
|----|------|
| R-215 | Production VSA MUST NOT be initiated on DRAFT/IDEA stage documents |
| R-216 | Operational docs may be generated directly by R-216-eligible contributors |
| R-197 | Governance docs MUST go through #MetaAgent (IMMUTABLE — unchanged) |

### EXPECTED FAIL (D-064)

| Scenario | Classification |
|----------|---------------|
| Production VSA on DRAFT doc | ❌ EXPECTED FAIL (DRAFT) |
| Counted in pass rate? | ❌ NO |
| #BadAgent? | ❌ NO (R-215) |
| Logged? | ✅ YES — separately in VSA registry |

---

## 📋 DOCUMENT MANAGEMENT PROTOCOL

### ROLES (R-175 + R-216)

| Role | Can Manage Docs? | Can Generate Docs? |
|------|------------------|--------------------|
| CCC | ❌ NO | ❌ NO |
| MAIT | ❌ NO | ❌ NO |
| ADMIN | ✅ YES | ⚠️ Operational only (R-216) |
| #MetaAgent | — | ✅ Governance docs (R-197) |

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
| 3.1.3.1 | 2026-W08 | GTM_2026-W08_069 | GTM_2026-W08_071 | +#DocLifecycle Protocol section (D-062, R-215, BP-063); +Protocol Index entry; Document Management +R-216 reference; +Operational doc generation role; TOC → 11 items; FULL PRESERVE (L-097) |
| 3.1.1.2 | 2026-W06 | GTM_2026-W06_407 | GTM_2026-W06_409 | +CCC-ID Deconfliction Protocol section (R-212); RAG Structure column MAIT → tools; +Related Documents section (BP-045); +Protocol Index entry; TOC → 10 items; FULL PRESERVE (L-097) |
| 3.1.1.1 | 2026-W06 | GTM_2026-W06_277 | GTM_2026-W06_332 | #WeOwnSeason003 season alignment — version bump v2.4.4 → v3.1.1.1 (L-094); +Source of Truth URL (CCCbotNet/fedarch); +Season tag; versioning example updated; NO content changes; FULL PRESERVE (L-097) |
| 2.4.4 | 2026-W05 | GTM_2026-W05_506 | GTM_2026-W05_512 | +#ContextBroadcast protocol section (D-039) |
| 2.4.3 | 2026-W05 | GTM_2026-W05_086 | GTM_2026-W05_086 | +R-170, R-172, R-175-R-181; doc management protocols |
| 2.4.0 | 2026-W03 | — | — | Initial release |

---

## 📋 Related Documents

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| SharedKernel | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/SharedKernel.md) |
| BEST-PRACTICES | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/BEST-PRACTICES.md) |
| PROTOCOLS | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/PROTOCOLS.md) |
| CCC | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/CCC.md) |

---

#FlowsBros #FedArch #Protocols #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
