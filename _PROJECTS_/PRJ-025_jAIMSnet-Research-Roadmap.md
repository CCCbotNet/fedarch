# PRJ-025_jAIMSnet-Research-Roadmap.md

## 📋 Document Metadata

| Field | Value |
|-------|-------|
| **Document** | PRJ-025_jAIMSnet-Research-Roadmap.md |
| **Version** | **v3.2.3.2** |
| **CCC-ID** | RMN_2026-W12_077 |
| **Approval CCC-ID** | GTM_2026-W11_330 |
| **Created** | 2026-W12 |
| **Updated** | **2026-03-19 (W12)** |
| **Season** | #WeOwnSeason003 🚀 |
| **Status** | 🔄 IN PROGRESS — Roadmap ~50% Complete (SDLC: Research + Design Required) |
| **#LLMmodel** | Claude Sonnet 4.6 |
| **Source of Truth** | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-025_jAIMSnet-Research-Roadmap.md) |

> **⚠️ SCOPE CLARIFICATION:** This document covers the foundational **research and roadmap** for jAIMSnet. It is NOT the implementation guide — full implementation details, deployment instructions, and technical specifications for each track will live in dedicated downstream PRJ documents that stem from this research. This research must be completed before implementation of any dependent PRJs can begin.

---

## 📖 Table of Contents

1. [Project Identity](#-project-identity)
2. [Executive Summary](#-executive-summary)
3. [Why This Research is Critical — Ecosystem Priority](#-why-this-research-is-critical--ecosystem-priority)
4. [Dependent PRJs — What This Unlocks](#-dependent-prjs--what-this-unlocks)
5. [SDLC Status — Research + Design Required](#-sdlc-status--research--design-required)
6. [jAIMSnet Architecture — Current State](#-jaimsnet-architecture--current-state)
7. [Repository Structure (Monorepo)](#-repository-structure-monorepo)
8. [Namespace Architecture](#-namespace-architecture)
9. [Platform Status — All Tools by Phase](#-platform-status--all-tools-by-phase)
10. [Tool Evaluation — Locked vs Under Evaluation](#-tool-evaluation--locked-vs-under-evaluation)
11. [Architecture Decisions — Hub vs Tenant](#-architecture-decisions--hub-vs-tenant)
12. [8 Research Tracks — Full Research Plan](#-8-research-tracks--full-research-plan)
13. [ISO/IEC 42001 Alignment](#-isoiec-42001-alignment)
14. [Domains — Current + Planned](#-domains--current--planned)
15. [Integration with Other PRJs](#-integration-with-other-prjs)
16. [Roadmap Completion Status](#-roadmap-completion-status)
17. [Version History](#-version-history)
18. [Related Documents](#-related-documents)
19. [Discovered By (BP-047)](#-discovered-by-bp-047)
20. [Governance Compliance](#-governance-compliance)

---

## 📋 Project Identity

| Field | Value |
|-------|-------|
| Project ID | **PRJ-025** |
| Title | **jAIMSnet — Research + Roadmap** |
| Type | Infrastructure + Governance — Foundational Research + Platform Roadmap |
| Priority | 🔴 **P0 — HIGHEST PRIORITY IN ECOSYSTEM** |
| Owner | @RMN (Roman Di Domizio) |
| Status | 🔄 IN PROGRESS — Roadmap ~50% Complete (SDLC: Research + Design Required) |
| #masterCCC | GTM_2026-W10_026 |
| Approval CCC-ID | GTM_2026-W11_330 |

---

## 📋 Executive Summary

### What Is This Document?

This document captures the **foundational research and roadmap** for jAIMSnet — the AI Management Systems platform for the ♾️ WeOwnNet 🌐 ecosystem. It is the **prerequisite** to all downstream jAIMSnet implementation projects and many other ecosystem PRJs.

> **⚠️ IMPORTANT — Scope of This Document:**
> - ✅ This document = **Research plan, tool evaluation, architecture decisions, and roadmap**
> - ❌ This document ≠ Implementation guide, deployment instructions, or technical specs
> - 📋 Implementation details for each area will live in **dedicated downstream PRJs** that stem from each research track's findings
> - 🔒 No further implementation should happen until this research is substantially complete

### What Is jAIMSnet?

| Field | Value |
|-------|-------|
| **Brand** | **jAIMSnet** |
| **Meaning** | j + **AIMS** (AI Management Systems) + net (network) |
| **ISO Reference** | **ISO/IEC 42001:2023** — AI Management Systems |
| **ISO URL** | [iso.org/standard/81230.html](https://www.iso.org/standard/81230.html) |
| **Positioning** | Full-stack platform engineering, including fully open-source AI observability & management infrastructure |
| **Relationship** | Ecosystem brand under ♾️ WeOwnNet 🌐 |
| **Primary Domain** | jAIMS.network |
| **GitHub Org** | [github.com/jAIMSnet](https://github.com/jAIMSnet) |
| **X (Twitter)** | [x.com/jAIMSnet](https://x.com/jAIMSnet) |

### Why jAIMSnet?

| Problem | jAIMSnet Solution |
|---------|------------------|
| Fragmented AI tooling | ✅ Unified platform (gateway + observability + inference) |
| No ISO 42001 alignment | ✅ Built-in compliance framework |
| Manual infrastructure | ✅ GitOps + IaC automation |
| Security gaps | ✅ Integrated security stack (Trivy, Falco, CrowdSec) |
| No cost visibility | ✅ Langfuse + LiteLLM = per-request cost tracking |
| Vendor lock-in | ✅ FOSS-first, multi-provider routing |

### Current Status (W12)

| Metric | Value |
|--------|-------|
| **Roadmap Completion** | ~50% (research track 1 complete, tracks 2-8 planned) |
| **Infrastructure** | ✅ DOKS Cluster LIVE, Load Balancer LIVE, Uptime Kuma (NYC1) LIVE |
| **Phase 1** | 🔄 ~90% complete (implementation paused — SDLC compliance required) |
| **Phase 2** | 📋 ~50% planned (pending research tracks 4-5) |
| **Phase 3** | 📋 ~25% planned (pending research tracks 6-7) |
| **Phase 4** | 📋 ~0% planned (pending research tracks 7-8) |
| **Priority** | 🔴 **HIGHEST PRIORITY** — self-hosted AnythingLLM in production + most downstream PRJs blocked |

### ⚠️ SDLC Alert — Implementation Paused

> **Issues occurred during initial implementation (LiteLLM/Redis, Langfuse, Infisical by @RMN; OpenTofu by @LDC) because there was no finished roadmap, design, or plan to follow.** jAIMSnet is the most complex platform engineering project in the ecosystem with many tools and a hub + tenant architecture. Per SDLC best practices, proper research, analysis, design, and planning MUST be completed before any further implementation, or there will be many issues, wasted dev time, and things needing to be fixed. This is very high priority given self-hosted AnythingLLM instances in production.

### Deployed Infrastructure (W10 — Live)

| Component | Spec | Status |
|-----------|------|--------|
| **DOKS Cluster** | jaimsnet-cluster · ATL1 · K8s 1.34.1 · Premium AMD 2vCPU/8GiB | ✅ LIVE |
| **Load Balancer** | 129.212.240.75 · ATL1 | ✅ LIVE |
| **Uptime Kuma** | Basic Droplet · NYC1 · ~$6/mo (standalone, separate from ATL1 cluster) | ✅ LIVE |
| **Managed PostgreSQL** | ATL1 · port 25060 · sslmode=require | ✅ LIVE (PRJ-021) |
| **Ingress Controller** | ingress-nginx + cert-manager (auto-TLS) | 🔄 In Progress (implementation paused) |
| **LiteLLM** | AI Gateway (gateway namespace) | 🔄 In Progress (implementation paused) |
| **Langfuse** | LLM Observability (observability namespace) | 🔄 In Progress (implementation paused) |
| **Redis** | Semantic cache for LiteLLM | 🔄 In Progress (implementation paused) |
| **Infisical Operator** | Secret sync (secrets namespace) | 🔄 In Progress (implementation paused) |

### Cost Breakdown

| Phase | Monthly Cost (est.) | Components |
|-------|:-------------------:|------------|
| **Phase 1 🔴** | **~$57/mo** | DOKS (1 node) + LB + Managed PG + Kuma Droplet (NYC1) |
| **Phase 2 🟠** | **~$112+/mo** | Phase 1 + autoscale node + GPU Droplet (MI300X/MI325X) |
| **Phase 3 🟡** | **~$120+/mo** | Phase 2 + additional tooling overhead |
| **Phase 4 🟢** | **TBD** | Phase 3 + customer platform infrastructure |

---

## 📋 Why This Research is Critical — Ecosystem Priority

### PRJ-025 = Foundational to the Entire Platform

> **This is the most complex and most important research + design project in the ♾️ WeOwnNet 🌐 ecosystem.** The jAIMSnet platform is the backbone for all AI infrastructure, tooling, security, observability, and automation that every other PRJ relies on.

### Complexity Factors

| Factor | Detail |
|--------|--------|
| **Multi-tool stack** | 40+ tools being evaluated across 8 research tracks |
| **Hub + Tenant architecture** | Two deployment paradigms (DOKS clusters + Docker Droplets) |
| **Multi-tenancy** | Internal + SMB + Enterprise + Trial/Demo tenant types |
| **Cross-PRJ dependencies** | 8+ existing PRJs + multiple new PRJs blocked on this research |
| **SDLC violation risk** | Implementation without research = wasted effort + rework (already proven W10) |
| **Production impact** | Self-hosted AnythingLLM instances in production RIGHT NOW |
| **Compliance requirements** | ISO 42001, ISO 27001, SOC 2 all dependent on architecture decisions |

### Why It Must Be Done First

| Without PRJ-025 Research | With PRJ-025 Research Complete |
|--------------------------|-------------------------------|
| ❌ Wasted implementation effort (proven W10) | ✅ Confident, correct implementation |
| ❌ Rework and technical debt | ✅ Clean, tested, production-ready |
| ❌ Security gaps from ad-hoc decisions | ✅ Security-by-design from the start |
| ❌ Blocked downstream PRJs | ✅ Downstream PRJs can proceed in sequence |
| ❌ Multiple tools deployed that may not fit | ✅ Right tools chosen for right use cases |
| ❌ Compliance gaps | ✅ Compliance-ready architecture from day 1 |

---

## 📋 Dependent PRJs — What This Unlocks

### Existing PRJs Directly Dependent on PRJ-025 Research

> These PRJs exist but have incomplete implementation or design decisions that are blocked pending PRJ-025 research completion.

| PRJ | Title | Dependency | What PRJ-025 Unlocks |
|-----|-------|------------|---------------------|
| **PRJ-015** | HybridArchitecture (GB10 + MI300X/MI325X) | Track 2, 3 | OpenTofu modules for GPU provisioning, deployment architecture decisions |
| **PRJ-016** | LiteLLM AI Gateway | Track 4, 3 | Routing strategy, Redis vs alternatives, tenant isolation model |
| **PRJ-017** | Observability (Langfuse + LGTM) | Track 5 | Hub + Spoke observability architecture, agent deployment per tenant type |
| **PRJ-023** | Context Persistence (mem0) | Track 4, 3 | Memory architecture per tenant, hub vs per-tenant mem0 |
| **PRJ-024** | Secrets Management (Infisical) | Track 2, 6 | OpenTofu + Ansible secret management automation, per-tier secrets |
| **PRJ-026** | Cybersecurity Frameworks + ISMS | Track 6, 3 | Security tooling per tier, compliance controls per deployment type |
| **PRJ-032** | OpenTofu IaC | Track 2 | OpenTofu module structure, state backend, DO provider config, Ansible handoff |
| **PRJ-035** | Semaphore UI | Track 2, 3 | CI/CD pipeline architecture, deployment automation strategy |

### Future PRJs That Will Stem From PRJ-025 Research

> These PRJ documents do not yet exist but will be created once each research track is complete. PRJ-025 is the seed from which all platform implementation PRJs grow.

| Research Track | Expected New PRJs | Type |
|----------------|-------------------|------|
| **Track 2** (OpenTofu + Ansible) | PRJ-032 implementation docs | Implementation |
| **Track 3** (Deployment Architecture) | PRJ-0XX_Hub-Tenant-Architecture.md | Implementation |
| **Track 4** (Core Infrastructure) | PRJ-0XX_Redis-Config.md, PRJ-0XX_LGTM-Stack.md | Implementation |
| **Track 5** (Observability Hub + Spoke) | PRJ-0XX_Observability-Hub.md, PRJ-0XX_Observability-Spokes.md | Implementation |
| **Track 6** (Security + Compliance) | PRJ-0XX_K8s-Security-Stack.md, PRJ-0XX_Compliance-Automation.md | Implementation |
| **Track 7** (Platform + Portal) | PRJ-0XX_Backstage.md, PRJ-0XX_Keycloak.md | Implementation |
| **Track 8** (AI + Testing) | PRJ-0XX_AI-Ops-Agents.md, PRJ-0XX_Load-Chaos-Testing.md | Implementation |

> **Each research track completion = new PRJ documents created for its implementation.** PRJ-025 is the mother document; the research tracks give birth to implementation PRJs.

---

## 📋 SDLC Status — Research + Design Required

### What Happened + Why Implementation Paused

| Event | Detail |
|-------|--------|
| **W10 Implementation Started** | @RMN began LiteLLM/Redis, Langfuse, Infisical; @LDC began OpenTofu |
| **Issue Encountered** | Implementation issues arose from lack of finished roadmap, design, and plan |
| **Root Cause** | jAIMSnet is extremely complex (many tools + hub + tenant architecture) — cannot implement without complete research + design |
| **Decision** | Follow SDLC: Complete research + design first, THEN implement |
| **Current State** | Research Track 1 complete ✅, Tracks 2-8 planned with detailed context |

### SDLC Phases for jAIMSnet

| Phase | Status | Detail |
|-------|--------|--------|
| **1. Requirements** | ✅ COMPLETE | PRJ-025 context volleys, business questions to @GTM/@THY |
| **2. Research** | 🔄 50% | Track 1 complete, Tracks 2-8 detailed and planned |
| **3. Analysis + Design** | ⬜ TODO | Depends on research track completion + @GTM/@THY answers |
| **4. Architecture Decisions** | ⬜ TODO | ADRs (docs/decisions/) to be created per track |
| **5. Implementation** | ⏸️ PAUSED | Cannot resume until Phase 2-4 complete |
| **6. Testing** | ⬜ TODO | Integration, load, chaos testing (Track 8) |
| **7. Operations** | ⬜ TODO | Runbooks, incident response (docs/runbooks/) |

### Blockers — @GTM/@THY Business Questions (Unanswered)

> Some research is blocked pending business/architectural answers that were asked in W11 (11Mar2026).

| Question Category | Impact | Status |
|-------------------|--------|--------|
| User counts + SLA requirements | Affects droplet vs cluster decision matrix | ⏳ Awaiting @GTM/@THY |
| Product tier definitions | Affects multi-tenancy architecture | ⏳ Awaiting @GTM/@THY |
| Budget constraints + billing model | Affects cost optimization tool selection | ⏳ Awaiting @GTM/@THY |
| Compliance requirements per tier | Affects security policy configuration | ⏳ Awaiting @GTM/@THY |
| Migration strategy + client expectations | Affects OpenTofu module design | ⏳ Awaiting @GTM/@THY |
| Multi-region requirements | Affects hub design + OpenTofu modules | ⏳ Awaiting @GTM/@THY |

---

## 📋 jAIMSnet Architecture — Current State

### High-Level Architecture

```
Internet → DO Load Balancer (129.212.240.75 · ATL1)
  → ingress-nginx
    → litellm.jAIMS.app  → LiteLLM     (gateway/)
    → langfuse.jAIMS.app → Langfuse    (observability/)
    → pgadmin.jAIMS.app  → pgAdmin     (observability/)
    → cert-manager (auto-TLS via Let's Encrypt)

LiteLLM → Redis            (gateway/redis)
LiteLLM → Langfuse         (callback / traces)
LiteLLM → OpenRouter / vLLM (providers)
LiteLLM → PostgreSQL       (spend tracking)
Langfuse → PostgreSQL      (traces + evals)

Infisical Cloud → Infisical Operator → K8s Secrets → Pods

Uptime Kuma (STANDALONE DROPLET · NYC1) → monitors all endpoints
  Rationale: NYC1 for geographic diversity — if ATL1 fails, Kuma still monitors

[Phase 2] vLLM on MI300X/MI325X GPU Droplet (VPC) → LiteLLM backend
[Phase 2] Prometheus + Grafana + Loki + Alloy + Mimir
[Phase 3] ArgoCD, Watchtower, Kyverno, Trivy, CrowdSec, Falco, kube-bench,
          docker-bench, Gitleaks, Syft, Grype, Ansible, full CI pipelines
[Phase 4] AI automation agents, customer-facing platform, k6 load testing,
          Litmus chaos engineering, Backstage IDP
```

### GitHub Flow Branching Strategy

| Branch | Purpose |
|--------|---------|
| `main` | Production — protected, requires PR + review |
| `develop` | Integration branch |
| `feature/*` | Feature branches (e.g., `feature/litellm-routing`) |
| `fix/*` | Bug fixes |
| `release/*` | Release preparation |

### Hybrid CI/CD + GitOps Pipeline

| Layer | Tool | Target |
|-------|------|--------|
| **CI** | GitHub Actions | Build, test, scan |
| **GitOps (K8s)** | ArgoCD (UNDER EVALUATION vs FluxCD) | DOKS cluster (jAIMSnet) |
| **GitOps (Docker)** | Watchtower | Docker Droplets (tenants) |
| **IaC** | OpenTofu | DO resources (clusters, droplets, DNS, LB) |
| **Config** | Ansible | Docker Droplet configuration |

---

## 📋 Repository Structure (Monorepo)

> **Research Track 1 Complete.** Structured monorepo adopted. GitHub Flow branching. Hybrid CI/CD + GitOps.

```
jaimsnet/
├── README.md                          # Root README — project overview
├── docs/
│   ├── README.md                      # Docs index — Diátaxis navigation
│   ├── decisions/                     # ADRs (Explanation quadrant)
│   │   ├── template.md                # ADR template
│   │   ├── 001-litellm-over-alternatives.md  # Skeleton (fill after research)
│   │   ├── 002-langfuse-over-phoenix.md      # Skeleton (fill after research)
│   │   ├── 003-doks-over-droplet.md          # Skeleton (fill after research)
│   │   ├── 004-infisical-for-secrets.md      # Skeleton (fill after research)
│   │   ├── 005-monorepo-structure.md         # EXISTS (Track 1.1)
│   │   ├── 006-branch-strategy.md            # EXISTS (Track 1.2)
│   │   ├── 007-cicd-architecture.md          # EXISTS (Track 1.3)
│   │   ├── 008-documentation-structure.md    # EXISTS (Track 1.4)
│   │   └── TBD-<future-decisions>.md         # Later (all tracks)
│   ├── runbooks/                      # Operational runbooks (How-To quadrant)
│   │   ├── template.md                # Runbook template
│   │   ├── litellm-operations.md      # Create after LiteLLM deployed
│   │   ├── langfuse-operations.md     # Create after Langfuse deployed
│   │   ├── secret-rotation.md         # Create after Infisical deployed
│   │   ├── disaster-recovery.md       # Create after backup strategy defined
│   │   ├── gpu-operations.md          # Create after vLLM deployed
│   │   ├── backup-restore.md          # Create after backup strategy defined
│   │   ├── security-incident.md       # Create after security tools deployed
│   │   └── incident-response.md       # Create after alerting configured
│   ├── architecture/                  # Architecture docs (Explanation quadrant)
│   │   ├── overview.md                # System overview
│   │   ├── deployment-model.md        # Create after Track 3 complete
│   │   ├── hub-spoke-topology.md      # Create after Track 6 complete
│   │   └── diagrams/
│   │       ├── hub-cluster.drawio
│   │       └── spoke-agents.drawio
│   ├── guides/                        # How-To + Tutorials (Diátaxis)
│   │   ├── getting-started.md
│   │   ├── deploy-cluster.md          # Create after Track 2 complete
│   │   ├── deploy-droplet.md          # Create after Track 2 complete
│   │   ├── add-client.md              # Create after multi-tenancy defined
│   │   └── troubleshoot-common.md
│   ├── reference/                     # Technical Reference (Diátaxis)
│   │   ├── api-reference.md
│   │   ├── configuration-options.md
│   │   ├── weownver-standard.md       # L-094, L-115 reference
│   │   └── glossary.md
│   ├── compliance/                    # ISO 42001 evidence
│   │   ├── control-mapping.md         # Create after Track 6 complete
│   │   ├── evidence-collection.md     # Create after Track 6 complete
│   │   └── audit-checklist.md         # Create after Track 6 complete
│   └── research/                      # Research notes (temporary)
│       ├── track1-summary.md          # Track 1 research summary
│       ├── track2/
│       ├── track3/
│       └── ...
├── gateway/         # LiteLLM overview
├── observability/   # Observability stack overview
├── iac/             # OpenTofu modules + Ansible playbooks
├── security/        # Security tooling overview
├── compliance/      # Compliance framework overview
├── testing/         # Testing framework overview
├── cluster/         # Cluster configs overview
├── ingress/         # Ingress config overview
├── secrets/         # Secrets management overview
├── gitops/          # GitOps config overview
├── gpu/             # GPU inference overview
├── portal/          # Backstage config overview (Phase 4)
├── identity/        # Keycloak config overview
├── cost/            # OpenCost config overview
├── memory/          # mem0 config overview (PRJ-023)
├── mcp/             # MCP servers overview
└── scripts/         # Utility scripts overview
```

---

## 📋 Namespace Architecture

| Namespace | Services | Phase | Status |
|-----------|----------|-------|--------|
| `gateway` | LiteLLM, Redis | Phase 1 🔴 | 🔄 In Progress (paused) |
| `observability` | Langfuse, pgAdmin, Prometheus, Grafana, Loki | Phase 1–2 | 🔄 In Progress (paused) |
| `secrets` | Infisical Operator | Phase 1 🔴 | 🔄 In Progress (paused) |
| `automation` | Semaphore UI (PRJ-035) | Phase 1 🔴 | 📋 Planned (W12) |
| `memory` | mem0 (PRJ-023) | Phase 1 🔴 | 📋 Planned (W12) |
| `gpu` | vLLM on MI300X/MI325X | Phase 2 🟠 | 📋 Planned |
| `security` | Kyverno, Trivy, Falco | Phase 2–3 | 📋 Planned |
| `gitops` | ArgoCD | Phase 3 🟡 | 📋 Planned |

---

## 📋 Platform Status — All Tools by Phase

> **⚠️ IMPORTANT:** Tool selection for Phase 2-4 is PRELIMINARY. Final decisions will be made after research tracks 2-8 are completed. Tools may change based on main hub K8s cluster vs tenant K8s cluster vs tenant Docker Droplet architecture.

### Phase 1 🔴 — Core Platform (~90% Infrastructure, Implementation Paused)

| Component | Tool | Status | Decision |
|-----------|------|--------|----------|
| Ingress controller | ingress-nginx | 🔄 Paused | LOCKED |
| TLS automation | cert-manager + Let's Encrypt | 🔄 Paused | LOCKED |
| AI gateway | LiteLLM | 🔄 Paused | LOCKED |
| Response caching | Redis | 🔄 Paused | LOCKED (pending Track 4 validation) |
| LLM observability | Langfuse | 🔄 Paused | LOCKED |
| Secret management | Infisical Operator | 🔄 Paused | LOCKED |
| Endpoint monitoring | Uptime Kuma (NYC1 Droplet) | ✅ LIVE | LOCKED |
| Infrastructure as Code | OpenTofu | 🔄 Started (paused) | LOCKED (pending Track 2) |
| Config automation | Ansible | 📋 Planned | LOCKED (pending Track 2) |
| Context memory | mem0 (PRJ-023) | 📋 Planned | LOCKED (W12) |
| CI automation | Semaphore UI (PRJ-035) | 📋 Planned | LOCKED (W12) |

### Phase 2 🟠 — Observability + GPU (~50% Planned)

| Component | Tool | Status | Decision |
|-----------|------|--------|----------|
| Metrics + dashboards | Prometheus + Grafana | 📋 Planned | LIKELY (industry standard) |
| Log aggregation | Loki + Alloy | 📋 Planned | UNDER EVALUATION (Track 4: Alloy vs Fluent Bit vs OTel) |
| Long-term metrics | Mimir | 📋 Planned | UNDER EVALUATION (Track 4: Mimir vs Thanos vs VictoriaMetrics) |
| GPU inference | vLLM on AMD MI300X/MI325X | 📋 Planned | LOCKED (DO GPU — awaiting availability) |
| Policy engine | Kyverno | 📋 Planned | UNDER EVALUATION (Track 6: Kyverno vs OPA) |
| Network policies | Cilium | 📋 Planned | UNDER EVALUATION (Track 6: Cilium vs Calico) |

### Phase 3 🟡 — GitOps + Security + Compliance (~25% Planned)

| Component | Tool | Status | Decision |
|-----------|------|--------|----------|
| GitOps (K8s) | ArgoCD | 📋 Planned | UNDER EVALUATION (Track 4: ArgoCD vs FluxCD) |
| GitOps (Docker) | Watchtower | 📋 Planned | UNDER EVALUATION (Track 4: Watchtower vs GH Actions) |
| Image scanning | Trivy Operator | 📋 Planned | LIKELY (FOSS, comprehensive) |
| Runtime security | Falco | 📋 Planned | UNDER EVALUATION (Track 6: Falco vs Tracee) |
| IDS + WAF | CrowdSec | 📋 Planned | UNDER EVALUATION (Track 6: CrowdSec vs Fail2Ban) |
| K8s benchmarking | kube-bench | 📋 Planned | LIKELY (CIS benchmarks) |
| Docker benchmarking | docker-bench | 📋 Planned | LIKELY (CIS benchmarks) |
| Secret scanning (CI) | Gitleaks | 📋 Planned | LIKELY (FOSS) |
| SBOM generation | Syft + Grype | 📋 Planned | UNDER EVALUATION |
| Droplet automation | Ansible | 📋 Planned | LOCKED (pending Track 2) |

### Phase 4 🟢 — AI Automation + Customer Platform (~0% Planned)

| Component | Tool | Status | Decision |
|-----------|------|--------|----------|
| Developer portal / IDP | Backstage | 📋 Planned (Season 4) | UNDER EVALUATION (Track 7: Backstage vs Portainer vs Custom) |
| SSO/Identity | Keycloak | 📋 Planned | UNDER EVALUATION (Track 7: Keycloak vs Auth0 vs ZITADEL) |
| Cost optimization | OpenCost | 📋 Planned | UNDER EVALUATION (Track 7: OpenCost vs Kubecost) |
| AI agents for Ops | TBD | 📋 Planned | UNDER EVALUATION (Track 8: Kagent vs k8sGPT vs custom) |
| MCP servers | TBD | 📋 Planned | UNDER EVALUATION (Track 8) |
| Load testing | k6 / Locust | 📋 Planned | UNDER EVALUATION (Track 8) |
| Chaos engineering | Litmus / Chaos Mesh | 📋 Planned | UNDER EVALUATION (Track 8) |
| Integration testing | Testkube / Custom | 📋 Planned | UNDER EVALUATION (Track 8) |

---

## 📋 Tool Evaluation — Locked vs Under Evaluation

### LOCKED Decisions (Phase 1)

| Tool | Why Locked | Alternative Considered |
|------|------------|----------------------|
| **LiteLLM** | MIT license, native Langfuse callback, 100+ providers, multi-tenant | Portkey (proprietary), Traefik (general proxy) |
| **Langfuse** | MIT license, native LiteLLM integration, auto cost tracking | Phoenix (ELv2, not OSI), custom OTEL |
| **ingress-nginx** | K8s standard, well-documented, DO-compatible | Traefik, HAProxy |
| **cert-manager** | K8s native, Let's Encrypt auto-renewal | Manual certs, commercial CA |
| **Redis** | Industry standard, LiteLLM native support (pending Track 4 validation) | Memcached, Dragonfly |
| **Infisical Operator** | K8s native, cloud-free tier, MIT license | External Secrets Operator, Vault |
| **Uptime Kuma** | FOSS, simple, self-hosted, ~$6/mo Droplet, NYC1 for resilience | Pingdom, UptimeRobot (SaaS) |
| **OpenTofu** | MPL 2.0 FOSS, Terraform-compatible | Terraform (BSL) |
| **Ansible** | Mature FOSS, agentless, Python | Chef, Puppet, SaltStack |
| **mem0** | Apache 2.0 FOSS, 25k+ stars, PGvector backend (PRJ-023) | Zep, custom build |
| **Semaphore UI** | FOSS, K8s-native deployment (@LDC) | Droplet deployment (rejected) |

### UNDER EVALUATION (Phase 2-4)

| Decision | Options | Research Track | Blocked By |
|----------|---------|----------------|------------|
| **Log Collection** | Alloy vs Fluent Bit vs OTel Collector | Track 4 | Not blocked |
| **Long-term Metrics** | Mimir vs Thanos vs VictoriaMetrics | Track 4 | Not blocked |
| **GitOps (K8s)** | ArgoCD vs FluxCD | Track 4 | Not blocked |
| **GitOps (Docker)** | Watchtower vs GH Actions | Track 4 | Not blocked |
| **Policy Engine** | Kyverno vs OPA Gatekeeper | Track 6 | Not blocked |
| **Runtime Security** | Falco vs Tracee vs Sysdig | Track 6 | Not blocked |
| **IDS + WAF** | CrowdSec vs Fail2Ban vs ModSecurity | Track 6 | Not blocked |
| **Network Policies** | Cilium vs Calico | Track 6 | Not blocked |
| **Developer Portal** | Backstage vs Portainer vs Custom | Track 7 | Not blocked |
| **SSO/Identity** | Keycloak vs Auth0 vs ZITADEL | Track 7 | Not blocked |
| **Cost Optimization** | OpenCost vs Kubecost | Track 7 | Not blocked |
| **AI Agents for Ops** | Kagent vs k8sGPT vs custom | Track 8 | Not blocked |
| **Load Testing** | k6 vs Locust vs JMeter | Track 8 | Not blocked |
| **Chaos Engineering** | Litmus vs Chaos Mesh vs Gremlin | Track 8 | Not blocked |

---

## 📋 Architecture Decisions — Hub vs Tenant

> **⚠️ CRITICAL:** Final architecture TBD based on scale, cost, and operational complexity. Partially blocked pending @GTM/@THY business questions.

### Deployment Architecture Options

| Option | Main Hub | Tenants | Pros | Cons | Status |
|--------|----------|---------|------|------|--------|
| **A: Single Cluster** | jAIMSnet DOKS (ATL1) | Namespaces in same cluster | Simple, cheap, shared resources | No isolation, single point of failure | 🔄 Current (Phase 1) |
| **B: Hub + Tenant K8s** | jAIMSnet DOKS (ATL1) | Per-tenant DOKS clusters | Isolation, scalability | Complex, expensive (~$24/mo per tenant) | 📋 Phase 3+ |
| **C: Hub + Tenant Docker** | jAIMSnet DOKS (ATL1) | Per-tenant Docker Droplets (~$6-12/mo) | Isolation, cheaper than K8s | Less automation, manual updates | 📋 Phase 2+ |
| **D: Hybrid** | jAIMSnet DOKS (ATL1) | Mix of K8s + Docker based on tenant needs | Flexibility, cost optimization | Most complex to manage | 📋 Recommended (pending Track 3) |

### Recommended Architecture (Hybrid — Option D)

| Tenant Type | Deployment | Rationale |
|-------------|------------|-----------|
| **Internal (WeOwnNet)** | jAIMSnet DOKS (same cluster, separate namespace) | No isolation needed, cost-effective |
| **Enterprise Customers** | Dedicated DOKS cluster (per customer) | Full isolation, compliance, SLA |
| **SMB Customers** | Docker Droplet (shared or dedicated) | Cost-effective, sufficient isolation |
| **Trial/Demo ("0 to 100")** | Docker Droplet | Low cost, easy provisioning |

### Namespace Quotas (Phase 1)

| Resource | Request | Limit | Purpose |
|----------|---------|-------|---------|
| CPU | 500m | 2000m | Prevent resource hogging |
| Memory | 1Gi | 4Gi | Prevent OOM issues |
| Storage | 10Gi | 50Gi | Control disk usage |
| Pods | 10 | 50 | Limit workload count |

---

## 📋 8 Research Tracks — Full Research Plan

> **Research Track 1 is COMPLETE (✅). Tracks 2-8 are PLANNED with detailed context. Overall roadmap = ~50% complete.**
>
> **Each completed research track will produce one or more new downstream PRJ documents with full implementation details. This document is the roadmap — not the implementation guide.**

### Research Track 1: Repository & Team Structure — ✅ COMPLETE

| Deliverable | Status |
|-------------|--------|
| ADR-005: Monorepo Structure | ✅ EXISTS |
| ADR-006: Branch Strategy (GitHub Flow) | ✅ EXISTS |
| ADR-007: CI/CD Architecture (Hybrid) | ✅ EXISTS |
| ADR-008: Documentation Structure (Diátaxis) | ✅ EXISTS |
| Repo structure | ✅ DEFINED |
| **New PRJs created** | None (foundational structure, not standalone PRJ) |

### Research Track 2: OpenTofu + Ansible Provisioning — 🔄 IN PROGRESS (Not Blocked)

| Topic | Status | Output |
|-------|--------|--------|
| OpenTofu Module Structure | 📋 Planned | Module directory structure + examples |
| OpenTofu State Backend (DO Spaces) | 📋 Planned | State backend config + security policy |
| OpenTofu DO Provider Config | 📋 Planned | Provider config best practices |
| OpenTofu CI/CD Integration | 📋 Planned | Workflow configs + protection rules |
| OpenTofu + Infisical Integration | 📋 Planned | Integration pattern + examples |
| Ansible Playbook Structure | 📋 Planned | Playbook directory structure |
| Ansible Role Organization | 📋 Planned | Role inventory + templates |
| Ansible Inventory Management | 📋 Planned | Inventory config + DO integration |
| Ansible Docker Setup | 📋 Planned | Docker role + CIS benchmark integration |
| **Expected New PRJ** | **PRJ-032_OpenTofu-IaC.md** | Implementation guide |

### Research Track 3: Deployment Architecture — 🔴 BLOCKED (@GTM/@THY)

| Topic | Status | Blocked By |
|-------|--------|------------|
| Droplet vs Cluster Decision Matrix | 🔴 Blocked | User counts, SLA, budget, product definitions |
| Migration Strategy (Droplet ↔ Cluster) | 🔴 Blocked | Migration strategy from @GTM |
| Shared vs Dedicated Infrastructure | 🔴 Blocked | Isolation requirements + compliance |
| Multi-Region Architecture | 🔴 Blocked | If/when multi-region required |
| Client Tenancy Model | 🔴 Blocked | Product definitions |
| **Expected New PRJs** | Hub-Tenant-Architecture.md | Implementation guide |

### Research Track 4: Core Infrastructure — 🟠 Partially Blocked

| Topic | Status | Output |
|-------|--------|--------|
| Redis vs Alternatives for LiteLLM | 📋 Planned (not blocked) | Tool selection |
| Memory Buffer (mem0 vs Zep) | ✅ Decided — mem0 (PRJ-023) | DONE |
| Long-term Metrics (Mimir vs Thanos vs VictoriaMetrics) | 📋 Planned (not blocked) | Tool selection |
| Log Collection (Alloy vs Fluent Bit vs OTel) | 📋 Planned (not blocked) | Tool selection |
| GitOps for Droplets (Watchtower vs GH Actions) | 📋 Planned (not blocked) | Tool selection |
| **Expected New PRJs** | Redis-Config.md, LGTM-Stack-Config.md | Implementation guides |

### Research Track 5: Observability Hub & Spoke — 🟠 Partially Blocked

| Topic | Status | Output |
|-------|--------|--------|
| Hub Observability Stack | 📋 Planned (not blocked) | Hub architecture + Helm configs |
| Spoke Agents (Cluster) | 📋 Planned (not blocked) | Agent deployment guide |
| Spoke Agents (Droplet) | 📋 Planned (not blocked) | Agent deployment guide |
| Data Forwarding | 📋 Planned (not blocked) | Data pipeline architecture |
| Retention Policies | 🔴 Blocked (compliance per tier) | Retention policy ADR |
| Dashboard + Alerting Strategy | 📋 Planned (not blocked) | Alerting architecture |
| **Expected New PRJs** | Observability-Hub.md, Observability-Spokes.md | Implementation guides |

### Research Track 6: Security & Compliance — 🟠 Partially Blocked

| Topic | Status | Output |
|-------|--------|--------|
| Policy Engine (Kyverno vs OPA) | 📋 Planned (not blocked) | Tool selection + policy library |
| Runtime Security (Falco vs Tracee) | 📋 Planned (not blocked) | Tool selection + rule set |
| IDS/WAF (CrowdSec vs Fail2Ban) | 📋 Planned (not blocked) | Tool selection + integration |
| Image Scanning (Trivy vs Clair) | 📋 Planned (not blocked) | Tool selection + CI integration |
| Compliance Evidence Mapping | 🔴 Blocked (compliance reqs per tier) | Evidence matrix |
| Network Policy (Cilium vs Calico) | 📋 Planned (not blocked) | Tool selection + policy examples |
| CIS Benchmarking Automation | 📋 Planned (not blocked) | Benchmark automation scripts |
| **Expected New PRJs** | K8s-Security-Stack.md, Compliance-Automation.md | Implementation guides |

### Research Track 7: Platform & Portal — 📋 Planned (Mostly Not Blocked)

| Topic | Status | Output |
|-------|--------|--------|
| Developer Portal (Backstage vs Portainer) | 📋 Planned (not blocked) — Phase 4 | Tool selection + deployment |
| SSO/Identity (Keycloak vs Auth0 vs ZITADEL) | 📋 Planned (not blocked) | Tool selection + integration |
| Cost Optimization (OpenCost vs Kubecost) | 📋 Planned (not blocked) | Tool selection + metrics |
| Portal Access Model | ⚠️ Partially blocked (product tier access) | Access control architecture |
| **Expected New PRJs** | Backstage-IDP.md, Keycloak-SSO.md | Implementation guides |

### Research Track 8: AI & Testing — 📋 Planned (Not Blocked)

| Topic | Status | Output |
|-------|--------|--------|
| OpenLLMetry Necessity | 📋 Planned | Decision + integration plan |
| Load Testing (k6 vs Locust) | 📋 Planned | Tool selection + test scenarios |
| Chaos Engineering (Litmus vs Chaos Mesh) | 📋 Planned | Tool selection + chaos scenarios |
| AI Agents for Ops (Kagent vs k8sGPT) | 📋 Planned | Tool selection + use cases |
| MCP Servers | 📋 Planned | MCP strategy ADR |
| Integration Testing (Testkube) | 📋 Planned | Tool selection + test suite |
| **Expected New PRJs** | AI-Ops-Agents.md, Load-Chaos-Testing.md | Implementation guides |

### Research Prioritization

| Phase | Tracks | Status | When |
|-------|--------|--------|------|
| **Phase A (Start Now)** | Track 1 ✅, Track 2, Track 4, Track 5 (hub), Track 8 | 🟢 Not Blocked | Immediately |
| **Phase B (Continue)** | Track 5 (spoke), Track 6, Track 7 | 🟠 Partially Blocked | While awaiting @GTM/@THY |
| **Phase C (After Answers)** | Track 3, Tier-specific Track 2/5 | 🔴 Blocked | After @GTM/@THY respond |

---

## 📋 ISO/IEC 42001 Alignment

| ISO 42001 Requirement | jAIMSnet Implementation | Phase |
|----------------------|------------------------|-------|
| **AI system monitoring** | Langfuse traces + dashboards | Phase 1 🔴 |
| **Risk management** | Observability → incident detection | Phase 1 🔴 |
| **Performance evaluation** | Token cost, latency, error rates | Phase 1 🔴 |
| **Continual improvement** | Data-driven optimization | Phase 2 🟠 |
| **Documentation** | #FedArch governance (SharedKernel, BP, PROTO) | Phase 1 🔴 |
| **Accountability** | CCC attribution system | Phase 1 🔴 |
| **Infrastructure monitoring** | Prometheus + Grafana + Loki | Phase 2 🟠 |
| **Security controls** | Kyverno, Trivy, Falco, CrowdSec | Phase 3 🟡 |
| **Access control** | Infisical secrets, RBAC | Phase 1 🔴 |
| **Audit logging** | All actions logged to PostgreSQL | Phase 1 🔴 |

### Compliance Roadmap

| Phase | Framework | Status |
|-------|-----------|--------|
| **Phase 1 🔴** | ISO 42001 (basic) | 🔄 In Progress |
| **Phase 2 🟠** | ISO 27001 (ISMS) | 📋 Planned |
| **Phase 3 🟡** | SOC 2 Type II | 📋 Planned |
| **Phase 3 🟡** | NIST CSF 2.0 | 📋 Planned |
| **Phase 3 🟡** | CIS Controls v8 | 📋 Planned |
| **Phase 4 🟢** | FedRAMP | 📋 Planned |

---

## 📋 Domains — Current + Planned

### Registered Domains (6 — Porkbun / Web3FreedomClub)

| # | Domain | Purpose | Status |
|---|--------|---------|--------|
| 1 | **jAIMS.network** | **Primary** — infrastructure brand | ✅ Registered |
| 2 | jAIMS.app | App/tool landing page | ✅ Registered |
| 3 | jAIMS.xyz | Alternative | ✅ Registered |
| 4 | jAIMSnet.com | Corporate redirect | ✅ Registered |
| 5 | jAIMSnet.org | Community/open-source | ✅ Registered |
| 6 | jAIMSnet.xyz | Alternative | ✅ Registered |

### Service Domains (Planned)

| Service | Domain | Phase | Status |
|---------|--------|-------|--------|
| **LiteLLM** | litellm.jAIMS.app | Phase 1 🔴 | 🔄 In Progress |
| **Langfuse** | langfuse.jAIMS.app | Phase 1 🔴 | 🔄 In Progress |
| **pgAdmin** | pgadmin.jAIMS.app | Phase 1 🔴 | 📋 Planned |
| **Uptime Kuma** | kuma.jAIMS.app | Phase 1 🔴 | ✅ LIVE (NYC1) |
| **Grafana** | grafana.jAIMS.app | Phase 2 🟠 | 📋 Planned |
| **ArgoCD** | argocd.jAIMS.app | Phase 3 🟡 | 📋 Planned |
| **Wildcard** | *.jAIMS.app | Phase 1 🔴 | 📋 Planned |

---

## 📋 Integration with Other PRJs

| PRJ | Title | Integration Point | Namespace | Dependency Type |
|-----|-------|-------------------|-----------|-----------------|
| **PRJ-015** | HybridArchitecture (GB10 + MI300X/MI325X) | GPU inference backend (Phase 2) | `gpu` | 🔴 Blocked on Track 2+3 |
| **PRJ-016** | LiteLLM AI Gateway | Deployed IN jAIMSnet DOKS | `gateway` | 🔴 Blocked on Track 4+3 |
| **PRJ-017** | Observability (Langfuse + LGTM) | Langfuse + LGTM+ IN jAIMSnet | `observability` | 🔴 Blocked on Track 5 |
| **PRJ-018** | P.O.P. Database | PostgreSQL cluster used by jAIMSnet | Shared (VPC) | 🟡 Partial (PG deployed) |
| **PRJ-021** | PostgreSQL Operations | DO cluster, LB, Managed PG | Shared (VPC) | 🟡 Partial (PG deployed) |
| **PRJ-023** | Context Persistence (mem0) | mem0 IN jAIMSnet | `memory` | 🔴 Blocked on Track 4+3 |
| **PRJ-024** | Secrets Management (Infisical) | Infisical Operator IN jAIMSnet | `secrets` | 🔴 Blocked on Track 2+6 |
| **PRJ-026** | Cybersecurity Frameworks + ISMS | Security tools via jAIMSnet | `security` | 🔴 Blocked on Track 6+3 |
| **PRJ-032** | OpenTofu IaC | IaC for all DO resources | `iac/` | 🔴 Blocked on Track 2 |
| **PRJ-035** | Semaphore UI | CI automation IN jAIMSnet | `automation` | 🔴 Blocked on Track 2+3 |

---

## 📋 Roadmap Completion Status

### Current Progress (~50% Roadmap Complete)

| Section | Status | Notes |
|---------|--------|-------|
| Research Track 1 (Repo + Team) | ✅ COMPLETE | Monorepo, GitHub Flow, Hybrid CI/CD, Diátaxis docs |
| Infrastructure Live | ✅ COMPLETE | DOKS cluster, LB, PG, Uptime Kuma (NYC1) |
| Research Track 2 (OpenTofu + Ansible) | 📋 Planned | Not blocked — PRJ-032 depends on this |
| Research Track 3 (Deployment Architecture) | 🔴 Blocked | Awaiting @GTM/@THY — blocks many PRJs |
| Research Track 4 (Core Infrastructure) | 📋 Planned | mem0 decided (PRJ-023) |
| Research Track 5 (Observability Hub + Spoke) | 📋 Planned | Hub not blocked, Spoke + retention partially blocked |
| Research Track 6 (Security + Compliance) | 📋 Planned | Tool selection not blocked, policy config partially blocked |
| Research Track 7 (Platform + Portal) | 📋 Planned | Mostly not blocked, Backstage = Phase 4 (Season 4) |
| Research Track 8 (AI + Testing) | 📋 Planned | Not blocked |
| Phase 1 Implementation | ⏸️ PAUSED | Resume after research complete |
| Phase 2 Implementation | ⬜ TODO | — |
| Phase 3 Implementation | ⬜ TODO | — |
| Phase 4 Implementation | ⬜ TODO | — |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| **3.2.3.2** | **2026-W12** | **GTM_2026-W10_026** | **GTM_2026-W11_330** | **Renamed document: PRJ-025_jAIMSnet-Research-Roadmap.md (previously PRJ-025_jAIMSnet-Platform-Engineering.md). Title updated: jAIMSnet — Research + Roadmap. Added scope clarification (this doc = research + roadmap ONLY, not implementation guide). Priority elevated to 🔴 HIGHEST PRIORITY IN ECOSYSTEM. Added Section 3: Why This Research is Critical. Added Section 4: Dependent PRJs — What This Unlocks (PRJ-015/016/017/023/024/026/032/035 all dependent). Added expected new PRJs per research track. Added Dependency Type column to Integration table. Clarified that each research track completion creates downstream implementation PRJs. Updated type to Infrastructure + Governance — Foundational Research + Platform Roadmap.** |
| 3.2.3.1 | 2026-W12 | GTM_2026-W10_026 | GTM_2026-W11_330 | Initial document creation — jAIMSnet brand identity, SDLC alert (implementation paused), infrastructure live (DOKS/LB/Kuma NYC1), monorepo structure (Track 1 complete ADR-005/006/007/008), 8 namespaces, GitHub Flow + Hybrid CI/CD, platform status by phase, 8 research tracks, blocker analysis (@GTM/@THY questions), Hub vs Tenant architecture (Hybrid Option D), ISO 42001 alignment, 6 domains, 9 PRJ integrations, compliance roadmap |

---

## 📋 Related Documents

| Document | Version | #masterCCC | Approval | Location |
|----------|---------|------------|----------|----------|
| PRJ-015_HybridArchitecture.md | 3.2.3.1 | GTM_2026-W09_104 | GTM_2026-W09_108 | _PROJECTS_/ (GH LIVE) |
| PRJ-016_AIGateway-LiteLLM.md | 3.2.3.1 | GTM_2026-W10_122 | GTM_2026-W10_026 | _PROJECTS_/ (GH LIVE) |
| PRJ-017_Observability.md | 3.2.3.1 | GTM_2026-W09_121 | GTM_2026-W09_108 | _PROJECTS_/ (GH LIVE) |
| PRJ-021_PostgreSQL-Operations.md | 3.2.3.1 | GTM_2026-W10_026 | GTM_2026-W10_026 | _PROJECTS_/ |
| PRJ-023_Context-Persistence-Pipeline.md | 3.2.3.1 | GTM_2026-W10_026 | GTM_2026-W11_326 | _PROJECTS_/ |
| PRJ-024_Secrets-Management-Infisical.md | 3.2.3.1 | GTM_2026-W10_026 | GTM_2026-W11_328 | _PROJECTS_/ |
| PRJ-026_Cybersecurity-Frameworks-ISMS.md | 3.2.3.1 | GTM_2026-W10_026 | GTM_2026-W10_026 | _PROJECTS_/ |
| PRJ-032_OpenTofu-IaC.md | TBD | TBD | ⬜ TBD | _PROJECTS_/ (Future — from Track 2) |
| PRJ-035_SemaphoreUI.md | TBD | TBD | ⬜ TBD | _PROJECTS_/ (Future — from Track 2+3) |
| GUIDE-011_Governance-Oversight-VSA-Process.md | 3.2.1.1 | GTM_2026-W10_066 | GTM_2026-W10_073 | _GUIDES_/ |

---

## 📋 Discovered By (BP-047)

| CCC | Contributor | Role | Context |
|-----|-------------|------|---------|
| RMN | Roman Di Domizio | AI Platform Engineer | Conceived jAIMSnet platform (W10), designed architecture, deployed DOKS cluster + LB + ingress (paused), LiteLLM + Langfuse + Infisical (paused), research track 1 complete, 8-track research plan created, SDLC enforcement decision |
| GTM | Jason Younker | Co-Founder | Approved PRJ assignment (GTM_2026-W10_026), jAIMSnet green light, domain registration, approved PRJ-025 with updates (GTM_2026-W11_330) |
| LDC | Dhruv | Agentic AI Engineer | OpenTofu implementation started (paused), platform engineering feedback, Semaphore deployment in DOKS |
| SHD | Shahid | Sr. Full-Stack DevOps Engineer | Docker deployment expertise, security tooling evaluation |

---

## 📋 Governance Compliance

| Requirement | Status |
|-------------|--------|
| #masterCCC | ✅ GTM_2026-W10_026 |
| Approval CCC-ID | ✅ GTM_2026-W11_330 |
| Version History | ✅ Included |
| Related Documents | ✅ Included (+PRJ-032, PRJ-035) |
| Discovered By (BP-047) | ✅ Included |
| Lifecycle Stage | 🔄 IN PROGRESS |
| VSA Eligibility | ✅ FULL or DEEP FULL (at APPROVED+ stage) |
| GUIDE-011 | ✅ APPROVED — compensation eligible |

---

#FlowsBros #FedArch #jAIMSnet #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
