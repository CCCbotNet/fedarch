# PRJ-032: OpenTofu — Infrastructure as Code for #FedArch

## 📋 PRJ-032_OpenTofu-IaC_v3.2.1.1.md
## ♾️ WeOwnNet 🌐

| Field | Value |
|-------|-------|
| Document | PRJ-032_OpenTofu-IaC.md |
| Version | 3.2.1.1 |
| CCC-ID | GTM_2026-W10_265 |
| Created | 2026-03-06 (W10) |
| Season | #WeOwnSeason003 🚀 |
| Status | ✅ 🔒 APPROVED |
| Lifecycle Stage | ✅ 🔒 APPROVED (#DocLifecycle) |
| Source of Truth | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-032_OpenTofu-IaC.md) |
| Tags | #OpenTofu #IaC #FOSS #Infrastructure #FedArch #FlowsBros |

---

## 📖 Table of Contents

1. [Project Identity](#-project-identity)
2. [Why OpenTofu](#-why-opentofu)
3. [FOSS Alignment](#-foss-alignment)
4. [Phase Plan](#-phase-plan)
5. [Infrastructure Matrix — OpenTofu vs Ansible](#-infrastructure-matrix--opentofu-vs-ansible)
6. [HCL Examples](#-hcl-examples)
7. [State Management — DO Spaces](#-state-management--do-spaces)
8. [Infisical Integration](#-infisical-integration)
9. [GitHub Actions CI/CD](#-github-actions-cicd)
10. [Project Team](#-project-team)
11. [Dependencies](#-dependencies)
12. [Deployment Checklist](#-deployment-checklist)
13. [#SmokeTest](#-smoketest)
14. [Budget](#-budget)
15. [Risk Matrix](#-risk-matrix)
16. [Relationship to Other Projects](#-relationship-to-other-projects)
17. [Discovered By](#-discovered-by)
18. [Related Documents](#-related-documents)
19. [Version History](#-version-history)

---

## 📋 Project Identity

| Field | Value |
|-------|-------|
| Project ID | **PRJ-032** |
| Title | **OpenTofu — Infrastructure as Code for #FedArch** |
| Type | Infrastructure — IaC Adoption |
| Priority | 🟡 **P2** — after LiteLLM (PRJ-016) + Langfuse (PRJ-017) |
| Tool | [OpenTofu](https://opentofu.org/) |
| License | **MPL-2.0** ✅ (FOSS — OSI-approved) |
| Foundation | **Linux Foundation** |
| GitHub | [github.com/opentofu/opentofu](https://github.com/opentofu/opentofu) — 24K+ stars |
| Owner | **@LDC** (Agentic AI Engineer) |
| Oversight | **@RMN** (Platform) + **@GTM** (Governance) |
| Start | **W12-W13** |
| State Backend | DO Spaces ($5/mo) |
| CI/CD | GitHub Actions |
| Secrets | Infisical provider |
| Complementary | Ansible (application deployment) |
| #masterCCC | GTM_2026-W10_265 |

---

## 📋 Why OpenTofu

### The Problem

| Current State | Issue |
|--------------|-------|
| Infrastructure created manually | ❌ No reproducibility |
| @SHD creates Droplets via DO dashboard | ❌ No version control |
| DNS configured manually | ❌ Drift from intended state |
| No infrastructure documentation-as-code | ❌ Tribal knowledge |
| 10+ Droplets + DOKS + Managed DB + DNS | ❌ Growing complexity |

### The Solution

| OpenTofu Provides | Benefit |
|------------------|---------|
| Declarative infrastructure | ✅ "What" not "how" |
| Version-controlled HCL files | ✅ Git history = infrastructure history |
| State tracking | ✅ Know what exists vs what should exist |
| Reproducibility | ✅ Spin up identical environments |
| Plan before apply | ✅ Preview changes before executing |
| State encryption | ✅ Sensitive data protected at rest |

### Ecosystem Pattern

| Decision | Corporate (Rejected) | FOSS (Adopted) | Rule |
|----------|---------------------|----------------|------|
| Observability | Phoenix (ELv2) | **Langfuse (MIT)** | L-129 |
| **IaC** | **Terraform (BSL)** | **OpenTofu (MPL-2.0)** | **L-129 pattern** |
| Pattern | Source-available | **Community-owned** | Priority #2 |

---

## 📋 FOSS Alignment

| Priority | Score | Detail |
|----------|-------|--------|
| **#2 FOSS** | **10/10** | MPL-2.0 — OSI-approved, no commercial restrictions |
| **#3 Data Sovereignty** | **9/10** | State encryption at rest (OpenTofu-exclusive) |
| **#4 Cooperative** | **10/10** | Linux Foundation governance — no single vendor |
| **Overall** | **9.75/10** | |

### License Comparison

| Tool | License | OSI | FOSS | Verdict |
|------|---------|-----|------|---------|
| **OpenTofu** | **MPL-2.0** | ✅ | ✅ | ✅ **ADOPT** |
| Terraform | BSL 1.1 | ❌ | ❌ | ❌ Priority #2 violation |
| Pulumi | Apache 2.0 | ✅ | ✅ | 🟡 Alternative (different paradigm) |
| Ansible | GPL-3.0 | ✅ | ✅ | ✅ Complementary (not competing) |

---

## 📋 Phase Plan

| Phase | When | What | Owner | Deliverable |
|-------|------|------|-------|-------------|
| **1** | **W12-W13** | Create `infrastructure/` repo + DO Spaces state backend | @LDC | Repo + backend configured |
| **2** | **W13-W14** | Define existing infrastructure in HCL (Droplets, DOKS, DB, DNS) | @LDC + @RMN | `.tf` files for all resources |
| **3** | **W14-W15** | Import existing state (`tofu import`) | @LDC | State file reflects reality |
| **4** | **W15+** | All new infrastructure via OpenTofu (no more manual) | @LDC | PR → plan → apply workflow |

### Phase 1 Detail — Foundation

| # | Step | Owner |
|---|------|-------|
| 1 | Create `CCCbotNet/infrastructure` repo | @LDC |
| 2 | Create DO Spaces bucket (`fedarch-tofu-state`) | @LDC |
| 3 | Configure OpenTofu backend (DO Spaces) | @LDC |
| 4 | Configure Infisical provider | @LDC |
| 5 | Create GitHub Actions workflow | @LDC |
| 6 | Test: create + destroy test Droplet | @LDC |

### Phase 2 Detail — Define Existing

| # | Resource | HCL File |
|---|----------|----------|
| 1 | VPC (ATL1) | `vpc.tf` |
| 2 | Droplets (INT-P01, INT-P05, INT-S003, jAIMSnet) | `droplets.tf` |
| 3 | DOKS cluster | `kubernetes.tf` |
| 4 | Managed PostgreSQL | `database.tf` |
| 5 | DNS records (WeOwn.Agency, WeOwn.tools, jAIMS.app, ccc.bot) | `dns.tf` |
| 6 | Firewalls | `firewall.tf` |
| 7 | DO Spaces | `spaces.tf` |
| 8 | Variables + outputs | `variables.tf` + `outputs.tf` |

### Phase 3 Detail — Import

```bash
# Import existing Droplet
tofu import digitalocean_droplet.int_p01 <droplet-id>

# Import existing DOKS
tofu import digitalocean_kubernetes_cluster.fedarch <cluster-id>

# Import existing PostgreSQL
tofu import digitalocean_database_cluster.pop_db <db-id>

# Verify: plan should show no changes
tofu plan
# Expected: "No changes. Your infrastructure matches the configuration."
```

### Phase 4 Detail — New Infrastructure via PR

```
1. Developer creates branch: feature/add-int-p06
2. Writes HCL: new Droplet definition
3. Opens PR → GitHub Actions runs `tofu plan`
4. Team reviews plan output
5. Merge → GitHub Actions runs `tofu apply`
6. Infrastructure created automatically
```

---

## 📋 Infrastructure Matrix — OpenTofu vs Ansible

| Component | OpenTofu (Provisioning) | Ansible (Configuration) |
|-----------|----------------------|----------------------|
| **DO Droplets** | ✅ Create/destroy | Configure OS, users |
| **DOKS** | ✅ Create/scale | Deploy Helm charts |
| **Managed PostgreSQL** | ✅ Create/configure | Create databases/users |
| **DNS Records** | ✅ Create/update | — |
| **VPC + Firewall** | ✅ Define rules | — |
| **DO Spaces** | ✅ Create buckets | — |
| **AnythingLLM** | ✅ Helm release | Configure prompts, RAG |
| **LiteLLM** | — | ✅ Docker deploy + config |
| **Langfuse** | — | ✅ Docker deploy + config |
| **Uptime Kuma** | — | ✅ Docker deploy + config |
| **Infisical** | — | ✅ Self-hosted deploy |
| **Paperless-ngx** | — | ✅ Docker deploy + config |
| **Caddy** | — | ✅ Caddyfile config |

> **OpenTofu = cloud infrastructure. Ansible = application deployment.** Clear separation. No overlap.

---

## 📋 HCL Examples

### DO Droplet (INT-P05)

```hcl
resource "digitalocean_droplet" "int_p05" {
  name     = "int-p05-pro-weown-agency"
  region   = "atl1"
  size     = "s-2vcpu-4gb"
  image    = "ubuntu-24-04-x64"
  vpc_uuid = digitalocean_vpc.fedarch.id

  tags = ["fedarch", "production", "anythingllm"]
}

resource "digitalocean_record" "pro_weown_agency" {
  domain = "weown.agency"
  type   = "A"
  name   = "pro"
  value  = digitalocean_droplet.int_p05.ipv4_address
}
```

### DOKS Cluster

```hcl
resource "digitalocean_kubernetes_cluster" "fedarch" {
  name    = "fedarch-doks"
  region  = "atl1"
  version = "1.31.1-do.0"

  node_pool {
    name       = "default"
    size       = "s-2vcpu-4gb"
    node_count = 3
    auto_scale = true
    min_nodes  = 2
    max_nodes  = 5
  }
}
```

### Managed PostgreSQL

```hcl
resource "digitalocean_database_cluster" "fedarch_db" {
  name       = "fedarch-postgresql"
  engine     = "pg"
  version    = "17"
  size       = "db-s-1vcpu-1gb"
  region     = "atl1"
  node_count = 1

  maintenance_window {
    day  = "sunday"
    hour = "04:00:00"
  }
}

resource "digitalocean_database_db" "pop_db" {
  cluster_id = digitalocean_database_cluster.fedarch_db.id
  name       = "pop_db"
}

resource "digitalocean_database_db" "langfuse_db" {
  cluster_id = digitalocean_database_cluster.fedarch_db.id
  name       = "langfuse_db"
}
```

### DNS Records

```hcl
# WeOwn.Agency subdomains
resource "digitalocean_record" "ai_weown_agency" {
  domain = "weown.agency"
  type   = "A"
  name   = "ai"
  value  = digitalocean_droplet.int_p01.ipv4_address
}

# jAIMS.app subdomains
resource "digitalocean_record" "langfuse_jaims" {
  domain = "jaims.app"
  type   = "A"
  name   = "langfuse"
  value  = digitalocean_droplet.jaimsnet.ipv4_address
}

resource "digitalocean_record" "litellm_jaims" {
  domain = "jaims.app"
  type   = "A"
  name   = "litellm"
  value  = digitalocean_droplet.jaimsnet.ipv4_address
}
```

---

## 📋 State Management — DO Spaces

### Backend Configuration

```hcl
# backend.tf
terraform {
  backend "s3" {
    endpoints = {
      s3 = "https://atl1.digitaloceanspaces.com"
    }
    bucket                      = "fedarch-tofu-state"
    key                         = "infrastructure/terraform.tfstate"
    region                      = "us-east-1"  # Required but ignored by DO
    skip_credentials_validation = true
    skip_metadata_api_check     = true
    skip_requesting_account_id  = true
    skip_s3_checksum            = true
  }
}
```

### State Encryption (OpenTofu-Exclusive)

```hcl
# State encryption — not available in Terraform
terraform {
  encryption {
    key_provider "pbkdf2" "state_key" {
      passphrase = var.state_encryption_passphrase
    }

    method "aes_gcm" "encrypt" {
      keys = key_provider.pbkdf2.state_key
    }

    state {
      method   = method.aes_gcm.encrypt
      enforced = true
    }
  }
}
```

### State Management Rules

| Rule | Description |
|------|-------------|
| Remote state ONLY | No local state files in production |
| Encryption enforced | State encrypted at rest (OpenTofu-exclusive) |
| Locking enabled | Prevent concurrent modifications |
| Backup | DO Spaces versioning enabled |
| Access | Infisical manages Spaces credentials |

---

## 📋 Infisical Integration

```hcl
# providers.tf
terraform {
  required_providers {
    digitalocean = {
      source  = "digitalocean/digitalocean"
      version = "~> 2.0"
    }
    infisical = {
      source  = "infisical/infisical"
      version = "~> 0.1"
    }
  }
}

provider "infisical" {
  host          = "https://infisical.weown.tools"
  client_id     = var.infisical_client_id
  client_secret = var.infisical_client_secret
}

# Pull DO API token from Infisical
data "infisical_secrets" "digitalocean" {
  env_slug    = "prod"
  folder_path = "/digitalocean"
}

provider "digitalocean" {
  token = data.infisical_secrets.digitalocean.secrets["DO_API_TOKEN"]
}
```

---

## 📋 GitHub Actions CI/CD

```yaml
# .github/workflows/infrastructure.yml
name: Infrastructure — OpenTofu
on:
  pull_request:
    paths: ['infrastructure/**']
  push:
    branches: [main]
    paths: ['infrastructure/**']

env:
  TOFU_VERSION: "1.9.0"

jobs:
  plan:
    if: github.event_name == 'pull_request'
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: infrastructure
    steps:
      - uses: actions/checkout@v4
      - uses: opentofu/setup-opentofu@v1
        with:
          tofu_version: ${{ env.TOFU_VERSION }}
      - name: Init
        run: tofu init
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.DO_SPACES_KEY }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.DO_SPACES_SECRET }}
      - name: Plan
        run: tofu plan -no-color
        env:
          TF_VAR_infisical_client_id: ${{ secrets.INFISICAL_CLIENT_ID }}
          TF_VAR_infisical_client_secret: ${{ secrets.INFISICAL_CLIENT_SECRET }}

  apply:
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: infrastructure
    steps:
      - uses: actions/checkout@v4
      - uses: opentofu/setup-opentofu@v1
        with:
          tofu_version: ${{ env.TOFU_VERSION }}
      - name: Init
        run: tofu init
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.DO_SPACES_KEY }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.DO_SPACES_SECRET }}
      - name: Apply
        run: tofu apply -auto-approve -no-color
        env:
          TF_VAR_infisical_client_id: ${{ secrets.INFISICAL_CLIENT_ID }}
          TF_VAR_infisical_client_secret: ${{ secrets.INFISICAL_CLIENT_SECRET }}
```

### CI/CD Workflow

```
Developer → Branch → Write HCL → PR
                                  │
                                  ↓
                    GitHub Actions: `tofu plan`
                    (shows what WILL change)
                                  │
                                  ↓
                    Team reviews plan in PR
                                  │
                                  ↓
                    Merge to main
                                  │
                                  ↓
                    GitHub Actions: `tofu apply`
                    (infrastructure changes applied)
```

---

## 📋 Project Team

| CCC | Role | Focus |
|-----|------|-------|
| **LDC** | **Owner** | HCL authoring, state management, CI/CD, imports |
| **RMN** | **Oversight** | Architecture review, DOKS guidance, Helm integration |
| **GTM** | **Governance** | PRJ oversight, FOSS alignment, documentation |

---

## 📋 Dependencies

| # | Dependency | Status | Blocks |
|---|-----------|--------|--------|
| 1 | PRJ-016 (LiteLLM) deployed | 🔄 @RMN deploying | Phase 1 (not blocking — can start repo) |
| 2 | PRJ-017 (Langfuse) deployed | 🔄 @RMN deploying | Phase 1 (not blocking) |
| 3 | @LDC availability | ✅ After PRJ-016/017 | Phase 1 |
| 4 | DO Spaces bucket | ⬜ Phase 1 | Phase 2 |
| 5 | Infisical provider config | ⬜ Phase 2 | Phase 2 |
| 6 | GitHub Actions secrets | ⬜ Phase 2 | Phase 2 |
| 7 | Existing resource IDs (for import) | ⬜ Phase 3 | Phase 3 |

---

## 📋 Deployment Checklist

| # | Step | Owner | Phase | Status |
|---|------|-------|-------|--------|
| 1 | Create `CCCbotNet/infrastructure` repo | @LDC | 1 | ⬜ |
| 2 | Create DO Spaces bucket (`fedarch-tofu-state`) | @LDC | 1 | ⬜ |
| 3 | Enable Spaces versioning | @LDC | 1 | ⬜ |
| 4 | Configure OpenTofu backend (DO Spaces) | @LDC | 1 | ⬜ |
| 5 | Configure state encryption | @LDC | 1 | ⬜ |
| 6 | Configure Infisical provider | @LDC | 1 | ⬜ |
| 7 | Create GitHub Actions workflow | @LDC | 1 | ⬜ |
| 8 | Add GH secrets (DO Spaces + Infisical) | @LDC | 1 | ⬜ |
| 9 | Test: create + destroy test Droplet | @LDC | 1 | ⬜ |
| 10 | Write `vpc.tf` | @LDC | 2 | ⬜ |
| 11 | Write `droplets.tf` (all INT-xxx) | @LDC | 2 | ⬜ |
| 12 | Write `kubernetes.tf` (DOKS) | @LDC + @RMN | 2 | ⬜ |
| 13 | Write `database.tf` (PostgreSQL) | @LDC | 2 | ⬜ |
| 14 | Write `dns.tf` (all domains) | @LDC | 2 | ⬜ |
| 15 | Write `firewall.tf` | @LDC | 2 | ⬜ |
| 16 | Write `variables.tf` + `outputs.tf` | @LDC | 2 | ⬜ |
| 17 | `tofu import` all existing resources | @LDC | 3 | ⬜ |
| 18 | `tofu plan` — verify "No changes" | @LDC | 3 | ⬜ |
| 19 | #SmokeTest (10-point) | @GTM | 3 | ⬜ |
| 20 | FULL:SYNC:META | @GTM | 3 | ⬜ |

---

## 📋 #SmokeTest (10-Point)

| # | Test | Expected | Status |
|---|------|----------|--------|
| 1 | `tofu init` succeeds | Backend connected to DO Spaces | ⬜ |
| 2 | `tofu plan` — no errors | Valid HCL, providers resolved | ⬜ |
| 3 | `tofu plan` — "No changes" (after import) | State matches reality | ⬜ |
| 4 | State encrypted at rest | Encrypted state in DO Spaces | ⬜ |
| 5 | Infisical secrets resolve | DO API token pulled from Infisical | ⬜ |
| 6 | GH Actions plan runs on PR | Plan output visible in PR | ⬜ |
| 7 | GH Actions apply runs on merge | Infrastructure changes applied | ⬜ |
| 8 | Create test Droplet via PR | Droplet appears in DO | ⬜ |
| 9 | Destroy test Droplet via PR | Droplet removed from DO | ⬜ |
| 10 | State locking works | Concurrent apply blocked | ⬜ |

---

## 📋 Budget

| Component | Monthly |
|-----------|---------|
| OpenTofu | **$0** (FOSS) |
| DO Spaces (state backend) | **$5/mo** |
| GitHub Actions | **$0** (included in GH plan) |
| Infisical | **$0** (self-hosted) |
| **TOTAL** | **$5/mo** |

---

## 📋 Risk Matrix

| # | Risk | Prob | Impact | Mitigation |
|---|------|------|--------|------------|
| 1 | Import fails (state mismatch) | Medium | Medium | `tofu import` one resource at a time; verify with plan |
| 2 | State corruption | Low | High | DO Spaces versioning + encryption + backups |
| 3 | @LDC learning curve | Low | Low | HCL is simple; @RMN provides guidance |
| 4 | Provider breaking changes | Low | Medium | Pin provider versions in `required_providers` |
| 5 | Concurrent state modifications | Low | Medium | State locking via DO Spaces |
| 6 | OpenTofu project abandoned | Very Low | Medium | Linux Foundation backed; 24K stars; MPL-2.0 = forkable |

---

## 📋 Relationship to Other Projects

| PRJ | Connection | URL |
|-----|-----------|-----|
| **PRJ-014** | #FedArchExpansion — OpenTofu manages expanded infrastructure | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-014_FedArchExpansion.md) |
| **PRJ-015** | #HybridArchitecture — GPU instances via OpenTofu | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-015_HybridArchitecture.md) |
| **PRJ-016** | LiteLLM — Ansible deploys, OpenTofu provisions Droplet | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-016_AIGateway-LiteLLM.md) |
| **PRJ-017** | Langfuse — Ansible deploys, OpenTofu provisions Droplet | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-017_Observability.md) |
| **PRJ-013** | Paperless-ngx — OpenTofu provisions GB10-1 infrastructure | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-013_Paperless-ngx.md) |
| **PRJ-024** | Infisical — secrets provider for OpenTofu | — |

---

## 📋 Discovered By (BP-047)

| CCC | Contributor | Role | Context |
|-----|-------------|------|---------|
| GTM | [yonks](https://GitHub.com/YonksTEAM) | Co-Founder / Chief Digital Alchemist | Identified OpenTofu as FOSS IaC standard; SEEK:META #DeepDive (GTM_2026-W10_265); same FOSS-over-corporate pattern as Langfuse (L-129) |
| LDC | Dhruv | Agentic AI Engineer / Project Lead | Assigned as Project Owner — HCL authoring + state management |
| RMN | Roman Di Domizio | AI Platform Engineer | Project Oversight — DOKS + Helm architectural guidance |

---

## 📋 Related Documents

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| SharedKernel | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/SharedKernel.md) |
| OpenTofu Docs | — | — | — | [opentofu.org/docs](https://opentofu.org/docs/) |
| OpenTofu GitHub | — | — | — | [github.com/opentofu/opentofu](https://github.com/opentofu/opentofu) |
| DO Provider | — | — | — | [registry.opentofu.org/providers/digitalocean](https://search.opentofu.org/provider/digitalocean/digitalocean) |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| 3.2.1.1 | 2026-W10 | GTM_2026-W10_265 | GTM_2026-W10_268 | Initial project; OpenTofu IaC for #FedArch; MPL-2.0 (FOSS 10/10); Linux Foundation governance; 4-phase plan (W12-W15+); @LDC owner + @RMN oversight; DO provider (Droplets, DOKS, PostgreSQL, DNS, VPC, Firewall, Spaces); state backend on DO Spaces ($5/mo) with encryption; Infisical secrets integration; GitHub Actions CI/CD (plan on PR, apply on merge); OpenTofu vs Ansible matrix; HCL examples (4); 20-step deployment checklist; 10-point #SmokeTest; $5/mo budget; 6-risk matrix; same FOSS pattern as Langfuse (L-129) |

---

#FlowsBros #FedArch #OpenTofu #IaC #FOSS #Infrastructure #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
