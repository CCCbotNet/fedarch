# PRJ-030: Email Infrastructure — WeOwn.net Migration + Stalwart

## 📋 PRJ-030_EmailInfrastructure_v3.2.1.2.md
## ♾️ WeOwnNet 🌐

| Field | Value |
|-------|-------|
| Document | PRJ-030_EmailInfrastructure.md |
| Version | 3.2.1.2 |
| CCC-ID | GTM_2026-W10_130 |
| Created | 2026-03-04 (W10) |
| Updated | 2026-03-04 (W10) |
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
4. [Phase 1: Proton Business Suite](#-phase-1-proton-business-suite)
5. [Phase 2-4: Stalwart (Long-Term)](#-phase-2-4-stalwart-long-term)
6. [Address Matrix](#-address-matrix)
7. [Functional Addresses](#-functional-addresses)
8. [Proton Licenses](#-proton-licenses)
9. [DNS Configuration](#-dns-configuration)
10. [Migration Checklist](#-migration-checklist)
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
| Domain | **WeOwn.net** (primary) / WeOwn.email (legacy) |
| Phase 1 Solution | **Proton Business Suite ($42/mo — 6 licenses)** |
| Long-Term Solution | Stalwart (FOSS — $6/mo self-hosted) |
| Phase 1 Status | ✅ **COMPLETE** |
| Timeline | Phase 1: W10 ✅ / Phase 2-4: S003 late - S004 |
| #masterCCC | GTM_2026-W10_130 |

---

## 📋 Current State

> ⚠️ Email addresses redacted for public repository.

### Two Proton Accounts (Both Kept)

| Account | Plan | Service | Custom Domain | Status |
|---------|------|---------|---------------|--------|
| `[REDACTED]@proton.me` | Proton Visionary (~$30/mo) | Email | WeOwn.email | ✅ **KEPT** (legacy) |
| `[REDACTED]@protonmail.com` | **Proton Business Suite ($42/mo)** | Email + VPN (6 licenses) | **WeOwn.net** | ✅ **NEW — Phase 1** |

### Email Domains

| Domain | Status | Used For |
|--------|--------|----------|
| **WeOwn.net** | ✅ **ACTIVE (Phase 1)** | Primary Key Staff email |
| **WeOwn.email** | ✅ Active (legacy) | @RMN + historical addresses |

---

## 📋 The Problem

| # | Issue | Impact |
|---|-------|--------|
| 1 | **Fragmented across 2 Proton accounts** | Billing complexity, admin overhead |
| 2 | **Visionary plan cannot add VPN** | Key Staff lack VPN access |
| 3 | **VPN account has no custom email** | Cannot use primary brand domain |
| 4 | **WeOwn.email ≠ primary brand domain** | Brand inconsistency |
| 5 | **No unified admin** | 2 separate dashboards |
| 6 | **No individual user accounts** | Shared login = security risk |

### Brand Alignment

| Domain | Brand Alignment | Professional |
|--------|----------------|-------------|
| WeOwn.email | 🟡 Secondary TLD | ✅ |
| **WeOwn.net** | ✅ **Primary brand domain** | ✅ |

> **Email should match the primary brand domain.** `<CCC>@weown.net` is more recognizable and consistent than `<CCC>@weown.email`.

---

## 📋 Phase 1: Proton Business Suite

### Strategy

Deploy **Proton Business Suite** with 6 individual licenses on the VPN account. Add WeOwn.net as custom domain. Each Key Staff member gets their own login, email, and VPN.

### Why Business Suite (Not Unlimited)

| Factor | Unlimited ($10/mo) | Business Suite ($42/mo) |
|--------|-------------------|------------------------|
| Addresses | 15 shared | **Per-user (individual logins)** |
| VPN | 1 shared | **6 individual VPNs** |
| Admin | Single account | **Per-user admin** |
| Security | Shared login | **Individual credentials** |
| Scalability | 15 max | **Add users as needed** |
| Cost per user | $10 total | **$7/user** |

### What Changed from Original Plan

| Aspect | Original (v3.2.1.1) | Actual (v3.2.1.2) |
|--------|---------------------|-------------------|
| Plan | Proton Unlimited ($10/mo) | **Proton Business Suite ($42/mo)** |
| Users | 15 shared addresses, 1 login | **6 individual licenses** |
| VPN | 1 shared | **6 individual VPNs** |
| Visionary | Cancel (W13) | **KEEP (legacy WeOwn.email)** |
| Forwarding | WeOwn.email → WeOwn.net | **DEFERRED** |
| Value prop | Cost savings ($30/mo) | **Individual accounts + VPN per user** |

### What Proton Business Suite Provides

| Feature | Per License |
|---------|-------------|
| Email | ✅ Individual @weown.net address |
| VPN | ✅ Individual Proton VPN |
| Calendar | ✅ Proton Calendar |
| Drive | ✅ Proton Drive (15 GB/user) |
| Admin | ✅ Individual login + 2FA |
| Custom domain | ✅ WeOwn.net |

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
| Cost | $42/mo (ongoing) | **~$6/mo** (DO Droplet) |
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

| Phase | Solution | Timeline | Status |
|-------|----------|----------|--------|
| **Phase 1** | **Proton Business Suite** | **W10** | ✅ **COMPLETE** |
| Phase 2 | Evaluate Stalwart | W15-W18 | ⬜ |
| Phase 3 | Deploy Stalwart (DO ATL1) | S003 late or S004 | ⬜ |
| Phase 4 | Migrate Proton → Stalwart | After stable | ⬜ |

---

## 📋 Address Matrix

> ⚠️ Individual email addresses redacted. Format shown for reference.

### Individual Addresses

| CCC | @WeOwn.net (Primary) | @WeOwn.email (Legacy) | Phase | Status |
|-----|---------------------|----------------------|-------|--------|
| GTM | `<CCC>@weown.net` (×2 — admin + personal) | `<CCC>@weown.email` | Phase 1 | ✅ Confirmed |
| THY | `<CCC>@weown.net` | `<CCC>@weown.email` | Phase 1 | ✅ Confirmed |
| LDC | `<CCC>@weown.net` | `<CCC>@weown.email` | Phase 1 | ✅ Confirmed |
| LFG | `<CCC>@weown.net` | — | Phase 1 | ✅ Confirmed |
| SHD | `<CCC>@weown.net` | — | Phase 1 | ⬜ Pending creation |
| RMN | — (stays on WeOwn.email) | `<CCC>@weown.email` | — | ✅ No change |
| IAL | `<CCC>@weown.net` | — | Phase 2 | ⬜ |
| CRO | `<CCC>@weown.net` | — | Phase 2 | ⬜ |
| CEO | `<CCC>@weown.net` | — | Phase 2 | ⬜ |

### @RMN Decision

| Decision | Detail |
|----------|--------|
| @RMN stays on WeOwn.email | No Business Suite license needed |
| VPN | Addressed separately if needed |

### Address Count

| Type | Phase 1 | Phase 2 | Total |
|------|---------|---------|-------|
| Individual (WeOwn.net) | 5 (GTM×2, THY, LDC, LFG) + SHD pending | +3 (IAL, CRO, CEO) | 9 |
| Functional | 4 | — | 4 |
| **Total** | **~10** | **~13** | **~13** |

---

## 📋 Functional Addresses

| Address | Purpose | Status |
|---------|---------|--------|
| `admin@weown.net` | Administrative (**catch-all**) | ✅ Created |
| `billing@weown.net` | Billing + financial | ✅ Created |
| `dev@weown.net` | Developer team | ✅ Created |
| `social@weown.net` | Social media accounts | ✅ Created |

### Planned but Not Created (Deferred)

| Address | Purpose | Status |
|---------|---------|--------|
| `team@weown.net` | Core TEAM distribution | ⬜ Deferred |
| `support@weown.net` | Member support | ⬜ Deferred |
| `info@weown.net` | General inquiries | ⬜ Deferred |

---

## 📋 Proton Licenses

### Business Suite — 6 Licenses

| # | License Name | Role | CCC | Status |
|---|-------------|------|-----|--------|
| 1 | WeOwn.net | Primary Admin | — | ✅ Active |
| 2 | YonksTEAM | Member | GTM | ✅ Active |
| 3 | [REDACTED] | Member | THY | ✅ Active |
| 4 | [REDACTED] | Member | LDC | ✅ Active |
| 5 | [REDACTED] | Member | LFG | ✅ Active |
| 6 | [REDACTED] | Member | SHD | ✅ Active (email pending) |

### Not Licensed (Phase 2)

| CCC | Reason |
|-----|--------|
| RMN | Stays on WeOwn.email (no license needed) |
| IAL | Phase 2 |
| CRO | Phase 2 (was in original Phase 1 → moved) |
| CEO | Phase 2 |

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
| **DNS hosting** | **DigitalOcean** (nameservers migrated) |
| Owner | @GTM |

### Deliverability Checklist

| # | Check | Purpose | Status |
|---|-------|---------|--------|
| 1 | MX records resolve | Mail routing works | ✅ |
| 2 | SPF passes | Sender authentication | ✅ |
| 3 | DKIM passes | Email integrity | ✅ |
| 4 | DMARC configured | Anti-spoofing policy | ✅ |
| 5 | Test email (send + receive) | End-to-end verification | ✅ |
| 6 | Check mail-tester.com | Deliverability score | ⬜ |

---

## 📋 Migration Checklist

### Phase 1: Proton Business Suite (13 Steps)

| # | Step | Owner | Est. Time | Status |
|---|------|-------|-----------|--------|
| 1 | Upgrade VPN account → Proton Business Suite ($42/mo, 6 licenses) | @GTM | 5 min | ✅ |
| 2 | Add WeOwn.net as custom domain in Proton | @GTM | 10 min | ✅ |
| 3 | Get DNS records from Proton dashboard | @GTM | 5 min | ✅ |
| 4 | Add DNS records at DigitalOcean (MX + SPF + DKIM + DMARC + verify) | @GTM | 20 min | ✅ |
| 5 | Wait for DNS propagation | — | 1-48 hrs | ✅ |
| 6 | Verify domain in Proton | @GTM | 5 min | ✅ |
| 7 | Create individual addresses (5 confirmed + 1 pending) | @GTM | 10 min | ✅ |
| 8 | Create functional addresses (4 created) | @GTM | 5 min | ✅ |
| 9 | Configure WeOwn.email → WeOwn.net forwarding | @GTM | — | ⬜ **DEFERRED** |
| 10 | Notify Key Staff via Signal | @GTM | 5 min | ✅ |
| 11 | Each Key Staff tests send/receive | ALL | 10 min | ✅ |
| 12 | Update external services (DO accounts, etc.) | ALL | Ongoing | 🔄 |
| 13 | Verify all addresses working | @GTM | Ongoing | 🔄 |

**Phase 1 Status: ✅ COMPLETE** (Steps 1-8, 10-11 done. Step 9 deferred. Steps 12-13 ongoing.)

---

## 📋 Cost Summary

| Service | Entity | Monthly | Annual | Pre-existing? |
|---------|--------|---------|--------|--------------|
| Proton Business Suite (6 × $14.99) | ♾️ WeOwnNet 🌐 | **$89.94** | **$1,079.28** | ❌ NEW (PRJ-030) |
| VPN Professional (dedicated IP) | ♾️ WeOwnNet 🌐 | **$73.79** | **$885.48** | ✅ Pre-existing |
| **TOTAL (♾️ WeOwnNet 🌐)** | | **$163.73/mo** | **$1,964.76/yr** | |
| Proton Visionary (~$30/mo) | YonksTEAM LLC | — | — | ❌ EXCLUDED |

### Net New Cost from PRJ-030

| Metric | Value |
|--------|-------|
| Net new monthly | **$89.94/mo** (Business Suite only) |
| Net new annual | **$1,079.28/yr** |
| VPN Professional | Pre-existing — NOT a PRJ-030 cost |
| Proton Visionary | YonksTEAM LLC — NOT a ♾️ WeOwnNet 🌐 cost |

### Future Optimization

| Optimization | Potential Savings |
|-------------|------------------|
| Annual billing (Business Suite) | ~$30/mo (~$360/yr) |
| Evaluate VPN Pro necessity | $73.79/mo ($885/yr) — Business Suite includes VPN |
| Stalwart (Phase 3) | Replace Business Suite → $6/mo |

### Long-Term Cost Path

| Phase | Solution | Monthly (WeOwnNet) |
|-------|----------|-------------------|
| **Pre-PRJ-030** | VPN Professional only | $73.79 |
| **Phase 1 (current)** | **Business Suite + VPN Pro** | **$163.73** |
| **Phase 1 (optimized)** | Annual billing + VPN Pro | ~$133 |
| **Phase 3+** | Stalwart + VPN Pro | ~$79.79 |
| **Phase 3+ (no VPN Pro)** | Stalwart only | ~$6 |

---

## 📋 Timeline

| Phase | Action | Timeline | Priority | Status |
|-------|--------|----------|----------|--------|
| **Phase 1** | **Proton Business Suite + WeOwn.net** | **W10** | 🟠 P1 | ✅ **COMPLETE** |
| Phase 1b | @SHD email creation | W10-W11 | 🟠 P1 | ⬜ |
| Phase 1c | External services updated | W10-W13 | 🟡 P2 | 🔄 |
| Phase 2 | Evaluate Stalwart (test deploy) | W15-W18 | 🟡 P2 | ⬜ |
| Phase 3 | Deploy Stalwart on DO ATL1 | S003 late or S004 | 🟡 P2 | ⬜ |
| Phase 4 | Migrate Proton → Stalwart | After Stalwart stable | 🟡 P2 | ⬜ |

---

## 📋 Risk Matrix

| # | Risk | Prob | Impact | Mitigation |
|---|------|------|--------|------------|
| 1 | DNS propagation delay | Low | Medium | ✅ RESOLVED — propagated |
| 2 | WeOwn.email forwarding not configured | Low | Low | DEFERRED — not urgent; legacy addresses still work |
| 3 | Business Suite 6-license limit | Low | Low | Add licenses as needed ($7/user) |
| 4 | Stalwart deliverability (new IP) | Medium | Medium | Warm IP gradually; SPF/DKIM/DMARC |
| 5 | Self-hosted email complexity | Medium | Medium | Phase 2 evaluation before commitment |
| 6 | Key Staff don't update external services | Medium | Low | Legacy addresses still receiving; gradual transition |
| 7 | Combined cost ($72/mo) higher than planned | Low | Low | Value justifies — individual accounts + VPN; Stalwart reduces long-term |

---

## 📋 Discovered By (BP-047)

| CCC | Contributor | Role | Context |
|-----|-------------|------|---------|
| GTM | [yonks](https://GitHub.com/YonksTEAM) | Co-Founder / Chief Digital Alchemist | Identified fragmented Proton accounts; proposed WeOwn.net consolidation + Stalwart long-term; executed Phase 1 (Business Suite) |

---

## 📋 Related Documents

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| SharedKernel | v3.1.3.1 | GTM_2026-W08_069 | GTM_2026-W08_071 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/SharedKernel.md) |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| 3.2.1.2 | 2026-W10 | GTM_2026-W10_130 | GTM_2026-W10_153 | Phase 1 COMPLETE; Proton Unlimited → Business Suite (6 × $14.99 = $89.94/mo); VPN Professional ($73.79/mo) pre-existing; total ♾️ WeOwnNet 🌐 = $163.73/mo; Visionary = YonksTEAM LLC (excluded); Visionary NOT cancelling; WeOwn.email forwarding DEFERRED; 5 individual addresses confirmed + SHD pending; 4 functional addresses (admin catch-all, billing, dev, social); @CRO → Phase 2; @RMN stays on WeOwn.email; +Proton Licenses section; DNS = DigitalOcean; -Cancellation Checklist; FULL PRESERVE (L-097); all emails REDACTED |
| 3.2.1.1 | 2026-W10 | GTM_2026-W10_130 | GTM_2026-W10_132 | Initial project; email infrastructure consolidation; 2 Proton accounts → 1 Unlimited ($10/mo); WeOwn.net primary domain; 9 individual + 5 functional addresses; WeOwn.email → WeOwn.net forwarding; 14-step migration checklist; 5-item cancellation checklist; Phase 2-4 Stalwart (FOSS self-hosted $6/mo); DNS config (redacted); $408/yr total savings; 6-risk matrix; all email addresses REDACTED for public GH |

---

#FlowsBros #FedArch #Email #Infrastructure #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
