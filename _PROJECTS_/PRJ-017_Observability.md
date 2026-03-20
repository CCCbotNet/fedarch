# PRJ-017_Observability.md

## 📋 Document Metadata

| Field | Value |
|-------|-------|
| **Document** | PRJ-017_Observability.md |
| **Version** | **v3.2.3.1** |
| **CCC-ID** | RMN_2026-W12_075 |
| **Approval CCC-ID** | GTM_2026-W10_161 (existing) |
| **Created** | 2026-02-27 (W09) |
| **Updated** | **2026-03-19 (W12)** |
| **Season** | #WeOwnSeason003 🚀 |
| **Status** | ✅ APPROVED — 🔄 DEPLOYING W12 |
| **Lifecycle Stage** | 🚀 GH LIVE |
| **#LLMmodel** | Claude Sonnet 4.6 |
| **Source of Truth** | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-017_Observability-3Layer-jAIMSnet-Stack.md) |
| **Tags** | #Observability #Langfuse #UptimeKuma #jAIMSnet #FOSS #FlowsBros #Prometheus #Grafana #Loki #Tempo #Alloy #Mimir |
| **Brand** | **jAIMSnet** (AI Management Systems network) |
| **Urgency** | 🔴 **HIGH — 6 blind incidents W06-W11, 11.5 hrs no visibility** |

---

## 📖 Table of Contents

1. [Project Identity](#-project-identity)
2. [jAIMSnet Brand Identity](#-jaimsnet-brand-identity)
3. [jAIMSnet Observability Stack — 3 Layers](#-jaimsnet-observability-stack--3-layers)
4. [Incident History](#-incident-history)
5. [Phoenix → Langfuse Decision](#-phoenix--langfuse-decision)
6. [Why Langfuse](#-why-langfuse)
7. [What Gets Traced](#-what-gets-traced)
8. [jAIMS.app Domain Family](#-jaimsapp-domain-family)
9. [LiteLLM Integration (PRJ-016)](#-litellm-integration-prj-016)
10. [Multi-Tenant Tracking (#ZeroTo100)](#-multi-tenant-tracking-zeroto100)
11. [Deployment Architecture — jAIMSnet DOKS Cluster](#-deployment-architecture--jaimsnet-doks-cluster)
12. [Phase 0 — Langfuse + Uptime Kuma (Deploying W11-W12)](#-phase-0--langfuse--uptime-kuma-deploying-w11-w12)
13. [Phase 0 — Deployment Checklist](#-phase-0--deployment-checklist)
14. [Phase 0 — K8s Manifests (jAIMSnet DOKS)](#-phase-0--k8s-manifests-jaimsnet-doks)
15. [Phase 0 — Verification (#SmokeTest)](#-phase-0--verification-smoketest)
16. [Phase 0.5 — Full LGTM + Tempo + Mimir + Alloy Stack](#-phase-05--full-lgtm--tempo--mimir--alloy-stack)
17. [Phase 0.5 — Deployment Checklist](#-phase-05--deployment-checklist)
18. [Phase 0.5 — K8s Deployment (Helm Charts)](#-phase-05--k8s-deployment-helm-charts)
19. [Phase 0.5 — Verification (#SmokeTest)](#-phase-05--verification-smoketest)
20. [Phase 1 — Local Services (GB10-1)](#-phase-1--local-services-gb10-1)
21. [Phase 2 — LiteLLM Integration](#-phase-2--litellm-integration)
22. [Phase 3 — Full Stack](#-phase-3--full-stack)
23. [OTEL Instrumentation Plan](#-otel-instrumentation-plan)
24. [Dashboard Configuration](#-dashboard-configuration)
25. [Hub + Tenant Observability Architecture](#-hub--tenant-observability-architecture)
26. [Integration with Other PRJs](#-integration-with-other-prjs)
27. [Project Team](#-project-team)
28. [MAIT Architecture — 3 MAITs](#-mait-architecture--3-maits)
29. [Risk Matrix](#-risk-matrix)
30. [Relationship to Other Projects](#-relationship-to-other-projects)
31. [Discovered By (BP-047)](#-discovered-by-bp-047)
32. [Related Documents](#-related-documents)
33. [Version History](#-version-history)

---

## 📋 Project Identity

| Field | Value |
|-------|-------|
| Project ID | **PRJ-017** |
| Title | **Observability — 3-Layer jAIMSnet Stack** |
| Type | Infrastructure — Observability |
| Priority | 🔴 P0 (Phase 0 + 0.5) / 🟠 P1 (Phase 1-3) |
| Owner | @GTM (Layers 2+3) + @RMN (Layer 1) |
| Brand | **jAIMSnet** |
| Deployment | Phase 0+0.5: jAIMSnet DOKS Cluster (ATL1) + Uptime Kuma Droplet (NYC1) / Phase 1+: GB10-1 #NoDe |
| Timeline | **Phase 0: W11-W12** / **Phase 0.5: W11-W12** / Phase 1: W12+ / Phase 2: W12 / Phase 3: W13+ |
| Depends on | Phase 0: PRJ-025 (jAIMSnet cluster) / Phase 1: PRJ-015 / Phase 2: PRJ-016 |
| Feeds into | PRJ-016 (LiteLLM OTEL → Langfuse) |
| #masterCCC | GTM_2026-W10_122 |
| Approval CCC-ID | GTM_2026-W10_161 |

---

## 📋 jAIMSnet Brand Identity

### Brand

| Field | Value |
|-------|-------|
| Brand | **jAIMSnet** |
| Meaning | j + **AIMS** (AI Management Systems) + net (network) |
| ISO Reference | **ISO/IEC 42001:2023** — AI Management Systems |
| ISO URL | [iso.org/standard/42001](https://www.iso.org/standard/42001) |
| Positioning | Open-source AI observability & management infrastructure |
| Relationship | Ecosystem brand under ♾️ WeOwnNet 🌐 |

### Digital Presence

| Asset | URL | Status |
|-------|-----|--------|
| **Primary Domain** | **[jAIMS.network](https://jAIMS.network)** | ✅ Registered |
| GitHub Org | [github.com/jAIMSnet](https://github.com/jAIMSnet) | ✅ Created |
| X (Twitter) | [x.com/jAIMSnet](https://x.com/jAIMSnet) | ✅ Created |

### All Domains (6 — Porkbun / Web3FreedomClub)

| # | Domain | Purpose |
|---|--------|---------|
| 1 | **jAIMS.network** | **Primary** — infrastructure brand |
| 2 | jAIMS.app | App/tool landing page |
| 3 | jAIMS.xyz | Alternative |
| 4 | jAIMSnet.com | Corporate redirect |
| 5 | jAIMSnet.org | Community/open-source |
| 6 | jAIMSnet.xyz | Alternative |

### ISO/IEC 42001 Alignment

| ISO 42001 Requirement | jAIMSnet Implementation |
|----------------------|------------------------|
| AI system monitoring | Langfuse traces + dashboards |
| Risk management | Observability → incident detection |
| Performance evaluation | Token cost, latency, error rates |
| Continual improvement | Data-driven optimization |
| Documentation | #FedArch governance (SharedKernel, BP, PROTO) |
| Accountability | CCC attribution system |
| **Infrastructure monitoring** | **Prometheus + Grafana + Loki + Tempo + Mimir (Layer 1)** |

### jAIMSnet × PRJ-017

| PRJ-017 Component | jAIMSnet Role |
|-------------------|---------------|
| Langfuse deployment | jAIMSnet Layer 3 (AI observability) |
| Uptime Kuma | jAIMSnet Layer 2 (endpoint monitoring) |
| **Prometheus + Grafana + Loki + Tempo + Mimir + Alloy** | **jAIMSnet Layer 1 (infrastructure)** |
| OTEL instrumentation | jAIMSnet tooling |
| Dashboards | jAIMSnet monitoring platform |
| @MAIT:#Langfuse + @MAIT:#UptimeKuma + @MAIT:#InfraObs | jAIMSnet knowledge base (3 MAITs) |

---

## 📋 jAIMSnet Observability Stack — 3 Layers

```
┌─────────────────────────────────────────────────┐
│  Layer 3: AI OBSERVABILITY                       │
│  Langfuse + OTEL                    → @GTM       │
│  "What is the AI doing?"                         │
│  @MAIT:#Langfuse                                 │
│  Deployment: jAIMSnet DOKS (ATL1)                │
├─────────────────────────────────────────────────┤
│  Layer 2: ENDPOINT MONITORING                    │
│  Uptime Kuma                        → @GTM       │
│  "Is it reachable?"                              │
│  @MAIT:#UptimeKuma                               │
│  Deployment: Standalone Droplet (NYC1)           │
├─────────────────────────────────────────────────┤
│  Layer 1: INFRASTRUCTURE                         │
│  Prometheus + Grafana + Loki        → @RMN       │
│  + Tempo + Mimir + Alloy                         │
│  "What is the machine doing?"                    │
│  @MAIT:#InfraObs                                 │
│  Deployment: jAIMSnet DOKS (ATL1)                │
│             → Phase 1: GB10-1 #NoDe             │
└─────────────────────────────────────────────────┘
```

| Layer | Name | Tools | Owner | Answers |
|-------|------|-------|-------|---------|
| **3** | AI Observability | Langfuse + OTEL | @GTM | "What is the AI doing?" |
| **2** | Endpoint Monitoring | Uptime Kuma | @GTM | "Is it reachable?" |
| **1** | Infrastructure | Prometheus + Grafana + Loki + Tempo + Mimir + Alloy | @RMN | "What is the machine doing?" |

### Why 3 Layers

| Question | Layer 3 (Langfuse) | Layer 2 (Kuma) | Layer 1 (LGTM+Tempo+Mimir) |
|----------|------------------|----------------|---------------------------|
| LLM call latency is high — why? | ✅ Shows latency | ❌ | ✅ Shows CPU/GPU pressure |
| Website is down — why? | ❌ | ✅ Shows down | ✅ Shows container crash |
| Tokens cost spiked — why? | ✅ Shows per-request cost | ❌ | ❌ |
| Disk is full — what happens? | ❌ | ❌ | ✅ Shows disk pressure |
| Container OOM killed — what? | ❌ | ✅ Shows endpoint gone | ✅ Shows memory + restart |
| Need to search logs | ❌ | ❌ | ✅ Loki log search |
| Trace a request end-to-end | ❌ | ❌ | ✅ Tempo distributed tracing |
| Long-term metrics retention | ❌ | ❌ | ✅ Mimir scalable storage |

> **No single layer answers all questions. All 3 together = complete observability.**

---

## 📋 Incident History

| # | When | Duration | Root Cause | Detection | Layer That Catches It |
|---|------|----------|-----------|-----------|----------------------|
| 1 | W08 | 2h 18m | API key expired | User report (blind) | Layer 3 (Langfuse) |
| 2 | W06 | ~67 min | Embedder reverted | User report (blind) | Layer 2 (Kuma) + Layer 3 |
| 3 | W09 Tue | ~6.5 hrs | API key expired | @LDC report (blind) | Layer 3 (Langfuse) |
| 4 | W09 Sun AM | ~18 min | API key restart | @GTM manual (blind) | Layer 3 (Langfuse) |
| 5 | W09 Sun PM | ~9 min | API key lost | @GTM manual (blind) | Layer 3 + Layer 2 |
| 6 | W10 Mon | ~2h | INT-P01 OOM + Infisical broken | Manual debugging | Layer 1 + Layer 3 |
| **TOTAL** | | **~11.5 hrs** | **All blind** | **All human-detected** | **All preventable** |

> **11.5 hours of cumulative downtime. All blind. All same pattern. All preventable with observability.**

---

## 📋 Phoenix → Langfuse Decision

### Decision Record

| Field | Value |
|-------|-------|
| Decision | **Langfuse replaces Phoenix as Layer 3** |
| Decided by | @GTM + @RMN consensus |
| @RMN analysis | RMN_2026-W10_043 |
| Approved | GTM_2026-W10_161 |
| Sunk cost | **$0** — Phoenix never deployed |

### Comparison

| Factor | Phoenix (ELv2) | Langfuse (MIT) | Winner |
|--------|---------------|----------------|--------|
| **License** | ❌ ELv2 (NOT OSI-approved) | ✅ **MIT** (OSI-approved) | **Langfuse** 🏆 |
| **Priority #2 (FOSS)** | ⚠️ Questionable | ✅ **Aligned** | **Langfuse** 🏆 |
| **LiteLLM integration** | 🟡 Manual OTEL config | ✅ **Native callback (5 min)** | **Langfuse** 🏆 |
| **Multi-tenant** | 🟡 Manual tagging | ✅ **Automatic projects** | **Langfuse** 🏆 |
| **Self-hosted** | ✅ Docker | ✅ Docker + K8s | Langfuse 🏆 |
| **Score** | 3.5/10 | **9.5/10** | **Langfuse** 🏆 |
| **@RMN recommends** | ❌ | ✅ | **Langfuse** 🏆 |

### Learning

| ID | Learning |
|----|----------|
| L-129 | ELv2 (Elastic License v2) is NOT OSI-approved — conflicts with Priority #2 (FOSS); ecosystem MUST prefer OSI-approved licenses (MIT, Apache 2.0, AGPL) over source-available licenses (ELv2, BSL, SSPL) when FOSS alternatives exist |

---

## 📋 Why Langfuse

| Factor | Value |
|--------|-------|
| **License** | ✅ MIT (OSI-approved FOSS) |
| **Stars** | 10K+ GitHub stars |
| **LiteLLM Native** | `success_callback: ["langfuse"]` — zero extra config |
| **Multi-tenant** | Automatic project-based isolation |
| **Self-hosted** | Full control, full prompt logging |
| **Auto cost tracking** | Per-request cost visible immediately |
| **OTEL compatible** | Standard OTEL SDK support |
| **K8s native** | Helm chart available, DOKS compatible |

---

## 📋 What Gets Traced

| Trace Type | Source | #FedArch Value |
|-----------|--------|---------------|
| **LLM calls** | AnythingLLM → LLM provider | Token usage, cost, latency per request |
| **Embedding ops** | AnythingLLM → Qwen3 4B | Embedding latency, batch sizes |
| **RAG retrieval** | AnythingLLM vector search | Retrieval relevance, doc chunks returned |
| **Tool calls** | MAIT thread interactions | MAIT response quality |
| **Agent spans** | Parent → child request chains | #ContextVolley flow visualization |
| **Cache events** | LiteLLM Redis (PRJ-016) | Hit/miss rate, savings |
| **Failover events** | LiteLLM provider switching | OpenRouter → vLLM transitions |
| **Errors** | Any failure in pipeline | Root cause analysis |

---

## 📋 jAIMS.app Domain Family

| Subdomain | Service | Layer | Status |
|-----------|---------|-------|--------|
| **langfuse.jAIMS.app** | **Langfuse** | Layer 3 (LLM) | 🔄 Deploying |
| **kuma.jAIMS.app** | Uptime Kuma (NYC1) | Layer 2 (Endpoints) | ✅ LIVE |
| **grafana.jAIMS.app** | Grafana | Layer 1 (Metrics) | 📋 Phase 0.5 |
| **litellm.jAIMS.app** | LiteLLM (PRJ-016) | Gateway | 🔄 Deploying |
| **pgadmin.jAIMS.app** | pgAdmin (PRJ-021) | Database UI | 📋 Planned |

---

## 📋 LiteLLM Integration (PRJ-016)

### How LiteLLM Feeds Langfuse

```
ALL INSTANCES → LiteLLM (PRJ-016) [gateway namespace, jAIMSnet DOKS]
                    │
                    ├── Routes to: MI300X/MI325X / OpenRouter / GB10
                    │
                    └── success_callback: ["langfuse"]
                        │
                        └── langfuse.jAIMS.app receives:
                            ├── Every LLM call (automatic)
                            ├── Model, tokens, cost, latency
                            ├── Instance + user metadata
                            └── Full prompt/response (self-hosted)
```

### LiteLLM Configuration

```yaml
litellm_settings:
  success_callback: ["langfuse"]

environment_variables:
  LANGFUSE_PUBLIC_KEY: "pk-lf-..."
  LANGFUSE_SECRET_KEY: "sk-lf-..."
  LANGFUSE_HOST: "https://langfuse.jAIMS.app"
```

> **5 minutes.** Add 3 environment variables to LiteLLM. Every LLM call across every instance = automatically traced.

---

## 📋 Multi-Tenant Tracking (#ZeroTo100)

### Langfuse Multi-Tenant Architecture

```
Langfuse Projects:
├── weownnet-governance    ← INT-P01 traces
├── burnedout-media        ← INT-P02 traces
├── pop-database           ← INT-P03 traces
├── agencypro-production   ← INT-P05 traces
│   ├── customer-001       ← Per AgencyPRO customer
│   └── ... (scale to 40-100 customers)
├── seasonal-shared        ← INT-S003 traces
├── home-gtm               ← INT-OG1 traces
└── home-rmn               ← INT-OG8 traces
```

---

## 📋 Deployment Architecture — jAIMSnet DOKS Cluster

### Updated Architecture (W11-W12)

> **⚠️ KEY CHANGE FROM v3.2.1.1:** jAIMSnet is deployed on a DOKS cluster (not Docker Droplets), with the sole exception of Uptime Kuma which runs on a standalone Droplet in NYC1 for geographic resilience.

```
Internet → DO Load Balancer (129.212.240.75 · ATL1)
  → ingress-nginx (jAIMSnet DOKS cluster · ATL1)
    → litellm.jAIMS.app  → LiteLLM   (gateway namespace)
    → langfuse.jAIMS.app → Langfuse  (observability namespace)
    → pgadmin.jAIMS.app  → pgAdmin   (observability namespace)
    → grafana.jAIMS.app  → Grafana   (observability namespace) [Phase 0.5]
    → cert-manager (auto-TLS via Let's Encrypt)

LiteLLM → Redis               (gateway/redis)
LiteLLM → Langfuse            (success_callback: ["langfuse"])
LiteLLM → OpenRouter / vLLM   (providers)
LiteLLM → PostgreSQL          (spend tracking · PRJ-021)
Langfuse → PostgreSQL         (traces + evals · PRJ-021)
Infisical Cloud → Infisical Operator → K8s Secrets → Pods (PRJ-024)

Uptime Kuma (STANDALONE DROPLET · NYC1 · ~$6/mo — separate for resilience)
  → monitors: litellm.jAIMS.app, langfuse.jAIMS.app, pgadmin.jAIMS.app,
              INT-P01, INT-OG1, INT-OG8, INT-P02, PostgreSQL cluster

[Phase 0.5] Prometheus + Grafana + Loki + Tempo + Mimir + Alloy
            (observability namespace · jAIMSnet DOKS · ATL1)

[Phase 2] vLLM on MI300X/MI325X GPU Droplet (VPC · ATL1) → LiteLLM backend
```

### Why Uptime Kuma Is Separate (NYC1)

| Reason | Detail |
|--------|--------|
| **Resilience** | If ATL1 cluster fails, Kuma still monitors and alerts |
| **Independence** | Kuma monitors cluster health externally |
| **Geographic Diversity** | NYC1 provides geographic diversity from ATL1 |
| **Cost** | ~$6/mo Basic Droplet vs cluster resources |
| **Simplicity** | Docker Compose (single container) vs K8s complexity |

---

## 📋 Phase 0 — Langfuse + Uptime Kuma (Deploying W11-W12)

### Phase 0 Scope

| # | What to Observe | Source | Method |
|---|----------------|--------|--------|
| 1 | **LLM calls** (all instances) | AnythingLLM → LiteLLM | LiteLLM callback → Langfuse |
| 2 | **Token cost per instance** | OTEL metadata | Langfuse dashboard |
| 3 | **Request latency** | OTEL spans | Langfuse dashboard |
| 4 | **Cache effectiveness** | LiteLLM Redis | Langfuse traces |
| 5 | **Error rates** | OTEL traces | Langfuse alerting |
| 6 | **Endpoint uptime** | All domains | Uptime Kuma (NYC1) |
| 7 | **SSL certificate expiry** | All domains | Uptime Kuma (NYC1) |
| 8 | **PostgreSQL connectivity** | DO Managed DB | Uptime Kuma (NYC1) |

### 7 Uptime Kuma Monitors (NYC1 Droplet)

| # | Endpoint | Type | Interval | Priority |
|---|----------|------|----------|----------|
| 1 | litellm.jAIMS.app | HTTP(s) | 1 min | 🔴 P0 |
| 2 | langfuse.jAIMS.app | HTTP(s) | 1 min | 🔴 P0 |
| 3 | pgadmin.jAIMS.app | HTTP(s) | 5 min | 🟠 P1 |
| 4 | INT-P01 (AI.WeOwn.Agency) | HTTP(s) | 1 min | 🔴 P0 |
| 5 | INT-OG1 (AI.YonksTEAM.xyz) | HTTP(s) | 5 min | 🟠 P1 |
| 6 | INT-OG8 (AI.RomanDiD.xyz) | HTTP(s) | 5 min | 🟠 P1 |
| 7 | PostgreSQL Cluster | TCP Port (25060) | 1 min | 🔴 P0 |

---

## 📋 Phase 0 — Deployment Checklist

| # | Step | Owner | Status |
|---|------|-------|--------|
| 1 | Deploy Langfuse to jAIMSnet DOKS (observability namespace) | @RMN | ⬜ |
| 2 | Configure Langfuse K8s Ingress (langfuse.jAIMS.app, cert-manager) | @RMN | ⬜ |
| 3 | Connect Langfuse to PostgreSQL (PRJ-021) | @RMN | ⬜ |
| 4 | Store Langfuse credentials in Infisical (PRJ-024) | @RMN | ⬜ |
| 5 | Create Langfuse API keys (per instance) | @RMN | ⬜ |
| 6 | Create Langfuse projects (per instance) | @RMN | ⬜ |
| 7 | Deploy Uptime Kuma on NYC1 Droplet (Docker Compose) | @GTM | ✅ LIVE |
| 8 | Configure DNS (kuma.jAIMS.app → NYC1 Droplet) | @GTM | ✅ LIVE |
| 9 | Configure 7 Uptime Kuma monitors | @GTM | ⬜ |
| 10 | Add Langfuse callback to LiteLLM (3 env vars) | @RMN | ⬜ |
| 11 | Send test LLM call → verify trace in Langfuse | @GTM | ⬜ |
| 12 | Phase 0 #SmokeTest (8-point) | @GTM | ⬜ |
| 13 | FULL:SYNC:META | @GTM | ⬜ |

---

## 📋 Phase 0 — K8s Manifests (jAIMSnet DOKS)

### Langfuse Deployment + Ingress

```yaml
# observability/langfuse-deployment.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: langfuse
  namespace: observability
  labels:
    app: langfuse
    jaimsnet.component: observability
spec:
  replicas: 1
  selector:
    matchLabels:
      app: langfuse
  template:
    metadata:
      labels:
        app: langfuse
    spec:
      containers:
      - name: langfuse
        image: langfuse/langfuse:latest
        ports:
        - containerPort: 3000
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: langfuse-db-secret
              key: url
        - name: NEXTAUTH_SECRET
          valueFrom:
            secretKeyRef:
              name: langfuse-secret
              key: nextauth-secret
        - name: NEXTAUTH_URL
          value: "https://langfuse.jAIMS.app"
        - name: SALT
          valueFrom:
            secretKeyRef:
              name: langfuse-secret
              key: salt
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: langfuse-ingress
  namespace: observability
  annotations:
    cert-manager.io/cluster-issuer: "jaimsnet-cluster-issuer"
spec:
  rules:
  - host: langfuse.jAIMS.app
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: langfuse-service
            port:
              number: 3000
```

### Uptime Kuma Docker Compose (NYC1 Standalone Droplet)

```yaml
# docker-compose.yml — Uptime Kuma (NYC1 Droplet)
version: '3.8'

services:
  uptime-kuma:
    image: louislam/uptime-kuma:1
    container_name: uptime-kuma
    restart: unless-stopped
    ports:
      - "3001:3001"
    volumes:
      - kuma-data:/app/data

volumes:
  kuma-data:
```

---

## 📋 Phase 0 — Verification (#SmokeTest)

### Phase 0 #SmokeTest (8-Point)

| # | Test | Expected | Status |
|---|------|----------|--------|
| 1 | Langfuse UI accessible | https://langfuse.jAIMS.app → login | ⬜ |
| 2 | LLM call trace | Make call via LiteLLM → trace in Langfuse | ⬜ |
| 3 | Cost visible | Trace shows $ amount | ⬜ |
| 4 | Latency visible | Trace shows ms | ⬜ |
| 5 | Prompt logged | Full prompt visible (self-hosted) | ⬜ |
| 6 | Multi-project | Separate projects per instance | ⬜ |
| 7 | Uptime Kuma running | https://kuma.jAIMS.app → dashboard | ✅ |
| 8 | Uptime Kuma monitors | All 7 endpoints green | ⬜ |

---

## 📋 Phase 0.5 — Full LGTM + Tempo + Mimir + Alloy Stack

### Why This Stack?

> **Note:** Final tool confirmation depends on jAIMSnet roadmap research (PRJ-025 Tracks 4-5). However, Prometheus + Grafana + Loki + Tempo + Mimir + Alloy is the highly likely stack based on research to date. May be refined after PRJ-025 research is complete.

| Factor | Value |
|--------|-------|
| **Stack** | Prometheus + Grafana + Loki + Tempo + Mimir + Alloy |
| **Ecosystem** | All Grafana Labs FOSS tools — native integration |
| **License** | All AGPL 3.0 / Apache 2.0 (FOSS) |
| **K8s Native** | All designed for Kubernetes, Helm charts available |
| **Status** | Highly likely (subject to PRJ-025 final research) |

### LGTM+ Stack Components

| Component | Tool | Purpose | Namespace | Port | License |
|-----------|------|---------|-----------|------|---------|
| **Metrics Collection** | Prometheus | Scrape metrics from nodes, pods, services | observability | 9090 | Apache 2.0 |
| **Log Aggregation** | Loki | Collect and query logs | observability | 3100 | AGPL 3.0 |
| **Distributed Tracing** | Tempo | Collect and query distributed traces | observability | 3200 | AGPL 3.0 |
| **Log/Metric/Trace Collection** | Alloy | Ship logs, metrics, traces to Loki/Prom/Tempo | observability | — | Apache 2.0 |
| **Long-term Metrics** | Mimir | Scalable, long-term Prometheus-compatible storage | observability | 9009 | AGPL 3.0 |
| **Visualization** | Grafana | Dashboards for ALL observability signals | observability | 3000 | AGPL 3.0 |

### Why Each Component

| Component | Why |
|-----------|-----|
| **Prometheus** | Industry standard, K8s native, extensive ecosystem |
| **Loki** | Lightweight, K8s native, tight Grafana integration, FOSS |
| **Tempo** | FOSS distributed tracing, integrates natively with Grafana + Loki, compatible with OTEL |
| **Alloy** | Grafana's next-gen collector (replaces Promtail/Grafana Agent), handles logs + metrics + traces in one agent |
| **Mimir** | Horizontal scaling for Prometheus metrics, long-term retention, multi-tenant |
| **Grafana** | Single pane of glass for Prometheus + Loki + Tempo + Mimir |

### What Langfuse sees vs LGTM+ stack

| Question | Langfuse (Layer 3) | LGTM+ (Layer 1) |
|----------|-------------------|-----------------|
| LLM call latency — why? | ✅ Shows latency per request | ✅ Shows CPU/GPU pressure causing it |
| Token cost | ✅ Per-request cost | ❌ |
| Container OOM killed | ❌ | ✅ Shows memory + restart |
| Log search | ❌ | ✅ Loki full-text log search |
| Distributed trace (infra level) | ❌ | ✅ Tempo end-to-end infra trace |
| Long-term metrics trends | ❌ | ✅ Mimir 1yr+ retention |
| Disk/CPU/Memory | ❌ | ✅ Prometheus + node_exporter |

### Resource Requirements (LGTM+ Stack)

| Component | CPU Request | Memory Request | Storage |
|-----------|:-----------:|:--------------:|:-------:|
| Prometheus | 500m | 1Gi | 50Gi |
| Grafana | 100m | 256Mi | 10Gi |
| Loki | 500m | 1Gi | 100Gi |
| Tempo | 500m | 1Gi | 100Gi |
| Mimir | 500m | 1Gi | 200Gi |
| Alloy | 100m | 256Mi | — |
| **TOTAL** | **~2.2 CPU** | **~4.5 Gi** | **~460 Gi** |

---

## 📋 Phase 0.5 — Deployment Checklist

| # | Step | Owner | Status |
|---|------|-------|--------|
| 1 | Create observability namespace (if not exists) | @RMN | ⬜ |
| 2 | Add Helm repos (Prometheus, Grafana, Loki, Tempo, Mimir, Alloy) | @RMN | ⬜ |
| 3 | Deploy kube-prometheus-stack (Prometheus + Grafana) | @RMN | ⬜ |
| 4 | Deploy Loki (log aggregation) | @RMN | ⬜ |
| 5 | Deploy Tempo (distributed tracing) | @RMN | ⬜ |
| 6 | Deploy Mimir (long-term metrics) | @RMN | ⬜ |
| 7 | Deploy Alloy (log + metric + trace collection agent) | @RMN | ⬜ |
| 8 | Configure Grafana datasources (Prometheus, Loki, Tempo, Mimir) | @RMN | ⬜ |
| 9 | Import Grafana dashboards (node, K8s, containers) | @RMN | ⬜ |
| 10 | Configure Grafana Ingress (grafana.jAIMS.app) | @RMN | ⬜ |
| 11 | Deploy node_exporter DaemonSet (host metrics) | @RMN | ⬜ |
| 12 | Deploy kube-state-metrics (K8s object metrics) | @RMN | ⬜ |
| 13 | Phase 0.5 #SmokeTest (10-point) | @RMN | ⬜ |
| 14 | FULL:SYNC:META | @RMN | ⬜ |

---

## 📋 Phase 0.5 — K8s Deployment (Helm Charts)

```bash
# 1. Add all Helm repos
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update

# 2. Deploy kube-prometheus-stack (Prometheus + Grafana + Alertmanager)
helm install kube-prometheus prometheus-community/kube-prometheus-stack \
  --namespace observability \
  --set prometheus.prometheusSpec.resources.requests.memory=1Gi \
  --set grafana.adminPassword=${GRAFANA_ADMIN_PASSWORD} \
  --set grafana.ingress.enabled=true \
  --set grafana.ingress.hosts[0]=grafana.jAIMS.app \
  --set grafana.ingress.annotations."cert-manager\.io/cluster-issuer"=jaimsnet-cluster-issuer

# 3. Deploy Loki
helm install loki grafana/loki \
  --namespace observability \
  --set loki.storage.type=filesystem \
  --set loki.persistence.enabled=true \
  --set loki.persistence.size=100Gi

# 4. Deploy Tempo
helm install tempo grafana/tempo \
  --namespace observability \
  --set tempo.storage.trace.backend=local \
  --set persistence.enabled=true \
  --set persistence.size=100Gi

# 5. Deploy Mimir
helm install mimir grafana/mimir-distributed \
  --namespace observability \
  --set mimir.structuredConfig.common.storage.backend=filesystem

# 6. Deploy Alloy (unified collector)
helm install alloy grafana/alloy \
  --namespace observability \
  --set alloy.configMap.content="$(cat alloy-config.yaml)"
```

### Alloy Configuration (logs + metrics + traces)

```yaml
# alloy-config.yaml — Collects logs, metrics, and traces

// Collect logs from all pods
loki.source.kubernetes "pods" {
  targets    = discovery.kubernetes.pods.targets
  forward_to = [loki.write.default.receiver]
}

loki.write "default" {
  endpoint {
    url = "http://loki:3100/loki/api/v1/push"
  }
}

// Collect metrics
prometheus.scrape "pods" {
  targets    = discovery.kubernetes.pods.targets
  forward_to = [prometheus.remote_write.mimir.receiver]
}

prometheus.remote_write "mimir" {
  endpoint {
    url = "http://mimir:9009/api/v1/push"
  }
}

// Receive OTEL traces and forward to Tempo
otelcol.receiver.otlp "default" {
  grpc { endpoint = "0.0.0.0:4317" }
  http { endpoint = "0.0.0.0:4318" }
  output {
    traces = [otelcol.exporter.otlp.tempo.input]
  }
}

otelcol.exporter.otlp "tempo" {
  client {
    endpoint = "tempo:4317"
  }
}
```

---

## 📋 Phase 0.5 — Verification (#SmokeTest)

### Phase 0.5 #SmokeTest (10-Point)

| # | Test | Expected | Status |
|---|------|----------|--------|
| 1 | Prometheus running | http://prometheus:9090 → UI | ⬜ |
| 2 | Grafana accessible | https://grafana.jAIMS.app → login | ⬜ |
| 3 | Prometheus datasource | Grafana → Prometheus → Test → ✅ | ⬜ |
| 4 | Loki datasource | Grafana → Loki → Test → ✅ | ⬜ |
| 5 | Tempo datasource | Grafana → Tempo → Test → ✅ | ⬜ |
| 6 | Mimir datasource | Grafana → Mimir → Test → ✅ | ⬜ |
| 7 | Node metrics visible | CPU, memory, disk, network in dashboard | ⬜ |
| 8 | K8s pod metrics visible | Container health, restarts in dashboard | ⬜ |
| 9 | Log search | Grafana → Explore → Loki → query returns logs | ⬜ |
| 10 | Persistence | Restart all → data retained | ⬜ |

---

## 📋 Phase 1 — Local Services (GB10-1)

### Timeline: W12+ (After PRJ-015)

| Service | Instrumentation | Method |
|---------|----------------|--------|
| **AnythingLLM (local)** | LLM calls + RAG retrieval | OTEL Python SDK or langfuse.otel |
| **Ollama** | Inference calls | OTEL wrapper |

### Migration Plan (DOKS → GB10-1)

| Step | Action | Timeline | Downtime |
|------|--------|----------|----------|
| 1 | Deploy LGTM+ stack on GB10-1 | W12 | 0 min |
| 2 | Test GB10-1 observability locally | W12 | 0 min |
| 3 | Export Langfuse data (PostgreSQL) | W12 | 0 min |
| 4 | Update DNS (langfuse.jAIMS.app → GB10-1) | W12 | ~5 min |
| 5 | Add nvidia_exporter for GPU monitoring | W12 | 0 min |
| 6 | Scale down/remove from jAIMSnet DOKS (optional) | W13 | 0 min |

### Deployment Checklist (Phase 1)

| # | Step | Owner | Status |
|---|------|-------|--------|
| 1 | GB10-1 #NoDe operational (PRJ-015) | @GTM | ⬜ |
| 2 | Deploy LGTM+ stack on GB10-1 (Docker Compose) | @RMN | ⬜ |
| 3 | Add nvidia_exporter for GPU monitoring | @RMN | ⬜ |
| 4 | Migrate Langfuse from DOKS to GB10-1 | @GTM | ⬜ |
| 5 | Migrate Uptime Kuma from NYC1 to GB10-1 (optional) | @GTM | ⬜ |
| 6 | Install OTEL SDK on AnythingLLM (local) | @RMN | ⬜ |
| 7 | Send test trace → verify in Langfuse | @GTM | ⬜ |
| 8 | Instrument Ollama calls | @RMN | ⬜ |

---

## 📋 Phase 2 — LiteLLM Integration

### Timeline: W12 (After PRJ-016)

```yaml
# In LiteLLM config.yaml (3 env vars — 5 min setup)
litellm_settings:
  success_callback: ["langfuse"]

environment_variables:
  LANGFUSE_PUBLIC_KEY: "pk-lf-..."
  LANGFUSE_SECRET_KEY: "sk-lf-..."
  LANGFUSE_HOST: "https://langfuse.jAIMS.app"
```

> **When PRJ-016 deploys, ALL LLM traffic automatically traces to Langfuse.** Zero additional instrumentation needed per instance.

### What Langfuse Receives (Automatic from LiteLLM)

| Data Point | Automatic? | Detail |
|-----------|:----------:|--------|
| Model requested + used | ✅ | `smart` alias → actual model |
| Provider | ✅ | OpenRouter, Anthropic, vLLM, etc. |
| Input/output | ✅ | Full prompt + response |
| Tokens (in/out/total) | ✅ | Token counts |
| Cost (calculated) | ✅ | Per-request cost |
| Latency (total + TTFT) | ✅ | Response time |
| Cache hit/miss | ✅ | Redis cache status |
| API key + team ID | ✅ | Per-instance tracking |
| Success/failure | ✅ | Error messages |
| Fallback used | ✅ | Which backend was used |

---

## 📋 Phase 3 — Full Stack

### Timeline: W13+

| Service | Instrumentation | Method |
|---------|----------------|--------|
| **INT-P01, INT-S003, etc.** | LLM calls via LiteLLM | Automatic (LiteLLM traces all) |

---

## 📋 OTEL Instrumentation Plan

### OTEL Configuration (Direct — Phase 0/1)

```python
# For direct AnythingLLM instrumentation
from langfuse.otel import register
from openinference.instrumentation.openai import OpenAIInstrumentor

tracer_provider = register(
    endpoint="https://langfuse.jAIMS.app/v1/traces",
    project_name="fedarch"
)

OpenAIInstrumentor().instrument(tracer_provider=tracer_provider)
```

### OTEL Configuration (LiteLLM — Phase 2)

```yaml
# In LiteLLM config.yaml
litellm_settings:
  success_callback: ["langfuse"]

environment_variables:
  LANGFUSE_PUBLIC_KEY: "pk-lf-..."
  LANGFUSE_SECRET_KEY: "sk-lf-..."
  LANGFUSE_HOST: "https://langfuse.jAIMS.app"
```

---

## 📋 Dashboard Configuration

### Layer 3 — Langfuse Dashboards

| Dashboard | Metrics | Purpose |
|-----------|---------|---------|
| **Traces** | Request waterfall, spans, latency | Debug individual requests |
| **LLM Calls** | Model, tokens in/out, cost, latency | Usage patterns |
| **Cost by Instance** | Tokens × cost per instance | Budget tracking |
| **Model Distribution** | % Claude vs % Llama vs % Qwen3 | Hybrid balance |
| **Cache Effectiveness** | Hit/miss rate (via LiteLLM Redis) | Savings validation |
| **Error Rate** | Errors by provider, model, instance | Health monitoring |

### Layer 1 — Grafana Dashboards (LGTM+ Stack)

| Dashboard | ID | Metrics | Purpose |
|-----------|:--:|---------|---------|
| **Node Exporter Full** | 1860 | CPU, memory, disk, network | Host-level metrics |
| **Kubernetes Cluster** | 6417 | Cluster-wide pods, nodes, namespaces | K8s overview |
| **Kubernetes Pods** | 6336 | Per-pod CPU, memory, network | Pod health |
| **Loki Stats** | 13407 | Loki health, log volume | Log system health |
| **Tempo** | Built-in | Distributed traces (infra level) | Infra trace analysis |
| **Mimir** | Built-in | Long-term metrics | Trend analysis |
| **Custom: WeOwnNet Instances** | TBD | INT-P01, INT-OG1, INT-OG8, INT-P02 health | Instance monitoring |
| **Custom: jAIMSnet Services** | TBD | LiteLLM, Langfuse, Redis health | Service monitoring |
| **GPU Monitoring** | TBD | GPU utilization, temperature, memory | GB10-1 + MI300X health |

---

## 📋 Hub + Tenant Observability Architecture

> **Note:** This section reflects the planned architecture for jAIMSnet Hub + Tenant model (from PRJ-025). Final tenant observability details TBD after PRJ-025 research Tracks 5 and 3 are complete.

### Hub Observability (jAIMSnet DOKS — ATL1)

| Component | Location | Status |
|-----------|----------|--------|
| Prometheus (hub) | jAIMSnet DOKS observability namespace | 📋 Phase 0.5 |
| Grafana (hub) | jAIMSnet DOKS observability namespace | 📋 Phase 0.5 |
| Loki (hub) | jAIMSnet DOKS observability namespace | 📋 Phase 0.5 |
| Tempo (hub) | jAIMSnet DOKS observability namespace | 📋 Phase 0.5 |
| Mimir (hub) | jAIMSnet DOKS observability namespace | 📋 Phase 0.5 |
| Langfuse (hub) | jAIMSnet DOKS observability namespace | 📋 Phase 0 |
| Uptime Kuma | NYC1 Standalone Droplet | ✅ LIVE |

### Tenant Spoke Agents (Preliminary — TBD after PRJ-025 Track 3+5)

| Tenant Type | Observability Agent | Sends Data To | Status |
|-------------|--------------------|-|--------|
| **DOKS Cluster tenants** | Alloy DaemonSet (inside cluster) | Hub Loki + Mimir + Tempo | 📋 TBD after PRJ-025 |
| **Docker Droplet tenants** | Alloy (Docker container) | Hub Loki + Mimir + Tempo | 📋 TBD after PRJ-025 |

---

## 📋 Integration with Other PRJs

| PRJ | Title | Integration Point |
|-----|-------|-------------------|
| **PRJ-015** | HybridArchitecture (GB10 + MI300X) | Phase 1 migration to GB10-1, nvidia_exporter for GPU monitoring |
| **PRJ-016** | LiteLLM AI Gateway | Langfuse native callback, cost tracking, per-instance budgets |
| **PRJ-018** | P.O.P. Database | PostgreSQL cluster shared (db-postgresql-atl1-weownnet) |
| **PRJ-020** | Interns Co-op Pipeline | PostgreSQL cluster shared, monitoring |
| **PRJ-021** | PostgreSQL Operations | PostgreSQL cluster owner, Trusted Sources |
| **PRJ-024** | Secrets Management (Infisical) | Langfuse + Grafana credentials in Infisical Operator |
| **PRJ-025** | jAIMSnet Platform Engineering | Observability deployed IN jAIMSnet DOKS cluster |
| **PRJ-026** | Cybersecurity Frameworks + ISMS | Security monitoring, audit logging (Loki, Grafana SIEM) |

---

## 📋 Project Team

| CCC | Role | Layers | Focus |
|-----|------|--------|-------|
| **GTM** | **Owner** | Layer 3 + Layer 2 | Langfuse, Uptime Kuma, Phase 0, dashboards, @MAIT |
| **RMN** | **Platform + Infra Observability** | **Layer 1** | **Prometheus, Grafana, Loki, Tempo, Mimir, Alloy, OTEL instrumentation, Phase 0.5** |

---

## 📋 MAIT Architecture — 3 MAITs

### @MAIT:#Langfuse

| Field | Value |
|-------|-------|
| Thread | MAIT_Langfuse |
| ShortCode | @MAIT:#Langfuse |
| Steward | @GTM |
| Instance | INT-P01 |
| Scope | Langfuse LLM observability + LiteLLM callback integration |

### @MAIT:#UptimeKuma

| Field | Value |
|-------|-------|
| Thread | MAIT_UptimeKuma |
| UUID | 002676d5-66f8-42fb-aee8-a89f67c63fb3 |
| ShortCode | @MAIT:#UptimeKuma |
| Steward | @GTM |
| Instance | INT-P01 |
| Scope | Uptime Kuma endpoint monitoring + SSL + DNS health |

### @MAIT:#InfraObs

| Field | Value |
|-------|-------|
| Thread | MAIT_InfraObs |
| ShortCode | @MAIT:#InfraObs |
| Steward | **@RMN** |
| Instance | INT-P01 |
| Scope | Prometheus + Grafana + Loki + Tempo + Mimir + Alloy |

---

## 📋 Risk Matrix

| # | Risk | Prob | Impact | Mitigation |
|---|------|------|--------|------------|
| 1 | GB10-1 not ready (PRJ-015) | Medium | High | **Phase 0 + 0.5 on jAIMSnet DOKS covers interim** |
| 2 | OTEL instrumentation complexity | Low | Medium | Langfuse provides helper library (langfuse.otel) |
| 3 | Storage growth (traces/logs) | Low | Low | Configurable retention per component |
| 4 | LGTM+ stack resource usage | Medium | Medium | DOKS autoscale covers Phase 0.5; GB10-1 covers Phase 1 |
| 5 | Langfuse project abandoned | Low | Low | MIT = fork-friendly |
| 6 | PRJ-025 research changes tool selection | Low | Medium | Stack is highly likely but subject to final research |
| 7 | Uptime Kuma NYC1 Droplet failure | Low | Medium | NYC1 provides geographic independence from ATL1 |
| 8 | **@RMN availability for Layer 1** | Low | Medium | Phase 0 (Layer 2+3) deploys independently; Layer 1 = parallel track |

---

## 📋 Relationship to Other Projects

| PRJ | Relationship |
|-----|-------------|
| **PRJ-014** | INT-P01 + INT-S003 traffic observed by Langfuse |
| **PRJ-015** | All observability migrates TO GB10-1 #NoDe (Phase 1 — hardware dependency) |
| **PRJ-016** | LiteLLM sends OTEL traces TO Langfuse (Phase 2 — Langfuse = endpoint) |
| **PRJ-018** | P.O.P. PostgreSQL monitored by Uptime Kuma |
| **PRJ-025** | jAIMSnet DOKS cluster = home for Phase 0 + 0.5 observability |

---

## 📋 Discovered By (BP-047)

| CCC | Contributor | Role | Context |
|-----|-------------|------|---------|
| GTM | Jason Younker | Co-Founder | ADK Observability Ecosystem analysis — Phoenix selected W09; Phase 0 driven by 5 blind incidents W06-W09; Langfuse final approval (GTM_2026-W10_161) |
| RMN | Roman Di Domizio | AI Platform Engineer | Identified missing Layer 1 (infrastructure observability) — W09; Langfuse recommendation (RMN_2026-W10_043) — MIT license + native LiteLLM callback; jAIMSnet DOKS architecture for observability deployment; LGTM + Tempo + Mimir + Alloy stack design |
| LDC | Dhruv | Agentic AI Engineer | Feedback on observability requirements, AI-specific monitoring |

---

## 📋 Related Documents

| Document | Version | #masterCCC | Approval | Location |
|----------|---------|------------|----------|----------|
| PRJ-015_HybridArchitecture.md | 3.2.3.1 | GTM_2026-W10_122 | GTM_2026-W10_125 | _PROJECTS_/ (GH LIVE) |
| PRJ-016_AIGateway-LiteLLM.md | 3.2.3.1 | GTM_2026-W09_117 | GTM_2026-W09_119 | _PROJECTS_/ (GH LIVE) |
| PRJ-018_POP-Database.md | 3.2.3.1 | GTM_2026-W10_026 | GTM_2026-W11_308 | _PROJECTS_/ |
| PRJ-021_PostgreSQL-Operations.md | 3.2.3.1 | GTM_2026-W10_026 | GTM_2026-W10_026 | _PROJECTS_/ |
| PRJ-024_Secrets-Management-Infisical.md | 3.2.3.1 | GTM_2026-W10_026 | GTM_2026-W11_328 | _PROJECTS_/ |
| PRJ-025_jAIMSnet-Platform-Engineering.md | 3.2.3.1 | GTM_2026-W10_026 | GTM_2026-W11_330 | _PROJECTS_/ |
| PRJ-026_Cybersecurity-Frameworks-ISMS.md | 3.2.3.1 | GTM_2026-W10_026 | GTM_2026-W10_026 | _PROJECTS_/ |
| GUIDE-011_Governance-Oversight-VSA-Process.md | 3.2.1.1 | GTM_2026-W10_066 | GTM_2026-W10_073 | _GUIDES_/ |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| **3.2.3.1** | **2026-W12** | **GTM_2026-W10_122** | **GTM_2026-W10_161** | **Updated deployment architecture: jAIMSnet DOKS cluster (ATL1) for Langfuse + LGTM+ stack (not Docker Droplet); Uptime Kuma = standalone Droplet (NYC1) for geographic resilience (confirmed LIVE). Phase 0.5 LGTM+ stack expanded: added Tempo (distributed tracing), Mimir (long-term metrics), Alloy (unified log+metric+trace collector, replaces Promtail). Full K8s Helm chart deployment commands. Updated 3-layer architecture diagram to reflect DOKS deployment. Added Hub + Tenant Observability Architecture section (preliminary, TBD after PRJ-025 Tracks 3+5). Updated incident history (+W10 incident = 6 total, 11.5 hrs). Added Alloy configuration YAML. Updated all integrations (+PRJ-024, PRJ-025, PRJ-026). Updated related documents to v3.2.3.1. Updated Discovered By (@RMN contributions: DOKS architecture, LGTM+Tempo+Mimir+Alloy stack). Note: final stack subject to PRJ-025 research confirmation.** |
| 3.2.1.1 | 2026-W10 | GTM_2026-W10_122 | GTM_2026-W10_161 | Phoenix → Langfuse (Layer 3); MIT replaces ELv2 (L-129); self-host from Day 1 at langfuse.jAIMS.app; native LiteLLM callback (5 min); +Multi-Tenant Tracking; +jAIMS.app Domain Family; +Phoenix→Langfuse Decision; 5 blind incidents (9.5 hrs) |
| 3.1.4.3 | 2026-W09 | GTM_2026-W09_185 | GTM_2026-W09_191 | +3-layer jAIMSnet observability stack; +Phase 0.5 (Prometheus+Grafana+Loki); +@MAIT:#InfraObs (@RMN); 5 incidents history; @RMN elevated |
| 3.1.4.2 | 2026-W09 | GTM_2026-W09_154 | GTM_2026-W09_158 | +Phase 0 (DO Infrastructure Observability); +jAIMSnet brand identity; +Uptime Kuma; +Phase 0 deployment checklist |
| 3.1.4.1 | 2026-W09 | GTM_2026-W09_121 | GTM_2026-W09_122 | Initial project; Phoenix observability; 3-phase rollout; LiteLLM integration |

---

#FlowsBros #FedArch #Observability #Langfuse #OTEL #jAIMSnet #Prometheus #Grafana #Loki #Tempo #Mimir #Alloy #FOSS #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
