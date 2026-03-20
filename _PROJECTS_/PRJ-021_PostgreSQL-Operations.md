# PRJ-021_PostgreSQL-Operations.md

## 📋 Document Metadata

| Field | Value |
|-------|-------|
| **Document** | PRJ-021_PostgreSQL-Operations.md |
| **Version** | **v3.2.3.1** |
| **CCC-ID** | RMN_2026-W12_063 |
| **Approval CCC-ID** | GTM_2026-W10_026 |
| **Created** | 2026-W12 |
| **Updated** | **2026-03-19 (W12)** |
| **Season** | #WeOwnSeason003 🚀 |
| **Status** | 🔄 IN PROGRESS |
| **#LLMmodel** | Qwen3.5-397B-A17B |
| **Source of Truth** | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-021_PostgreSQL-Operations.md) |
| **R-199** | Database credentials = RAG ONLY, NEVER GitHub |

---

## 📖 Table of Contents

1. [Project Identity](#-project-identity)
2. [Executive Summary](#-executive-summary)
3. [PostgreSQL Cluster — Full Specification](#-postgresql-cluster--full-specification)
4. [Connection Scenarios — GUIDE-010 Compliant](#-connection-scenarios--guide-010-compliant)
5. [Trusted Sources Configuration (P0 Task)](#-trusted-sources-configuration-p0-task)
6. [Connection Pool (PgBouncer) — P1 Task](#-connection-pool-pgbouncer--p1-task)
7. [pgAdmin Deployment — jAIMSnet DOKS Cluster](#-pgadmin-deployment--jaimsnet-doks-cluster)
8. [jAIMSnet Integration (PRJ-025)](#-jaimsnet-integration-prj-025)
9. [Database Users + Roles](#-database-users--roles)
10. [P0 Tasks — Critical](#-p0-tasks--critical)
11. [P1 Tasks — Important](#-p1-tasks--important)
12. [P2 Tasks — Nice to Have](#-p2-tasks--nice-to-have)
13. [Learnings Locked (PRJ-021)](#-learnings-locked-prj-021)
14. [Related PRJs](#-related-prjs)
15. [Version History](#-version-history)
16. [Related Documents](#-related-documents)
17. [Discovered By (BP-047)](#-discovered-by-bp-047)
18. [Governance Compliance](#-governance-compliance)

---

## 📋 Project Identity

| Field | Value |
|-------|-------|
| Project ID | **PRJ-021** |
| Title | **PostgreSQL Operations** |
| Type | Infrastructure — Database Operations |
| Priority | 🔴 P0 |
| Owner | @RMN (Roman Di Domizio) |
| Backend | DO Managed PostgreSQL (db-postgresql-atl1-weownnet) |
| Interface | pgAdmin (jAIMSnet DOKS), SQL Agent, Direct Connection |
| Timeline | **W07-W12** |
| #masterCCC | GTM_2026-W10_026 |
| Approval CCC-ID | GTM_2026-W10_026 |

---

## 📋 Executive Summary

### What Is PRJ-021?

PRJ-021 encompasses all PostgreSQL cluster operations for the ♾️ WeOwnNet 🌐 ecosystem, including:

- **PostgreSQL Cluster Management** — db-postgresql-atl1-weownnet (DO Managed PG)
- **Trusted Sources Configuration** — Secure access control for cross-team connections (GUIDE-010)
- **Connection Pooling** — PgBouncer for scaling connections (22 → 100+)
- **Cross-Team Connectivity** — Academy ↔ Labs secure connections (GUIDE-010)
- **Database UI** — pgAdmin deployment in jAIMSnet DOKS cluster for visual database management
- **Monitoring** — Connection health, performance, backup verification

### DO Project Migration

| Field | Before | After |
|-------|--------|-------|
| **DO Project** | ♾️ WeOwn.Dev 💻 | **♾️ WeOwnNet 🌐** |
| **Reason** | Initial dev project | Aligned with ecosystem branding |
| **Impact** | None — cluster unchanged | Better org alignment |
| **Migration Date** | — | W10-W11 |

### Why This Matters

| Without PRJ-021 | With PRJ-021 |
|-----------------|--------------|
| Ad-hoc DB access, security gaps | ✅ Trusted Sources, role-based access (GUIDE-010) |
| Connection limits (22 max) | ✅ PgBouncer pool (100+ effective) |
| Manual connection management | ✅ Documented scenarios per team/location |
| No database UI | ✅ pgAdmin in jAIMSnet DOKS cluster |
| No monitoring | ✅ Connection health checks, alerts |

### Current Status

| Metric | Value |
|--------|-------|
| **Completion** | 40% |
| **P0 Tasks** | 8 tasks — ⬜ TODO |
| **P1 Tasks** | 7 tasks — ⬜ TODO |
| **P2 Tasks** | 3 tasks — ⬜ TODO |
| **Deployed** | W07 (Mon 02 Feb 2026) |
| **Deployed By** | @RMN (P-009/PRJ-021) |

---

## 📋 PostgreSQL Cluster — Full Specification

### Cluster Identity

| Field | Value |
|-------|-------|
| **Cluster Name** | db-postgresql-atl1-weownnet |
| **Engine** | PostgreSQL v18 |
| **Plan** | Basic Premium AMD NVMe — $15/mo |
| **vCPU** | 1 |
| **RAM** | 1 GB |
| **Connections** | 22 (→ 100+ with PgBouncer) |
| **Storage** | 15 GiB NVMe (autoscale → 75 GiB @ 80% threshold) |
| **Port** | 25060 (SSL), 25061 (pool — when created) |
| **Cost** | $18.23/mo ($15 compute + $3.23 storage) |
| **Datacenter** | ATL1 (Atlanta) |
| **DO Team** | We Own Labs |
| **DO Project** | **♾️ WeOwnNet 🌐** (moved from ♾️ WeOwn.Dev 💻) |
| **Deployed** | Mon 02 Feb 2026 (W07) |

### Storage Details

| Metric | Value |
|--------|-------|
| **Current Usage** | ~50-100 MB (estimated) |
| **Autoscale Threshold** | 80% (12 GiB) |
| **Max Autoscale** | 75 GiB |
| **Storage Type** | NVMe (only option in ATL1 — L-122) |
| **I/O Performance** | 2-3x faster than regular SSD |

### Connection Limits

| Metric | Value |
|--------|-------|
| **Default Connections** | 22 |
| **With PgBouncer** | 100+ effective |
| **Pool Mode** | Transaction (recommended) |
| **Pool Size** | 15 |

---

## 📋 Connection Scenarios — GUIDE-010 Compliant

### Team Architecture

| Team | Components | DC |
|------|------------|-----|
| **We Own Labs** | db-postgresql-atl1-weownnet, INT-P01 (DOKS), jAIMSnet DOKS cluster | ATL1 |
| **We Own Academy** | INT-OG1 (DOKS), INT-OG8 (DOKS), INT-P02 (Droplet), n8n (DOKS) | ATL1 |

### Connection Matrix (GUIDE-010)

| From Component | Team | To PG Cluster | Method | Cost | Latency |
|----------------|------|---------------|--------|------|---------|
| **INT-P01** | We Own Labs | Labs→Labs | VPC Private IP | FREE | <1ms |
| **jAIMSnet DOKS** | We Own Labs | Labs→Labs | VPC Private IP | FREE | <1ms |
| **INT-OG8** | We Own Academy | Academy→Labs | Public + Trusted Sources + SSL | $0.01/GiB | 2-5ms |
| **INT-OG1** | We Own Academy | Academy→Labs | Public + Trusted Sources + SSL | $0.01/GiB | 2-5ms |
| **INT-P02** | We Own Academy | Academy→Labs | Public + Trusted Sources + SSL | $0.01/GiB | 2-5ms |
| **n8n** | We Own Academy | Academy→Labs | Public + Trusted Sources + SSL | $0.01/GiB | 2-5ms |
| **pgAdmin** | We Own Labs (jAIMSnet) | Labs→Labs | VPC Private IP | FREE | <1ms |

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

## 📋 Trusted Sources Configuration (P0 Task)

### What Are Trusted Sources?

Trusted Sources is a DO Managed PostgreSQL security feature that whitelists specific IPs/resources allowed to connect to the database. Without configuration, ALL IPs are allowed (security risk).

### Current Status

| Field | Value |
|-------|-------|
| **Status** | ⚠️ EMPTY — all IPs currently allowed |
| **Risk Level** | 🔴 HIGH — security vulnerability |
| **Priority** | 🔴 P0 — blocks PRJ-018, PRJ-020, PRJ-023 |

### Resources to Add

| Resource | IP/Type | Team | Status |
|----------|---------|------|--------|
| **n8n pod (DOKS Academy)** | Dynamic (DOKS egress IP range) | We Own Academy | ⬜ TODO |
| **INT-OG8 (DOKS Academy)** | Dynamic (DOKS egress IP range) | We Own Academy | ⬜ TODO |
| **INT-OG1 (DOKS Academy)** | Dynamic (DOKS egress IP range) | We Own Academy | ⬜ TODO |
| **INT-P02 (Droplet Academy)** | Static Droplet IP | We Own Academy | ⬜ TODO |
| **jAIMSnet DOKS cluster** | Same VPC — auto-trusted | We Own Labs | ✅ Auto |
| **INT-P01 (DOKS Labs)** | Same VPC — auto-trusted | We Own Labs | ✅ Auto |

### DOKS Egress IP Challenge

| Challenge | Solution |
|-----------|----------|
| DOKS pods have dynamic egress IPs | Use DO's DOKS egress IP range for ATL1 |
| IPs can change on pod restart | Document range, monitor for changes |
| Alternative: NAT Gateway | More expensive, not needed at current scale |

### Configuration Steps (GUIDE-010)

| # | Step | Action | Est. Time |
|---|------|--------|:---------:|
| 1 | Open DO Console | Navigate to PostgreSQL cluster | 0.5 min |
| 2 | Go to Connections | Click "Trusted Sources" tab | 0.5 min |
| 3 | Add DOKS Academy Range | Add ATL1 DOKS egress IP range | 1 min |
| 4 | Add INT-P02 Droplet IP | Add static Droplet IP | 0.5 min |
| 5 | Save Changes | Click "Save" | 0.5 min |
| 6 | Verify | Test connection from n8n pod | 2 min |
| **TOTAL** | | | **5 min** |

---

## 📋 Connection Pool (PgBouncer) — P1 Task

### Why PgBouncer?

| Problem | Solution |
|---------|----------|
| 22 connection limit | PgBouncer pools connections → 100+ effective |
| Connection overhead | Reuse existing connections |
| Multiple consumers | n8n + INT-OG8 + INT-OG1 + INT-P02 + pgAdmin + jAIMSnet services = 6+ |

### Recommended Configuration

| Field | Value |
|-------|-------|
| **Mode** | Transaction (recommended for most workloads) |
| **Pool Size** | 15 |
| **Port** | 25061 |
| **When to Enable** | 3+ concurrent consumers |
| **DO Managed** | Yes — DO provides built-in PgBouncer |

### Connection Pool Benefits

| Metric | Without Pool | With Pool |
|--------|--------------|-----------|
| Max Connections | 22 | 100+ |
| Connection Overhead | High (new per request) | Low (reused) |
| Consumer Limit | ~5 apps | ~20+ apps |
| Performance | Degrades at limit | Stable |

---

## 📋 pgAdmin Deployment — jAIMSnet DOKS Cluster

### What Is pgAdmin?

| Field | Value |
|-------|-------|
| **Name** | pgAdmin 4 |
| **Type** | Web-based PostgreSQL administration |
| **License** | PostgreSQL License (FOSS) |
| **Features** | Query tool, ERD, backup/restore, user management, monitoring |
| **URL** | [pgadmin.org](https://www.pgadmin.org/) |

### Why pgAdmin in jAIMSnet Cluster?

| Use Case | Value |
|----------|-------|
| Visual schema browsing | See all tables, relationships, indexes |
| Query development | Write + test SQL with autocomplete |
| User/role management | Create users, grant permissions visually |
| Backup/restore | GUI for PITR, exports |
| Performance monitoring | Live query stats, locks, connections |
| PRJ-018/020/023 work | Essential for schema development + data verification |

### Deployment Decision

| Option | Where | Pros | Cons | Recommendation |
|--------|-------|------|------|----------------|
| **A: jAIMSnet DOKS Cluster** | ATL1 (same VPC as PG) | Native K8s, shared LB, auto-SSL, VPC private | Requires K8s config | ✅ **RECOMMENDED** |
| B: DO App Platform | DO managed | Easy deploy, auto-SSL | More expensive (~$5-10/mo) | 🟡 Alternative |
| C: Local install | @RMN laptop | Free, immediate | Not shared, security risk | ❌ Not recommended |
| D: DO Marketplace | One-click Droplet | Easy | Separate Droplet cost ($6-12/mo) | ❌ jAIMSnet is DOKS now |

### Recommended Deployment (Option A)

| Field | Value |
|-------|-------|
| **Host** | jAIMSnet DOKS cluster (ATL1) |
| **Method** | Kubernetes Deployment + Helm |
| **Image** | `dpage/pgadmin4:latest` |
| **Namespace** | `observability` (jAIMSnet) |
| **Port** | 5050 (internal), 443 via ingress-nginx + cert-manager |
| **Domain** | pgadmin.jAIMS.app |
| **SSL** | cert-manager auto-SSL (Let's Encrypt) |
| **Auth** | pgAdmin master password + DO PG credentials |
| **Connection** | VPC Private IP to PG cluster (FREE, <1ms) |

### Kubernetes Deployment (jAIMSnet Cluster)

```yaml
# observability/pgadmin-deployment.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: pgadmin
  namespace: observability
  labels:
    app: pgadmin
    jaimsnet.component: observability
spec:
  replicas: 1
  selector:
    matchLabels:
      app: pgadmin
  template:
    metadata:
      labels:
        app: pgadmin
    spec:
      containers:
      - name: pgadmin
        image: dpage/pgadmin4:latest
        ports:
        - containerPort: 80
        env:
        - name: PGADMIN_DEFAULT_EMAIL
          value: roman@weown.email
        - name: PGADMIN_DEFAULT_PASSWORD
          valueFrom:
            secretKeyRef:
              name: pgadmin-secret
              key: password
        - name: PGADMIN_CONFIG_SERVER_MODE
          value: "False"
        - name: PGADMIN_CONFIG_MASTER_PASSWORD_REQUIRED
          value: "False"
        volumeMounts:
        - name: pgadmin-data
          mountPath: /var/lib/pgadmin
      volumes:
      - name: pgadmin-data
        persistentVolumeClaim:
          claimName: pgadmin-pvc

---

apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: pgadmin-ingress
  namespace: observability
  annotations:
    cert-manager.io/cluster-issuer: "jaimsnet-cluster-issuer"
spec:
  rules:
  - host: pgadmin.jAIMS.app
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: pgadmin-service
            port:
              number: 80
```

### Security Considerations

| Concern | Mitigation |
|---------|------------|
| Web access to DB admin | Restrict to known IPs (Cloudflare Access or DO firewall) |
| Master password | Store in Infisical Operator (PRJ-024) → K8s Secret |
| PG credentials | Store in Infisical Operator, sync to K8s Secret |
| Audit logging | Enable pgAdmin audit logs |
| Session timeout | Configure 30-min idle timeout |
| Namespace isolation | Deploy in `observability` namespace with NetworkPolicy |

### Recommended Access Control

| User | Access Level | Use Case |
|------|--------------|----------|
| @RMN | Superuser | Full admin, schema changes, user management |
| @GTM | Read-Write | Query data, verify PRJ-018/020 data |
| @LDC | Read-Write | PRJ-023 context pipeline development |
| @THY | Read-Only | Financial oversight, intern data review |

### pgAdmin Server Registration

| Field | Value |
|-------|-------|
| **Host** | db-postgresql-atl1-weownnet-private (VPC IP) |
| **Port** | 25060 (SSL) |
| **Database** | defaultdb (initial), then pop_db, cccid_db, etc. |
| **Username** | doadmin (admin), p012_app (limited) |
| **SSL Mode** | Require |
| **SSL CA** | DO PostgreSQL CA certificate |

---

## 📋 jAIMSnet Integration (PRJ-025)

### jAIMSnet Architecture Summary

| Component | Detail |
|-----------|--------|
| **Cluster** | jaimsnet-cluster · DOKS · ATL1 · K8s 1.34.1 |
| **Load Balancer** | 129.212.240.75 · ATL1 |
| **Ingress** | ingress-nginx + cert-manager (auto-TLS) |
| **Phase 1 Services** | LiteLLM, Langfuse, Redis, Infisical Operator, pgAdmin |
| **Phase 2 Services** | Prometheus, Grafana, Loki, vLLM on MI300X |
| **Cost** | ~$57/mo (Phase 1) |

### PostgreSQL Integration with jAIMSnet

| Service | PG Usage | Connection Method | Notes |
|---------|----------|-------------------|-------|
| **LiteLLM** | Spend tracking, virtual keys, budgets | VPC Private IP (same team) | PRJ-016 |
| **Langfuse** | Trace storage, evals, sessions | VPC Private IP (same team) | PRJ-017 |
| **pgAdmin** | Visual DB management | VPC Private IP (same team) | This PRJ |
| **Future: CCC-ID Registry** | CCC-ID ledger | VPC Private IP (same team) | PRJ-028 |

### jAIMSnet Namespaces (Relevant to PRJ-021)

| Namespace | Services | PG Connection |
|-----------|----------|---------------|
| `gateway` | LiteLLM, Redis | ✅ VPC Private IP |
| `observability` | Langfuse, pgAdmin, Prometheus, Grafana, Loki | ✅ VPC Private IP |
| `secrets` | Infisical Operator | ✅ VPC Private IP (for PG creds) |
| `gpu` | vLLM (Phase 2) | ✅ VPC Private IP |
| `automation` | Semaphore (PRJ-035) | ✅ VPC Private IP |

### Infisical Operator Integration

| Field | Value |
|-------|-------|
| **Tool** | Infisical Operator (K8s) |
| **Purpose** | Sync secrets from Infisical Cloud → K8s Secrets |
| **PG Credentials** | Stored in Infisical, synced to K8s Secret |
| **Access** | Pods reference K8s Secret (not env vars) |
| **Rotation** | Automatic (when Infisical fixed — PRJ-024) |

### Uptime Kuma (Separate Droplet — NYC1)

| Field | Value |
|-------|-------|
| **Deployment** | Standalone DO Droplet (Basic, ~$6/mo) |
| **Location** | NYC1 (separate from ATL1 cluster) |
| **Purpose** | Endpoint monitoring for all jAIMSnet services + PG cluster |
| **Monitors** | litellm.jAIMS.app, langfuse.jAIMS.app, pgadmin.jAIMS.app, PG cluster health |
| **Integration** | Not in jAIMSnet cluster — standalone for resilience |

### Why Separate Droplet for Kuma?

| Reason | Detail |
|--------|--------|
| **Resilience** | If jAIMSnet cluster fails, Kuma still monitors |
| **Independence** | Kuma can monitor cluster health externally |
| **Cost** | ~$6/mo Droplet vs. cluster resources |
| **Location** | NYC1 provides geographic diversity from ATL1 |

---

## 📋 Database Users + Roles

### Current Users

| User | Purpose | Permissions | Status |
|------|---------|-------------|--------|
| **doadmin** | DO admin user | Full superuser | ✅ Active |
| **defaultdb** | Default database | — | ✅ Active |

### Planned Users

| User | Purpose | Permissions | PRJ | Status |
|------|---------|-------------|-----|--------|
| **p012_app** | PRJ-020 intern eval pipeline | SELECT, INSERT on interns schema | PRJ-020 | ⬜ TODO |
| **cccid_app** | CCC-ID registry API | SELECT, INSERT on cccid schema | PRJ-028 | ⬜ TODO |
| **langfuse_app** | Langfuse observability | SELECT, INSERT on langfuse schema | PRJ-017 | ⬜ TODO |
| **litellm_app** | LiteLLM gateway | SELECT, INSERT on litellm schema | PRJ-016 | ⬜ TODO |
| **pgadmin_user** | pgAdmin read-only | SELECT on all schemas | pgAdmin | ⬜ TODO |

### p012_app User (PRJ-020)

```sql
-- CREATE USER
CREATE USER p012_app WITH PASSWORD '****';

-- GRANT CONNECTION
GRANT CONNECT ON DATABASE defaultdb TO p012_app;

-- GRANT SCHEMA ACCESS
GRANT USAGE ON SCHEMA public TO p012_app;

-- GRANT TABLE ACCESS (PRJ-020 interns schema)
GRANT SELECT, INSERT ON ALL TABLES IN SCHEMA public TO p012_app;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO p012_app;

-- NO UPDATE, NO DELETE — intern data is immutable once registered
```

### Principle of Least Privilege

| Principle | Application |
|-----------|-------------|
| Minimum permissions | Each user gets only what they need |
| No UPDATE/DELETE | Audit trail preserved (append-only where possible) |
| Schema isolation | Each app has own schema when possible |
| Credential rotation | Infisical Operator manages secrets (PRJ-024) |

---

## 📋 P0 Tasks — Critical

| # | Task | Action | Status | Blocks |
|---|------|--------|--------|--------|
| 1 | Configure Trusted Sources | Add n8n, INT-OG8, INT-OG1, INT-P02, jAIMSnet IPs | ⬜ TODO | PRJ-018, PRJ-020, PRJ-023 |
| 2 | Download SSL CA certificate | DO PG Console → Download CA | ⬜ TODO | All SSL connections |
| 3 | Test connection from n8n pod | Verify connectivity | ⬜ TODO | PRJ-020, PRJ-023 |
| 4 | CREATE EXTENSION citext | `CREATE EXTENSION IF NOT EXISTS citext;` | ⬜ TODO | PRJ-020 schema |
| 5 | CREATE USER p012_app + GRANT | Limited permissions for PRJ-020 | ⬜ TODO | PRJ-020 |
| 6 | Run PRJ-020 schema (5 tables) | Execute CREATE TABLE statements | ⬜ TODO | PRJ-020 |
| 7 | Store p012_app creds in Infisical | Manual until PRJ-024 fixed | ⬜ TODO | PRJ-024 |
| 8 | Verify n8n can connect as p012_app | Test INSERT/SELECT | ⬜ TODO | PRJ-020 |

---

## 📋 P1 Tasks — Important

| # | Task | Action | Status |
|---|------|--------|--------|
| 9 | Add INT-P01 as Trusted Source | Same team — auto-updates | ⬜ TODO |
| 10 | Add INT-P02 Droplet | Add Droplet directly | ⬜ TODO |
| 11 | Add INT-OG1 IPs | Get from @GTM | ⬜ TODO |
| 12 | Create connection pool (PgBouncer) | Transaction mode, size 15 | ⬜ TODO |
| 13 | Test pool connection (port 25061) | Verify PgBouncer works | ⬜ TODO |
| 14 | Set up n8n monitoring cron | Connection health checks | ⬜ TODO |
| 15 | Document all Trusted Sources | Table of IPs/resources | ⬜ TODO |

---

## 📋 P2 Tasks — Nice to Have

| # | Task | Action | Status |
|---|------|--------|--------|
| 16 | VPC peering evaluation | Confirm DO doesn't support cross-team | ⬜ TODO |
| 17 | NYC3 fallback migration plan | Disaster recovery planning | ⬜ TODO |
| 18 | Test PITR (Point-in-Time Recovery) | Backup verification | ⬜ TODO |

---

## 📋 Learnings Locked (PRJ-021)

| ID | Learning | Detail | Source |
|----|----------|--------|--------|
| **L-122** | ATL1 disk-type limitation | Regular SSD unavailable in ATL1, NVMe only (+$2/mo, 2-3x faster I/O) | P-009 |
| **L-123** | Inter-team VPC not supported | DO doesn't support VPC peering across teams. Academy→Labs = Public + Trusted Sources only | P-009 |
| **L-124** | No downgrade path | DO Managed PG: can upgrade plan, cannot downgrade | P-009 |
| **L-125** | PgBouncer extends connections | 22 connections → 100+ with PgBouncer connection pool (Transaction mode) | P-009 |

---

## 📋 Related PRJs

| PRJ | Title | Relationship |
|-----|-------|--------------|
| **PRJ-016** | LiteLLM AI Gateway | Uses PG for spend tracking, virtual keys (jAIMSnet `gateway` namespace) |
| **PRJ-017** | Observability (Langfuse) | Uses PG for trace storage (jAIMSnet `observability` namespace) |
| **PRJ-018** | P.O.P. Database | Primary schema — people, orgs, places, interns |
| **PRJ-020** | Interns Co-op Pipeline | Data stored in POP DB (5 tables) |
| **PRJ-023** | Context Persistence Pipeline | Chat history → PG → RAG |
| **PRJ-024** | Secrets Management (Infisical) | PG credentials stored in Infisical Operator |
| **PRJ-025** | jAIMSnet Platform Engineering | DOKS cluster hosting LiteLLM, Langfuse, pgAdmin |
| **PRJ-028** | CCC-ID Registry | Separate DB on same cluster (cccid_db) |
| **PRJ-035** | Semaphore Automation | Deploys to jAIMSnet DOKS (`automation` namespace) |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| **3.2.3.1** | **2026-W12** | **GTM_2026-W10_026** | **GTM_2026-W10_026** | **Initial document creation — PRJ-021 PostgreSQL Operations. Cluster specification (PG v18, NVMe 15 GiB, $18.23/mo, ATL1), connection scenarios (GUIDE-010 compliant, Labs→Labs vs Academy→Labs), Trusted Sources configuration (P0, currently EMPTY — security risk), PgBouncer pool plan (22→100+ connections, Transaction mode), pgAdmin deployment (jAIMSnet DOKS, observability namespace, K8s YAML), jAIMSnet integration (PRJ-025, 5 namespaces including automation for PRJ-035 Semaphore), database users/roles (p012_app, litellm_app, langfuse_app, cccid_app, pgadmin_user), P0/P1/P2 task registry (8+7+3 tasks), learnings locked (L-122/123/124/125), DO project migration (WeOwn.Dev → WeOwnNet W10-W11), Uptime Kuma NYC1 Droplet (separate for resilience), principle of least privilege, R-199 compliance** |

---

## 📋 Related Documents

| Document | Version | #masterCCC | Approval | Location |
|----------|---------|------------|----------|----------|
| PRJ-018_POP-Database.md | 3.2.3.1 | GTM_2026-W10_026 | GTM_2026-W11_308 | _PROJECTS_/ |
| PRJ-020_Interns-Co-op-Candidate-Pipeline.md | 3.2.3.1 | GTM_2026-W10_026 | GTM_2026-W11_318 | _PROJECTS_/ |
| PRJ-025_jAIMSnet-Platform-Engineering.md | 3.2.3.1 | GTM_2026-W10_026 | ⬜ AWAITING | _PROJECTS_/ |
| GUIDE-010_PostgreSQL-Setup.md | 3.2.1.1 | GTM_2026-W10_026 | GTM_2026-W10_073 | _GUIDES_/ |
| GUIDE-011_Governance-Oversight-VSA-Process.md | 3.2.1.1 | GTM_2026-W10_066 | GTM_2026-W10_073 | _GUIDES_/ |

---

## 📋 Discovered By (BP-047)

| CCC | Contributor | Role | Context |
|-----|-------------|------|---------|
| RMN | Roman Di Domizio | AI Platform Engineer | Deployed PostgreSQL cluster (W07), designed Trusted Sources architecture (GUIDE-010), pgAdmin deployment plan (jAIMSnet DOKS), P0/P1/P2 task registry |
| GTM | Jason Younker | Co-Founder | Approved PRJ assignment (GTM_2026-W10_026), DO team structure (Labs + Academy), jAIMSnet DOKS cluster decision |
| THY | Tyler Younker | CFO | Approved PostgreSQL budget ($18.23/mo) |

---

## 📋 Governance Compliance

| Requirement | Status |
|-------------|--------|
| #masterCCC | ✅ GTM_2026-W10_026 |
| Approval CCC-ID | ✅ GTM_2026-W10_026 |
| Version History | ✅ Included |
| Related Documents | ✅ Included |
| Discovered By (BP-047) | ✅ Included |
| Lifecycle Stage | 🔄 IN PROGRESS |
| VSA Eligibility | ✅ FULL or DEEP FULL (at APPROVED+ stage) |
| GUIDE-011 | ✅ APPROVED — compensation eligible |
| R-199 (Credential Protection) | ✅ Database credentials = RAG ONLY, NEVER GitHub |

---

#FlowsBros #FedArch #PRJ-021 #PostgreSQL #jAIMSnet #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
