# PRJ-023_Context-Persistence-Pipeline.md

## 📋 Document Metadata

| Field | Value |
|-------|-------|
| **Document** | PRJ-023_Context-Persistence-Pipeline.md |
| **Version** | **v3.2.3.1** |
| **CCC-ID** | RMN_2026-W12_067 |
| **Approval CCC-ID** | GTM_2026-W11_326 |
| **Created** | 2026-W12 |
| **Updated** | **2026-03-19 (W12)** |
| **Season** | #WeOwnSeason003 🚀 |
| **Status** | ✅ DECIDED — 🔄 IMPLEMENTATION W12 |
| **#LLMmodel** | Qwen3.5-397B-A17B |
| **Source of Truth** | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-023_Context-Persistence-Pipeline.md) |
| **Implementation** | mem0.ai (Apache 2.0 FOSS, 25k+ GitHub stars) |

---

## 📖 Table of Contents

1. [Project Identity](#-project-identity)
2. [Executive Summary](#-executive-summary)
3. [The Problem — Context Loss](#-the-problem--context-loss)
4. [Project Handoff — @RMN to @LDC (W10)](#-project-handoff--rmn-to-ldc-w10)
5. [Solution — mem0.ai Adoption](#-solution--mem0ai-adoption)
6. [Pipeline Architecture — Baseline (6 Steps)](#-pipeline-architecture--baseline-6-steps)
7. [PRJ-028 Interweave — Shared Pipeline](#-prj-028-interweave--shared-pipeline)
8. [Infrastructure — Detailed Specifications](#-infrastructure--detailed-specifications)
9. [Dependencies](#-dependencies)
10. [@GTM Concerns — Addressed](#-gtm-concerns--addressed)
11. [Phases — Implementation Roadmap](#-phases--implementation-roadmap)
12. [Success Metrics](#-success-metrics)
13. [Version History](#-version-history)
14. [Related Documents](#-related-documents)
15. [Discovered By (BP-047)](#-discovered-by-bp-047)
16. [Governance Compliance](#-governance-compliance)

---

## 📋 Project Identity

| Field | Value |
|-------|-------|
| Project ID | **PRJ-023** |
| Title | **Context Persistence Pipeline** |
| Type | Infrastructure — Context Persistence + Memory |
| Priority | 🟠 P1 |
| Owner | @LDC (Lead) + @RMN (Infrastructure Support) |
| Original Owner | @RMN (handed off Thu Feb 27, W10) |
| Implementation | **mem0.ai** (Apache 2.0 FOSS, 25k+ GitHub stars) |
| Status | ✅ DECIDED (GTM_2026-W11_326) — 🔄 IMPLEMENTATION W12 |
| #masterCCC | GTM_2026-W10_026 |
| Approval CCC-ID | GTM_2026-W11_326 |

---

## 📋 Executive Summary

### What Is PRJ-023?

PRJ-023 addresses a critical pain point: **context loss between AnythingLLM sessions**. Currently, when a session ends or RAG is updated, all conversation history is lost unless manually preserved. This project builds an automated pipeline to export chat history, store it in PostgreSQL via mem0.ai, parse signal from noise, and feed it back into RAG for persistent cross-session memory.

### Key Decision — mem0.ai Adoption

| Decision | Detail |
|----------|--------|
| **Adopt mem0.ai** | Apache 2.0 FOSS, 25k+ GitHub stars |
| **Phase 0 Timeline** | **W12 (after LiteLLM deploys)** |
| **Build Effort** | **2-4h** (vs 14-26h custom) |
| **Deployment** | jAIMSnet DOKS cluster (ATL1), `memory` namespace |
| **Backend** | PGvector (db-postgresql-atl1-weownnet) |
| **Embedder** | Qwen3 Embedding 4B (via LiteLLM) |
| **Cost** | **$0 additional** (shared DOKS + shared PG) |

### The Problem — Context Loss

| Symptom | Current Behavior | Impact |
|---------|------------------|--------|
| **Session ends** | All chat history lost | Must re-seed context manually |
| **RAG updated** | Fresh session required (BP-034) | Previous conversation context lost |
| **Cross-instance work** | No shared memory | Each instance starts from zero |
| **Long projects** | Context exceeds token limit | Older decisions/constraints forgotten |
| **Manual checkpointing** | ~2+ hours per thread | 52% of CCC-IDs = seeding overhead |

### Real-World Impact (@RMN Experience)

| Scenario | Time Lost | Frequency |
|----------|:---------:|:---------:|
| Re-seeding MAIT threads after RAG update | 2-3 hours | Weekly |
| Re-explaining project context after session gap | 30-60 min | Per session |
| Lost decisions/constraints from earlier conversation | Variable | Every long session |
| Cross-instance context transfer (manual volleys) | 1-2 hours | Per major sync |
| **Total monthly overhead** | **~15-20 hours** | **Recurring** |

### The Solution — Automated Context Persistence with mem0

```
AnythingLLM Chat Session → mem0.ai → PostgreSQL ATL1 DB → AnythingLLM Workspace RAG
     │                        │                        │
     │  User chats            │  Chat history          │  Auto-fed back
     │  with agent            │  stored + parsed       │  as searchable
     │                        │  + CCC-IDs extracted   │  context
     └────────────────────────┴────────────────────────┘
                                      │
                                      ▼
                              cccid.info Registry (PRJ-028)
```

### Why This Matters

| Without PRJ-023 | With PRJ-023 (mem0) |
|-----------------|---------------------|
| Context lost between sessions | ✅ Persistent cross-session memory |
| Manual seeding (2+ hrs/thread) | ✅ Automatic |
| 52% of CCC-IDs = seeding overhead | ✅ Near-zero overhead |
| No cross-instance memory | ✅ Shared knowledge base |
| Chat history only in local SQLite | ✅ Centralized in PostgreSQL + mem0 |
| Knowledge dies with thread | ✅ Knowledge persists forever |
| Token limits constrain conversation length | ✅ mem0 decay + relevance extends effective context |
| Custom build 14-26h | ✅ mem0 2-4h with ALL advanced features |

---

## 📋 The Problem — Context Loss

### Current State Analysis

| Issue | Impact | Frequency |
|-------|--------|-----------|
| Session context reset on RAG update | Lost decisions, constraints, project context | Every RAG update |
| No cross-instance memory sharing | Each instance (INT-P01, INT-OG8, INT-P02) starts from zero | Per instance |
| Manual re-seeding required | 2+ hours per thread, 52% CCC-ID overhead | Every session |
| Token limits constrain length | Older context dropped when limit exceeded | Every long session |
| No decision/constraint tracking | Key decisions forgotten, re-discussed | Every multi-session project |

### Quantified Overhead

| Metric | Current | Target (with mem0) |
|--------|---------|-------------------|
| Manual seeding time | 15-20 hrs/month | <2 hrs/month |
| CCC-ID overhead | 52% seeding | <10% seeding |
| Session continuity | 0% (all lost) | 80%+ preserved |
| Cross-instance memory | None | Shared via mem0 |
| Decision recall | ~50% (manual) | ~90% (automated) |

---

## 📋 Project Handoff — @RMN to @LDC (W10)

### What @RMN Handed Off to @LDC

| # | Item | Detail |
|---|------|--------|
| 1 | **Task writeup** | Full description of pipeline architecture, steps, and goals |
| 2 | **n8n access** | Login credentials for n8n.weown.app |
| 3 | **PostgreSQL access** | Connection details for db-postgresql-atl1-weownnet |
| 4 | **API keys** | OpenRouter + AnythingLLM API keys for evaluation calls |
| 5 | **Connection guidance** | Which connection scenario applies (Academy → Labs = public + SSL) |
| 6 | **Target scope** | INT-P01, INT-P02, INT-OG8 — all three instances |
| 7 | **Architecture direction** | Export → Store → Parse → Transform → Embed → Automate |

### @LDC Guidance Given (RMN_2026-W10_029)

| Topic | Key Answers |
|-------|------------|
| **n8n specs (Q1)** | Single n8n on DOKS, cron 4x daily EST, 1800s timeout, single workflow |
| **PostgreSQL specs (Q2)** | PG v18, $15 plan, 7-11 connections, GUIDE-010 reference |
| **Embedding specs (Q3)** | Qwen3 4B, Option A (direct RAG) first, test Option B (PGvector) |
| **Chunking strategy (Q4)** | Per conversation turn, skip noise, table per instance |

### @RMN Time Investment (Handoff Only)

| Metric | Value |
|--------|-------|
| **Hours** | 2h (writeup, n8n/PG access, API keys, connection guidance) |
| **CCC-ID** | RMN_2026-W10_029 (guidance volley) |
| **Status** | ✅ Complete — awaiting @LDC progress |

---

## 📋 Solution — mem0.ai Adoption

### What Is mem0?

| Field | Value |
|-------|-------|
| Product | mem0 (formerly EmbedChain) |
| URL | https://mem0.ai |
| GitHub | 25k+ stars |
| License | **Apache 2.0** ✅ (Priority #2 FOSS) |
| Language | Python |
| Purpose | Memory layer for AI agents — persistent, cross-session, cross-agent memory |
| Tagline | "The Memory Layer for Personalized AI" |

### What mem0 Does

```
WITHOUT mem0:
  Session 1: "I prefer tables over paragraphs" → Agent knows
  Session 2: "I prefer tables over paragraphs" → Agent forgot. Tell again.
  Session 3: "I prefer tables over paragraphs" → Agent forgot. Tell again.

WITH mem0:
  Session 1: "I prefer tables over paragraphs" → mem0 stores
  Session 2: Agent already knows → retrieves from mem0
  Session 3: Agent already knows → retrieves from mem0
  Forever: Agent always knows
```

### Core Features

| Feature | Detail |
|---------|--------|
| **Add memories** | `m.add("User prefers tables", user_id="GTM")` |
| **Search memories** | `m.search("formatting preference", user_id="GTM")` |
| **Get all memories** | `m.get_all(user_id="GTM")` |
| **Memory types** | User, Agent, Session, Cross-agent |
| **Conflict resolution** | Detects contradictions, keeps latest |
| **Decay/relevance** | Older memories decay, frequently accessed persist |
| **Graph memory** | Neo4j-backed relationship graphs (optional) |
| **PGvector backend** | ✅ Supported (our chosen backend) |

### mem0 Architecture

```
┌─────────────────────────────────────────┐
│  Application (AnythingLLM / n8n)        │
│                                         │
│  mem0.add("context")                    │
│  mem0.search("query")                   │
└───────────┬─────────────────────────────┘
            │
┌───────────▼─────────────────────────────┐
│  mem0 Core                              │
│  ├── Memory Manager (add/update/delete) │
│  ├── Embedding (Qwen3 4B via LiteLLM)   │
│  ├── Vector Search (similarity)         │
│  ├── Conflict Resolution               │
│  └── Decay/Relevance Scoring           │
└───────────┬─────────────────────────────┘
            │
┌───────────▼─────────────────────────────┐
│  Storage Backend                        │
│  └── PostgreSQL + PGvector ✅           │
│      (db-postgresql-atl1-weownnet)      │
└─────────────────────────────────────────┘
```

### mem0 vs PRJ-023 Custom Build

| Feature | PRJ-023 Custom | **mem0** | Winner |
|---------|:--------------:|:-------:|:------:|
| FOSS | ✅ (custom code) | ✅ Apache 2.0 | Tie |
| Build effort | 14-26h | **2-4h** | **mem0** |
| Maintenance | High (custom) | **Low (community)** | **mem0** |
| Features | Basic → Advanced | **Advanced from day 1** | **mem0** |
| PGvector support | ✅ (Phase 2) | ✅ **Native** | **mem0** |
| Our PG cluster | ✅ | ✅ | Tie |
| Conflict resolution | ❌ Build it | ✅ **Built-in** | **mem0** |
| Memory decay | ❌ Build it | ✅ **Built-in** | **mem0** |
| Cross-agent | ❌ Build it | ✅ **Built-in** | **mem0** |
| Graph memory | ❌ | ✅ **Optional** | **mem0** |
| Community | 0 (internal) | **25k+ stars** | **mem0** |
| Python SDK | N/A | ✅ **pip install mem0ai** | **mem0** |
| **Total** | 3/12 | **10/12** | **mem0** |

### Why mem0 Wins

> **mem0 IS PRJ-023 Advanced Options (A-D) — already built, tested, and maintained by a community of 25k+ stars.**

| PRJ-023 Approach | mem0 Equivalent |
|-----------------|-----------------|
| Option A (Long-Term Memory) | ✅ mem0 core feature |
| Option B (Memory Buffering) | ✅ mem0 structured memories |
| Option C (Hierarchical Summarization) | ✅ mem0 decay + relevance |
| Option D (Hybrid) | ✅ mem0 = the hybrid |
| Custom n8n pipeline | ✅ mem0 Python SDK + API |
| Custom PGvector schemas | ✅ mem0 PGvector backend |

### Deployment Configuration

| Field | Value |
|-------|-------|
| **Where** | jAIMSnet DOKS cluster (ATL1) |
| **Namespace** | `memory` (new) |
| **Image** | `mem0ai/mem0:latest` |
| **Backend** | PGvector (db-postgresql-atl1-weownnet) |
| **Embedder** | Qwen3 Embedding 4B (via LiteLLM) |
| **Cost** | **$0 additional** (shared DOKS + shared PG) |

### Per-User Memory

| User | mem0 user_id | Memories |
|------|-------------|----------|
| @GTM | `GTM` | Preferences, decisions, project context |
| @RMN | `RMN` | Infrastructure decisions, deployment patterns |
| @LDC | `LDC` | Code patterns, architecture decisions |
| @THY | `THY` | Financial approvals, budget constraints |
| @CEO | `CEO` | Business strategy, partnership context |

### Cross-Agent Memory

| Memory Type | Example |
|-------------|---------|
| **User** | "@GTM prefers tables over paragraphs" |
| **Agent** | "#MetaAgent knows R-204 was amended in W11" |
| **Session** | "W11 Day 4 call: @RMN SOW approved with reorder" |
| **Project** | "PRJ-016 deploys on DOKS ATL1" |

---

## 📋 Pipeline Architecture — Baseline (6 Steps)

### Step 1: Export

| Field | Value |
|-------|-------|
| **Source** | AnythingLLM chat history |
| **Method** | REST API or direct DB access (SQLite) |
| **Format** | JSON (native AnythingLLM export) |
| **Frequency** | Per session end OR scheduled (4x daily) |
| **Target Instances** | INT-P01, INT-P02, INT-OG8 |

### Step 2: Store (mem0)

| Field | Value |
|-------|-------|
| **Destination** | mem0.ai → PostgreSQL (db-postgresql-atl1-weownnet) |
| **Schema** | `mem0` + `context_persistence` (new schemas in POP DB cluster) |
| **Tables** | mem0-managed tables + `raw_chats`, `instances`, `sessions`, `messages` |
| **Retention** | Indefinite (append-only, with decay/relevance scoring) |

### Step 3: Parse

| Field | Value |
|-------|-------|
| **Purpose** | Filter noise from signal |
| **Signal Types** | Decisions, rules, project updates, learnings, constraints, action items, CCC-IDs |
| **Noise Types** | Greetings, acknowledgments, redundant restatements, failed queries |
| **Method** | LLM classification (Qwen3.5-397B or routed alias) + mem0 automatic |
| **Output** | Structured JSON with metadata (type, confidence, tags) + mem0 memories |

### Step 4: Transform

| Field | Value |
|-------|-------|
| **Purpose** | Convert parsed data into RAG-ready documents |
| **Format** | Markdown (compatible with AnythingLLM RAG) |
| **Structure** | Header (metadata) + Body (content) + Footer (attribution) |
| **Grouping** | By project, by contributor, by topic, by date |

### Step 5: Embed

| Field | Value |
|-------|-------|
| **Destination** | mem0 (PGvector backend) + AnythingLLM workspace RAG |
| **Method** | mem0.add() + Option A: Direct upload via API |
| **Embedding Model** | Qwen3 Embedding 4B (via LiteLLM) |
| **Frequency** | After each parse/transform cycle |

### Step 6: Automate

| Field | Value |
|-------|-------|
| **Orchestrator** | n8n workflow (shared with PRJ-028) |
| **Schedule** | Cron: `0 */6 * * *` (4x daily EST) |
| **Trigger** | Session end OR scheduled OR manual |
| **Error Handling** | Retry logic, error logging, alerting |
| **Dual Output** | mem0.add() (context) + cccid.info POST (CCC-IDs) |

---

## 📋 PRJ-028 Interweave — Shared Pipeline

### The Connection

| PRJ-023 | PRJ-028 | Overlap |
|---------|---------|---------|
| Store chat history in PostgreSQL | Store CCC-IDs in PostgreSQL | **Same PG cluster** |
| Parse signal from noise | Validate CCC-ID sequences | **Both parse structured data** |
| n8n automation | FastAPI automation | **Both automate data flows** |
| Track what was SAID | Track what was CREATED | **Together = full audit trail** |

### How They Interweave

```
CURRENT (Separate):
  PRJ-023: Chat → mem0 → RAG (context memory)
  PRJ-028: CCC-ID → FastAPI → cccid.info (sequence integrity)

INTERWEAVED:
  Chat Session → n8n Pipeline
    ├── Extract CCC-IDs → PRJ-028 registry (cccid.info)
    ├── Extract decisions/constraints → PRJ-023 mem0 memory
    ├── Extract action items → PRJ-023 mem0 memory
    └── Store raw chat → PRJ-023 archive
```

| Benefit | Detail |
|---------|--------|
| **Single pipeline** | One n8n workflow extracts BOTH CCC-IDs AND context |
| **CCC-ID auto-registration** | No manual POST to cccid.info — pipeline does it |
| **Decision-to-CCC-ID linking** | "Decision X was made at CCC-ID Y" — traceable |
| **Shared PG cluster** | Both use db-postgresql-atl1-weownnet — zero additional infra |

### Recommendation

| Decision | Detail |
|----------|--------|
| **Keep PRJ-023 and PRJ-028 as separate PRJs** | Different owners, different timelines |
| **Share the pipeline** | One n8n workflow, two output streams |
| **Phase 0 of PRJ-023 includes CCC-ID extraction** | @RMN adds cccid.info POST to pipeline |

> **Don't merge the PRJs. Merge the pipeline.** PRJ-028 = the registry API. PRJ-023 = the memory system. The n8n workflow feeds both.

---

## 📋 Infrastructure — Detailed Specifications

### n8n Configuration

| Field | Value |
|-------|-------|
| **Instance** | n8n.weown.app (DOKS, ATL1, We Own Academy) |
| **Workflow Count** | 1 (shared context persistence + CCC-ID registry) |
| **Nodes** | ~20 (HTTP Request, Code, PostgreSQL, mem0 API, AnythingLLM API, cccid.info POST, Error Handling) |
| **Schedule** | Cron: `0 */6 * * *` (4x daily EST) |
| **Timeout** | 1800s (30 minutes) |
| **Error Handling** | try/catch + ignoreHttpStatusErrors + alerting |

### mem0 Configuration

| Field | Value |
|-------|-------|
| **Deployment** | jAIMSnet DOKS cluster (ATL1) |
| **Namespace** | `memory` |
| **Image** | `mem0ai/mem0:latest` |
| **Backend** | PostgreSQL + PGvector (db-postgresql-atl1-weownnet) |
| **Embedder** | Qwen3 Embedding 4B (via LiteLLM) |
| **Cost** | $0 additional (shared DOKS + shared PG) |

### PostgreSQL Configuration

| Field | Value |
|-------|-------|
| **Cluster** | db-postgresql-atl1-weownnet (PRJ-021) |
| **Engine** | PostgreSQL v18 |
| **Extension** | PGvector (for mem0 semantic search) |
| **Schema** | `mem0` + `context_persistence` + `cccid_registry` (new) |
| **Connection** | Public + Trusted Sources + SSL (Academy→Labs) |
| **Port** | 25060 (SSL), 25061 (pool — when created) |

### AnythingLLM API

| Field | Value |
|-------|-------|
| **API Endpoint** | `https://<instance>/api/v1/workspace/<id>/documents` |
| **Auth** | API key (per instance) |
| **Method** | POST (upload), GET (list), DELETE (remove) |
| **Rate Limits** | Instance-dependent (configure in n8n) |

### Connection Scenarios (GUIDE-010)

| From | To | Method | Cost | Latency |
|------|----|--------|------|---------|
| n8n (Academy) | PostgreSQL (Labs) | Public + Trusted Sources + SSL | $0.01/GiB | 2-5ms |
| mem0 (DOKS) | PostgreSQL (Labs) | VPC Private IP | FREE | <1ms |
| INT-P01 (Labs) | PostgreSQL (Labs) | VPC Private IP | FREE | <1ms |
| INT-P02 (Academy) | PostgreSQL (Labs) | Public + Trusted Sources + SSL | $0.01/GiB | 2-5ms |
| INT-OG8 (Academy) | PostgreSQL (Labs) | Public + Trusted Sources + SSL | $0.01/GiB | 2-5ms |

### jAIMSnet Namespace Map — Updated

```
jaimsnet-cluster (ATL1, DOKS)
├── gateway/        → LiteLLM, Redis
├── observability/  → Langfuse, pgAdmin, Prometheus, Grafana, Loki
├── secrets/        → Infisical Operator
├── automation/     → Semaphore UI, n8n
├── memory/         → mem0 ← NEW (PRJ-023)
└── gpu/            → vLLM (Phase 2, MI300X)
```

---

## 📋 Dependencies

| Dependency | PRJ | Status | Blocks |
|------------|-----|--------|--------|
| **PostgreSQL Trusted Sources** | PRJ-021 | ⬜ TODO | PRJ-023 (cannot connect from n8n) |
| **PostgreSQL Connection Pool** | PRJ-021 | ⬜ TODO | PRJ-023 (needed at 3+ consumers) |
| **PGvector Extension** | PRJ-021 | ⬜ TODO | PRJ-023 (mem0 semantic search) |
| **LiteLLM Deployment** | PRJ-016 | 🔄 Deploying W11 | PRJ-023 (mem0 embedder via LiteLLM) |
| **AnythingLLM API Access** | — | ✅ Available | — |
| **n8n Access** | — | ✅ Available | — |
| **PRJ-028 CCC-ID Registry API** | PRJ-028 | ⬜ TBD | Shared pipeline integration |

---

## 📋 @GTM Concerns — Addressed

### Concern 1: "Not Necessary Yet"

| @GTM View | @RMN Counter | Resolution |
|-----------|--------------|------------|
| Current manual workflow works | ✅ Works but scales poorly — 15-20 hrs/month overhead | ✅ **mem0 reduces to <2 hrs/month** |
| Only 3 active instances now | ✅ Will be 10+ instances by W22 — manual doesn't scale | ✅ **mem0 scales automatically** |
| Contributors can re-seed manually | ✅ Can, but 52% CCC-ID overhead is unsustainable | ✅ **mem0 = near-zero overhead** |
| Priority is cost reduction (PRJ-016) | ✅ Agreed — but context loss affects productivity NOW | ✅ **After LiteLLM (P0), mem0 is P1** |

### Concern 2: "Complexity Overhead"

| @GTM View | @RMN Counter | Resolution |
|-----------|--------------|------------|
| Another system to maintain | ✅ True — but n8n + PG already exist (sunk cost) | ✅ **mem0 = maintained by 25k+ community** |
| LDC could be doing other work | ✅ Valid — but @RMN can lead infrastructure, @LDC focuses on agentic layer | ✅ **mem0 = 2-4h vs 14-26h custom** |
| Can defer until after LiteLLM | ✅ Partial agree — baseline pipeline first, advanced memory later | ✅ **W12 deployment (after LiteLLM W11)** |

### Concern 3: "Value Not Clear"

| @GTM View | @RMN Counter | Resolution |
|-----------|--------------|------------|
| Hard to measure ROI | ✅ Can measure: hours saved, CCC-ID overhead reduction, session continuity | ✅ **Success metrics defined** |
| Benefits are indirect | ✅ True — but indirect benefits compound (better decisions, less rework) | ✅ **15-20 hrs/month → <2 hrs/month** |
| Not customer-facing | ✅ True — but internal productivity enables customer delivery | ✅ **Productivity = capacity for customer work** |

### Final Decision (GTM_2026-W11_326)

| Decision | Detail |
|----------|--------|
| **Adopt mem0.ai** | Apache 2.0 FOSS, 25k+ GitHub stars |
| **Phase 0 Timeline** | **W12 (after LiteLLM deploys)** |
| **Build Effort** | **2-4h** (vs 14-26h custom) |
| **Priority** | **🟠 P1 (after LiteLLM P0)** |
| **Shared Pipeline** | **One n8n workflow feeds both mem0 + cccid.info** |

> **📋 This is the right call.** mem0 has ALL the advanced memory features built-in. We get Phase 0+2 capabilities for Phase 0 effort.

---

## 📋 Phases — Implementation Roadmap

### Phase 0: mem0 Deploy + Shared Pipeline (W12)

| # | Task | Owner | Est. Hours | Status |
|---|------|-------|:----------:|--------|
| 1 | Deploy mem0 on jAIMSnet DOKS (`memory` namespace) | @RMN | 2h | ⬜ TODO |
| 2 | Configure PGvector backend (db-postgresql-atl1-weownnet) | @RMN | 0.5h | ⬜ TODO |
| 3 | Configure Qwen3 Embedding 4B via LiteLLM | @RMN | 0.5h | ⬜ TODO |
| 4 | Build shared n8n pipeline (mem0.add() + cccid.info POST) | @RMN + @LDC | 3h | ⬜ TODO |
| 5 | Test end-to-end (INT-OG8 first) | @RMN | 1h | ⬜ TODO |
| **TOTAL** | | | **7h** | |

### Phase 1: Measurement (W13)

| # | Task | Owner | Est. Hours | Status |
|---|------|-------|:----------:|--------|
| 1 | Track manual seeding time (before) | @RMN | 0.5h/week | ⬜ TODO |
| 2 | Track auto-pipeline time (after) | @RMN | 0.5h/week | ⬜ TODO |
| 3 | Calculate CCC-ID overhead reduction | @RMN | 0.5h/week | ⬜ TODO |
| 4 | Weekly report to @GTM | @RMN | 0.5h/week | ⬜ TODO |
| **TOTAL** | | | **2h/week** | |

### Phase 2: Advanced Memory (W14+ — If ROI Positive)

| # | Task | Owner | Est. Hours | Status |
|---|------|-------|:----------:|--------|
| 1 | Graph memory (Neo4j optional backend) | @LDC | 2h | ⬜ TBD |
| 2 | Cross-instance sync (INT-P01 ↔ INT-OG8 ↔ INT-P02) | @LDC | 2h | ⬜ TBD |
| 3 | Advanced mem0 configurations (decay rates, relevance scoring) | @LDC | 2h | ⬜ TBD |
| 4 | AnythingLLM middleware layer (if needed beyond mem0) | @LDC | 3h | ⬜ TBD |
| **TOTAL** | | | **9h** | |

---

## 📋 Success Metrics

| Metric | Baseline (Before) | Target (After) | Measurement |
|--------|------------------|----------------|-------------|
| **Manual seeding time** | 15-20 hrs/month | <2 hrs/month | Time tracking |
| **CCC-ID overhead** | 52% seeding | <10% seeding | CCC-ID analysis |
| **Session continuity** | 0% (all lost) | 80%+ preserved | User survey |
| **Cross-instance memory** | None | Shared via mem0 | Functional test |
| **Token efficiency** | 100% verbatim | 60-80% with mem0 decay | Token count analysis |
| **Decision recall** | ~50% (manual) | ~90% (automated) | Spot checks |
| **Build effort** | 14-26h (custom) | **2-4h (mem0)** | Actual hours |
| **Maintenance** | High (custom) | **Low (community)** | Ongoing hours |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| **3.2.3.1** | **2026-W12** | **GTM_2026-W10_026** | **GTM_2026-W11_326** | **Initial document creation — PRJ-023 Context Persistence Pipeline. Problem statement (context loss, 15-20 hrs/month overhead). mem0.ai adoption (Apache 2.0 FOSS, 25k+ stars, 2-4h deploy vs 14-26h custom). Baseline pipeline (6 steps: Export → Store → Parse → Transform → Embed → Automate). PRJ-028 interweave (shared n8n pipeline feeds both mem0 + cccid.info). Infrastructure specs (jAIMSnet DOKS `memory` namespace, PGvector backend, Qwen3 Embedding 4B via LiteLLM). @GTM concerns addressed (not necessary yet, complexity overhead, value not clear). Implementation phases (Phase 0: mem0 deploy + shared pipeline W12, Phase 1: measurement W13, Phase 2: advanced memory W14+). Success metrics (15-20 hrs/month → <2 hrs/month, 52% → <10% CCC-ID overhead). Dependencies (PRJ-021 Trusted Sources/PGvector, PRJ-016 LiteLLM, PRJ-028 CCC-ID registry)** |

---

## 📋 Related Documents

| Document | Version | #masterCCC | Approval | Location |
|----------|---------|------------|----------|----------|
| PRJ-018_POP-Database.md | 3.2.3.1 | GTM_2026-W10_026 | GTM_2026-W11_308 | _PROJECTS_/ |
| PRJ-021_PostgreSQL-Operations.md | 3.2.3.1 | GTM_2026-W10_026 | GTM_2026-W10_026 | _PROJECTS_/ |
| PRJ-028_CCC-ID-Registry.md | TBD | GTM_2026-W10_026 | ⬜ AWAITING | _PROJECTS_/ |
| GUIDE-010_PostgreSQL-Setup.md | 3.2.1.1 | GTM_2026-W10_026 | GTM_2026-W10_073 | _GUIDES_/ |
| GUIDE-011_Governance-Oversight-VSA-Process.md | 3.2.1.1 | GTM_2026-W10_066 | GTM_2026-W10_073 | _GUIDES_/ |
| mem0.ai Documentation | — | — | Apache 2.0 | https://mem0.ai |

---

## 📋 Discovered By (BP-047)

| CCC | Contributor | Role | Context |
|-----|-------------|------|---------|
| RMN | Roman Di Domizio | AI Platform Engineer | Conceived PRJ-023 (W10), built baseline architecture, handed off to @LDC (2h investment), continues to advocate for context persistence due to ongoing context loss problems, mem0.ai discovery and evaluation |
| LDC | Dhruv | Agentic AI Engineer | Current lead — researching AnythingLLM API, building pipeline (W10-W11), exploring advanced memory architectures, mem0 integration |
| GTM | Jason Younker | Co-Founder | Approved PRJ assignment (GTM_2026-W10_026), expressed skepticism about value/necessity (work on hold pending decision), approved mem0 adoption (GTM_2026-W11_326), PRJ-028 interweave decision |
| #MetaAgent | INT-P01:tools | AI Reviewer | mem0.ai #DeepDive evaluation (10/12 score), PRJ-023 + PRJ-028 interweave recommendation |

---

## 📋 Governance Compliance

| Requirement | Status |
|-------------|--------|
| #masterCCC | ✅ GTM_2026-W10_026 |
| Approval CCC-ID | ✅ GTM_2026-W11_326 |
| Version History | ✅ Included |
| Related Documents | ✅ Included |
| Discovered By (BP-047) | ✅ Included |
| Lifecycle Stage | ✅ DECIDED — 🔄 IMPLEMENTATION W12 |
| VSA Eligibility | ✅ FULL or DEEP FULL (at APPROVED+ stage) |
| GUIDE-011 | ✅ APPROVED — compensation eligible |

---

#FlowsBros #FedArch #PRJ-023 #mem0 #PRJ-028 #ContextPersistence #jAIMSnet #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
