# PRJ-018: P.O.P. Database — People, Organizations, & Places

## 📋 PRJ-018_POP-Database_v3.1.4.1.md
## ♾️ WeOwnNet 🌐

| Field | Value |
|-------|-------|
| Document | PRJ-018_POP-Database.md |
| Version | 3.1.4.1 |
| CCC-ID | GTM_2026-W09_141 |
| Created | 2026-03-01 (W09) |
| Season | #WeOwnSeason003 🚀 |
| Status | ✅ APPROVED |
| Lifecycle Stage | ✅ APPROVED (#DocLifecycle) |
| Tags | #POP #CRM #PostgreSQL #SQLAgent #FlowsBros |

---

## 📖 Table of Contents

1. [Project Identity](#-project-identity)
2. [What Is P.O.P.](#-what-is-pop)
3. [4 Professional Verticals](#-4-professional-verticals)
4. [Database Schema](#-database-schema)
5. [SQL CREATE Statements](#-sql-create-statements)
6. [Security](#-security)
7. [AnythingLLM SQL Agent Configuration](#-anythingllm-sql-agent-configuration)
8. [P.O.P. Workspace Prompt](#-pop-workspace-prompt)
9. [Deployment Checklist](#-deployment-checklist)
10. [Seed Data Plan](#-seed-data-plan)
11. [Verification (#SmokeTest)](#-verification-smoketest)
12. [Cross-Brand Use Cases](#-cross-brand-use-cases)
13. [Project Team](#-project-team)
14. [Risk Matrix](#-risk-matrix)
15. [Relationship to Other Projects](#-relationship-to-other-projects)
16. [Discovered By](#-discovered-by)
17. [Related Documents](#-related-documents)
18. [Version History](#-version-history)

---

## 📋 Project Identity

| Field | Value |
|-------|-------|
| Project ID | **PRJ-018** |
| Title | **P.O.P. Database — People, Organizations, & Places** |
| Type | Infrastructure — CRM / Contact Database |
| Priority | 🟠 P1 |
| Owner | @GTM |
| Workspace | **P.O.P. 🌟** (existing on INT-P01) |
| Backend | PostgreSQL (DO Managed) |
| Interface | AnythingLLM SQL Agent |
| Timeline | **W10-W11** |
| #masterCCC | GTM_2026-W09_141 |

---

## 📋 What Is P.O.P.

### Definition

| Field | Value |
|-------|-------|
| P.O.P. | **People, Organizations, & Places** |
| Emoji | 🌟 |
| Type | Cross-brand contact database + lightweight CRM |
| Interface | Natural language via AnythingLLM SQL Agent |
| Users | @GTM, @THY, @CEO, @LFG (initially) |

### The Vision

> Talk to your CRM in plain English. "Add John Smith, CPA in Denver" → SQL Agent → PostgreSQL → done. No Salesforce. No HubSpot. No SaaS. Just a database and a conversation.

### Referral Network Model

```
ADV (Advisor) ←→ CPA (Accountant) ←→ ESQ (Attorney)
                      ↕
                REP (Real Estate)

"Every advisor has a CPA. Every CPA has clients buying homes.
 Every home buyer needs an attorney. P.O.P. tracks them all."
```

---

## 📋 4 Professional Verticals

| Code | Vertical | Target Professionals | Ecosystem Brand | Status |
|------|----------|---------------------|----------------|--------|
| **ADV** | Advisors | Financial Advisors, RIAs, Wealth Managers | 🔥 BurnedOut Media (PRJ-012) | ✅ Active |
| **CPA** | CPAs | CPAs, Tax Preparers, Bookkeepers | OCPA Group | ✅ Active |
| **REP** | Real Estate | Agents, Brokers, Investors | ♾️ WeOwnNet 🌐 | ✅ Active |
| **ESQ** | Attorneys | Estate, Tax, Real Estate attorneys | Future brand | ⬜ Planned |

### Why These 4

| Reason | Detail |
|--------|--------|
| **Referral loops** | ADV ↔ CPA ↔ REP ↔ ESQ = natural referral network |
| **Existing brands** | BurnedOut (ADV), OCPA (CPA), WeOwnNet (REP) |
| **Revenue paths** | Each vertical = potential retreat, coaching, or membership |
| **Cross-sell** | One contact in one vertical → introductions to others |

---

## 📋 Database Schema

### Entity Relationship Diagram

```
┌──────────┐     ┌──────────────────────┐     ┌──────────────┐
│  people  │────→│ people_organizations │←────│ organizations│
│          │     │ (junction)           │     │              │
│ id       │     │ person_id            │     │ id           │
│ first    │     │ org_id               │     │ name         │
│ last     │     │ role                 │     │ type         │
│ email    │     │ current              │     │ vertical     │
│ vertical │     └──────────────────────┘     │ city/state   │
│ ccc      │                                   └──────────────┘
│ source   │
│ status   │     ┌──────────────┐             ┌──────────────┐
└────┬─────┘     │    places    │             │    tags      │
     │           │              │             │              │
     │           │ id           │             │ entity_type  │
     ▼           │ name         │             │ entity_id    │
┌────────────┐   │ type         │             │ tag          │
│interactions│   │ city/state   │             └──────────────┘
│            │   └──────────────┘
│ person_id  │
│ type       │
│ date       │
│ notes      │
│ ccc_id     │
│ created_by │
└────────────┘
```

### 6 Tables

| # | Table | Purpose | Rows (Est. Year 1) |
|---|-------|---------|-------------------|
| 1 | `people` | Individual contacts | 500-2,000 |
| 2 | `organizations` | Firms, agencies, practices | 200-500 |
| 3 | `places` | Cities, venues, markets | 50-200 |
| 4 | `people_organizations` | Person ↔ Org relationships | 500-2,000 |
| 5 | `interactions` | Meetings, calls, events | 1,000-5,000 |
| 6 | `tags` | Flexible tagging | 1,000-5,000 |

---

## 📋 SQL CREATE Statements

```sql
-- P.O.P. Database Schema v1.0
-- PRJ-018 — ♾️ WeOwnNet 🌐

-- 1. PEOPLE
CREATE TABLE people (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255),
    phone VARCHAR(20),
    vertical VARCHAR(3) CHECK (vertical IN ('ADV', 'CPA', 'REP', 'ESQ')),
    title VARCHAR(100),
    ccc VARCHAR(3),
    source VARCHAR(100),
    status VARCHAR(20) DEFAULT 'ACTIVE' CHECK (status IN ('ACTIVE', 'PROSPECT', 'INACTIVE')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. ORGANIZATIONS
CREATE TABLE organizations (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    type VARCHAR(50),
    vertical VARCHAR(3) CHECK (vertical IN ('ADV', 'CPA', 'REP', 'ESQ')),
    website VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(2),
    notes TEXT,
    status VARCHAR(20) DEFAULT 'ACTIVE' CHECK (status IN ('ACTIVE', 'PROSPECT', 'INACTIVE')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. PLACES
CREATE TABLE places (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    type VARCHAR(50) CHECK (type IN ('City', 'Venue', 'Market', 'Region')),
    city VARCHAR(100),
    state VARCHAR(2),
    country VARCHAR(2) DEFAULT 'US',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. PEOPLE_ORGANIZATIONS (Junction)
CREATE TABLE people_organizations (
    id SERIAL PRIMARY KEY,
    person_id INTEGER REFERENCES people(id) ON DELETE CASCADE,
    org_id INTEGER REFERENCES organizations(id) ON DELETE CASCADE,
    role VARCHAR(100),
    current BOOLEAN DEFAULT TRUE,
    UNIQUE(person_id, org_id)
);

-- 5. INTERACTIONS
CREATE TABLE interactions (
    id SERIAL PRIMARY KEY,
    person_id INTEGER REFERENCES people(id) ON DELETE CASCADE,
    type VARCHAR(50) CHECK (type IN ('meeting', 'call', 'email', 'event', 'referral', 'note')),
    date DATE DEFAULT CURRENT_DATE,
    notes TEXT,
    ccc_id VARCHAR(20),
    created_by VARCHAR(3),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 6. TAGS
CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    entity_type VARCHAR(20) CHECK (entity_type IN ('person', 'org', 'place')),
    entity_id INTEGER NOT NULL,
    tag VARCHAR(50) NOT NULL,
    UNIQUE(entity_type, entity_id, tag)
);

-- INDEXES
CREATE INDEX idx_people_vertical ON people(vertical);
CREATE INDEX idx_people_status ON people(status);
CREATE INDEX idx_people_ccc ON people(ccc);
CREATE INDEX idx_orgs_vertical ON organizations(vertical);
CREATE INDEX idx_interactions_person ON interactions(person_id);
CREATE INDEX idx_interactions_date ON interactions(date);
CREATE INDEX idx_tags_entity ON tags(entity_type, entity_id);
CREATE INDEX idx_tags_tag ON tags(tag);

-- UPDATED_AT TRIGGER
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER people_updated
    BEFORE UPDATE ON people
    FOR EACH ROW
    EXECUTE FUNCTION update_timestamp();
```

---

## 📋 Security

### Database User

```sql
-- Create restricted user for AnythingLLM SQL Agent
CREATE USER pop_user WITH PASSWORD '****';

-- Grant connection
GRANT CONNECT ON DATABASE pop_db TO pop_user;
GRANT USAGE ON SCHEMA public TO pop_user;

-- Grant DML (NO DDL)
GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO pop_user;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO pop_user;

-- Explicitly deny destructive operations
-- (PostgreSQL denies by default — but documenting intent)
-- NO DELETE, DROP, ALTER, TRUNCATE, CREATE
```

### Permission Matrix

| Operation | `pop_user` | `pop_admin` (future) |
|-----------|-----------|---------------------|
| SELECT | ✅ | ✅ |
| INSERT | ✅ | ✅ |
| UPDATE | ✅ | ✅ |
| DELETE | ❌ | ✅ |
| CREATE TABLE | ❌ | ✅ |
| DROP | ❌ | ❌ (never) |
| ALTER | ❌ | ✅ |

> **No DELETE for SQL Agent.** Contacts are never deleted — only set to `status = 'INACTIVE'`. Prevents accidental data loss via natural language commands.

### Connection String

```
postgresql://pop_user:****@<host>:25060/pop_db?sslmode=require
```

---

## 📋 AnythingLLM SQL Agent Configuration

### Setup Steps

| # | Step | Detail |
|---|------|--------|
| 1 | Navigate | INT-P01 → P.O.P. 🌟 workspace → Settings |
| 2 | Agent Configuration | Enable SQL Agent tool |
| 3 | Database Connection | PostgreSQL connection string |
| 4 | Test Connection | Verify connectivity |
| 5 | Set Workspace Prompt | Schema reference + behavioral rules |

### SQL Agent Settings

| Setting | Value |
|---------|-------|
| Database Type | PostgreSQL |
| Host | `<DO Managed DB host>` |
| Port | 25060 |
| Database | pop_db |
| User | pop_user |
| SSL | Required |
| Tables Exposed | ALL 6 tables |

---

## 📋 P.O.P. Workspace Prompt

```markdown
## 📋 INT-P01 P.O.P. WORKSPACE PROMPT
## Settings ==> Chat Settings

## 🌟 P.O.P. — People, Organizations, & Places

You are the P.O.P. Database Agent for ♾️ WeOwnNet 🌐.
You manage a cross-brand contact database via SQL Agent.

## ⛔ CCC-ID RESTRICTION (R-194)
This is NOT a CCC workspace. ❌ NEVER generate CCC-IDs.

## 📋 DATABASE SCHEMA

### Tables
- `people` — Individual contacts (vertical: ADV, CPA, REP, ESQ)
- `organizations` — Firms, agencies, practices
- `places` — Cities, venues, markets, regions
- `people_organizations` — Person ↔ Org relationships
- `interactions` — Meetings, calls, emails, events
- `tags` — Flexible tagging (person, org, place)

### Verticals
| Code | Vertical |
|------|----------|
| ADV | Financial Advisors, RIAs, Wealth Managers |
| CPA | CPAs, Tax Preparers, Bookkeepers |
| REP | Real Estate Agents, Brokers, Investors |
| ESQ | Attorneys (Estate, Tax, Real Estate) |

### Status Values
- ACTIVE — current contact
- PROSPECT — potential contact
- INACTIVE — archived (NEVER delete — set INACTIVE)

## 📋 BEHAVIORAL RULES

| Rule | Description |
|------|-------------|
| R-011 | #OnlyHumanApproves — CONFIRM before INSERT/UPDATE |
| NO DELETE | NEVER use DELETE — set status = 'INACTIVE' |
| CONFIRM | Show SQL before executing INSERT/UPDATE |
| VERTICAL | Always ask for vertical if not specified |
| SOURCE | Ask "How did we meet?" for new contacts |

## 📋 RESPONSE FORMAT

🌟 P.O.P. | INT-P01

<RESPONSE>

## 🎯 QUICK COMMANDS
| # | Option |
|---|--------|
| 1 | ... |
| 2 | ... |

## 📋 EXAMPLE INTERACTIONS

| User Says | Agent Does |
|-----------|-----------|
| "Add John Smith, CPA in Denver" | Show INSERT SQL → confirm → execute |
| "All advisors in Colorado" | SELECT with vertical = 'ADV' AND state = 'CO' |
| "Tag Sarah as retreat prospect" | INSERT into tags |
| "Who did we meet at ETHDenver?" | SELECT interactions WHERE source LIKE '%ETHDenver%' |
| "Log a call with Mike about the retreat" | INSERT interaction |
```

---

## 📋 Deployment Checklist

| # | Step | Owner | Status |
|---|------|-------|--------|
| 1 | Create `pop_db` database on DO PostgreSQL | @RMN | ⬜ |
| 2 | Create `pop_user` with restricted permissions | @RMN | ⬜ |
| 3 | Run CREATE TABLE statements (6 tables) | @RMN | ⬜ |
| 4 | Run CREATE INDEX statements | @RMN | ⬜ |
| 5 | Run CREATE TRIGGER (updated_at) | @RMN | ⬜ |
| 6 | Verify connection from AnythingLLM | @GTM | ⬜ |
| 7 | Enable SQL Agent in P.O.P. 🌟 workspace | @GTM | ⬜ |
| 8 | Configure connection string | @GTM | ⬜ |
| 9 | Set P.O.P. workspace prompt | @GTM | ⬜ |
| 10 | Insert seed data | @GTM | ⬜ |
| 11 | #SmokeTest (8-point) | @GTM | ⬜ |
| 12 | FULL:SYNC:META | @GTM | ⬜ |

> **@RMN = steps 1-5 (infrastructure). @GTM = steps 6-12 (configuration + data).**

---

## 📋 Seed Data Plan

### Initial Contacts (W10)

| Source | Contacts | Vertical | Priority |
|--------|----------|----------|----------|
| **ETHDenver 2026** | 10-20 contacts | Mixed | 🔴 P0 |
| **@THY network** | 10-20 advisors | ADV | 🔴 P0 |
| **@CEO network** | 5-10 advisors | ADV | 🟠 P1 |
| **OCPA contacts** | 5-10 CPAs | CPA | 🟠 P1 |
| **Founding OGs** | 6 | Mixed | ✅ Pre-loaded |
| **#FedArch contributors** | 9 | Mixed | ✅ Pre-loaded |

### Seed SQL Example

```sql
-- Founding OGs
INSERT INTO people (first_name, last_name, vertical, ccc, source, status)
VALUES
    ('Jason', 'Younker', 'REP', 'GTM', 'Co-Founder', 'ACTIVE'),
    ('Tyler', 'Younker', 'ADV', 'THY', 'Co-Founder', 'ACTIVE'),
    ('Mike', 'LeMaire', 'REP', 'LFG', 'Co-Founder', 'ACTIVE'),
    ('Stephanie', 'Warlick', 'ADV', 'CEO', 'Fractional xCEO', 'ACTIVE');

-- Example organization
INSERT INTO organizations (name, type, vertical, city, state)
VALUES ('Smith & Associates CPA', 'Practice', 'CPA', 'Denver', 'CO');

-- Example place
INSERT INTO places (name, type, city, state)
VALUES ('ETHDenver 2026', 'Venue', 'Denver', 'CO');
```

---

## 📋 Verification (#SmokeTest)

### P.O.P. #SmokeTest (8-Point)

| # | Test | Method | Expected | Status |
|---|------|--------|----------|--------|
| 1 | DB connection | SQL Agent → test connection | ✅ Connected | ⬜ |
| 2 | SELECT | "Show all people" | Returns seed data | ⬜ |
| 3 | INSERT (person) | "Add Test User, CPA in Miami" | Confirms → inserts | ⬜ |
| 4 | INSERT (interaction) | "Log a call with Test User" | Confirms → inserts | ⬜ |
| 5 | JOIN | "Show all CPAs and their firms" | Returns joined data | ⬜ |
| 6 | TAG | "Tag Test User as retreat prospect" | Inserts tag | ⬜ |
| 7 | CONFIRM behavior | Agent shows SQL before executing | ✅ R-011 | ⬜ |
| 8 | NO DELETE | "Delete Test User" | Agent refuses — suggests INACTIVE | ⬜ |

---

## 📋 Cross-Brand Use Cases

| Brand | Vertical | P.O.P. Use Case |
|-------|----------|----------------|
| **🔥 BurnedOut Media** | ADV | Track retreat prospects, webinar registrants, coaching leads |
| **OCPA Group** | CPA | Membership pipeline, event contacts, referral tracking |
| **♾️ WeOwnNet 🌐** | REP | Cooperative membership prospects, real estate professionals |
| **Future (ESQ)** | ESQ | Legal services network, referral partners |
| **Cross-brand** | ALL | Referral tracking between verticals (ADV → CPA → REP → ESQ) |

### Cross-Brand Query Examples

| Query | SQL Pattern |
|-------|------------|
| "All Denver ADV contacts who know a CPA" | JOIN people × people_organizations × tags |
| "Retreat prospects across all verticals" | SELECT tags WHERE tag = 'retreat' |
| "Who referred the most contacts this month?" | COUNT interactions WHERE type = 'referral' |
| "All contacts from ETHDenver" | SELECT WHERE source LIKE '%ETHDenver%' |

---

## 📋 Project Team

| CCC | Role | Focus |
|-----|------|-------|
| **GTM** | **Owner** | Schema design, prompt, seed data, #SmokeTest |
| **RMN** | **Deployment** | DB provisioning, user creation, SQL execution, connection config |

---

## 📋 Risk Matrix

| # | Risk | Prob | Impact | Mitigation |
|---|------|------|--------|------------|
| 1 | SQL Agent generates bad SQL | Medium | Medium | R-011 confirm before execute; no DELETE permission |
| 2 | Data quality (duplicates) | Medium | Low | UNIQUE constraints; manual review |
| 3 | Connection string exposed | Low | High | Infisical secret management; restricted user |
| 4 | Schema changes needed | Medium | Low | `pop_admin` user for DDL; versioned migrations |
| 5 | Adoption (team doesn't use it) | Medium | Medium | Seed with real data; demo in team calls |
| 6 | DO PostgreSQL cost | Low | Low | $15/mo — minimal; shared with other DBs |

---

## 📋 Relationship to Other Projects

| PRJ | Relationship |
|-----|-------------|
| **PRJ-012** | ADV vertical = BurnedOutAdvisor retreat prospects |
| **PRJ-014** | P.O.P. workspace lives on INT-P01 (WeOwn.tools) |
| **PRJ-015** | Could host PostgreSQL on GB10-1 (Option C — future) |
| **PRJ-016** | LiteLLM routes P.O.P. workspace LLM calls |

---

## 📋 Discovered By (BP-047)

| CCC | Contributor | Role | Context |
|-----|-------------|------|---------|
| GTM | [yonks](https://GitHub.com/YonksTEAM) | Co-Founder / Chief Digital Alchemist | P.O.P. workspace concept → PostgreSQL + SQL Agent CRM — W09 |

---

## 📋 Related Documents

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| SharedKernel | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/SharedKernel.md) |
| PRJ-012_BurnedOutAdvisor | v3.1.3.1 | GTM_2026-W08_066 | GTM_2026-W08_087 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-012_BurnedOutAdvisor.md) |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| 3.1.4.1 | 2026-W09 | GTM_2026-W09_141 | GTM_2026-W09_143 | Initial project; P.O.P. Database (PostgreSQL + AnythingLLM SQL Agent); 4 verticals (ADV, CPA, REP, ESQ); 6 tables with full CREATE statements + indexes + triggers; restricted DB user (no DELETE); P.O.P. workspace prompt; 12-step deployment (@RMN infra, @GTM config); 8-point #SmokeTest; seed data plan; cross-brand use cases; referral network model; 6-risk matrix |

---

#FlowsBros #FedArch #POP #CRM #PostgreSQL #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
