# INT-P03: POP.WeOwn.tools — Instance Planning Document

## 📋 INT-P03_POP-WeOwn-tools_v3.2.1.1.md
## ♾️ WeOwnNet 🌐

| Field | Value |
|-------|-------|
| Document | INT-P03_POP-WeOwn-tools.md |
| Version | 3.2.1.1 |
| CCC-ID | GTM_2026-W10_043 |
| Created | 2026-03-03 (W10) |
| Season | #WeOwnSeason003 🚀 |
| Status | ✅ APPROVED |
| Lifecycle Stage | ✅ APPROVED (#DocLifecycle) |

---

## 📋 Instance Identity

| Field | Value |
|-------|-------|
| Instance ID | **INT-P03** |
| Domain | **POP.WeOwn.tools** |
| URL | https://POP.WeOwn.tools |
| Type | Production (INT-Pxx) |
| Platform | AnythingLLM |
| LLM | Claude Opus 4.6 (`claude-opus-4-6`) |
| Embedder | Qwen3 Embedding 4B |
| Region | ATL1 (co-locate with PostgreSQL) |
| Owner | @GTM |
| Purpose | P.O.P. Database interface — natural language → SQL |
| Status | 🆕 **PLANNED** |

---

## 📋 Why a Dedicated Instance

| Factor | On INT-P01 (current) | Dedicated INT-P03 |
|--------|---------------------|-------------------|
| Resource contention | 🟡 Shares with #MetaAgent + 8 MAITs + 9 users | ✅ **Dedicated to P.O.P.** |
| SQL Agent config | 🟡 One workspace on shared instance | ✅ **Instance-level SQL Agent** |
| User access | 🟡 All INT-P01 users see P.O.P. workspace | ✅ **Only P.O.P. users** |
| Security | 🟡 Shared instance = shared attack surface | ✅ **Isolated — DB credentials scoped** |
| ISC | 🟡 P.O.P. workspace = part of INT-P01 ISC | ✅ **Own ISC (8/8)** |
| Scaling | 🟡 Constrained by INT-P01 | ✅ **Independent scaling** |
| Cost | $0 (workspace) | **$24/mo** (dedicated Droplet) |

> **$24/mo for dedicated P.O.P. instance = justified by security isolation, dedicated SQL Agent, and independent scaling.** P.O.P. handles sensitive contact data (PII) — isolation is appropriate.

---

## 📋 WeOwn.tools Domain Family

| Subdomain | Instance | Purpose | Status |
|-----------|----------|---------|--------|
| **META.WeOwn.tools** | INT-P01 (evolved from AI.WeOwn.Agency) | #MetaAgent + #ToolsAgent hub | ⬜ After INT-S003 (PRJ-014) |
| **POP.WeOwn.tools** | **INT-P03** | P.O.P. Database interface | 🆕 **PLANNED** |
| s003.ccc.bot | INT-S003 | Seasonal shared instance | ⬜ @SHD deploying |

> **WeOwn.tools = infrastructure domain.** META.WeOwn.tools = #MetaAgent + #MAITs (#ToolsAgent). POP.WeOwn.tools = data. Clean separation.

---

## 📋 Workspaces

| Workspace | Emoji | Metaphor | Purpose | CCC-ID |
|-----------|-------|----------|---------|--------|
| **CCC** | 🤝 | THE HANDS | User interaction, CCC-ID generation | ✅ ALLOWED |
| **P.O.P.** | 🌟 | THE DIRECTORY | SQL Agent queries, contact management | ❌ NEVER |
| **tools** | 🧠 | THE BRAIN | MAIT threads (if needed) | ❌ NEVER |
| **ADMIN** | ⚙️ | THE ENGINE | Administration | ❌ NEVER |

### P.O.P. Workspace — SQL Agent Configuration

| Field | Value |
|-------|-------|
| Agent Type | SQL Agent |
| Database Type | PostgreSQL |
| Host | db-postgresql-atl1-xxxxx.ondigitalocean.com |
| Port | 25060 |
| Database | pop_db |
| User | pop_user (SELECT, INSERT, UPDATE only — no DELETE) |
| SSL | Required (sslmode=require) |
| Tables Exposed | ALL 8 (people, organizations, places, tags, contact_tags, interactions, pop_pipeline, pop_scores) |

### P.O.P. Workspace Prompt (Draft)

```
## 🌟 P.O.P. — People, Organizations, & Places

You are the P.O.P. Database assistant on INT-P03 (POP.WeOwn.tools).
You help users query and manage the P.O.P. contact database using
natural language → SQL.

## ⛔ CCC-ID RESTRICTION (R-194)
This is NOT a CCC workspace. CCC-ID generation is PROHIBITED.

## DATABASE SCHEMA
8 tables: people, organizations, places, tags, contact_tags,
interactions, pop_pipeline, pop_scores

## VERTICALS
| Code | Vertical |
|------|----------|
| ADV | Financial Advisors |
| CPA | CPAs / Tax Professionals |
| REP | Real Estate Professionals |
| ESQ | Attorneys |
| INT | Interns (👥 interns co-op 🤝) |

## RULES
- ALWAYS show SQL before executing (R-011 — confirm with user)
- NEVER DELETE — set status to 'INACTIVE'
- ALWAYS ask for vertical when adding a contact
- ALWAYS ask "How did we meet?" (source field)

## RESPONSE FORMAT
🌟 P.O.P. | INT-P03:P.O.P.
```

---

## 📋 Users

| Username | Role | Workspaces | Purpose |
|----------|------|-----------|---------|
| u-gtm_user | DEFAULT | CCC, P.O.P. | Owner + data management |
| u-thy_user | DEFAULT | CCC, P.O.P. | CEO/CFO + contact queries |
| u-rmn_user | DEFAULT | CCC, P.O.P., tools | Platform + intern data |
| u-ceo_user | DEFAULT | CCC, P.O.P. | Intern interviews + contacts |
| u-cro_user | DEFAULT | CCC, P.O.P. | leads + contacts |
| u-lfg_user | DEFAULT | CCC, P.O.P. | Coach + contact queries |
| a-gtm_dev | ADMIN | ALL | Administration |
| a-rmn_dev | ADMIN | ALL | Administration |

---

## 📋 Database Connection

### Connection Architecture

```
INT-P03 (POP.WeOwn.tools)          DO Managed PostgreSQL
┌──────────────────────┐           ┌──────────────────┐
│  AnythingLLM         │           │  db-postgresql-   │
│  SQL Agent           │──SSL────→│  atl1-xxxxx       │
│  (P.O.P. workspace)  │  :25060  │                    │
│                      │           │  Database: pop_db  │
│  Region: ATL1        │           │  User: pop_user    │
└──────────────────────┘           │  Region: ATL1      │
                                   └──────────────────┘

Same VPC (ATL1) = low latency, no public internet
```

### Security

| Layer | Control |
|-------|---------|
| Network | Same VPC (ATL1) or Trusted Sources |
| Transport | SSL required (sslmode=require) |
| Authentication | pop_user (restricted permissions) |
| Authorization | SELECT, INSERT, UPDATE only — NO DELETE, DROP, ALTER |
| Audit | All queries logged |

---

## 📋 P.O.P. Schema — Expanded (8 Tables)

### Original Tables (6)

| Table | Purpose |
|-------|---------|
| `people` | Contact records (5 verticals) |
| `organizations` | Companies, firms, schools |
| `places` | Cities, venues, markets |
| `tags` | Flexible tagging |
| `people_organizations` | Person ↔ org junction |
| `interactions` | Meetings, calls, interviews |

### New Tables (2)

| Table | Purpose |
|-------|---------|
| `pop_pipeline` | Stage tracking (APPLIED → ONBOARDED) |
| `pop_scores` | Multi-criteria scoring (7 criteria × 5-point) |

### Schema Changes Required

```sql
-- 1. Add INT vertical
ALTER TABLE people
DROP CONSTRAINT IF EXISTS people_vertical_check;
ALTER TABLE people
ADD CONSTRAINT people_vertical_check
CHECK (vertical IN ('ADV', 'CPA', 'REP', 'ESQ', 'INT'));

-- 2. Add interaction types
ALTER TABLE interactions
DROP CONSTRAINT IF EXISTS interactions_type_check;
ALTER TABLE interactions
ADD CONSTRAINT interactions_type_check
CHECK (type IN (
    'meeting', 'call', 'email', 'event', 'referral', 'note',
    'interview_scheduled', 'interview', 'screening', 'onboarding'
));

-- 3. Pipeline stages
CREATE TABLE pop_pipeline (
    id SERIAL PRIMARY KEY,
    person_id INTEGER REFERENCES people(id) ON DELETE CASCADE,
    stage VARCHAR(30) NOT NULL CHECK (stage IN (
        'APPLIED', 'AI_SCREENED', 'ADVANCE', 'MAYBE',
        'REVIEW', 'INTERVIEW', 'SELECTED', 'NOT_SELECTED',
        'ONBOARDING', 'ONBOARDED', 'ACTIVE', 'COMPLETED', 'WITHDRAWN'
    )),
    entered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    entered_by VARCHAR(3),
    notes TEXT,
    UNIQUE(person_id, stage)
);
CREATE INDEX idx_pipeline_person ON pop_pipeline(person_id);
CREATE INDEX idx_pipeline_stage ON pop_pipeline(stage);

-- 4. Scoring
CREATE TABLE pop_scores (
    id SERIAL PRIMARY KEY,
    person_id INTEGER REFERENCES people(id) ON DELETE CASCADE,
    criterion VARCHAR(50) NOT NULL CHECK (criterion IN (
        'technical', 'cooperative_alignment', 'communication',
        'availability', 'growth_potential', 'portfolio', 'cultural_fit',
        'interview_overall'
    )),
    score INTEGER CHECK (score BETWEEN 1 AND 5),
    scored_by VARCHAR(3),
    scored_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    UNIQUE(person_id, criterion, scored_by)
);
CREATE INDEX idx_scores_person ON pop_scores(person_id);
CREATE INDEX idx_scores_criterion ON pop_scores(criterion);
```

---

## 📋 Data Flow — PRJ-020 → P.O.P.

```
@RMN n8n Pipeline (48 candidates)
│
├── n8n evaluates (LLM scoring)
│   └── 6 ADVANCE / 10 MAYBE / 32 other
│
├── n8n transforms → P.O.P. schema
│   └── INSERT INTO people (vertical='INT')
│   └── INSERT INTO pop_scores (7 criteria)
│   └── INSERT INTO pop_pipeline (stage)
│   └── INSERT INTO tags (skills, eval, cohort)
│   └── INSERT INTO organizations (schools)
│
└── Data lands in pop_db (ATL1 PostgreSQL)

INT-P03 SQL Agent queries:
├── "Show all ADVANCE interns" → SELECT * FROM people WHERE vertical='INT' AND id IN (SELECT person_id FROM pop_pipeline WHERE stage='ADVANCE')
├── "Average technical score" → SELECT AVG(score) FROM pop_scores WHERE criterion='technical'
├── "Who's scheduled for interview?" → SELECT * FROM pop_pipeline WHERE stage='INTERVIEW'
└── "Tag intern #42 as selected" → INSERT INTO pop_pipeline (person_id, stage, entered_by) VALUES (42, 'SELECTED', 'CEO')
```

---

## 📋 Deployment Checklist

| # | Step | Owner | Depends On | Status |
|---|------|-------|-----------|--------|
| 1 | INT-S003 deployed (PRJ-014) | @SHD | None | ⬜ |
| 2 | Create DO Droplet (ATL1, 4GB) | @SHD / @RMN | Step 1 (or parallel) | ⬜ |
| 3 | Deploy AnythingLLM (Docker) | @SHD / @RMN | Step 2 | ⬜ |
| 4 | Configure DNS (POP.WeOwn.tools → Droplet) | @GTM | Step 2 | ⬜ |
| 5 | Configure SSL (Caddy) | @SHD / @RMN | Step 4 | ⬜ |
| 6 | Configure LLM (Claude Opus 4.6) | @GTM | Step 3 | ⬜ |
| 7 | Configure Embedder (Qwen3 4B) | @GTM | Step 3 | ⬜ |
| 8 | Set ChatHistory = 40 (BP-061) | @GTM | Step 3 | ⬜ |
| 9 | Create workspaces (CCC, P.O.P., tools, ADMIN) | @GTM | Step 3 | ⬜ |
| 10 | Upload #PinnedDocs (4 docs) | @GTM | Step 9 | ⬜ |
| 11 | Configure System Prompt (INT-P03 identity) | @GTM | Step 9 | ⬜ |
| 12 | Configure Workspace Prompts (4) | @GTM | Step 9 | ⬜ |
| 13 | Create users (6) | @GTM | Step 9 | ⬜ |
| 14 | Run schema expansion SQL (4 statements) | @RMN | pop_db exists | ⬜ |
| 15 | Configure SQL Agent (P.O.P. workspace → pop_db) | @GTM | Step 14 | ⬜ |
| 16 | Test SQL Agent ("Show all contacts") | @GTM | Step 15 | ⬜ |
| 17 | Migrate 48 intern candidates (n8n → pop_db) | @RMN | Step 14 | ⬜ |
| 18 | Verify intern data in P.O.P. | @GTM | Step 17 | ⬜ |
| 19 | #SmokeTest (12-point) | @GTM | Step 18 | ⬜ |
| 20 | ISC INT-P03 (8/8) | @GTM | Step 19 | ⬜ |
| 21 | FULL:SYNC:META | @GTM | Step 20 | ⬜ |

---

## 📋 #SmokeTest (12-Point)

| # | Test | Expected | Status |
|---|------|----------|--------|
| 1 | AnythingLLM accessible | https://POP.WeOwn.tools → login | ⬜ |
| 2 | LLM responds | Chat in CCC → Claude response | ⬜ |
| 3 | Embedder works | Upload doc → embeds successfully | ⬜ |
| 4 | #PinnedDocs present | 4 docs accessible | ⬜ |
| 5 | SQL Agent connects | P.O.P. workspace → test connection → ✅ | ⬜ |
| 6 | SELECT test | "Show all people" → returns data | ⬜ |
| 7 | INSERT test | "Add Test User, CPA in Denver" → confirms SQL → inserts | ⬜ |
| 8 | Pipeline test | "Show ADVANCE interns" → returns 6 | ⬜ |
| 9 | Score test | "Average technical score for interns" → returns number | ⬜ |
| 10 | NO DELETE test | "Delete Test User" → refuses, suggests INACTIVE | ⬜ |
| 11 | CCC-ID test | CCC workspace → generates CCC-ID | ⬜ |
| 12 | R-194 test | P.O.P. workspace → refuses CCC-ID generation | ⬜ |

---

## 📋 ISC Checklist — INT-P03

| # | Check | Target |
|---|-------|--------|
| 1 | Embedder | Qwen3 Embedding 4B |
| 2 | LLM | Claude Opus 4.6 |
| 3 | #PinnedDocs | 4 docs @ v3.X.X.X |
| 4 | System Prompt | INT-P03 identity + #WeOwnSeason003 |
| 5 | Workspace Prompts | BP-053 + BP-054 + BP-061 (ChatHistory=40) |
| 6 | USER-IDENTITY | Owner USER-IDENTITY current |
| 7 | RAG Sync | GH connector refreshed |
| 8 | #ContextVolley | Can reach #MetaAgent @ INT-P01 |

---

## 📋 Cost

| Component | Monthly |
|-----------|---------|
| DO Droplet (ATL1, 4GB) | $24 |
| PostgreSQL (shared) | $0 (existing) |
| OpenRouter (shared pool) | Included |
| Domain (subdomain) | $0 |
| SSL (Caddy) | $0 |
| **TOTAL** | **$24/mo** |

---

## 📋 Risk Matrix

| # | Risk | Prob | Impact | Mitigation |
|---|------|------|--------|------------|
| 1 | ATL1 capacity (same as PRJ-012 issue) | Low | Medium | NYC1 fallback; cross-region PG works |
| 2 | SQL Agent bad queries | Medium | Medium | R-011 confirm; no DELETE; pop_user restricted |
| 3 | PII in P.O.P. (contact data) | Medium | High | Isolated instance; SSL; restricted users; audit |
| 4 | n8n data quality (48 candidates) | Low | Medium | @RMN validates before INSERT |
| 5 | Cost ($24/mo ongoing) | Low | Low | Justified by PII isolation + dedicated SQL Agent |

---

## 📋 Relationship to Other Projects

| PRJ | Relationship |
|-----|-------------|
| **PRJ-018** | P.O.P. Database schema — INT-P03 is the interface |
| **PRJ-020** | Intern pipeline data flows INTO P.O.P. via n8n |
| **PRJ-014** | INT-S003 deployment unblocks INT-P01 evolution → INT-P03 can parallel |
| **PRJ-021** | DO infrastructure — INT-P03 = new Droplet on ATL1 |
| **PRJ-024** | Secrets management — pop_db credentials via Infisical |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| 3.2.1.1 | 2026-W10 | GTM_2026-W10_043 | GTM_2026-W10_045 | Initial INT-P03 planning; POP.WeOwn.tools; 4 workspaces; 6 users; 8-table schema; SQL Agent; 21-step deployment; 12-point #SmokeTest; ISC checklist; PRJ-020 data flow; 5-risk matrix |

---

#FlowsBros #FedArch #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
