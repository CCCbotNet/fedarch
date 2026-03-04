# PRJ-030: Email Infrastructure — WeOwn.net Migration + Stalwart

## 📋 PRJ-030_EmailInfrastructure_v3.2.1.1.md
## ♾️ WeOwnNet 🌐

| Field | Value |
|-------|-------|
| Document | PRJ-030_EmailInfrastructure.md |
| Version | 3.2.1.1 |
| CCC-ID | GTM_2026-W10_130 |
| Created | 2026-03-04 (W10) |
| Season | #WeOwnSeason003 🚀 |
| Status | ✅ APPROVED |
| Lifecycle Stage | ✅ APPROVED (#DocLifecycle) |
| Source of Truth | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-030_EmailInfrastructure.md) |
| Tags | #Email #Infrastructure #Proton #Stalwart #FOSS #FlowsBros |
| ⚠️ Classification | **REDACTED — Public Repository** |

---

## 📖 Table of Contents

1. [Project Identity](#-project-identity)
2. [Current State](#-current-state)
3. [The Problem](#-the-problem)
4. [Phase 1: Proton Consolidation](#-phase-1-proton-consolidation)
5. [Phase 2-4: Stalwart (Long-Term)](#-phase-2-4-stalwart-long-term)
6. [Address Matrix](#-address-matrix)
7. [Functional Addresses](#-functional-addresses)
8. [DNS Configuration](#-dns-configuration)
9. [Migration Checklist](#-migration-checklist)
10. [Cancellation Checklist](#-cancellation-checklist)
11. [Cost Summary](#-cost-summary)
12. [Timeline](#-timeline)
13. [Risk Matrix](#-risk-matrix)
14. [Discovered By](#-discovered-by)
15. [Related Documents](#-related-documents)
16. [Version History](#-version-history)

---

## 📋 Project Identity

| Field | Value |
|-------|-------|
| Project ID | **PRJ-030** |
| Title | **Email Infrastructure — WeOwn.net Migration + Stalwart** |
| Type | Infrastructure — Email |
| Priority | 🟠 P1 (Phase 1) / 🟡 P2 (Stalwart) |
| Owner | @GTM |
| Domain | **WeOwn.net** (primary) / WeOwn.email (alias) |
| Interim Solution | Proton Unlimited ($10/mo) |
| Long-Term Solution | Stalwart (FOSS — $6/mo self-hosted) |
| Timeline | Phase 1: W10-W11 / Phase 2-4: S003 late - S004 |
| #masterCCC | GTM_2026-W10_130 |

---

## 📋 Current State

> ⚠️ Email addresses redacted for public repository.

### Two Proton Accounts

| Account | Plan | Service | Custom Domain | Issue |
|---------|------|---------|---------------|-------|
| `[REDACTED]@proton.me` | Proton Visionary (~$30/mo) | Email | WeOwn.email | ❌ Cannot add VPN |
| `[REDACTED]@protonmail.com` | VPN Professional | VPN | N/A | ❌ No custom domain email |

### Current Email Domain

| Domain | Status | Used For |
|--------|--------|----------|
| **WeOwn.email** | ✅ Active | Key Staff email addresses |
| **WeOwn.net** | ❌ No email | Web domain only |

---

## 📋 The Problem

| # | Issue | Impact |
|---|-------|--------|
| 1 | **Fragmented across 2 Proton accounts** | Billing complexity, admin overhead |
| 2 | **Visionary plan cannot add VPN** | Key Staff lack VPN access |
| 3 | **VPN account has no custom email** | Cannot use primary brand domain |
| 4 | **WeOwn.email ≠ primary brand domain** | Brand inconsistency |
| 5 | **No unified admin** | 2 separate dashboards |
| 6 | **$40/mo for fragmented service** | Overpaying for incomplete solution |

### Brand Alignment

| Domain | Brand Alignment | Professional |
|--------|----------------|-------------|
| WeOwn.email | 🟡 Secondary TLD | ✅ |
| **WeOwn.net** | ✅ **Primary brand domain** | ✅ |

> **Email should match the primary brand domain.** `<CCC>@weown.net` is more recognizable and consistent than `<CCC>@weown.email`.

---

## 📋 Phase 1: Proton Consolidation

### Strategy

Consolidate both Proton accounts into one **Proton Unlimited** plan on the VPN account. Add WeOwn.net as custom domain. Unified email + VPN on one account.

### Proton Plan Selection

| Plan | Email | VPN | Custom Domains | Cost/mo | Verdict |
|------|-------|-----|----------------|---------|---------|
| Proton Free | ✅ (1 addr) | ❌ | ❌ | $0 | ❌ |
| Mail Plus | ✅ (10 addr) | ❌ | ✅ (1) | ~$4 | 🟡 No VPN |
| **Unlimited** | ✅ (15 addr) | ✅ | ✅ (3) | **~$10** | ✅ **BEST FIT** |
| Visionary | ✅ (unlimited) | ❌ | ✅ | ~$30 | ❌ No VPN |
| Business | ✅ (per user) | ✅ | ✅ | ~$7/user | 🟡 $63/mo for 9 users |

### Why Unlimited

| Factor | Value |
|--------|-------|
| 15 addresses | Fits 9 individual + 5 functional + 1 spare |
| 3 custom domains | WeOwn.net (primary) + WeOwn.email (alias) + 1 spare |
| VPN included | ✅ Solves VPN gap |
| $10/mo | **75% cheaper than current $40/mo** |
| Single admin | One dashboard for everything |

### What Changes

| Aspect | Before | After |
|--------|--------|-------|
| Accounts | 2 (fragmented) | **1 (unified)** |
| Plan | Visionary + VPN Pro | **Unlimited** |
| Cost | ~$40/mo | **$10/mo** |
| Email domain | WeOwn.email | **WeOwn.net** (primary) + WeOwn.email (alias) |
| VPN | Separate account | **Included** |
| Admin | 2 dashboards | **1 dashboard** |

---

## 📋 Phase 2-4: Stalwart (Long-Term)

### What Is Stalwart

| Field | Value |
|-------|-------|
| Name | **Stalwart** |
| URL | [stalw.art](https://stalw.art) |
| Type | Self-hosted email server |
| License | **AGPL-3.0 (FOSS)** |
| Features | SMTP, IMAP, JMAP, CalDAV, CardDAV |
| Language | Rust |

### Why Stalwart (Long-Term)

| Factor | Proton | Stalwart |
|--------|--------|----------|
| Data sovereignty | 🟡 Proton servers (Switzerland) | ✅ **Our servers (ATL1)** |
| Cost | $10/mo (ongoing) | **~$6/mo** (DO Droplet) |
| FOSS | ❌ Proprietary | ✅ **AGPL-3.0** |
| Control | 🟡 Proton admin panel | ✅ **Full server control** |
| Cooperative alignment | 🟡 Third-party service | ✅ **Priority #2 (FOSS) + #3 (Data Sovereignty)** |
| Complexity | ✅ Managed service | 🟡 Self-managed (DNS, TLS, deliverability) |
| Deliverability | ✅ Proton reputation | 🟡 Must build IP reputation |

### Stalwart Deployment (Future)

| Component | Detail |
|-----------|--------|
| Hosting | DigitalOcean Droplet (ATL1, 2 GB) |
| Cost | ~$6/mo |
| Domain | WeOwn.net |
| TLS | Let's Encrypt (Caddy or Certbot) |
| DNS | MX + SPF + DKIM + DMARC |
| Backup | Automated to DO Spaces or GB10-1 |

### Migration Path

| Phase | Solution | Timeline | Action |
|-------|----------|----------|--------|
| **Phase 1** | **Proton Unlimited** | **W10-W11** | **Consolidate NOW** |
| Phase 2 | Evaluate Stalwart | W15-W18 | Test deployment |
| Phase 3 | Deploy Stalwart (DO ATL1) | S003 late or S004 | Production deploy |
| Phase 4 | Migrate Proton → Stalwart | After stable | Move all addresses |
| Phase 5 | Cancel Proton | After verified | $0/mo email cost |

---

## 📋 Address Matrix

> ⚠️ Individual email addresses redacted. Format shown for reference.

### Individual Addresses

| CCC | @WeOwn.net (Primary) | @WeOwn.email (Alias) | Phase |
|-----|---------------------|---------------------|-------|
| GTM | `<CCC>@weown.net` | `<CCC>@weown.email` → forward | Phase 1 |
| THY | `<CCC>@weown.net` | `<CCC>@weown.email` → forward | Phase 1 |
| RMN | `<CCC>@weown.net` | `<CCC>@weown.email` → forward | Phase 1 |
| LDC | `<CCC>@weown.net` | `<CCC>@weown.email` → forward | Phase 1 |
| SHD | `<CCC>@weown.net` | `<CCC>@weown.email` → forward | Phase 1 |
| IAL | `<CCC>@weown.net` | — | Phase 2 |
| LFG | `<CCC>@weown.net` | — | Phase 2 |
| CRO | `<CCC>@weown.net` | — | Phase 2 |
| CEO | `<CCC>@weown.net` | — | Phase 2 |

### Address Count

| Type | Phase 1 | Phase 2 | Total |
|------|---------|---------|-------|
| Individual | 5 | +4 | 9 |
| Functional | 5 | — | 5 |
| **Total** | **10** | **14** | **14** |
| **Unlimited slots** | 15 | 15 | **1 spare** |

---

## 📋 Functional Addresses

| Address | Purpose | Forwards To |
|---------|---------|-------------|
| `team@weown.net` | Core TEAM distribution | All Key Staff |
| `admin@weown.net` | Administrative | Founders |
| `dev@weown.net` | Developer team | Dev team members |
| `support@weown.net` | Member support | Operations lead |
| `info@weown.net` | General inquiries | Operations lead + Founders |

---

## 📋 DNS Configuration

> ⚠️ Actual DNS record values redacted. Obtain from Proton dashboard during setup.

### Required DNS Records (WeOwn.net)

| Record | Type | Value | Purpose |
|--------|------|-------|---------|
| MX (primary) | MX | `[REDACTED — from Proton dashboard]` | Mail routing |
| MX (backup) | MX | `[REDACTED — from Proton dashboard]` | Failover routing |
| SPF | TXT | `[REDACTED — from Proton dashboard]` | Sender verification |
| DKIM (×3) | CNAME | `[REDACTED — from Proton dashboard]` | Email signing |
| DMARC | TXT | `[REDACTED — configure per policy]` | Anti-spoofing |
| Verification | TXT | `[REDACTED — from Proton dashboard]` | Domain ownership |

### DNS Provider

| Field | Value |
|-------|-------|
| Registrar | Porkbun |
| DNS hosting | Porkbun (or DigitalOcean if migrated per PRJ-012 pattern) |
| Owner | @GTM |

### Deliverability Checklist

| # | Check | Purpose |
|---|-------|---------|
| 1 | MX records resolve | Mail routing works |
| 2 | SPF passes | Sender authentication |
| 3 | DKIM passes | Email integrity |
| 4 | DMARC configured | Anti-spoofing policy |
| 5 | Test email (send + receive) | End-to-end verification |
| 6 | Check mail-tester.com | Deliverability score |

---

## 📋 Migration Checklist

### Phase 1: Proton Consolidation (14 Steps)

| # | Step | Owner | Est. Time | Status |
|---|------|-------|-----------|--------|
| 1 | Upgrade VPN account → Proton Unlimited ($10/mo) | @GTM | 5 min | ⬜ |
| 2 | Add WeOwn.net as custom domain in Proton | @GTM | 10 min | ⬜ |
| 3 | Get DNS records from Proton dashboard | @GTM | 5 min | ⬜ |
| 4 | Add DNS records at Porkbun (MX + SPF + DKIM + DMARC + verify) | @GTM | 20 min | ⬜ |
| 5 | Wait for DNS propagation | — | 1-48 hrs | ⬜ |
| 6 | Verify domain in Proton | @GTM | 5 min | ⬜ |
| 7 | Create 5 individual addresses (Phase 1 contributors) | @GTM | 10 min | ⬜ |
| 8 | Create 5 functional addresses | @GTM | 5 min | ⬜ |
| 9 | Configure WeOwn.email → WeOwn.net forwarding | @GTM | 10 min | ⬜ |
| 10 | Notify Key Staff via Signal | @GTM | 5 min | ⬜ |
| 11 | Each Key Staff tests send/receive | ALL | 10 min | ⬜ |
| 12 | Update external services (DO accounts, etc.) | @LDC + ALL | 15 min | ⬜ |
| 13 | Verify all addresses working (2-4 weeks) | @GTM | Ongoing | ⬜ |
| 14 | Cancel Visionary account (after verification) | @GTM | W13 | ⬜ |

**Total estimated time: ~2-3 hours** (excluding DNS propagation)

---

## 📋 Cancellation Checklist

### Before Cancelling Visionary Account

| # | Check | Verified? |
|---|-------|-----------|
| 1 | All WeOwn.email addresses forwarding to WeOwn.net | ☐ |
| 2 | All external services updated to @weown.net | ☐ |
| 3 | All Key Staff confirmed receiving on @weown.net | ☐ |
| 4 | No critical services tied to Visionary account | ☐ |
| 5 | Export any data from Visionary account | ☐ |

> **Do NOT cancel until ALL 5 checks pass.** Overlap period = ~$30 for 2-4 weeks. Worth the safety margin.

---

## 📋 Cost Summary

| Phase | Solution | Monthly | Annual | vs Current |
|-------|----------|---------|--------|-----------|
| **Current** | Visionary + VPN Pro | **~$40/mo** | **~$480/yr** | — |
| **Phase 1** | **Proton Unlimited** | **$10/mo** | **$120/yr** | **-$360/yr** |
| **Phase 3+** | **Stalwart (self-hosted)** | **~$6/mo** | **~$72/yr** | **-$408/yr** |

### Savings

| Transition | Monthly Savings | Annual Savings |
|-----------|----------------|---------------|
| Current → Phase 1 (Proton Unlimited) | **$30/mo** | **$360/yr** |
| Phase 1 → Phase 3 (Stalwart) | **$4/mo** | **$48/yr** |
| **Current → Phase 3 (total)** | **$34/mo** | **$408/yr** |

---

## 📋 Timeline

| Phase | Action | Timeline | Priority |
|-------|--------|----------|----------|
| **Phase 1** | **Proton → Unlimited + WeOwn.net** | **W10-W11** | 🟠 **P1** |
| Phase 1b | Cancel Visionary | W13 | 🟡 |
| Phase 2 | Evaluate Stalwart (test deploy) | W15-W18 | 🟡 P2 |
| Phase 3 | Deploy Stalwart on DO ATL1 | S003 late or S004 | 🟡 P2 |
| Phase 4 | Migrate Proton → Stalwart | After Stalwart stable | 🟡 P2 |
| Phase 5 | Cancel Proton Unlimited | After migration verified | 🟢 P3 |

---

## 📋 Risk Matrix

| # | Risk | Prob | Impact | Mitigation |
|---|------|------|--------|------------|
| 1 | DNS propagation delay | Low | Medium | Configure early; 48h buffer |
| 2 | WeOwn.email forwarding breaks | Low | Medium | Test before cancelling Visionary |
| 3 | Proton Unlimited 15-address limit | Low | Low | 14 needed; 1 spare; Business plan available |
| 4 | Stalwart deliverability (new IP) | Medium | Medium | Warm IP gradually; SPF/DKIM/DMARC |
| 5 | Self-hosted email complexity | Medium | Medium | Phase 2 evaluation before commitment |
| 6 | Key Staff don't update external services | Medium | Low | Forwarding catches missed updates |

---

## 📋 Discovered By (BP-047)

| CCC | Contributor | Role | Context |
|-----|-------------|------|---------|
| GTM | [yonks](https://GitHub.com/YonksTEAM) | Co-Founder / Chief Digital Alchemist | Identified fragmented Proton accounts; proposed WeOwn.net consolidation + Stalwart long-term; $408/yr savings |

---

## 📋 Related Documents

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| SharedKernel | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/SharedKernel.md) |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| 3.2.1.1 | 2026-W10 | GTM_2026-W10_130 | GTM_2026-W10_132 | Initial project; email infrastructure consolidation; 2 Proton accounts → 1 Unlimited ($10/mo); WeOwn.net primary domain; 9 individual + 5 functional addresses; WeOwn.email → WeOwn.net forwarding; 14-step migration checklist; 5-item cancellation checklist; Phase 2-4 Stalwart (FOSS self-hosted $6/mo); DNS config (redacted); $408/yr total savings; 6-risk matrix; all email addresses REDACTED for public GH |

---

#FlowsBros #FedArch #Email #Infrastructure #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
