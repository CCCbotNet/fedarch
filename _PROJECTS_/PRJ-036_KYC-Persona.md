# PRJ-036: KYC Deployment with Persona

## 📋 PRJ-036_KYC-Persona_v3.2.2.1.md
## ♾️ WeOwnNet 🌐 — Project Document

| Field | Value |
|-------|-------|
| **PRJ** | PRJ-036 |
| **Title** | KYC Deployment with Persona |
| **Short Name** | KYC-Persona |
| **Version** | 3.2.2.1 |
| **CCC-ID** | GTM_2026-W11_438 |
| **Approval** | GTM_2026-W11_478 |
| **Created** | 2026-03-13 (W11) |
| **Season** | #WeOwnSeason003 🚀 |
| **Status** | ✅ 🔒 APPROVED |
| **Priority** | 🔴 P0 (Critical Path for #ZeroTo100) |
| **Target** | W12-W13 (Phase 1), Jun-Jul (Phase 2) |
| **#LLMmodel** | Qwen3.5-397B-A17B (AI.YonksTEAM.xyz @GTM) |
| **#LLMmodel** | Claude Opus 4.6 (meta.WeOwn.tools #MetaAgent) |
| **Source of Truth** | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-036_KYC-Persona.md) |

---

## 📖 Table of Contents

1. [Executive Summary](#-executive-summary)
2. [Discovered By](#-discovered-by-bp-047)
3. [Project Overview](#-project-overview)
4. [Provider Selection](#-provider-selection)
5. [Scope — Phased Approach](#-scope--phased-approach)
6. [User Type Matrix](#-user-type-matrix)
7. [Integration Points](#-integration-points)
8. [Project Team](#-project-team)
9. [Resource Requirements](#-resource-requirements)
10. [Cost Estimate](#-cost-estimate)
11. [Compliance + Governance](#-compliance--governance)
12. [Data Sovereignty Mitigations](#-data-sovereignty-mitigations)
13. [Risks + Mitigations](#-risks--mitigations)
14. [Success Criteria](#-success-criteria)
15. [Related Documents](#-related-documents)
16. [Version History](#-version-history)

---

## 📋 Executive Summary

| Field | Value |
|-------|-------|
| **Problem** | ♾️ WeOwnNet 🌐 needs KYC/identity verification for contributors, investors, and cooperative members |
| **Solution** | Phase 1: WordPress + Persona (BurnedOutAdvisor.com). Phase 2: Migrate to jAIMSnet |
| **Timeline** | W12-W13 (Phase 1), Jun-Jul 2026 (Phase 2) |
| **Budget** | Phase 1: ~$1-3/verification. Phase 2: Included in jAIMSnet |
| **Owner** | @GTM (oversight) + @LDC (implementation) |
| **Architecture** | WordPress-First (March 2026 webinar) → jAIMSnet (post-May) |

### Why This Matters

| Use Case | Impact |
|----------|--------|
| **#ZeroTo100 Campaign** | Step 5 of 7 — KYC blocks Agency Owner eligibility |
| **BurnedOutAdvisor.com** | Webinar attendees → KYC → Retreat Bundle ($4,888) |
| **Cooperative Membership** | CCCbot.Net onchain cooperative requires KYC/AML |
| **AgencyPRO Clients** | Client identity verification before purchase |

### 7-Step User Journey (#ZeroTo100)

| # | Step | Platform | PRJ |
|---|------|----------|-----|
| 1 | Social media ad | LinkedIn/Meta | PRJ-012 |
| 2 | Landing page | WordPress (BurnedOutAdvisor.com) | PRJ-012 |
| 3 | Webinar | Zoom | PRJ-012 |
| 4 | Buy Retreat BUNDLE ($4,888) | Fluent Cart (WordPress) | PRJ-012 |
| 5 | **Complete KYC** | **Persona → WordPress → FluentCRM** | **PRJ-036** |
| 6 | AgencyPRO Fast Track | May 2026 | PRJ-002 |
| 7 | Summer Retreat | Colorado | PRJ-012 |

> **Step 5 is CRITICAL PATH.** No KYC = no Agency Owner eligibility = no retreat fulfillment.

---

## 📋 Discovered By (BP-047)

| CCC | Contributor | Role | Context |
|-----|-------------|------|---------|
| GTM | Jason Younker | Co-Founder | KYC requirement identified for #ZeroTo100 campaign — GTM_2026-W11_438 |
| LDC | Dhruv | Agentic AI Engineer | Implementation lead |
| META | #MetaAgent | Orchestrator | Provider selection (Persona), FOSS exception, data sovereignty mitigations |

---

## 📋 Project Overview

### Objectives

| # | Objective | Success Metric |
|---|-----------|----------------|
| 1 | Deploy Persona identity verification | < 5 minutes per verification |
| 2 | Integrate with WordPress (Phase 1) | FluentCRM tags + automations |
| 3 | Integrate with jAIMSnet (Phase 2) | Verification status → user profile |
| 4 | Implement role-based KYC flows | 6 user types supported |
| 5 | Achieve compliance (GDPR, CCPA) | DPA signed, audit trail |

### Scope Boundaries

| In Scope | Out of Scope |
|----------|--------------|
| ✅ Identity verification (ID + liveness) | ❌ Credit checks |
| ✅ AML screening (Phase 2+) | ❌ Background checks (criminal) |
| ✅ Document verification (accreditation) | ❌ Ongoing monitoring (Phase 3+) |
| ✅ WordPress webhook integration | ❌ Mobile app SDK (web only for MVP) |
| ✅ FluentCRM automation | ❌ Multi-language (English only Phase 1) |

---

## 📋 Provider Selection

### Why Persona?

| Criteria | Persona | Alternatives Considered |
|----------|---------|------------------------|
| **API Quality** | ✅ Excellent REST API + SDKs | Jumio (legacy), Onfido (complex) |
| **Pricing** | ✅ Pay-per-verification (~$1-3) | Veriff (expensive), Trulioo (enterprise) |
| **Integration** | ✅ React SDK + Webhooks | Alloy (overkill for MVP) |
| **Compliance** | ✅ SOC 2, GDPR, CCPA | All major providers compliant |
| **Workflow Builder** | ✅ Custom onboarding flows | Limited in competitors |
| **Support** | ✅ Startup-friendly | Enterprise-focused (others) |

### FOSS Exception (Priority #2)

| Provider | License | FOSS? | KYC Capable? |
|----------|---------|:-----:|:------------:|
| **Persona** | Proprietary | ❌ | ✅ **YES** |
| Ory Kratos | Apache 2.0 | ✅ | ❌ Auth only (no KYC) |
| Keycloak | Apache 2.0 | ✅ | ❌ Auth only (no KYC) |
| Verifiable Credentials (W3C) | W3C Standard | ✅ | ⚠️ Emerging (not production-ready) |

> **Exception Approved:** Persona is proprietary, but **no viable FOSS KYC provider exists** at equivalent quality/compliance. KYC/identity verification is a specialized compliance domain where proprietary providers (Persona, Jumio, Onfido) are industry standard. FOSS alternatives provide authentication (login), NOT verification (KYC/AML).

### Data Sovereignty Note (Priority #3)

| Statement | Reality | Mitigation |
|-----------|---------|------------|
| "Persona stores data (not us)" | ⚠️ Persona has users' PII | DPA + retention policy + consent flow |

> **See Data Sovereignty Mitigations section** for full details.

---

## 📋 Scope — Phased Approach

### Phase 1: WordPress + Persona (W12-W13)

| Feature | Detail | Effort |
|---------|--------|--------|
| Persona Account Setup | Sandbox + production config | 1h |
| WordPress REST API Endpoint | functions.php or custom plugin | 2-3h |
| Persona React SDK Embed | WordPress page (shortcode/block) | 2-3h |
| Webhook Handler (WordPress) | Receives Persona POST, updates FluentCRM | 2-3h |
| FluentCRM Automation | Tag-based email sequences | 1-2h |
| Testing (end-to-end) | Sandbox verifications | 2h |
| **Total** | | **10-14h** |

**Exit Criteria:** 10+ test verifications passed, FluentCRM tags working, emails triggering.

**Architecture:**
```
User buys BUNDLE → Fluent Cart → Persona Hosted Flow → 
Webhook → WordPress REST API → FluentCRM tags → 
Email automation ("Welcome to Agency" or "KYC Issue")
```

### Phase 2: Migrate to jAIMSnet (Jun-Jul 2026)

| Feature | Detail | Effort |
|---------|--------|--------|
| jAIMSnet webhook handler | LiteLLM or n8n in `automation` namespace | 4h |
| PostgreSQL POP DB schema | kyc_verifications table | 2h |
| Langfuse tracing | KYC event observability | 2h |
| Data migration | wp_kyc_verifications → POP DB | 2h |
| Testing + cutover | Parallel run, then deprecate WordPress | 2h |
| **Total** | | **12h** |

**Exit Criteria:** jAIMSnet handling all verifications, WordPress webhook deprecated.

**Architecture:**
```
Persona webhook → jAIMSnet (LiteLLM) → Langfuse traces → 
PostgreSQL → n8n automations → Email/Profile updates
```

### Phase 3: Scale (W14+)

| Feature | Detail | Effort |
|---------|--------|--------|
| Multi-tenant KYC | "0 to 100" AgencyPRO clients | TBD |
| Cooperative membership | CCCbot.Net onchain KYC/AML | TBD |
| Ongoing monitoring | Annual renewal, sanctions re-check | TBD |

---

## 📋 User Type Matrix

| User Type | KYC Level | Checks Required | When Triggered | Persona Workflow |
|-----------|-----------|-----------------|----------------|------------------|
| **Contributors** (Founding OGs) | 🟡 Basic | Government ID + liveness | Onboarding | `contributor_basic` |
| **Interns** (PRJ-020) | 🟡 Basic | ID + work authorization | Before start | `intern_basic` |
| **Investors** | 🔴 Enhanced | Accredited investor verification | Before investment | `investor_enhanced` |
| **AgencyPRO Customers** | 🟡 Basic | ID verification | Before purchase | `customer_basic` |
| **Cooperative Members** | 🔴 Enhanced | KYC/AML (sanctions, PEP) | Before membership | `cooperative_enhanced` |
| **Vendors** (@Vxy — VAW, VRB, VCP) | 🟡 Basic | ID + company verification | Before instance access | `vendor_basic` |

### KYC Level Definitions

| Level | Checks | Turnaround | Cost |
|-------|--------|------------|------|
| **🟡 Basic** | ID + liveness | < 5 min (automated) | ~$1-2 |
| **🔴 Enhanced** | ID + AML + accreditation | < 24 hours (manual review) | ~$2-3 |

---

## 📋 Integration Points

| PRJ | Project | Integration | Detail | Owner |
|-----|---------|-------------|--------|-------|
| **PRJ-002** | #AgencyPRO — #ResponsibleAgenticAI for Professionals | Client onboarding flow | KYC before purchase | @LDC |
| **PRJ-012** | BurnedOutAdvisor.com — Webinar + Retreat Campaign | Webinar → KYC funnel | WordPress integration | @LDC |
| **PRJ-020** | Interns Co-op Pipeline | Intern verification | ID + work authorization | @LDC |
| **PRJ-025** | jAIMSnet Platform Engineering | Verification status → profile | Phase 2 migration | @LDC |
| **PRJ-026** | Cybersecurity Frameworks + ISMS | **KYC = compliance control** | **@CCO oversight** | @CCO |
| **PRJ-030** | Email Infrastructure — WeOwn.net Migration + Stalwart | KYC complete → welcome | Automated notification | @LDC |
| **PRJ-032** | OpenTofu — Infrastructure as Code | Persona config as code | IaC (Phase 2) | @SHD |
| **PRJ-035** | SemaphoreUI Deployment | KYC workflow automation | Pipeline triggers (Phase 2) | @LDC |

---

## 📋 Project Team

| CCC | Contributor | Role | Responsibilities |
|-----|-------------|------|------------------|
| **GTM** | yonks | Project Owner | Oversight, stakeholder mgmt |
| **LDC** | Dhruv | Implementation Lead | API, SDK, webhooks, integration |
| **CCO** | Sharon Robertson | Compliance Officer | DPA, regulatory review, audit |
| **SHD** | Shahid | Frontend Engineer | React SDK integration, UI |

### RACI Matrix

| Task | GTM | LDC | CCO | SHD |
|------|-----|-----|-----|-----|
| Persona account setup | A | R | C | — |
| WordPress integration | C | R | — | C |
| jAIMSnet migration (Phase 2) | C | A | — | R |
| Compliance review | C | — | R | — |
| DPA negotiation | A | — | R | — |
| Production deployment | A | R | C | C |

**R** = Responsible | **A** = Accountable | **C** = Consulted | **—** = Not Involved

---

## 📋 Resource Requirements

| Resource | Estimate | Owner | Status |
|----------|----------|-------|--------|
| **Persona Account** | Setup + sandbox | @GTM | ⬜ TODO |
| **WordPress Integration** | 10-14 hours | @LDC | ⬜ TODO |
| **jAIMSnet Migration** | 12 hours | @LDC | ⬜ Phase 2 |
| **Frontend (React SDK)** | 4-6 hours | @SHD | ⬜ TODO |
| **Compliance Review** | 4-8 hours | @CCO | ⬜ TODO |
| **Testing** | 4 hours | @GTM + @LDC | ⬜ TODO |
| **Total** | **~30-40 hours** | — | — |

---

## 📋 Cost Estimate

| Item | Cost | Notes |
|------|------|-------|
| **Persona Sandbox** | FREE | Development + testing |
| **Production (per verification)** | ~$1-3/verification | Usage-based |
| **Monthly Minimum** | TBD | Depends on volume |
| **Phase 1 (W12-W13)** | Budget required | Estimate: $10-60/mo initial |
| **Phase 2 (Jun-Jul)** | Included in jAIMSnet | No additional infrastructure |

### Volume Projections

| Phase | Users/Month | Verifications/Mo | Cost/Mo (@$1-3) |
|-------|:-----------:|:----------------:|:---------------:|
| W12-W13 (sandbox) | 0 | 0 | $0 |
| W14-W16 (early production) | 10-20 | 10-20 | $10-60 |
| W17-W22 (Season 3 growth) | 50-100 | 50-100 | $50-300 |
| "0 to 100" (40 AgencyPRO) | 40-80 | 40-80 | $40-240 |
| Cooperative members | 100-500 | 100-500 | $100-1,500 |

### Budget Approval

| Phase | Cost | Approval Required |
|-------|------|-------------------|
| Phase 1 (WordPress) | $10-60/mo | ✅ Pre-approved |
| Phase 2 (jAIMSnet) | Included | ✅ Pre-approved |

---

## 📋 Compliance + Governance

### Regulatory Requirements

| Requirement | Status | Owner |
|-------------|--------|-------|
| GDPR Compliance | ✅ Persona handles EU data | @CCO |
| CCPA Compliance | ✅ Persona supports CA requests | @CCO |
| SOC 2 (Persona) | ✅ Provider certified | @CCO |
| Audit Trail | ✅ Persona provides verification logs | @CCO |
| User Consent | ⬜ Our responsibility (UI + TOS) | @GTM |

### Governance Gates

| Gate | Phase | Check | Owner |
|------|-------|-------|-------|
| **Gate 1** | Phase 1 | WordPress integration complete | @GTM |
| **Gate 2** | Phase 1 | @CCO compliance review | @CCO |
| **Gate 3** | Phase 1 | **Persona DPA signed** | @CCO |
| **Gate 4** | Phase 2 | jAIMSnet migration complete | @LDC |
| **Gate 5** | Phase 2 | Production budget approved | @GTM |

---

## 📋 Data Sovereignty Mitigations (Priority #3)

> **Tension:** Persona stores PII (not us). This conflicts with Priority #3 (Users own data). **Mitigation:** Legal + technical controls.

| Mitigation | Detail | Status |
|------------|--------|--------|
| **Persona DPA (Data Processing Agreement)** | Legal contract governing data handling | ⬜ Phase 1 Gate 3 |
| **Data Retention Policy** | Configure minimum retention in Persona | ⬜ Phase 1 |
| **User Consent Flow** | Explicit opt-in before KYC (UI + TOS) | ⬜ Phase 1 |
| **Right to Deletion** | Persona supports GDPR deletion requests | ✅ Available |
| **Audit Logging** | Track what data was shared + when | ⬜ Phase 1 |
| **Data Minimization** | Only collect what's legally required | ⬜ Phase 1 |

### User Consent Flow (Phase 1)

```
User clicks "Verify Identity" → Consent Modal →
[ ] I agree to share data with Persona for KYC verification
[ ] I understand Persona will store my data per their Privacy Policy
[ ] I consent to GDPR-compliant processing
→ Proceed to Persona verification
```

---

## 📋 Risks + Mitigations

| Risk | Probability | Impact | Mitigation | Owner |
|------|-------------|--------|------------|-------|
| API rate limits | Low | Medium | Batch requests, caching | @LDC |
| False positives | Medium | Low | Manual review workflow | @CCO |
| Cost overrun | Low | Medium | Usage alerts, caps | @GTM |
| WordPress integration complexity | Low | Low | Persona SDK well-documented | @LDC |
| Compliance gaps | Low | High | @CCO review before production | @CCO |
| DPA negotiation delays | Medium | Medium | Start early (Phase 1 Gate 2) | @CCO |
| User drop-off | Medium | Medium | Optimize UX, clear instructions | @SHD |
| jAIMSnet migration delays | Low | Medium | Parallel run before cutover | @LDC |

---

## 📋 Success Criteria

| Metric | Target | Measurement |
|--------|--------|-------------|
| Verification Time | < 5 minutes (automated) | Persona dashboard |
| False Positive Rate | < 5% | Manual review logs |
| User Completion Rate | > 80% | Funnel analytics |
| Integration Uptime | > 99% | WordPress/jAIMSnet monitoring |
| Cost per Verification | < $3 | Persona billing |
| Compliance Audit | 0 findings | @CCO review |

---

## 📋 Related Documents

| Document | Version | #masterCCC | Approval | URL |
|----------|---------|------------|----------|-----|
| SharedKernel | v3.2.2.1 | GTM_2026-W11_118 | GTM_2026-W11_139 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_SYS_/SharedKernel.md) |
| PRJ-002: #AgencyPRO — #ResponsibleAgenticAI for Professionals | v3.1.3.1 | GTM_2026-W08_043 | GTM_2026-W08_049 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-002_AgencyPRO.md) |
| PRJ-012: BurnedOutAdvisor.com — Webinar + Retreat Campaign | v3.1.3.1 | GTM_2026-W08_066 | GTM_2026-W08_089 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-012_BurnedOutAdvisor.md) |
| PRJ-020: Interns Co-op Pipeline | v3.2.1.1 | GTM_2026-W10_026 | GTM_2026-W11_318 | ⬜ GH Push Pending |
| PRJ-025: jAIMSnet Platform Engineering | v3.2.1.1 | GTM_2026-W10_026 | GTM_2026-W11_332 | ⬜ GH Push Pending |
| PRJ-026: Cybersecurity Frameworks + ISMS | v3.2.1.1 | GTM_2026-W10_026 | GTM_2026-W11_332 | ⬜ GH Push Pending |
| PRJ-030: Email Infrastructure — WeOwn.net Migration + Stalwart | v3.2.1.2 | GTM_2026-W10_130 | GTM_2026-W10_153 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-030_Email-Infrastructure.md) |
| PRJ-032: OpenTofu — Infrastructure as Code | v3.2.1.1 | GTM_2026-W10_265 | GTM_2026-W10_268 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-032_OpenTofu.md) |
| PRJ-035: SemaphoreUI Deployment | v3.2.2.1 | GTM_2026-W11_308 | GTM_2026-W11_455 | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_PROJECTS_/PRJ-035_SemaphoreUI.md) |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| v3.2.2.1 | 2026-W11 | GTM_2026-W11_438 | GTM_2026-W11_478 | Initial — KYC deployment with Persona (withpersona.com); 2-phase approach (WordPress W12-W13 → jAIMSnet Jun-Jul); 6 user types (Contributors, Interns, Investors, Customers, Cooperative Members, Vendors); 8 PRJ integrations (PRJ-002, 012, 020, 025, 026, 030, 032, 035); project team (GTM, LDC, CCO, SHD); FOSS exception documented (no viable FOSS KYC); data sovereignty mitigations (DPA, retention, consent, deletion); compliance gates (@CCO review, DPA required Phase 1 Gate 3); ~30-40 hours dev time; $10-60/mo Phase 1 budget; WordPress-first architecture (BurnedOutAdvisor.com) per GTM_2026-W11_445; #ZeroTo100 7-step user journey (Step 5 = KYC critical path); L-166/L-167 compliant (Related Docs populated DURING generation, 0 fix cycles); **META VSA 39/39 PASS** |

---

#FlowsBros #FedArch #PRJ-036 #KYC #Persona #WordPress #WeOwnSeason003

♾️ WeOwnNet 🌐 ● 🏡 Real Estate and 🤝 cooperative ownership for everyone ● An 🤗 inclusive community, by 👥 invitation only.
