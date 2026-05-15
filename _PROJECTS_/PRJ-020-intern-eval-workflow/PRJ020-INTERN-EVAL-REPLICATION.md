# 📘 REPLICATION GUIDE: PRJ-020 Intern Evaluation Pipeline

| **Metadata** | **Value** |
|---|---|
| **Doc ID** | `DOC-PRJ020-REPL-V3.4.3.1` |
| **Owner** | @RMN (Roman Di Domizio) |
| **Target** | DevOps / Platform Engineering Intern (PRJ-020) |
| **Repo Location** | `CCCbotNet/fedarch` → `_PROJECTS_/PRJ-020-intern-eval-workflow` |
| **Version** | 3.4.3.1 |
| **Status** | 🏁 COMPLETE & AUDITED |
| **Tech** | n8n (`n8n.weown.app`), WordPress & FluentForms (`weown.xyz`), AnythingLLM + Qwen (`ai.weown.agency`) |
| **Last Updated** | 2026-05-15 |

---

> ⛔ **REPLICATION & AUTOMATION RECOMMENDATION:** For immediate replication or future cohort runs, **the manual FluentForms API extraction and the manual one-time Python export to PostgreSQL are highly recommended to be automated or improved**. Relying on manual pulls creates duplicate evaluations, race conditions, and excessive manual overhead. **Before re-running this pipeline for another intake, implement a FluentForms → n8n webhook trigger, add strict date-cutoff logic, and replace the Python script with a native n8n PostgreSQL upsert node.** (See Section 10 for implementation path).

---

## 📑 Table of Contents

- [1. Project Overview & Target Profile](#1-project-overview--target-profile)
- [2. Application Form Architecture (FluentForms)](#2-application-form-architecture-fluentforms)
- [3. LLM Workspace & Context (AnythingLLM)](#3-llm-workspace--context-anythingllm)
- [4. n8n Workflow Architecture & Trigger Limitations](#4-n8n-workflow-architecture--trigger-limitations)
- [5. Step-by-Step Workflow Setup & Node Breakdown](#5-step-by-step-workflow-setup--node-breakdown)
  - [Setup Instructions](#setup-instructions)
  - [Node-by-Node Breakdown](#node-by-node-breakdown-exact-names-from-workflow)
    - [Phase 1: Input & Ingestion](#%F0%9F%9F%A6-phase-1-input--ingestion)
    - [Phase 2: Pass 1 – Hard Filters & Structured Scoring](#%F0%9F%9F%A8-phase-2-pass-1--hard-filters--structured-scoring)
    - [Phase 3: Resume Processing](#%F0%9F%9F%A7-phase-3-resume-processing)
    - [Phase 4: Pass 2 – LLM Evaluation](#%F0%9F%9F%A9-phase-4-pass-2--llm-evaluation)
    - [Phase 5: Scoring & Pass 3 Routing](#%F0%9F%9F%A6-phase-5-scoring--pass-3-routing)
    - [Phase 6: Pass 3 – Meta-Review & Hard Overrides](#%F0%9F%9F%AA-phase-6-pass-3--meta-review--hard-overrides)
    - [Phase 7: Aggregation & Export](#%F0%9F%9F%A5-phase-7-aggregation--export)
- [6. Critical Workflow Logic Notes](#6-critical-workflow-logic-notes)
- [7. Complete Results Analysis (Anonymized)](#7-complete-results-analysis-anonymized)
- [8. Troubleshooting & Common Failure Points](#8-troubleshooting--common-failure-points)
- [9. Cost Breakdown & ROI Analysis](#9-cost-breakdown--roi-analysis)
- [10. PostgreSQL Data Pipeline Integration (Python Export)](#10-postgresql-data-pipeline-integration-python-export)
- [11. Future Automation & Scaling Recommendations](#11-future-automation--scaling-recommendations)
- [Appendix: Quick Reference](#appendix-quick-reference)

---

## 1. Project Overview & Target Profile

**Purpose:** Automated, rubric-driven evaluation pipeline for DevOps / Platform Engineer Intern applications.  
**Target Candidate:** Students & recent grads interested in K8s, GitOps, AI/LLM infra, self-hosted OSS, and cooperative ownership.  
**Hiring Priority Stack (per THY directive):**
1. **Attitude** — Willingness to learn, honesty, genuine ecosystem interest
2. **Skill** — Evidence from resume, skills matrix, short answers
3. **Location** — US-based prioritized. All US locations equal. Non-US flagged for manual review.

**Output:** Ranked shortlist (ADVANCE/MAYBE/PASS) with full auditable scoring, interview questions, and hiring pipeline status.

---

## 2. Application Form Architecture (FluentForms)

**Platform:** WordPress FluentForms (`weown.xyz`)  
**Form ID:** `8`  
**Public Application Link:** https://www.weown.xyz/ai/devops-intern-application/  
**FluentForms Editor Link:** https://www.weown.xyz/wp-admin/admin.php?page=fluent_forms&route=editor&form_id=8  
**Data Source:** WP REST API (`/wp-json/fluentform/v1/submissions`)

### Field Mapping & Keys
| FluentForms Key | Label / Purpose | Type | Validation |
|---|---|---|---|
| `names` | First & Last Name | Names | Required |
| `email` | Email Address | Email | Required |
| `numeric_field_10` | Phone Number | Number | Optional |
| `checkbox_1` | Location(s) | Checkbox | Multi-select |
| `input_radio_3` | College Major | Radio | Required |
| `datetime_1` | Graduation Date | Date | Required |
| `input_radio` | Hours/Week | Radio | 10, 20, or 40 |
| `input_radio_2` | Start Timeframe | Radio | Immediately / Soon / Summer |
| `datetime` | Preferred Start Date | Date | Optional |
| `input_radio_1` | US Work Auth? | Radio | **Critical:** Must be "yes" |
| `file-upload_3` | Resume Upload | File | PDF only |
| `url` | GitHub URL | URL | Optional |
| `url_2` | LinkedIn URL | URL | Optional |
| `url_3` | Portfolio/Website | URL | Optional |
| `checkbox_2` | Tracks of Interest | Checkbox | Multi-select |
| `checkbox_3` | Track Experience | Checkbox | Multi-select |
| `tabular_grid` | Skills Matrix | Grid | 16 Skills × 4 Levels |
| `description` | Short Answer 1: OCPA Interest | Textarea | Required (>15 chars) |
| `description_2` | Short Answer 2: Self-Hosted K8s | Textarea | Required (>15 chars) |
| `description_1` | Short Answer 3: Anything Else | Textarea | Optional |
| `checkbox` | Newsletter Opt-in | Checkbox | Optional |

### Skills Matrix (16 Fixed Grid Items)
Mapped in `tabular_grid` key. Levels: `Not interested (0)`, `Willing to learn (1)`, `Some experience (2)`, `Strong experience (3)`.

1. `Linux & Docker basics`
2. `Kubernetes (core concepts, ingress, networking/DNS)`
3. `Helm charts (build/upgrade + values)`
4. `GitOps (Argo CD / Argo tools)`
5. `Infrastructure-as-Code (IaC; Terraform / OpenTofu)`
6. `CI (GitHub Actions / GitLab)`
7. `Metrics, dashboards, and alerting (Prometheus / Grafana)`
8. `Log pipelines (Loki / Alloy)`
9. `Access & security basics (RBAC/SSO, NetworkPolicies, TLS)`
10. `Policy-as-code (Kyverno / OPA Gatekeeper)`
11. `Secrets management (Vault / Infisical / SOPS)`
12. `PostgreSQL fundamentals (SQL, indexing, transactions)`
13. `DB operations on Kubernetes (backups/restores, HA, operators)`
14. `WordPress (self-hosted)`
15. `n8n (automation/workflows)`
16. `LLM ops on K8s (agents, RAG, MCP, inference)`

---

## 3. LLM Workspace & Context (AnythingLLM)

**Instance:** `ai.weown.agency` (Self-Hosted AnythingLLM)  
**Workspace:** `intern-eval`  
**Auth:** Bearer Token `[SEE: ANYTHINGLLM UI SETTINGS]`  
**Purpose:** Serves as the brain for Pass 2 and Pass 3 evaluations. The n8n workflow sends the application data to this workspace, which retrieves context from its attached documents to apply the rubric accurately and generate the specific JSON schema.

### 📁 Attached Documents (4)
*These documents are ONLY in this workspace and dictate how the LLM evaluates.*

1. **`JOB-DESCRIPTION.md`** — Defines the role, team, ecosystem, and core requirements.
2. **`RUBRIC.md`** — The authoritative scoring guide (3-pass pipeline, criteria, weightings).
3. **`SCORING-RULES.md`** — Math formulas, normalization steps, and hard filter logic.
4. **`SUCCESS-CRITERIA.md`** — Hiring goals, priority stack, and ideal candidate profile.

### 📍 Workspace Management & Token Retrieval
*   **UI Access:** `https://ai.weown.agency/workspace/intern-eval`
*   **Prompt Rule:** If conflict between `System Prompt` and `RUBRIC.md`, **RUBRIC.md takes precedence**.
*   **Model:** Qwen3.5-397B-A17B
*   **Updates:** To change scoring rules, update the `.md` files in this workspace. The workflow will pick up changes immediately on next run.
*   **🔑 Token Location:** The Bearer token is currently hardcoded directly inside the `LLM Pass 2 - Evaluate` and `LLM Pass 3 - Meta Review` nodes under the `Authorization` header. 
*   **🔄 To Generate a New Token:**
    1. Log into `ai.weown.agency` as Admin.
    2. Go to **Settings > API Keys**.
    3. Click **Create New API Key**.
    4. Copy and paste the new key directly into the `Authorization: Bearer <KEY>` line inside the respective n8n Code nodes.

---

## 4. n8n Workflow Architecture & Trigger Limitations

**Host:** `n8n.weown.app`  
**Workflow ID:** `7RFrLRAqikBKdPuL`  
**Trigger:** **Manual Execution Only** (currently no webhook/auto-trigger on new submissions)  
**Current Behavior:** Pulls ALL form entries at once via API (`per_page=100`), including previously evaluated applicants.

### ⚠️ Critical Limitation
Because the workflow exports the entire form history on each run, you will get duplicate evaluations unless:
1. **Date Cutoff** is added to filter only submissions after a specific timestamp
2. **New Form** is created per hiring cohort (recommended)
3. **Auto-Trigger Webhook** is built to push only NEW submissions to n8n

**Recommendation for Future Runs:** Build a FluentForms → n8n webhook trigger + deduplication node, or archive the current form and spin up a fresh one per intake.

---

## 5. Step-by-Step Workflow Setup & Node Breakdown

### Setup Instructions
1. Import the n8n workflow JSON into `n8n.weown.app`
2. Configure credentials:
   - **WP App Password:** Located in the `Fetch All Entries` node's Auth settings. *(To update: Go to WP Admin > Users > App Passwords, generate new, and paste into the node).*
   - **LLM Bearer Token:** Hardcoded directly in the `LLM Pass 2/3` code nodes. *(To update: Paste new AnythingLLM API key directly into the `Authorization` header string in those nodes).*
3. Set HTTP request timeouts to `180000ms` (3 min) to accommodate LLM generation
4. Run with **1 item** to validate JSON parsing before full batch

### Node-by-Node Breakdown (Exact Names from Workflow)

#### 🟦 Phase 1: Input & Ingestion
| Node Name | Type | Function | Key Details |
|-----------|------|----------|-------------|
| `Trigger - Batch` | Manual Trigger | Starts the workflow manually. | Configuration: None |
| `Fetch All Entries` | HTTP Request | Calls WP FluentForms REST API (`/wp-json/fluentform/v1/submissions?form_id=8&per_page=100`). | Auth: `httpHeaderAuth` (WP App Password). Returns `{ total: X, data: [...] }` wrapper. |
| `Unwrap + Split` | Code | Parses WP API wrapper, extracts `data` array, flattens into individual execution items. | Handles both array-wrapped and direct responses. Splits 1 big payload into N items. |
| `Parse Application` | Code | Maps raw form fields (`names`, `checkbox_1`, `tabular_grid`, etc.) to standardized app schema. | Extracts skills matrix, track interests, short answers, contact info. Sets base `json` structure. |

#### 🟨 Phase 2: Pass 1 – Hard Filters & Structured Scoring
| Node Name | Type | Function | Key Details |
|-----------|------|----------|-------------|
| `Hard Filters` | Code | Applies 5 hard disqualification rules & generates flags. | **HF-2:** Work auth ≠ "yes" → DQ<br>**HF-3:** Any skill = 0 ("Not interested") → DQ<br>**HF-4/5:** Short answers < 15 chars → DQ<br>**HF-6:** All answered skills = 3 (max inflation) → DQ<br>Flags: `inflation_flag`, `country_mismatch`, `missing_skills` |
| `Route Pass/Fail` | IF Node | Splits flow based on `passed` boolean. | `True` → `Structured Scoring`<br>`False` → `Log DQ` |
| `Log DQ` | Code | Formats disqualified entries for final output merge. | Sets `status: DISQUALIFIED`, `recommendation: PASS`, `final_score: 0`. Carries `disqualify_reason`. |
| `Structured Scoring` | Code | Calculates Pass 1 score (35% weight). | Formula: `skills_sum + hours_pts(0-3) + website_pts(0-3) + answer3_pts(0-2)`. Outputs `structured_raw`, `structured_max`. |

#### 🟧 Phase 3: Resume Processing
| Node Name | Type | Function | Key Details |
|-----------|------|----------|-------------|
| `Download Resume` | HTTP Request | Fetches the applicant's PDF from `resume_url`. | Direct GET request. Binary output. |
| `Extract Resume Text` | Extract from File | Parses PDF → plain text. | ⚠️ **Critical Setting:** `onError: "continueErrorOutput"` prevents pipeline crash on bad PDFs. |
| `Merge Resume With App` | Merge Node | Joins scored app data with extracted resume text. | `combineBy: position`. Input 1: Scoring output. Input 2: PDF text. |
| `Attach Resume Text` | Code | Truncates text to 15k chars, counts pages, sets extraction status. | Adds `resume_pages`, `resume_pages_flag (>1)`, `resume_extraction_status`. Passes clean payload to Pass 2. |

#### 🟩 Phase 4: Pass 2 – LLM Evaluation
| Node Name | Type | Function | Key Details |
|-----------|------|----------|-------------|
| `Format Pass 2 Payload` | Code | Builds strict JSON schema & prompt rules. | Forces GitHub/Portfolio exclusion. Defines 6 scoring categories. Injects explicit "NO thinking process" rules. |
| `LLM Pass 2 - Evaluate` | Code/HTTP | POSTs to `intern-eval` workspace. | URL: `https://ai.weown.agency/api/v1/workspace/intern-eval/chat`<br>Headers: Bearer `[SEE: ANYLLM SETTINGS]`<br>Mode: `query`<br>Timeout: 3 min |
| `Parse Pass 2 Response` | Code | Strips LLM thinking blocks, extracts clean JSON. | Removes `ynchroneg>` & `Thinking Process:` prefixes. Strips markdown. Finds last valid `{}` block. Validates `scores` & `sorting` exist. Fallback: `llm_total: 0` |

#### 🟦 Phase 5: Scoring & Pass 3 Routing
| Node Name | Type | Function | Key Details |
|-----------|------|----------|-------------|
| `Combine Scores` | Code | Normalizes Pass 1 + Pass 2, calculates preliminary score. | `Pass1_normalized = (raw/max)*35`<br>`Pass2_normalized = (llm_total/100)*65`<br>`Bonus = 10 (if military/athlete) else 0`<br>`Final_prelim = Pass1_norm + Pass2_norm + Bonus` |
| `Format Pass 3 Payload` | Code | Condenses data for meta-review. | Strips `resume_text`, `github_url`. Passes only scores, flags, short answers, tracks. Reduces context to stay under 262K limit. |
| `Skip if Pass 2 Failed` | IF Node | Checks `skip_pass3` flag. | `False` → `LLM Pass 3 - Meta Review`<br>`True` → `Merge` (bypasses Pass 3) |

#### 🟪 Phase 6: Pass 3 – Meta-Review & Hard Overrides
| Node Name | Type | Function | Key Details |
|-----------|------|----------|-------------|
| `LLM Pass 3 - Meta Review` | Code/HTTP | POSTs condensed payload for consistency/AI/review. | Same LLM endpoint. Expects `meta_recommendation`, `meta_red_flags`, `meta_interview_questions`. |
| `Parse Pass 3 Response` | Code | Extracts Pass 3 results, defaults on error. | Parses JSON. Sets `recommendation`, `confidence`, `status: SCORED` or `PARSE_ERROR`. |
| `Code in JavaScript` | Code | **Hard Override Node** for final recommendation. | **Rules:**<br>• `score < 75` → `PASS`<br>• `75 ≤ score < 85` → `MAYBE`<br>• `score ≥ 85` → KEEP LLM `meta_recommendation`<br>• `country_mismatch` → `MAYBE`<br>• `flag_ai_content = suspected` → `PASS` |
| `Merge` | Merge Node | Joins Pass 3 scored items with skipped/failed items. | Input 1: Override node output. Input 2: Skipped Pass 3 output. |

#### 🟥 Phase 7: Aggregation & Export
| Node Name | Type | Function | Key Details |
|-----------|------|----------|-------------|
| `Merge All Candidates` | Merge Node | Joins evaluated path with disqualified path. | Input 1: Main scoring pipeline. Input 2: `Log DQ` output. Full dataset reconstruction. |
| `Build Summary` | Code | Sorts, ranks, categorizes. | Builds `top_5`, `full_ranking`, `preferred_city_top_5`, `country_flagged`, `advance/maybe/pass` arrays. Calculates pipeline stats. |
| `Human Review Summary` | Code | Deduplicates, builds concise review JSON. | Dedupes by email. Creates `all_advance`, `all_maybe`, `stats`, `interview_shortlist_emails`. Clean output for HR/Exec review. |
| `Save Results` | Code | Writes final JSON to n8n container filesystem. | Output: `/tmp/p012_eval_results_<timestamp>.json`. Returns `filename` & `saved_to` path. |

---

## 6. Critical Workflow Logic Notes

| Concept | Implementation |
|---------|----------------|
| **Error Resilience** | `Extract Resume Text` uses `continueErrorOutput`. LLM nodes catch HTTP errors and return `status: FAILED` instead of breaking the flow. |
| **Deduplication** | Handled at the very end in `Human Review Summary` using `Set` on `email` fields. Prevents retry loops from inflating candidate counts. |
| **Token Limit Management** | Pass 3 payload explicitly strips `resume_text`, `github_url`, `website_url`. Pass 2 response parsing searches for the **last** `{}` to avoid partial JSON. |
| **Recommendation Overrides** | `Code in JavaScript` enforces business rules *after* LLM evaluation. Ensures country mismatches & AI flags cannot bypass thresholds. |
| **Merge Strategy** | n8n `Merge` nodes use `combineByPosition`. Order is critical: Main pipeline must be Input 1, bypassed/DQ must be Input 2. |

---

## 7. Complete Results Analysis (Anonymized)

| Metric | Value |
|--------|-------|
| Total Applications | 95 |
| Auto-Disqualified | 24 |
| Scored Successfully | 71 |
| **ADVANCE (85+)** | **11** |
| **MAYBE (75–84)** | **28** |
| **PASS (<75 or flagged)** | **32** |

### Score Distribution
| Range | Count | Notes |
|-------|-------|-------|
| 90+ | 4 | Top tier, immediate availability, strong ecosystem research |
| 85–89 | 7 | Strong candidates, some require hour/location confirmation |
| 80–84 | 9 | Solid technical base, minor gaps or country flags |
| 75–79 | 11 | Borderline, require manual review or hour confirmation |
| <70 | 40 | Filtered out via hard rules, minimal effort, or major red flags |

### Key Observations
- **Country Mismatch Rate:** ~15% of scored apps flagged (non-US IP vs declared US location)
- **AI Content Flag:** <3% suspected; primarily flagged on generic/templated short answers
- **Availability Mismatch:** 30% of ADVANCE/MAYBE candidates requested <40 hrs or summer-only start
- **Top Strength Signal:** Named specific OCPA Group projects, self-hosted K8s, or WeOwnNet tools in short answers
- **Top Red Flag:** "Senior" titles for intern role, country mismatch, or all 16 skills rated "Strong" with no resume evidence

---

## 8. Troubleshooting & Common Failure Points

| Issue | Root Cause | Fix Applied |
|-------|-----------|-------------|
| `"."`, `","`, or empty responses | LLM rate limiting / timeout mid-generation | Added 3-retry logic (node `Check LLM Response` + `Retry Loop`), validates response starts with `{` |
| Thinking block leakage | Model generation behavior | Strips `ynchroneg>` block in `Parse Pass 2 Response` node before JSON extraction |
| Pass 3 context limit (262K) | Payload included full resume + Pass 2 reasoning | Node `Format Pass 3 Payload` strips `resume_text`, condenses Pass 2 to scores/flags only, removes RAG for Pass 3 |
| Schema mismatch | LLM followed RUBRIC.md instead of system prompt | Injected exact schema in `Format Pass 2 Payload`; explicit "NO Pass 3 fields in Pass 2" rule |
| Duplicate entries | Retry logic / batch re-processing | Node `Human Review Summary` filters by `email` before final output |
| Country-flagged candidates scoring ADVANCE | Country check ran before score thresholds | Reordered logic in `Code in JavaScript`: score thresholds → AI content → country mismatch |

---

## 9. Cost Breakdown & ROI Analysis

| Component | Cost | Notes |
|-----------|------|-------|
| OpenRouter API (Qwen 3.5 397B) | ~$18.00 | 71 scored × 3 passes × ~$0.0003/token avg |
| n8n Hosting | $0 (existing infra) | Self-hosted, minimal CPU/memory for JSON processing |
| Development Time | ~12 hours | Schema design, node iteration, prompt tuning, testing |
| Runtime Duration | ~35 minutes | Sequential processing with 2–4s delays between items |
| Review & Decision Time | ~2 hours | Manual verification of ADVANCE/MAYBE, interview scheduling |

### ROI Impact
- **Replaces:** 2–3 weeks of manual resume screening + rubric scoring.
- **Accuracy:** Consistent, auditable scoring across all 95 applications.
- **Scalability:** Can handle 500+ applications with same cost curve (~$0.25/app).
- **Audit Trail:** Full JSON logs, parse results, LLM reasoning preserved for compliance.
- **Time-to-Hire:** Reduced from ~14 days to ~5 days from close to interview shortlist.

---

## 10. PostgreSQL Data Pipeline Integration (Python Export)

### Overview & Architecture
Due to timeline constraints for the initial Q2 intake, automated n8n → PostgreSQL export was bypassed in favor of a reliable, one-time Python migration script. This script ingests the n8n workflow's comprehensive JSON output and writes it directly into `popdb` with full referential integrity, idempotency, and audit compliance.

**Database Location:** The data migration occurs into the `popdb` database, located within our ecosystem PostgreSQL cluster.  
**Path:** `WeOwnNet` Project → `We Own Labs` Team → DigitalOcean Managed PostgreSQL Cluster.

The script connects to `popdb` using least-privilege credentials (`pop_write`) via SSL. It maps the monolithic n8n JSON into four normalized tables, handles foreign key constraints, and leverages the `trg_applicant_to_people` trigger for identity management.

### Data Flow & Table Mapping
| Source Data | Target Table | Key Fields Mapped |
|-------------|--------------|-------------------|
| Contact Info, Tracks, Skills | `applicants` → `people` | `email`, `first_name`, `last_name`, `phone`, `location`, `linkedin`, `github`, `resume_url`. Auto-links to `people` table via trigger + backfill. |
| Submissions, Scores, Flags | `applications` | `applicant_id` (FK), `form_id`, `submitted_at`, `hours_per_week`, `skills_matrix` (JSONB), `short_answer_1/2/3`, `country`, `final_score`, `recommendation`, `confidence`, `rank`, `flag_ai_content`, `inflation_flag`. |
| 3-Pass Evaluation Breakdown | `application_evaluations` | `application_id` (FK), `evaluation_type` (pass1/2/3), `score`, `max_score`, `normalized_score`, `evaluation_data` (JSONB). |
| Final Ranking & Pipeline | `application_ranks` | `application_id` (FK), `rank`, `final_score`, `structured_normalized`, `llm_normalized`, `bonus_total`, `recommendation`, `confidence`, `pipeline_status`. |

### How to View Data
- **INT-P03 (`pop.weown.tools`):** Native SQL agent is disabled. Use the `pop-mcp` tools in the P.O.P. Workspace. Prompt examples:
  - `@agent Show me all ADVANCE candidates ranked by score`
  - `@agent Select id, first_name, email, pipeline_status from application_ranks where rank < 10 limit 10`
  - The `pop_db_read` tool enforces read-only access and automatically sanitizes PII (emails/phones) in responses.
- **Other Instances:** Use the native SQL Agent (`sql-query`) connected to `popdb` with the `pop_read` user. Query directly via the UI chat: `@agent Show me application_ranks WHERE pipeline_status = 'HIRED'`.
- **Direct CLI:** `psql "postgresql://pop_read:{PASS}@{HOST}:25060/popdb?sslmode=require&sslrootcert=/path/to/ca.crt"`

### How to Edit Data
Write access is strictly limited to INT-P03 via `pop-mcp`. In the P.O.P. Workspace, request: 
`@agent Update application_ranks SET pipeline_status = 'INTERVIEWED' WHERE id = X`
The `pop_db_write` tool enforces R-011: it will display the exact SQL, require explicit `yes` confirmation, and block all `DELETE` operations (enforcing soft-delete/archiving).

### Export Files & Directory Structure
All files are located in the following subdirectory: 
`CCCbotNet/fedarch/_PROJECTS_/PRJ-020-intern-eval-workflow/data-migration-popdb/`

| File | Purpose |
|------|---------|
| `intern_eval_comprehensive_2026-03-18.json` | Raw output from the n8n workflow. Contains all applicant data, scores, flags, and metadata. |
| `migrate-prj020.py` | Python script that parses the JSON, deduplicates by email, handles FK constraints, executes batched `INSERT ... ON CONFLICT DO UPDATE` commands, and commits/rolls back on error. |
| `validate-prj020.py` | Validation script that runs post-migration to verify row counts, FK integrity, score normalization, and data completeness against the source JSON. |
| `PRJ020_MIGRATION_REPORT.md` | Executive summary of the migration execution, timing, row counts (92 applicants, 204 evals, 92 ranks), and validation results. |

### Reusing the Script for a New Cohort
1. Run the n8n workflow for the new batch. Export the new JSON output.
2. Place the new JSON file in the `data-migration-popdb` directory and update the `SOURCE_FILE` variable in `migrate-prj020.py`.
3. Ensure dependencies are installed: `pip3 install psycopg2-binary python-dotenv`
4. Set environment variables for DB connection (`POP_DB_HOST`, `POP_DB_PORT`, `POP_BUSINESS_DB`, `POP_WRITE_USER`, `POP_WRITE_PASSWORD`, `POP_DB_SSL_CA`).
5. Run: `python3 migrate-prj020.py`
6. Run: `python3 validate-prj020.py`
*Note:* The script is idempotent. Safe to re-run on the same or updated JSON. It uses `ON CONFLICT` on unique keys (email, application_id) to update existing records without duplicating data.

### Path to Full Automation (n8n → PostgreSQL)
For future cohorts, replace the Python script with native n8n PostgreSQL operations:
1. Add a `PostgreSQL` node at the end of the n8n workflow.
2. Configure it with `pop_write` credentials (via Infisical/Env vars).
3. Use `INSERT ... ON CONFLICT (email) DO UPDATE` for `applicants` and `people`.
4. Use `application_id` as the FK key for `application_evaluations` and `application_ranks`.
5. Add a `date_cutoff` filter to only process submissions after a specific timestamp.
6. Trigger via FluentForms webhook instead of manual batch pull.
This eliminates the Python dependency, enables real-time dashboard updates, and fully automates the hiring pipeline.

---

## 11. Future Automation & Scaling Recommendations

| Improvement | Effort | Impact |
|-------------|--------|--------|
| FluentForms → n8n Webhook Trigger | 2 hrs | Eliminates manual export, processes only new submissions. |
| Date Cutoff / Cohort Form Separation | 30 min | Prevents duplicate evaluations. |
| PostgreSQL Upsert Node | 3 hrs | Fully automated DB pipeline, live hiring dashboard. |
| Auto-DQ Rule Tuning | 1 hr | Reduce false positives on short answers / skill inflation. |
| Interview Scheduler Integration | 4 hrs | Auto-email interview invites to ADVANCE candidates. |
| Multi-Cohort Support | 6 hrs | Reusable workflow with dynamic thresholds per intake. |

---

## Appendix: Quick Reference

### Core URLs & Tokens
- **n8n Instance:** `n8n.weown.app`
- **FluentForms API:** `https://www.weown.xyz/wp-json/fluentform/v1/submissions?form_id=8`
- **LLM Endpoint:** `https://ai.weown.agency/api/v1/workspace/intern-eval/chat`
- **LLM Workspace:** `https://ai.weown.agency/workspace/intern-eval` (Manage docs here)
- **Auth:** WP App Password & Bearer Token are **hardcoded directly in their respective n8n nodes**. 

### Score Thresholds (Current)
| Recommendation | Score | Confidence | Override Rules |
|---|---|---|---|
| **ADVANCE** | ≥ 85.00 | HIGH | LLM recommendation kept |
| **MAYBE** | 75.00 – 84.99 | MEDIUM / HIGH | Country mismatch auto-forces MAYBE |
| **PASS** | < 75.00 OR Flagged | HIGH / MEDIUM | AI content suspected → auto-PASS |

### Hard Filters (Auto-DQ)
- Work Authorization ≠ "yes"
- Any core skill = "Not interested" (0)
- Short Answer 1 or 2 < 15 characters
- 100% of answered skills rated "Strong" (3)
