# PRJ-013: Paperless-ngx — Document Management Hub

## 📋 PRJ-013_Paperless-ngx_v3.2.3.1.md
## ♾️ WeOwnNet 🌐

| Field | Value |
|-------|-------|
| Document | PRJ-013_Paperless-ngx.md |
| Version | **3.2.3.1** (REGENERATED W12) |
| Folder | `_PROJECTS_/` ✅ |
| Category | PROJECT:Document Management |
| Type | Document Management + AnythingLLM Data Connector |
| CCC-ID | GTM_2026-W09_065 |
| Regeneration CCC-ID | GTM_2026-W12_302 |
| **Approval CCC-ID** | **GTM_2026-W12_304** |
| Created | 2026-02-27 (W09) |
| Regenerated | 2026-03-18 (W12 Day 3) |
| Season | #WeOwnSeason003 🚀 |
| Lifecycle Stage | ✅ 🔒 APPROVED + 🚀 GH LIVE (D-062)** |
| **#LLMmodel** | **Qwen3.5-397B-A17B (INT-OG1:CCC @GTM)** |
| **#LLMmodel** | **Claude Opus 4.6 (INT-P01:tools #MetaAgent)** |
| Tags | #Paperless #DocumentManagement #FOSS #FlowsBros |

---

## 📖 Table of Contents

1. [Project Identity](#-project-identity)
2. [What Is Paperless-ngx](#-what-is-paperless-ngx)
3. [Why Paperless-ngx](#-why-paperless-ngx)
4. [Use Cases](#-use-cases)
5. [#WeeklySummary Workflow](#-weeklysummary-workflow)
6. [AnythingLLM Native Connector](#-anythingllm-native-connector)
7. [Infrastructure](#-infrastructure)
8. [Integration with #FedArch](#-integration-with-fedarch)
9. [Project Team](#-project-team)
10. [Deployment Scope (W10-W12)](#-deployment-scope-w10-w12)
11. [Risk Matrix](#-risk-matrix)
12. [Related Projects](#-related-projects)
13. [Discovered By](#-discovered-by)
14. [Related Documents](#-related-documents)
15. [Version History](#-version-history)

---

## 📋 Project Identity

| Field | Value |
|-------|-------|
| Project ID | **PRJ-013** |
| Title | **Paperless-ngx — Document Management Hub** |
| Type | Infrastructure — Document Management |
| Priority | 🔴 P0 |
| Owner | @GTM |
| Domain | docs.weown.net |
| #masterCCC | GTM_2026-W09_065 |
| Key Discovery | AnythingLLM v1.9.1+ has **NATIVE** Paperless-ngx Data Connector |

---

## 📋 What Is Paperless-ngx

| Field | Value |
|-------|-------|
| Tool | [Paperless-ngx](https://docs.paperless-ngx.com/) |
| License | GPL-3.0 (**FOSS** ✅) |
| Type | Self-hosted document management system |
| Language | Python (Django) |
| Database | PostgreSQL |
| Search | Full-text search (Elasticsearch or SQLite) |
| OCR | Built-in (Tesseract) |
| API | RESTful API (full CRUD) |
| Docker | ✅ Official Docker Compose |
| Mobile | ✅ Progressive Web App (PWA) |

### Key Features

| Feature | Value for ♾️ WeOwnNet 🌐 |
|---------|--------------------------|
| **Document ingestion** | Upload, email, API — multiple input methods |
| **Auto-tagging** | AI-powered classification + custom tags |
| **Full-text search** | Search across ALL documents |
| **REST API** | Programmatic access (used by AnythingLLM native connector) |
| **User management** | Multi-user with permissions |
| **Correspondent tracking** | Map to CCC contributors |
| **Custom metadata** | CCC-ID, season, week, project |
| **Self-hosted** | Data sovereignty — FOSS priority #3 |
| **OCR** | Scan physical documents (receipts, contracts) |
| **Email ingestion** | Send docs via email — auto-processed |

---

## 📋 Why Paperless-ngx

### The Problem

| Issue | Current State |
|-------|--------------|
| #WeeklySummary workflow | ❌ 15-20 min, requires ADMIN, manual RAG upload |
| Session notes (R-199) | ❌ RAG-only, no central archive |
| Contributor self-service | ❌ Non-technical contributors need ADMIN help |
| Document search | ❌ GH search only — no full-text across RAG |
| Scalability | ❌ 9 contributors × manual workflow = bottleneck |

### The Solution

| Solution | How |
|----------|-----|
| **Self-service ingestion** | Web UI, email, mobile — no ADMIN needed |
| **Native AnythingLLM connector** | Auto-sync to RAG — zero custom code |
| **CCC attribution** | Correspondent = CCC contributor |
| **Full-text search** | Search across ALL ecosystem documents |
| **FOSS + self-hosted** | Data sovereignty maintained |

### Decision Matrix — Why Not Alternatives

| Alternative | Why Not |
|-------------|---------|
| Google Drive | ❌ Not FOSS, not self-hosted |
| Notion | ❌ Not FOSS, not self-hosted |
| SharePoint | ❌ Not FOSS, Microsoft dependency |
| DrupalWiki (PRJ-005) | 🟡 Wiki ≠ document management; different use case |
| GH `_WEEKLY_/` only | 🟡 Works for text, no email ingestion, no OCR, public repo |
| **Paperless-ngx** | ✅ FOSS, self-hosted, email ingestion, OCR, native AnythingLLM connector |

---

## 📋 Use Cases

### Primary Use Cases

| # | Use Case | Description | Priority |
|---|----------|-------------|----------|
| 1 | **#WeeklySummary ingestion** | Contributors upload/email weekly summaries → auto-tagged → native connector syncs to AnythingLLM RAG | 🔴 P0 |
| 2 | **Session notes archive** | R-199 session notes stored privately (not GH) → searchable archive | 🟠 P1 |
| 3 | **Contributor self-service** | Non-technical contributors (@THY, @LFG, @CEO) upload via web or email — no GH/ADMIN required | 🟠 P1 |
| 4 | **Document search** | Full-text search across ALL ecosystem documents | 🟠 P1 |

### Secondary Use Cases

| # | Use Case | Description | Priority |
|---|----------|-------------|----------|
| 5 | **Meeting recordings transcripts** | Upload call transcripts → auto-tagged by project + contributor | 🟡 P2 |
| 6 | **Financial documents** | Receipts, invoices, contracts for 🔥 Burned Out Media 🔀 | 🟡 P2 |
| 7 | **Legal / compliance** | Agreements, NDAs, partnership docs | 🟡 P2 |
| 8 | **Knowledge base** | Long-term institutional memory beyond AnythingLLM sessions | 🟡 P2 |

---

## 📋 #WeeklySummary Workflow

### Current Workflow (PAIN)

```
Contributor → Generate in CCC → Export .md → Ask ADMIN →
ADMIN uploads to RAG (_WEEKLY_/) → ADMIN syncs ALL instances →
Fresh session → Verify

⏱️ ~15-20 min per contributor
👤 Requires ADMIN
📦 Copies across instances
❌ Does NOT scale
```

### New Workflow (Paperless-ngx)

```
Contributor → Generate in CCC → Choose ingestion method:
    │
    ├── 📧 Email to summaries@weown.net (EASIEST)
    ├── 🌐 Upload via Paperless web UI
    └── 📱 Upload via Paperless mobile PWA
    │
    ▼
Paperless-ngx auto-processes:
    ├── Auto-tag: #WeeklySummary + <CCC> + <YYYY>-W<WW>
    ├── Assign correspondent: <CCC contributor>
    ├── OCR (if scanned/image)
    └── Index for full-text search
    │
    ▼
AnythingLLM Native Data Connector (v1.9.1+):
    ├── Polls Paperless API automatically
    ├── Syncs new documents to RAG
    └── Available across ALL workspaces
    │
    ▼
✅ Available in AnythingLLM — ZERO manual steps

⏱️ ~2-3 min per contributor
👤 ZERO ADMIN dependency
📦 Single source of truth (Paperless)
✅ Scales to 9, 20, 100 contributors
```

### Workflow Comparison

| Metric | Current | Paperless-ngx |
|--------|---------|---------------|
| Time per contributor | 15-20 min | **2-3 min** |
| ADMIN required | ✅ Every time | **❌ Never** |
| Technical skill | GH + RAG upload | **Email** |
| Scalability | ❌ Bottleneck at 9 | ✅ **Unlimited** |
| Search | GH search only | ✅ **Full-text** |
| RAG sync | Manual per instance | ✅ **Automatic (native connector)** |
| Data sovereignty | GH (public) | ✅ **Self-hosted (private)** |

---

## 📋 AnythingLLM Native Connector

### Discovery

| Field | Value |
|-------|-------|
| Feature | Paperless-ngx Data Connector |
| Introduced | **AnythingLLM v1.9.1** |
| Source | [docs.anythingllm.com/changelog/v1.9.1](https://docs.anythingllm.com/changelog/v1.9.1) |
| Type | Native — built into AnythingLLM |
| Custom code needed | **ZERO** |

### How It Works

```
Paperless-ngx                    AnythingLLM
┌──────────────┐                ┌──────────────────┐
│  Documents   │  REST API      │  Data Connectors  │
│  stored +    │ ──────────────►│  → Paperless-ngx  │
│  tagged +    │  Auth token    │  → Pulls documents │
│  indexed     │                │  → Embeds to RAG   │
└──────────────┘                └──────────────────┘

Configuration:
  AnythingLLM → Settings → Data Connectors → Paperless-ngx
  → Enter: API URL + Auth Token
  → Select: Tags/folders to sync
  → Done ✅
```

### Configuration Requirements

| Field | Value |
|-------|-------|
| Paperless API URL | `https://<domain>/api/` |
| Auth Token | Generated in Paperless admin |
| Sync scope | By tag, correspondent, or document type |
| Refresh | Configurable polling interval |

### What This Eliminates

| Eliminated | Was | Now |
|-----------|-----|-----|
| Custom Python connector | @LDC / @RMN build (4+ weeks) | ❌ **NOT NEEDED** |
| Zapier/n8n integration | Alternative to custom build | ❌ **NOT NEEDED** |
| Manual RAG upload | ADMIN workflow | ❌ **NOT NEEDED** |
| Phase 2 (W13+) | Separate development phase | ❌ **MERGED into Phase 1** |

### Version Check Required

| Instance | AnythingLLM v1.9.1+ | Status |
|----------|---------------------|--------|
| INT-P01 | ⬜ Verify | ⬜ CHECK (@RMN) |
| INT-OG1 | ⬜ Verify | ⬜ CHECK (@RMN) |
| INT-OG8 | ⬜ Verify | ⬜ CHECK (@RMN) |
| INT-P02 | ⬜ Verify | ⬜ CHECK (@RMN) |

---

## 📋 Infrastructure

### Recommended Deployment

| Field | Value |
|-------|-------|
| Platform | DigitalOcean Droplet |
| Plan | Basic Premium AMD |
| CPU | 1 vCPU |
| RAM | 2 GB |
| Storage | 50 GB (NVMe) |
| Datacenter | **ATL1** |
| Cost | **$18/mo** |
| Deployment | Docker Compose |
| Database | PostgreSQL (internal via Docker) |
| Domain | ⬜ TBD (e.g., docs.weown.net) |

### Architecture

```
┌─────────────────────────────────────────────────────────────┐
│  DigitalOcean — ATL1                                         │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  Droplet: Paperless-ngx ($18/mo)                       │ │
│  │                                                         │ │
│  │  ┌──────────────┐  ┌────────────┐  ┌───────────────┐  │ │
│  │  │  Paperless    │  │  PostgreSQL │  │  Redis        │  │ │
│  │  │  (Django)     │  │  (internal) │  │  (task queue) │  │ │
│  │  │  Port: 8000   │  │  Port: 5432 │  │  Port: 6379   │  │ │
│  │  └──────┬───────┘  └────────────┘  └───────────────┘  │ │
│  │         │                                               │ │
│  │  ┌──────┴───────┐                                      │ │
│  │  │  Gotenberg    │  (optional — PDF conversion)        │ │
│  │  └──────────────┘                                      │ │
│  └────────────────────────────────────────────────────────┘ │
│         │                                                    │
│         │ REST API (native connector)                        │
│         ▼                                                    │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  AnythingLLM Instances                                  │ │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐  │ │
│  │  │ INT-P01  │ │ INT-OG1  │ │ INT-OG8  │ │ INT-P02  │  │ │
│  │  │ Native   │ │ Native   │ │ Native   │ │ Native   │  │ │
│  │  │ Connector│ │ Connector│ │ Connector│ │ Connector│  │ │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘  │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  Email Ingestion                                        │ │
│  │  summaries@weown.net → Paperless SMTP inbound          │ │
│  └────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

### Cost Summary

| Item | Monthly |
|------|---------|
| Paperless Droplet (1 vCPU / 2 GB / 50 GB) | **$18** |
| Domain (if new) | ~$1 |
| **TOTAL** | **~$19/mo** |

---

## 📋 Integration with #FedArch

### Native Connector Integration

| Integration Point | Method | Effort |
|-------------------|--------|--------|
| **Paperless → AnythingLLM RAG** | ✅ **NATIVE** Data Connector (v1.9.1+) | **Configuration only** |
| **Tag mapping** | Paperless tags → connector filter | Low |
| **CCC attribution** | Paperless correspondent → CCC | Low |
| **Multi-instance** | Configure connector on EACH instance | Low (repeat config) |

### Tag Schema

| Tag | Maps To | Example |
|-----|---------|---------|
| `weekly-summary` | #WeeklySummary | WEEKLY-SUMMARY_GTM_2026-W09_001 |
| `session-notes` | R-199 docs | SESSION-SUMMARY_GTM_... |
| `project-<prj>` | Project docs | project-012 |
| `<ccc>` | Contributor | gtm, thy, lfg, etc. |
| `<yyyy>-w<ww>` | ISO week | 2026-w09 |
| `season-003` | Season | #WeOwnSeason003 |

### Correspondent → CCC Mapping

| Paperless Correspondent | CCC | Contributor |
|------------------------|-----|-------------|
| yonks | GTM | Jason Younker |
| mrsyonks | THY | Tyler Younker |
| CoachLFG | LFG | Mike LeMaire |
| Stephanie Warlick | CEO | Stephanie Warlick |
| Roman | RMN | Roman Di Domizio |
| IamLotus | IAL | IamLotus |
| Webb | CRO | Jason Webb |
| Dhruv | LDC | Dhruv |
| Shahid | SHD | Shahid |

### Connector Configuration (Per Instance)

| # | Step | Action |
|---|------|--------|
| 1 | Navigate | AnythingLLM → Settings → Data Connectors |
| 2 | Select | Paperless-ngx |
| 3 | Enter API URL | `https://docs.weown.net/api/` |
| 4 | Enter Auth Token | Generated from Paperless admin panel |
| 5 | Configure scope | Select tags to sync (e.g., `weekly-summary`) |
| 6 | Set refresh | Polling interval (e.g., every 1 hour) |
| 7 | Test | Verify documents appear in RAG |
| 8 | Repeat | For each AnythingLLM instance |

---

## 📋 Project Team

| CCC | Role | Focus |
|-----|------|-------|
| **GTM** | **Owner** | Architecture, tag schema, contributor onboarding |
| **SHD** | **DevOps** | Droplet provisioning, Docker, DNS, SSL, email ingestion |
| **RMN** | **Platform** | AnythingLLM version verification, connector configuration |

> **No @LDC needed.** Native connector eliminates custom development.

---

## 📋 Deployment Scope (W12-W14)

### Single Phase — Merged (was Phase 1 + Phase 2)

| # | Deliverable | Owner | Priority | Week | Status |
|---|-------------|-------|----------|------|--------|
| 1 | **Verify AnythingLLM v1.11.1+** on all instances | @GTM | 🔴 P0 | W12 | ⬜ TODO |
| 2 | Provision DO Droplet (ATL1) | @SHD | 🔴 P0 | W12 | ⬜ TODO |
| 3 | Deploy Paperless-ngx via Docker Compose | @SHD | 🔴 P0 | W12 | ⬜ TODO |
| 4 | Configure domain + SSL | @SHD | 🔴 P0 | W12 | ⬜ TODO |
| 5 | Create 9 correspondents (CCC mapping) | @GTM | 🟠 P1 | W12 | ⬜ TODO |
| 6 | Configure tag schema | @GTM | 🟠 P1 | W12 | ⬜ TODO |
| 7 | **Configure native AnythingLLM connector (INT-P01)** | @CTO / @GTM / @RMN | 🔴 P0 | W13 | ⬜ TODO |
| 8 | **Verify RAG sync (Paperless → AnythingLLM)** | @GTM | 🔴 P0 | W13 | ⬜ TODO |
| 9 | Set up email ingestion (anythingllm@weown.net) | @SHD | 🟠 P1 | W13 | ⬜ TODO |
| 10 | Test upload workflow (web + email + mobile) | @GTM | 🟠 P1 | W13 | ⬜ TODO |
| 11 | **Configure connector on remaining instances** (INT-OG1, INT-OG8, INT-P02) | @LDC | 🟠 P1 | W13 | ⬜ TODO |
| 12 | Pilot — onboard @LFG or @THY | @LFG | 🟠 P1 | W14 | ⬜ TODO |
| 13 | **Onboard ALL 9 contributors** | @LFG | 🟠 P1 | W14 | ⬜ TODO |
| 14 | Document contributor workflow (GUIDE-XXX) | @GTM | 🟡 P2 | W14 | ⬜ TODO |

> **⚠️ Timeline Note:** Timeline reflects original W09 plan. Actual deployment: ⬜ NOT STARTED (blocked by other W10-W12 priorities including PRJ-039, L-184 cascade, INT-P01 stability).

### Deployment Timeline

```
W10 (Mar 2-8):     Infrastructure
                    ├── Verify AnythingLLM versions
                    ├── Provision Droplet
                    ├── Deploy Paperless-ngx
                    ├── DNS + SSL
                    └── Tag schema + correspondents

W11 (Mar 9-15):    Integration
                    ├── Configure native connector (INT-P01)
                    ├── Verify RAG sync ← KEY MILESTONE
                    ├── Email ingestion setup
                    ├── Configure remaining instances
                    └── Test all ingestion methods

W12 (Mar 16-22):   Onboarding
                    ├── Pilot with @LFG or @THY
                    ├── Onboard all 9 contributors
                    └── Document workflow
```

---

## 📋 Risk Matrix

| # | Risk | Probability | Impact | Mitigation |
|---|------|-------------|--------|------------|
| 1 | AnythingLLM version < v1.9.1 | Low | High | @RMN verifies + upgrades if needed |
| 2 | Storage growth | Low | Low | 50 GB sufficient for years of text; monitor |
| 3 | Contributor adoption | Medium | Medium | Email ingestion = lowest friction; pilot first |
| 4 | PostgreSQL overlap with ecosystem DB | Low | Low | Internal PG via Docker — separate from managed DB |
| 5 | Maintenance burden | Low | Low | Paperless-ngx = mature, well-maintained FOSS |
| 6 | Email deliverability (inbound) | Low | Medium | Test with multiple providers; SPF/DKIM config |
| 7 | Native connector limitations | Low | Medium | Verify tag filtering + sync scope before full deployment |

---

## 📋 FOSS Alignment

| Principle | Paperless-ngx |
|-----------|--------------|
| Priority #1 — #SpeedToMarket | ✅ Docker Compose = deploy in hours |
| Priority #2 — FOSS | ✅ **GPL-3.0** |
| Priority #3 — Data Sovereignty | ✅ **Self-hosted — users own data** |
| Priority #4 — Cooperative Ownership | ✅ Community-maintained project |
| AnythingLLM integration | ✅ **Native connector — zero custom code** |

---

## 📋 Related Projects

| PRJ | Title | Relationship |
|-----|-------|-------------|
| PRJ-005 | WeOwn.wiki (DrupalWiki) | Wiki = collaborative editing; Paperless = document archive |
| PRJ-012 | BurnedOutAdvisor.com | Financial docs use case (Phase 2) |

---

## 📋 Discovered By (BP-047)

| CCC | Contributor | Role | Context |
|-----|-------------|------|---------|
| GTM | [yonks](https://GitHub.com/YonksTEAM) | Co-Founder / Chief Digital Alchemist | #WeeklySummary workflow improvement + AnythingLLM v1.9.1 native connector discovery — W09 |

---

## 📋 Related Documents (BP-045)

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| SharedKernel | v3.2.2.1 | GTM_2026-W11_118 | GTM_2026-W11_139 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/SharedKernel.md) |
| BEST-PRACTICES | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/BEST-PRACTICES.md) |
| PROTOCOLS | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/PROTOCOLS.md) |
| AnythingLLM Changelog v1.9.1 | — | — | — | [docs.anythingllm.com/changelog/v1.9.1](https://docs.anythingllm.com/changelog/v1.9.1) |
| Paperless-ngx Docs | — | — | — | [docs.paperless-ngx.com](https://docs.paperless-ngx.com/) |

---

## 📋 Version History (BP-045)

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| **3.2.3.1** | **2026-W12** | **GTM_2026-W09_065** | **GTM_2026-W12_304** | **REGENERATION + CALHOUN FIXES: #WeOwnVer updated (v3.1.4.1 → v3.2.3.1 — calendar-driven L-094/L-115); +dual #LLMmodel header (L-166); +deployment timeline reality note (Calhoun Finding #2); lifecycle → ✅ APPROVED + 🚀 GH LIVE; 39/41 VSA PASS (VSA_GTM_W12_303); ALL content PRESERVED (L-097); Calhoun Gate 2+3 audit complete; @GTM MANUALLY UPDATED TIMELINE** |
| 3.1.4.1 | 2026-W09 | GTM_2026-W09_065 | GTM_2026-W09_068 | Initial project; Paperless-ngx deployment; AnythingLLM v1.9.1 NATIVE connector (eliminates custom build); Phase 1+2 MERGED into W10-W12; 8 use cases; ATL1 infrastructure ($18/mo); tag schema + 9 CCC correspondents; email ingestion; 14 deliverables; 7-risk matrix; FOSS alignment verified |

---

#FlowsBros #FedArch #Paperless #DocumentManagement #FOSS #WeOwnSeason003 #PRJ-013

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
