# PRJ-024_Secrets-Management-Infisical.md

## 📋 Document Metadata

| Field | Value |
|-------|-------|
| **Document** | PRJ-024_Secrets-Management-Infisical.md |
| **Version** | **v3.2.3.1** |
| **CCC-ID** | RMN_2026-W12_069 |
| **Approval CCC-ID** | GTM_2026-W11_328 |
| **Created** | 2026-W12 |
| **Updated** | **2026-03-19 (W12)** |
| **Season** | #WeOwnSeason003 🚀 |
| **Status** | 🔄 IN PROGRESS — ❌ BROKEN (INT-P01 K8s only) |
| **#LLMmodel** | Claude Sonnet 4.6 |
| **Source of Truth** | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-024_Secrets-Management-Infisical.md) |
| **R-199** | Credentials = RAG ONLY, NEVER GitHub |

---

## 📖 Table of Contents

1. [Project Identity](#-project-identity)
2. [Executive Summary](#-executive-summary)
3. [Infisical Architecture — Complete Overview](#-infisical-architecture--complete-overview)
4. [Deployment Methods — Helm (K8s) vs Docker Compose](#-deployment-methods--helm-k8s-vs-docker-compose)
5. [API Key Rotation — Full Automation Options](#-api-key-rotation--full-automation-options)
6. [Instance Integration Status](#-instance-integration-status)
7. [@SHD Docker PR — Status](#-shd-docker-pr--status)
8. [Secrets Inventory — What Needs to Be Stored](#-secrets-inventory--what-needs-to-be-stored)
9. [P0 Tasks — Critical](#-p0-tasks--critical)
10. [P1 Tasks — Important](#-p1-tasks--important)
11. [P2 Tasks — Nice to Have](#-p2-tasks--nice-to-have)
12. [Learnings Locked (PRJ-024)](#-learnings-locked-prj-024)
13. [Related PRJs](#-related-prjs)
14. [Version History](#-version-history)
15. [Related Documents](#-related-documents)
16. [Discovered By (BP-047)](#-discovered-by-bp-047)
17. [Governance Compliance](#-governance-compliance)

---

## 📋 Project Identity

| Field | Value |
|-------|-------|
| Project ID | **PRJ-024** |
| Title | **Secrets Management (Infisical)** |
| Type | Infrastructure — Security + Secrets |
| Priority | 🔴 P0 |
| Owner | @RMN (Roman Di Domizio) |
| Status | 🔄 IN PROGRESS — ❌ BROKEN (INT-P01 K8s only) — ⬜ NOT STARTED (all other instances) |
| #masterCCC | GTM_2026-W10_026 |
| Approval CCC-ID | GTM_2026-W11_328 |

---

## 📋 Executive Summary

### What Is PRJ-024?

PRJ-024 implements Infisical as the centralized secrets management platform for the ♾️ WeOwnNet 🌐 ecosystem. This includes:

- **Secrets Storage** — Centralized vault for API keys, database credentials, tokens
- **Secret Sync** — Automatic sync to Kubernetes pods (Infisical Operator) and Docker containers (SDK/API)
- **API Key Rotation** — Automated rotation for OpenRouter, Anthropic, and other providers (7D/30D cycles per BP-064)
- **Access Control** — Per-instance, per-service secret access with audit logging
- **Compliance** — Meets SOC 2, ISO 27001 requirements for secrets management

### Current Status

| Component | Status | Notes |
|-----------|--------|-------|
| **Infisical Account** | ✅ Created | Cloud-hosted (Infisical.com) |
| **INT-P01 (DOKS)** | ❌ BROKEN (50%) | K8s operator deployed but not syncing secrets properly |
| **INT-OG1 (DOKS)** | ⬜ NOT STARTED | DOKS cluster — needs Infisical Operator integration |
| **INT-OG8 (DOKS)** | ⬜ NOT STARTED | DOKS cluster — needs Infisical Operator integration |
| **jAIMSnet (DOKS)** | ⬜ NOT STARTED | DOKS cluster — needs Infisical Operator integration |
| **INT-P02 (Droplet)** | ⬜ NOT STARTED | Docker Droplet — needs Infisical SDK/init container |
| **All other instances (Droplets)** | ⬜ NOT STARTED | Docker Droplets (being deployed) — need Infisical integration |
| **n8n (DOKS)** | ⬜ NOT STARTED | Workflow automation — needs Infisical integration |
| **Rotation Automation** | ⬜ NOT STARTED | n8n workflow, agent skill, or cronjob (TBD) |

> **⚠️ IMPORTANT:** Infisical is 50% complete ONLY for INT-P01. All other instances have ZERO Infisical integration. This is a significant security gap across the entire ecosystem.

### Instance Architecture Clarification

| Instance Type | Instances | Infisical Method |
|---------------|-----------|------------------|
| **DOKS Clusters** | INT-P01, INT-OG1, INT-OG8, jAIMSnet, n8n.weown.app | Infisical Operator (Helm) |
| **Docker Droplets** | INT-P02 + all others being deployed | Infisical SDK or init container |

### Why This Matters

| Without PRJ-024 | With PRJ-024 |
|-----------------|--------------|
| Manual API key management | ✅ Centralized vault + auto-sync |
| No rotation (security risk) | ✅ 7D/30D automated rotation (BP-064) |
| Shared keys across instances | ✅ Per-instance virtual keys |
| No audit trail | ✅ Full access logging |
| Key exposure in env files | ✅ Encrypted at rest + in transit |
| INT-P01 incidents (key lost) | ✅ Automatic recovery from vault |

### The INT-P01 Incident (Mon 3/2, W10)

| Event | Detail |
|-------|--------|
| **What Happened** | INT-P01 OOM crash + Infisical broken + API key lost |
| **Discovery** | Mon 3/2 — INT-P01 unresponsive, manual API key restore required |
| **Root Cause** | K8s operator not syncing secrets properly after pod restart |
| **Impact** | Manual API key management until fixed |
| **Resolution** | Manual API key restore, Infisical investigation ongoing |
| **Time Lost** | ~2h incident response + ~3h Infisical debugging |

---

## 📋 Infisical Architecture — Complete Overview

### What Is Infisical?

| Field | Value |
|-------|-------|
| **Name** | Infisical |
| **Type** | Open-source secrets management platform |
| **License** | MIT (FOSS) |
| **Deployment** | Cloud (Infisical.com) or Self-hosted |
| **Current** | Cloud-hosted (free tier) |
| **Features** | Secret vault, sync to K8s/Docker, API key rotation, audit logs, access control |
| **URL** | [infisical.com](https://infisical.com) |

### Infisical Components

| Component | Purpose | Deployment |
|-----------|---------|------------|
| **Infisical Vault** | Centralized secret storage | Cloud (Infisical.com) |
| **Infisical Operator** | K8s CRD + controller for secret sync | DOKS clusters (INT-P01, INT-OG1, INT-OG8, jAIMSnet) |
| **Infisical SDK** | Library for Docker/container secret fetch | Docker Droplets (INT-P02 + others) |
| **Infisical CLI** | Command-line tool for secret management | Local dev, CI/CD |
| **Infisical API** | REST API for programmatic access | n8n workflows, custom scripts |

### Secret Sync Methods

| Method | Target | Automation Level | Notes |
|--------|--------|------------------|-------|
| **Infisical Operator (K8s)** | DOKS clusters | Partial (sync only) | Requires K8s CRD + controller |
| **Infisical SDK (Docker)** | Docker Droplets | Partial (sync only) | Requires app code integration |
| **Infisical API + n8n** | Any system | Full (sync + rotation) | Custom workflow |
| **Infisical API + Cronjob** | Any system | Full (sync + rotation) | K8s CronJob or Docker cron |
| **AnythingLLM Agent Skill** | AnythingLLM | Full (sync + rotation) | Custom skill development |

> **⚠️ CRITICAL:** Infisical Operator enables secret SYNC but NOT automatic ROTATION. Rotation requires an additional workflow (n8n recommended).

---

## 📋 Deployment Methods — Helm (K8s) vs Docker Compose

### Method A: Helm Chart (DOKS Clusters)

**Target:** INT-P01, INT-OG1, INT-OG8, jAIMSnet

#### Prerequisites

| Requirement | Detail |
|-------------|--------|
| Kubernetes cluster | v1.25+ |
| Helm | v3.12+ |
| Infisical account | Cloud or self-hosted |
| Service account | K8s service account with appropriate RBAC |

#### Helm Installation (Infisical Operator)

```bash
# 1. Add Infisical Helm repo
helm repo add infisical https://infisical.github.io/infisical-helm
helm repo update

# 2. Create namespace
kubectl create namespace infisical-system

# 3. Install Infisical Operator
helm install infisical-operator infisical/infisical-operator \
  --namespace infisical-system \
  --set infisical.apiHost=https://app.infisical.com \
  --set infisical.token=<INFISICAL_SERVICE_TOKEN>

# 4. Verify installation
kubectl get pods -n infisical-system
kubectl get secretsync -n infisical-system
```

#### SecretSync CRD Example

```yaml
apiVersion: secrets.infisical.com/v1alpha1
kind: SecretSync
metadata:
  name: openrouter-secret
  namespace: default
spec:
  infisicalToken: <INFISICAL_SERVICE_TOKEN>
  projectId: <PROJECT_ID>
  environment: production
  secrets:
    - name: OPENROUTER_API_KEY
      key: openrouter-api-key
    - name: ANTHROPIC_API_KEY
      key: anthropic-api-key
  output:
    type: kubernetes-secret
    name: infisical-secrets
```

#### Pod Integration

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: anythingllm
  namespace: default
spec:
  containers:
  - name: anythingllm
    image: mintplexlabs/anythingllm:latest
    envFrom:
    - secretRef:
        name: infisical-secrets
```

#### Debugging INT-P01 Operator

```bash
# Check operator logs
kubectl logs -n infisical-system deployment/infisical-operator -f

# Check RBAC
kubectl auth can-i get secrets --as=system:serviceaccount:infisical-system:infisical-operator

# Test SecretSync CRD
kubectl get secretsync -A
kubectl describe secretsync openrouter-secret -n default

# Force sync
kubectl annotate secretsync openrouter-secret -n default infisical.com/force-sync=true
```

---

### Method B: Docker Compose (Droplets)

**Target:** INT-P02 + all other Docker Droplet instances

#### Prerequisites

| Requirement | Detail |
|-------------|--------|
| Docker | v24+ |
| Docker Compose | v2.20+ |
| Infisical account | Cloud or self-hosted |
| Infisical CLI | Installed on host (optional) |

#### Option 1: Infisical SDK Integration (App Code)

```python
# Python example (AnythingLLM custom wrapper)
from infisical import InfisicalClient

client = InfisicalClient(token="INFISICAL_SERVICE_TOKEN")

# Fetch secrets
secrets = client.get_secrets(
    project_id="PROJECT_ID",
    environment="production"
)

# Use in app
OPENROUTER_API_KEY = secrets["openrouter-api-key"]
```

#### Option 2: Infisical CLI + Env File

```bash
# 1. Install Infisical CLI
curl -1sLf 'https://dl.cloudsmith.io/public/infisical/infisical-cli/setup.deb.sh' | sudo -E bash
sudo apt install infisical

# 2. Login
infisical login

# 3. Download secrets to env file
infisical secrets scan --env-file > .env.infisical

# 4. Use in Docker Compose
docker compose --env-file .env.infisical up -d
```

#### Option 3: Docker Init Container (Recommended)

```yaml
# docker-compose.yml
version: '3.8'

services:
  infisical-fetch:
    image: infisical/infisical-cli:latest
    command: ["infisical", "secrets", "scan", "--env-file", "/tmp/.env"]
    environment:
      - INFISICAL_TOKEN=${INFISICAL_SERVICE_TOKEN}
    volumes:
      - infisical-secrets:/tmp
    restart: "no"

  anythingllm:
    image: mintplexlabs/anythingllm:latest
    depends_on:
      infisical-fetch:
        condition: service_completed_successfully
    env_file:
      - /tmp/.env
    volumes:
      - infisical-secrets:/tmp

volumes:
  infisical-secrets:
```

---

## 📋 API Key Rotation — Full Automation Options

### Rotation Requirements (BP-064)

| Requirement | Detail |
|-------------|--------|
| **Rotation Frequency** | 7 days (high-security) or 30 days (standard) |
| **Providers** | OpenRouter, Anthropic, DO API, Infisical itself |
| **Notification** | Alert before rotation (24h warning) |
| **Rollback** | Previous key retained for 24h post-rotation |
| **Audit** | Log all rotation events |
| **Verification** | Test new key before activating |

---

### Option A: n8n Workflow (Recommended ✅)

| Component | Detail |
|-----------|--------|
| **Orchestrator** | n8n.weown.app (DOKS, ATL1) |
| **Schedule** | Cron: `0 0 */7 * *` (every 7 days) or `0 0 1 * *` (monthly) |
| **Integration** | Infisical API + Provider API (OpenRouter, Anthropic) |
| **Notification** | Signal webhook, email, or Slack |
| **Rollback** | Store previous key in Infisical (versioned) |

#### n8n Workflow Architecture

```
Cron Trigger (every 7 days)
    │
    ▼
Fetch Current Key (Infisical API)
    │
    ▼
Generate New Key (Provider API)
    │
    ├──→ Store New Key (Infisical API)
    │   └──→ Version: v2 (v1 retained for 24h)
    │
    ├──→ Notify Team (Signal webhook)
    │   └──→ "API key rotated — v2 active, v1 expires in 24h"
    │
    ├──→ Test New Key (HTTP Request)
    │   └──→ Verify new key works
    │
    └──→ Delete Old Key (after 24h)
        └──→ Infisical API — remove v1
```

#### n8n Nodes Required

| Node | Purpose |
|------|---------|
| Cron | Schedule trigger |
| HTTP Request | Infisical API calls |
| HTTP Request | Provider API (OpenRouter, Anthropic) |
| Code | Key validation, error handling |
| Signal/Slack | Notification |
| Wait | 24h delay before deleting old key |

---

### Option B: AnythingLLM Agent Skill

| Component | Detail |
|-----------|--------|
| **Orchestrator** | AnythingLLM custom skill |
| **Schedule** | AnythingLLM scheduler or external trigger |
| **Integration** | Infisical API + Provider API via LLM tool calls |
| **Notification** | In-chat notification or webhook |
| **Rollback** | Store previous key in Infisical (versioned) |

#### Agent Skill Architecture

```
User Command: "/rotate-keys"
    │
    ▼
AnythingLLM Skill (custom Python/JS)
    │
    ▼
Infisical API Call (fetch current key)
    │
    ▼
Provider API Call (generate new key)
    │
    ▼
Infisical API Call (store new key, version)
    │
    ▼
Response to User: "✅ Keys rotated — v2 active"
```

#### Skill Code Structure

```python
# AnythingLLM custom skill
from infisical import InfisicalClient
import openrouter

def rotate_api_keys(provider="openrouter"):
    client = InfisicalClient(token="INFISICAL_SERVICE_TOKEN")
    current_key = client.get_secret("openrouter-api-key")
    new_key = openrouter.rotate_key(current_key)
    client.update_secret("openrouter-api-key", new_key, version="v2")
    return "✅ API keys rotated successfully"
```

---

### Option C: K8s CronJob (DOKS Clusters)

| Component | Detail |
|-----------|--------|
| **Orchestrator** | Kubernetes CronJob |
| **Schedule** | Cron: `0 0 */7 * *` (every 7 days) |
| **Integration** | Python/Go script with Infisical SDK |
| **Notification** | Kubernetes events + webhook |
| **Rollback** | Store previous key in Infisical (versioned) |

#### CronJob Manifest

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: api-key-rotation
  namespace: infisical-system
spec:
  schedule: "0 0 */7 * *"
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: rotation-script
            image: python:3.12-slim
            command: ["python", "/scripts/rotate_keys.py"]
            env:
            - name: INFISICAL_TOKEN
              valueFrom:
                secretKeyRef:
                  name: infisical-credentials
                  key: token
            volumeMounts:
            - name: scripts
              mountPath: /scripts
          restartPolicy: OnFailure
          volumes:
          - name: scripts
            configMap:
              name: rotation-scripts
```

#### Rotation Script (Python)

```python
# /scripts/rotate_keys.py
from infisical import InfisicalClient
import requests
import os

def rotate_keys():
    client = InfisicalClient(token=os.environ["INFISICAL_TOKEN"])
    current_key = client.get_secret("openrouter-api-key")
    new_key = requests.post(
        "https://openrouter.ai/api/v1/keys/rotate",
        headers={"Authorization": f"Bearer {current_key}"}
    ).json()["new_key"]
    client.update_secret("openrouter-api-key", new_key, version="v2")
    print("✅ Keys rotated successfully")

if __name__ == "__main__":
    rotate_keys()
```

---

### Option D: Docker Cronjob (Droplets)

| Component | Detail |
|-----------|--------|
| **Orchestrator** | Docker container with cron |
| **Schedule** | Cron: `0 0 */7 * *` (every 7 days) |
| **Integration** | Python/Shell script with Infisical CLI |
| **Notification** | Email or webhook |
| **Rollback** | Store previous key in Infisical (versioned) |

#### Docker Compose (Cron Service)

```yaml
services:
  key-rotation:
    image: python:3.12-slim
    command: ["cron", "-f"]
    volumes:
      - ./scripts:/scripts
      - /var/spool/cron:/var/spool/cron
    environment:
      - INFISICAL_TOKEN=${INFISICAL_SERVICE_TOKEN}
    restart: unless-stopped
```

#### Crontab Entry

```bash
# /etc/cron.d/key-rotation
0 0 */7 * * root cd /scripts && python rotate_keys.py >> /var/log/key-rotation.log 2>&1
```

---

### Rotation Option Comparison

| Option | Dev Time | Maintenance | Reliability | Flexibility | Recommendation |
|--------|:--------:|:-----------:|:-----------:|:-----------:|:--------------:|
| **n8n Workflow** | 4-6h | 0.5h/month | High | High | ✅ **RECOMMENDED** |
| **Agent Skill** | 6-8h | 1h/month | Medium | Medium | 🟡 Alternative |
| **K8s CronJob** | 3-5h | 0.5h/month | High | Medium | 🟡 For K8s-only |
| **Docker Cron** | 2-4h | 0.5h/month | Medium | High | 🟡 For Docker-only |

> **Recommendation:** n8n is already deployed, monitored, and proven. One n8n workflow covers both K8s and Docker instances — no additional infrastructure required.

---

## 📋 Instance Integration Status

### DOKS Clusters (Infisical Operator via Helm)

| Instance | Owner | Status | Priority | Notes |
|----------|-------|--------|----------|-------|
| **INT-P01** | We Own Labs | ❌ BROKEN (50%) | 🔴 P0 | Operator deployed, not syncing after pod restart |
| **INT-OG1** | @GTM + @THY | ⬜ NOT STARTED | 🟠 P1 | Same cluster as INT-P01 — can share operator |
| **INT-OG8** | @RMN | ⬜ NOT STARTED | 🟠 P1 | Same cluster as INT-P01 — can share operator |
| **jAIMSnet** | Platform Hub | ⬜ NOT STARTED | 🔴 P0 | Hosts LiteLLM + Langfuse secrets |

### Docker Droplets (Infisical SDK or Init Container)

| Instance | Owner | Status | Priority | Notes |
|----------|-------|--------|----------|-------|
| **INT-P02** | 🔥 BurnedOut.Media | ⬜ NOT STARTED | 🟠 P1 | @SHD Docker PR being revised |
| **All others (deploying)** | Various | ⬜ NOT STARTED | 🟠 P1 | New instances as team grows — all Docker Droplets |
| **n8n** | Workflow Automation | ⬜ NOT STARTED | 🔴 P0 | Critical for rotation workflow |

---

## 📋 @SHD Docker PR — Status

### PR Details

| Field | Value |
|-------|-------|
| **Repo** | `weownnetwork/ai` → `anythingllm/docker/` |
| **Delivered** | Feb 23, 2026 |
| **Reviewed By @RMN** | ✅ W12 (a few days ago) |
| **Feedback Given** | ✅ @RMN reviewed + provided updated instructions |
| **Current Status** | ⏳ Waiting for @SHD to revise + push updated changes |
| **Next Action** | @SHD pushes revised PR with @RMN's updated instructions |
| **Blocks** | INT-P02 + all Docker Droplet Infisical setup |

### Expected PR Contents (After @SHD Revision)

| File | Purpose |
|------|---------|
| `docker-compose.yml` | Infisical init container + AnythingLLM |
| `.env.infisical.example` | Environment variable template |
| `README.md` | Infisical setup instructions for Docker |
| `infisical-config.json` | Infisical SDK configuration |

### Next Steps for @SHD PR

| # | Action | Owner | Timeline |
|---|--------|-------|----------|
| 1 | Revise PR with @RMN's updated instructions | @SHD | W12 (awaiting) |
| 2 | Push updated changes | @SHD | W12 |
| 3 | @RMN review round 2 | @RMN | After @SHD push |
| 4 | Merge to main | @RMN | After approval |
| 5 | Deploy to INT-P02 | @SHD | After merge |
| 6 | Deploy to all other Docker Droplets | @RMN | After merge |

---

## 📋 Secrets Inventory — What Needs to Be Stored

### API Keys

| Secret | Provider | Rotation | Priority |
|--------|----------|----------|----------|
| `OPENROUTER_API_KEY` | OpenRouter | 7 days | 🔴 P0 |
| `ANTHROPIC_API_KEY` | Anthropic | 30 days | 🟠 P1 |
| `DIGITALOCEAN_TOKEN` | DigitalOcean | 90 days | 🟠 P1 |
| `GITHUB_TOKEN` | GitHub | 90 days | 🟡 P2 |
| `PROTONMAIL_API_KEY` | ProtonMail | 90 days | 🟡 P2 |

### Database Credentials

| Secret | Database | Rotation | Priority |
|--------|----------|----------|----------|
| `PGSQL_HOST` | DO Managed PG | Static | 🔴 P0 |
| `PGSQL_PORT` | DO Managed PG | Static | 🔴 P0 |
| `PGSQL_USER` | DO Managed PG | 90 days | 🟠 P1 |
| `PGSQL_PASSWORD` | DO Managed PG | 90 days | 🟠 P1 |
| `PGSQL_DATABASE` | DO Managed PG | Static | 🔴 P0 |

### Application Secrets

| Secret | Service | Rotation | Priority |
|--------|---------|----------|----------|
| `INFISICAL_SERVICE_TOKEN` | Infisical | 90 days | 🔴 P0 |
| `N8N_ENCRYPTION_KEY` | n8n | Static | 🔴 P0 |
| `LANGFUSE_SECRET_KEY` | Langfuse | 90 days | 🟠 P1 |
| `LANGFUSE_PUBLIC_KEY` | Langfuse | Static | 🟠 P1 |
| `LITELLM_MASTER_KEY` | LiteLLM | 90 days | 🟠 P1 |

### Total Secrets Summary

| Category | Total | P0 | P1/P2 |
|----------|:-----:|:--:|:-----:|
| API Keys | 5 | 1 | 4 |
| Database Credentials | 5 | 3 | 2 |
| Application Secrets | 5 | 2 | 3 |
| **TOTAL** | **15** | **6** | **9** |

---

## 📋 P0 Tasks — Critical

| # | Task | Action | Status | Blocks |
|---|------|--------|--------|--------|
| 1 | Debug INT-P01 Infisical Operator | Check logs, verify RBAC, test SecretSync CRD | ❌ BROKEN | PRJ-016, PRJ-017 |
| 2 | Await @SHD revised Docker PR | @SHD pushing updated changes per @RMN feedback | ⏳ Awaiting @SHD | INT-P02 + all Droplets |
| 3 | Set up Infisical for jAIMSnet | Deploy Operator via Helm, configure secrets | ⬜ TODO | PRJ-016, PRJ-017 |
| 4 | Set up Infisical for n8n | Deploy Operator via Helm, configure secrets | ⬜ TODO | Rotation workflow |

---

## 📋 P1 Tasks — Important

| # | Task | Action | Status |
|---|------|--------|--------|
| 5 | Deploy Infisical to INT-OG1 | Helm chart + SecretSync CRD (shares INT-P01 cluster operator) | ⬜ TODO |
| 6 | Deploy Infisical to INT-OG8 | Helm chart + SecretSync CRD (shares INT-P01 cluster operator) | ⬜ TODO |
| 7 | Deploy Infisical to INT-P02 | Docker init container + SDK (after @SHD PR merged) | ⬜ TODO |
| 8 | Deploy Infisical to all new Docker Droplets | Docker init container + SDK (templated from @SHD PR) | ⬜ TODO |
| 9 | Build n8n rotation workflow | Infisical API + Provider API (n8n recommended) | ⬜ TODO |
| 10 | Test rotation end-to-end | Verify 7D rotation works for OpenRouter | ⬜ TODO |
| 11 | Document Infisical integration | Runbook for future instance setup | ⬜ TODO |

---

## 📋 P2 Tasks — Nice to Have

| # | Task | Action | Status |
|---|------|--------|--------|
| 12 | Set up monitoring/alerting | Uptime Kuma + Infisical webhook | ⬜ TODO |
| 13 | Audit log review | Monthly access log review | ⬜ TODO |
| 14 | Self-host Infisical (optional) | Evaluate self-hosting vs cloud | ⬜ TBD |
| 15 | AnythingLLM agent skill (optional) | Custom rotation skill | ⬜ TBD |

---

## 📋 Learnings Locked (PRJ-024)

| ID | Learning | Detail | Source |
|----|----------|--------|--------|
| **L-126** | API Key Rotation = Intentional Security | 7D/30D rotation cycles are intentional security, not bugs | PRJ-024 |
| **BP-064** | API Key Rotation Best Practice | 7D/30D rotation cycles, Infisical storage, automated rotation | GUIDE-011 |
| **New** | Infisical Operator = Partial Automation | Enables secret SYNC but NOT full ROTATION — requires n8n/cronjob/agent for rotation | PRJ-024 |
| **New** | K8s Operator Debugging | Check logs, verify RBAC, test SecretSync CRD, force-sync annotation before assuming broken | INT-P01 incident |
| **New** | Instance Architecture Split | DOKS clusters (INT-P01, INT-OG1, INT-OG8, jAIMSnet) = Helm; Docker Droplets (INT-P02 + others) = SDK/init container | PRJ-024 |

---

## 📋 Related PRJs

| PRJ | Title | Relationship |
|-----|-------|--------------|
| **PRJ-016** | LiteLLM AI Gateway | Secrets stored in Infisical (API keys, virtual keys) |
| **PRJ-017** | Observability (Langfuse) | Secrets stored in Infisical (secret/public keys, DB creds) |
| **PRJ-021** | PostgreSQL Operations | PostgreSQL credentials stored in Infisical |
| **PRJ-025** | jAIMSnet Platform Engineering | Infisical Operator deployed to jAIMSnet DOKS cluster |
| **PRJ-026** | Cybersecurity Frameworks + ISMS | Infisical meets SOC 2, ISO 27001 secrets management requirements |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| **3.2.3.1** | **2026-W12** | **GTM_2026-W10_026** | **GTM_2026-W11_328** | **Initial document creation — Infisical architecture (vault, operator, SDK, CLI, API). Instance architecture split: DOKS clusters (INT-P01, INT-OG1, INT-OG8, jAIMSnet) = Helm; Docker Droplets (INT-P02 + others) = SDK/init container. Deployment methods (Helm for DOKS, Docker for Droplets). API key rotation options (n8n workflow recommended, agent skill, K8s CronJob, Docker Cronjob — comparison table). Instance integration status (INT-P01 50% broken, ALL other instances 0% not started). @SHD Docker PR (reviewed by @RMN W12, awaiting @SHD revised push). Secrets inventory (15 total: 6 P0, 9 P1/P2). P0/P1/P2 task registry (4+7+4 tasks). Learnings locked (L-126, BP-064, Operator = partial automation, K8s debugging, instance architecture split). Related PRJs (PRJ-016/017/021/025/026)** |

---

## 📋 Related Documents

| Document | Version | #masterCCC | Approval | Location |
|----------|---------|------------|----------|----------|
| PRJ-016_AIGateway-LiteLLM.md | 3.2.3.1 | GTM_2026-W10_122 | GTM_2026-W10_026 | _PROJECTS_/ (GH LIVE) |
| PRJ-017_Observability-Langfuse.md | 3.2.3.1 | GTM_2026-W09_121 | GTM_2026-W09_108 | _PROJECTS_/ (GH LIVE) |
| PRJ-021_PostgreSQL-Operations.md | 3.2.3.1 | GTM_2026-W10_026 | GTM_2026-W10_026 | _PROJECTS_/ |
| PRJ-025_jAIMSnet-Platform-Engineering.md | 3.2.3.1 | GTM_2026-W10_026 | ⬜ AWAITING | _PROJECTS_/ |
| PRJ-026_Cybersecurity-Frameworks.md | 3.2.3.1 | GTM_2026-W10_026 | ⬜ AWAITING | _PROJECTS_/ |
| GUIDE-011_Governance-Oversight-VSA-Process.md | 3.2.1.1 | GTM_2026-W10_066 | GTM_2026-W10_073 | _GUIDES_/ |

---

## 📋 Discovered By (BP-047)

| CCC | Contributor | Role | Context |
|-----|-------------|------|---------|
| RMN | Roman Di Domizio | AI Platform Engineer | Conceived + implemented PRJ-024 (W09-W10), Infisical account created, K8s operator deployed (INT-P01), INT-P01 incident response + debugging, @SHD PR review + feedback (W12) |
| SHD | Shahid | Sr. Full-Stack DevOps Engineer | Docker Infisical integration PR (delivered Feb 23, reviewed by @RMN W12, revising per @RMN feedback) |
| GTM | Jason Younker | Co-Founder | Approved PRJ assignment (GTM_2026-W10_026), approved document (GTM_2026-W11_328) |

---

## 📋 Governance Compliance

| Requirement | Status |
|-------------|--------|
| #masterCCC | ✅ GTM_2026-W10_026 |
| Approval CCC-ID | ✅ GTM_2026-W11_328 |
| Version History | ✅ Included |
| Related Documents | ✅ Included |
| Discovered By (BP-047) | ✅ Included |
| Lifecycle Stage | 🔄 IN PROGRESS |
| VSA Eligibility | ✅ FULL or DEEP FULL (at APPROVED+ stage) |
| GUIDE-011 | ✅ APPROVED — compensation eligible |
| R-199 (Credential Protection) | ✅ Credentials = RAG ONLY, NEVER GitHub |

---

#FlowsBros #FedArch #PRJ-024 #Infisical #Secrets #jAIMSnet #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
