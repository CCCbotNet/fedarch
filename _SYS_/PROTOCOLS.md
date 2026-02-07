# PROTOCOLS.md

## 📋 PROTOCOLS_v3.1.1.1.md
## ♾️ WeOwnNet 🌐 — #Protocols

| Field | Value |
|-------|-------|
| Document | PROTOCOLS.md |
| Version | 3.1.1.1 |
| CCC-ID | GTM_2026-W06_277 |
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
8. [Version History](#-version-history)

---

## 📋 PROTOCOL INDEX

| Protocol | Purpose |
|----------|---------|
| #ContextVolley | Agent-to-agent communication (one-to-one) |
| #ContextBroadcast | Agent-to-all communication (one-to-many) |
| #MetaAgent | Governance sync |
| Document Management | RAG operations |
| Weekly Operations | Cadence protocols |

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

| Doc Type | CCC | MAIT | ADMIN |
|----------|-----|------|-------|
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
| `<NAME>_v<VERSION>.md` | PROTOCOLS_v3.1.1.1.md |

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

## 📋 VERSION HISTORY

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| 3.1.1.1 | 2026-W06 | GTM_2026-W06_277 | GTM_2026-W06_332 | #WeOwnSeason003 season alignment — version bump v2.4.4 → v3.1.1.1 (L-094); +Source of Truth URL (CCCbotNet/fedarch); +Season tag; versioning example updated; NO content changes; FULL PRESERVE (L-097) |
| 2.4.4 | 2026-W05 | GTM_2026-W05_506 | GTM_2026-W05_512 | +#ContextBroadcast protocol section (D-039) |
| 2.4.3 | 2026-W05 | GTM_2026-W05_086 | GTM_2026-W05_086 | +R-170, R-172, R-175-R-181; doc management protocols |
| 2.4.0 | 2026-W03 | — | — | Initial release |

---

#FlowsBros #FedArch #Protocols #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
