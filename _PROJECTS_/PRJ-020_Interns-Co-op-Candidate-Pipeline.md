# PRJ-020_Interns-Co-op-Candidate-Pipeline.md

## 📋 Document Metadata

| Field | Value |
|-------|-------|
| **Document** | PRJ-020_Interns-Co-op-Candidate-Pipeline.md |
| **Version** | **v3.2.3.1** |
| **CCC-ID** | RMN_2026-W12_061 |
| **Approval CCC-ID** | GTM_2026-W11_318 |
| **Created** | 2026-W12 |
| **Updated** | **2026-03-19 (W12)** |
| **Season** | #WeOwnSeason003 🚀 |
| **Status** | 🚀 GH LIVE |
| **#LLMmodel** | Qwen3.5-397B-A17B |
| **Source of Truth** | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-020_Interns-Co-op-Candidate-Pipeline.md) |
| **R-199** | Candidate data = RAG ONLY, NEVER GitHub |

---

## 📖 Table of Contents

1. [Project Identity](#-project-identity)
2. [Executive Summary](#-executive-summary)
3. [Pipeline Architecture](#-pipeline-architecture)
4. [Evaluation Framework](#-evaluation-framework)
5. [Technical Decisions](#-technical-decisions)
6. [Issues Encountered + Resolved](#-issues-encountered--resolved)
7. [PostgreSQL Integration (PRJ-018 + PRJ-021)](#-postgresql-integration-prj-018--prj-021)
8. [Next Actions](#-next-actions)
9. [Future Documentation](#-future-documentation)
10. [Version History](#-version-history)
11. [Related Documents](#-related-documents)
12. [Discovered By (BP-047)](#-discovered-by-bp-047)
13. [Governance Compliance](#-governance-compliance)

---

## 📋 Project Identity

| Field | Value |
|-------|-------|
| Project ID | **PRJ-020** |
| Title | **Interns Co-op — Candidate Pipeline** |
| Type | Infrastructure + HR — AI Evaluation |
| Priority | 🔴 P0 |
| Owner | @RMN (Roman Di Domizio) |
| Workspace | **intern-eval** (INT-P01) |
| Backend | n8n (DOKS ATL1) + AnythingLLM + PostgreSQL POP DB |
| Timeline | **W10-W12** |
| #masterCCC | GTM_2026-W10_026 |
| Approval CCC-ID | GTM_2026-W11_318 |

---

## 📋 Executive Summary

### What Is PRJ-020?

PRJ-020 is an AI-powered candidate evaluation pipeline for the WeOwnNet Interns Co-op program. The pipeline automates the screening, scoring, and ranking of intern applications using a combination of structured rules (n8n) and LLM evaluation (AnythingLLM + Qwen3.5-397B-A17B).

### MVP Status

| Field | Value |
|-------|-------|
| **Pipeline Status** | ✅ Complete and operational |
| **Batches Processed** | Multiple (application reopened for additional candidates) |
| **Pipeline Runtime** | ~35 minutes per batch |
| **Hours Invested** | First-time pipeline build |

### W11-W12 Updates

| Field | Value |
|-------|-------|
| **Application Status** | 🔄 REOPENED (additional candidates processed) |
| **Scoring Update** | @THY requested: 10 pts MAX for military AND/OR sports (combined, not stacked) |
| **Priority Change** | Prioritize "available to start now" candidates |
| **PostgreSQL Integration** | ⬜ TODO (PRJ-018 interns schema) |
| **Next Action** | Save all results to POP DB, document full process in replication document |

### Why This Matters

| Without PRJ-020 | With PRJ-020 |
|-----------------|--------------|
| Manual review: 20-30+ hours | ✅ ~35 minutes automated |
| Reviewer fatigue + bias drift | ✅ Consistent rubric for all |
| Surface-level screening | ✅ Deep LLM analysis (skills inflation, AI-generated content, cross-reference claims) |
| No audit trail | ✅ Full JSON output with every score + reasoning |
| One-time effort | ✅ Reusable pipeline for future cohorts |

---

## 📋 Pipeline Architecture

### Data Flow

```
WordPress Fluent Forms API
    │
    ▼
n8n Pass 1: Hard Filters + Structured Scoring
    │
    ▼
AnythingLLM Pass 2: Full LLM Evaluation (6 categories, 100 pts)
    │
    ▼
AnythingLLM Pass 3: Meta-Review + Final Recommendation
    │
    ▼
PostgreSQL POP DB (PRJ-018) — 5 tables
    ├── applicants
    ├── applications
    ├── application_skills
    ├── application_evaluations
    └── application_ranks
```

### Infrastructure

| Component | Detail |
|-----------|--------|
| **n8n** | 18+ nodes, self-hosted on DOKS (ATL1, We Own Academy) |
| **AnythingLLM** | INT-P01, dedicated `intern-eval` workspace |
| **LLM** | Qwen3.5-397B-A17B |
| **Data Source** | WordPress Fluent Forms Pro REST API (`www.weown.xyz`) |
| **Resume Processing** | n8n Extract From File (PDF → text) |
| **Storage** | PostgreSQL POP DB (PRJ-018) — db-postgresql-atl1-weownnet |

### RAG Documents (INT-P01 intern-eval workspace)

| Document | Purpose |
|----------|---------|
| `RUBRIC.md` | Full scoring rubric — categories, points, criteria, examples |
| `JOB-DESCRIPTION.md` | Intern posting — role, stack, tracks, requirements |
| `SUCCESS-CRITERIA.md` | @THY directives, ideal candidate, priority stack |
| `SCORING-RULES.md` | Formulas, hard filters, JSON schemas |

---

## 📋 Evaluation Framework

### Hard Filters (Auto-DQ)

| Filter ID | Criteria | Notes |
|-----------|----------|-------|
| **HF-1** | Country flag (IP geolocation) | Removed as DQ — flag only (unreliable) |
| **HF-2** | Not authorized to work in US | Required for co-op structure |
| **HF-3** | "Not interested" in one or more skills | Must be willing to learn all tracks |
| **HF-4/5** | Short answer too short (< 15 chars) | Effort indicator |

### LLM Evaluation Categories (Per Application)

| Category | Max Points | What Is Scored |
|----------|:----------:|----------------|
| Short Answer Quality | 25 | Thoughtfulness, specificity, effort |
| Resume & Links Evaluation | 25 | Skills claims vs evidence, GitHub quality |
| Attitude & Willingness to Learn | 20 | Growth mindset, coachability |
| Track Alignment & Consistency | 15 | Match between stated interest + resume |
| Communication Quality | 10 | Clarity, professionalism |
| Major Alignment | 5 | Relevant field of study |
| **LLM Total** | **100** | |

### Scoring Formula

#### Current (W11-W12 — @THY Changes)

```
Final = (Structured / structured_max × 35) + (LLM / 100 × 65) + Availability + Bonus

Where:
- Structured: Hard filters + skills matrix (35%)
- LLM: 6 categories (65%)
- Availability: +5 if "available to start now"
- Bonus: +10 MAX for military AND/OR sports (combined — not stacked)
- Max Possible: 115
```

### Bonus Criteria (@THY Priority Stack)

| Bonus | Points | How Detected | Important Note |
|-------|:------:|--------------|----------------|
| Military/Veteran | +10 | LLM scans resume for service indicators | **MAX 10 pts combined** |
| College Athlete | +10 | LLM scans resume for sports participation | **If candidate has BOTH, still only 10 pts total** |

> **⚠️ CRITICAL:** Bonus points are NOT stacked. If a candidate has both military service AND college athlete status, they receive +10 points MAX (not +20). This prevents double-dipping; the bonus is for service/commitment, not for accumulating traits.

### Priority Stack (THY-defined)

| Priority | Criteria | Weight |
|----------|----------|:------:|
| 1 | Attitude | 20 pts (LLM category) |
| 2 | Skill | 25 pts (LLM category) + 35% structured |
| 3 | Availability | +5 pts bonus (W11-W12 NEW) |
| 4 | Location | Tiebreaker (Denver, Las Vegas, Orlando, Nashville) |
| 5 | Bonus (Military/Sports) | +10 pts MAX combined (updated W11-W12) |

### Pass 3 Meta-Review Output

| Output | Detail |
|--------|--------|
| Consistency check | Structured vs LLM scores |
| Skills inflation detection | LLM flags exaggeration |
| AI-generated content detection | LLM identifies AI-written answers |
| Red flags | 2-3 specific, concrete |
| Strengths | 2-3 specific, concrete |
| Overall narrative summary | Full candidate profile |
| Recommendation | ADVANCE / MAYBE / PASS with confidence level |
| Interview questions | 2-3 personalized per candidate |

---

## 📋 Technical Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Scoring split | 35% structured / 65% LLM | LLM handles nuanced evaluation |
| Track multiplier | None — equal skill weights | Prevents gaming; LLM handles track fit |
| HF-1 country check | Removed — flag only | IP geolocation unreliable |
| n8n keyword scan for bonuses | Removed | LLM scans resume instead |
| Variable structured_max | Per applicant | Form changed during live period — fair scoring |
| AnythingLLM mode | `query` not `chat` | Prevents context accumulation over 30+ calls |
| Resume extraction | n8n Extract From File (PDF) | Native, no external dependency |
| Error handling | try/catch + ignoreHttpStatusErrors | Failed LLM calls don't crash the batch |
| n8n task timeout | Increased to 1800s | Required for batch processing |

---

## 📋 Issues Encountered + Resolved

| Issue | Resolution |
|-------|-----------|
| Fluent Forms API endpoint wrong | Corrected to `/submissions?form_id=8` not `/forms/8/entries` |
| Domain needed `www` prefix | `www.weown.xyz` not `weown.xyz` |
| Response field is JSON string | Added `JSON.parse(entry.response)` in parser |
| Skills matrix values are arrays | Access `[0]` — `["Strong experience"]` not `"Strong experience"` |
| Extract From File strips app data | Added Merge node to reunite resume text with app data |
| n8n Code node has no `fetch` | Used `this.helpers.httpRequest` instead |
| JSON expression escaping in HTTP node | Replaced HTTP Request node with Code node for LLM calls |
| n8n task runner 300s timeout | Set `N8N_RUNNERS_TASK_TIMEOUT=1800` |
| AnythingLLM chat history accumulation | Switched to `query` mode for batch processing |
| IP geolocation unreliable for location | Removed HF-1, flagged country mismatch for LLM review |
| Form changed during live period | Variable skill count handling with `-1` for missing skills |

---

## 📋 PostgreSQL Integration (PRJ-018 + PRJ-021)

### Storage Location

| Field | Value |
|-------|-------|
| **Database** | db-postgresql-atl1-weownnet (DO Managed PG) |
| **Cluster** | PRJ-021 (DigitalOcean Infrastructure) |
| **Schema** | PRJ-018 (P.O.P. Database) — interns tables |
| **Tables** | 5 (applicants, applications, application_skills, application_evaluations, application_ranks) |
| **Storage Estimate** | <10 MB (negligible on 15 GiB cluster) |

### Data Flow to PostgreSQL

| Step | Action | Owner |
|------|--------|-------|
| 1 | n8n completes Pass 3 (meta-review) | @RMN |
| 2 | n8n INSERT into 5 tables | @RMN |
| 3 | Verify data integrity | @RMN |
| 4 | Generate summary reports per candidate | @RMN |
| 5 | Share with @GTM, @THY, @CEO | @RMN |

### Required PostgreSQL Setup (PRJ-021 P0 Tasks)

| # | Task | Status |
|---|------|--------|
| 1 | Configure Trusted Sources (add n8n, INT-OG8, INT-OG1, INT-P02) | ⬜ TODO |
| 2 | Download SSL CA certificate | ⬜ TODO |
| 3 | CREATE EXTENSION citext | ⬜ TODO |
| 4 | CREATE USER p012_app + GRANT | ⬜ TODO |
| 5 | Run PRJ-020 schema (5 tables) | ⬜ TODO |
| 6 | Store p012_app creds in Infisical | ⬜ TODO (Infisical broken) |
| 7 | Verify n8n can connect as p012_app | ⬜ TODO |

---

## 📋 Next Actions

| # | Task | Priority | Est. Hours | Status |
|---|------|----------|:----------:|--------|
| 1 | Save all results to PRJ-018 POP DB | 🔴 HIGH | 2h | ⬜ TODO |
| 2 | Review top candidates from all batches | 🔴 HIGH | 2h | ⬜ TODO |
| 3 | Select 5 for interviews | 🔴 HIGH | 0.5h | ⬜ TODO |
| 4 | Schedule interviews with @RMN + @CEO | 🔴 HIGH | 1h | ⬜ TODO |
| 5 | Email ADVANCE candidates — confirm start date + availability | 🔴 HIGH | 0.5h | ⬜ TODO |
| 6 | Share results with @GTM, @THY, @CEO | 🟡 MEDIUM | 0.5h | ⬜ TODO |
| 7 | Create replication document (full process + results) | 🟠 P1 | 3h | ⬜ TODO |
| 8 | Evaluate Deel.com (global compliance, payments, co-op support) | 🟡 P2 | 2h | ⬜ TODO |

### Deel.com Evaluation Criteria

| Criteria | Detail |
|----------|--------|
| Global compliance | Background checks, employment law per country |
| Payment processing | International payments, multiple currencies |
| Co-op support | Support for cooperative entities (not just LLCs) |
| Pricing | Small-scale and international candidate pricing |
| Integration | Notion, Signal, existing tools |
| Unpaid internships | Handling of unpaid internship arrangements |

---

## 📋 Future Documentation

### Replication Document (To Be Created by @RMN)

| Field | Value |
|-------|-------|
| **Purpose** | Document full workflow process, results, and replication steps |
| **Owner** | @RMN |
| **Status** | ⬜ TODO (W12-W13) |
| **Content** | n8n workflow export, step-by-step setup, full results analysis, lessons learned |
| **Audience** | Future HR/Recruiting teams, future @RMN successors |
| **Location** | `_PROJECTS_/PRJ-020_Interns-Co-op-Replication.md` |

### What This Document Contains vs. Replication Document

| This Doc (PRJ-020) | Replication Doc (Future — @RMN to create) |
|--------------------|-----------------------------------------|
| Pipeline architecture | Full n8n workflow export |
| Evaluation framework | Step-by-step setup guide |
| Scoring formula | Complete results analysis |
| Issues + resolutions | Troubleshooting guide |
| PostgreSQL integration | Screenshots + video walkthrough |
| Time tracking | Cost breakdown + ROI analysis |
| **NO specific applicant results** | **Full results (anonymized)** |
| **NO cost info** | **Complete cost breakdown** |

> **Note:** Candidate PII (names, emails, scores) stored in PostgreSQL POP DB only — NEVER in GitHub (R-199). Specific workflow results and applicant data will be documented in the future replication document created by @RMN, not in this PRJ doc.

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| **3.2.3.1** | **2026-W12** | **GTM_2026-W10_026** | **GTM_2026-W11_318** | **Initial document creation — PRJ-020 Interns Co-op Candidate Pipeline. Pipeline architecture (n8n + AnythingLLM + PostgreSQL), evaluation framework (hard filters, 6 LLM categories, scoring formula), @THY scoring updates (10 pts MAX bonus for military AND/OR sports combined, +5 availability), technical decisions, 12 issues encountered + resolved, PostgreSQL integration (PRJ-018 + PRJ-021), next actions, future replication document noted (to be created by @RMN W12-W13)** |

---

## 📋 Related Documents

| Document | Version | #masterCCC | Approval | Location |
|----------|---------|------------|----------|----------|
| PRJ-018_POP-Database.md | 3.2.3.1 | GTM_2026-W10_026 | GTM_2026-W11_308 | _PROJECTS_/ |
| PRJ-021_DO-Infrastructure.md | 3.2.3.1 | GTM_2026-W10_026 | ⬜ AWAITING | _PROJECTS_/ |
| PRJ-020_Interns-Co-op-Replication.md | TBD | TBD | ⬜ TBD | _PROJECTS_/ (Future — @RMN to create) |
| GUIDE-010_PostgreSQL-Setup.md | 3.2.1.1 | GTM_2026-W10_026 | GTM_2026-W10_073 | _GUIDES_/ |
| GUIDE-011_Governance-Oversight-VSA-Process.md | 3.2.1.1 | GTM_2026-W10_066 | GTM_2026-W10_073 | _GUIDES_/ |

---

## 📋 Discovered By (BP-047)

| CCC | Contributor | Role | Context |
|-----|-------------|------|---------|
| RMN | Roman Di Domizio | AI Platform Engineer | Conceived + built PRJ-020 eval pipeline (W10), first-time pipeline build, multiple batches processed |
| THY | Tyler Younker | CFO | Requested POP DB storage (not separate DB), scoring updates (10 pts MAX bonus combined for military/sports), prioritize availability |
| GTM | Jason Younker | Co-Founder | Approved PRJ assignment (GTM_2026-W10_026), GUIDE-011 compliance, PRJ-020 approval (GTM_2026-W11_318) |

---

## 📋 Governance Compliance

| Requirement | Status |
|-------------|--------|
| #masterCCC | ✅ GTM_2026-W10_026 |
| Approval CCC-ID | ✅ GTM_2026-W11_318 |
| Version History | ✅ Included |
| Related Documents | ✅ Included |
| Discovered By (BP-047) | ✅ Included |
| Lifecycle Stage | 🚀 GH LIVE (PostgreSQL integration pending) |
| VSA Eligibility | ✅ FULL or DEEP FULL (at APPROVED+ stage) |
| GUIDE-011 | ✅ APPROVED — compensation eligible |
| R-199 (PII Protection) | ✅ Candidate data = RAG ONLY, NEVER GitHub |

---

#FlowsBros #FedArch #PRJ-020 #PRJ-018 #InternsCoop #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
