# PRJ-029: ♾️ WeOwn.Events 📆 — Event Management Platform

## 📋 PRJ-029_WeOwn-Events_v3.2.1.1.md
## ♾️ WeOwnNet 🌐

| Field | Value |
|-------|-------|
| Document | PRJ-029_WeOwn-Events.md |
| Version | 3.2.1.1 |
| CCC-ID | GTM_2026-W10_076 |
| CCC-ID APPROVAL | GTM_2026-W10_078 |
| Created | 2026-03-03 (W10) |
| Season | #WeOwnSeason003 🚀 |
| Status | ✅ APPROVED |
| Lifecycle Stage | ✅ APPROVED (#DocLifecycle) |
| **#LLMmodel** | **Qwen3.5-397B-A17B (AI.YonksTEAM.xyz @GTM)** |
| **#LLMmodel** | **Claude Opus 4.6 (meta.WeOwn.tools #MetaAgent)** |
| Tags | #WeOwnEvents #Luma #Eventbrite #Events #FlowsBros |
| Source of Truth | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-029_WeOwn-Events_v3.2.1.1.md) |

---

## 📖 Table of Contents

1. [Project Identity](#-project-identity)
2. [Why ♾️ WeOwn.Events 📆](#-why--weownevents-)
3. [♾️ WeOwn.Events 📆 Brand Identity](#-weownevents--brand-identity)
4. [Use Cases](#-use-cases)
5. [Events → P.O.P. Pipeline](#-events--pop-pipeline)
6. [MAIT Registry](#-mait-registry)
7. [Prior Event History](#-prior-event-history)
8. [Replaces INT-Exx Pattern](#-replaces-int-exx-pattern)
9. [Project Team](#-project-team)
10. [Deployment Checklist](#-deployment-checklist)
11. [Risk Matrix](#-risk-matrix)
12. [Relationship to Other Projects](#-relationship-to-other-projects)
13. [Discovered By](#-discovered-by)
14. [Related Documents](#-related-documents)
15. [Version History](#-version-history)

---

## 📋 Project Identity

| Field | Value |
|-------|-------|
| Project ID | **PRJ-029** |
| Title | **♾️ WeOwn.Events 📆 — Event Management Platform** |
| Type | Infrastructure — Event Management |
| Priority | 🟡 P2 |
| Owner | @LFG (events lead) + @GTM (infrastructure) |
| Instance | **INT-P04 (Events.WeOwn.tools)** |
| Timeline | **W12-W13** |
| Cost | **$18/mo** |
| Depends on | INT-S003 deployed (PRJ-014), Phase 0 deployed (PRJ-017) |
| Feeds into | PRJ-018 (P.O.P. Database — Events → contacts pipeline) |
| #masterCCC | GTM_2026-W10_076 |

---

## 📋 Why ♾️ WeOwn.Events 📆

### The Problem

3 events in S003. Each managed manually. No centralized event intelligence.

| Event | Platform | Attendees Tracked? | Follow-ups? | Contacts → P.O.P.? |
|-------|----------|-------------------|-------------|-------------------|
| PRJ-003 (#SideEvent_Redeem2026) | Luma | 🟡 Manual | 🟡 Manual | ❌ No |
| PRJ-006 (#SideEvent ETHDenver Wed) | Luma | 🟡 Manual | 🟡 Manual | ❌ No |
| PRJ-011 (#BUIDLathon ETHDenver) | ETHDenver native | 🟡 Manual | ❌ None | ❌ No |

### The Impact

| Metric | Value |
|--------|-------|
| Events run (S003) | 3 |
| Attendees tracked centrally | 0 |
| Contacts added to P.O.P. from events | 0 |
| Post-event follow-ups automated | 0 |
| MAIT knowledge of event platforms | 0 |

### The Solution

**One instance. Two MAITs. Events → P.O.P. pipeline.**

```
BEFORE:
  Event → manual RSVP tracking → manual follow-up → contacts lost

AFTER:
  Event → INT-P04 (MAIT_Luma / MAIT_Eventbrite)
    → RSVP tracking (AI-assisted)
    → Attendee management
    → Post-event follow-up
    → Contacts → P.O.P. (PRJ-018)
    → Intelligence: "Who attended 2+ events?" "Which CPAs came?"
```

---

## 📋 ♾️ WeOwn.Events 📆 Brand Identity

| Field | Value |
|-------|-------|
| Name | **♾️ WeOwn.Events 📆** |
| Type | Brand (operational label — entity later when revenue justifies) |
| Relationship | Sub-brand of ♾️ WeOwnNet 🌐 |
| Positioning | Community events, side events, workshops, conferences |
| Domain | **Events.WeOwn.tools** (instance) + **weown.events** (public-facing) |
| Emoji | 📆 |

### Ecosystem Brand Map (Updated)

| Brand | Focus | Instance |
|-------|-------|----------|
| ♾️ WeOwnNet 🌐 | Cooperative ecosystem | — |
| ♾️ WeOwn.Dev 💻 | Development | — |
| **♾️ WeOwn.Events 📆** | **Events** | **INT-P04** |
| jAIMSnet | AI observability | — |
| CCCbot.Net | CCC governance | — |

---

## 📋 Use Cases

### Use Case 1: Luma Events (lu.ma)

| Field | Value |
|-------|-------|
| Platform | [lu.ma](https://lu.ma) |
| Use | Side events, community events, free RSVPs |
| MAIT | @MAIT:#Luma |
| Examples | PRJ-003 (Redeem), PRJ-006 (ETHDenver Wed) |

**What MAIT_Luma enables:**

| Capability | Without MAIT | With MAIT |
|-----------|-------------|-----------|
| Create event | Manual on lu.ma | "Create a Luma event for March 15 in Denver" |
| RSVP tracking | Check lu.ma manually | "How many RSVPs for our next event?" |
| Attendee export | Manual CSV download | "Export attendee list to P.O.P." |
| Follow-up | Manual email | "Draft follow-up for all attendees" |
| Analytics | Manual counting | "Compare attendance across last 3 events" |

### Use Case 2: Eventbrite (eventbrite.com)

| Field | Value |
|-------|-------|
| Platform | [eventbrite.com](https://eventbrite.com) |
| Use | Ticketed events, workshops, paid conferences |
| MAIT | @MAIT:#Eventbrite |
| Examples | Future paid workshops, cooperative summits |

**What MAIT_Eventbrite enables:**

| Capability | Without MAIT | With MAIT |
|-----------|-------------|-----------|
| Ticketing strategy | Manual research | "What's the optimal ticket price for a 50-person workshop?" |
| Revenue tracking | Check Eventbrite manually | "Total ticket revenue this month?" |
| Attendee management | Manual | "Who bought VIP tickets?" |
| Promo codes | Manual creation | "Create a 20% promo code for CPA members" |
| Analytics | Manual | "Conversion rate from page view to ticket purchase?" |

---

## 📋 Events → P.O.P. Pipeline

### Data Flow

```
EVENT PLATFORM                     INT-P04                    P.O.P. (INT-P03)
──────────────                     ───────                    ────────────────

Luma RSVP list        ──→  events workspace   ──→  pop_contacts
                           "Export RSVPs"            vertical = tag-based

Eventbrite attendees  ──→  events workspace   ──→  pop_contacts
                           "Export attendees"        vertical = tag-based

Post-event            ──→  events workspace   ──→  pop_interactions
                           "Log follow-up"           type = 'event'

Speakers              ──→  events workspace   ──→  pop_contacts + pop_tags
                           "Add speaker"             tag = 'speaker:PRJ-006'

Venues                ──→  events workspace   ──→  pop_organizations
                           "Add venue"               + pop_places
```

### Pipeline Stages

| Stage | Action | Where |
|-------|--------|-------|
| 1. Pre-event | Create event, set up RSVPs | INT-P04 (events workspace) |
| 2. During event | Track attendance, notes | INT-P04 (events workspace) |
| 3. Post-event | Export attendees, log follow-ups | INT-P04 → INT-P03 (P.O.P.) |
| 4. Follow-up | Contact attendees, schedule meetings | INT-P03 (P.O.P.) |
| 5. Intelligence | "Who attended 2+ events?" | INT-P03 (P.O.P. SQL Agent) |

### Example Queries (Post-Pipeline)

| Query | Instance | Result |
|-------|----------|--------|
| "Show all attendees from PRJ-006" | INT-P03 | SQL → pop_contacts WHERE tag = 'event:PRJ-006' |
| "Which CPAs attended any event?" | INT-P03 | SQL → pop_contacts WHERE vertical = 'CPA' AND tag LIKE 'event:%' |
| "Who attended 2+ events?" | INT-P03 | SQL → GROUP BY person_id HAVING COUNT > 1 |
| "Draft follow-up for Redeem attendees" | INT-P04 | AI generates email draft |

---

## 📋 MAIT Registry

| Thread | ShortCode | Steward | Tool Agent | Scope |
|--------|-----------|---------|------------|-------|
| **MAIT_Luma** | **@MAIT:#Luma** | **@LFG** | **t-luma_tool** | lu.ma API, event creation, RSVPs, analytics |
| **MAIT_Eventbrite** | **@MAIT:#Eventbrite** | **@LFG** | **t-eventbrite_tool** | Eventbrite API, ticketing, revenue, analytics |

### RAG Sources

| MAIT | Source | Depth |
|------|--------|-------|
| @MAIT:#Luma | lu.ma/docs (if available) + help articles | 2 |
| @MAIT:#Eventbrite | eventbrite.com/platform/docs | 2 |

---

## 📋 Prior Event History

| PRJ | Event | Date | Platform | Attendees | Status |
|-----|-------|------|----------|-----------|--------|
| PRJ-003 | #SideEvent_Redeem2026 | Thu 12 Feb 2026 | Luma | ~20 | ✅ COMPLETE |
| PRJ-006 | #SideEvent ETHDenver Wed | Wed 18 Feb 2026 | Luma | ~30 | ✅ COMPLETE |
| PRJ-011 | #BUIDLathon ETHDenver | 20-22 Feb 2026 | ETHDenver native | ~50 | ✅ COMPLETE |
| **TOTAL** | **3 events** | | | **~100 attendees** | **0 in P.O.P.** |

> **100 attendees across 3 events — zero in P.O.P.** That's the gap PRJ-029 closes.

---

## 📋 Replaces INT-Exx Pattern

| Aspect | INT-Exx (Old Pattern) | INT-P04 (New Pattern) |
|--------|----------------------|----------------------|
| Type | Ephemeral (INT-Exx) | **Permanent (INT-Pxx)** |
| Scope | Single event | **ALL events** |
| Lifecycle | Deploy → event → decommission (R-214) | **Deploy → permanent** |
| MAITs | None | **2 (Luma + Eventbrite)** |
| P.O.P. integration | None | **Events → P.O.P. pipeline** |
| Cost per event | $18-48/mo × event duration | **$18/mo flat** |
| Knowledge retention | Lost on decommission | **Permanent — grows over time** |

> **INT-Exx remains available** for special cases (large conferences with dedicated demo needs). But for standard events, INT-P04 handles everything.

---

## 📋 Project Team

| CCC | Role | Focus |
|-----|------|-------|
| **LFG** | **Events Lead** | Event planning, Luma/Eventbrite, content, MAITs |
| **GTM** | **Infrastructure** | Instance setup, governance, P.O.P. integration |
| **CEO** | **Strategy** | Event strategy, partnerships |
| **THY** | **Budget** | Financial oversight |

---

## 📋 Deployment Checklist

> Deployment = INT-P04 deployment. See INT-P04 planning doc for full checklist.

| # | Step | Owner | Status |
|---|------|-------|--------|
| 1 | INT-S003 deployed (PRJ-014) | @SHD | ⬜ Prerequisite |
| 2 | Phase 0 deployed (PRJ-017) | @GTM | ⬜ Prerequisite |
| 3 | Create DO Droplet (ATL1, 2GB) | @SHD / @RMN | ⬜ |
| 4 | Deploy AnythingLLM (Docker) | @SHD / @RMN | ⬜ |
| 5 | Configure DNS (Events.WeOwn.tools) | @GTM | ⬜ |
| 6 | Configure LLM + Embedder | @GTM | ⬜ |
| 7 | Create workspaces (CCC, events, tools, ADMIN) | @GTM | ⬜ |
| 8 | Configure prompts (System + 4 workspace) | @GTM | ⬜ |
| 9 | Create users (5) | @GTM | ⬜ |
| 10 | Upload #PinnedDocs (4) | @GTM | ⬜ |
| 11 | Deploy MAIT_Luma (RAG + tool agent) | @LFG | ⬜ |
| 12 | Deploy MAIT_Eventbrite (RAG + tool agent) | @LFG | ⬜ |
| 13 | #SmokeTest (10-point) | @GTM | ⬜ |
| 14 | ISC INT-P04 (8/8) | @GTM | ⬜ |
| 15 | FULL:SYNC:META | @GTM | ⬜ |

---

## 📋 Risk Matrix

| # | Risk | Prob | Impact | Mitigation |
|---|------|------|--------|------------|
| 1 | Low event frequency (no urgency) | Medium | Low | P2 priority — deploy when ready, not rushed |
| 2 | Luma API changes | Low | Medium | MAIT RAG updated; lu.ma = stable platform |
| 3 | Eventbrite API complexity | Medium | Medium | @LFG stewards MAIT; Eventbrite docs = comprehensive |
| 4 | Events → P.O.P. data quality | Medium | Medium | Manual review before P.O.P. INSERT |
| 5 | @LFG availability for MAIT setup | Low | Medium | @GTM backup; MAIT setup = BP-026 standard |
| 6 | Cost ($18/mo for low-frequency use) | Low | Low | Justified by knowledge retention + P.O.P. pipeline |

---

## 📋 Relationship to Other Projects

| PRJ | Connection |
|-----|-----------|
| **PRJ-003** | #SideEvent_Redeem2026 — Luma event (retroactive tracking) |
| **PRJ-006** | #SideEvent ETHDenver Wed — Luma event (retroactive tracking) |
| **PRJ-011** | #BUIDLathon ETHDenver — event reference |
| **PRJ-014** | INT-S003 deployment = prerequisite |
| **PRJ-017** | Uptime Kuma monitors INT-P04 |
| **PRJ-018** | P.O.P. Database — Events → contacts pipeline |
| **PRJ-024** | Infisical manages INT-P04 API keys |

---

## 📋 Discovered By (BP-047)

| CCC | Contributor | Role | Context |
|-----|-------------|------|---------|
| GTM | [yonks](https://GitHub.com/YonksTEAM) | Co-Founder / Chief Digital Alchemist | 3 events in S003 with zero centralized tracking; identified need for permanent event platform; Events → P.O.P. pipeline concept |
| LFG | CoachLFG | Co-Host / Coach | Natural events lead — Co-Host role + #MemeLord visual content |

---

## 📋 Related Documents

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| SharedKernel | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/SharedKernel.md) |
| INT-P04 Planning | v3.2.1.1 | GTM_2026-W10_076 | GTM_2026-W10_078 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_INSTANCE_/INT-P04_Events-WeOwn-tools.md) |
| PRJ-018 (P.O.P.) | v3.1.4.1 | GTM_2026-W09_143 | GTM_2026-W09_143 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-018_POP-Database.md) |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| 3.2.1.1 | 2026-W10 | GTM_2026-W10_076 | GTM_2026-W10_078 | Initial project; ♾️ WeOwn.Events 📆 event management platform; INT-P04 (Events.WeOwn.tools); 2 MAITs (Luma + Eventbrite); Events → P.O.P. pipeline; prior event history (3 events, ~100 attendees, 0 in P.O.P.); replaces INT-Exx pattern; @LFG events lead; $18/mo; P2 W12-W13; 6-risk matrix; 15-step deployment; **#LLMmodel: Qwen3.5-397B-A17B (AI.YonksTEAM.xyz @GTM)** + **#LLMmodel: Claude Opus 4.6 (meta.WeOwn.tools #MetaAgent)** |

---

#FlowsBros #FedArch #WeOwnEvents #Luma #Eventbrite #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
