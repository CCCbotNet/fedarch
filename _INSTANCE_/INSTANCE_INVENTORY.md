# 🏗️ Infrastructure Instance Inventory

## INSTANCE_INVENTORY_v3.2.0.0.md
## ♾️ WeOwnNet 🌐 — Master Infrastructure Index

| Field | Value |
|-------|-------|
| Document | INSTANCE_INVENTORY.md |
| Version | 3.2.1.1 |
| CCC-ID | CTO_2026-W11_001 |
| Updated | 2026-03-17 (W11) |
| Season | #WeOwnSeason003 🚀 |
| Status | 🔄 LIVING DOCUMENT |
| Purpose | Single source of truth for all infrastructure instances |
| Steward(s) | @CTO (Nik Cimino) + @RMN |
| Related | GUIDE-007, TMPL-011, SharedKernel (Elevated Instance Registry) |

---

## 📖 Table of Contents

1. [Overview](#-overview)
2. [Instance Registry — Active](#-instance-registry--active)
3. [Instance Registry — Planning](#-instance-registry--planning)
4. [Resource Allocation Details](#-resource-allocation-details)
5. [Droplets & Physical Resources](#-droplets--physical-resources)
6. [Network & Connectivity](#-network--connectivity)
7. [Owner & Team Assignment](#-owner--team-assignment)
8. [Maintenance & SLA](#-maintenance--sla)
9. [Security & Access](#-security--access)
10. [Capacity & Growth](#-capacity--growth)
11. [Deployment & CI/CD](#-deployment--cicd)
12. [Observability & Monitoring](#-observability--monitoring)
13. [Backup & Disaster Recovery](#-backup--disaster-recovery)
14. [Cost & Billing](#-cost--billing)
15. [Update & Maintenance Log](#-update--maintenance-log)
16. [Version History](#-version-history)
17. [Related Documents](#-related-documents)

---

## 📋 Overview

### Purpose

This document tracks **all infrastructure instances** in the ♾️ WeOwnNet 🌐 ecosystem, including:
- **Domain/Cloud Instances** — AnythingLLM deployment details
- **Compute Resources** — DigitalOcean Droplets, DOKS clusters
- **Database Infrastructure** — PostgreSQL managed instances
- **DNS & Networking** — Domain registrations, VPCs
- **Backup & Storage** — Data persistence strategy
- **Team & Ownership** — Who manages what, escalation paths

### Living Document Standard

This inventory is updated **immediately** when:
- ✅ New instance deployed
- ✅ Owner or team changes
- ✅ Resource scaling (compute, storage, database plan)
- ✅ SLA or maintenance window changes
- ✅ Security policy updates (key rotation, firewall rules)
- ✅ Critical incident or outage

**Update Window:** Within **24 hours** of change; critical incidents within **1 hour**.

### Update Process (per BP-027)

1. **Set #masterCCC** at start of maintenance/deployment session
2. **Document change** with timestamp and rationale
3. **Stage & commit** changes to GitHub
4. **Sync to RAG** (automated every 5 minutes via git-sync)
5. **Notify team** via #WeeklySummary or #ContextBroadcast

---

## 📋 Instance Registry — ACTIVE

### Current Deployment Map

| Instance ID | Type | Name | Domain | Owner(s) | Team | Business Purpose | Status | Location | Deployed | Notes |
|------------|------|------|--------|----------|------|------------------|--------|----------|----------|-------|
| **INT-P01** | Production | AI.WeOwn.Agency | ai.weown.agency | ORG (@GTM + @THY) | Core / WeOwn.Agency | ♾️ #FedArch Hub + Production MAITs + User Agents | ✅ Active | AWS? | 2025-Q4 | Primary production instance; 4 workspaces (CCC, tools, ADMIN, P.O.P.); 10+ users |
| **INT-P02** | Production | BurnedOut.Media | lite.burnedout.xyz | @LDC | BurnedOut.Media | 🔥 BurnedOut.Media #ProjectConnex (multi-user) | ✅ Active | DigitalOcean / DOKS | 2025-Q4 | Project-specific; 2 MAITs (connexOmni, connexAthena); 5+ users |
| **INT-P03** | Production | POP-WeOwn-tools | — | @GTM | Core | P.O.P. Database Instance (People, Orgs, Places) | ✅ Active | DOKS | 2025-Q4 | Shared multi-instance tool; indexed data platform |
| **INT-P05** | Production | AgencyPRO | pro.weown.tools | @GTM | Core | AgencyPRO (PRJ-002, multi-customer SaaS) | ✅ Active | DOKS | 2025-Q4 | Product: PRJ-002; scaling with customer growth |
| **INT-P06** | Production | [NAME TBD] | — | — | Core | [Purpose TBD] | 🔄 Reserved | — | TBD | Future expansion; planned post-Season003 |
| **INT-OG1** | HomeInstance | YonksTEAM | ai.yonksteam.xyz | @GTM, @THY | Core | Personal #HomeInstance (Jason + Tyler) | ✅ Active | Custom | 2025-Q3 | Founding OG personal domain |
| **INT-OG8** | HomeInstance | [NAME TBD] | ai.romanid.xyz | @RMN | Core | Personal #HomeInstance (@RMN) | 🔄 Setup | Custom | 2026-W05 | Infrastructure engineer personal instance |
| **INT-OG9** | HomeInstance | CoachLFG | ai.coachlfg.com | @LFG | Core | Personal #HomeInstance (@LFG) | ✅ Active | Custom | 2025-Q4 | Founding OG personal domain |
| **INT-S003** | Seasonal | [NAME TBD] | s003.ccc.bot | ORG | Core | Seasonal Shared #HomeInstance (#WeOwnSeason003) | 📋 Planning | DOKS | 2026-W07 | Multi-contributor shared instance; 3-4 users |
| **INT-M01** | META | META.ccc.bot | meta.weown.tools | ORG (@GTM) | Core | #MetaAgent Governance Hub (Orchestrator + VSA) | 📋 Planned | DOKS | 2026-W12 | Central governance authority; planned post-ISC Phase |
| **INT-VSA** | Verification | VSA.ccc.bot | vsa.weown.tools | ORG (@GTM) | Core | VSA Verification Services (governance attestation) | 📋 Planned | DOKS | 2026-W12 | Reports to INT-M01; document verification |

---

## 📋 Instance Registry — PLANNING

| Instance ID | Type | Name | Domain | Owner(s) | Team | Business Purpose | Status | Target Date | Notes |
|------------|------|------|--------|----------|------|------------------|--------|-------------|-------|
| **INT-OG4** | HomeInstance | [TBD] | — | @IAL | Core | Personal #HomeInstance (@IAL) | ⬜ SHD P3 | 2026-W15 | CoFounder; infrastructure TBD |
| **INT-OG7** | HomeInstance | [TBD] | — | @CRO | Core | Personal #HomeInstance (@CRO) | ⬜ Reserved | 2026-W20 | Founder; infrastructure TBD |
| **INT-P04** | Production | [TBD] | — | — | — | [Purpose TBD] | ⬜ Backlog | TBD | Future production workload |
| **INT-S004** | Seasonal | [TBD] | — | ORG | Core | Seasonal Shared #HomeInstance (#WeOwnSeason004) | ⬜ Planned | 2026-W21 | Deployment 2 weeks before S003 ends |

---

## 📋 Resource Allocation Details

### INT-P01 (AI.WeOwn.Agency)

| Resource | Specification | Capacity | Current Load | Notes |
|----------|---------------|----------|--------------|-------|
| **Platform** | AnythingLLM | v1.11+ | v1.11+ | Core platform |
| **LLM Model** | Qwen3.5-397B-A17B | 397B params | — | Via OpenRouter (Apache 2.0) |
| **Embedder** | Qwen3 Embedding 4B | 4B params | — | Local embedding |
| **Compute** | ? | ? | ? | **[DOCUMENT NEEDED]** |
| **Storage** | PostgreSQL (Managed) | 2-50GB tier | ~5-10GB est. | DigitalOcean Managed; connections: 22 (basic) |
| **Memory** | ? | ? | ? | **[DOCUMENT NEEDED]** |
| **Workspaces** | 5 (CCC, tools, ADMIN, events, P.O.P.) | All active | 4+ concurrent | Full multi-workspace |
| **Users** | 10+ | Unlimited tier | 10+ active | Invite-only participation |
| **SLA** | 99.5% uptime | — | TBD | Documented target |
| **Backup** | Daily automated | 30-day retention | — | DigitalOcean managed |
| **SSL/TLS** | Let's Encrypt | — | Auto-renew | Free, auto-managed |

### INT-P02 (Lite.BurnedOut.xyz)

| Resource | Specification | Capacity | Current Load | Notes |
|----------|---------------|----------|--------------|-------|
| **Platform** | AnythingLLM | v1.11+ | v1.11+ | Core platform |
| **LLM Model** | Qwen3.5-397B-A17B | 397B params | — | Via OpenRouter |
| **Embedder** | Qwen3 Embedding 4B | 4B params | — | Local embedding |
| **Compute** | DOKS (DigitalOcean Kubernetes) | Standard node | 50-70% CPU est. | Shared cluster; scaling enabled |
| **Storage** | PostgreSQL (Managed) | 2-50GB tier | ~3-5GB est. | DigitalOcean Managed; pooled connections |
| **Memory** | 2-4GB per pod | — | — | Kubernetes auto-scaling |
| **Workspaces** | 4 (CCC, tools, ADMIN, events) | All active | 3+ concurrent | Project-specific tools |
| **Users** | 5+ | Unlimited tier | 5+ active | BurnedOut.Media team |
| **SLA** | 99.0% uptime | — | TBD | Project-level guarantee |
| **Backup** | Daily automated | 30-day retention | — | DigitalOcean managed |
| **SSL/TLS** | Let's Encrypt | — | Auto-renew | Free, auto-managed |

### INT-P03 (POP-WeOwn-tools)

| Resource | Specification | Notes |
|----------|---------------|-------|
| **Purpose** | People, Organizations, Places database | Indexed data platform |
| **Platform** | AnythingLLM | v1.11+ |
| **LLM Model** | Qwen3.5-397B-A17B | Via OpenRouter |
| **Compute** | DOKS | Shared multi-tool cluster |
| **Storage** | PostgreSQL | Managed; scaling per data growth |
| **Users** | 3-5+ | Cross-team access |
| **Notes** | **[EXPAND WITH CURRENT DETAILS]** | — |

### INT-P05 (AgencyPRO)

| Resource | Specification | Notes |
|----------|---------------|-------|
| **Purpose** | Multi-customer SaaS product | PRJ-002 commercial offering |
| **Platform** | AnythingLLM | v1.11+ |
| **LLM Model** | Qwen3.5-397B-A17B | Via OpenRouter |
| **Compute** | DOKS with auto-scaling | Scales with customer base |
| **Storage** | PostgreSQL | Premium plan for reliability |
| **Database Connections** | Connection pooling (PgBouncer) | Supports 50+ concurrent users |
| **Users** | 5+ core, scaling to 50+ | Multi-tenant architecture |
| **Backup** | Hourly automated | Mission-critical data |
| **Monitoring** | Langfuse + custom dashboards | Real-time performance tracking |
| **Notes** | **[EXPAND WITH CURRENT DETAILS]** | — |

---

## 📋 Droplets & Physical Resources

### DigitalOcean Account Structure

| Resource | Details | Owner | Status | Notes |
|----------|---------|-------|--------|-------|
| **Account 1** | [Team name] | @GTM + @RMN | Active | Production instances (INT-Pxx) |
| **Account 2** | [Team name] | — | — | **[IF APPLICABLE]** — separate team/billing? |

### Droplet Inventory

| Droplet Name | Instance(s) | Size | Region | IP | Created | Backup? | Status | Notes |
|--------------|-------------|------|--------|-----|---------|---------|--------|-------|
| INT-P01-Primary | INT-P01 | — | — | — | — | ✅ | 🔄 **[POPULATE]** | Production; monitor uptime |
| INT-P02-DOKS-Node-1 | INT-P02 (DOKS) | Standard | ATL1 | — | — | ✅ | 🔄 **[POPULATE]** | DOKS cluster node; auto-scaling |
| — | — | — | — | — | — | — | — | **[Add rows for all droplets]** |

### Database Resources

| Database | Instance | Plan | Size | Backup | Retention | Connection Pool | Status | Notes |
|----------|----------|------|------|--------|-----------|-----------------|--------|-------|
| INT-P01 PG | INT-P01 | Managed Basic | 2-50GB | Daily auto | 30 days | PgBouncer (22 connections + pooling) | ✅ | Primary production DB |
| INT-P02 PG | INT-P02 | Managed Basic | 2-50GB | Daily auto | 30 days | PgBouncer (pooling enabled) | ✅ | Project-specific DB |
| INT-P05 PG | INT-P05 | Managed Premium | 10GB+ | Hourly auto | 60 days | Heavy pooling for multi-tenant | ✅ | Mission-critical SaaS |
| — | — | — | — | — | — | — | — | **[Add all databases]** |

### Networking Resources

| Resource | Type | Purpose | Provider | Status | Notes |
|----------|------|---------|----------|--------|-------|
| ai.weown.agency | Domain | INT-P01 | Porkbun? | ✅ | Primary production |
| lite.burnedout.xyz | Domain | INT-P02 | ? | ✅ | Project domain |
| pro.weown.tools | Domain | INT-P05 | ? | ✅ | AgencyPRO SaaS |
| s003.ccc.bot | Domain | INT-S003 (planned) | ? | 📋 | Seasonal shared instance |
| meta.weown.tools | Domain | INT-M01 (planned) | ? | 📋 | Governance meta-instance |
| vsa.weown.tools | Domain | INT-VSA (planned) | ? | 📋 | VSA verification services |
| **WeOwn.Dev VPC** | VPC | Internal networking | DigitalOcean | ✅ | If applicable; DOKS clusters |
| **Firewall Rules** | — | Inbound/outbound | DigitalOcean | ✅ | HTTP(80), HTTPS(443) inbound |

---

## 📋 Network & Connectivity

### Instance Connectivity

| Instance | Region | VPC | Type | Public IP | Private IP | Firewall Rules | Load Balancer? |
|----------|--------|-----|------|-----------|------------|-----------------|----------------|
| INT-P01 | ? | — | Droplet / DOKS | ? | ? | Allow: HTTP, HTTPS | ? |
| INT-P02 | ATL1 | WeOwn.Dev VPC | DOKS | — | 10.x.x.x | Allow: HTTP, HTTPS | ✅ (if DOKS) |
| INT-P03 | ? | ? | — | — | — | — | — |
| INT-P05 | ? | ? | DOKS | — | — | Allow: HTTPS only | ✅ (SaaS) |

### Cross-Instance Communication

| From | To | Protocol | Purpose | Status | Notes |
|------|-----|----------|---------|--------|-------|
| INT-P01:tools | INT-M01 (planned) | HTTPS / #ContextVolley | Governance sync (R-170) | 📋 Pending | #MetaAgent will be central |
| INT-P02 | INT-P01 | HTTPS (#ContextVolley) | Cross-instance communication | 🔄 Testing | VSA sync, shared learnings |
| INT-Pxx | INT-Sxx | HTTPS (#ContextVolley) | Seasonal contributor access | 📋 Planned | Will integrate when S003 deploys |

### DNS Configuration

| Domain | Registrar | Nameservers | CNAME Target | Status | Auto-Renew |
|--------|-----------|-----------|---|---|---|
| ai.weown.agency | ? | ? | ai.weown.agency | ✅ | ✅ |
| lite.burnedout.xyz | ? | ? | lite.burnedout.xyz | ✅ | ✅ |
| pro.weown.tools | ? | ? | pro.weown.tools | ✅ | ✅ |

---

## 📋 Owner & Team Assignment

### Instance Stewardship

| Instance | Owner(s) | Team | Backup Contact | Escalation | CCC-ID |
|----------|----------|------|-----------------|------------|--------|
| INT-P01 | @GTM, @THY | Core/WeOwn.Agency | @RMN | @RMN (CTO) | GTM_2026-W11_XXX |
| INT-P02 | @LDC | BurnedOut.Media | @GTM | @RMN | LDC_2026-W11_XXX |
| INT-P03 | @GTM | Core | @RMN | @RMN | GTM_2026-W11_XXX |
| INT-P05 | @GTM | Core | @RMN | @RMN | GTM_2026-W11_XXX |
| INT-OG1 | @GTM, @THY | Core | — | @RMN | GTM_2026-W11_XXX |
| INT-OG8 | @RMN | Core | — | @GTM | RMN_2026-W11_XXX |
| INT-OG9 | @LFG | Core | — | @GTM | LFG_2026-W11_XXX |
| INT-S003 (planned) | @GTM + seasonal team | Core | @RMN | @RMN | GTM_2026-W11_XXX |
| INT-M01 (planned) | ORG (@GTM) | Core | @RMN | — | GTM_2026-W11_XXX |

### On-Call Schedule

| Instance | On-Call | Secondary | Escalation | Contact Method |
|----------|---------|-----------|------------|-----------------|
| INT-P01 | @RMN | @GTM | @THY (CEO) | Signal: ♾️ WeOwn.Agency 👥 |
| INT-P02 | @LDC | @GTM | @RMN | Signal: 🔥 BurnedOut.Media 🔀 |
| INT-S003 | @GTM | @RMN | — | Signal: #incidents |

---

## 📋 Maintenance & SLA

### Service Level Agreements

| Instance | Target Uptime | Maintenance Window | Backup Schedule | Update Policy | Notes |
|----------|---|---|---|---|---|
| INT-P01 | 99.5% | Sundays 00:00-04:00 EST | Daily 02:00 EST | Monthly (Patch Tuesday equivalent) | Mission-critical; business hours preferred |
| INT-P02 | 99.0% | Sundays 02:00-06:00 EST | Daily 02:00 EST | Monthly | Project-specific; lower SLA acceptable |
| INT-P05 | 99.9% | Sundays 01:00-03:00 EST | Hourly | Weekly for patches | SaaS product; higher availability required |

### Maintenance Calendar

| Instance | Weekly | Monthly | Quarterly |
|----------|--------|---------|-----------|
| INT-P01 | DigitalOcean security updates | #WeOwnSeason review | Full infrastructure audit |
| INT-P02 | Droplet updates | Connection pool optimization | Cluster scaling review |
| INT-P05 | Database optimization | Customer health check | SLA performance audit |

---

## 📋 Security & Access

### Authentication & Authorization

| Instance | Auth Method | 2FA | SSO? | API Keys | Management | Notes |
|----------|-------------|-----|------|----------|-----------|-------|
| INT-P01 | AnythingLLM LDAP + Invite | ⬜ | ❌ | OpenRouter (7-day rotation per BP-064) | ADMIN users | Default + ADMIN roles |
| INT-P02 | AnythingLLM LDAP + Invite | ⬜ | ❌ | OpenRouter (7-day rotation per BP-064) | ADMIN users | Per-project teams |
| INT-P05 | AnythingLLM + Custom API | ✅ Recommended | ❌ | OpenRouter (7-day rotation per BP-064) | SaaS admin panel | Multi-tenant isolation |

### API Key Rotation Policy (BP-064)

| Service | Instance Type | Rotation Cadence | Manager | Storage | Status |
|---------|---|---|---|---|---|
| OpenRouter | #SharedInstance (INT-Pxx) | 7 days | ADMIN | Infisical (Tier 2) | 🔄 Implemented |
| OpenRouter | #HomeInstance (INT-OGx) | 30 days | Owner | Infisical (Tier 2) | 📋 Phase 2 |
| GitHub PAT | All instances | 90 days (GitHub default) | @RMN | Infisical (Tier 2) | ✅ Active |

### Firewall & Network Security

| Instance | Inbound Rules | Outbound Rules | VPC Isolation | Notes |
|----------|---|---|---|---|
| INT-P01 | HTTP(80), HTTPS(443) | DNS, HTTPS (LLM APIs) | — | Open to public (Web UI) |
| INT-P02 | HTTP(80), HTTPS(443) | DNS, HTTPS (LLM APIs) | WeOwn.Dev VPC (if DOKS) | Database access restricted to pod network |
| INT-P05 | HTTPS(443) only | DNS, HTTPS (LLM + payment APIs) | WeOwn.Dev VPC | Database access restricted to SaaS tier |

---

## 📋 Capacity & Growth

### User Growth Projections

| Instance | Current Users | Max Capacity | Growth Rate | 12-Month Projection | Notes |
|----------|---|---|---|---|---|
| INT-P01 | 10+ | 50-100 (estimated) | +2-3 users/week | 50-75 users | Core team + community |
| INT-P02 | 5+ | 20-30 (estimated) | +1 user/month | 10-15 users | BurnedOut.Media team |
| INT-P05 | 5+ core | 500+ | +50 users/quarter | 100-200 SaaS users | AgencyPRO commercial customers |

### Resource Scaling Triggers

| Metric | Threshold | Action | Responsible |
|--------|-----------|--------|-------------|
| CPU Usage | >80% sustained | Scale compute up | @RMN |
| Memory Usage | >80% sustained | Adjust pod resources | @RMN |
| Database Connections | >18/22 (Basic plan) | Enable pooling or upgrade plan (L-123) | @RMN |
| Storage Usage | >85% disk space | Expand volume or migrate | @RMN |
| API Latency | >5 seconds average | Analyze + optimize bottleneck | @GTM + @RMN |

---

## 📋 Deployment & CI/CD

### Deployment Methods

| Instance | Deploy Method | Version Control | CI/CD | Rollback Plan | Status |
|----------|---|---|---|---|---|
| INT-P01 | Manual + IaC (Helm) | CCCbotNet/fedarch (GitHub) | ⬜ Planned | Blue-green swap | ✅ Ready |
| INT-P02 | Manual + IaC (Helm) | CCCbotNet/fedarch (GitHub) | ⬜ Planned | Pod restart rollback | ✅ Ready |
| INT-P05 | GitOps (ArgoCD planned) | CCCbotNet/fedarch (GitHub) | ⬜ Phase 2 | Automatic rollback | 🔄 Planned |

### Update Strategy

| Instance | Release Cycle | Patch Policy | Testing | Approval | Status |
|----------|---|---|---|---|---|
| INT-P01 | Monthly | Auto-security patches | Staging env (manual) | @RMN + @GTM | ✅ Active |
| INT-P02 | Monthly | Auto-security patches | Manual verification | @LDC + @GTM | ✅ Active |
| INT-P05 | Bi-weekly | Auto-security + feature patches | Full test suite | @GTM (CCC-ID approval per R-011) | 🔄 Maturing |

---

## 📋 Observability & Monitoring

### Logging

| Instance | Tool | Retention | Centralized? | Queries | Status |
|----------|------|-----------|---|---|---|
| INT-P01 | Docker logs (built-in) | 30 days (default) | ⬜ No | Manual via docker logs | ✅ |
| INT-P02 | Docker + DOKS events | 14 days (DOKS default) | ⬜ No | Kubectl logs | ✅ |
| INT-P05 | Docker + application logs | 60 days | ⬜ Recommended | ELK or Datadog (Phase 2) | 🔄 Planned |

### Metrics & Dashboards

| Metric | Tool | Dashboard | Alert Threshold | Current Status | Notes |
|--------|------|-----------|---|---|---|
| Uptime | Uptime Robot (or DO monitoring) | ✅ | 99.5% / 99.0% / 99.9% (per SLA) | 🔄 Tracking | Email alerts when down |
| CPU Usage | DigitalOcean monitoring | ✅ | >80% | 🔄 Visible in DO dashboard | Auto-scale on DOKS |
| Memory Usage | DigitalOcean + Kubernetes | ✅ | >80% | 🔄 Visible in K8s dashboard | Pod restart on OOM |
| Database Connections | PostgreSQL query | ⬜ | >18/22 (Basic plan) | 🔄 Manual checks | Pooling helps extend limit |
| Storage Usage | DigitalOcean volumes | ✅ | >85% | 🔄 Monitored | Triggers scale-up alert |
| API Latency | AnythingLLM built-in | ⬜ | >5 seconds average | 🔄 Available in logs | Per-request in AnythingLLM debug |

### Alerting

| Alert Type | Condition | Notification Channel | Escalation | Status |
|---|---|---|---|---|
| **CRITICAL** | Instance down | @RMN (SMS + Signal) | @GTM (15 min) | ✅ Active |
| **HIGH** | CPU > 85% | @RMN (Signal notification) | Auto-scale + manual review | ✅ Active |
| **MEDIUM** | DB connections > 20 | @RMN (email) | Review connection pool config | 🔄 Manual checks |
| **LOW** | Storage > 80% | @RMN (weekly summary) | Plan scaling | 🔄 Trending |

---

## 📋 Backup & Disaster Recovery

### Backup Strategy

| Instance | Database Backup | Application Backup | Frequency | Retention | Test Schedule | Notes |
|----------|---|---|---|---|---|---|
| INT-P01 | DigitalOcean Managed PG | Docker volume snapshot (manual) | Daily (DB) | 30 days | Quarterly | Production mission-critical |
| INT-P02 | DigitalOcean Managed PG | DOKS persistent volume | Daily (DB) | 30 days | Quarterly | Project-critical |
| INT-P05 | DigitalOcean Managed PG Premium | DOKS + object storage | Hourly (DB) + Daily (app) | 60 days | Monthly | SaaS production; highest priority |

### Disaster Recovery Plan

| Scenario | RTO | RPO | Recovery Steps | Status |
|----------|-----|-----|---|---|
| **Database Corruption** | 1 hour | 24 hours | Restore from latest backup; test in staging first | 🔄 Planned |
| **Instance Failure** | 30 minutes | 1 hour | Redeploy from backup; point DNS to new instance | 🔄 Planned |
| **Data Loss** | 4 hours | 24 hours | Contact DO support; restore from DigitalOcean backups | 🔄 Documented |
| **Complete Outage** | 4 hours | 24 hours | Failover to secondary datacenter (if configured) | ⬜ Future |

### Backup Testing

| Instance | Last Test | Result | Next Test | Notes |
|----------|---|---|---|---|
| INT-P01 | — | — | 2026-Q2 | Restore plan documented |
| INT-P02 | — | — | 2026-Q2 | Restore plan documented |
| INT-P05 | — | — | 2026-Q1 | SaaS; monthly tests required |

---

## 📋 Cost & Billing

### Monthly Infrastructure Costs

| Resource | Instance(s) | Unit Cost | Qty | Monthly | Notes |
|----------|---|---|---|---|---|
| **Droplets** | INT-P01 | $? | 1 | $? | Compute baseline |
| **DOKS Cluster** | INT-P02, INT-P03, INT-P05 | $12-15 | 1 | $12-15 | Kubernetes management fee |
| **DOKS Nodes** | INT-P02, INT-P03, INT-P05 | $6-12 each | 2-3 nodes | $12-36 | Worker nodes (Standard size) |
| **PostgreSQL Basic** | INT-P01, INT-P02 | $15 | 2 | $30 | Managed database (basic tier) |
| **PostgreSQL Premium** | INT-P05 | $28-50 | 1 | $28-50 | Mission-critical SaaS tier |
| **Bandwidth** | All instances | $0.01/GB over 1TB | — | $10-50 | egress billing |
| **Backups** | All instances | Built-in | — | $0 | Included in managed DB pricing |
| **SSL Certificates** | All domains | $0 | — | $0 | Let's Encrypt free |
| **Domains** | ai.weown.agency, lite.burnedout.xyz, pro.weown.tools | $10-15/year | 3 | $2.50 | Annual registrar fees |
| **OpenRouter API** | All instances | Pay-per-token | — | $500-2000 | LLM inference costs (variable) |
| **GitHub** | fedarch repo | $0-21/month | — | $0 | Free tier (no private repos) |
| **Infisical** | Secrets management | $0-100+ | — | $0 (self-hosted) | Secret vaults |
| **Monitoring** | Uptime Robot, etc. | — | — | $0-50 | Optional uptime monitoring |
| **TOTAL ESTIMATED** | — | — | — | **$600-2300/month** | **[REFINE WITH ACTUAL COSTS]** |

### Cost Optimization Opportunities

| Opportunity | Potential Savings | Priority | Status |
|---|---|---|---|
| Consolidate DOKS nodes | $5-15/month | Low | Monitor usage first |
| Use reserved instances (DO) | 15-20% discount | Medium | Annual commitment needed |
| Optimize database plan (L-123) | $0-15/month | Medium | Connection pooling first |
| Batch API calls (LLM) | 10-20% savings | High | Depends on usage patterns |
| Cache LLM responses | 5-30% savings | Medium | Implement caching layer |

---

## 📋 Update & Maintenance Log

| Date | Instance | Change | Owner | CCC-ID | Status |
|------|----------|--------|-------|--------|--------|
| 2026-03-17 | ALL | 🚀 **INITIAL INVENTORY CREATED** | @CTO (Nik Cimino) | CTO_2026-W11_001 | ✅ Live |
| [ongoing] | [instance] | [document changes here] | @[owner] | CCC-ID | Status |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| **3.2.1.1** | **2026-W11** | **CTO_2026-W11_001** | **⬜ AWAITING HUMAN APPROVAL (R-011)** | **🚀 INITIAL RELEASE** — Complete living infrastructure inventory; aligned with governance framework (BP-025, BP-051, BP-059, BP-064); 12 sections covering instances, resources, networking, team, SLA, security, capacity, CI/CD, monitoring, backup, cost, and maintenance log; 10 active instances + 4 planning; standardized format for ongoing updates; NOTE: Many fields marked [POPULATE] or [DOCUMENT NEEDED] — to be filled in with actual current infrastructure data |

---

## 🔗 Related Documents

| Document | Version | Purpose | URL |
|---|---|---|---|
| SharedKernel | v3.2.2.1 | Instance definitions (D-053→D-057) + Elevated Registry | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/SharedKernel.md) |
| GUIDE-007 | v3.2.0.0 | How to maintain this inventory (procedures) | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_GUIDES_/GUIDE-007_Infrastructure-Inventory-Management.md) |
| TMPL-011 | v3.2.0.0 | Instance deployment checklist template | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_TEMPLATES_/TMPL-011_Instance-Deployment-Checklist.md) |
| BEST-PRACTICES | v3.1.3.1 | Instance setup (BP-025, BP-051), ISC (BP-059), API key rotation (BP-064) | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/BEST-PRACTICES.md) |
| PROTOCOLS | v3.1.3.1 | Document management + weekly operations | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/PROTOCOLS.md) |
| GUIDE-006 | v3.1.1.1 | GitHub RAG connector setup + API key management | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_GUIDES_/GUIDE-006_GitHub-PAT-for-AnythingLLM.md) |

---

#FlowsBros #FedArch #Infrastructure #InstanceInventory #WeOwnSeason003 #LivingDocument

♾️ WeOwnNet 🌐 ● 🏡 Real estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
