# TMPL-011: Weekly Events Tracker

## 📋 TMPL-011_WEEKLY-EVENTS_v3.2.1.1.md
## ♾️ WeOwnNet 🌐 — Template

| Field | Value |
|-------|-------|
| Document | TMPL-011_WEEKLY-EVENTS.md |
| Version | 3.2.1.1 |
| CCC-ID | GTM_2026-W10_086 |
| Created | 2026-03-03 (W10) |
| Season | #WeOwnSeason003 🚀 |
| Status | ✅ APPROVED |
| Source of Truth | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_TEMPLATES_/TMPL-011_WEEKLY-EVENTS.md) |

---

## 📖 Table of Contents

1. [Overview](#-overview)
2. [Usage Instructions](#-usage-instructions)
3. [Filename Convention](#-filename-convention)
4. [Template Body](#-template-body)
5. [Section Guide](#-section-guide)
6. [#SpecialDays Guide](#-specialdays-guide)
7. [Events → P.O.P. Pipeline Guide](#-events--pop-pipeline-guide)
8. [Example — EVENTS_2026-W10.md](#-example--events_2026-w10md)
9. [Related Rules + Documents](#-related-rules--documents)
10. [Version History](#-version-history)

---

## 📋 Overview

This template standardizes weekly event tracking for **PRJ-029 (♾️ WeOwn.Events 📆)**. Instead of assigning PRJ numbers per event, all events are tracked in weekly documents under a single umbrella project.

| Field | Value |
|-------|-------|
| Parent PRJ | PRJ-029 (♾️ WeOwn.Events 📆) |
| Pattern | One document per ISO week (only when events exist) |
| Owner | @LFG (events lead) + @GTM (governance) |
| Doc type | **Operational (R-216)** — filled by @LFG, no SEEK:META required |
| Storage | `_EVENTS_/` folder — GH + RAG |

### Why This Pattern

| Factor | PRJ per event (old) | Weekly Tracker (new) |
|--------|---------------------|---------------------|
| PRJ burn rate | 🔴 2+/week | ✅ **ZERO** |
| Governance overhead | 🔴 SEEK:META per event | ✅ **R-216 operational** |
| Context density | 🟡 Scattered across PRJs | ✅ **One doc per week** |
| Events → P.O.P. | 🟡 Per-PRJ | ✅ **Weekly batch** |
| Historical browse | 🟡 Search PRJs | ✅ **Browse by week** |

---

## 📋 Usage Instructions

### When to Create

| Condition | Action |
|-----------|--------|
| Events planned or held this week | ✅ Create `EVENTS_<YYYY>-W<WW>.md` |
| No events this week | ❌ Do NOT create (skip week) |
| Event added mid-week | ✅ Update existing tracker |

### Who Creates

| Role | Action |
|------|--------|
| **@LFG** (events lead) | Creates + fills weekly tracker |
| **@GTM** | Reviews, governs template, GH push |
| **Any contributor** | Can add events with @LFG approval |

### Where to Store

| Location | Path |
|----------|------|
| GH | `CCCbotNet/fedarch/_EVENTS_/EVENTS_<YYYY>-W<WW>.md` |
| RAG | Upload to relevant instances (INT-P01, INT-OG1, INT-P04 when deployed) |

### Workflow

| # | Step | Owner |
|---|------|-------|
| 1 | Event identified (planned or spontaneous) | Any contributor |
| 2 | Create or update weekly tracker | @LFG |
| 3 | Fill event details (pre-event) | @LFG |
| 4 | Update attendees + outcomes (post-event) | @LFG |
| 5 | Events → P.O.P. pipeline (post-event) | @LFG + @GTM |
| 6 | GH push (end of week or after last event) | @GTM |
| 7 | RAG sync | @GTM_ADMIN |

---

## 📋 Filename Convention

### Format

```
EVENTS_<YYYY>-W<WW>.md
```

| Component | Description | Example |
|-----------|-------------|---------|
| `EVENTS` | Prefix (always) | EVENTS |
| `<YYYY>` | Year | 2026 |
| `W<WW>` | ISO week (zero-padded) | W10 |

### Examples

| Filename | Week |
|----------|------|
| `EVENTS_2026-W10.md` | 24 Feb - 02 Mar 2026 |
| `EVENTS_2026-W11.md` | 03 Mar - 09 Mar 2026 |
| `EVENTS_2026-W15.md` | 31 Mar - 06 Apr 2026 |

---

## 📋 Template Body

> **Copy everything below this line when creating a new weekly tracker.**

---

```markdown
# ♾️ WeOwn.Events 📆 — <YYYY>-W<WW>

## 📋 EVENTS_<YYYY>-W<WW>.md
## PRJ-029 — ♾️ WeOwn.Events 📆

| Field | Value |
|-------|-------|
| Week | <YYYY>-W<WW> (<Start Date> - <End Date>) |
| PRJ | PRJ-029 |
| Owner | @LFG + @GTM |
| Events | <count> |
| #SpecialDays | <list or "None"> |
| Status | 📋 PLANNING / 🔄 IN PROGRESS / ✅ COMPLETE |

---

## 📋 Events This Week

| # | Event | Date | Time | Platform | Hosts | Status |
|---|-------|------|------|----------|-------|--------|
| 1 | <Event Name> | <Day Date> | <Time TZ> | <Platform> | <@CCC> | <Status> |

---

## 📋 Event 1: <Event Name>

| Field | Value |
|-------|-------|
| What | <Description> |
| When | <Day Date Time TZ> |
| Where | <Platform / Venue / URL> |
| Hosts | <@CCC list> |
| Audience | <Target audience> |
| Connection | <Related PRJ / brand / none> |
| #SpecialDay | <If applicable / none> |

### Details

<Event-specific details, agenda, goals, notes>

### Pre-Event Checklist

| # | Task | Owner | Status |
|---|------|-------|--------|
| 1 | Create event on platform | @LFG | ⬜ |
| 2 | Promote on social | @LFG | ⬜ |
| 3 | Prepare content/slides | <Owner> | ⬜ |

### Attendees (Post-Event)

| # | Name | Vertical | Contact | → P.O.P.? |
|---|------|----------|---------|-----------|
| 1 | | | | ⬜ |

### Outcomes

| Metric | Value |
|--------|-------|
| RSVPs | <count> |
| Actual attendance | <count> |
| Key takeaways | <notes> |
| Follow-up actions | <list> |

---

## 📋 #SpecialDays This Week

| Date | Hashtag | Significance | Recurring? |
|------|---------|-------------|-----------|
| <Date> | <#Hashtag> | <Why> | ✅ / ❌ |

> *If no #SpecialDays this week, write "None."*

---

## 📋 Post-Event → P.O.P. Pipeline

| # | Event | Attendees | → P.O.P.? | Follow-up Sent? |
|---|-------|-----------|-----------|----------------|
| 1 | <Event> | <count> | ⬜ | ⬜ |

### Pipeline Steps

| # | Step | Owner | Status |
|---|------|-------|--------|
| 1 | Export attendee list from platform | @LFG | ⬜ |
| 2 | Review + clean data | @LFG | ⬜ |
| 3 | Import to P.O.P. (INT-P03) | @GTM | ⬜ |
| 4 | Tag contacts (event, vertical) | @GTM | ⬜ |
| 5 | Send follow-up | @LFG | ⬜ |

---

## 📋 Week Summary

| Metric | Value |
|--------|-------|
| Events planned | <count> |
| Events held | <count> |
| Total RSVPs | <count> |
| Total attendance | <count> |
| → P.O.P. contacts | <count> |
| Follow-ups sent | <count> |

---

#FlowsBros #FedArch #WeOwnEvents #WeOwnSeason003

♾️ WeOwnNet 🌐
```

---

## 📋 Section Guide

### Required Sections (Every Week)

| Section | Required | When to Fill |
|---------|----------|-------------|
| Header (metadata) | ✅ Always | When creating |
| Events This Week (table) | ✅ Always | When creating |
| Event N (detail per event) | ✅ Per event | Pre-event |
| Attendees | ✅ Per event | Post-event |
| Outcomes | ✅ Per event | Post-event |
| #SpecialDays | ✅ Always | When creating ("None" if none) |
| Post-Event → P.O.P. | ✅ Always | Post-event |
| Week Summary | ✅ Always | End of week |

### Optional Sections

| Section | When |
|---------|------|
| Pre-Event Checklist | For events requiring preparation |
| Details (extended) | For complex events |

---

## 📋 #SpecialDays Guide

### What Qualifies

| Type | Description | Example |
|------|-------------|---------|
| **Recurring annual** | Same date every year | #3winDay (03/03) |
| **Statehood / founding** | Historical significance | #WeOwnFL (03/03 — FL statehood 1845) |
| **Season milestone** | #WeOwnSeason boundary | S003 start (W06) |
| **Ecosystem anniversary** | Founding dates, milestones | #FoundersDay (TBD) |

### #SpecialDays Registry (Growing)

| Date | Hashtag | Significance | First Year |
|------|---------|-------------|-----------|
| **03/03** | **#3winDay** | 3 wins — Community, Contributors, Ecosystem | 2026 |
| **03/03** | **#WeOwnFL** | Florida statehood (1845) | 2026 |
| TBD | #FoundersDay | ♾️ WeOwnNet founding | TBD |

> **Add new #SpecialDays to this registry as they're established.** Include in weekly tracker when they fall in that week.

---

## 📋 Events → P.O.P. Pipeline Guide

### When to Run Pipeline

| Trigger | Action |
|---------|--------|
| Event completed | Export attendees → P.O.P. |
| Follow-up needed | Create pop_interactions (type='event') |
| Speaker identified | Add to pop_contacts + tag 'speaker' |
| Venue identified | Add to pop_organizations + pop_places |

### Data Mapping

| Event Data | P.O.P. Table | P.O.P. Field |
|-----------|-------------|-------------|
| Attendee name | pop_contacts | name |
| Attendee email | pop_contacts | email |
| Professional vertical | pop_contacts | vertical (ADV/CPA/REP/ESQ) |
| Event attended | pop_tags | tag = 'event:EVENTS_2026-W10' |
| Follow-up sent | pop_interactions | type = 'event' |
| Speaker | pop_tags | tag = 'speaker' |
| Venue | pop_organizations | org_type = 'venue' |

### Pipeline Availability

| Status | Pipeline |
|--------|---------|
| **Now (W10)** | Manual — export CSV, review, manual entry |
| **INT-P03 deployed** | SQL Agent — "Import these attendees to P.O.P." |
| **INT-P04 deployed** | Direct — events workspace → P.O.P. pipeline |

---

## 📋 Example — EVENTS_2026-W10.md

> See the first weekly tracker created at:
> `CCCbotNet/fedarch/_EVENTS_/EVENTS_2026-W10.md`
>
> Contains: #3winDay LiveStream + #WeOwnFL Launch (2 events, 2 #SpecialDays)

---

## 📋 Related Rules + Documents

### Rules

| ID | Description | Relevance |
|----|-------------|-----------|
| R-216 | Operational docs = Founding OG + ADMIN | Weekly trackers = operational |
| R-199 | Session notes = RAG only | Events ≠ session notes → GH + RAG |

### Projects

| PRJ | Relevance |
|-----|-----------|
| PRJ-029 | Parent project (♾️ WeOwn.Events 📆) |
| PRJ-018 | P.O.P. Database (Events → contacts pipeline) |

### Best Practices

| ID | Description |
|----|-------------|
| BP-045 | Version History + Related Documents format |

### Templates

| TMPL | Description |
|------|-------------|
| TMPL-007 | GH Commit Message (for GH push) |
| **TMPL-011** | **This template** |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| 3.2.1.1 | 2026-W10 | GTM_2026-W10_086 | GTM_2026-W10_090 | Initial template; Weekly Event Tracker pattern for PRJ-029; `_EVENTS_/` folder; `EVENTS_<YYYY>-W<WW>.md` filename convention; event detail sections (pre/post); #SpecialDays guide + registry (#3winDay, #WeOwnFL); Events → P.O.P. pipeline guide with data mapping; pre-event checklist; attendee tracking; week summary metrics; usage instructions (who/when/where); section guide (required vs optional); pipeline availability phases (manual → SQL Agent → direct) |

---

#FlowsBros #FedArch #WeOwnEvents #Templates #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
