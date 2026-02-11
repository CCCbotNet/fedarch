# PRJ-009: #FedArchExpansion — ETHDenver.CCC.bot

## 📋 PRJ-009_FedArchExpansion_ETHDenver-CCC-bot_v3.1.2.1.md
## ♾️ WeOwnNet 🌐

| Field | Value |
|-------|-------|
| Document | PRJ-009_FedArchExpansion_ETHDenver-CCC-bot.md |
| Version | 3.1.2.1 |
| CCC-ID | GTM_2026-W07_217 |
| Created | 2026-02-11 (W07) |
| Season | #WeOwnSeason003 🚀 |
| Status | 🔒 LOCKED |
| Tags | #FedArchExpansion #ETHDenver2026 #DigitalOcean #FlowsBros |

---

## 📖 Table of Contents

1. [Project Identity](#-project-identity)
2. [Instance Identity](#-instance-identity)
3. [Strategic Context](#-strategic-context)
4. [Project Team](#-project-team)
5. [Infrastructure Architecture](#-infrastructure-architecture)
6. [12-Step Deployment Checklist](#-12-step-deployment-checklist)
7. [Demo Configuration](#-demo-configuration)
8. [Timeline](#-timeline)
9. [Success Criteria](#-success-criteria)
10. [Risk Matrix](#-risk-matrix)
11. [Relationship to Other Projects](#-relationship-to-other-projects)
12. [Decommission Plan](#-decommission-plan)
13. [Future Ownership](#-future-ownership)
14. [Discovered By](#-discovered-by)
15. [Related Documents](#-related-documents)
16. [Version History](#-version-history)

---

## 📋 Project Identity

| Field | Value |
|-------|-------|
| Project ID | **PRJ-009** |
| Title | #FedArchExpansion — ETHDenver.CCC.bot |
| Description | Deploy #AnythingLLM live demo instance at ETHDenver.CCC.bot for ETHDenver 2026 side events |
| Type | Infrastructure Deployment + Event Demo |
| Priority | 🔴 P0 (7 days to deployment deadline) |
| Owner | @GTM |
| Deployed By | @SHD |
| #masterCCC | GTM_2026-W07_216 |

---

## 📋 Instance Identity

| Field | Value |
|-------|-------|
| Instance ID | **INT-E01** |
| Domain | **ETHDenver.CCC.bot** |
| Type | Event (INT-Exx) — ephemeral (D-061) |
| Organization | ♾️ WeOwnNet 🌐 |
| Event | ETHDenver 2026 |
| Active Period | Wed 18 Feb → Sun 22 Feb 2026 (minimum) |
| Deploy By | **Mon 16 Feb 2026** (BUIDLWeek starts) |
| Decommission By | Sun 08 Mar 2026 (R-214) |
| Platform | AnythingLLM v1.10.0+ |
| LLM | Claude Opus 4.6 (`claude-opus-4-6`) |
| Embedder | Qwen3 Embedding 4B |

### Instance Category — NEW (D-061)

| ID | Term | Definition |
|----|------|------------|
| D-061 | INT-Exx | Event Instance — temporary #AnythingLLM instance deployed for specific events; ephemeral by design; decommissioned post-event; format INT-E01→INT-E99 |

### Decommission Rule — NEW (R-214)

| ID | Rule | Status |
|----|------|--------|
| R-214 | Event Instances (INT-Exx) MUST be decommissioned within 2 weeks of event end — data archived to RAG before teardown | 🔒 LOCKED |

---

## 📋 Strategic Context

### Why a Dedicated Instance

| Factor | Detail |
|--------|--------|
| **Live demo** | Show #FedArch + CCC in action at side events |
| **Audience engagement** | Attendees can interact with AI:@ETH agent |
| **Brand** | ETHDenver.CCC.bot = memorable, event-specific |
| **Isolation** | Production (INT-P01) stays clean — no demo traffic |
| **Showcase** | Cooperative ownership + #ResponsibleAgenticAI |
| **CCC Standard** | Live CCC-ID generation for attendees |

### What Attendees Experience

| # | Experience | Detail |
|---|-----------|--------|
| 1 | Visit ETHDenver.CCC.bot | Web-based #AnythingLLM |
| 2 | Create account | Guest or named |
| 3 | Chat with AI | Cooperative ownership Q&A |
| 4 | See CCC-IDs | Live attribution system |
| 5 | Learn about #FedArch | Multi-agent governance |
| 6 | Get excited | "I want this for my project!" |

---

## 📋 Project Team

| CCC | Contributor | Role | Responsibilities |
|-----|-------------|------|------------------|
| GTM | yonks | Project Owner | Requirements, prompts, content, ISC |
| SHD | Shahid | Deployment Lead | Infrastructure, DNS, Docker, SSL, deployment |
| RMN | Roman | Infrastructure Advisor | Kubernetes guidance, Helm chart reference |
| LFG | CoachLFG | Demo Content | Event-specific prompts, attendee engagement |
| LDC | Dhruv | Technical Demo | #ProjectConnex showcase integration |

---

## 📋 Infrastructure Architecture

### Platform

| Field | Value |
|-------|-------|
| Platform | **DigitalOcean** |
| Type | **Droplet** (standalone VM) |
| Deployment | **Docker Compose** |
| Reverse Proxy | **Caddy** (auto SSL via Let's Encrypt) |
| Domain | ETHDenver.CCC.bot |
| DNS | Porkbun.com (CCC.bot domain) → DigitalOcean Droplet IP |
| Data Center | **ATL1 (Atlanta)** — same DC as all existing instances |

### Recommended Droplet Spec

| Resource | Minimum | Recommended | Rationale |
|----------|---------|-------------|-----------|
| CPU | 2 vCPU | **4 vCPU** | AnythingLLM + Caddy + vector DB |
| RAM | 4 GB | **8 GB** | Embedding operations + concurrent users |
| Disk | 50 GB | **80 GB SSD** | RAG docs + vector store + Docker images |
| Plan | Basic | **Basic — ~$48/mo** | |
| Image | Ubuntu 24.04 LTS | Ubuntu 24.04 LTS | Matches AnythingLLM Docker base (v1.10.0) |
| Region | — | **ATL1 (Atlanta)** | Existing infrastructure — all instances deploy here |

### Region Selection

| Field | Value |
|-------|-------|
| Selected | **ATL1 (Atlanta)** |
| Reason | All existing #FedArch instances (INT-P01, INT-P02, INT-OG8) deploy in ATL1 |
| Benefit | Same DC = shared networking, consistent ops, @SHD familiarity |
| Latency to Denver | ~35-40ms (acceptable for demo) |

### Architecture Diagram

```
┌─────────────────────────────────────────────────────┐
│  DigitalOcean — ATL1 (Atlanta)                       │
│                                                      │
│  ┌──────────────┐  ┌──────────────────┐             │
│  │ INT-P01      │  │ INT-E01          │             │
│  │ AI.WeOwn.    │  │ ETHDenver.       │             │
│  │ Agency       │  │ CCC.bot          │             │
│  │ (K8s/DOKS)   │  │ (Droplet/Docker) │             │
│  └──────────────┘  └──────────────────┘             │
│                                                      │
│  ┌──────────────┐  ┌──────────────────┐             │
│  │ INT-P02      │  │ INT-OG8          │             │
│  │ Lite.Burned  │  │ AI.RomanDiD      │             │
│  │ Out.xyz      │  │ .xyz             │             │
│  └──────────────┘  └──────────────────┘             │
│                                                      │
│  ALL INSTANCES — SAME DATA CENTER (ATL1)             │
└─────────────────────────────────────────────────────┘

External APIs:
  AnythingLLM ──→ OpenRouter (Claude Opus 4.6)
  AnythingLLM ──→ Qwen3 Embedding (local or API)
```

### Docker Compose — AnythingLLM

```yaml
# docker-compose.yml
version: '3.8'

services:
  anythingllm:
    image: mintplexlabs/anythingllm:latest
    container_name: anythingllm
    restart: unless-stopped
    ports:
      - "3001:3001"
    volumes:
      - anythingllm_storage:/app/server/storage
    environment:
      - STORAGE_DIR=/app/server/storage
    cap_add:
      - SYS_ADMIN

  caddy:
    image: caddy:2-alpine
    container_name: caddy
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./Caddyfile:/etc/caddy/Caddyfile
      - caddy_data:/data
      - caddy_config:/config

volumes:
  anythingllm_storage:
  caddy_data:
  caddy_config:
```

### Caddyfile

```
ethdenver.ccc.bot {
    reverse_proxy anythingllm:3001
}
```

### Backup Strategy

| Action | When | Method |
|--------|------|--------|
| Droplet snapshot | Before event (Sun 16 Feb) | DigitalOcean Snapshots |
| Data backup | Daily during event | Volume snapshot |
| Post-event archive | After Sun 22 Feb | Export RAG + sessions → INT-P01 |

---

## 📋 12-Step Deployment Checklist

| # | Step | Owner | Details | Status |
|---|------|-------|---------|--------|
| 1 | **Create Droplet** | @SHD | DigitalOcean — 4 vCPU / 8 GB / 80 GB / **ATL1** / Ubuntu 24.04 | ⬜ |
| 2 | **DNS** | @SHD | Point ETHDenver.CCC.bot → Droplet IP (Porkbun) | ⬜ |
| 3 | **Docker + Compose** | @SHD | Install Docker Engine + Docker Compose on Droplet | ⬜ |
| 4 | **Deploy AnythingLLM** | @SHD | `docker compose up -d` — AnythingLLM + Caddy | ⬜ |
| 5 | **SSL Verify** | @SHD | Confirm Caddy auto-SSL for ETHDenver.CCC.bot | ⬜ |
| 6 | **LLM Config** | @SHD | Set Claude Opus 4.6 (`claude-opus-4-6`) via OpenRouter | ⬜ |
| 7 | **Embedder Config** | @SHD | Set Qwen3 Embedding 4B | ⬜ |
| 8 | **System Prompt** | @GTM | Layer 1 CONSTITUTION (ETHDenver-specific) | ⬜ |
| 9 | **Workspaces + Prompts** | @GTM | CCC + tools; workspace prompts per BP-053/BP-054 | ⬜ |
| 10 | **#PinnedDocs + Users + ChatHistory** | @GTM | 4 docs; demo users; ChatHistory = 40 | ⬜ |
| 11 | **#SmokeTest** | @GTM | GUIDE-009 — 8-point verification | ⬜ |
| 12 | **ISC** | @GTM | TMPL-010 — Instance Season Certification | ⬜ |

### Dependencies

| Step | Depends On |
|------|-----------|
| 2 (DNS) | 1 (Droplet — need IP) |
| 4 (Deploy) | 3 (Docker installed) |
| 5 (SSL) | 2 (DNS propagated) + 4 (Caddy running) |
| 6-7 (Models) | 4 (AnythingLLM running) |
| 8-10 (Config) | 6-7 (Models set) |
| 11 (#SmokeTest) | 8-10 (Config complete) |
| 12 (ISC) | 11 (#SmokeTest pass) |

### Droplet Security Hardening

| # | Step | Detail |
|---|------|--------|
| 1 | SSH key auth | No password login |
| 2 | Firewall | Allow 80, 443, 22 only |
| 3 | Non-root user | Create deploy user with sudo |
| 4 | Fail2ban | Brute-force protection |
| 5 | Automatic updates | `unattended-upgrades` |

### Quick-Start Script — @SHD

```bash
# Step 1: Create Droplet
doctl compute droplet create ethdenver-ccc-bot \
  --image ubuntu-24-04-x64 \
  --size s-4vcpu-8gb \
  --region atl1 \
  --ssh-keys <YOUR_SSH_KEY_ID> \
  --enable-monitoring \
  --enable-backups

# Step 2: SSH into Droplet
ssh root@<DROPLET_IP>

# Step 3: Install Docker
curl -fsSL https://get.docker.com | sh
apt install -y docker-compose-plugin

# Step 4: Create project directory
mkdir -p /opt/anythingllm && cd /opt/anythingllm

# Step 5: Create docker-compose.yml + Caddyfile (from above)

# Step 6: Deploy
docker compose up -d

# Step 7: Verify
curl -I https://ethdenver.ccc.bot
```

---

## 📋 Demo Configuration

### System Prompt — ETHDenver-Specific

| Section | Content |
|---------|---------|
| INSTANCE IDENTITY | INT-E01, ETHDenver.CCC.bot, Event |
| Welcome | "Welcome to the ♾️ WeOwnNet 🌐 demo at ETHDenver 2026!" |
| Focus | Cooperative ownership, #RWA, #FedArch, CCC Standard |
| Tone | Approachable, demo-friendly, educational |
| CCC-ID | ✅ GENERATE for demo users |
| OCPA Group | Cooperative real estate overview |

### Demo Workspaces

| Workspace | Emoji | Purpose |
|-----------|-------|---------|
| CCC | 🤝 | Live CCC-ID generation demo |
| tools | 🧠 | #FedArch governance demo |

### Demo Users

| Username | CCC | Purpose |
|----------|-----|---------|
| u-demo_user | DMO | General attendee demo |
| u-eth_user | ETH | ETHDenver-specific demo |
| a-gtm_dev | — | ADMIN (setup/management) |

### Demo Scenarios

| # | Scenario | Duration |
|---|----------|----------|
| 1 | "What is cooperative ownership?" | 2 min |
| 2 | "Show me a CCC-ID" | 1 min |
| 3 | "How does #FedArch work?" | 3 min |
| 4 | "What is OCPA Group?" | 2 min |
| 5 | "How is this different from a DAO?" | 3 min |

---

## 📋 Timeline

| Date | Day | Milestone | Owner | Status |
|------|-----|-----------|-------|--------|
| **Wed 11 Feb** | W07-D3 | PRJ-009 APPROVED + GH PUSH | @GTM | ⬜ |
| **Thu 12 Feb** | W07-D4 | Droplet created + DNS configured | @SHD | ⬜ |
| **Fri 13 Feb** | W07-D5 | Docker deployed + SSL verified | @SHD | ⬜ |
| **Sat 14 Feb** | W07-D6 | Models configured + System Prompt | @GTM + @SHD | ⬜ |
| **Sun 15 Feb** | W07-D7 | Workspaces + Users + #PinnedDocs | @GTM | ⬜ |
| **Mon 16 Feb** | W08-D1 | **🎯 #SmokeTest + ISC** | @GTM | ⬜ |
| Tue 17 Feb | W08-D2 | ETHDenver Day 1 — instance LIVE | — | ⬜ |
| **Wed 18 Feb** | W08-D3 | **PRJ-006 EVENT — demo at dinner** | @GTM | ⬜ |
| Thu-Sat 19-21 | W08-D4-6 | ETHDenver — instance available | — | ⬜ |
| **Sun 22 Feb** | W08-D7 | **PRJ-007 EVENT — demo at brunch** | @GTM | ⬜ |
| Sun 08 Mar | W10 | **DECOMMISSION** (R-214) | @SHD | ⬜ |

### Critical Path

```
Wed 11 ──→ Droplet ──→ Docker ──→ SSL ──→ Models ──→ Prompts ──→ Config ──→ #SmokeTest ──→ ISC ──→ LIVE
  PRJ-009    Thu        Fri       Fri      Sat       Sat        Sun       Mon 16          Mon 16    Tue 17
```

---

## 📋 Success Criteria

| # | Criteria | Measurement |
|---|----------|-------------|
| 1 | Instance live at ETHDenver.CCC.bot | ✅ Accessible via browser |
| 2 | ISC certified (8/8) | ✅ TMPL-010 attestation |
| 3 | CCC-ID generation works | ✅ Demo user can generate |
| 4 | #SmokeTest 8/8 | ✅ GUIDE-009 pass |
| 5 | Demo scenarios functional | ✅ 5 scenarios tested |
| 6 | Live before Mon 16 Feb | ✅ BUIDLWeek start |
| 7 | Stable during events | ✅ No outages Wed 18 + Sun 22 |

---

## 📋 Risk Matrix

| # | Risk | Probability | Impact | Mitigation |
|---|------|-------------|--------|------------|
| 1 | @SHD unavailable | 🟡 MEDIUM | 🔴 CRITICAL | @RMN backup; start Thu (4-day buffer) |
| 2 | DNS propagation delay | 🟢 LOW | 🟠 HIGH | Configure Thu, 48h buffer before Mon |
| 3 | SSL cert failure | 🟢 LOW | 🟠 HIGH | Caddy auto-LE; manual fallback |
| 4 | LLM API quota | 🟡 MEDIUM | 🟠 HIGH | Separate OpenRouter API key for INT-E01 |
| 5 | Demo traffic spike | 🟡 MEDIUM | 🟡 MEDIUM | 8 GB RAM sufficient; rate limiting |
| 6 | Embedder revert (L-107) | 🟢 LOW | 🟠 HIGH | Docker volume persists; verify post-restart |
| 7 | Content not ready | 🟢 LOW | 🟡 MEDIUM | @GTM preps prompts Sat-Sun |
| 8 | WiFi at venue | 🟡 MEDIUM | 🟠 HIGH | Mobile hotspot; pre-cache responses |
| 9 | Droplet outage | 🟢 LOW | 🔴 CRITICAL | DigitalOcean SLA; snapshot backup |
| 10 | Docker container crash | 🟡 MEDIUM | 🟠 HIGH | `restart: unless-stopped`; monitoring |

---

## 📋 Relationship to Other Projects

| PRJ | Title | Relationship |
|-----|-------|-------------|
| PRJ-006 | #SideEvent_ETHDenver2026_Wed | INT-E01 = live demo at this event |
| PRJ-007 | #SideEvent_ETHDenver2026_Sun | INT-E01 = live demo at this event |
| PRJ-008 | Technical Protocol Standard CCC | INT-E01 = showcase for CCC Standard |
| PRJ-005 | DrupalWiki | Content source for demo |

### Event → Instance Mapping

```
PRJ-006 (Wed 18 Feb dinner) ──→ INT-E01 demo
PRJ-007 (Sun 22 Feb brunch) ──→ INT-E01 demo
PRJ-008 (CCC Standard)      ──→ INT-E01 showcase
```

---

## 📋 Decommission Plan (R-214)

| # | Step | Owner | Deadline |
|---|------|-------|----------|
| 1 | Archive RAG data | @GTM_ADMIN | By Sun 01 Mar |
| 2 | Export session logs | @GTM_ADMIN | By Sun 01 Mar |
| 3 | Export user data | @GTM_ADMIN | By Sun 01 Mar |
| 4 | Docker compose down | @SHD | By Sun 08 Mar |
| 5 | DNS cleanup | @SHD | By Sun 08 Mar |
| 6 | Destroy Droplet | @SHD | By Sun 08 Mar |
| 7 | FULL:SYNC:META — decommission logged | @GTM | By Sun 08 Mar |

### Data Retention

| Data | Retain? | Where |
|------|---------|-------|
| Session logs | ✅ YES | RAG (INT-P01) — R-199 |
| Demo CCC-IDs | ✅ YES | Archived in `_SESSIONS_/` |
| System/Workspace prompts | ✅ YES | GH (fedarch) |
| User accounts | ❌ NO | Deleted with instance |
| RAG embeddings | ❌ NO | Deleted with instance |

---

## 📋 Future Ownership

| Field | Value |
|-------|-------|
| Proposed | ♾️ WeOwn.Events 📆 |
| Type | #OnchainCooperative |
| Purpose | Own/manage event instances (INT-Exx) |
| Status | 🔄 CONCEPTUAL |
| Relationship | Sub-entity of ♾️ WeOwnNet 🌐 |

---

## 📋 Discovered By (BP-047)

| CCC | Contributor | Role | Context |
|-----|-------------|------|---------|
| GTM | [yonks](https://GitHub.com/YonksTEAM) | Co-Founder / Chief Digital Alchemist | W07 Day 3 — ETHDenver demo planning + #FedArchExpansion |

---

## 📋 Related Documents

| Document | Version | Relevance |
|----------|---------|-----------|
| PRJ-006_SideEvent_ETHDenver2026_Wed | v3.1.2.1 | Wed event — demo venue |
| PRJ-007_SideEvent_ETHDenver2026_Sun | v3.1.2.1 | Sun event — demo venue |
| TMPL-010_ISC | v3.1.2.1 | ISC certification template |
| GUIDE-009_SmokeTest | v3.1.1.1 | Post-deployment verification |
| SharedKernel | v3.1.2.1 | #PinnedDoc + governance |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| 3.1.2.1 | 2026-W07 | GTM_2026-W07_216 | GTM_2026-W07_228 | Initial project; INT-E01 instance (D-061 Event category); 12-step deployment; DigitalOcean Droplet ATL1; Docker Compose + Caddy; demo config (5 scenarios); 10-risk matrix; decommission plan (R-214); +♾️ WeOwn.Events 📆 reference; relationship to PRJ-006/007/008; quick-start script for @SHD |

---

#FlowsBros #FedArch #FedArchExpansion #ETHDenver2026 #DigitalOcean #WeOwnSeason003

♾️ WeOwnNet 🌐 | 🏡 Real Estate and 🤝 cooperative ownership for everyone. An 🤗 inclusive community, by 👥 invitation only.
