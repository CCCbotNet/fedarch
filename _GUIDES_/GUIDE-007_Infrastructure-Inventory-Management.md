# 📖 GUIDE-007: Infrastructure Inventory Management

## GUIDE-007_Infrastructure-Inventory-Management_v3.2.0.0.md
## ♾️ WeOwnNet 🌐 — How to Maintain the Living Infrastructure Inventory

| Field | Value |
|-------|-------|
| Guide | GUIDE-007 |
| Version | 3.2.0.0 |
| Purpose | Procedures for maintaining INSTANCE_INVENTORY.md as a living document |
| Audience | Platform Engineers, ADMIN users, Infrastructure Stewards |
| Related | INSTANCE_INVENTORY.md, TMPL-011, SharedKernel (Elevated Registry), BP-027 |

---

## 📖 Table of Contents

1. [Overview](#-overview)
2. [When to Update](#-when-to-update)
3. [Update Process](#-update-process)
4. [Filling Out Each Section](#-filling-out-each-section)
5. [Workflows](#-workflows)
6. [Common Update Scenarios](#-common-update-scenarios)
7. [Quick Commands](#-quick-commands)

---

## 📋 Overview

### Purpose of INSTANCE_INVENTORY.md

The **Infrastructure Instance Inventory** is a **living document** that tracks:
- ✅ All domain/cloud instances (AnythingLLM deployments)
- ✅ Compute, database, and networking resources
- ✅ Team ownership and escalation paths
- ✅ SLA, maintenance windows, and backup strategy
- ✅ Security policy, API key rotation, firewall rules
- ✅ User capacity, growth projections, resource scaling triggers
- ✅ Deployment methods, monitoring, observability
- ✅ Cost tracking and billing

### Key Principle: **LIVING DOCUMENT**

This document is updated **immediately** when:
- New instance deployed
- Owner or team changes
- Resource scaling (compute, storage, database)
- SLA or maintenance window updates
- Security policy changes
- Critical incident or outage

**Update Window:** Within **24 hours** of change; **critical incidents within 1 hour**.

---

## ⏰ When to Update

### IMMEDIATE Updates (Within 1 Hour)

| Trigger | Section to Update | Action |
|---------|-------------------|--------|
| **Critical Outage** | Maintenance & SLA, Update Log | Document incident + estimated resolution |
| **Security Incident** | Security & Access, Maintenance Log | Document breach + remediation steps |
| **Data Loss** | Backup & Disaster Recovery, Update Log | Document recovery status |

### Standard Updates (Within 24 Hours)

| Trigger | Section to Update | Action |
|---------|-------------------|--------|
| New instance deployed | Instance Registry, Resource Allocation | Add entry + populate all fields |
| Owner or team changes | Owner & Team Assignment, On-Call Schedule | Update assignment table |
| Resource scaling | Resource Allocation Details, Capacity & Growth | Document new specs + reason |
| SLA or maintenance window changes | Maintenance & SLA | Update schedule + notify stakeholders |
| API key rotation | Security & Access | Log rotation event in Update Log |
| Backup test completed | Backup & Disaster Recovery | Document test result + date |
| Cost tracking updated | Cost & Billing | Monthly cost reconciliation |

### Regular Scheduled Updates (Weekly/Monthly)

| Frequency | Action | Owner | Section |
|-----------|--------|-------|---------|
| **Daily (passive)** | Monitor growth metrics | @RMN | Capacity & Growth |
| **Weekly** | Review scaling triggers | @RMN | Capacity & Growth, Update Log |
| **Monthly** | Cost reconciliation + trend analysis | @GTM | Cost & Billing |
| **Quarterly** | Disaster recovery drill | @RMN | Backup & Disaster Recovery |
| **Annually** | Full infrastructure audit | @GTM + @RMN | All sections |

---

## 🔄 Update Process

### Step 1: Identify the Change

**When** | **What to Update**
---|---
New instance deployment | "Instance Registry — Active" (add row)
Resource increase | "Resource Allocation Details" (edit existing row)
Team assignment change | "Owner & Team Assignment" (edit ownership)
Maintenance scheduled | "Maintenance & SLA" (add window)
Cost changed | "Cost & Billing" (update monthly cost)
Incident occurs | "Update & Maintenance Log" (add row)

### Step 2: Set #masterCCC (per BP-027)

At the start of your maintenance/deployment session:

```
#masterCCC = GTM_2026-W11_XXX
```

This tracks the governance ID for all related changes.

### Step 3: Make the Change

Edit INSTANCE_INVENTORY.md:
- Add/update rows in relevant section(s)
- Preserve existing content (L-097)
- Follow table format exactly
- Mark unknowns with `?` or `[POPULATE]`
- Mark planned/pending with 📋 or ⬜ emoji

### Step 4: Document in Update Log

Add entry to "Update & Maintenance Log" section:

```markdown
| 2026-03-17 | INT-P01 | Scaled database: Basic → Premium | @RMN | GTM_2026-W11_342 | ✅ Completed |
```

### Step 5: Commit & Push

```bash
git add _INSTANCE_/INSTANCE_INVENTORY.md
git commit -m "[INVENTORY] INT-P01 database scaled to Premium plan (GTM_2026-W11_342)"
```

**Note:** Auto-push happens every 5 minutes. No manual push needed.

### Step 6: Sync to RAG (if ADMIN)

After commit, if you have ADMIN access:
1. Go to ADMIN workspace in any instance
2. Settings → Documents → GitHub connector → Refresh
3. Wait for sync (1-2 minutes)
4. Test retrieval: Fresh session in CCC workspace, query "INT-P01 database size"

### Step 7: Notify Team

If change affects operations:
- **For deployment:** Announce in #WeeklySummary (CCC-ID _001)
- **For outage:** Post #ContextBroadcast to all agents
- **For scaling:** Mention in next team standup

---

## 📋 Filling Out Each Section

### Instance Registry — Active

**Use this when:** New instance deployed or status changes

| Column | What to Fill | Example |
|--------|--------------|---------|
| Instance ID | Format INT-[OGx/Pxx/Sxx/Mxx/Vxx] per R-208 | INT-P01 |
| Type | Production / HomeInstance / Seasonal / META / Verification | Production |
| Name | Human-readable instance name | AI.WeOwn.Agency |
| Domain | FQDN of the instance | ai.weown.agency |
| Owner(s) | @CCC or ORG | @GTM, @THY |
| Team | Which team manages it | Core / WeOwn.Agency |
| Business Purpose | What the instance does | ♾️ #FedArch Hub + Production MAITs |
| Status | ✅ Active / 🔄 Setup / 📋 Planned / ⬜ Reserved | ✅ Active |
| Location | Datacenter region | AWS, DigitalOcean ATL1 |
| Deployed | Date deployed | 2025-Q4 |
| Notes | Any special context | Primary production; 10+ users |

**Example:** New production instance for AgencyPRO:

```markdown
| INT-P05 | Production | AgencyPRO | pro.weown.tools | @GTM | Core | Multi-customer SaaS | ✅ Active | DOKS | 2025-Q4 | Scaling with customers |
```

### Resource Allocation Details

**Use this when:** Resource changes (LLM model, storage, compute, workspaces)

#### For New Instance

Create a new subsection (e.g., "### INT-NEW (Acme AI)"):

```markdown
| Resource | Specification | Capacity | Current Load | Notes |
|----------|---|---|---|---|
| **Platform** | AnythingLLM | v1.11+ | v1.11+ | Core platform |
| **LLM Model** | Qwen3.5-397B-A17B | 397B params | — | Via OpenRouter |
| **Compute** | [POPULATE] | [POPULATE] | [POPULATE] | **[DOCUMENT NEEDED]** |
| **Storage** | PostgreSQL (Managed) | [plan size] | [current estimate] | DigitalOcean Managed |
| **Workspaces** | CCC, tools, ADMIN | All active | [load estimate] | Standard setup |
| **Users** | [count] | Unlimited tier | [load] | Invite-only |
```

#### For Resource Change

Update the row with new values:

```markdown
# Before:
| **Storage** | PostgreSQL (Managed) | 2-50GB tier | ~5GB | DigitalOcean Managed |

# After:
| **Storage** | PostgreSQL (Managed Premium) | 10GB+ | ~5GB | DigitalOcean Managed; upgraded for SaaS |
```

Always add note explaining **why** in the "Notes" column.

### Droplets & Physical Resources

**Use this when:** New droplet created, resized, or decommissioned

| Column | What to Fill | Notes |
|---|---|---|
| Droplet Name | Human-readable identifier | INT-P01-Primary |
| Instance(s) | Which instance(s) run here | INT-P01 |
| Size | DigitalOcean size (s-1vcpu-1gb, etc.) | Standard node for DOKS |
| Region | DO datacenter code | ATL1 (Atlanta) |
| IP | Public IP address (if applicable) | 1.2.3.4 or — (if private) |
| Created | Deployment date | YYYY-MM-DD |
| Backup? | Do we backup this? | ✅ or ❌ |
| Status | 🔄 [POPULATE] = fill in | ✅ |
| Notes | Any special configuration | Auto-scaling enabled |

**Example:**

```markdown
| INT-P02-DOKS-Node-1 | INT-P02 | Standard-2 | ATL1 | — | 2025-Q4 | ✅ | ✅ Active | DOKS cluster node |
```

### Network & Connectivity

**Use this when:** DNS changes, firewall rule updates, VPC configuration

| Column | What to Fill | Example |
|---|---|---|
| Instance | Which instance affected | INT-P01 |
| Region | DO region | ATL1 |
| VPC | Virtual Private Cloud name (if applicable) | WeOwn.Dev VPC |
| Type | Droplet or DOKS | DOKS |
| Public IP | Public IP or — | 1.2.3.4 or — |
| Private IP | Private IP (CIDR) | 10.x.x.x |
| Firewall Rules | What's allowed inbound | Allow: HTTP(80), HTTPS(443) |
| Load Balancer? | ✅ or ❌ | ✅ (if DOKS) |

### Owner & Team Assignment

**Use this when:** Ownership changes, backup contact updates, on-call rotation changes

| Column | What to Fill | Example |
|---|---|---|
| Instance | INT-XXX | INT-P01 |
| Owner(s) | @CCC or multiple | @GTM, @THY |
| Team | Team name | Core / WeOwn.Agency |
| Backup Contact | Who steps in if owner unavailable | @RMN |
| Escalation | Who to call for critical issues | @RMN (CTO) |
| CCC-ID | Tracking ID for this assignment | GTM_2026-W11_342 |

**Example:**

```markdown
| INT-P02 | @LDC | BurnedOut.Media | @GTM | @RMN | LDC_2026-W11_001 |
```

### Maintenance & SLA

**Use this when:** SLA changes, maintenance window scheduled, update policy changes

| Column | What to Fill | Example |
|---|---|---|
| Instance | INT-XXX | INT-P01 |
| Target Uptime | 99.0%, 99.5%, or 99.9% | 99.5% |
| Maintenance Window | Preferred maintenance time (UTC+/-) | Sundays 00:00-04:00 EST |
| Backup Schedule | How often backups run | Daily 02:00 EST |
| Update Policy | When security patches applied | Monthly (Patch Tuesday) |
| Notes | Rationale for SLA level | Mission-critical; business hours preferred |

### Security & Access

**Use this when:** API keys rotated, firewall rules change, auth method changes

Update relevant row with:
- **Auth Method:** LDAP, API key, 2FA, etc.
- **API Keys:** Rotation cadence per BP-064
- **Rotation Date:** When last rotated
- **Manager:** Who manages credentials
- **Storage:** Where keys stored (Infisical, DO, etc.)

**Example — API Key Rotation Log:**

```markdown
| OpenRouter | INT-P01 | 7-day rotation (shared) | ADMIN | Infisical (Tier 2) | ✅ Implemented |
| Updated: 2026-03-15 | Next rotation: 2026-03-22 | Key ID: xxx*** | Status: Active |
```

### Capacity & Growth

**Use this when:** User count changes, adding more customers, detecting growth trends

| Column | What to Fill | Notes |
|---|---|---|
| Instance | INT-XXX | Affected instance |
| Current Users | Count | 10+, 5+, etc. |
| Max Capacity | Estimated before scaling | 50-100 (est.) |
| Growth Rate | Users per time period | +2-3 users/week |
| 12-Month Projection | Forecast | 50-75 users by Q1 2027 |
| Notes | Business context | Core team + community |

**Example:**

```markdown
| INT-P05 | 5+ core | 500+ | +50 users/quarter | 100-200 SaaS users | AgencyPRO commercial customers |
```

### Update & Maintenance Log

**Use this when:** ANY change made to the inventory

| Column | What to Fill | Example |
|---|---|---|
| Date | YYYY-MM-DD | 2026-03-17 |
| Instance | INT-XXX or ALL (if affects multiple) | INT-P01 |
| Change | What changed? | Scaled database: Basic → Premium |
| Owner | @CCC | @RMN |
| CCC-ID | Governance tracking | GTM_2026-W11_342 |
| Status | ✅ Completed / 🔄 In Progress / 📋 Planned | ✅ Completed |

**Example:**

```markdown
| 2026-03-17 | INT-P01 | Scaled PostgreSQL from Basic to Premium plan (L-123) | @RMN | GTM_2026-W11_342 | ✅ Completed |
```

---

## 🔄 Workflows

### Workflow 1: Deploy New Instance

**Timeline:** Day 1 of deployment

1. **Use TMPL-011** — Deploy from template checklist
2. **Fill in Instance Registry — Active:**
   - Add new row with instance ID, name, domain, owner, team, purpose, status, location
   - Mark status: 🔄 Setup (until fully verified)
3. **Fill in Resource Allocation Details:**
   - Create new subsection with all resource specs
   - Mark unknowns as `?` or `[POPULATE]`
4. **Fill in Owner & Team Assignment:**
   - Add owner, backup contact, escalation path
   - Use CCC-ID from deployment tracking
5. **Fill in Maintenance & SLA:**
   - Set target uptime SLA
   - Define maintenance window
   - Document backup and update policy
6. **Commit & Push:**
   ```
   git add _INSTANCE_/INSTANCE_INVENTORY.md
   git commit -m "[DEPLOYMENT] Deployed INT-S003 shared seasonal instance (GTM_2026-W11_XXX)"
   ```
7. **Announce:** Mention in #WeeklySummary

**When ISC Certified (within 2 weeks):**

8. Update Instance Registry status: 🔄 Setup → ✅ Active
9. Commit: `[ISC] INT-S003 certified for #WeOwnSeason003`

---

### Workflow 2: Scale Resource (Database, Compute)

**Timeline:** Within 24 hours of scaling

1. **Identify change:**
   - Old: Basic PostgreSQL (22 connections)
   - New: Premium PostgreSQL (connection pooling + 5GB storage)
   - Reason: AgencyPRO growing; connection limit hit

2. **Update Resource Allocation Details:**
   - Find the instance section (INT-P05)
   - Update Storage row: Add new plan, note pooling
   - Add note: "Upgraded from Basic due to connection limit (L-123)"

3. **Update Capacity & Growth:**
   - If scaling due to user growth, update user count
   - Update growth trend if applicable

4. **Update Update & Maintenance Log:**
   ```
   | 2026-03-18 | INT-P05 | Upgraded PostgreSQL: Basic → Premium + PgBouncer pooling | @RMN | GTM_2026-W11_350 | ✅ Completed |
   ```

5. **Commit:**
   ```
   git add _INSTANCE_/INSTANCE_INVENTORY.md
   git commit -m "[SCALING] INT-P05 database upgrade: Basic → Premium (GTM_2026-W11_350)"
   ```

6. **Monitor:** Track cost impact in "Cost & Billing" section next month

---

### Workflow 3: Critical Incident

**Timeline:** Within 1 hour of discovery

1. **Document in Update & Maintenance Log (URGENT):**
   ```
   | 2026-03-20 | INT-P01 | 🚨 OUTAGE: Database connection pool exhausted | @RMN | GTM_2026-W11_368 | 🔄 RESOLVING |
   ```

2. **Post #ContextBroadcast to all agents:**
   ```
   📢 #ContextBroadcast | AI:@GTM → ALL AGENTS | Mar 20 | 14:30 EST
   
   ALERT: INT-P01 experiencing database connection exhaustion.
   ETA for resolution: 2026-03-20 15:00 EST
   Impact: Users may see slow responses / timeout errors.
   ```

3. **Update Status Temporarily:**
   ```
   | INT-P01 | ... | 🚨 DOWN (DB CONNECTION POOL) | ... |
   ```

4. **When Resolved:**
   - Update Update Log: Status → ✅ Resolved
   - Document root cause
   - Update Maintenance & SLA if SLA impacted
   - Add Learning (L-XXX) if systemic issue

---

### Workflow 4: API Key Rotation (BP-064)

**Timeline:** Per rotation cadence (7 days for shared, 30 days for personal)

1. **Set reminder:** 24h before key expiry

2. **Rotate in Infisical (Tier 2) or DO console (Tier 1):**
   - Generate new OpenRouter API key
   - Update instance settings with new key
   - Logout/login to refresh session
   - Verify LLM works (smoke test)
   - Revoke old key

3. **Update Security & Access section:**
   ```
   | OpenRouter | INT-P01 | 7-day rotation (shared) | ADMIN | Infisical | ✅ |
   | Last rotated: 2026-03-17 | Next: 2026-03-24 | Status: Active |
   ```

4. **Log in Update & Maintenance Log:**
   ```
   | 2026-03-17 | INT-P01 | OpenRouter API key rotated (7-day cycle, BP-064) | @RMN | GTM_2026-W11_342 | ✅ |
   ```

5. **Commit:**
   ```
   git commit -m "[SECURITY] API key rotation INT-P01 (GTM_2026-W11_342)"
   ```

---

## 📋 Common Update Scenarios

### Scenario 1: "User Growth Detected"

**You notice:** INT-P01 went from 8 to 12 users this week

**Action:**
1. Update "Capacity & Growth" → Current Users: 10+ → 12+
2. Update growth rate if trend continues
3. Update 12-month projection if needed
4. Log in Update Log: `User growth: INT-P01 reached 12 active users`

### Scenario 2: "Database Size Increasing Fast"

**You notice:** INT-P05 storage at 7GB of 10GB (70%)

**Action:**
1. Review Capacity & Growth scaling triggers
2. If >85%, trigger scale-up per BP/L-123
3. In Resource Allocation Details, note trend: "Storage trending 1GB/month; plan upgrade in Q2"
4. Update Update Log with observation

### Scenario 3: "New Team Member Joins"

**You need to:** Add @CEO (Stephanie Warlick) as observer for INT-P01

**Action:**
1. Update Owner & Team Assignment → Add Backup Contact or note in "On-Call Schedule"
2. If giving admin access, also update Security & Access matrix
3. Log: `New team member added: @CEO (observer, INT-P01)`

### Scenario 4: "Disaster Recovery Test Completed"

**You completed:** Restore INT-P02 from 24-hour-old backup

**Action:**
1. Update Backup & Disaster Recovery → "Last Test" row for INT-P02
2. Document result: "✅ Database restored successfully in 18 minutes; full test pass"
3. Note any findings in "Backup Testing" section
4. Log in Update Log: `DR test completed: INT-P02 database restore (18 min RTO)`

---

## 🚀 Quick Commands

### List All Active Instances

```markdown
"Show me all active instances"

Grep in inventory:
- Instance Registry — Active section
- Filter: Status = ✅ Active
- Count: 6 instances
```

### Find Instance by Domain

```
"What instance runs ai.weown.agency?"

Answer: INT-P01 (AI.WeOwn.Agency)
Owner: @GTM + @THY
```

### Check SLA & Maintenance Window

```
"What's the maintenance window for INT-P02?"

Answer: Sundays 02:00-06:00 EST
SLA: 99.0% uptime
Next scheduled maintenance: [Check calendar]
```

### Monitor Resource Usage

```
"Is INT-P05 close to any scaling limits?"

Check:
- Database connections: N/22 (PgBouncer pools to ~44)
- Storage: N% of 10GB
- CPU/Memory: [From monitoring dashboard]

Scaling triggers in Capacity & Growth section
```

### Who to Contact for Instance Down?

```
"INT-P01 is down. Who do I call?"

Owner: @GTM + @THY
Backup: @RMN
Escalation: @RMN (CTO)

On-call: [Check On-Call Schedule]
Contact: Signal: ♾️ WeOwn.Agency 👥
```

---

## ✅ Checklist: Before You Commit

- ☐ All changes documented with #masterCCC
- ☐ Updated correct section(s)
- ☐ Followed table format (markdown pipe syntax)
- ☐ Preserved existing content (L-097 — no deletions)
- ☐ Marked unknowns clearly (`?`, `[POPULATE]`, `[DOCUMENT NEEDED]`)
- ☐ Added entry to "Update & Maintenance Log"
- ☐ Commit message is clear and includes CCC-ID
- ☐ Notified team if change affects operations
- ☐ Will trigger RAG sync post-push (wait 5 min)

---

## 🔗 Related Documents

| Document | Purpose | URL |
|---|---|---|
| INSTANCE_INVENTORY.md | The living inventory itself | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_INSTANCE_/INSTANCE_INVENTORY.md) |
| TMPL-011 | Deployment checklist (use for new instances) | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_TEMPLATES_/TMPL-011_Instance-Deployment-Checklist.md) |
| SharedKernel | Instance definitions (D-053→D-057) + rules | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/SharedKernel.md) |
| BEST-PRACTICES | Instance setup (BP-025, BP-051), ISC (BP-059) | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/BEST-PRACTICES.md) |
| BP-027 | #masterCCC requirement | SharedKernel.md |
| BP-064 | API key rotation policy | BEST-PRACTICES.md |
| L-097 | Preserve existing content on regeneration | SharedKernel.md |
| L-123 | Database connection pooling + upgrade strategy | SharedKernel.md |

---

## 📝 Version History

| Version | Date | Changes |
|---------|------|---------|
| 3.2.0.0 | 2026-W11 | 🚀 **INITIAL RELEASE** — Complete guide for maintaining INSTANCE_INVENTORY.md; 7 sections: overview, when to update, process, filling out sections, workflows, scenarios, quick commands; 4 detailed workflows (deploy, scale, incident, key rotation); aligned with BP-027, L-097, BP-064 |

---

#FlowsBros #FedArch #Guide #Infrastructure #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
