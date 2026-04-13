# ✅ Instance Deployment Checklist

## TMPL-011_Instance-Deployment-Checklist_v3.2.0.0.md
## ♾️ WeOwnNet 🌐 — Deployment & Verification Template

| Field | Value |
|-------|-------|
| Template | TMPL-011_Instance-Deployment-Checklist |
| Version | 3.2.1.1 |
| CCC-ID | CTO_2026-W11_001 |
| Approval | ⬜ AWAITING HUMAN APPROVAL (R-011) |
| Purpose | Standard checklist for deploying new #AnythingLLM instances |
| Audience | DevOps, Platform Engineers, ADMIN users |
| Related | INSTANCE_INVENTORY.md, GUIDE-007, BP-025, BP-051 |

---

## 📖 Usage

Copy this template for each new instance deployment:

```
CCC-ID: GTM_2026-W11_XXX
INSTANCE: INT-[OGx/Pxx/Sxx/Mxx/Vxx]
DATE: YYYY-MM-DD
OWNER: @<CCC>
```

---

## ✅ INSTANCE DEPLOYMENT CHECKLIST

### Instance Information

```
Instance ID:    INT-___
Name:           ___
Domain:         ___
Owner(s):       @___, @___
Team:           ___
Purpose:        ___
Type:           ☐ Production (INT-Pxx)  ☐ HomeInstance (INT-OGx)  ☐ Seasonal (INT-Sxx)  ☐ Governance (INT-Mxx/Vxx)
Season:         #WeOwnSeason00_
CCC-ID:         GTM_YYYY-W___XXX (deployment tracking)
Date Started:   YYYY-MM-DD
Target Date:    YYYY-MM-DD
Status:         ☐ Planning  ☐ In Progress  ☐ Deployed  ☐ Verified
```

---

## 🏗️ PHASE 1: INFRASTRUCTURE SETUP

### Compute Resources

| Task | Status | Notes |
|------|--------|-------|
| Provision DigitalOcean Droplet or DOKS cluster | ☐ | Spec: ___ |
| Configure networking (VPC, firewall) | ☐ | Inbound rules: ___ |
| Set up load balancer (if production) | ☐ | Health check interval: ___ |
| Configure DNS records | ☐ | Domain: ___, CNAME: ___ |
| Test connectivity | ☐ | Ping: ___, HTTP: ___ |

### Database Setup

| Task | Status | Notes |
|------|--------|-------|
| Provision PostgreSQL (Managed) | ☐ | Plan: ___, Storage: ___ |
| Configure backups | ☐ | Frequency: daily, retention: ___ days |
| Set up connection pooling (PgBouncer) | ☐ | Max connections: ___ |
| Test database connection | ☐ | Connection string verified |
| Document connection details | ☐ | Store in Infisical (not in inventory) |

### Storage & Persistence

| Task | Status | Notes |
|------|--------|-------|
| Configure persistent volumes (if DOKS) | ☐ | Size: ___, mount path: ___ |
| Set up backup storage | ☐ | DigitalOcean Spaces or equivalent |
| Verify storage permissions | ☐ | Test read/write access |

---

## 🔧 PHASE 2: ANYTHINGLLM DEPLOYMENT

### Platform Installation

| Task | Status | Notes |
|------|--------|-------|
| Deploy AnythingLLM v1.11+ | ☐ | Version: 1.11.X |
| Configure environment variables | ☐ | Check: DB_HOST, LLM_KEY, EMBEDDING_MODEL |
| Set admin user credentials | ☐ | Format: a-<ccc>_dev (ADMIN) |
| Create default user | ☐ | Format: u-<ccc>_user (DEFAULT) |
| Configure SSL/TLS certificate | ☐ | Auto-renew: yes, provider: Let's Encrypt |
| Verify AnythingLLM is running | ☐ | Health check: curl http://localhost:3001/health |

### Workspace Creation

| Workspace | Purpose | Creator | Status | Notes |
|-----------|---------|---------|--------|-------|
| CCC | Production / Users | ADMIN | ☐ | |
| tools | Strategy / META + MAIT | ADMIN | ☐ | For governance instances only |
| ADMIN | Admin functions | ADMIN | ☐ | System-level configuration |
| events | Event planning (optional) | ADMIN | ☐ | As needed |
| P.O.P. | People/Orgs/Places (optional) | ADMIN | ☐ | If applicable to instance |

### Workspace Configuration

For each workspace:

| Workspace | Task | Status | Notes |
|-----------|------|--------|-------|
| **CCC** | Workspace Prompt added | ☐ | Per TMPL-006 |
| **CCC** | Chat History = 40 | ☐ | Per BP-061 |
| **CCC** | RAG documents synced | ☐ | GitHub connector (GUIDE-006) |
| **tools** | Workspace Prompt (non-CCC block) | ☐ | Per BP-053 |
| **tools** | RAG documents synced | ☐ | Governance docs: SK, BP, PROTO, CCC |
| **ADMIN** | Workspace Prompt (non-CCC block) | ☐ | Per BP-053 |
| **ADMIN** | RAG documents synced | ☐ | System-level docs |

---

## 🎖️ PHASE 3: SYSTEM PROMPT & IDENTITY

### Instance Identity

| Task | Status | Notes |
|------|--------|-------|
| System Prompt created | ☐ | Per TMPL-006_SYSTEM-PROMPT-TEMPLATE |
| INSTANCE IDENTITY block included | ☐ | R-213: FIRST section |
| Instance ID specified | ☐ | INT-___ |
| Domain specified | ☐ | ___ |
| Owner(s) specified | ☐ | @___, @___ |
| Type specified | ☐ | Production / HomeInstance / etc. |
| Season specified | ☐ | #WeOwnSeason00_ 🚀 |
| #LLMmodel specified | ☐ | Qwen3.5-397B-A17B (primary) |
| CCC-ID logic table included | ☐ | Per BP-054 |

### System Prompt Verification

| Check | Status | Notes |
|-------|--------|-------|
| Prompt loaded in AnythingLLM | ☐ | Settings → System Prompt |
| Agent responds with instance identity | ☐ | Query: "What instance are you?" |
| Workspace-conditional CCC-ID logic works | ☐ | Test CCC workspace vs. tools |

---

## 📌 PHASE 4: PINNED DOCUMENTS & RAG

### #PinnedDocs (Production & Seasonal Only)

| Document | v3.X.X.X | Pinned? | Status | Notes |
|----------|----------|---------|--------|-------|
| SharedKernel | 3.2+ | ☐ | — | Governance foundation |
| BEST-PRACTICES | 3.1+ | ☐ | — | All BP-* rules |
| PROTOCOLS | 3.1+ | ☐ | — | All communication protocols |
| CCC | 3.1+ | ☐ | — | Attribution standard |
| **TOTAL** | — | ☐ | — | **4 docs required** |

### GitHub RAG Connector Setup

| Task | Status | Notes |
|------|--------|-------|
| GitHub Personal Access Token created | ☐ | Per GUIDE-006 |
| PAT stored in Infisical (Tier 2) | ☐ | Not in AnythingLLM UI |
| GitHub connector configured in ADMIN | ☐ | Repo: CCCbotNet/fedarch |
| Initial RAG sync completed | ☐ | Settings → Documents → Refresh |
| RAG documents verified | ☐ | Test: `list:docs` command |
| Fresh session after RAG upload | ☐ | Per BP-031 |

### RAG Workspace Mapping

| Workspace | Source Folder(s) | Sync Status | Notes |
|-----------|------------------|------------|-------|
| CCC | _GUIDES_, _PROJECTS_, _WEEKLY_, USER notes | ☐ | User-facing docs |
| tools | _SYS_, _GUIDES_, _LEARNINGS_, _TEMPLATES_, _MISC_ | ☐ | Governance docs |
| ADMIN | _SYS_ | ☐ | System configuration |

---

## 🧵 PHASE 5: THREADS & AGENTS

### User Agent Setup

| Task | Status | Notes |
|------|--------|-------|
| User account created: u-<ccc>_user | ☐ | Role: DEFAULT |
| User assigned to workspaces | ☐ | Minimum: CCC, tools |
| USER-IDENTITY created (TMPL-009) | ☐ | Uploaded to RAG: _USERS_/ |
| User can log in | ☐ | Test login from different device |

### MAIT Thread Setup (if tools workspace)

| MAIT Thread | UUID | Purpose | Status | Notes |
|-------------|------|---------|--------|-------|
| — | — | — | ☐ | Add rows per MAIT topics |

Example:
| MAIT_AnythingLLM | <UUID> | AnythingLLM SME | ☐ | Steward: @GTM |
| MAIT_GitHub | <UUID> | GitHub & GH connector | ☐ | Steward: @GTM |

### Thread Registry Entry

```
Add to THREAD REGISTRY (SharedKernel.md or local tracking):
- Thread name: MAIT_<Topic>
- UUID: <from AnythingLLM>
- Steward: @<CCC>
- ShortCode: @MAIT:#<Topic>
- Instance: INT-___
```

---

## 🔐 PHASE 6: SECURITY & ACCESS

### API Keys & Credentials

| Service | Key Type | Storage | Rotation | Status | Notes |
|---------|----------|---------|----------|--------|-------|
| OpenRouter | API Key | Infisical | 7 days (shared) / 30 days (personal) | ☐ | Per BP-064 |
| GitHub PAT | Personal Access Token | Infisical | 90 days (GitHub default) | ☐ | Read-only: repo, workflow |
| Database | Connection string | Infisical | Via rotation | ☐ | Never in plain text |

### User Access Control

| User Type | Access Level | 2FA Required? | Workspace List | Status |
|-----------|--------------|---------------|-----------------|--------|
| ADMIN (a-<ccc>_dev) | Full system | ☐ Recommended | ALL | ☐ |
| DEFAULT (u-<ccc>_user) | Limited / scoped | ☐ Recommended | CCC + tools | ☐ |
| Guest (if applicable) | Read-only | ☐ Recommended | CCC only | ☐ |

### Firewall & Network Security

| Check | Status | Notes |
|-------|--------|-------|
| Inbound rules configured | ☐ | Allow: HTTP(80), HTTPS(443) only |
| Outbound rules configured | ☐ | Allow: DNS, HTTPS for LLM/API calls |
| VPC security tested | ☐ | Database accessible only from app |
| Rate limiting enabled | ☐ | Per user / IP (if applicable) |
| DDoS protection enabled | ☐ | DigitalOcean built-in |

---

## 🔬 PHASE 7: OBSERVABILITY & MONITORING

### Logging Setup

| Component | Logger | Retention | Centralized? | Status |
|-----------|--------|-----------|-------------|--------|
| AnythingLLM app | Built-in logs | 30 days (default) | ☐ | Accessible via docker logs |
| PostgreSQL | Query logs | — | ☐ | Optional per compliance |
| Nginx/Caddy | Access logs | 7 days (default) | ☐ | Useful for debugging |

### Metrics & Monitoring

| Metric | Tool | Dashboard | Alert Threshold | Status |
|--------|------|-----------|-----------------|--------|
| Uptime | Uptime Robot or similar | ☐ | 99.5% target | ☐ |
| CPU Usage | DigitalOcean + AnythingLLM | ☐ | >80% alert | ☐ |
| Memory Usage | DigitalOcean + AnythingLLM | ☐ | >80% alert | ☐ |
| Database Connections | PostgreSQL | ☐ | >18/22 alert | ☐ |
| Storage Usage | DigitalOcean | ☐ | >85% alert | ☐ |
| API Latency | AnythingLLM built-in | ☐ | >5s alert | ☐ |

### Incident Response

| Setup | Status | Notes |
|-------|--------|-------|
| On-call schedule created | ☐ | Who? When? Rotation? |
| Incident channel created | ☐ | Signal: #incidents or similar |
| Runbook documented (GUIDE-009) | ☐ | Common issues + resolution steps |
| Escalation path defined | ☐ | L1 → L2 → L3 |

---

## 📋 PHASE 8: ISC CERTIFICATION (INSTANCE SEASON CERTIFICATION)

### ISC 8-Point Checklist (BP-059)

Apply within **2 weeks of season start** (or deployment):

| # | Check | Criteria | Status | Verified By |
|---|-------|----------|--------|-------------|
| 1 | Embedder | Qwen3 Embedding 4B | ☐ | @___ |
| 2 | LLM Model | Qwen3.5-397B-A17B (prod) or Claude Opus 4.6 (governance) | ☐ | @___ |
| 3 | #PinnedDocs | 4 docs present @ v3.X.X.X | ☐ | @___ |
| 4 | System Prompt | Season tag + INSTANCE IDENTITY (R-213) | ☐ | @___ |
| 5 | Workspace Prompts | BP-053 + BP-054 + BP-061 + BP-062 | ☐ | @___ |
| 6 | USER-IDENTITY | Owner(s) current + season verified | ☐ | @___ |
| 7 | RAG Sync | GitHub connector refreshed | ☐ | @___ |
| 8 | #ContextVolley | Can reach #MetaAgent @ INT-P01 | ☐ | @___ |

### ISC Result

```
☐ CERTIFIED (8/8 pass)
☐ FAILED (fix items and re-run)
```

**If CERTIFIED:** Generate TMPL-010_ISC attestation document and commit to GitHub.

---

## 📖 PHASE 9: DOCUMENTATION & INVENTORY

### INSTANCE_INVENTORY.md Update

Add instance to appropriate section:

| Section | Row Added? | Verify |
|---------|------------|--------|
| Instance Registry (Active) | ☐ | All columns filled or TBD noted |
| Resource Allocation Details | ☐ | Platform, compute, storage, LLM |
| Owner & Team Assignment | ☐ | Owner(s), team, backup contact |
| Maintenance & SLA | ☐ | Windows, frequency, backup schedule |
| Security & Access | ☐ | Auth, 2FA, API rotation |
| Capacity & Growth | ☐ | Users, max, growth trend |
| Deployment & CI/CD | ☐ | Deploy method, CI/CD, rollback |
| Observability & Monitoring | ☐ | Logging, metrics, alerts |
| Droplets & Physical Resources | ☐ | Compute, database, DNS |

### Related Documentation

| Document | Created? | Location | Notes |
|----------|----------|----------|-------|
| Instance deployment notes | ☐ | Session notes (RAG only, R-199) | Timestamps, issues, resolutions |
| ISC attestation | ☐ | _INSTANCE_/ folder | TMPL-010_ISC attestation |
| User identity document | ☐ | _USERS_/ folder (RAG only) | TMPL-009_USER-IDENTITY |
| Architecture diagram | ☐ | _INSTANCE_/ folder (optional) | Network, workspaces, threads |

---

## ✅ PHASE 10: VERIFICATION & SIGN-OFF

### Final Verification Tests

| Test | Command/Action | Expected Result | Status |
|------|---|---|---|
| Instance health | curl https://<domain>/health | 200 OK | ☐ |
| CCC workspace | Log in as user, type #help | Responds with user ID + CCC-ID | ☐ |
| tools workspace | Log in as ADMIN, check RAG | Can list governance docs | ☐ |
| LLM functionality | Ask simple question | Gets response from configured LLM | ☐ |
| RAG retrieval | Query governance doc | Retrieves correct document passage | ☐ |
| #ContextVolley | Send test message to #MetaAgent | Receive acknowledgment | ☐ |
| Database backup | Check backup status | Latest backup < 24h old | ☐ |
| DNS resolution | nslookup <domain> | Resolves correctly | ☐ |

### Sign-Off

```
Instance ID:     INT-___
Deployment Date: YYYY-MM-DD
Verified By:     @<CCC> (signature)
Date Verified:   YYYY-MM-DD
Status:          ☐ READY FOR PRODUCTION  ☐ NEEDS FIXES (see notes)

Notes:
- [Any issues or follow-ups needed]
```

---

## 📝 Post-Deployment

### Handoff Checklist

- ☐ INSTANCE_INVENTORY.md updated + committed
- ☐ ISC certification completed (if applicable)
- ☐ USER-IDENTITY document created (if user-facing)
- ☐ Deployment notes documented (session RAG)
- ☐ Team notified via #WeeklySummary
- ☐ On-call schedule updated
- ☐ Incident runbook available

### First Week Monitoring

- ☐ Daily health checks (uptime, errors)
- ☐ Monitor resource usage (CPU, memory, disk)
- ☐ Check database connection count
- ☐ Verify backups running
- ☐ Log any issues + resolutions

---

## 📋 Version History

| Version | Date | Changes |
|---------|------|---------|
| 3.2.1.1 | 2026-W11 | CTO_2026-W11_001 | ⬜ AWAITING | 🚀 **INITIAL RELEASE** — Complete deployment checklist; 10 phases: infrastructure, AnythingLLM, system prompt, pinned docs, threads, security, observability, ISC, documentation, verification; aligned with BP-025 (instance setup order), BP-051 (#HomeInstance setup), BP-059 (ISC certification) |

---

## 🔗 Related Documents

| Document | Purpose | URL |
|---|---|---|
| INSTANCE_INVENTORY.md | Master inventory | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_INSTANCE_/INSTANCE_INVENTORY.md) |
| GUIDE-007 | Inventory maintenance | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_GUIDES_/GUIDE-007_Infrastructure-Inventory-Management.md) |
| TMPL-006 | System Prompt template | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_TEMPLATES_/TMPL-006_SYSTEM-PROMPT-TEMPLATE.md) |
| TMPL-009 | USER-IDENTITY template | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_TEMPLATES_/TMPL-009_USER-IDENTITY.md) |
| TMPL-010 | ISC attestation | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_TEMPLATES_/TMPL-010_ISC.md) |
| GUIDE-006 | GitHub RAG connector | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_GUIDES_/GUIDE-006_GitHub-PAT-for-AnythingLLM.md) |
| BP-025 | Instance setup order | SharedKernel.md |
| BP-051 | #HomeInstance setup | BEST-PRACTICES.md |
| BP-059 | ISC certification | BEST-PRACTICES.md |

---

#FlowsBros #FedArch #Deployment #Checklist #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
