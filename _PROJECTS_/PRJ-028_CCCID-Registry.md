# PRJ-028: cccid.info — Centralized CCC-ID Registry

## 📋 PRJ-028_CCCID-Registry_v3.2.1.1.md
## ♾️ WeOwnNet 🌐

| Field | Value |
|-------|-------|
| Document | PRJ-028_CCCID-Registry.md |
| Version | 3.2.1.1 |
| CCC-ID | GTM_2026-W10_057 |
| Created | 2026-03-03 (W10) |
| Season | #WeOwnSeason003 🚀 |
| Status | ✅ APPROVED |
| Lifecycle Stage | ✅ APPROVED (#DocLifecycle) |
| Tags | #CCCID #Registry #API #R212 #Governance #FOSS #FlowsBros |

---

## 📖 Table of Contents

1. [Project Identity](#-project-identity)
2. [Why cccid.info](#-why-cccidinfo)
3. [R-212 Tier Evolution](#-r-212-tier-evolution)
4. [Architecture](#-architecture)
5. [API Specification](#-api-specification)
6. [Database Schema](#-database-schema)
7. [Phased Rollout](#-phased-rollout)
8. [Public Dashboard](#-public-dashboard)
9. [Deployment Checklist](#-deployment-checklist)
10. [Docker Compose](#-docker-compose)
11. [Verification (#SmokeTest)](#-verification-smoketest)
12. [Security](#-security)
13. [CCC Domain Portfolio](#-ccc-domain-portfolio)
14. [Project Team](#-project-team)
15. [Risk Matrix](#-risk-matrix)
16. [Relationship to Other Projects](#-relationship-to-other-projects)
17. [Discovered By](#-discovered-by)
18. [Related Documents](#-related-documents)
19. [Version History](#-version-history)

---

## 📋 Project Identity

| Field | Value |
|-------|-------|
| Project ID | **PRJ-028** |
| Title | **cccid.info — Centralized CCC-ID Registry** |
| Type | Governance Infrastructure |
| Priority | 🟠 P1 |
| Owner | @GTM (governance/schema) + @RMN (API build) |
| Domain | **[cccid.info](https://cccid.info)** |
| Stack | FastAPI (Python) + PostgreSQL (ATL1) |
| Solves | **R-212 Tier 3** — centralized CCC-ID counter |
| Timeline | **Phase 1: W11-W12** / Phase 2: W13+ / Phase 3: W15+ |
| Depends on | PRJ-021 (PostgreSQL ATL1 operational) |
| Feeds into | ALL instances — eliminates manual CCC-ID deconfliction |
| #masterCCC | GTM_2026-W10_057 |

---

## 📋 Why cccid.info

### The Problem

9 contributors generate CCC-IDs across 5+ instances. Each instance maintains its own local counter. When a contributor switches instances mid-week, the counters diverge.

| Scenario | Risk |
|----------|------|
| @GTM generates _057 on INT-OG1 | INT-OG1 counter = 57 |
| @GTM switches to INT-P01 | INT-P01 counter = ??? (doesn't know about 57) |
| @GTM generates _057 on INT-P01 | **DUPLICATE — #BadAgent #13** |

### The Impact

| Metric | Value |
|--------|-------|
| Duplication incidents (S003) | 1 (#BadAgent #13 — W06) |
| Contributors at risk | 9 |
| Active instances | 5+ (INT-P01, INT-OG1, INT-OG8, INT-S003, INT-P02) |
| CCC-IDs per week (ecosystem) | ~150-250 |
| Manual deconfliction overhead | ~30 seconds per session start × ~20 sessions/week = ~10 min/week |

### The Solution

**One API. One database. One source of truth.**

```
BEFORE (Tier 1 — Manual):
  Human: "Highest = GTM_2026-W10_057"
  Agent: "✅ Continuing from _058"
  ↑ Manual. Error-prone. Already failed once.

AFTER (Tier 3 — cccid.info):
  Agent: GET cccid.info/api/v1/next/GTM/2026/10
  API:   { "next_seq": 58 }
  Agent: Generates GTM_2026-W10_058
  Agent: POST cccid.info/api/v1/register
  API:   { "registered": true }
  ↑ Automatic. Zero human intervention. Zero duplication.
```

---

## 📋 R-212 Tier Evolution

| Tier | Method | Status | PRJ |
|------|--------|--------|-----|
| **Tier 1** | Human states highest CCC-ID | ✅ Active (becomes fallback) | — |
| **Tier 2** | #MetaAgent tracks high-water mark | ❌ **SKIP** | — |
| **Tier 3** | **cccid.info centralized API** | 🆕 **PRJ-028** | **This project** |

### Why Skip Tier 2

| Tier 2 (#MetaAgent) | Tier 3 (cccid.info) |
|---------------------|---------------------|
| Depends on #MetaAgent being online | Independent API — always available |
| Single point of failure (INT-P01) | Separate service — isolated |
| Session-dependent (context window) | Database-persistent — permanent |
| Cannot serve multiple agents simultaneously | REST API — concurrent access |
| Adds complexity to #MetaAgent | Clean separation of concerns |

> **Going directly Tier 1 → Tier 3 is simpler, more reliable, and eliminates an unnecessary intermediate step.**

---

## 📋 Architecture

### System Architecture

```
┌─────────────────────────────────────────────────────────┐
│  cccid.info (DO Droplet or GB10-1)                       │
│                                                          │
│  ┌──────────────────────────────────────────────────┐   │
│  │  FastAPI Application (Python)                     │   │
│  │  Port: 8000                                       │   │
│  │                                                    │   │
│  │  ┌────────────┐  ┌─────────────┐  ┌───────────┐  │   │
│  │  │ /api/v1/   │  │ /stats      │  │ /docs     │  │   │
│  │  │ register   │  │ (dashboard) │  │ (Swagger) │  │   │
│  │  │ next       │  │             │  │           │  │   │
│  │  │ latest     │  │             │  │           │  │   │
│  │  │ validate   │  │             │  │           │  │   │
│  │  └────────────┘  └─────────────┘  └───────────┘  │   │
│  └──────────────────┬───────────────────────────────┘   │
│                     │ SQL                                │
│  ┌──────────────────┴───────────────────────────────┐   │
│  │  PostgreSQL (ATL1 — shared with PRJ-018)          │   │
│  │  Database: cccid_db                               │   │
│  │  Table: ccc_ids                                   │   │
│  └──────────────────────────────────────────────────┘   │
│                                                          │
│  ┌──────────────────────────────────────────────────┐   │
│  │  Caddy (reverse proxy + auto-SSL)                 │   │
│  │  cccid.info:443 → FastAPI:8000                    │   │
│  └──────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘

         ▲              ▲              ▲
         │              │              │
┌────────┴──┐  ┌───────┴────┐  ┌─────┴──────┐
│  INT-OG1  │  │  INT-P01   │  │  INT-S003  │
│  Agent    │  │  Agent     │  │  Agent     │
│  POST/GET │  │  POST/GET  │  │  POST/GET  │
└───────────┘  └────────────┘  └────────────┘
```

### Data Flow

```
1. Agent on ANY instance generates CCC-ID
2. Agent queries: GET cccid.info/api/v1/next/{CCC}/{YYYY}/{WW}
3. API returns next available sequence from PostgreSQL
4. Agent generates CCC-ID with that sequence
5. Agent registers: POST cccid.info/api/v1/register
6. PostgreSQL stores: ccc, year, week, seq, instance, timestamp
7. Next query from ANY instance gets updated sequence
8. Zero duplication. Zero manual deconfliction.
```

---

## 📋 API Specification

### Base URL

```
https://cccid.info/api/v1
```

### Authentication

| Endpoint Type | Auth | Method |
|--------------|------|--------|
| Write (POST) | API key | `X-API-Key` header |
| Read (GET — private) | API key | `X-API-Key` header |
| Read (GET — public) | None | Open access |

### Endpoints

#### POST /api/v1/register

Register a new CCC-ID.

**Request:**
```json
{
  "ccc": "GTM",
  "year": 2026,
  "week": 10,
  "seq": 58,
  "instance": "INT-OG1",
  "workspace": "CCC"
}
```

**Response (201):**
```json
{
  "registered": true,
  "ccc_id": "GTM_2026-W10_058",
  "next_seq": 59,
  "timestamp": "2026-03-03T08:06:00Z"
}
```

**Response (409 — Duplicate):**
```json
{
  "registered": false,
  "error": "CCC-ID GTM_2026-W10_058 already exists",
  "existing_instance": "INT-P01",
  "next_seq": 59
}
```

#### GET /api/v1/next/{CCC}/{YYYY}/{WW}

Get next available sequence for a contributor in a specific week.

**Response (200):**
```json
{
  "ccc": "GTM",
  "year": 2026,
  "week": 10,
  "highest_seq": 57,
  "next_seq": 58,
  "total_this_week": 54
}
```

#### GET /api/v1/latest/{CCC}

Get the highest CCC-ID for a contributor (any week).

**Response (200):**
```json
{
  "ccc": "GTM",
  "latest": "GTM_2026-W10_057",
  "year": 2026,
  "week": 10,
  "seq": 57,
  "instance": "INT-OG1",
  "timestamp": "2026-03-03T07:54:00Z"
}
```

#### GET /api/v1/latest/{CCC}/{YYYY}/{WW}

Get the highest CCC-ID for a contributor in a specific week.

**Response (200):**
```json
{
  "ccc": "GTM",
  "year": 2026,
  "week": 10,
  "highest_seq": 57,
  "next_seq": 58,
  "total_this_week": 54
}
```

#### GET /api/v1/stats (Public)

Global CCC-ID statistics.

**Response (200):**
```json
{
  "total_ccc_ids": 2847,
  "contributors": 9,
  "active_instances": 5,
  "current_week": {
    "year": 2026,
    "week": 10,
    "total": 148
  },
  "top_contributors_this_week": [
    { "ccc": "GTM", "count": 57 },
    { "ccc": "THY", "count": 46 },
    { "ccc": "RMN", "count": 25 }
  ]
}
```

#### GET /api/v1/stats/{CCC} (Public)

Per-contributor statistics.

**Response (200):**
```json
{
  "ccc": "GTM",
  "total_all_time": 1247,
  "current_week": {
    "year": 2026,
    "week": 10,
    "count": 57,
    "highest_seq": 57
  },
  "instances_used": ["INT-OG1", "INT-P01"],
  "first_ccc_id": "GTM_2026-W02_001",
  "weeks_active": 9
}
```

#### GET /api/v1/validate/{CCC_ID} (Public)

Validate a CCC-ID exists in the registry.

**Response (200):**
```json
{
  "valid": true,
  "ccc_id": "GTM_2026-W10_057",
  "instance": "INT-OG1",
  "workspace": "CCC",
  "registered_at": "2026-03-03T07:54:00Z"
}
```

**Response (404):**
```json
{
  "valid": false,
  "ccc_id": "GTM_2026-W10_999",
  "error": "CCC-ID not found in registry"
}
```

---

## 📋 Database Schema

```sql
-- cccid.info Database Schema v1.0
-- PRJ-028 — ♾️ WeOwnNet 🌐

-- Main CCC-ID registry
CREATE TABLE ccc_ids (
    id SERIAL PRIMARY KEY,
    ccc VARCHAR(3) NOT NULL,
    year INTEGER NOT NULL CHECK (year >= 2024 AND year <= 2099),
    week INTEGER NOT NULL CHECK (week >= 1 AND week <= 53),
    seq INTEGER NOT NULL CHECK (seq >= 1 AND seq <= 999),
    instance VARCHAR(20) NOT NULL,
    workspace VARCHAR(20) DEFAULT 'CCC',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(ccc, year, week, seq)
);

-- Performance indexes
CREATE INDEX idx_ccc_week ON ccc_ids(ccc, year, week);
CREATE INDEX idx_ccc_latest ON ccc_ids(ccc, year DESC, week DESC, seq DESC);
CREATE INDEX idx_instance ON ccc_ids(instance);
CREATE INDEX idx_created ON ccc_ids(created_at);

-- Registered contributors
CREATE TABLE contributors (
    ccc VARCHAR(3) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    role VARCHAR(100),
    status VARCHAR(20) DEFAULT 'ACTIVE' CHECK (status IN ('ACTIVE', 'INACTIVE')),
    joined_week VARCHAR(8),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- API keys for authenticated endpoints
CREATE TABLE api_keys (
    id SERIAL PRIMARY KEY,
    key_hash VARCHAR(256) NOT NULL UNIQUE,
    instance VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP,
    active BOOLEAN DEFAULT true
);

-- Seed contributors
INSERT INTO contributors (ccc, name, role, joined_week) VALUES
('GTM', 'yonks', 'Co-Founder / Chief Digital Alchemist', '2026-W02'),
('THY', 'mrsyonks', 'Co-Founder / CEO / CFO', '2026-W02'),
('IAL', 'IamLotus', 'Co-Founder / Chief Catalyst Officer', '2026-W02'),
('RMN', 'Roman', 'AI Platform Engineer', '2026-W02'),
('LFG', 'CoachLFG', 'Co-Host / Coach', '2026-W02'),
('CRO', 'Webb', 'xCRO', '2026-W02'),
('LDC', 'Dhruv', 'Agentic AI Engineer / Project Lead', '2026-W02'),
('SHD', 'Shahid', 'Sr. Full-Stack DevOps Engineer', '2026-W02'),
('CEO', 'Stephanie Warlick', 'xCEO', '2026-W07');

COMMENT ON TABLE ccc_ids IS 'CCC-ID Registry v1.0 — PRJ-028 — ♾️ WeOwnNet 🌐';
```

### Schema Notes

| Table | Purpose | Rows (Est. Y1) |
|-------|---------|----------------|
| `ccc_ids` | Every CCC-ID ever generated | ~5,000-10,000 |
| `contributors` | Registered CCC holders | 9 (growing) |
| `api_keys` | Instance API authentication | 5-10 |

---

## 📋 Phased Rollout

### Phase 1: Manual Registration (W11-W12)

| # | Step | Detail |
|---|------|--------|
| 1 | Deploy FastAPI + PostgreSQL | cccid.info live |
| 2 | Generate API keys per instance | INT-OG1, INT-P01, INT-S003 |
| 3 | Agent generates CCC-ID normally | No change to current flow |
| 4 | Agent POSTs to /api/v1/register | After generation |
| 5 | Agent reports: "Registered at cccid.info ✅" | In response |

**Agent prompt addition (Phase 1):**
```
After generating a CCC-ID, register it:
POST https://cccid.info/api/v1/register
Include in response: "Registered at cccid.info ✅"
```

### Phase 2: Semi-Automatic (W13+)

| # | Step | Detail |
|---|------|--------|
| 1 | Agent queries BEFORE generating | GET /api/v1/next/{CCC}/{YYYY}/{WW} |
| 2 | API returns next available sequence | Agent uses it |
| 3 | Agent generates with API-provided sequence | Guaranteed unique |
| 4 | Agent registers AFTER generating | POST /api/v1/register |

**Agent prompt addition (Phase 2):**
```
BEFORE generating a CCC-ID:
1. GET https://cccid.info/api/v1/next/{CCC}/{YYYY}/{WW}
2. Use returned next_seq as the sequence number
3. Generate CCC-ID
4. POST https://cccid.info/api/v1/register
5. Report: "CCC-ID verified via cccid.info ✅"
```

### Phase 3: Fully Automatic (W15+)

| # | Step | Detail |
|---|------|--------|
| 1 | AnythingLLM webhook or n8n trigger | On CCC-ID generation |
| 2 | Automatic POST to cccid.info | No agent involvement |
| 3 | Real-time dashboard updates | Live stats |

---

## 📋 Public Dashboard

### cccid.info Home Page

```
┌─────────────────────────────────────────────────┐
│                                                  │
│           🤖 CCC-ID Registry                     │
│           cccid.info                             │
│                                                  │
│   Total CCC-IDs:    2,847                        │
│   Contributors:     9                            │
│   Active Instances: 5                            │
│   This Week (W10):  148                          │
│                                                  │
├─────────────────────────────────────────────────┤
│                                                  │
│   TOP CONTRIBUTORS (W10)                         │
│                                                  │
│   @GTM: 57  ████████████████████                 │
│   @THY: 46  ████████████████                     │
│   @RMN: 25  █████████                            │
│   @LFG: 11  ████                                 │
│   @CEO:  9  ███                                  │
│                                                  │
├─────────────────────────────────────────────────┤
│                                                  │
│   RECENT CCC-IDs                                 │
│                                                  │
│   GTM_2026-W10_057  INT-OG1  08:06 MST          │
│   THY_2026-W09_057  INT-OG1  22:45 EST          │
│   RMN_2026-W10_025  INT-OG8  19:00 EST          │
│                                                  │
├─────────────────────────────────────────────────┤
│                                                  │
│   [ API Docs (/docs) ]  [ GitHub ]  [ ccc.bot ] │
│                                                  │
│   Part of ♾️ WeOwnNet 🌐                        │
│   Powered by CCC (Contributor Code Convention)   │
│                                                  │
└─────────────────────────────────────────────────┘
```

---

## 📋 Deployment Checklist (16 Steps)

| # | Step | Owner | Depends On | Status |
|---|------|-------|-----------|--------|
| 1 | Create cccid_db on ATL1 PostgreSQL | @RMN | PRJ-021 (PG operational) | ⬜ |
| 2 | Run schema SQL (3 tables + indexes + seed) | @RMN | Step 1 | ⬜ |
| 3 | Create cccid_user (restricted permissions) | @RMN | Step 1 | ⬜ |
| 4 | Build FastAPI application | @RMN | None (parallel) | ⬜ |
| 5 | Write 7 API endpoints | @RMN | Step 4 | ⬜ |
| 6 | Write public dashboard (HTML/CSS) | @RMN / @GTM | Step 5 | ⬜ |
| 7 | Containerize (Dockerfile) | @RMN | Step 5 | ⬜ |
| 8 | Create Docker Compose (FastAPI + Caddy) | @RMN | Step 7 | ⬜ |
| 9 | Deploy to DO Droplet (ATL1) or co-locate | @RMN | Step 8 | ⬜ |
| 10 | Configure DNS (cccid.info → IP) | @GTM | Step 9 | ⬜ |
| 11 | Verify SSL (Caddy auto-SSL) | @RMN | Step 10 | ⬜ |
| 12 | Generate API keys per instance | @RMN | Step 11 | ⬜ |
| 13 | Store API keys in Infisical (PRJ-024) | @RMN | Step 12 | ⬜ |
| 14 | #SmokeTest (12-point) | @GTM | Step 13 | ⬜ |
| 15 | Backfill historical CCC-IDs (optional — W09-W10) | @GTM | Step 14 | ⬜ |
| 16 | FULL:SYNC:META | @GTM | Step 14 | ⬜ |

---

## 📋 Docker Compose

```yaml
# docker-compose.yml — cccid.info (PRJ-028)
version: '3.8'

services:
  cccid-api:
    build: .
    container_name: cccid-api
    restart: unless-stopped
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://cccid_user:${DB_PASSWORD}@${DB_HOST}:25060/cccid_db?sslmode=require
      - API_KEY_HASH=${API_KEY_HASH}
    depends_on: []

  caddy:
    image: caddy:2-alpine
    container_name: caddy-cccid
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./Caddyfile:/etc/caddy/Caddyfile
      - caddy_data:/data
      - caddy_config:/config

volumes:
  caddy_data:
  caddy_config:
```

### Caddyfile

```
cccid.info {
    reverse_proxy cccid-api:8000
}
```

### Dockerfile

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### requirements.txt

```
fastapi==0.109.0
uvicorn==0.27.0
psycopg2-binary==2.9.9
python-dotenv==1.0.0
```

### Cost

| Component | Monthly |
|-----------|---------|
| DO Droplet (ATL1, 1 vCPU / 1 GB) | **$6/mo** |
| PostgreSQL (shared with PRJ-018) | $0 |
| Domain (cccid.info — already owned) | $0 |
| SSL (Caddy) | $0 |
| **TOTAL** | **$6/mo** |

> **$6/mo for ecosystem-wide CCC-ID integrity.** The cheapest governance infrastructure in #FedArch.

---

## 📋 Verification (#SmokeTest) — 12-Point

| # | Test | Expected | Status |
|---|------|----------|--------|
| 1 | https://cccid.info loads | Dashboard renders | ⬜ |
| 2 | /docs loads | Swagger UI renders | ⬜ |
| 3 | POST /register (valid) | 201 + registered: true | ⬜ |
| 4 | POST /register (duplicate) | 409 + error message | ⬜ |
| 5 | GET /next/{CCC}/{YYYY}/{WW} | Returns next_seq | ⬜ |
| 6 | GET /latest/{CCC} | Returns highest CCC-ID | ⬜ |
| 7 | GET /latest/{CCC}/{YYYY}/{WW} | Returns week-specific highest | ⬜ |
| 8 | GET /stats | Returns global stats | ⬜ |
| 9 | GET /stats/{CCC} | Returns contributor stats | ⬜ |
| 10 | GET /validate/{CCC_ID} (exists) | valid: true | ⬜ |
| 11 | GET /validate/{CCC_ID} (not exists) | valid: false, 404 | ⬜ |
| 12 | POST without API key | 401 Unauthorized | ⬜ |

---

## 📋 Security

| Layer | Control |
|-------|---------|
| **Transport** | TLS 1.3 (Caddy auto-SSL) |
| **Authentication** | API key (X-API-Key header) for write operations |
| **Authorization** | Per-instance API keys — each instance has own key |
| **Database** | cccid_user — SELECT, INSERT only (no UPDATE, no DELETE) |
| **Rate limiting** | FastAPI middleware — 100 req/min per API key |
| **Input validation** | Pydantic models — CCC format, year/week/seq ranges |
| **CORS** | Restricted to known domains |
| **Secrets** | API keys + DB credentials in Infisical (PRJ-024) |

### Database User Permissions

```sql
CREATE USER cccid_user WITH PASSWORD '****';
GRANT CONNECT ON DATABASE cccid_db TO cccid_user;
GRANT USAGE ON SCHEMA public TO cccid_user;
GRANT SELECT, INSERT ON ALL TABLES IN SCHEMA public TO cccid_user;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO cccid_user;
-- NO UPDATE, NO DELETE — CCC-IDs are immutable once registered
```

> **CCC-IDs are IMMUTABLE.** Once registered, they cannot be modified or deleted. This is by design — the registry is an append-only audit log.

---

## 📋 CCC Domain Portfolio

| # | Domain | Role | PRJ |
|---|--------|------|-----|
| 1 | **ccc.bot** | PRIMARY website | PRJ-027 |
| 2 | **cccid.io** | Email (OCPA ProtonMail) | — |
| 3 | **cccid.info** | **Data/API (CCC-ID registry)** | **PRJ-028** |
| 4 | cccbot.net | Redirect → ccc.bot | PRJ-027 |
| 5 | cccbot.org | Redirect → ccc.bot | PRJ-027 |
| 6 | cccbot.us.com | Redirect → ccc.bot | PRJ-027 |
| 7 | cccbot.xyz | Redirect → ccc.bot | PRJ-027 |
| 8 | cccid.blog | Future — blog | ⬜ |
| 9 | cccid.us.com | Redirect → ccc.bot | PRJ-027 |
| 10 | cccid.xyz | Redirect → ccc.bot | PRJ-027 |

---

## 📋 Project Team

| CCC | Role | Focus |
|-----|------|-------|
| **GTM** | **Governance + Schema** | CCC-ID rules, schema, API spec, dashboard content |
| **RMN** | **API Build + Deploy** | FastAPI, Docker, PostgreSQL, deployment |
| **LDC** | **Agent Integration** (Phase 2+) | AnythingLLM API hooks, n8n triggers |

---

## 📋 Risk Matrix

| # | Risk | Prob | Impact | Mitigation |
|---|------|------|--------|------------|
| 1 | API downtime | Low | Medium | Tier 1 (manual) remains as fallback; Uptime Kuma monitors |
| 2 | Duplicate registration race condition | Low | Medium | UNIQUE constraint on (ccc, year, week, seq) — DB-level enforcement |
| 3 | API key compromise | Low | Medium | Per-instance keys; rotation via Infisical (PRJ-024); revocation endpoint |
| 4 | Historical data gap | Medium | Low | Backfill optional; forward-looking registry is sufficient |
| 5 | Agent integration complexity | Low | Medium | Phase 1 = manual POST; complexity deferred to Phase 2+ |
| 6 | PostgreSQL shared cluster load | Low | Low | ccc_ids table = tiny (~10K rows Y1); negligible load |

---

## 📋 Relationship to Other Projects

| PRJ | Connection |
|-----|-----------|
| **PRJ-018** | Shared PostgreSQL cluster (ATL1) — same DB host, different database |
| **PRJ-021** | DO Infrastructure — PostgreSQL must be operational |
| **PRJ-023** | Same pipeline pattern (data → PG) — different problem domain |
| **PRJ-024** | Infisical manages API keys + DB credentials |
| **PRJ-017** | Phoenix traces API calls (Phase 0+) |
| **PRJ-027** | ccc.bot links to cccid.info stats dashboard |
| **ALL instances** | Every instance POSTs CCC-IDs to cccid.info |

---

## 📋 Discovered By (BP-047)

| CCC | Contributor | Role | Context |
|-----|-------------|------|---------|
| GTM | [yonks](https://GitHub.com/YonksTEAM) | Co-Founder / Chief Digital Alchemist | R-212 Tier 3 concept — centralized CCC-ID counter; domain portfolio analysis revealed cccid.info = perfect fit; #BadAgent #13 (W06) = catalyst |

---

## 📋 Related Documents

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| SharedKernel | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/SharedKernel.md) |
| CCC | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/CCC.md) |
| PROTOCOLS (R-212) | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/PROTOCOLS.md) |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| 3.2.1.1 | 2026-W10 | GTM_2026-W10_057 | GTM_2026-W10_059 | Initial project; cccid.info centralized CCC-ID registry; R-212 Tier 3 (skip Tier 2); FastAPI + PostgreSQL; 7 REST API endpoints; 3-phase rollout (manual → semi-auto → automatic); public stats dashboard; 3-table schema (ccc_ids, contributors, api_keys); Docker Compose + Caddyfile; 16-step deployment; 12-point #SmokeTest; 6-risk matrix; $6/mo; append-only immutable registry; 10 CCC domains catalogued |

---

#FlowsBros #FedArch #CCCID #Registry #R212 #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
