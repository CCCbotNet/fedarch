# GUIDE-010: PostgreSQL Database Connections

## 📋 GUIDE-010_PostgreSQL-Database-Connections_v3.1.3.1.md
## ♾️ WeOwnNet 🌐

| Field | Value |
|-------|-------|
| Document | GUIDE-010_PostgreSQL-Database-Connections.md |
| Version | 3.1.3.1 |
| CCC-ID | RMN_2026-W08_021 |
| Created | 2026-02-15 (W07) |
| Season | #WeOwnSeason003 🚀 |
| Status | 🔒 LOCKED |
| Audience | @RMN, @SHD, @LDC, @GTM |
| Tags | #PostgreSQL #DigitalOcean #Infrastructure |

---

## 📖 Table of Contents

1. [Database Overview](#-section-1-database-overview)
2. [Connection Scenarios](#-section-2-connection-scenarios)
3. [Connection Methods Deep Dive](#-section-3-connection-methods-deep-dive)
4. [Autoscale Storage](#-section-4-autoscale-storage)
5. [Connection Monitoring + Upgrade Triggers](#-section-5-connection-monitoring--upgrade-triggers)
6. [Upgrade Process](#-section-6-upgrade-process)
7. [Connection Pools](#-section-7-connection-pools)
8. [Network Access](#-section-8-network-access)
9. [Quick Reference Card](#-section-9-quick-reference-card)
10. [Related Documents](#-related-documents)
11. [Version History](#-version-history)

---

## 📋 Section 1: Database Overview

### 1A: Cluster Specifications

| Field | Value |
|-------|-------|
| Engine | PostgreSQL |
| Version | **v18** |
| Plan | Basic Premium AMD — $15/mo |
| CPU | 1 vCPU |
| RAM | 1 GB |
| Disk Type | NVMe |
| Storage | 15 GiB (autoscale enabled) |
| Connection Limit | **22** |
| Datacenter | **ATL1** (Atlanta) |
| VPC | default-atl1 |
| DO Team | **We Own Labs** |
| DO Project | **♾️ WeOwn.Dev 💻** |
| Cluster Name | **db-postgresql-atl1-weownnet** |
| Host | `db-postgresql-atl1-weownnet-do-user-XXXXXXX-0.g.db.ondigitalocean.com` |
| Port | **25060** (SSL) |
| Default Database | `defaultdb` |
| Default User | `doadmin` |
| Deployed | Mon 02 Feb 2026 |
| Deployed By | @RMN |

### 1B: What Is a DigitalOcean Managed Database?

A **Managed Database** is a fully-managed database service where DigitalOcean handles the infrastructure operations so your team can focus on building applications.

#### What DigitalOcean Manages FOR You

| Responsibility | Detail |
|----------------|--------|
| **Automated Backups** | Daily backups retained for 7 days (Basic plan) |
| **Failover** | Automatic failover for HA plans (not Basic — single node) |
| **Maintenance Windows** | Automated engine patches and security updates |
| **Point-in-Time Recovery** | Restore to any point within backup window |
| **OS Patching** | Underlying OS kept current |
| **Engine Upgrades** | PostgreSQL minor version upgrades applied automatically |
| **Monitoring** | Built-in metrics dashboard (CPU, RAM, disk, connections) |
| **SSL/TLS** | Enforced on all connections — certificates managed |

#### What YOUR TEAM Is Responsible For

| Responsibility | Detail |
|----------------|--------|
| **Connection Management** | Monitor and manage the 22-connection limit |
| **Query Optimization** | Write efficient queries, use indexes |
| **Schema Design** | Tables, relationships, migrations |
| **Access Control** | Users, roles, permissions, Trusted Sources |
| **Monitoring** | Set up alerts, respond to threshold warnings |
| **Connection Pooling** | Configure pools if needed (Section 7) |
| **Backup Verification** | Periodically test restore from backup |
| **Application Config** | Connection strings, retry logic, SSL certs |

### 1C: Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│  DigitalOcean — ATL1 (Atlanta)                                  │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  VPC: default-atl1 (Private Network)                     │   │
│  │                                                           │   │
│  │  ┌─────────────────────┐   ┌──────────────────────────┐  │   │
│  │  │  PostgreSQL v18     │   │  DOKS Cluster            │  │   │
│  │  │  db-postgresql-     │◄──│  (Kubernetes)             │  │   │
│  │  │  atl1-weownnet      │   │  Apps connect via         │  │   │
│  │  │                     │   │  Private IP (<1ms)        │  │   │
│  │  │  Primary Node       │   └──────────────────────────┘  │   │
│  │  │  1 vCPU / 1 GB RAM  │                                 │   │
│  │  │  22 connections     │   ┌──────────────────────────┐  │   │
│  │  │  Port: 25060 (SSL)  │◄──│  Droplets (ATL1)         │  │   │
│  │  │                     │   │  Connect via              │  │   │
│  │  │  Private IP: 10.x.x │   │  Private IP (<1ms)        │  │   │
│  │  │  Public IP: x.x.x.x│   └──────────────────────────┘  │   │
│  │  └─────────────────────┘                                 │   │
│  └──────────────────────────────────────────────────────────┘   │
│                          │                                       │
│                          │ Public Endpoint                       │
│                          │ (SSL enforced)                        │
│                          ▼                                       │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  Internet / Other DCs / Other DO Teams                   │   │
│  │  Connect via Public IP + Trusted Sources                 │   │
│  │  Latency: 2-50ms depending on location                   │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

### 1D: Primary Node vs Read-Only Replicas

| Aspect | Primary Node | Read-Only Replica |
|--------|-------------|-------------------|
| Read queries | ✅ | ✅ |
| Write queries | ✅ | ❌ |
| Connection limit | 22 (shared) | Separate pool |
| Cost | Included in plan | Additional cost |
| Use case | All operations | Read-heavy scaling |
| Current config | **✅ Active** | ❌ Not deployed |

#### When to Add a Read-Only Replica

| Signal | Action |
|--------|--------|
| Read queries consuming >60% of connections | Consider replica |
| Application has clear read/write separation | Good candidate |
| Reporting/analytics queries slowing production | Offload to replica |
| Connection limit hit but mostly reads | Replica before upgrade |

> **Current state:** Primary only. At 22 connections, consider connection pooling (Section 7) BEFORE adding a replica. Replica adds cost; pooling is free.

### 1E: Maintenance Window

| Field | Value |
|-------|-------|
| Default | Sunday 00:00-04:00 UTC |
| What happens | Minor patches, security updates applied |
| Downtime | Brief (seconds to minutes) |
| Notification | DO sends email 24h before scheduled maintenance |

#### How to Change Maintenance Window

| Step | Action |
|------|--------|
| 1 | Navigate to: Databases → db-postgresql-atl1-weownnet → Settings |
| 2 | Find "Maintenance Window" section |
| 3 | Select preferred day + time |
| 4 | Click "Save" |

#### Best Practices

| Practice | Detail |
|----------|--------|
| Schedule during low traffic | Choose lowest-usage period |
| Notify team | Share maintenance window with all developers |
| Test retry logic | Apps should handle brief disconnects |
| Monitor after maintenance | Check connections + performance post-window |

---

## 📋 Section 2: Connection Scenarios

### Scenario Decision Matrix

```
                        ┌─────────────────────┐
                        │  Where is your       │
                        │  resource?            │
                        └──────────┬────────────┘
                                   │
                    ┌──────────────┼──────────────┐
                    │              │              │
              Same DO Team    Same DO Team   Different DO Team
              Same DC (ATL1)  Diff DC        (Any DC)
                    │              │              │
                    ▼              ▼              ▼
              ┌──────────┐  ┌──────────┐  ┌──────────────┐
              │ Scenario 1│  │ Scenario 2│  │ Scenario 3/4 │
              │ VPC       │  │ VPC       │  │ Public       │
              │ Private IP│  │ Peering   │  │ Endpoint     │
              │ FREE      │  │ $0.01/GiB │  │ $0.01/GiB    │
              │ <1ms      │  │ 15-50ms   │  │ 2-50ms       │
              └──────────┘  └──────────┘  └──────────────┘
```

### Scenario Comparison

| Field | Scenario 1 | Scenario 2 | Scenario 3 | Scenario 4 |
|-------|-----------|-----------|-----------|----------|
| **Location** | Same Team + Same DC | Same Team + Diff DC | Diff Team + Same DC | Diff Team + Diff DC |
| **Method** | VPC (Private IP) | VPC Peering | Public + Trusted Sources | Public + Trusted Sources |
| **Cost** | **FREE** | $0.01/GiB | $0.01/GiB | $0.01/GiB |
| **Latency** | **<1ms** | 15-50ms | 2-5ms | 15-50ms |
| **Security** | Excellent | Good | Good | Good |
| **Complexity** | Low | Medium | Medium | Medium |
| **Recommended** | ✅ **BEST** | ✅ Good | 🟡 Acceptable | ⚠️ Avoid if possible |

---

### Scenario 1: Same DO Team + Same Datacenter (ATL1 → ATL1)

#### When This Applies

| Condition | Value |
|-----------|-------|
| Resource DO Team | Same as database |
| Resource Datacenter | ATL1 |
| Examples | DOKS cluster in ATL1, Droplet in ATL1 |
| Method | **VPC (Private IP)** |

#### How It Works

Resources in the same DO Team and same datacenter automatically join the **default VPC** for that datacenter (`default-atl1`). The database also has a private endpoint in this VPC. Traffic between them **never leaves the private network** — it never touches the public internet.

#### Step-by-Step

| # | Step | Action |
|---|------|--------|
| 1 | **Verify resource is in ATL1** | DO Dashboard → Resource → Networking tab → Datacenter = ATL1 |
| 2 | **Verify resource is in default-atl1 VPC** | DO Dashboard → Resource → Networking tab → VPC = default-atl1 |
| 3 | **Get Private connection string** | DO Dashboard → Databases → db-postgresql-atl1-weownnet → Connection Details → Toggle "Private network" ON |
| 4 | **Copy Private Host** | The private host will be different from the public host (usually `private-db-postgresql-...`) |
| 5 | **Configure application** | Use the private connection string in your app config |
| 6 | **Verify connection** | Run `psql` or app test query |

#### Finding Private vs Public Connection Details

| Field | Where to Find |
|-------|---------------|
| Public Host | Databases → Overview → Connection Details (default view) |
| **Private Host** | Databases → Overview → Connection Details → Toggle **"Private network"** |
| Port | Same for both: **25060** |
| Database | `defaultdb` |
| User | `doadmin` |
| Password | Click "show" in Connection Details |
| SSL Mode | `require` (always) |

#### Connection String — Private

```
postgresql://doadmin:<PASSWORD>@private-db-postgresql-atl1-weownnet-do-user-XXXXXXX-0.g.db.ondigitalocean.com:25060/defaultdb?sslmode=require
```

#### psql Command — Private

```bash
psql "postgresql://doadmin:<PASSWORD>@private-db-postgresql-atl1-weownnet-do-user-XXXXXXX-0.g.db.ondigitalocean.com:25060/defaultdb?sslmode=require"
```

#### Application Examples

**Node.js (pg):**
```javascript
const { Pool } = require('pg');

const pool = new Pool({
  host: 'private-db-postgresql-atl1-weownnet-do-user-XXXXXXX-0.g.db.ondigitalocean.com',
  port: 25060,
  database: 'defaultdb',
  user: 'doadmin',
  password: process.env.DB_PASSWORD,
  ssl: { rejectUnauthorized: true,
         ca: fs.readFileSync('/path/to/ca-certificate.crt').toString() }
});
```

**Python (psycopg2):**
```python
import psycopg2

conn = psycopg2.connect(
    host='private-db-postgresql-atl1-weownnet-do-user-XXXXXXX-0.g.db.ondigitalocean.com',
    port=25060,
    dbname='defaultdb',
    user='doadmin',
    password=os.environ['DB_PASSWORD'],
    sslmode='require',
    sslrootcert='/path/to/ca-certificate.crt'
)
```

#### Security Considerations

| Consideration | Detail |
|---------------|--------|
| Traffic path | **Private network only** — never touches internet |
| Encryption | SSL still enforced (defense-in-depth) |
| Trusted Sources | Not required for VPC connections (but recommended) |
| Firewall | No public port exposure needed |
| Credentials | Still protect password — use env vars |

#### Cost

| Item | Cost |
|------|------|
| Bandwidth | **FREE** — all intra-VPC traffic |
| Database | $15/mo (plan cost only) |

#### Expected Latency

| Metric | Value |
|--------|-------|
| Typical | **<1ms** |
| Worst case | 1-2ms |

#### Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| Connection refused | Wrong host (using public instead of private) | Toggle "Private network" in Connection Details |
| Connection timeout | Resource not in same VPC | Verify VPC membership in Networking tab |
| SSL error | Missing CA cert | Download from Databases → Overview → Download CA certificate |
| Auth failed | Wrong password | Re-copy from Connection Details |
| Too many connections | 22 limit reached | Check `pg_stat_activity`, close idle connections |

#### Verification Checklist

| # | Check | How | Expected |
|---|-------|-----|----------|
| 1 | Resource in ATL1 | Dashboard → Networking | ATL1 |
| 2 | Resource in default-atl1 VPC | Dashboard → Networking | default-atl1 |
| 3 | Using private host | Connection string starts with `private-` | ✅ |
| 4 | Port = 25060 | Connection string | 25060 |
| 5 | SSL mode = require | Connection string | sslmode=require |
| 6 | Test query works | `SELECT 1;` | Returns 1 |

---

### Scenario 2: Same DO Team + Different Datacenter (e.g., SFO3 → ATL1)

#### When This Applies

| Condition | Value |
|-----------|-------|
| Resource DO Team | Same as database |
| Resource Datacenter | Different from ATL1 (e.g., SFO3, NYC3) |
| Examples | Droplet in SFO3 connecting to database in ATL1 |
| Method | **VPC Peering (cross-region)** |

#### How It Works

VPC Peering creates an encrypted tunnel between two VPCs in different datacenters. Once peered, resources in VPC-A (SFO3) can reach resources in VPC-B (ATL1) using private IPs — as if they were in the same network.

#### What Is CIDR Notation?

| CIDR | Meaning | IP Range | Total IPs |
|------|---------|----------|-----------|
| `10.116.0.0/20` | ATL1 default VPC | 10.116.0.0 - 10.116.15.255 | 4,096 |
| `10.132.0.0/20` | SFO3 default VPC | 10.132.0.0 - 10.132.15.255 | 4,096 |

> **Key rule:** Peered VPCs MUST NOT have overlapping CIDR ranges. Default VPCs in different DCs use different ranges, so they won't overlap.

#### Step-by-Step: VPC Peering Setup

| # | Step | Action |
|---|------|--------|
| 1 | **Verify VPCs exist** | DO Dashboard → Networking → VPC → Confirm VPC exists in BOTH datacenters |
| 2 | **Check CIDR ranges** | Note the CIDR range for each VPC — ensure NO overlap |
| 3 | **Create Peering** | Networking → VPC → VPC Peering → "Create VPC Peering" |
| 4 | **Select Source VPC** | Choose the VPC where your resource lives (e.g., default-sfo3) |
| 5 | **Select Destination VPC** | Choose the VPC where the database lives (default-atl1) |
| 6 | **Name the peering** | e.g., `sfo3-to-atl1-peering` |
| 7 | **Create** | Click "Create VPC Peering" |
| 8 | **Wait for ACTIVE** | Status will show PENDING → ACTIVE (usually <1 min) |
| 9 | **Add peered CIDR to Trusted Sources** | Databases → db-postgresql-atl1-weownnet → Settings → Trusted Sources → Add the SFO3 VPC CIDR range |
| 10 | **Verify connectivity** | From SFO3 resource, connect to database using private host |

#### Peering States

| State | Meaning | Action |
|-------|---------|--------|
| PENDING | Peering being established | Wait |
| **ACTIVE** | Peering operational | ✅ Ready to use |
| FAILED | Error during setup | Check CIDR conflicts, retry |

#### Connection String — Via Peering

```
postgresql://doadmin:<PASSWORD>@private-db-postgresql-atl1-weownnet-do-user-XXXXXXX-0.g.db.ondigitalocean.com:25060/defaultdb?sslmode=require
```

> Same private host as Scenario 1 — peering makes the private endpoint reachable from the peered VPC.

#### ⚠️ Legacy Resource Considerations

| Issue | Affected | Fix |
|-------|----------|-----|
| **Droplets created before Oct 2, 2024** | May not automatically route peered traffic | Run manual route script (Section 3B) |
| **DOKS worker nodes** | May need recycling for peering routes | Recycle worker nodes in DOKS dashboard |

#### Manual Route Script (Legacy Droplets)

```bash
PEERED_VPC_CIDR="10.116.0.0/20"
GATEWAY=$(ip route | grep default | awk '{print $3}')
ip route add $PEERED_VPC_CIDR via $GATEWAY
echo "post-up ip route add $PEERED_VPC_CIDR via $GATEWAY" >> /etc/network/interfaces.d/50-cloud-init
```

#### DOKS Worker Node Recycling

| # | Step | Action |
|---|------|--------|
| 1 | Navigate to | Kubernetes → Cluster → Nodes |
| 2 | Select node | Click on worker node |
| 3 | Recycle | Actions → Recycle → Confirm |
| 4 | Wait | Node will drain, terminate, and recreate (~5 min) |
| 5 | Repeat | For each worker node (one at a time for zero downtime) |

#### Security Considerations

| Consideration | Detail |
|---------------|--------|
| Traffic path | Encrypted tunnel between DCs — never public internet |
| Peering is bidirectional | Both VPCs can reach each other |
| Trusted Sources | MUST add peered VPC CIDR to database Trusted Sources |
| Credentials | Still protect password — use env vars |

#### Cost

| Item | Cost |
|------|------|
| Peering setup | **FREE** |
| **Bandwidth (cross-DC)** | **$0.01/GiB** |

#### Cost Estimation

| Monthly Transfer | Cost |
|-----------------|------|
| 1 GiB | $0.01 |
| 10 GiB | $0.10 |
| 100 GiB | $1.00 |
| 1 TiB | $10.24 |

> For most application database traffic, cross-DC bandwidth costs are negligible (<$1/mo).

#### Expected Latency

| Route | Typical |
|-------|---------|
| SFO3 → ATL1 | **30-40ms** |
| NYC3 → ATL1 | **15-25ms** |
| TOR1 → ATL1 | **20-30ms** |

#### Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| Connection timeout | Peering not ACTIVE | Check peering status in Networking → VPC Peering |
| Connection refused | CIDR not in Trusted Sources | Add peered VPC CIDR to database Trusted Sources |
| Unreachable | Legacy Droplet missing route | Run manual route script |
| DOKS pods can't connect | Worker nodes need recycling | Recycle nodes one at a time |
| CIDR conflict | Overlapping ranges | Create custom VPC with non-overlapping CIDR |

#### Verification Checklist

| # | Check | How | Expected |
|---|-------|-----|----------|
| 1 | Peering status | Networking → VPC Peering | ACTIVE |
| 2 | CIDR in Trusted Sources | Databases → Settings → Trusted Sources | Peered VPC CIDR listed |
| 3 | Using private host | Connection string | `private-` prefix |
| 4 | Test query | `SELECT 1;` from SFO3 resource | Returns 1 |
| 5 | Latency check | `\timing` in psql | <50ms |

---

### Scenario 3: Different DO Team + Same Datacenter (ATL1 → ATL1, different billing)

#### When This Applies

| Condition | Value |
|-----------|-------|
| Resource DO Team | **Different** from database team |
| Resource Datacenter | ATL1 (same as database) |
| Examples | Resource on Team B (ATL1) connecting to database on Team A (ATL1) |
| Method | **Public Endpoint + Trusted Sources** |

#### Why Not VPC Peering?

| Reason | Detail |
|--------|--------|
| **Inter-team VPC Peering is NOT supported by DigitalOcean** | VPC Peering only works within the same DO Team/account |
| Workaround | Must use public endpoint with IP-based access control |

#### Step-by-Step

| # | Step | Action |
|---|------|--------|
| 1 | **Get Public connection string** | DO Dashboard → Databases → db-postgresql-atl1-weownnet → Connection Details (default = public) |
| 2 | **Find connecting resource's Public IP** | On the resource: `curl -s ifconfig.me` or DO Dashboard → Resource → Networking → Public IPv4 |
| 3 | **Add IP to Trusted Sources** | Databases → Settings → Trusted Sources → "Add Trusted Source" → Enter IP |
| 4 | **Download CA Certificate** | Databases → Overview → "Download CA certificate" |
| 5 | **Configure application** | Use public connection string + CA cert |
| 6 | **Verify connection** | Test with psql or app |

#### Connection String — Public

```
postgresql://doadmin:<PASSWORD>@db-postgresql-atl1-weownnet-do-user-XXXXXXX-0.g.db.ondigitalocean.com:25060/defaultdb?sslmode=require
```

> Note: NO `private-` prefix — this is the public endpoint.

#### psql Command — Public with CA Cert

```bash
psql "postgresql://doadmin:<PASSWORD>@db-postgresql-atl1-weownnet-do-user-XXXXXXX-0.g.db.ondigitalocean.com:25060/defaultdb?sslmode=verify-ca" \
  --set=sslrootcert=/path/to/ca-certificate.crt
```

#### Application Examples

**Node.js (pg):**
```javascript
const { Pool } = require('pg');
const fs = require('fs');

const pool = new Pool({
  host: 'db-postgresql-atl1-weownnet-do-user-XXXXXXX-0.g.db.ondigitalocean.com',
  port: 25060,
  database: 'defaultdb',
  user: 'doadmin',
  password: process.env.DB_PASSWORD,
  ssl: {
    rejectUnauthorized: true,
    ca: fs.readFileSync('/path/to/ca-certificate.crt').toString()
  }
});
```

**Python (psycopg2):**
```python
import psycopg2
import os

conn = psycopg2.connect(
    host='db-postgresql-atl1-weownnet-do-user-XXXXXXX-0.g.db.ondigitalocean.com',
    port=25060,
    dbname='defaultdb',
    user='doadmin',
    password=os.environ['DB_PASSWORD'],
    sslmode='verify-ca',
    sslrootcert='/path/to/ca-certificate.crt'
)
```

#### SSL Mode Options

| Mode | Encryption | CA Verification | Recommended |
|------|-----------|----------------|-------------|
| `require` | ✅ Yes | ❌ No | Minimum acceptable |
| **`verify-ca`** | ✅ Yes | ✅ Yes | **✅ RECOMMENDED** |
| `verify-full` | ✅ Yes | ✅ Yes + hostname | Most secure (may cause issues with DO hostnames) |

#### Dynamic IP Problem

| Issue | Detail |
|-------|--------|
| **Droplets** | Public IP is static — add once to Trusted Sources ✅ |
| **DOKS Pods** | Egress IP may change — need to find DOKS egress range |
| **Serverless** | IP unpredictable — consider wide CIDR or VPN |

#### Solutions for Dynamic IPs

| Solution | Cost | Complexity | Stability |
|----------|------|------------|----------|
| **Floating IP** | $5/mo | Low | ✅ Static — attach to Droplet |
| **NAT Gateway** | Varies | High | ✅ Stable egress IP |
| **Wide CIDR** | Free | Low | ⚠️ Less secure — allows range |
| **DO Droplet Tags** | Free | Low | ✅ Auto-update Trusted Sources |

#### Finding DOKS Egress IP

```bash
kubectl run tmp-shell --rm -i --tty --image=curlimages/curl -- sh
curl -s ifconfig.me
```

#### Security Considerations

| Consideration | Detail |
|---------------|--------|
| Traffic path | **Public internet** — SSL encrypted |
| Attack surface | Larger than VPC — IP exposed |
| Trusted Sources | **CRITICAL** — restrict to known IPs only |
| CA Certificate | Download and verify to prevent MITM |
| Credentials | Use env vars, never commit to code |
| IP changes | Monitor — if IP changes, connection breaks |

#### Cost

| Item | Cost |
|------|------|
| **Outbound bandwidth** | **$0.01/GiB** |
| Floating IP (optional) | $5/mo |
| Database plan | $15/mo |

#### Expected Latency

| Metric | Value |
|--------|-------|
| Same DC (ATL1 → ATL1 public) | **2-5ms** |

#### Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| Connection refused | IP not in Trusted Sources | Add IP to Trusted Sources |
| SSL certificate error | Missing or wrong CA cert | Re-download from DO dashboard |
| Connection timeout | Firewall blocking port 25060 | Check DO Cloud Firewall rules |
| Intermittent failures | Dynamic IP changed | Use Floating IP or update Trusted Sources |
| Auth failed | Wrong password or user | Re-copy credentials from Connection Details |

#### Verification Checklist

| # | Check | How | Expected |
|---|-------|-----|----------|
| 1 | Resource Public IP known | `curl ifconfig.me` | IP address |
| 2 | IP in Trusted Sources | Databases → Settings | ✅ Listed |
| 3 | CA cert downloaded | Local file | Present |
| 4 | Using public host | Connection string | NO `private-` prefix |
| 5 | SSL mode | Connection string | `require` or `verify-ca` |
| 6 | Test query | `SELECT 1;` | Returns 1 |

---

### Scenario 4: Different DO Team + Different Datacenter

#### When This Applies

| Condition | Value |
|-----------|-------|
| Resource DO Team | **Different** from database team |
| Resource Datacenter | **Different** from ATL1 |
| Examples | Resource on Team B in SFO3 connecting to database on Team A in ATL1 |
| Method | **Public Endpoint + Trusted Sources** |

#### Configuration

Same as Scenario 3 — public endpoint + Trusted Sources + SSL. The only difference is **higher latency** due to cross-DC routing.

#### Additional Latency

| Route | Typical Latency |
|-------|----------------|
| SFO3 → ATL1 (public) | **35-50ms** |
| NYC3 → ATL1 (public) | **20-30ms** |
| TOR1 → ATL1 (public) | **25-35ms** |

> These are higher than VPC Peering (Scenario 2) because traffic goes through public internet routing, not DO's internal backbone.

#### ⚠️ AVOID IF POSSIBLE

| Recommendation | Detail |
|----------------|--------|
| **This is the LEAST optimal path** | Highest latency + public exposure + cross-team billing |
| Consider migration | Move resource to ATL1 on the database team |
| Consider team consolidation | Merge DO teams if possible |
| Consider dedicated database | Deploy database in resource's DC if latency-critical |

#### Migration Decision Matrix

| Current State | Latency Acceptable? | Recommendation |
|--------------|---------------------|----------------|
| Low-traffic app in SFO3 | ✅ Yes (<50ms OK) | **Stay — accept latency** |
| High-traffic app in SFO3 | ❌ No (needs <5ms) | **Migrate app to ATL1** |
| Multiple apps in SFO3 | ❌ No | **Deploy replica DB in SFO3** |
| Single query per minute | ✅ Yes | **Stay — not worth migrating** |

#### How to Measure Latency

```bash
psql "postgresql://doadmin:<PASSWORD>@db-postgresql-atl1-weownnet-do-user-XXXXXXX-0.g.db.ondigitalocean.com:25060/defaultdb?sslmode=require" \
  -c "\timing" -c "SELECT 1;"

# Or use ping to estimate network latency:
ping db-postgresql-atl1-weownnet-do-user-XXXXXXX-0.g.db.ondigitalocean.com
```

#### Verification Checklist

Same as Scenario 3 checklist + additional:

| # | Check | How | Expected |
|---|-------|-----|----------|
| 7 | Latency measured | `\timing` in psql | Document baseline |
| 8 | Migration evaluated | Decision matrix above | Decision documented |

---

## 📋 Section 3: Connection Methods Deep Dive

### 3A: VPC (Virtual Private Cloud)

#### What Is a VPC?

A **Virtual Private Cloud (VPC)** is an isolated private network within a DigitalOcean datacenter. Resources inside a VPC can communicate with each other using **private IP addresses** (10.x.x.x range) — traffic never touches the public internet.

| Field | Value |
|-------|-------|
| Provider | DigitalOcean |
| Scope | Single datacenter |
| IP Range | Private (10.x.x.x) |
| Cost | **FREE** — all intra-VPC traffic |
| Security | Excellent — isolated from internet |
| Created | Automatically per datacenter (default VPC) |

#### How DO Creates Default VPCs

| Event | What Happens |
|-------|-------------|
| First resource in a DC | DO automatically creates `default-<dc>` VPC |
| Example | First Droplet in ATL1 → `default-atl1` created |
| CIDR | Auto-assigned (e.g., `10.116.0.0/20`) |
| All subsequent resources | Automatically join `default-<dc>` VPC |

#### Default VPCs in Our Ecosystem

| Datacenter | VPC Name | CIDR (typical) | Resources |
|-----------|----------|----------------|----------|
| **ATL1** | default-atl1 | 10.116.0.0/20 | Database, DOKS, Droplets |
| SFO3 | default-sfo3 | 10.132.0.0/20 | Some Droplets |
| NYC3 | default-nyc3 | 10.136.0.0/20 | Some Droplets |

#### Creating a Custom VPC

| # | Step | Action |
|---|------|--------|
| 1 | Navigate | Networking → VPC → "Create VPC" |
| 2 | Name | e.g., `production-atl1` |
| 3 | Datacenter | Select datacenter |
| 4 | IP Range | Choose CIDR (or let DO auto-assign) |
| 5 | Description | Optional — describe purpose |
| 6 | Create | Click "Create VPC" |

#### Why Create a Custom VPC?

| Reason | Detail |
|--------|--------|
| **Isolation** | Separate production from staging |
| **CIDR control** | Choose specific IP ranges |
| **Security** | Limit blast radius — compromised resource can't reach other VPCs |
| **Compliance** | Some regulations require network segmentation |

> **Current recommendation:** Use `default-atl1` for simplicity. Create custom VPCs when you need isolation between environments (prod/staging/dev).

#### How Resources Join a VPC

| Method | When |
|--------|------|
| **Automatic** | At creation — resource joins the selected VPC |
| **Manual** | Existing resource → cannot change VPC (must recreate) |

> ⚠️ **You cannot move an existing resource to a different VPC.** You must destroy and recreate it in the target VPC.

#### Private IP Addressing

| Range | Meaning |
|-------|--------|
| `10.0.0.0/8` | Private address space (RFC 1918) |
| `10.116.0.0/20` | ATL1 default VPC (4,096 addresses) |
| `10.116.0.1` | Example: Droplet private IP |
| `10.116.0.5` | Example: Database private IP |

#### How to Verify a Resource Is in the Correct VPC

| # | Step | Action |
|---|------|--------|
| 1 | Navigate | Dashboard → Resource (Droplet/DOKS) |
| 2 | Click | Networking tab |
| 3 | Find | "VPC" section |
| 4 | Verify | Shows `default-atl1` (or your custom VPC) |
| 5 | Private IP | Listed under VPC section |

#### Database Private Endpoint

| Field | Detail |
|-------|--------|
| Automatic | Database gets a private endpoint in its VPC |
| Host format | `private-db-postgresql-atl1-weownnet-...` |
| Finding it | Databases → Connection Details → Toggle "Private network" |
| Port | Same as public: **25060** |

#### Security Benefits

| Benefit | Detail |
|---------|--------|
| **No internet exposure** | Private IPs are not routable on the internet |
| **No Trusted Sources needed** | VPC resources are implicitly trusted (but still recommended) |
| **No bandwidth cost** | All intra-VPC traffic is FREE |
| **Reduced attack surface** | No public port to scan or attack |
| **Defense in depth** | SSL still enforced even on private connections |

#### Limitations

| Limitation | Detail |
|-----------|--------|
| **Same datacenter only** | VPC is DC-scoped — need peering for cross-DC |
| **Same team only** | VPC belongs to one DO Team — need public for cross-team |
| **Cannot move resources** | Must recreate to change VPC |
| **CIDR is fixed** | Cannot resize VPC CIDR after creation |

---

### 3B: VPC Peering

#### What Is VPC Peering?

**VPC Peering** connects two VPCs so resources in each can communicate using private IPs — as if they were in the same network. Traffic flows through DigitalOcean's internal backbone, not the public internet.

| Field | Value |
|-------|-------|
| Purpose | Connect two VPCs |
| Types | Same-DC peering, Cross-DC peering |
| Direction | **Bidirectional** — both sides can initiate |
| Cost | FREE (same-DC), $0.01/GiB (cross-DC) |
| Requirement | Same DO Team/account |

#### Same-DC vs Cross-DC Peering

| Aspect | Same-DC | Cross-DC |
|--------|---------|----------|
| Example | default-atl1 ↔ production-atl1 | default-atl1 ↔ default-sfo3 |
| Latency | <1ms | 15-50ms |
| Cost | FREE | $0.01/GiB |
| Use case | Environment isolation | Multi-region architecture |

#### Step-by-Step: Create a Peering Connection

| # | Step | Action |
|---|------|--------|
| 1 | Navigate | Networking → VPC → "VPC Peering" tab |
| 2 | Click | "Create VPC Peering" |
| 3 | Source VPC | Select first VPC (e.g., `default-sfo3`) |
| 4 | Destination VPC | Select second VPC (e.g., `default-atl1`) |
| 5 | Name | e.g., `sfo3-to-atl1` |
| 6 | Create | Click "Create VPC Peering" |
| 7 | Wait | Status: PENDING → **ACTIVE** |

#### Peering States

| State | Icon | Meaning | Action |
|-------|------|---------|--------|
| **PENDING** | 🟡 | Being established | Wait (<1 min) |
| **ACTIVE** | 🟢 | Operational | ✅ Ready to use |
| **FAILED** | 🔴 | Error | Check CIDR conflicts, retry |
| **DELETING** | 🟡 | Being removed | Wait |

#### CIDR Range Requirements

| Rule | Detail |
|------|--------|
| **No overlapping CIDRs** | Peered VPCs MUST have different IP ranges |
| Default VPCs | Usually non-overlapping (DO assigns unique ranges per DC) |
| Custom VPCs | YOU must ensure no overlap |

#### How to Check for CIDR Conflicts

```
✅ OK:     10.116.0.0/20 ↔ 10.132.0.0/20  (different ranges)
❌ CONFLICT: 10.116.0.0/20 ↔ 10.116.0.0/20  (identical ranges)
❌ CONFLICT: 10.116.0.0/16 ↔ 10.116.0.0/20  (one contains the other)
```

#### Bidirectional Nature

| Direction | Traffic |
|-----------|--------|
| VPC-A → VPC-B | ✅ Allowed |
| VPC-B → VPC-A | ✅ Allowed |

> Peering is **always bidirectional**. You cannot create one-way peering. Both sides can initiate connections.

#### Routing — How Traffic Flows

```
Resource in VPC-A (SFO3)
    │
    │ Sends packet to 10.116.0.5 (ATL1 private IP)
    │
    ▼
VPC-A routing table
    │
    │ Matches peering route → forward to peered VPC
    │
    ▼
DO Internal Backbone (encrypted)
    │
    │ Cross-DC tunnel
    │
    ▼
VPC-B routing table (ATL1)
    │
    │ Delivers to 10.116.0.5 (database)
    │
    ▼
PostgreSQL receives connection
```

#### Managed Database Compatibility

| Action | Required |
|--------|----------|
| Peering created | ✅ |
| **Add peered VPC CIDR to Trusted Sources** | ✅ **REQUIRED** |
| Database restart | ❌ Not needed |
| Connection string change | ❌ Same private host |

> ⚠️ **Critical step:** After peering, you MUST add the peered VPC's CIDR range to the database's Trusted Sources. Without this, the database will reject connections from the peered VPC.

#### Adding Peered CIDR to Trusted Sources

| # | Step | Action |
|---|------|--------|
| 1 | Navigate | Databases → db-postgresql-atl1-weownnet → Settings |
| 2 | Find | "Trusted Sources" section |
| 3 | Click | "Edit Trusted Sources" |
| 4 | Add | Enter peered VPC CIDR (e.g., `10.132.0.0/20`) |
| 5 | Save | Click "Save" |
| 6 | Verify | CIDR appears in Trusted Sources list |

#### Legacy Resource Considerations

##### Droplets Created Before October 2, 2024

| Issue | Detail |
|-------|--------|
| Problem | Older Droplets may not have automatic routing for peered VPCs |
| Symptom | Connection timeout to peered resources |
| Fix | Add manual route (see script below) |
| Check | `ip route show` — look for peered CIDR |

##### Manual Route Addition Script

```bash
#!/bin/bash
# Add route for peered VPC on legacy Droplet
# Run as root

PEERED_VPC_CIDR="10.116.0.0/20"  # Replace with actual peered VPC CIDR
GATEWAY=$(ip route | grep "default via" | head -1 | awk '{print $3}')

echo "Adding route for $PEERED_VPC_CIDR via $GATEWAY"
ip route add $PEERED_VPC_CIDR via $GATEWAY

# Verify
ip route show | grep $PEERED_VPC_CIDR

# Make persistent across reboots
# For Ubuntu 20.04+ (netplan):
cat >> /etc/netplan/99-vpc-peering.yaml << EOF
network:
  version: 2
  ethernets:
    eth1:
      routes:
        - to: $PEERED_VPC_CIDR
          via: $GATEWAY
EOF

netplan apply
echo "Route added and persisted."
```

##### DOKS Worker Node Recycling

| # | Step | Action |
|---|------|--------|
| 1 | Navigate | Kubernetes → Cluster → Nodes tab |
| 2 | Select | Worker node to recycle |
| 3 | Click | "..." menu → "Recycle" |
| 4 | Confirm | "Recycle Node" |
| 5 | Wait | ~3-5 minutes for drain + recreate |
| 6 | Verify | New node shows "Ready" status |
| 7 | Repeat | One node at a time (maintain availability) |

> ⚠️ **Recycle ONE node at a time** to maintain application availability. Wait for each node to reach "Ready" before recycling the next.

---

### 3C: Public Endpoint

#### When Public Endpoint Is the ONLY Option

| Scenario | Why Public Required |
|----------|-------------------|
| **Cross-team** (Scenario 3/4) | VPC Peering not supported between DO Teams |
| **External services** | Third-party apps outside DO |
| **Local development** | Developer laptop connecting to managed DB |
| **CI/CD pipelines** | GitHub Actions, GitLab CI, etc. |

#### SSL/TLS Enforcement

| Field | Value |
|-------|-------|
| Default | **Always enforced** — cannot connect without SSL |
| Protocol | TLS 1.2+ |
| Certificate | DigitalOcean-managed CA |
| Download | Databases → Overview → "Download CA certificate" |

> DigitalOcean managed databases **always** enforce SSL on public connections. You cannot connect without encryption.

#### How to Download CA Certificate

| # | Step | Action |
|---|------|--------|
| 1 | Navigate | Databases → db-postgresql-atl1-weownnet → Overview |
| 2 | Find | "Connection Details" section |
| 3 | Click | **"Download CA certificate"** |
| 4 | Save | Save as `ca-certificate.crt` |
| 5 | Store | Place in secure location on connecting resource |
| 6 | Permissions | `chmod 600 ca-certificate.crt` |

#### Connection String Format with SSL

```
postgresql://doadmin:<PASSWORD>@db-postgresql-atl1-weownnet-do-user-XXXXXXX-0.g.db.ondigitalocean.com:25060/defaultdb?sslmode=verify-ca&sslrootcert=/path/to/ca-certificate.crt
```

#### SSL Mode Options — Detailed

| Mode | Encryption | CA Verified | Hostname Verified | Security | Recommendation |
|------|-----------|-------------|-------------------|----------|---------------|
| `disable` | ❌ | ❌ | ❌ | ❌ None | **NEVER USE** (DO will reject anyway) |
| `allow` | Maybe | ❌ | ❌ | ⚠️ Weak | Not recommended |
| `prefer` | If available | ❌ | ❌ | ⚠️ Weak | Not recommended |
| `require` | ✅ Yes | ❌ | ❌ | 🟡 Good | Minimum acceptable |
| **`verify-ca`** | ✅ Yes | ✅ Yes | ❌ | ✅ **Strong** | **✅ RECOMMENDED** |
| `verify-full` | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Strongest | May fail with DO hostnames |

> **Use `verify-ca`** for production. It verifies the server's certificate was signed by the DO CA — preventing man-in-the-middle attacks.

#### Finding Public Host/Port

| # | Step | Action |
|---|------|--------|
| 1 | Navigate | Databases → db-postgresql-atl1-weownnet → Overview |
| 2 | Find | "Connection Details" section |
| 3 | Ensure | "Private network" toggle is **OFF** (default) |
| 4 | Copy | Host, Port, Database, User, Password |

| Field | Value |
|-------|-------|
| Host | `db-postgresql-atl1-weownnet-do-user-XXXXXXX-0.g.db.ondigitalocean.com` |
| Port | **25060** |
| Note | NO `private-` prefix = public endpoint |

#### Security Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| **IP exposure** | Database host is publicly resolvable | Trusted Sources — restrict to known IPs |
| **Brute force** | Attackers may try password guessing | Strong passwords + Trusted Sources |
| **MITM** | Traffic interception | Use `sslmode=verify-ca` with CA cert |
| **IP change** | Connection breaks if source IP changes | Use Floating IPs ($5/mo) or update Trusted Sources |
| **Port scanning** | Port 25060 discoverable | Trusted Sources blocks unauthorized IPs |

#### Bandwidth Costs

| Direction | Cost |
|-----------|------|
| Inbound to database | FREE |
| **Outbound from database** | **$0.01/GiB** |
| First 1 TiB/mo | $0.01/GiB |
| Over 1 TiB/mo | Tiered pricing |

#### Latency Expectations

| Source Location | To ATL1 (Public) |
|----------------|------------------|
| Same DC (ATL1) | 2-5ms |
| NYC3 | 20-30ms |
| SFO3 | 35-50ms |
| TOR1 | 25-35ms |
| Europe | 80-120ms |
| Asia | 150-250ms |

---

### 3D: Trusted Sources

#### What Are Trusted Sources?

**Trusted Sources** is an IP-based allowlist for your managed database. Only connections from listed IPs, Droplets, Kubernetes clusters, or CIDR ranges are allowed. All other connections are **rejected**.

| Field | Value |
|-------|-------|
| Location | Databases → Settings → Trusted Sources |
| Default | **EMPTY** (⚠️ all IPs allowed!) |
| Scope | Applies to public AND private connections |
| Types | IP, Droplet, DOKS cluster, CIDR range |

#### ⚠️ CRITICAL: Empty Trusted Sources = DANGEROUS

| State | Behavior |
|-------|----------|
| **Empty** (no sources) | ⚠️ **ALL IPs can connect** — anyone with credentials can reach your database |
| **1+ sources** | ✅ Only listed sources can connect — all others rejected |

> **ALWAYS add at least one Trusted Source.** An empty list means your database is accessible from ANY IP on the internet.

#### Types of Trusted Sources

| Type | What It Is | When to Use |
|------|-----------|-------------|
| **IP Address** | Single IPv4 address | Specific Droplet, office IP, developer laptop |
| **Droplet** | DO Droplet (by name) | Droplet → auto-updates if IP changes |
| **Kubernetes Cluster** | DOKS cluster | All nodes in cluster trusted |
| **CIDR Range** | IP range (e.g., 10.116.0.0/20) | VPC Peering, office IP range |

#### Step-by-Step: Adding a Trusted Source

##### Adding an IP Address

| # | Step | Action |
|---|------|--------|
| 1 | Navigate | Databases → db-postgresql-atl1-weownnet → Settings |
| 2 | Find | "Trusted Sources" section |
| 3 | Click | "Edit Trusted Sources" |
| 4 | Select | "IP Address" |
| 5 | Enter | IP address (e.g., `203.0.113.50`) |
| 6 | Save | Click "Save" |

##### Adding a Droplet

| # | Step | Action |
|---|------|--------|
| 1 | Navigate | Databases → Settings → Trusted Sources |
| 2 | Click | "Edit Trusted Sources" |
| 3 | Select | "Droplet" |
| 4 | Choose | Select Droplet from dropdown |
| 5 | Save | Click "Save" |

> **Advantage:** If the Droplet's IP changes, Trusted Sources updates automatically.

##### Adding a Kubernetes Cluster

| # | Step | Action |
|---|------|--------|
| 1 | Navigate | Databases → Settings → Trusted Sources |
| 2 | Click | "Edit Trusted Sources" |
| 3 | Select | "Kubernetes Cluster" |
| 4 | Choose | Select DOKS cluster from dropdown |
| 5 | Save | Click "Save" |

##### Adding a CIDR Range

| # | Step | Action |
|---|------|--------|
| 1 | Navigate | Databases → Settings → Trusted Sources |
| 2 | Click | "Edit Trusted Sources" |
| 3 | Select | "IP Address" |
| 4 | Enter | CIDR notation (e.g., `10.132.0.0/20`) |
| 5 | Save | Click "Save" |

> **Use for VPC Peering:** Add the peered VPC's CIDR range to allow all resources in that VPC.

#### Removing a Trusted Source

| # | Step | Action |
|---|------|--------|
| 1 | Navigate | Databases → Settings → Trusted Sources |
| 2 | Click | "Edit Trusted Sources" |
| 3 | Find | Source to remove |
| 4 | Click | "X" or "Remove" next to the source |
| 5 | Save | Click "Save" |

> ⚠️ **Removing the LAST source makes the list empty — ALL IPs allowed.** Always keep at least one source.

#### What Happens When a Non-Trusted IP Connects

| Event | Result |
|-------|--------|
| Connection attempt from untrusted IP | **Connection REFUSED** |
| Error message | `could not connect to server: Connection refused` |
| Logged | ✅ Visible in database logs |
| Alert | ❌ No automatic alert (set up monitoring) |

#### Best Practices

| Practice | Detail |
|----------|--------|
| **Never leave empty** | Always have at least one trusted source |
| **Use Droplet/DOKS types** | Auto-update on IP change |
| **Audit monthly** | Review list — remove stale entries |
| **Document changes** | Log who added/removed sources and why |
| **Use CIDR for VPC Peering** | More maintainable than individual IPs |
| **Minimize scope** | Add specific IPs, not wide ranges |

#### How to Audit Current Trusted Sources

| # | Step | Action |
|---|------|--------|
| 1 | Navigate | Databases → Settings → Trusted Sources |
| 2 | Screenshot | Document current list |
| 3 | For each source | Verify it's still needed |
| 4 | Remove | Any stale/unknown sources |
| 5 | Document | Log the audit date and findings |

#### Dynamic IP Problem and Solutions

| Resource Type | IP Behavior | Solution |
|--------------|-------------|----------|
| **Droplet** | Static public IP | ✅ Add Droplet as trusted source |
| **DOKS pods** | Dynamic egress IP | Add DOKS cluster as trusted source |
| **Floating IP** | Static ($5/mo) | Attach to Droplet, add Floating IP |
| **Serverless** | Unpredictable | Wide CIDR or VPN |
| **Developer laptop** | Changes (home/office/VPN) | Add current IP, update when changes |
| **CI/CD (GitHub Actions)** | Dynamic | Add GitHub's IP ranges (wide CIDR) |

#### DOKS Pod/Service Network

```bash
# Find DOKS egress IP from inside a pod:
kubectl run tmp-shell --rm -i --tty --image=curlimages/curl -- sh
curl -s ifconfig.me
exit
```

---

## 📋 Section 4: Autoscale Storage

### 4A: Current Configuration

| Field | Value |
|-------|-------|
| Initial Storage | **15 GiB** |
| Autoscale | **Enabled** |
| Threshold | **80%** (triggers when usage reaches 80% of current storage) |
| Increment | **+10 GiB** per autoscale event |
| Minimum | 15 GiB (plan default) |
| Maximum | **75 GiB** (plan limit) |
| Cost per GiB | ~$0.20/GiB/mo (varies by plan) |
| Disk Type | NVMe |

### 4B: How Autoscale Works

```
                    Autoscale Behavior Over Time

Storage (GiB)
    75 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  MAX LIMIT
    │
    65 ─┤
    │   │
    55 ─┤                                         ┌──── 55 GiB
    │   │                                    ┌────┘
    45 ─┤                               ┌────┘ Trigger @80% (44 GiB)
    │   │                          ┌────┘
    35 ─┤                     ┌────┘ 35 GiB
    │   │                ┌────┘ Trigger @80% (28 GiB)
    25 ─┤           ┌────┘ 25 GiB
    │   │      ┌────┘ Trigger @80% (20 GiB)
    15 ─┤ ─────┘ 15 GiB (initial)
    │   │  Trigger @80% (12 GiB)
    └───┼──────────────────────────────────────────── Time
        Month 1    Month 3    Month 6    Month 9
```

### 4C: Step-by-Step Example

| Event | Data Used | Storage | % Used | Trigger? | Action | New Storage |
|-------|-----------|---------|--------|----------|--------|-------------|
| Start | 0 GiB | 15 GiB | 0% | ❌ | — | 15 GiB |
| Growth | 8 GiB | 15 GiB | 53% | ❌ | — | 15 GiB |
| Growth | **12 GiB** | 15 GiB | **80%** | ✅ | **+10 GiB** | **25 GiB** |
| Growth | 16 GiB | 25 GiB | 64% | ❌ | — | 25 GiB |
| Growth | **20 GiB** | 25 GiB | **80%** | ✅ | **+10 GiB** | **35 GiB** |
| Growth | 24 GiB | 35 GiB | 69% | ❌ | — | 35 GiB |
| Growth | **28 GiB** | 35 GiB | **80%** | ✅ | **+10 GiB** | **45 GiB** |
| Growth | **36 GiB** | 45 GiB | **80%** | ✅ | **+10 GiB** | **55 GiB** |
| Growth | **44 GiB** | 55 GiB | **80%** | ✅ | **+10 GiB** | **65 GiB** |
| Growth | **52 GiB** | 65 GiB | **80%** | ✅ | **+10 GiB** | **75 GiB** |
| Growth | **60 GiB** | 75 GiB | **80%** | ❌ | ⚠️ **MAX — manual intervention** | 75 GiB |

### 4D: Cost at Each Autoscale Step

| Storage | Monthly Cost (est.) | Delta from Previous |
|---------|-------------------|-------------------|
| 15 GiB | Included in $15/mo plan | — |
| 25 GiB | ~$17/mo | +$2 |
| 35 GiB | ~$19/mo | +$2 |
| 45 GiB | ~$21/mo | +$2 |
| 55 GiB | ~$23/mo | +$2 |
| 65 GiB | ~$25/mo | +$2 |
| 75 GiB | ~$27/mo | +$2 |

> Costs are approximate. Actual pricing depends on DO's current storage rates. Total cost increase from 15→75 GiB ≈ **+$12/mo**.

### 4E: What Happens at 75 GiB Max

| Event | Consequence |
|-------|------------|
| Storage reaches 75 GiB | Autoscale **CANNOT** add more |
| Usage exceeds 75 GiB | Database enters **READ-ONLY MODE** |
| Read-only mode | ✅ SELECT works / ❌ INSERT, UPDATE, DELETE blocked |
| Recovery | Manual intervention required |

#### Recovery Options at Max Storage

| Option | Action | Downtime |
|--------|--------|----------|
| **Delete data** | Remove unnecessary tables/rows | None |
| **VACUUM FULL** | Reclaim dead tuple space | Brief lock per table |
| **Upgrade plan** | Move to higher plan (more storage range) | Brief (~seconds) |
| **Archive + purge** | Export old data, delete from DB | None |

### 4F: Checking Current Storage Usage

#### DO Dashboard

| # | Step | Action |
|---|------|--------|
| 1 | Navigate | Databases → db-postgresql-atl1-weownnet |
| 2 | Click | "Metrics" tab |
| 3 | Find | "Disk Usage" graph |
| 4 | Read | Current usage vs total storage |

#### SQL Query

```sql
-- Check database sizes
SELECT
    datname AS database,
    pg_size_pretty(pg_database_size(datname)) AS size
FROM pg_database
ORDER BY pg_database_size(datname) DESC;

-- Check total cluster size
SELECT pg_size_pretty(sum(pg_database_size(datname)))
FROM pg_database;

-- Check largest tables
SELECT
    schemaname || '.' || tablename AS table,
    pg_size_pretty(pg_total_relation_size(schemaname || '.' || tablename)) AS total_size
FROM pg_tables
WHERE schemaname NOT IN ('pg_catalog', 'information_schema')
ORDER BY pg_total_relation_size(schemaname || '.' || tablename) DESC
LIMIT 20;
```

### 4G: Manually Adjusting Storage

| # | Step | Action |
|---|------|--------|
| 1 | Navigate | Databases → db-postgresql-atl1-weownnet → Settings |
| 2 | Find | "Resize" or "Storage" section |
| 3 | Adjust | Increase storage (cannot decrease) |
| 4 | Confirm | Click "Resize" |
| 5 | Wait | Resize applies (~seconds, no downtime) |

> ⚠️ **Storage can only be INCREASED, never decreased.** Same as plan upgrades (Section 6).

### 4H: Changing Autoscale Settings

| # | Step | Action |
|---|------|--------|
| 1 | Navigate | Databases → db-postgresql-atl1-weownnet → Settings |
| 2 | Find | "Autoscale Disk" section |
| 3 | Options | Toggle on/off, adjust threshold %, adjust increment |
| 4 | Save | Click "Save" |

### 4I: Why You Probably Shouldn't Disable Autoscale

| Without Autoscale | With Autoscale |
|-------------------|----------------|
| ❌ Must manually monitor storage | ✅ Automatic expansion |
| ❌ Risk of read-only mode | ✅ Prevents read-only mode |
| ❌ Requires human intervention | ✅ Self-healing |
| ❌ Potential data loss if full | ✅ Buys time to address growth |

> **Disable ONLY if:** You have strict cost controls and prefer manual management with alerting.

### 4J: Setting Up Storage Alerts

| # | Step | Action |
|---|------|--------|
| 1 | Navigate | Databases → db-postgresql-atl1-weownnet → Settings |
| 2 | Find | "Alerts" section |
| 3 | Create | Disk usage alert |
| 4 | Threshold | Set to **70%** (pre-autoscale warning) |
| 5 | Notification | Email or Slack webhook |
| 6 | Save | Activate alert |

#### Recommended Alert Thresholds

| Threshold | % | Action |
|-----------|---|--------|
| Early warning | **70%** | Investigate growth trend |
| Autoscale trigger | 80% | Automatic — no action needed |
| High usage | **90%** | Plan for data cleanup or upgrade |
| Critical | **95%** | Immediate action — approaching max |

### 4K: Storage and Plan Relationship

| Plan | Price | Storage Range | Autoscale Max |
|------|-------|--------------|---------------|
| **Basic $15** | $15/mo | **15-75 GiB** | 75 GiB |
| Basic $28 | $28/mo | 25-150 GiB | 150 GiB |
| Basic $60 | $60/mo | 38-300 GiB | 300 GiB |
| Basic $82 | $82/mo | 80-600 GiB | 600 GiB |

> Upgrading the plan also increases the autoscale ceiling. If you're approaching 75 GiB max, upgrading to the $28 plan doubles your ceiling to 150 GiB.

---

## 📋 Section 5: Connection Monitoring + Upgrade Triggers

### 5A: Monitoring Active Connections

#### DO Dashboard

| # | Step | Action |
|---|------|--------|
| 1 | Navigate | Databases → db-postgresql-atl1-weownnet |
| 2 | Click | "Metrics" tab |
| 3 | Find | "Active Connections" graph |
| 4 | Read | Current connections vs limit (22) |

#### SQL Queries

##### Check Active Connection Count

```sql
SELECT count(*) AS active_connections
FROM pg_stat_activity;
```

##### Check Connection Limit

```sql
SHOW max_connections;
-- Returns: 22 (for Basic $15 plan)
```

##### Detailed Connection Info

```sql
SELECT
    datname AS database,
    usename AS user,
    client_addr AS client_ip,
    state,
    state_change,
    query_start,
    NOW() - query_start AS query_duration,
    LEFT(query, 80) AS query_preview
FROM pg_stat_activity
WHERE state IS NOT NULL
ORDER BY state_change DESC;
```

##### Connections by State

```sql
SELECT
    state,
    count(*) AS count
FROM pg_stat_activity
WHERE state IS NOT NULL
GROUP BY state
ORDER BY count DESC;
```

| State | Meaning | Concern |
|-------|---------|--------|
| `active` | Running a query | ✅ Normal |
| `idle` | Connected, not querying | ⚠️ Watch — consumes a slot |
| `idle in transaction` | In open transaction, not querying | 🔴 Bad — holds locks |
| `idle in transaction (aborted)` | Failed transaction, not closed | 🔴 Bad — must close |

##### Connections by User

```sql
SELECT
    usename AS user,
    count(*) AS connections
FROM pg_stat_activity
GROUP BY usename
ORDER BY connections DESC;
```

##### Connections by Client IP

```sql
SELECT
    client_addr AS client_ip,
    count(*) AS connections
FROM pg_stat_activity
WHERE client_addr IS NOT NULL
GROUP BY client_addr
ORDER BY connections DESC;
```

#### Identifying Idle Connections

```sql
-- Find connections idle for more than 5 minutes
SELECT
    pid,
    usename,
    client_addr,
    state,
    NOW() - state_change AS idle_duration,
    LEFT(query, 60) AS last_query
FROM pg_stat_activity
WHERE state = 'idle'
  AND NOW() - state_change > interval '5 minutes'
ORDER BY idle_duration DESC;
```

#### Terminating Idle Connections

```sql
-- Terminate a specific connection by PID
SELECT pg_terminate_backend(<PID>);

-- Terminate ALL idle connections older than 10 minutes
SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE state = 'idle'
  AND NOW() - state_change > interval '10 minutes'
  AND pid <> pg_backend_pid();  -- Don't kill your own connection!
```

> ⚠️ **Use with caution.** Terminating connections may cause application errors. Ensure apps have retry logic.

#### Third-Party Monitoring Options

| Tool | Type | Cost | Integration |
|------|------|------|-------------|
| **DO Built-in** | Dashboard + Alerts | Free | ✅ Native |
| **Datadog** | Full observability | Paid | PostgreSQL integration |
| **Grafana + Prometheus** | Self-hosted dashboards | Free (infra cost) | pg_exporter |
| **pgAdmin** | PostgreSQL GUI | Free | Direct connection |
| **New Relic** | APM + DB monitoring | Paid | PostgreSQL integration |

---

### 5B: Alert Thresholds

| Threshold | % of 22 | Connections | Color | Action |
|-----------|---------|-------------|-------|--------|
| **Normal** | 0-60% | 0-13 | 🟢 | No action needed |
| **Warning** | 60-75% | 13-16 | 🟡 | Monitor closely, identify growth cause |
| **High** | 75-85% | 17-19 | 🟠 | Plan upgrade or implement pooling |
| **Critical** | 85-95% | 19-21 | 🔴 | Upgrade NOW or terminate idle connections |
| **Exhausted** | 100% | 22 | ⛔ | New connections REFUSED — immediate action |

#### Setting Up DO Alerts

| # | Step | Action |
|---|------|--------|
| 1 | Navigate | Databases → db-postgresql-atl1-weownnet → Settings |
| 2 | Find | "Alerts" section |
| 3 | Create | "Connection count" alert |
| 4 | Threshold | Set to **75%** (17 connections) |
| 5 | Notification | Email and/or Slack webhook |
| 6 | Save | Activate alert |

#### Response Playbook

| Threshold | Immediate Action | Follow-Up |
|-----------|-----------------|----------|
| 🟢 Normal | None | — |
| 🟡 Warning | Check `pg_stat_activity` for idle connections | Review app connection patterns |
| 🟠 High | Terminate idle connections, review pool config | Plan upgrade timeline |
| 🔴 Critical | Terminate idle + idle-in-transaction immediately | Upgrade plan or deploy connection pool |
| ⛔ Exhausted | Emergency: terminate non-essential connections | **Upgrade plan immediately** |

---

### 5C: Automation Options

#### DO API — Check Database Metrics

```bash
# Get database cluster info
curl -s -X GET \
  "https://api.digitalocean.com/v2/databases/db-postgresql-atl1-weownnet" \
  -H "Authorization: Bearer $DO_API_TOKEN" \
  -H "Content-Type: application/json"
```

#### DO CLI (doctl)

```bash
# List databases
doctl databases list

# Get specific database
doctl databases get db-postgresql-atl1-weownnet

# Get connection details
doctl databases connection db-postgresql-atl1-weownnet

# List database pools
doctl databases pool list db-postgresql-atl1-weownnet
```

#### Automated Monitoring Script (Bash)

```bash
#!/bin/bash
# monitor-connections.sh
# Run via cron: */5 * * * * /opt/scripts/monitor-connections.sh

DB_HOST="private-db-postgresql-atl1-weownnet-do-user-XXXXXXX-0.g.db.ondigitalocean.com"
DB_PORT=25060
DB_NAME="defaultdb"
DB_USER="doadmin"
THRESHOLD=17  # 75% of 22

COUNT=$(PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME -t -c \
  "SELECT count(*) FROM pg_stat_activity;")

COUNT=$(echo $COUNT | tr -d ' ')

if [ "$COUNT" -ge "$THRESHOLD" ]; then
    echo "⚠️ HIGH CONNECTION COUNT: $COUNT / 22"
    # Send alert (Slack webhook example)
    curl -s -X POST "$SLACK_WEBHOOK_URL" \
      -H 'Content-type: application/json' \
      -d "{\"text\":\"⚠️ DB Alert: $COUNT/22 connections on db-postgresql-atl1-weownnet\"}"
fi

echo "$(date): Connections = $COUNT / 22" >> /var/log/db-monitor.log
```

#### Automated Monitoring Script (Python)

```python
#!/usr/bin/env python3
"""monitor_connections.py — Database connection monitor"""

import os
import psycopg2
import requests
from datetime import datetime

# Config
DB_CONFIG = {
    'host': os.environ.get('DB_HOST'),
    'port': 25060,
    'dbname': 'defaultdb',
    'user': 'doadmin',
    'password': os.environ.get('DB_PASSWORD'),
    'sslmode': 'require'
}
THRESHOLD = 17  # 75% of 22
SLACK_WEBHOOK = os.environ.get('SLACK_WEBHOOK_URL')

def check_connections():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM pg_stat_activity;")
    count = cur.fetchone()[0]
    cur.close()
    conn.close()
    return count

def alert(count):
    if SLACK_WEBHOOK:
        requests.post(SLACK_WEBHOOK, json={
            'text': f'⚠️ DB Alert: {count}/22 connections on db-postgresql-atl1-weownnet'
        })

def main():
    count = check_connections()
    timestamp = datetime.now().isoformat()
    print(f"{timestamp}: Connections = {count}/22")

    if count >= THRESHOLD:
        print(f"⚠️ THRESHOLD EXCEEDED: {count} >= {THRESHOLD}")
        alert(count)

if __name__ == '__main__':
    main()
```

#### Cron Job Setup

```bash
# Edit crontab
crontab -e

# Add monitoring every 5 minutes
*/5 * * * * /opt/scripts/monitor-connections.sh >> /var/log/db-monitor.log 2>&1

# Or Python version
*/5 * * * * /usr/bin/python3 /opt/scripts/monitor_connections.py >> /var/log/db-monitor.log 2>&1
```

#### Terraform Example

```hcl
# DigitalOcean Database Cluster
resource "digitalocean_database_cluster" "postgres" {
  name       = "db-postgresql-atl1-weownnet"
  engine     = "pg"
  version    = "18"
  size       = "db-s-1vcpu-1gb"
  region     = "atl1"
  node_count = 1

  maintenance_window {
    day  = "sunday"
    hour = "00:00:00"
  }
}

# Database Firewall (Trusted Sources)
resource "digitalocean_database_firewall" "postgres" {
  cluster_id = digitalocean_database_cluster.postgres.id

  rule {
    type  = "k8s"
    value = digitalocean_kubernetes_cluster.main.id
  }

  rule {
    type  = "droplet"
    value = digitalocean_droplet.app.id
  }
}
```

#### Auto-Upgrade Feasibility

| Method | Can Resize? | Downtime |
|--------|-------------|----------|
| **DO Dashboard** | ✅ Manual | Brief (seconds) |
| **DO API** | ✅ `PATCH /v2/databases/{id}/resize` | Brief (seconds) |
| **doctl** | ✅ `doctl databases resize` | Brief (seconds) |
| **Terraform** | ✅ Change `size` attribute | Brief (seconds) |

```bash
# Resize via API
curl -s -X PATCH \
  "https://api.digitalocean.com/v2/databases/db-postgresql-atl1-weownnet/resize" \
  -H "Authorization: Bearer $DO_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"size": "db-s-2vcpu-4gb", "num": 1}'
```

> ⚠️ **Auto-upgrade is TECHNICALLY possible** via API/Terraform but should be gated behind human approval due to the **NO DOWNGRADE** rule (Section 6C).

#### Webhook Options

| Platform | Method | Setup |
|----------|--------|-------|
| **Slack** | Incoming Webhook | Slack → Apps → Incoming Webhooks → Create |
| **Discord** | Webhook URL | Server Settings → Integrations → Webhooks |
| **PagerDuty** | Events API v2 | PagerDuty → Services → Events Integration |
| **Email** | SMTP or SendGrid | Direct from monitoring script |
| **Signal** | signal-cli | Self-hosted bridge |

---

## 📋 Section 6: Upgrade Process

### 6A: Upgrade Path

```
$15/mo          $28/mo          $60/mo          $82/mo
22 conn         47 conn         97 conn         197 conn
1 vCPU          2 vCPU          4 vCPU          4 vCPU
1 GB RAM        4 GB RAM        8 GB RAM        16 GB RAM
15-75 GiB       25-150 GiB      38-300 GiB      80-600 GiB
   │               │               │               │
   ├──── ✅ ───────►├──── ✅ ───────►├──── ✅ ───────►│
   │               │               │               │
   │◄── ❌ ────────┤◄── ❌ ────────┤◄── ❌ ────────┤
   │               │               │               │
   └───── NO DOWNGRADE PATH ──────────────────────┘
```

#### Full Plan Comparison

| Field | Basic $15 | Basic $28 | Basic $60 | Basic $82 |
|-------|-----------|-----------|-----------|----------|
| **Price** | $15/mo | $28/mo | $60/mo | $82/mo |
| **CPU** | 1 vCPU | 2 vCPU | 4 vCPU | 4 vCPU |
| **RAM** | 1 GB | 4 GB | 8 GB | 16 GB |
| **Connections** | **22** | **47** | **97** | **197** |
| **Storage Range** | 15-75 GiB | 25-150 GiB | 38-300 GiB | 80-600 GiB |
| **Disk** | NVMe | NVMe | NVMe | NVMe |
| **Backups** | 7 days | 7 days | 7 days | 7 days |
| **Standby** | ❌ | ❌ | ❌ | ❌ |

> **Basic plans** = single node, no standby. For HA (High Availability) with automatic failover, upgrade to **Professional** plans (higher cost).

#### Cost Delta Between Tiers

| Upgrade | Monthly Delta | Annual Delta | Connection Gain |
|---------|--------------|-------------|----------------|
| $15 → $28 | **+$13/mo** | +$156/yr | **+25 connections** (22→47) |
| $28 → $60 | +$32/mo | +$384/yr | +50 connections (47→97) |
| $60 → $82 | +$22/mo | +$264/yr | +100 connections (97→197) |

#### Connection Limit Per Dollar

| Plan | $/connection/mo | Efficiency |
|------|----------------|------------|
| $15 | $0.68/conn | Baseline |
| $28 | $0.60/conn | ✅ Better |
| $60 | $0.62/conn | Similar |
| $82 | $0.42/conn | ✅ **Best value** |

---

### 6B: Step-by-Step Upgrade

| # | Step | Action |
|---|------|--------|
| 1 | **Navigate** | DO Dashboard → Databases → db-postgresql-atl1-weownnet |
| 2 | **Click** | "Settings" tab |
| 3 | **Find** | "Resize Cluster" section |
| 4 | **Click** | "Resize" button |
| 5 | **Select Plan** | Choose target plan (e.g., Basic $28 — 2 vCPU / 4 GB) |
| 6 | **Review** | Confirm new specs, price, and connection limit |
| 7 | **Confirm** | Click "Resize This Database Cluster" |
| 8 | **Wait** | Resize in progress (~1-5 minutes) |
| 9 | **Verify** | Check new connection limit is active |

#### Expected Time for Resize

| Plan Change | Typical Duration |
|-------------|------------------|
| $15 → $28 | 1-3 minutes |
| $28 → $60 | 2-5 minutes |
| $60 → $82 | 2-5 minutes |

#### Verifying Resize Completed

| # | Method | Action |
|---|--------|--------|
| 1 | **Dashboard** | Databases → Overview → Plan shows new specs |
| 2 | **SQL** | `SHOW max_connections;` — should show new limit |
| 3 | **API** | `doctl databases get <cluster-id>` — check `size` field |

```sql
-- Verify new connection limit
SHOW max_connections;
-- Expected after $15 → $28: 47
```

---

### 6C: ⚠️ NO DOWNGRADE WARNING

```
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║   ⚠️  WARNING: DOWNSCALING IS NOT SUPPORTED                     ║
║                                                                  ║
║   Once you upgrade to a larger plan, you CANNOT go back          ║
║   to a smaller plan. This is a ONE-WAY operation.                ║
║                                                                  ║
║   $15 ──→ $28 ──→ $60 ──→ $82                                   ║
║         ✅       ✅       ✅                                      ║
║                                                                  ║
║   $82 ──→ $60 ──→ $28 ──→ $15                                   ║
║         ❌       ❌       ❌                                      ║
║                                                                  ║
║   You are LOCKED INTO the higher tier permanently.               ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

#### Cost Implications

| Scenario | Monthly Cost | Annual Cost |
|----------|-------------|-------------|
| Stay at $15 | $180/yr | ✅ Baseline |
| Upgrade to $28 (permanent) | $336/yr | +$156/yr **forever** |
| Upgrade to $60 (permanent) | $720/yr | +$540/yr **forever** |
| Upgrade to $82 (permanent) | $984/yr | +$804/yr **forever** |

#### Decision Framework: Upgrade vs Optimize First

| Question | If YES → | If NO → |
|----------|----------|---------|
| Are most connections `idle`? | **Optimize first** — terminate idle, add pool | Consider upgrade |
| Is connection count growing steadily? | **Upgrade** — you'll hit limit eventually | Optimize first |
| Can you implement connection pooling? | **Pool first** — multiply effective connections | Upgrade |
| Is this a temporary spike? | **Wait** — terminate idle, monitor | — |
| Are you at 85%+ consistently? | **Upgrade** — risk too high | Optimize first |

#### Alternatives to Upgrading

| Alternative | How | Impact |
|-------------|-----|--------|
| **Connection Pooling** (Section 7) | Create DO connection pool | 22 physical → 100+ effective |
| **Terminate idle connections** | SQL: `pg_terminate_backend()` | Free up slots immediately |
| **Optimize queries** | Reduce query time → connections return faster | Fewer concurrent connections |
| **App-level pooling** | Configure app connection pool (HikariCP, pg-pool) | Reuse connections |
| **Close idle-in-transaction** | Set `idle_in_transaction_session_timeout` | Auto-close stale transactions |

```sql
-- Auto-close idle-in-transaction after 5 minutes
ALTER DATABASE defaultdb
SET idle_in_transaction_session_timeout = '5min';
```

---

### 6D: Zero-Downtime Behavior

#### What "Zero-Downtime" Means in Practice

| Aspect | Detail |
|--------|--------|
| **Claim** | DigitalOcean calls resize "zero-downtime" |
| **Reality** | Brief connection interruption possible (1-10 seconds) |
| **What happens** | Database process migrates to new resources |
| **Active queries** | May be interrupted — retry needed |
| **Idle connections** | May be dropped — reconnect needed |

#### How Apps Should Handle Brief Disconnects

| Strategy | Implementation |
|----------|----------------|
| **Retry logic** | Retry failed queries 3x with exponential backoff |
| **Connection validation** | Test connection before use (`SELECT 1`) |
| **Pool reconnect** | Configure pool to validate + replace dead connections |

**Node.js Retry Example:**

```javascript
const { Pool } = require('pg');

const pool = new Pool({
  // ... connection config
  max: 5,
  idleTimeoutMillis: 30000,
  connectionTimeoutMillis: 5000,
});

async function queryWithRetry(sql, params, maxRetries = 3) {
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      const result = await pool.query(sql, params);
      return result;
    } catch (err) {
      if (attempt === maxRetries) throw err;
      const delay = Math.pow(2, attempt) * 100; // 200ms, 400ms, 800ms
      console.warn(`Query failed (attempt ${attempt}), retrying in ${delay}ms...`);
      await new Promise(r => setTimeout(r, delay));
    }
  }
}
```

**Python Retry Example:**

```python
import psycopg2
import time

def query_with_retry(sql, params=None, max_retries=3):
    for attempt in range(1, max_retries + 1):
        try:
            conn = psycopg2.connect(**DB_CONFIG)
            cur = conn.cursor()
            cur.execute(sql, params)
            result = cur.fetchall()
            cur.close()
            conn.close()
            return result
        except psycopg2.OperationalError as e:
            if attempt == max_retries:
                raise
            delay = 2 ** attempt * 0.1  # 0.2s, 0.4s, 0.8s
            print(f"Query failed (attempt {attempt}), retrying in {delay}s...")
            time.sleep(delay)
```

#### Recommended: Upgrade During Low Traffic

| Step | Action |
|------|--------|
| 1 | Identify lowest-traffic period (check Metrics tab) |
| 2 | Notify team: "Database resize at [time] — expect brief interruption" |
| 3 | Ensure all apps have retry logic deployed |
| 4 | Perform resize |
| 5 | Monitor connections post-resize |
| 6 | Confirm apps reconnected |

#### Verifying Apps Reconnected

```sql
-- After resize, check connections are re-established
SELECT
    usename,
    client_addr,
    state,
    backend_start
FROM pg_stat_activity
WHERE backend_start > NOW() - interval '5 minutes'
ORDER BY backend_start DESC;
```

> If `backend_start` shows recent timestamps, apps have reconnected. If expected apps are missing, check app logs for connection errors.

---

## 📋 Section 7: Connection Pools

### 7A: What Connection Pools Are

#### The Problem

Every PostgreSQL connection opens a **dedicated server process**. Each process consumes:

| Resource | Per Connection |
|----------|---------------|
| RAM | ~5-10 MB |
| CPU | Process overhead |
| Connection slot | 1 of 22 |

With only **22 connections**, you can run out quickly if multiple apps, workers, and admin tools connect simultaneously.

#### The Solution: Connection Pooling

A **connection pool** sits between your application and the database. It maintains a small number of **real** database connections and multiplexes **many** application connections through them.

```
WITHOUT POOLING:                    WITH POOLING:

App 1 ──→ DB Connection 1          App 1 ──→┐
App 2 ──→ DB Connection 2          App 2 ──→┤
App 3 ──→ DB Connection 3          App 3 ──→┤
App 4 ──→ DB Connection 4          App 4 ──→┤ Pool ──→ DB Conn 1
App 5 ──→ DB Connection 5          App 5 ──→┤ (5)  ──→ DB Conn 2
  ...       ...                    App 6 ──→┤       ──→ DB Conn 3
App 22 ──→ DB Connection 22        App 7 ──→┤       ──→ DB Conn 4
                                   App 8 ──→┤       ──→ DB Conn 5
❌ App 23 = REFUSED                App 9 ──→┤
                                   App 10──→┘
                                     ...
                                   App 100 ✅ OK!

22 apps MAX                        100+ apps through 5 connections
```

#### PgBouncer

DigitalOcean uses **PgBouncer** as the connection pooler for managed databases. PgBouncer is lightweight, battle-tested, and widely used in production PostgreSQL deployments.

| Field | Value |
|-------|-------|
| Pooler | PgBouncer |
| Managed by | DigitalOcean (built-in feature) |
| Cost | **FREE** (included with managed database) |
| Setup | Via DO Dashboard |

---

### 7B: Pool Modes

| Mode | Connection Returned | Best For | Compatibility |
|------|-------------------|----------|---------------|
| **Transaction** | After each transaction completes | ✅ **Most apps** | ⚠️ Some limitations |
| **Session** | When client disconnects | Legacy apps | ✅ Full compatibility |
| **Statement** | After each statement | Simple queries | ❌ Most limited |

#### Transaction Mode (RECOMMENDED)

| Aspect | Detail |
|--------|--------|
| How it works | Connection assigned when transaction starts, returned when it commits/rollbacks |
| Efficiency | **Highest** — connections reused between transactions |
| Multiplier | 5 pool connections can serve 50+ app connections |
| Best for | Modern web apps, APIs, microservices |

**⚠️ Transaction Mode Limitations:**

| Feature | Works? | Workaround |
|---------|--------|------------|
| Prepared statements | ❌ | Use `DEALLOCATE ALL` or disable |
| `SET` commands | ❌ | Use per-query settings |
| `LISTEN`/`NOTIFY` | ❌ | Use direct connection for pub/sub |
| Session variables | ❌ | Pass in query context |
| Temporary tables | ⚠️ | Only within single transaction |
| Advisory locks | ❌ | Use direct connection |
| `DECLARE CURSOR` | ⚠️ | Only within single transaction |

#### Session Mode

| Aspect | Detail |
|--------|--------|
| How it works | Connection assigned when client connects, held until disconnect |
| Efficiency | **Lowest** — same as direct connection (but with queue) |
| Multiplier | Minimal — mainly provides queuing |
| Best for | Legacy apps that use session features |

#### Statement Mode

| Aspect | Detail |
|--------|--------|
| How it works | Connection returned after EVERY statement |
| Efficiency | **Highest** — but most restrictive |
| Multiplier | Very high |
| Best for | Simple SELECT-only workloads |

**⚠️ Statement Mode Limitations:**

| Feature | Works? |
|---------|--------|
| Multi-statement transactions | ❌ |
| Prepared statements | ❌ |
| Session variables | ❌ |
| Everything in Transaction mode limitations | ❌ |

#### Recommendation

| Workload | Mode |
|----------|------|
| **Web apps / APIs** | ✅ **Transaction** |
| **Legacy apps with session features** | Session |
| **Read-only dashboards** | Statement |
| **Unsure** | ✅ **Transaction** (start here) |

---

### 7C: Creating a Connection Pool

#### Step-by-Step

| # | Step | Action |
|---|------|--------|
| 1 | **Navigate** | Databases → db-postgresql-atl1-weownnet |
| 2 | **Click** | "Connection Pools" tab |
| 3 | **Click** | "Create Connection Pool" |
| 4 | **Pool Name** | Enter name (e.g., `app-pool`) |
| 5 | **Database** | Select `defaultdb` (or your database) |
| 6 | **User** | Select `doadmin` (or specific user) |
| 7 | **Mode** | Select **Transaction** (recommended) |
| 8 | **Pool Size** | Enter size (see guidance below) |
| 9 | **Create** | Click "Create Pool" |

#### How to Choose Pool Size

| Factor | Guidance |
|--------|----------|
| **Max pool size** | Cannot exceed database connection limit (22) |
| **Reserved connections** | Leave 2-3 for admin/monitoring |
| **Single pool** | Set to **18-20** (leaving 2-4 for direct connections) |
| **Multiple pools** | Divide available connections among pools |
| **Rule of thumb** | Pool size = (connection limit - reserved) |

#### Example Pool Configurations

##### Single App — One Pool

| Pool | Database | User | Mode | Size | Remaining Direct |
|------|----------|------|------|------|------------------|
| `app-pool` | defaultdb | doadmin | Transaction | **19** | 3 (admin/monitoring) |

##### Multiple Apps — Multiple Pools

| Pool | Database | User | Mode | Size | Purpose |
|------|----------|------|------|------|--------|
| `api-pool` | defaultdb | api_user | Transaction | **10** | API backend |
| `worker-pool` | defaultdb | worker_user | Transaction | **6** | Background workers |
| `admin-pool` | defaultdb | doadmin | Session | **3** | Admin/monitoring |
| **Total** | | | | **19** | 3 remaining for direct |

#### ⚠️ Pools Consume From Connection Limit

```
Total Connection Limit:         22
├── app-pool (Transaction):     10 connections
├── worker-pool (Transaction):   6 connections
├── admin-pool (Session):        3 connections
├── Direct connections:          3 remaining
└── Total allocated:            22
```

> **Critical:** Pool sizes + direct connections MUST NOT exceed 22. If they do, pool creation will fail or direct connections will be refused.

---

### 7D: Connecting via Pool

#### Pool Connection Details

| # | Step | Action |
|---|------|--------|
| 1 | Navigate | Databases → db-postgresql-atl1-weownnet → Connection Pools |
| 2 | Find | Your pool (e.g., `app-pool`) |
| 3 | Click | "Connection Details" |
| 4 | Copy | Host, Port, Database, User, Password |

#### Pool vs Direct Connection

| Field | Direct Connection | Pool Connection |
|-------|------------------|------------------|
| Host | `db-postgresql-atl1-...` | `db-postgresql-atl1-...` (same) |
| **Port** | **25060** | **25061** (different!) |
| Database | `defaultdb` | `app-pool` (pool name) |
| User | `doadmin` | `doadmin` (same) |
| Password | Same | Same |
| SSL | `require` | `require` |

> **Key differences:** Pool uses **port 25061** and the **pool name as database**.

#### Pool Connection String

```
postgresql://doadmin:<PASSWORD>@db-postgresql-atl1-weownnet-do-user-XXXXXXX-0.g.db.ondigitalocean.com:25061/app-pool?sslmode=require
```

#### Application Examples — Pool Connection

**Node.js (pg):**

```javascript
const { Pool } = require('pg');

const pool = new Pool({
  host: 'db-postgresql-atl1-weownnet-do-user-XXXXXXX-0.g.db.ondigitalocean.com',
  port: 25061,           // Pool port (NOT 25060)
  database: 'app-pool',  // Pool name (NOT defaultdb)
  user: 'doadmin',
  password: process.env.DB_PASSWORD,
  ssl: { rejectUnauthorized: true,
         ca: fs.readFileSync('/path/to/ca-certificate.crt').toString() },
  max: 20,               // App-level pool (can be higher than DB pool)
  idleTimeoutMillis: 30000,
  connectionTimeoutMillis: 5000,
});
```

**Python (psycopg2):**

```python
import psycopg2

conn = psycopg2.connect(
    host='db-postgresql-atl1-weownnet-do-user-XXXXXXX-0.g.db.ondigitalocean.com',
    port=25061,           # Pool port
    dbname='app-pool',    # Pool name
    user='doadmin',
    password=os.environ['DB_PASSWORD'],
    sslmode='require',
    sslrootcert='/path/to/ca-certificate.crt'
)
```

#### Verifying Pool Connection

```sql
-- Connected via pool — verify
SELECT
    current_database(),  -- Should show 'defaultdb' (underlying DB)
    inet_server_port();  -- Should show 25061 (pool port)
```

---

### 7E: Managing Pools

#### Editing Pool Settings

| # | Step | Action |
|---|------|--------|
| 1 | Navigate | Databases → Connection Pools |
| 2 | Find | Pool to edit |
| 3 | Click | "..." menu → "Edit" |
| 4 | Modify | Mode, size, or user |
| 5 | Save | Click "Save" |

> ⚠️ Changing pool settings may briefly interrupt connections through that pool.

#### Deleting a Pool

| # | Step | Action |
|---|------|--------|
| 1 | Navigate | Databases → Connection Pools |
| 2 | Find | Pool to delete |
| 3 | Click | "..." menu → "Delete" |
| 4 | Confirm | Type pool name to confirm |
| 5 | Delete | Click "Delete" |

> ⚠️ **All connections through this pool will be immediately terminated.** Ensure no apps are using the pool before deleting.

#### Monitoring Pool Utilization

| Method | How |
|--------|-----|
| **DO Dashboard** | Connection Pools tab → shows active/waiting connections |
| **PgBouncer stats** | Connect to pool, run `SHOW POOLS;` |
| **Application logs** | Monitor connection acquisition time |

```sql
-- Connect to pool, then:
SHOW POOLS;
-- Shows: database, user, cl_active, cl_waiting, sv_active, sv_idle
```

| Column | Meaning |
|--------|--------|
| `cl_active` | Client connections actively using a server connection |
| `cl_waiting` | Client connections waiting for a server connection |
| `sv_active` | Server connections in use |
| `sv_idle` | Server connections available |

#### When Pool Size Needs Adjustment

| Signal | Action |
|--------|--------|
| `cl_waiting` > 0 consistently | **Increase pool size** (if connection limit allows) |
| `sv_idle` = pool size consistently | **Decrease pool size** (wasting connections) |
| Connection acquisition timeout | **Increase pool size** or optimize query speed |
| `sv_active` = pool size consistently | Pool is fully utilized — increase or optimize |

#### Relationship: Pool Size vs Database Connection Limit

```
Database Connection Limit: 22
    │
    ├── Pool 1 (size: 10) ──→ Serves 50+ app connections
    │       └── 10 real DB connections consumed
    │
    ├── Pool 2 (size: 6)  ──→ Serves 30+ app connections
    │       └── 6 real DB connections consumed
    │
    ├── Direct connections ──→ 6 remaining
    │       └── Admin, monitoring, migrations
    │
    └── Total: 10 + 6 + 6 = 22 ✅
```

> **Pools don't CREATE connections — they MANAGE them.** A pool of size 10 uses 10 of your 22 connections. The benefit is that those 10 connections can serve 50+ application connections through multiplexing.

---

## 📋 Section 8: Network Access

### 8A: What Network Access Is

Network Access controls **how** and **from where** connections reach your managed database. DigitalOcean provides two network paths (public and private) and an IP-based allowlist (Trusted Sources) to restrict access.

| Field | Value |
|-------|-------|
| Location | Databases → db-postgresql-atl1-weownnet → Settings → Trusted Sources |
| Scope | Controls ALL inbound connections |
| Default | ⚠️ No Trusted Sources = ALL IPs allowed |

#### Network Access Layers

```
┌─────────────────────────────────────────────────────┐
│  Layer 1: Network Path                               │
│  ┌─────────────────┐  ┌──────────────────────────┐  │
│  │  Public Network  │  │  Private Network (VPC)   │  │
│  │  Internet-facing │  │  Internal only            │  │
│  │  SSL enforced    │  │  SSL enforced             │  │
│  │  Port: 25060     │  │  Port: 25060              │  │
│  └────────┬────────┘  └────────────┬─────────────┘  │
│           │                         │                │
│           ▼                         ▼                │
│  ┌──────────────────────────────────────────────┐   │
│  │  Layer 2: Trusted Sources (IP Allowlist)      │   │
│  │  ✅ Listed IP/Droplet/DOKS/CIDR → ALLOWED    │   │
│  │  ❌ Unlisted IP → REJECTED                    │   │
│  └──────────────────────────────────────────────┘   │
│           │                                          │
│           ▼                                          │
│  ┌──────────────────────────────────────────────┐   │
│  │  Layer 3: PostgreSQL Authentication           │   │
│  │  Username + Password + SSL Certificate        │   │
│  └──────────────────────────────────────────────┘   │
│           │                                          │
│           ▼                                          │
│  ┌──────────────────────────────────────────────┐   │
│  │  Layer 4: PostgreSQL Authorization            │   │
│  │  GRANT / REVOKE — per-database, per-table     │   │
│  └──────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────┘
```

> **4 layers of security.** Even if an attacker passes Layer 1 (network), they still need to pass Trusted Sources (Layer 2), authentication (Layer 3), and authorization (Layer 4).

---

### 8B: Public Network

#### What Public Network Access Means

| Field | Value |
|-------|-------|
| Definition | Database is reachable from the public internet via its public hostname |
| Default | **Enabled** (always on for managed databases) |
| Can disable? | ❌ Cannot fully disable public endpoint on DO managed databases |
| Protection | Trusted Sources + SSL + Authentication |

#### How to Restrict Public Access

Since you can't disable the public endpoint, you **restrict** it:

| Method | How |
|--------|-----|
| **Trusted Sources** | Only allow specific IPs/resources |
| **SSL enforcement** | Already enforced by DO (always on) |
| **Strong passwords** | Use generated passwords from DO dashboard |
| **Separate users** | Create app-specific users with limited privileges |

---

### 8C: Private Network (VPC)

#### What Private Network Access Means

| Field | Value |
|-------|-------|
| Definition | Database is reachable via private IP within its VPC |
| Scope | Resources in same VPC (or peered VPC) |
| Host | `private-db-postgresql-atl1-weownnet-...` |
| Port | 25060 (same as public) |
| Cost | **FREE** |

#### How It Relates to VPC Membership

| Resource Location | Can Use Private? |
|-------------------|------------------|
| Same VPC (default-atl1) | ✅ Yes — automatic |
| Peered VPC | ✅ Yes — after peering setup |
| Different VPC (same DC, not peered) | ❌ No — need peering |
| Different DC (not peered) | ❌ No — need peering or public |
| Different DO Team | ❌ No — public only |

#### Performance Benefits

| Metric | Public | Private |
|--------|--------|--------|
| Latency | 2-50ms | **<1ms** |
| Bandwidth cost | $0.01/GiB | **FREE** |
| Internet exposure | Yes | **No** |
| SSL overhead | Minimal | Minimal (still enforced) |

#### How to Ensure Resources Use Private Connection

| # | Step | Action |
|---|------|--------|
| 1 | Verify | Resource is in same VPC as database |
| 2 | Get | Private connection string (toggle "Private network" in dashboard) |
| 3 | Configure | App uses `private-` host, NOT public host |
| 4 | Test | Confirm connection works with `SELECT 1;` |
| 5 | Verify | Check `client_addr` in `pg_stat_activity` shows 10.x.x.x (private) |

```sql
-- Verify you're connected via private network
SELECT inet_client_addr();
-- If result is 10.x.x.x → private connection ✅
-- If result is public IP → public connection ⚠️
```

---

### 8D: Trusted Sources (Detailed Management)

#### Full Dashboard Walkthrough

| # | Step | Action |
|---|------|--------|
| 1 | Navigate | DO Dashboard → Databases |
| 2 | Select | db-postgresql-atl1-weownnet |
| 3 | Click | "Settings" tab |
| 4 | Scroll | Find "Trusted Sources" section |
| 5 | Click | "Edit Trusted Sources" |
| 6 | View | Current sources listed |

#### Adding a Droplet as Trusted Source

| # | Step | Action |
|---|------|--------|
| 1 | Click | "Edit Trusted Sources" |
| 2 | Click | "Add a Trusted Source" |
| 3 | Select type | "Droplet" |
| 4 | Choose | Select Droplet from dropdown |
| 5 | Save | Click "Save" |

> **Advantage:** If Droplet IP changes (rebuild, resize), Trusted Sources auto-updates.

#### Adding a Kubernetes Cluster as Trusted Source

| # | Step | Action |
|---|------|--------|
| 1 | Click | "Edit Trusted Sources" |
| 2 | Click | "Add a Trusted Source" |
| 3 | Select type | "Kubernetes Cluster" |
| 4 | Choose | Select DOKS cluster from dropdown |
| 5 | Save | Click "Save" |

> **Advantage:** All worker nodes in the cluster are trusted. Node recycling doesn't break access.

#### Adding a Specific IP Address

| # | Step | Action |
|---|------|--------|
| 1 | Click | "Edit Trusted Sources" |
| 2 | Click | "Add a Trusted Source" |
| 3 | Select type | "IP Address" |
| 4 | Enter | IPv4 address (e.g., `203.0.113.50`) |
| 5 | Save | Click "Save" |

#### Adding a CIDR Range

| # | Step | Action |
|---|------|--------|
| 1 | Click | "Edit Trusted Sources" |
| 2 | Click | "Add a Trusted Source" |
| 3 | Select type | "IP Address" |
| 4 | Enter | CIDR notation (e.g., `10.132.0.0/20`) |
| 5 | Save | Click "Save" |

> **Use for:** VPC Peering (peered VPC CIDR), office networks, CI/CD IP ranges.

#### Removing a Trusted Source

| # | Step | Action |
|---|------|--------|
| 1 | Click | "Edit Trusted Sources" |
| 2 | Find | Source to remove |
| 3 | Click | "X" next to the source |
| 4 | Save | Click "Save" |

> ⚠️ **If you remove the LAST source → empty list → ALL IPs allowed.** Always keep at least one source.

#### Bulk Management Tips

| Tip | Detail |
|-----|--------|
| Use Droplet/DOKS types | Auto-update on infrastructure changes |
| Group by CIDR | One CIDR range covers entire VPC |
| Document all entries | Maintain a spreadsheet/table of trusted sources |
| Review quarterly | Remove stale entries |

#### Audit Checklist — Monthly Review

| # | Check | Action |
|---|-------|--------|
| 1 | List all trusted sources | Screenshot or export |
| 2 | For each IP | Verify resource still exists and needs access |
| 3 | For each Droplet | Verify Droplet still exists |
| 4 | For each DOKS | Verify cluster still exists |
| 5 | For each CIDR | Verify peering still active |
| 6 | Remove stale | Delete any source no longer needed |
| 7 | Document | Log audit date, findings, changes |
| 8 | Verify not empty | Ensure at least one source remains |

#### Emergency: Quick-Add an IP

| Scenario | Action |
|----------|--------|
| App can't connect after deploy | Find app's IP → add to Trusted Sources → retry |
| New developer needs access | Find their IP (`curl ifconfig.me`) → add → verify |
| CI/CD pipeline failing | Find runner IP → add → re-run pipeline |

| # | Step | Time |
|---|------|------|
| 1 | Find IP | 10 seconds |
| 2 | Navigate to Trusted Sources | 15 seconds |
| 3 | Add IP | 10 seconds |
| 4 | Save | 5 seconds |
| 5 | Retry connection | 10 seconds |
| **Total** | | **~50 seconds** |

---

### 8E: Firewall Rules

#### Database-Level vs Droplet vs Cloud Firewall

| Firewall | Scope | Manages |
|----------|-------|---------|
| **Trusted Sources** | Database only | Which IPs can reach the database |
| **Droplet Firewall** (ufw/iptables) | Single Droplet | Which ports are open on that Droplet |
| **DO Cloud Firewall** | Multiple resources | Network-level rules for tagged resources |

#### How They Interact

```
Internet → DO Cloud Firewall → Droplet Firewall → Application → Database Trusted Sources → PostgreSQL
```

> Each layer is independent. A request must pass ALL layers to reach the database.

#### Recommended Firewall Configuration

| Layer | Rule | Detail |
|-------|------|--------|
| **Cloud Firewall** | Allow outbound 25060 | From app resources to database |
| **Droplet Firewall** | Allow outbound 25060 | If ufw is enabled |
| **Trusted Sources** | Add app resources | IP, Droplet, or DOKS |
| **PostgreSQL** | User + password | App-specific credentials |

#### Common Mistakes

| Mistake | Symptom | Fix |
|---------|---------|-----|
| Cloud Firewall blocks 25060 outbound | Connection timeout | Add outbound rule for port 25060 |
| ufw blocks outbound on Droplet | Connection timeout | `ufw allow out 25060/tcp` |
| IP not in Trusted Sources | Connection refused | Add IP to Trusted Sources |
| Wrong security group in DOKS | Pods can't connect | Add DOKS cluster to Trusted Sources |
| Using public host from inside VPC | Higher latency, costs | Switch to private host |

---

## 📋 Section 9: Quick Reference Card

### Connection Decision — One Table

| Your Resource | Same DO Team? | Same DC (ATL1)? | Method | Cost | Latency |
|---------------|---------------|-----------------|--------|------|---------|
| Droplet in ATL1 | ✅ | ✅ | **VPC (Private IP)** | FREE | <1ms |
| DOKS in ATL1 | ✅ | ✅ | **VPC (Private IP)** | FREE | <1ms |
| Droplet in SFO3 | ✅ | ❌ | **VPC Peering** | $0.01/GiB | 30-40ms |
| Droplet in ATL1 (Team B) | ❌ | ✅ | **Public + Trusted Sources** | $0.01/GiB | 2-5ms |
| Droplet in SFO3 (Team B) | ❌ | ❌ | **Public + Trusted Sources** | $0.01/GiB | 35-50ms |
| Local dev laptop | ❌ | ❌ | **Public + Trusted Sources** | $0.01/GiB | Varies |
| CI/CD (GitHub Actions) | ❌ | ❌ | **Public + Trusted Sources** | $0.01/GiB | Varies |

### Connection String Templates

#### Private (Scenario 1 + 2)

```
postgresql://doadmin:<PASSWORD>@private-db-postgresql-atl1-weownnet-do-user-XXXXXXX-0.g.db.ondigitalocean.com:25060/defaultdb?sslmode=require
```

#### Public (Scenario 3 + 4)

```
postgresql://doadmin:<PASSWORD>@db-postgresql-atl1-weownnet-do-user-XXXXXXX-0.g.db.ondigitalocean.com:25060/defaultdb?sslmode=verify-ca&sslrootcert=/path/to/ca-certificate.crt
```

#### Pool Connection

```
postgresql://doadmin:<PASSWORD>@db-postgresql-atl1-weownnet-do-user-XXXXXXX-0.g.db.ondigitalocean.com:25061/<POOL_NAME>?sslmode=require
```

### Emergency Troubleshooting Checklist

| # | Symptom | Check | Fix |
|---|---------|-------|-----|
| 1 | Connection refused | IP in Trusted Sources? | Add IP |
| 2 | Connection timeout | Correct host (private vs public)? | Switch host |
| 3 | Connection timeout | Firewall blocking 25060? | Add outbound rule |
| 4 | SSL error | CA certificate present? | Re-download from DO |
| 5 | Auth failed | Correct password? | Re-copy from dashboard |
| 6 | Too many connections | Check `pg_stat_activity` | Terminate idle, add pool |
| 7 | Read-only mode | Storage full (75 GiB max)? | Delete data or upgrade plan |
| 8 | Slow queries | Cross-DC connection? | Migrate to ATL1 or use private |
| 9 | Pool exhausted | `cl_waiting` > 0? | Increase pool size |
| 10 | Can't connect after resize | App retry logic? | Restart app or wait |

### Key SQL Queries

```sql
-- Active connections
SELECT count(*) FROM pg_stat_activity;

-- Connection limit
SHOW max_connections;

-- Detailed connections
SELECT datname, usename, client_addr, state
FROM pg_stat_activity WHERE state IS NOT NULL;

-- Idle connections (>5 min)
SELECT pid, usename, state, NOW() - state_change AS idle_time
FROM pg_stat_activity
WHERE state = 'idle' AND NOW() - state_change > interval '5 minutes';

-- Kill idle connection
SELECT pg_terminate_backend(<PID>);

-- Database sizes
SELECT datname, pg_size_pretty(pg_database_size(datname))
FROM pg_database ORDER BY pg_database_size(datname) DESC;

-- Am I on private network?
SELECT inet_client_addr();
-- 10.x.x.x = private ✅ | public IP = public ⚠️

-- Pool stats (via pool connection)
SHOW POOLS;
```

### DO Dashboard Shortcuts

| Resource | Path |
|----------|------|
| Database Overview | Databases → db-postgresql-atl1-weownnet |
| Connection Details | Databases → Overview → Connection Details |
| Metrics | Databases → Metrics tab |
| Trusted Sources | Databases → Settings → Trusted Sources |
| Connection Pools | Databases → Connection Pools tab |
| Resize | Databases → Settings → Resize Cluster |
| VPC | Networking → VPC |
| VPC Peering | Networking → VPC → VPC Peering tab |
| Cloud Firewall | Networking → Firewalls |

### Contact / Escalation Path

| Level | Who | When |
|-------|-----|------|
| **L1** | @SHD / @LDC | Connection issues, config questions |
| **L2** | @RMN | Infrastructure, VPC, peering, Helm |
| **L3** | @GTM | Governance, budget approval for upgrades |
| **DO Support** | [cloud.digitalocean.com/support](https://cloud.digitalocean.com/support) | Platform issues, outages |

### Plan Quick Reference

| Plan | Price | Connections | RAM | Storage |
|------|-------|-------------|-----|--------|
| **$15** ← Current | $15/mo | **22** | 1 GB | 15-75 GiB |
| $28 | $28/mo | **47** | 4 GB | 25-150 GiB |
| $60 | $60/mo | **97** | 8 GB | 38-300 GiB |
| $82 | $82/mo | **197** | 16 GB | 80-600 GiB |

> ⚠️ NO DOWNGRADE. Upgrade is permanent.

---

## 📋 Related Documents

| Document | Version | Relevance |
|----------|---------|----------|
| SharedKernel | v3.1.2.1 | Governance source of truth |
| PRJ-009_FedArchExpansion_ETHDenver-CCC-bot | v3.1.2.1 | ATL1 Droplet deployment (uses same DC) |
| GUIDE-006_GitHub-PAT-for-AnythingLLM | v3.1.1.1 | Related infrastructure guide |

### External Sources

| Source | URL |
|--------|-----|
| DigitalOcean Managed Databases | [docs.digitalocean.com/products/databases](https://docs.digitalocean.com/products/databases/) |
| DigitalOcean VPC | [docs.digitalocean.com/products/networking/vpc](https://docs.digitalocean.com/products/networking/vpc/) |
| DigitalOcean VPC Peering | [docs.digitalocean.com/products/networking/vpc/how-to/create-peering](https://docs.digitalocean.com/products/networking/vpc/how-to/create-peering/) |
| DigitalOcean Trusted Sources | [docs.digitalocean.com/products/databases/postgresql/how-to/secure](https://docs.digitalocean.com/products/databases/postgresql/how-to/secure/) |
| DigitalOcean Connection Pools | [docs.digitalocean.com/products/databases/postgresql/how-to/manage-connection-pools](https://docs.digitalocean.com/products/databases/postgresql/how-to/manage-connection-pools/) |
| PgBouncer | [pgbouncer.org](https://www.pgbouncer.org/) |
| PostgreSQL Documentation | [postgresql.org/docs/18](https://www.postgresql.org/docs/18/) |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|--------|
| 3.1.2.1 | 2026-W07 | RMN_2026-W07_004 | **GTM_2026-W07_304** | Initial guide; 9 sections; 4 connection scenarios (VPC, Peering, Public×2); Connection methods deep dive (VPC, Peering, Public, Trusted Sources); Autoscale storage (visual diagram, 10-event walkthrough, cost table); Connection monitoring (6 SQL queries, 5 alert thresholds, Bash+Python scripts, Terraform); Upgrade process (4 plans, NO DOWNGRADE warning, retry logic); Connection pools (PgBouncer, 3 modes, creation, management); Network access (4 layers, firewall interaction); Quick reference card |

---

#FlowsBros #FedArch #PostgreSQL #DigitalOcean #WeOwnSeason003

♾️ WeOwnNet 🌐 | 🏡 Real Estate and 🤝 cooperative ownership for everyone. An 🤗 inclusive community, by 👥 invitation only.
