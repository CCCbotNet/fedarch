# PRJ-018: P.O.P. Database — People, Organizations, & Places

## 📋 PRJ-018_POP-Database_v3.2.3.1.md
## ♾️ WeOwnNet 🌐

| Field | Value |
|-------|-------|
| Document | PRJ-018_POP-Database.md |
| Version | 3.2.3.1 |
| CCC-ID | GTM_2026-W10_026 |
| Created | 2026-03-01 (W09) |
| Updated | 2026-03-19 (W12) |
| Season | #WeOwnSeason003 🚀 |
| Status | ✅ APPROVED |
| Lifecycle Stage | ✅ APPROVED (#DocLifecycle) |
| Tags | #POP #CRM #PostgreSQL #SQLAgent #PRJ-020 #PRJ-021 #FlowsBros |

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
16. [PRJ-020 Integration](#-prj-020-integration)
17. [PRJ-021 Integration](#-prj-021-integration)
18. [Connection Matrix](#-connection-matrix)
19. [Data Retention Policy](#-data-retention-policy)
20. [Discovered By](#-discovered-by)
21. [Related Documents](#-related-documents)
22. [Version History](#-version-history)

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
| Backend | PostgreSQL (DO Managed — db-postgresql-atl1-weownnet) |
| Interface | AnythingLLM SQL Agent |
| Timeline | **W10-W12** |
| #masterCCC | GTM_2026-W10_026 |
| Approval | GTM_2026-W10_026 |

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
|------|----------|---------------------|-----------------|--------|
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

┌──────────────┐     ┌──────────────────────┐     ┌──────────────┐
│  applicants  │────→│    applications      │←────│application_  │
│              │     │                      │     │   skills     │
│ id           │     │ id                   │     │              │
│ email        │     │ applicant_id (FK)    │     │ application_ │
│ first_name   │     │ form_id              │     │   id (FK)    │
│ last_name    │     │ track                │     │ skills_matrix│
│ location     │     │ availability         │     │ skill_levels │
│ linkedin     │     │ work_authorization   │     └──────────────┘
│ github       │     │ raw_response (JSONB) │
│ portfolio    │     └──────────┬───────────┘
└──────────────┘                │
                                ▼
                    ┌──────────────────────┐     ┌──────────────┐
                    │application_          │←────│application_  │
                    │  evaluations         │     │   ranks      │
                    │                      │     │              │
                    │ id                   │     │ id           │
                    │ application_id (FK)  │     │ application_ │
                    │ eval_type            │     │   id (FK)    │
                    │ score                │     │ final_score  │
                    │ max_score            │     │ rank         │
                    │ evaluator            │     │ recommendation│
                    │ eval_data (JSONB)    │     │ confidence   │
                    └──────────────────────┘     │interview_qs  │
                                                 └──────────────┘
```

### 11 Tables (6 Original + 5 PRJ-020)

| # | Table | Source | Purpose | Rows (Est. Year 1) |
|---|-------|--------|---------|-------------------|
| 1 | `people` | PRJ-018 (original) | Individual contacts | 500-2,000 |
| 2 | `organizations` | PRJ-018 (original) | Firms, agencies, practices | 200-500 |
| 3 | `places` | PRJ-018 (original) | Cities, venues, markets | 50-200 |
| 4 | `people_organizations` | PRJ-018 (original) | Person ↔ Org junction | 500-2,000 |
| 5 | `interactions` | PRJ-018 (original) | Meetings, calls, events | 1,000-5,000 |
| 6 | `tags` | PRJ-018 (original) | Flexible tagging | 1,000-5,000 |
| 7 | **`applicants`** | **PRJ-020 (new)** | **Identity dedup by email** | **50-200** |
| 8 | **`applications`** | **PRJ-020 (new)** | **Form submissions** | **50-300** |
| 9 | **`application_skills`** | **PRJ-020 (new)** | **Skills matrix JSON** | **50-300** |
| 10 | **`application_evaluations`** | **PRJ-020 (new)** | **Multi-eval per app** | **100-1,200** |
| 11 | **`application_ranks`** | **PRJ-020 (new)** | **Leaderboard** | **50-300** |

### Observation: `applicants` vs `people`

| Table | Purpose | Overlap? | Phase 2 Merge? |
|-------|---------|----------|----------------|
| `people` | Contacts (ADV, CPA, REP, ESQ verticals) | Professional contacts | ✅ Add `applicant_id` FK |
| `applicants` | Intern candidates | Intern candidates | ✅ Graduated interns → `people` |

> **Phase 1:** Separate tables (correct for now). **Phase 2:** Consider merging — applicant who gets hired becomes `people` record with `applicant_id` FK.

---

## 📋 SQL CREATE Statements

```sql
-- P.O.P. Database Schema v3.2.3.1
-- PRJ-018 — ♾️ WeOwnNet 🌐
-- db-postgresql-atl1-weownnet (ATL1, PG v18)

-- ============================================
-- ORIGINAL 6 TABLES (PRJ-018)
-- ============================================

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

-- ============================================
-- PRJ-020 INTERN SCHEMA (5 NEW TABLES)
-- ============================================

-- 7. APPLICANTS (identity dedup by email)
CREATE TABLE applicants (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    location VARCHAR(255),
    linkedin VARCHAR(255),
    github VARCHAR(255),
    portfolio VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 8. APPLICATIONS (one per form submission)
CREATE TABLE applications (
    id SERIAL PRIMARY KEY,
    applicant_id INTEGER REFERENCES applicants(id) ON DELETE CASCADE,
    form_id INTEGER NOT NULL,
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    track VARCHAR(3) CHECK (track IN ('ADV', 'CPA', 'REP', 'ESQ')),
    availability VARCHAR(255),
    work_authorization BOOLEAN,
    raw_response JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 9. APPLICATION_SKILLS (skills matrix per application)
CREATE TABLE application_skills (
    id SERIAL PRIMARY KEY,
    application_id INTEGER REFERENCES applications(id) ON DELETE CASCADE,
    skills_matrix JSONB NOT NULL,
    skill_levels JSONB NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 10. APPLICATION_EVALUATIONS (multiple per application)
CREATE TABLE application_evaluations (
    id SERIAL PRIMARY KEY,
    application_id INTEGER REFERENCES applications(id) ON DELETE CASCADE,
    eval_type VARCHAR(20) CHECK (eval_type IN ('structured', 'llm', 'hybrid', 'meta')),
    score NUMERIC(5,2),
    max_score NUMERIC(5,2),
    evaluator VARCHAR(50),
    eval_data JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 11. APPLICATION_RANKS (current leaderboard)
CREATE TABLE application_ranks (
    id SERIAL PRIMARY KEY,
    application_id INTEGER REFERENCES applications(id) ON DELETE CASCADE,
    final_score NUMERIC(5,2),
    rank INTEGER,
    recommendation VARCHAR(20) CHECK (recommendation IN ('ADVANCE', 'MAYBE', 'PASS')),
    confidence_level VARCHAR(20),
    interview_questions JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================
-- INDEXES (ALL 11 TABLES)
-- ============================================

-- Original 6 tables
CREATE INDEX idx_people_vertical ON people(vertical);
CREATE INDEX idx_people_status ON people(status);
CREATE INDEX idx_people_ccc ON people(ccc);
CREATE INDEX idx_orgs_vertical ON organizations(vertical);
CREATE INDEX idx_interactions_person ON interactions(person_id);
CREATE INDEX idx_interactions_date ON interactions(date);
CREATE INDEX idx_tags_entity ON tags(entity_type, entity_id);
CREATE INDEX idx_tags_tag ON tags(tag);

-- PRJ-020 tables
CREATE INDEX idx_applicants_email ON applicants(email);
CREATE INDEX idx_applications_applicant ON applications(applicant_id);
CREATE INDEX idx_applications_track ON applications(track);
CREATE INDEX idx_evals_application ON application_evaluations(application_id);
CREATE INDEX idx_evals_type ON application_evaluations(eval_type);
CREATE INDEX idx_ranks_application ON application_ranks(application_id);
CREATE INDEX idx_ranks_recommendation ON application_ranks(recommendation);

-- ============================================
-- UPDATED_AT TRIGGER
-- ============================================

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

CREATE TRIGGER applicants_updated
    BEFORE UPDATE ON applicants
    FOR EACH ROW
    EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER application_ranks_updated
    BEFORE UPDATE ON application_ranks
    FOR EACH ROW
    EXECUTE FUNCTION update_timestamp();
```

---

## 📋 Security

### Database Users

#### pop_user (Original — P.O.P. SQL Agent)

```sql
-- Create restricted user for AnythingLLM SQL Agent
CREATE USER pop_user WITH PASSWORD '****';

-- Grant connection
GRANT CONNECT ON DATABASE defaultdb TO pop_user;
GRANT USAGE ON SCHEMA public TO pop_user;

-- Grant DML (NO DDL)
GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO pop_user;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO pop_user;

-- Explicitly deny destructive operations
-- (PostgreSQL denies by default — but documenting intent)
-- NO DELETE, DROP, ALTER, TRUNCATE, CREATE
```

#### p012_app (PRJ-020 — Intern Eval Pipeline)

```sql
-- Create restricted user for PRJ-020 n8n pipeline
CREATE USER p012_app WITH PASSWORD '****';

-- Grant connection
GRANT CONNECT ON DATABASE defaultdb TO p012_app;
GRANT USAGE ON SCHEMA public TO p012_app;

-- Grant table access (PRJ-020 interns schema only)
GRANT SELECT, INSERT ON applicants TO p012_app;
GRANT SELECT, INSERT ON applications TO p012_app;
GRANT SELECT, INSERT ON application_skills TO p012_app;
GRANT SELECT, INSERT ON application_evaluations TO p012_app;
GRANT SELECT, INSERT ON application_ranks TO p012_app;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO p012_app;

-- NO UPDATE, NO DELETE — intern data is immutable once registered
```

### Permission Matrix

| Operation | `pop_user` | `p012_app` | `pop_admin` (future) |
|-----------|-----------|-----------|---------------------|
| SELECT (P.O.P. tables) | ✅ | ❌ | ✅ |
| SELECT (PRJ-020 tables) | ❌ | ✅ | ✅ |
| INSERT (P.O.P. tables) | ✅ | ❌ | ✅ |
| INSERT (PRJ-020 tables) | ❌ | ✅ | ✅ |
| UPDATE | ✅ | ❌ | ✅ |
| DELETE | ❌ | ❌ | ✅ |
| CREATE TABLE | ❌ | ❌ | ✅ |
| DROP | ❌ | ❌ | ❌ (never) |
| ALTER | ❌ | ❌ | ✅ |

> **No DELETE for SQL Agent or n8n pipeline.** Contacts are never deleted — only set to `status = 'INACTIVE'`. Intern data is immutable once registered. Prevents accidental data loss.

### Connection Strings

| User | Connection String |
|------|------------------|
| `pop_user` | `postgresql://pop_user:****@<host>:25060/defaultdb?sslmode=require` |
| `p012_app` | `postgresql://p012_app:****@<host>:25060/defaultdb?sslmode=require` |

---

## 📋 AnythingLLM SQL Agent Configuration

### Setup Steps

| # | Step | Detail |
|---|------|--------|
| 1 | Navigate | INT-P01 → P.O.P. 🌟 workspace → Settings |
| 2 | Agent Configuration | Enable SQL Agent tool |
| 3 | Database Connection | PostgreSQL connection string (pop_user) |
| 4 | Test Connection | Verify connectivity |
| 5 | Set Workspace Prompt | Schema reference + behavioral rules |

### SQL Agent Settings

| Setting | Value |
|---------|-------|
| Database Type | PostgreSQL |
| Host | `<DO Managed DB host>` |
| Port | 25060 (SSL) |
| Database | defaultdb |
| User | pop_user |
| SSL | Required |
| Tables Exposed | ALL 11 tables |

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

### Tables (11 Total)
**Original 6 (PRJ-018):**
- `people` — Individual contacts (vertical: ADV, CPA, REP, ESQ)
- `organizations` — Firms, agencies, practices
- `places` — Cities, venues, markets, regions
- `people_organizations` — Person ↔ Org relationships
- `interactions` — Meetings, calls, emails, events
- `tags` — Flexible tagging (person, org, place)

**PRJ-020 (5 new):**
- `applicants` — Intern candidate identity (dedup by email)
- `applications` — Form submissions (one per applicant)
- `application_skills` — Skills matrix JSON per application
- `application_evaluations` — Multiple evaluations per app
- `application_ranks` — Current leaderboard

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

### Recommendation Values (PRJ-020)
- ADVANCE — top candidates for interview
- MAYBE — secondary pool
- PASS — not selected

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
| "Show all ADVANCE intern candidates" | SELECT application_ranks WHERE recommendation = 'ADVANCE' |
```

---

## 📋 Deployment Checklist

| # | Step | Owner | Status |
|---|------|-------|--------|
| 1 | Create `defaultdb` database on DO PostgreSQL (already exists) | @RMN | ✅ |
| 2 | Configure Trusted Sources (add n8n, INT-OG8, INT-OG1, INT-P02 IPs) | @RMN | ⬜ |
| 3 | Download SSL CA certificate | @RMN | ⬜ |
| 4 | CREATE EXTENSION citext | @RMN | ⬜ |
| 5 | Create `pop_user` with restricted permissions | @RMN | ⬜ |
| 6 | Create `p012_app` with PRJ-020 permissions | @RMN | ⬜ |
| 7 | Run CREATE TABLE statements (11 tables) | @RMN | ⬜ |
| 8 | Run CREATE INDEX statements | @RMN | ⬜ |
| 9 | Run CREATE TRIGGER (updated_at) | @RMN | ⬜ |
| 10 | Store creds in Infisical | @RMN | ⬜ |
| 11 | Verify connection from AnythingLLM (pop_user) | @GTM | ⬜ |
| 12 | Verify connection from n8n (p012_app) | @RMN | ⬜ |
| 13 | Enable SQL Agent in P.O.P. 🌟 workspace | @GTM | ⬜ |
| 14 | Configure connection string | @GTM | ⬜ |
| 15 | Set P.O.P. workspace prompt | @GTM | ⬜ |
| 16 | Insert seed data (P.O.P. + PRJ-020) | @GTM + @RMN | ⬜ |
| 17 | #SmokeTest (10-point) | @GTM + @RMN | ⬜ |
| 18 | Enable PgBouncer (if 3+ consumers) | @RMN | ⬜ |

> **@RMN = steps 1-12, 18 (infrastructure). @GTM = steps 13-17 (configuration + data).**

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

### PRJ-020 Intern Data (W10 Complete)

| Metric | Value |
|--------|-------|
| Applications Processed | 48 |
| Auto-DQ'd | 18 (37.5%) |
| ADVANCE | 6 |
| MAYBE | 10 |
| PASS (scored) | 14 |
| Storage Estimate | <10 MB |

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

-- PRJ-020: Example applicant
INSERT INTO applicants (email, first_name, last_name, location, linkedin, github)
VALUES ('candidate@example.com', 'Jane', 'Doe', 'Denver, CO', 'linkedin.com/in/janedoe', 'github.com/janedoe');

-- PRJ-020: Example application
INSERT INTO applications (applicant_id, form_id, track, availability, work_authorization, raw_response)
VALUES (1, 8, 'ADV', 'Available now', TRUE, '{"skills": {...}}');

-- PRJ-020: Example evaluation
INSERT INTO application_evaluations (application_id, eval_type, score, max_score, evaluator, eval_data)
VALUES (1, 'hybrid', 92.5, 100, 'n8n+LLM', '{"strengths": [...], "red_flags": [...]}');

-- PRJ-020: Example rank
INSERT INTO application_ranks (application_id, final_score, rank, recommendation, confidence_level, interview_questions)
VALUES (1, 92.5, 1, 'ADVANCE', 'High', '["Tell me about...", "How would you..."]');
```

---

## 📋 Verification (#SmokeTest)

### P.O.P. #SmokeTest (10-Point)

| # | Test | Method | Expected | Status |
|---|------|--------|----------|--------|
| 1 | DB connection (pop_user) | SQL Agent → test connection | ✅ Connected | ⬜ |
| 2 | DB connection (p012_app) | n8n → test connection | ✅ Connected | ⬜ |
| 3 | SELECT (P.O.P.) | "Show all people" | Returns seed data | ⬜ |
| 4 | SELECT (PRJ-020) | "Show all ADVANCE candidates" | Returns 6 candidates | ⬜ |
| 5 | INSERT (person) | "Add Test User, CPA in Miami" | Confirms → inserts | ⬜ |
| 6 | INSERT (applicant) | n8n pipeline test | Inserts to applicants | ⬜ |
| 7 | JOIN | "Show all CPAs and their firms" | Returns joined data | ⬜ |
| 8 | TAG | "Tag Test User as retreat prospect" | Inserts tag | ⬜ |
| 9 | CONFIRM behavior | Agent shows SQL before executing | ✅ R-011 | ⬜ |
| 10 | NO DELETE | "Delete Test User" | Agent refuses — suggests INACTIVE | ⬜ |

---

## 📋 Cross-Brand Use Cases

| Brand | Vertical | P.O.P. Use Case |
|-------|----------|----------------|
| **🔥 BurnedOut Media** | ADV | Track retreat prospects, webinar registrants, coaching leads |
| **OCPA Group** | CPA | Membership pipeline, event contacts, referral tracking |
| **♾️ WeOwnNet 🌐** | REP | Cooperative membership prospects, real estate professionals |
| **Future (ESQ)** | ESQ | Legal services network, referral partners |
| **Cross-brand** | ALL | Referral tracking between verticals (ADV → CPA → REP → ESQ) |
| **PRJ-020** | Interns | Candidate pipeline, eval results, interview scheduling |

### Cross-Brand Query Examples

| Query | SQL Pattern |
|-------|------------|
| "All Denver ADV contacts who know a CPA" | JOIN people × people_organizations × tags |
| "Retreat prospects across all verticals" | SELECT tags WHERE tag = 'retreat' |
| "Who referred the most contacts this month?" | COUNT interactions WHERE type = 'referral' |
| "All contacts from ETHDenver" | SELECT WHERE source LIKE '%ETHDenver%' |
| "Top 5 intern candidates by score" | SELECT * FROM application_ranks ORDER BY final_score DESC LIMIT 5 |
| "All ADVANCE candidates available now" | SELECT a.* FROM applicants a JOIN applications ap ON a.id = ap.applicant_id JOIN application_ranks r ON ap.id = r.application_id WHERE r.recommendation = 'ADVANCE' AND ap.availability LIKE '%now%' |

---

## 📋 Project Team

| CCC | Role | Focus |
|-----|------|-------|
| **GTM** | **Owner** | Schema design, prompt, seed data, #SmokeTest |
| **RMN** | **Deployment** | DB provisioning, user creation, SQL execution, connection config, PRJ-020 integration |
| **LDC** | **PRJ-023 Lead** | Context persistence pipeline (future — chat history → POP DB) |

---

## 📋 Risk Matrix

| # | Risk | Prob | Impact | Mitigation |
|---|------|------|--------|------------|
| 1 | SQL Agent generates bad SQL | Medium | Medium | R-011 confirm before execute; no DELETE permission |
| 2 | Data quality (duplicates) | Medium | Low | UNIQUE constraints; manual review |
| 3 | Connection string exposed | Low | High | Infisical secret management; restricted user |
| 4 | Schema changes needed | Medium | Low | `pop_admin` user for DDL; versioned migrations |
| 5 | Adoption (team doesn't use it) | Medium | Medium | Seed with real data; demo in team calls |
| 6 | DO PostgreSQL cost | Low | Low | $18.23/mo — minimal; shared with other DBs |
| 7 | **PRJ-020 integration complexity** | **Medium** | **Medium** | **Clear schema separation, p012_app user isolation** |
| 8 | **Trusted Sources not configured** | **High** | **High** | **P0 task — blocks n8n, INT-OG8, INT-OG1, INT-P02 connections** |
| 9 | **PgBouncer not enabled (3+ consumers)** | **Medium** | **Medium** | **Enable proactively at 3 consumers (INT-P01 + n8n + INT-OG8)** |

---

## 📋 Relationship to Other Projects

| PRJ | Title | Relationship |
|-----|-------|-------------|
| **PRJ-012** | BurnedOutAdvisor | ADV vertical = retreat prospects |
| **PRJ-014** | SEPARATE | P.O.P. workspace lives on INT-P01 (WeOwn.tools) |
| **PRJ-015** | HybridArchitecture | Could host PostgreSQL on GB10-1 (Option C — future) |
| **PRJ-016** | LiteLLM AI Gateway | Routes P.O.P. workspace LLM calls |
| **PRJ-020** | Interns Co-op Pipeline | **5 tables in POP DB (applicants, applications, skills, evaluations, ranks)** |
| **PRJ-021** | DigitalOcean Infrastructure | **PostgreSQL cluster owner — Trusted Sources, PgBouncer, connection pool** |
| **PRJ-023** | Context Persistence Pipeline | Future — chat history → POP DB via n8n |

---

## 📋 PRJ-020 Integration

### Data Flow — PRJ-020 Eval Pipeline → POP DB

#### Current State (W10 Complete)

```
WordPress Fluent Forms API (48 apps)
    → n8n Pass 1: Hard filters + structured scoring
    → AnythingLLM Pass 2: Full LLM evaluation (6 categories, 100 pts)
    → AnythingLLM Pass 3: Meta-review + final recommendation
    → JSON file output (CURRENT — temporary)
```

#### Target State (W12 — After PRJ-018 v3.2.3.1)

```
WordPress Fluent Forms API (48 apps)
    → n8n Pass 1: Hard filters + structured scoring
    → AnythingLLM Pass 2: Full LLM evaluation
    → AnythingLLM Pass 3: Meta-review + final recommendation
    → PostgreSQL POP DB (5 tables — PRJ-018 schema)
        ├── applicants
        ├── applications
        ├── application_skills
        ├── application_evaluations
        └── application_ranks
```

### n8n Workflow Updates Required

| Node | Current | After Update |
|------|---------|--------------|
| Output | JSON file | PostgreSQL INSERT (5 tables) |
| Connection | Local file system | DO Managed PG (Public + SSL) |
| Auth | N/A | p012_app credentials (from Infisical when fixed) |
| Error Handling | File write errors | PG connection retry + error logging |

### Storage Estimate

| Data | Size |
|------|------|
| 200 applications × 4 evaluations × ~5KB avg | ~4 MB |
| Raw JSONB payloads | ~2 MB |
| **Total PRJ-020 data** | **<10 MB** — negligible on 15 GiB cluster |

---

## 📋 PRJ-021 Integration

### PostgreSQL Cluster Specification

| Field | Value |
|-------|-------|
| Cluster Name | db-postgresql-atl1-weownnet |
| Engine | PostgreSQL v18 |
| Plan | Basic Premium AMD NVMe — $15/mo |
| vCPU | 1 |
| RAM | 1 GB |
| Connections | 22 (→ 100+ with PgBouncer pool) |
| Storage | 15 GiB NVMe (autoscale → 75 GiB @ 80%) |
| Port | 25060 (SSL), 25061 (pool — when created) |
| Cost | $18.23/mo ($15 compute + $3.23 storage) |
| Datacenter | ATL1 (Atlanta) |
| DO Team | We Own Labs |
| DO Project | ♾️ WeOwnNet 🌐 (moved from ♾️ WeOwn.Dev 💻 W10-W11) |

### Trusted Sources Configuration (P0 Task)

| Resource | IP/Type | Status |
|----------|---------|--------|
| n8n pod (DOKS Academy) | Dynamic (DOKS egress) | ⬜ TODO |
| INT-OG8 (DOKS Academy) | Dynamic (DOKS egress) | ⬜ TODO |
| INT-OG1 (DOKS Academy) | Dynamic (DOKS egress) | ⬜ TODO |
| INT-P02 (Droplet Academy) | Static Droplet IP | ⬜ TODO |
| jAIMSnet DOKS (Labs) | Same VPC — auto-trusted | ✅ Auto |
| INT-P01 (DOKS Labs) | Same VPC — auto-trusted | ✅ Auto |

### Connection Pool (PgBouncer) — When Needed

| Field | Value |
|-------|-------|
| Trigger | 3+ concurrent consumers |
| Mode | Transaction (recommended) |
| Pool Size | 15 |
| Port | 25061 |
| Benefit | 22 connections → 100+ effective |
| Current Consumers | ~2 (INT-P01 + n8n) |
| After PRJ-020 | ~3-4 (+ INT-OG8, INT-P02) |

> **PgBouncer likely needed W12.** Enable proactively.

### Required PG Setup Steps (PRJ-021 P0 Tasks)

| # | Task | SQL/Action | Est. Time |
|---|------|------------|:---------:|
| 1 | Configure Trusted Sources | DO Console → PostgreSQL → Trusted Sources | 0.5h |
| 2 | Download SSL CA certificate | DO PG Console → Download CA | 0.25h |
| 3 | CREATE EXTENSION citext | `CREATE EXTENSION IF NOT EXISTS citext;` | 0.1h |
| 4 | CREATE USER pop_user | `CREATE USER pop_user WITH PASSWORD 'xxx';` | 0.25h |
| 5 | CREATE USER p012_app | `CREATE USER p012_app WITH PASSWORD 'xxx';` | 0.25h |
| 6 | GRANT permissions | `GRANT CONNECT ON DATABASE defaultdb TO pop_user/p012_app;` + schema grants | 0.25h |
| 7 | Run PRJ-018 + PRJ-020 schema | Execute 11 CREATE TABLE statements | 0.25h |
| 8 | Store creds in Infisical | Manual until PRJ-024 fixed | 0.25h |
| 9 | Verify n8n connection | Test connection as p012_app | 0.25h |
| **TOTAL** | | | **2.35h** |

---

## 📋 Connection Matrix

### Connection Scenarios (GUIDE-010 Compliant)

| From Instance | Team | To PG Cluster | Method | Cost | Latency |
|--------------|------|---------------|--------|------|---------|
| **INT-P01** | We Own Labs | Labs→Labs | VPC Private IP | FREE | <1ms |
| **jAIMSnet DOKS** | We Own Labs | Labs→Labs | VPC Private IP | FREE | <1ms |
| **INT-OG8** | We Own Academy | Academy→Labs | Public + Trusted Sources + SSL | $0.01/GiB | 2-5ms |
| **INT-OG1** | We Own Academy | Academy→Labs | Public + Trusted Sources + SSL | $0.01/GiB | 2-5ms |
| **INT-P02** | We Own Academy | Academy→Labs | Public + Trusted Sources + SSL | $0.01/GiB | 2-5ms |
| **n8n** | We Own Academy | Academy→Labs | Public + Trusted Sources + SSL | $0.01/GiB | 2-5ms |

### Connection Methods Explained (GUIDE-010)

| Method | When Used | Configuration |
|--------|-----------|---------------|
| **VPC Private IP** | Same DO Team + Same DC | No Trusted Sources needed — auto-trusted |
| **Public + Trusted Sources + SSL** | Different DO Team + Same DC | Add egress IPs to Trusted Sources, use SSL port 25060 |

### Why Inter-Team VPC Is Not Supported (L-123)

| Fact | Detail |
|------|--------|
| **DO Limitation** | DigitalOcean does not support VPC peering across teams |
| **Impact** | Academy→Labs must use Public + Trusted Sources + SSL |
| **Workaround** | Trusted Sources configuration (P0 task) |
| **Cost** | $0.01/GiB egress (negligible for DB traffic) |
| **Latency** | 2-5ms within same DC (ATL1) |

---

## 📋 Data Retention Policy

### P.O.P. Data (PRJ-018)

| Data Type | Retention | Archival Strategy |
|-----------|-----------|-------------------|
| Active contacts | Indefinite | Keep while relationship active |
| Inactive contacts | 7 years | Set `status = 'INACTIVE'`, archive annually |
| Interactions | Indefinite | Append-only, never deleted |
| Tags | Indefinite | Linked to entities |

### PRJ-020 Intern Data

| Data Type | Retention | Archival Strategy |
|-----------|-----------|-------------------|
| Applicants | 3 years | Keep for future hiring cycles |
| Applications | 3 years | Linked to applicants |
| Evaluations | 3 years | Audit trail, improve rubric |
| Ranks | 3 years | Historical leaderboard |

### Archival Process

| Step | Action | Frequency |
|------|--------|----------|
| 1 | Set `status = 'INACTIVE'` for old contacts | Annual |
| 2 | Export to CSV/JSON for backup | Annual |
| 3 | Move to cold storage (S3/Glacier) | Annual |
| 4 | Delete from active DB after 7 years | As needed |

> **No hard deletes in active DB.** All data archived, never permanently deleted (compliance, audit trail).

---

## 📋 Discovered By (BP-047)

| CCC | Contributor | Role | Context |
|-----|-------------|------|---------|
| GTM | Jason Younker | Project Owner | P.O.P. workspace concept → PostgreSQL + SQL Agent CRM — W09 |
| RMN | Roman Di Domizio | AI Platform Engineer | PRJ-020 intern eval pipeline, PRJ-021 PG ops, integration request — W11 |
| THY | Tyler Younker | CFO | Requested POP DB storage for intern data (not separate DB) — W10 |

---

## 📋 Related Documents

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| SharedKernel | v3.2.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/SharedKernel.md) |
| PRJ-012_BurnedOutAdvisor | v3.2.3.1 | GTM_2026-W08_066 | GTM_2026-W08_087 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-012_BurnedOutAdvisor.md) |
| PRJ-020_Interns-Co-op | v3.2.3.1 | GTM_2026-W10_026 | GTM_2026-W10_026 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-020_Interns-Co-op.md) |
| PRJ-021_DO-Infrastructure | v3.2.3.1 | GTM_2026-W10_026 | GTM_2026-W10_026 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-021_DO-Infrastructure.md) |
| PRJ-023_Context-Persistence | v3.2.3.1 | GTM_2026-W10_026 | GTM_2026-W10_026 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-023_Context-Persistence.md) |
| GUIDE-010_PostgreSQL-Setup | v3.2.1.1 | GTM_2026-W10_026 | GTM_2026-W10_073 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_GUIDES_/GUIDE-010_PostgreSQL-Setup.md) |
| GUIDE-011_Governance-Oversight | v3.2.1.1 | GTM_2026-W10_066 | GTM_2026-W10_073 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_GUIDES_/GUIDE-011_Governance-Oversight-VSA-Process.md) |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| 3.1.4.1 | 2026-W09 | GTM_2026-W09_141 | GTM_2026-W09_143 | Initial project; P.O.P. Database (PostgreSQL + AnythingLLM SQL Agent); 4 verticals (ADV, CPA, REP, ESQ); 6 tables with full CREATE statements + indexes + triggers; restricted DB user (no DELETE); P.O.P. workspace prompt; 12-step deployment (@RMN infra, @GTM config); 8-point #SmokeTest; seed data plan; cross-brand use cases; referral network model; 6-risk matrix |
| **3.2.3.1** | **2026-W12** | **GTM_2026-W10_026** | **GTM_2026-W10_026** | **Added PRJ-020 intern schema (5 tables: applicants, applications, application_skills, application_evaluations, application_ranks); Added PRJ-021 PostgreSQL integration details (cluster specs, Trusted Sources, PgBouncer, connection pool); Added connection matrix (Academy→Labs vs Labs→Labs per GUIDE-010); Added data retention policy; Updated deployment checklist (18 steps, 2.35h PG setup); Updated #SmokeTest (10-point); Updated project team (@RMN, @LDC); Updated risk matrix (PRJ-020/021 integration risks); Updated related documents (PRJ-020, PRJ-021, PRJ-023, GUIDE-010); DO project migration (WeOwn.Dev → WeOwnNet)** |

---

#FlowsBros #FedArch #POP #CRM #PostgreSQL #PRJ-020 #PRJ-021 #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
