# PRJ-014: #FedArchExpansion {2026-W10}

## 📋 PRJ-014_FedArchExpansion-W10_v3.1.4.2.md
## ♾️ WeOwnNet 🌐

| Field | Value |
|-------|-------|
| Document | PRJ-014_FedArchExpansion-W10.md |
| Version | 3.1.4.2 |
| CCC-ID | GTM_2026-W09_086 |
| Created | 2026-02-27 (W09) |
| Season | #WeOwnSeason003 🚀 |
| Status | ✅ APPROVED |
| Approval | GTM_2026-W09_099 |
| Lifecycle Stage | 📝 DRAFT (#DocLifecycle) |
| Tags | #FedArchExpansion #INT-S003 #WeOwnTools #FlowsBros |

---

## 📖 Table of Contents

1. [Project Identity](#-project-identity)
2. [Strategic Vision](#-strategic-vision)
3. [Deliverable 1: Deploy INT-S003](#-deliverable-1-deploy-int-s003)
4. [Deliverable 2: Evolve INT-P01 → AI.WeOwn.tools](#-deliverable-2-evolve-int-p01--aiweowntools)
5. [User Migration Matrix](#-user-migration-matrix)
6. [12-Step Deployment Checklist — INT-S003](#-12-step-deployment-checklist--int-s003)
7. [INT-P01 Evolution Plan](#-int-p01-evolution-plan)
8. [Thread URL Migration](#-thread-url-migration)
9. [Timeline](#-timeline)
10. [ISC Certification — INT-S003](#-isc-certification--int-s003)
11. [Infrastructure](#-infrastructure)
12. [Project Team](#-project-team)
13. [Risk Matrix](#-risk-matrix)
14. [Decommission Plan — INT-S003](#-decommission-plan--int-s003)
15. [#ContextSwap Log](#-contextswap-log)
16. [Cascade Impact — Domain Migration](#-cascade-impact--domain-migration)
17. [Relationship to Other Projects](#-relationship-to-other-projects)
18. [Discovered By](#-discovered-by)
19. [Related Documents](#-related-documents)
20. [Version History](#-version-history)

---

## 📋 Project Identity

| Field | Value |
|-------|-------|
| Project ID | **PRJ-014** |
| Title | **#FedArchExpansion {2026-W10}** |
| Description | Separate user-facing and governance concerns — deploy INT-S003 for contributors, evolve INT-P01 into governance hub (AI.WeOwn.tools) |
| Type | Infrastructure — Instance Expansion + Migration |
| Priority | 🔴 P0 |
| Owner | @GTM |
| #masterCCC | GTM_2026-W09_086 |
| Deliverables | **2** (INT-S003 deployment + INT-P01 evolution) |

---

## 📋 Strategic Vision

### The Problem

INT-P01 (AI.WeOwn.Agency) currently serves dual purpose:

| Function | Workspace | Users | Load |
|----------|-----------|-------|------|
| 🤝 User-facing | CCC | 9 contributors | High |
| 🧠 Governance | tools | #MetaAgent + 5 MAITs | Medium |

**Risks of dual purpose:**

| Risk | Impact |
|------|--------|
| User traffic competes with governance operations | Slower META responses |
| 9 users on single instance | Resource contention |
| Governance + user concerns mixed | Operational complexity |
| Single point of failure | Both user + governance down together |

### The Solution — Separation of Concerns

```
BEFORE (INT-P01 = everything):

INT-P01 (AI.WeOwn.Agency)
├── CCC workspace (9 contributors)
├── tools workspace (#MetaAgent + 5 MAITs)
└── ADMIN workspace

AFTER (separated):

INT-S003 (s003.ccc.bot)                    INT-P01 (AI.WeOwn.tools)
├── CCC workspace (6 contributors)         ├── CCC workspace (GTM + THY + RMN only)
└── tools workspace (minimal)              ├── tools workspace (#MetaAgent + 5+ MAITs)
                                           └── ADMIN workspace
User-facing                                Governance-focused
```

### Architecture — Before vs After

```
BEFORE:
┌─────────────────────────────────────────────────┐
│  INT-P01 (AI.WeOwn.Agency)                       │
│  ┌─────────┐ ┌──────────┐ ┌─────────┐          │
│  │ CCC     │ │ tools    │ │ ADMIN   │          │
│  │ 9 users │ │ META+5   │ │         │          │
│  │         │ │ MAITs    │ │         │          │
│  └─────────┘ └──────────┘ └─────────┘          │
└─────────────────────────────────────────────────┘

AFTER:
┌──────────────────────────┐  ┌──────────────────────────┐
│  INT-S003                │  │  INT-P01                  │
│  (s003.ccc.bot)          │  │  (AI.WeOwn.tools)         │
│  ┌─────────┐             │  │  ┌─────────┐ ┌──────────┐│
│  │ CCC     │             │  │  │ CCC     │ │ tools    ││
│  │ 6 users │             │  │  │ 3 users │ │ META+5+  ││
│  │ @LFG    │             │  │  │ @GTM    │ │ MAITs    ││
│  │ @LDC    │             │  │  │ @THY    │ │ EXPANDED ││
│  │ @SHD    │             │  │  │ @RMN    │ │          ││
│  │ @CEO    │             │  │  └─────────┘ └──────────┘│
│  │ @IAL    │             │  │                           │
│  │ @CRO    │             │  │  🧠 GOVERNANCE HUB       │
│  └─────────┘             │  │  Full resources for META  │
│  📅 Seasonal (→ W22)    │  │  + SME operations         │
└──────────────────────────┘  └──────────────────────────┘
```

---

## 📋 Deliverable 1: Deploy INT-S003

### Instance Identity

| Field | Value |
|-------|-------|
| Instance ID | **INT-S003** |
| Domain | **s003.ccc.bot** |
| Type | Seasonal Shared Instance (D-057, R-210) |
| Season | #WeOwnSeason003 🚀 |
| Purpose | #SharedInstance for contributors WITHOUT #HomeInstance |
| Active Period | W10 (Mon 02 Mar 2026) → W22 (Sun 31 May 2026) |
| Decommission | End of #WeOwnSeason003 (R-210) |
| Platform | AnythingLLM |
| LLM | Claude Opus 4.6 (`claude-opus-4-6`) |
| Embedder | Qwen3 Embedding 4B |

### What INT-S003 Provides

| Feature | Detail |
|---------|--------|
| CCC workspace | ✅ CCC-ID generation for 6 contributors |
| #PinnedDocs | ✅ 4 docs (SharedKernel, BEST-PRACTICES, PROTOCOLS, CCC) |
| ChatHistory | 40 (BP-061) |
| BP-065 | ✅ Shared instance self-ID required |
| ISC | ✅ Required (BP-059) — 8-point checklist |
| #ContextVolley | ✅ Can reach #MetaAgent @ INT-P01:tools |

### What INT-S003 Does NOT Have

| Feature | Reason |
|---------|--------|
| tools workspace | Not needed — governance stays on INT-P01 |
| #MetaAgent | Lives on INT-P01 |
| MAIT threads | Live on INT-P01 |
| ADMIN workspace | Optional — @GTM_ADMIN manages remotely |

---

## 📋 Deliverable 2: Evolve INT-P01 → AI.WeOwn.tools

### Evolution Plan

| Aspect | Before | After |
|--------|--------|-------|
| Primary purpose | Mixed (users + governance) | **Governance-focused** |
| CCC workspace users | 9 contributors | **3** (GTM + THY + RMN) |
| tools workspace | #MetaAgent + 5 MAITs | #MetaAgent + 5+ MAITs (**expanded capacity**) |
| User load | High | **Low** |
| MAIT capacity | Shared with user traffic | **Dedicated** |
| **Domain** | **AI.WeOwn.Agency** | **AI.WeOwn.tools** (primary — migrated) |

### What Changes on INT-P01

| Change | Detail |
|--------|--------|
| Remove 6 user accounts | @LFG, @LDC, @SHD, @CEO, @IAL, @CRO → INT-S003 |
| Update System Prompt | Reflect 3-user CCC workspace + AI.WeOwn.tools domain |
| Update CCC Workspace Prompt | Registered Users = 3 + domain = AI.WeOwn.tools |
| Update tools Workspace Prompt | Domain references → AI.WeOwn.tools |
| Optimize resources | Fewer users = more capacity for MAITs |
| **Domain migration** | **AI.WeOwn.Agency → AI.WeOwn.tools (DNS + SSL)** |
| **Thread URLs** | **ALL thread URLs update: ai.weown.agency → ai.weown.tools** |
| **Prompt references** | **ALL workspace prompts update domain references** |

### What Stays the Same on INT-P01

| Aspect | Value |
|--------|-------|
| Instance ID | INT-P01 |
| #MetaAgent thread UUID | cc965930-dfad-47ec-b576-22b38b1024a2 (unchanged) |
| ALL MAIT thread UUIDs | Unchanged |
| ALL Tool Agents | Unchanged |
| #PinnedDocs | 4 docs |
| Level in hierarchy | Level 2 — Production |
| #FedArch role | Central governance hub |
| AI.WeOwn.Agency | **Redirect → AI.WeOwn.tools** (optional — preserves old links) |

---

## 📋 User Migration Matrix

### Migration Direction

| CCC | Contributor | FROM | TO | Reason |
|-----|-------------|------|-----|--------|
| **LFG** | CoachLFG | INT-P01 | **INT-S003** | No #HomeInstance — seasonal shared |
| **LDC** | Dhruv | INT-P01 | **INT-S003** | No #HomeInstance — seasonal shared |
| **SHD** | Shahid | INT-P01 (interim R-211) | **INT-S003** | Interim → seasonal shared |
| **CEO** | Stephanie Warlick | INT-P01 | **INT-S003** | No #HomeInstance — seasonal shared |
| **IAL** | IamLotus | INT-P01 | **INT-S003** | No #HomeInstance — seasonal shared |
| **CRO** | Webb | INT-P01 | **INT-S003** | No #HomeInstance — seasonal shared |

### Remaining on INT-P01

| CCC | Contributor | Reason |
|-----|-------------|--------|
| **GTM** | yonks | Co-Founder — governance + #MetaAgent access |
| **THY** | mrsyonks | Co-Founder — governance access |
| **RMN** | Roman | AI Platform Engineer — infrastructure access |

### Migration Checklist (Per User)

| # | Step | Owner |
|---|------|-------|
| 1 | Create `u-<ccc>_user` on INT-S003 | @GTM_ADMIN |
| 2 | Upload USER-IDENTITY to INT-S003 RAG | @GTM_ADMIN |
| 3 | Verify CCC-ID generation on INT-S003 | @GTM |
| 4 | Notify contributor of new instance | @GTM |
| 5 | Deliver BP-065 self-ID instructions | @GTM |
| 6 | Verify R-212 deconfliction (if active on both during transition) | @GTM |
| 7 | Remove user from INT-P01 (after verification) | @GTM_ADMIN |

---

## 📋 12-Step Deployment Checklist — INT-S003

| # | Step | Owner | Details | Status |
|---|------|-------|---------|--------|
| 1 | **Create Droplet** | @SHD | DigitalOcean — 4 vCPU / 8 GB / 80 GB / ATL1 / Ubuntu 24.04 | ⬜ |
| 2 | **DNS** | @SHD | Point s003.ccc.bot → Droplet IP (Porkbun — CCC.bot domain) | ⬜ |
| 3 | **Docker + Compose** | @SHD | Install Docker Engine + Docker Compose | ⬜ |
| 4 | **Deploy AnythingLLM** | @SHD | `docker compose up -d` — AnythingLLM + Caddy | ⬜ |
| 5 | **SSL Verify** | @SHD | Confirm Caddy auto-SSL for s003.ccc.bot | ⬜ |
| 6 | **LLM Config** | @SHD | Set Claude Opus 4.6 (`claude-opus-4-6`) via OpenRouter | ⬜ |
| 7 | **Embedder Config** | @SHD | Set Qwen3 Embedding 4B | ⬜ |
| 8 | **System Prompt** | @GTM | INT-S003 identity (seasonal shared, 6 users) | ⬜ |
| 9 | **Workspaces + Prompts** | @GTM | CCC workspace + prompt (self-contained per L-132) | ⬜ |
| 10 | **#PinnedDocs + Users + ChatHistory** | @GTM | 4 docs; 6 users; ChatHistory = 40 | ⬜ |
| 11 | **#SmokeTest** | @GTM | 4-point verification | ⬜ |
| 12 | **ISC** | @GTM | TMPL-010 — Instance Season Certification (8/8) | ⬜ |

### Dependencies

| Step | Depends On |
|------|-----------|
| 2 (DNS) | 1 (Droplet — need IP) |
| 4 (Deploy) | 3 (Docker installed) |
| 5 (SSL) | 2 (DNS propagated) + 4 (Caddy running) |
| 6-7 (Models) | 4 (AnythingLLM running) |
| 8-10 (Config) | 6-7 (Models set) |
| 11 (#SmokeTest) | 8-10 (Config complete) |
| 12 (ISC) | 11 (#SmokeTest pass) |

### Docker Compose — INT-S003

```yaml
version: '3.8'

services:
  anythingllm:
    image: mintplexlabs/anythingllm:latest
    container_name: anythingllm
    restart: unless-stopped
    ports:
      - "3001:3001"
    volumes:
      - anythingllm_storage:/app/server/storage
    environment:
      - STORAGE_DIR=/app/server/storage
    cap_add:
      - SYS_ADMIN

  caddy:
    image: caddy:2-alpine
    container_name: caddy
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./Caddyfile:/etc/caddy/Caddyfile
      - caddy_data:/data
      - caddy_config:/config

volumes:
  anythingllm_storage:
  caddy_data:
  caddy_config:
```

### Caddyfile

```
s003.ccc.bot {
    reverse_proxy anythingllm:3001
}
```

---

## 📋 INT-P01 Evolution Plan

### Step-by-Step

| # | Step | Owner | Detail |
|---|------|-------|--------|
| 1 | Verify INT-S003 is LIVE + ISC 8/8 | @GTM | Must pass before migration |
| 2 | Migrate 6 users (per migration checklist) | @GTM_ADMIN | One at a time, verify each |
| 3 | **Configure DNS: AI.WeOwn.tools → INT-P01 IP** | **@SHD** | **Porkbun → A record → Droplet/K8s IP** |
| 4 | **Verify SSL: Caddy auto-SSL for AI.WeOwn.tools** | **@SHD** | **HTTPS working before URL updates** |
| 5 | **Update ALL thread URLs in prompts + docs** | **@GTM** | **ai.weown.agency → ai.weown.tools (see Cascade Impact)** |
| 6 | Update INT-P01 System Prompt | @GTM | Reflect 3-user instance + AI.WeOwn.tools domain |
| 7 | Update INT-P01 CCC Workspace Prompt | @GTM | Registered Users = GTM + THY + RMN + AI.WeOwn.tools |
| 8 | Update INT-P01 tools Workspace Prompt | @GTM | Domain refs → AI.WeOwn.tools |
| 9 | Remove migrated user accounts | @GTM_ADMIN | After all verified on INT-S003 |
| 10 | Verify INT-P01 #MetaAgent + MAITs unaffected | @GTM | All threads, UUIDs, agents intact |
| 11 | **Configure redirect: AI.WeOwn.Agency → AI.WeOwn.tools** | **@SHD** | **Optional — preserves old bookmarks** |
| 12 | #SmokeTest INT-P01 (post-evolution) | @GTM | 4-point verification |
| 13 | FULL:SYNC:META — log evolution complete | @GTM | Governance record |

---

## 📋 Thread URL Migration

| Thread | Old URL | New URL |
|--------|---------|---------|
| META | https://ai.weown.agency/workspace/tools/t/cc965930-dfad-47ec-b576-22b38b1024a2 | **https://ai.weown.tools/workspace/tools/t/cc965930-dfad-47ec-b576-22b38b1024a2** |
| MAIT_Deepnote.com | https://ai.weown.agency/workspace/tools/t/dfba7eba-9fc2-4fa6-acd0-132539a70f3f | **https://ai.weown.tools/workspace/tools/t/dfba7eba-9fc2-4fa6-acd0-132539a70f3f** |
| MAIT_AnythingLLM.com | https://ai.weown.agency/workspace/tools/t/76e9b360-5926-4157-a61c-ba9f878b37c0 | **https://ai.weown.tools/workspace/tools/t/76e9b360-5926-4157-a61c-ba9f878b37c0** |
| MAIT_Pinata.cloud | https://ai.weown.agency/workspace/tools/t/412ceea0-0b26-4009-b3e9-2a6453b85779 | **https://ai.weown.tools/workspace/tools/t/412ceea0-0b26-4009-b3e9-2a6453b85779** |
| MAIT_Paperless-ngx | https://ai.weown.agency/workspace/tools/t/6caf8b68-546a-4869-ad5e-f68706802c01 | **https://ai.weown.tools/workspace/tools/t/6caf8b68-546a-4869-ad5e-f68706802c01** |

> UUIDs are UNCHANGED. Only the domain prefix changes.

### URL Pattern

| Old Pattern | New Pattern |
|-------------|-------------|
| `https://ai.weown.agency/workspace/<ws>/t/<uuid>` | `https://ai.weown.tools/workspace/<ws>/t/<uuid>` |
| `https://ai.weown.agency/` | `https://ai.weown.tools/` |

---

## 📋 Timeline

| Week | Phase | Deliverables |
|------|-------|-------------|
| **W10 (Mar 2-8)** | **Deploy + Migrate** | INT-S003 live, 6 users migrated, INT-P01 evolved |
| **W11 (Mar 9-15)** | **Verify** | #SmokeTest both, ISC INT-S003, verify #ContextVolley |

### Detailed W10 Schedule

| Day | Activity | Owner |
|-----|---------|-------|
| Mon | Droplet (INT-S003) + Docker + DNS (s003.ccc.bot) | @SHD |
| Tue | SSL (INT-S003) + Models + System Prompt | @SHD + @GTM |
| Wed | INT-S003: Workspaces + Prompts + #PinnedDocs + Users | @GTM |
| Thu | INT-S003: #SmokeTest + ISC | @GTM |
| **Thu** | **DNS: AI.WeOwn.tools → INT-P01 IP** | **@SHD** |
| **Thu** | **SSL: Verify Caddy auto-SSL for AI.WeOwn.tools** | **@SHD** |
| Fri | User migration (6 users) → INT-S003 | @GTM_ADMIN |
| Fri | INT-P01 evolution (prompts, users, domain refs) | @GTM |
| **Fri** | **Update ALL thread URLs (ai.weown.agency → ai.weown.tools)** | **@GTM** |
| **Fri** | **Optional: AI.WeOwn.Agency → AI.WeOwn.tools redirect** | **@SHD** |

---

## 📋 ISC Certification — INT-S003

| # | Check | Pass Criteria | Status |
|---|-------|---------------|--------|
| 1 | EMBEDDER | Qwen3 Embedding 4B | ⬜ |
| 2 | LLM MODEL | Claude Opus 4.6 (`claude-opus-4-6`) | ⬜ |
| 3 | #PinnedDocs | 4 docs @ v3.1.x.x | ⬜ |
| 4 | SYSTEM PROMPT | #WeOwnSeason003 🚀 + INSTANCE IDENTITY (R-213) | ⬜ |
| 5 | WORKSPACE PROMPTS | BP-053 + BP-054 + BP-061 (ChatHistory=40) | ⬜ |
| 6 | USER-IDENTITY | 6 users current | ⬜ |
| 7 | RAG SYNC | GitHub connector refreshed | ⬜ |
| 8 | #ContextVolley | Can reach #MetaAgent @ INT-P01:tools | ⬜ |

---

## 📋 Infrastructure

### INT-S003 Spec

| Field | Value |
|-------|-------|
| Platform | DigitalOcean Droplet |
| Plan | Basic — 4 vCPU / 8 GB / 80 GB |
| Datacenter | **ATL1** |
| Cost | **~$48/mo** |
| Deployment | Docker Compose (Caddy + AnythingLLM) |
| Domain | s003.ccc.bot |
| DNS | Porkbun (CCC.bot domain) |

### Cost Impact

| Instance | Before | After | Delta |
|----------|--------|-------|-------|
| INT-P01 | $48/mo (K8s shared) | $48/mo (unchanged) | $0 |
| INT-S003 | $0 (doesn't exist) | **$48/mo** (new Droplet) | **+$48** |
| **TOTAL** | **$48** | **$96** | **+$48/mo** |

---

## 📋 Project Team

| CCC | Role | Focus |
|-----|------|-------|
| **GTM** | **Owner** | Architecture, prompts, migration, ISC, evolution |
| **SHD** | **DevOps** | Droplet provisioning, Docker, DNS, SSL |
| **RMN** | **Platform** | Infrastructure guidance, INT-P01 optimization |

---

## 📋 Risk Matrix

| # | Risk | Probability | Impact | Mitigation |
|---|------|-------------|--------|------------|
| 1 | @SHD unavailable W10 | Medium | High | @RMN backup; PRJ-009 pattern documented |
| 2 | DNS propagation delay | Low | Medium | Configure Mon, 48h buffer |
| 3 | User migration breaks CCC-ID sequence | Medium | High | R-212 deconfliction during transition |
| 4 | INT-P01 #MetaAgent disrupted | Low | Critical | Evolution AFTER INT-S003 verified |
| 5 | Contributors confused by instance change | Medium | Medium | Clear communication + BP-065 instructions |
| 6 | API key management (2 instances) | Low | Medium | BP-064 rotation for both |
| 7 | Cost increase not approved | Low | Medium | $48/mo = justified by separation of concerns |
| 8 | INT-S003 decommission forgotten | Low | Medium | R-210 + calendar reminder W22 |
| 9 | **Thread URL references break during migration** | **Medium** | **High** | **Update ALL prompts + docs BEFORE DNS cutover; verify each thread URL resolves on AI.WeOwn.tools; keep AI.WeOwn.Agency redirect active as fallback** |

---

## 📋 Decommission Plan — INT-S003

Per R-210:

| # | Step | Owner | Deadline |
|---|------|-------|----------|
| 1 | Archive RAG data | @GTM_ADMIN | W22 (Sun 25 May) |
| 2 | Export session logs | @GTM_ADMIN | W22 |
| 3 | Migrate any remaining users | @GTM | W22 |
| 4 | Docker compose down | @SHD | W23 (Sun 01 Jun) |
| 5 | DNS cleanup | @SHD | W23 |
| 6 | Destroy Droplet | @SHD | W23 |
| 7 | FULL:SYNC:META — decommission logged | @GTM | W23 |

### Data Retention

| Data | Retain? | Where |
|------|---------|-------|
| Session logs | ✅ YES | RAG (INT-P01) — R-199 |
| CCC-IDs generated | ✅ YES | Archived |
| USER-IDENTITY docs | ✅ YES | `_USERS_/` |
| System/Workspace prompts | ✅ YES | GH (fedarch) |
| User accounts | ❌ NO | Deleted with instance |
| RAG embeddings | ❌ NO | Deleted with instance |

### What Happens to Users at Decommission

| CCC | #WeOwnSeason004 Target |
|-----|------------------------|
| LFG | INT-OG9 (AI.CoachLFG.com) — if deployed |
| LDC | INT-S004 or personal #HomeInstance |
| SHD | INT-S004 or personal #HomeInstance |
| CEO | INT-S004 or personal #HomeInstance |
| IAL | INT-OG4 — if deployed |
| CRO | INT-OG7 — if deployed |

---

## 📋 #ContextSwap Log

| # | OLD | NEW | Contributor | Reason | CCC-ID |
|---|-----|-----|-------------|--------|--------|
| 9 | AI.WeOwn.Agency | **AI.WeOwn.tools** | @GTM | INT-P01 domain migration — governance hub identity; separation of concerns (PRJ-014) | GTM_2026-W09_098 |

---

## 📋 Cascade Impact — Domain Migration

### Documents Requiring URL Update

| Document | Location | URLs to Update |
|----------|----------|---------------|
| **SharedKernel** | _SYS_/ | META thread URL, ALL MAIT thread URLs, INT-P01 domain |
| **BEST-PRACTICES** | _SYS_/ | Any INT-P01 URL references |
| **PROTOCOLS** | _SYS_/ | #ContextVolley examples with INT-P01 URLs |
| **CCC** | _SYS_/ | AI Instance URL |
| INT-P01 System Prompt | Instance config | Domain, identity |
| INT-P01 CCC Workspace Prompt | Workspace config | META thread URL, response headers |
| INT-P01 tools Workspace Prompt | Workspace config | META thread URL, ALL MAIT URLs |
| INT-OG1 CCC Workspace Prompt | Workspace config | META thread URL |
| INT-OG8 System Prompt | Instance config | META thread URL (if referenced) |
| ALL USER-IDENTITY docs | _USERS_/ | Instance domain references |
| ALL ISC attestations | _INSTANCE_/ | Instance domain references |

### Cascade Sequence

| # | Step | Description |
|---|------|-------------|
| 1 | **DNS live** | AI.WeOwn.tools resolves to INT-P01 IP |
| 2 | **SSL verified** | HTTPS working on AI.WeOwn.tools |
| 3 | **Workspace prompts updated** | INT-P01 CCC + tools prompts → AI.WeOwn.tools URLs |
| 4 | **System Prompt updated** | INT-P01 identity → AI.WeOwn.tools |
| 5 | **_SYS_/ docs updated** | SharedKernel, BP, PROTO, CCC → AI.WeOwn.tools URLs |
| 6 | **GH push** | All updated docs → CCCbotNet/fedarch |
| 7 | **RAG sync** | All instances refresh RAG |
| 8 | **Remote prompts updated** | INT-OG1, INT-OG8 CCC prompts → AI.WeOwn.tools META URL |
| 9 | **Redirect configured** | AI.WeOwn.Agency → AI.WeOwn.tools (optional) |
| 10 | **Verify** | All thread URLs resolve on new domain |

---

## 📋 Relationship to Other Projects

| PRJ | Title | Relationship |
|-----|-------|-------------|
| PRJ-009 | #FedArchExpansion — ETHDenver.CCC.bot | Deployment pattern reuse (Docker Compose) |
| PRJ-013 | Paperless-ngx | INT-S003 users will use Paperless for #WeeklySummary |

### Instance Hierarchy — After PRJ-014

| Level | Instance | Role | Status |
|-------|----------|------|--------|
| **1** | INT-M01 | META.ccc.bot — Governance Hub | ⬜ PLANNED |
| **2** | **INT-P01** | **AI.WeOwn.tools — Governance Hub** | ✅ **EVOLVED** |
| **2** | INT-P02 | Lite.BurnedOut.xyz — BurnedOut | ✅ ACTIVE |
| **3** | INT-OG1 | AI.YonksTEAM.xyz — @GTM + @THY | ✅ ACTIVE |
| **3** | INT-OG8 | AI.RomanDiD.xyz — @RMN | ✅ ACTIVE |
| **4** | **INT-S003** | **s003.ccc.bot — Seasonal Shared** | 🆕 **NEW** |

---

## 📋 Discovered By (BP-047)

| CCC | Contributor | Role | Context |
|-----|-------------|------|---------|
| GTM | [yonks](https://GitHub.com/YonksTEAM) | Co-Founder / Chief Digital Alchemist | #FedArchExpansion — separation of user-facing and governance concerns — W09 |

---

## 📋 Related Documents

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| PRJ-009_FedArchExpansion_ETHDenver-CCC-bot | v3.1.2.1 | GTM_2026-W07_217 | GTM_2026-W07_228 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-009_FedArchExpansion_ETHDenver-CCC-bot.md) |
| SharedKernel | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/SharedKernel.md) |
| TMPL-010_ISC | v3.1.2.1 | GTM_2026-W07_071 | GTM_2026-W07_084 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_TEMPLATES_/TMPL-010_ISC.md) |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| 3.1.4.2 | 2026-W09 | GTM_2026-W09_086 | GTM_2026-W09_099 | +#ContextSwap #9 (AI.WeOwn.Agency → AI.WeOwn.tools — actual domain migration); +DNS migration steps (3, 4, 11); +Thread URL Migration section (5 threads); +Cascade Impact section (11 docs, 10-step sequence); +Risk #9 (thread URL references); Evolution Plan 8 → 13 steps; W10 schedule +4 DNS tasks; TOC → 20 items; FULL PRESERVE from v3.1.4.1 (L-097) |
| 3.1.4.1 | 2026-W09 | GTM_2026-W09_086 | GTM_2026-W09_093 | Initial project; dual deliverable (INT-S003 deploy + INT-P01 evolution); 6-user migration matrix; 12-step deployment checklist (PRJ-009 pattern); WeOwn.tools concept; ISC 8-point required; W10-W11 timeline; $48/mo cost; decommission plan (end S003); 8-risk matrix; Docker Compose + Caddy; s003.ccc.bot domain |

---

#FlowsBros #FedArch #FedArchExpansion #WeOwnTools #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
