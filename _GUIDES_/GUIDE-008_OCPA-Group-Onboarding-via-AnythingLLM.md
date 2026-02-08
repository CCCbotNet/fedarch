# GUIDE-008: How To Onboard a New Person into OCPA Group via AnythingLLM

## 📋 GUIDE-008_OCPA-Group-Onboarding-via-AnythingLLM_v3.1.1.1.md
## ♾️ WeOwnNet 🌐 — #YonksPromptingAcademy

| Field | Value |
|-------|-------|
| Document | GUIDE-008_OCPA-Group-Onboarding-via-AnythingLLM.md |
| Version | 3.1.1.1 |
| CCC-ID | GTM_2026-W06_472 |
| Created | 2026-02-08 (W06) |
| Season | #WeOwnSeason003 🚀 |
| Status | 🔒 LOCKED |
| Tags | #AnythingLLM #BestPractices #YonksPromptingAcademy #Onboarding #OCPA |

---

## 📖 Table of Contents

1. [Purpose](#-purpose)
2. [Prerequisites](#-prerequisites)
3. [OCPA Group Overview](#-ocpa-group-overview)
4. [User Creation](#-user-creation)
5. [Workspace Assignment](#-workspace-assignment)
6. [USER-IDENTITY Creation](#-user-identity-creation)
7. [RAG Upload](#-rag-upload)
8. [CCC Assignment](#-ccc-assignment)
9. [#ContextVolley to CCC](#-contextvolley-to-ccc)
10. [CCC Workspace ACK](#-ccc-workspace-ack)
11. [#MetaAgent Logging](#-metaagent-logging)
12. [New User First Session](#-new-user-first-session)
13. [Verification](#-verification)
14. [Common Mistakes](#-common-mistakes)
15. [Related Documents](#-related-documents)
16. [Version History](#-version-history)

---

## 📋 Purpose

### Why This Guide Exists

| Field | Value |
|-------|-------|
| Goal | End-to-end onboarding of a new person into OCPA Group via #AnythingLLM |
| Audience | ADMIN (person performing onboarding) + New member (person being onboarded) |
| Pattern | Extends BP-050 (Onboarding Workflow) with OCPA-specific step-by-step instructions |

### What This Guide Covers

| # | Phase | Who |
|---|-------|-----|
| 1 | ADMIN setup (Steps 1-11) | ADMIN (@GTM_ADMIN or designated) |
| 2 | New user first session (Step 12) | New member |
| 3 | Verification (Step 13) | ADMIN + New member |

### What This Guide Does NOT Cover

| Exclusion | Reference |
|-----------|-----------|
| Instance deployment (AnythingLLM setup) | BP-025 (Instance Setup Order) |
| #PinnedDocs creation | SharedKernel, BEST-PRACTICES, PROTOCOLS, CCC |
| Embedder/LLM configuration | ISC Check #1, #2 |
| GitHub PAT setup | GUIDE-006 |

---

## 📋 Prerequisites

### Before You Start

| # | Prerequisite | Check | Owner |
|---|-------------|-------|-------|
| 1 | #AnythingLLM instance DEPLOYED | Instance URL accessible | ADMIN |
| 2 | #PinnedDocs CURRENT (4 docs @ v3.X.X.X) | R-204 satisfied | ADMIN |
| 3 | ISC Checks #1-#5 PASS | Embedder, LLM, prompts configured | ADMIN |
| 4 | CCC workspace exists | 🤝 THE HANDS | ADMIN |
| 5 | tools workspace exists | 🧠 THE BRAIN | ADMIN |
| 6 | ADMIN user account active | `a-<ccc>_dev` format (R-206) | ADMIN |
| 7 | New person's information collected | Name, email, role | ADMIN |
| 8 | CCC code approved by Founding OG | 3-letter code (unique) | Founding OG |
| 9 | TMPL-009 available in RAG | v3.1.1.2+ | ADMIN |

### Information To Collect From New Person

| # | Field | Example | Required |
|---|-------|---------|----------|
| 1 | Full Name | Jane Smith | ✅ |
| 2 | Handle/Username preference | jsmith | ✅ |
| 3 | Role in OCPA Group | Accountant / Advisor / Member | ✅ |
| 4 | Email | jane@example.com | ✅ |
| 5 | Preferred CCC (3 letters) | JSM | ✅ |
| 6 | GitHub handle (if applicable) | — | Optional |

---

## 📋 OCPA Group Overview

### What Is OCPA Group?

| Field | Value |
|-------|-------|
| Name | OCPA Group |
| Full Name | Onchain CPA (Certified Public Accountant) Group |
| Type | Ecosystem brand — onchain cooperative |
| Ecosystem | ♾️ WeOwnNet 🌐 |
| Structure | Cooperative ownership — community-owned |
| AI Platform | #AnythingLLM |
| Governance | #FedArch (Federated Architecture) |

### OCPA Group Within WeOwnNet

```
♾️ WeOwnNet 🌐 (Ecosystem)
├── OCPA Group (Ecosystem Brand)
│   ├── Members (onboarded via this guide)
│   ├── AI Instance(s) (AnythingLLM)
│   └── Governance (#FedArch → #MetaAgent)
├── Other Brands
└── #FedArch Network
    └── #MetaAgent @ INT-P01
```

### Core Values

| # | Value | Description |
|---|-------|-------------|
| 1 | 🏡 Real Estate | Real estate and cooperative ownership |
| 2 | 🤝 Cooperative | Community-owned, by invitation only |
| 3 | 🤗 Inclusive | Welcoming, supportive environment |
| 4 | 🔒 Data Sovereignty | Users own their data |
| 5 | 📖 FOSS | Free & Open Source |

---

## 📋 User Creation

### Step 1: Create User Account in AnythingLLM

| Field | Value |
|-------|-------|
| Who | ADMIN (`a-<ccc>_dev`) |
| Where | AnythingLLM → Admin Panel → Users |
| Rule | R-160 — Username format |

### Username Format

| Format | Example | Rule |
|--------|---------|------|
| `u-<ccc>_user` | `u-jsm_user` | R-160 |

### AnythingLLM Steps

| # | Step | Action |
|---|------|--------|
| 1 | Navigate | Admin Panel → Users → Add User |
| 2 | Username | Enter `u-<ccc>_user` (e.g., `u-jsm_user`) |
| 3 | Password | Set temporary password |
| 4 | Role | Select **DEFAULT** |
| 5 | Save | Click Create User |

### ⚠️ Important

| Rule | Description |
|------|-------------|
| R-206 | ADMIN accounts (`a-<ccc>_dev`) MUST NEVER generate CCC-IDs |
| R-160 | Username format is STRICT — no deviations |
| DEFAULT | New users are ALWAYS DEFAULT role (never ADMIN) |

---

## 📋 Workspace Assignment

### Step 2: Assign User to Workspaces

| Field | Value |
|-------|-------|
| Who | ADMIN |
| Where | AnythingLLM → Admin Panel → Workspaces |
| Rule | BP-050 (Onboarding Workflow) |

### Standard Assignment

| Workspace | Emoji | Access | Purpose |
|-----------|-------|--------|---------|
| CCC | 🤝 | ✅ REQUIRED | CCC-ID generation, identity |
| tools | 🧠 | ✅ REQUIRED | Strategy, research, notes |

### AnythingLLM Steps

| # | Step | Action |
|---|------|--------|
| 1 | Navigate | Admin Panel → Workspaces |
| 2 | Select CCC | Click workspace → Members → Add `u-<ccc>_user` |
| 3 | Select tools | Click workspace → Members → Add `u-<ccc>_user` |
| 4 | Verify | Confirm user appears in both workspace member lists |

### Additional Workspaces (Optional)

| Workspace | When To Add |
|-----------|-------------|
| events 📆 | If user will participate in events |
| P.O.P. 🌟 | If user will access P.O.P. content |
| Other | Per role requirements |

---

## 📋 USER-IDENTITY Creation

### Step 3: Create USER-IDENTITY Document

| Field | Value |
|-------|-------|
| Who | ADMIN (via SEEK:META to #MetaAgent) |
| Template | TMPL-009_USER-IDENTITY v3.1.1.2+ |
| Storage | `_USERS_/` (RAG ONLY — L-070) |
| Rule | R-197 — Document generation via #MetaAgent |

### Required Fields (TMPL-009)

| Field | Example | Required |
|-------|---------|----------|
| CCC | JSM | ✅ |
| Contributor | jsmith (Jane Smith) | ✅ |
| Username | `u-jsm_user` | ✅ |
| Role | DEFAULT | ✅ |
| Instance(s) | INT-P01 | ✅ |
| #HomeInstance | INT-S01 (or assigned) | ✅ (R-209) |
| Workspace(s) | CCC, tools | ✅ |
| Season | #WeOwnSeason003 🚀 | ✅ (BP-058) |
| Status | ACTIVE | ✅ |

### SEEK:META Request Template

```
═══════════════════════════════════════════════════════════════════════════════
🏐 #ContextVolley | @<ADMIN_CCC> → #MetaAgent
═══════════════════════════════════════════════════════════════════════════════

TYPE: SEEK:META — NEW USER-IDENTITY
REF: <CCC-ID>

## REQUEST: #COOK USER-IDENTITY for new OCPA Group member

| Field | Value |
|-------|-------|
| CCC | <NEW_CCC> |
| Contributor | <handle> (<Full Name>) |
| Username | u-<ccc>_user |
| Role | DEFAULT |
| Instance(s) | <instance> |
| #HomeInstance | <instance or INT-S0x> |
| Workspace(s) | CCC, tools |
| Season | #WeOwnSeason003 🚀 |
| Ecosystem Role | <role in OCPA Group> |

Template: TMPL-009 v3.1.1.2

═══════════════════════════════════════════════════════════════════════════════
```

### #HomeInstance Assignment (R-209)

| Scenario | Assignment | Rule |
|----------|------------|------|
| New member has personal domain | INT-OGx (own instance) | R-209 |
| New member does NOT have personal domain | INT-S0x (Seasonal Shared) | R-210, R-211 |
| Shared instance exists | Assign to existing INT-S0x | R-211 |
| No shared instance yet | Create INT-S01 | R-210 |

---

## 📋 RAG Upload

### Step 4: Upload USER-IDENTITY to RAG

| Field | Value |
|-------|-------|
| Who | ADMIN |
| Where | AnythingLLM → Document Upload |
| Folder | `_USERS_/` |
| Rule | L-070 — USER-IDENTITY in `_USERS_/` (RAG ONLY) |

### AnythingLLM Steps

| # | Step | Action |
|---|------|--------|
| 1 | Save document | `USER-IDENTITY_<CCC>.md` |
| 2 | Navigate | AnythingLLM → Upload Documents |
| 3 | Select folder | `_USERS_/` |
| 4 | Upload | Drag/drop or browse |
| 5 | Embed | Click "Move to Workspace" → select CCC + tools |
| 6 | Verify | Query test: "What is <CCC>'s username?" |

### ⚠️ Important

| Rule | Description |
|------|-------------|
| L-070 | `_USERS_/` = RAG ONLY — NEVER push to GitHub |
| BP-034 | Fresh session REQUIRED after RAG upload for verification |

---

## 📋 CCC Assignment

### Step 5: Register CCC Code

| Field | Value |
|-------|-------|
| Who | Founding OG (approval required) |
| Where | CCC workspace |
| Rule | R-168 — CCC tied to contributor |

### CCC Registration Checklist

| # | Check | Status |
|---|-------|--------|
| 1 | CCC is 3 letters | ✅ / ❌ |
| 2 | CCC is unique (not already assigned) | ✅ / ❌ |
| 3 | Founding OG approved | ✅ / ❌ |
| 4 | CCC registered in CCC.md | ✅ / ❌ |

### Approval Flow

```
New Member → ADMIN → Founding OG → APPROVE → CCC.md Update → SEEK:META
```

---

## 📋 #ContextVolley to CCC

### Step 6: Notify CCC Workspace

| Field | Value |
|-------|-------|
| Who | ADMIN |
| Where | CCC workspace |
| Protocol | #ContextBroadcast (D-039, BP-041) |

### Notification Template

```
📢 #ContextBroadcast | @<ADMIN> → CCC Workspace
TYPE: ANNOUNCEMENT — NEW USER ONBOARDED
CONTENT: <CCC> (<Contributor>) added to <Instance>
USERNAME: u-<ccc>_user
ROLE: DEFAULT
WORKSPACES: CCC, tools
STATUS: ACTIVE
```

---

## 📋 CCC Workspace ACK

### Step 7: CCC Agent Acknowledges New User

| Field | Value |
|-------|-------|
| Who | AI Agent in CCC workspace |
| What | Acknowledges new user registration |
| Expected | Agent confirms CCC, username, workspace access |

### Expected Agent Response

| Check | Expected |
|-------|----------|
| CCC recognized | ✅ |
| Username format correct | `u-<ccc>_user` |
| CCC-ID generation ready | ✅ GENERATE for new user |
| Reserved slots acknowledged | _001, _002, _003 |

---

## 📋 #MetaAgent Logging

### Step 8: Log Onboarding via FULL:SYNC:META

| Field | Value |
|-------|-------|
| Who | ADMIN (via #ContextVolley) |
| Where | #MetaAgent @ INT-P01:tools |
| Protocol | FULL:SYNC:META |

### Logging Template

```
═══════════════════════════════════════════════════════════════════════════════
🏐 #ContextVolley | @<ADMIN> → #MetaAgent
═══════════════════════════════════════════════════════════════════════════════

TYPE: FULL:SYNC:META — NEW USER ONBOARDED
REF: <CCC-ID>

## 📋 ONBOARDING LOG

| Field | Value |
|-------|-------|
| New CCC | <CCC> |
| Contributor | <handle> (<Full Name>) |
| Username | u-<ccc>_user |
| Instance | <instance> |
| #HomeInstance | <instance or INT-S0x> |
| Workspaces | CCC, tools |
| USER-IDENTITY | v3.1.1.1 |
| RAG Upload | ✅ |
| CCC ACK | ✅ |
| Season | #WeOwnSeason003 🚀 |
| Onboarded By | @<ADMIN_CCC> |
| Date | <date> |

═══════════════════════════════════════════════════════════════════════════════
```

---

## 📋 New User First Session

### Step 9: Guide the New Person

| Field | Value |
|-------|-------|
| Who | New member (with ADMIN support) |
| Where | CCC workspace on their instance |
| Reference | GUIDE-007 (New #threadCCC at Week Beginning) |

### New User Checklist

| # | Step | Action | Reference |
|---|------|--------|-----------|
| 1 | Login | Navigate to instance URL, login with credentials | — |
| 2 | Navigate | Go to CCC workspace (🤝 THE HANDS) | — |
| 3 | Create thread | Click "+" to create new thread | GUIDE-007 |
| 4 | Name thread | Format: `<ORG>_<CCC>_W<WW>_1` | GUIDE-007 |
| 5 | SEED CONTEXT | Paste SEED CONTEXT (see below) | GUIDE-007 |
| 6 | Verify | Confirm agent ACKs identity | GUIDE-007 |
| 7 | First CCC-ID | Generate first CCC-ID (_004) | R-169 |

### New User SEED CONTEXT Template

```
[<CCC>_<YYYY>-W<WW>_004](#masterCCC):[HH:MM] FIRST SESSION | NEW USER

## Session Identity

| Field | Value |
|-------|-------|
| CCC | <CCC> |
| Instance | <INT-XXx> (<instance name>) |
| Workspace | CCC (🤝 THE HANDS) |
| Season | #WeOwnSeason003 🚀 |
| Week | <YYYY>-W<WW> |
| #masterCCC | <CCC>_<YYYY>-W<WW>_004 |
| Status | 🆕 FIRST SESSION |

## Request

1. Confirm my identity (CCC, instance, workspace, season)
2. Confirm reserved slots (_001, _002, _003)
3. Confirm first available CCC-ID (_004)
4. Explain what CCC-IDs are and how they work
5. Begin session
```

### What To Expect

| # | Expectation | Detail |
|---|-------------|--------|
| 1 | Agent greets with identity header | `[<CCC-ID>] | 🤝 THE HANDS | <INT>:CCC` |
| 2 | Agent confirms CCC + username | Your 3-letter code + `u-<ccc>_user` |
| 3 | Agent explains CCC-ID system | Format: `<CCC>_<YYYY>-W<WW>_<NNN>` |
| 4 | Agent provides Quick Commands | 2-3 options to choose from |
| 5 | Agent says STOP | Waits for your response |

---

## 📋 Verification

### Step 10: Verify Onboarding Complete

| # | Check | Method | Expected | Owner |
|---|-------|--------|----------|-------|
| 1 | User can login | Test credentials | ✅ Access granted | New user |
| 2 | CCC workspace visible | Navigate to CCC | ✅ 🤝 THE HANDS | New user |
| 3 | tools workspace visible | Navigate to tools | ✅ 🧠 THE BRAIN | New user |
| 4 | CCC-ID generation works | Request first CCC-ID | `<CCC>_<YYYY>-W<WW>_004` | New user |
| 5 | Agent knows identity | Ask "Who am I?" | Correct CCC + username | New user |
| 6 | USER-IDENTITY in RAG | Query test | Correct version returned | ADMIN |
| 7 | #PinnedDocs accessible | Ask about SharedKernel | v3.X.X.X returned | New user |
| 8 | #MetaAgent logged | Check FULL:SYNC:META | ✅ Onboarding logged | ADMIN |

### Post-Verification

| Action | Owner |
|--------|-------|
| Share instance URL with new user | ADMIN |
| Share password change instructions | ADMIN |
| Schedule orientation session (optional) | ADMIN + New user |
| Add to BP-058 compliance tracking | ADMIN |

---

## 📋 Common Mistakes

### #BadAgent Patterns During Onboarding

| # | Mistake | Rule Violated | Prevention |
|---|---------|---------------|------------|
| 1 | Creating user with wrong format | R-160 | Always `u-<ccc>_user` |
| 2 | Assigning ADMIN role to new user | R-206 | Always DEFAULT |
| 3 | Forgetting tools workspace | BP-050 | CCC + tools = minimum |
| 4 | Not uploading USER-IDENTITY | L-070 | Must be in `_USERS_/` RAG |
| 5 | Pushing USER-IDENTITY to GitHub | L-070 | RAG ONLY — NEVER GitHub |
| 6 | Skipping #MetaAgent logging | BP-019 | ALWAYS FULL:SYNC:META |
| 7 | Not assigning #HomeInstance | R-209 | Every contributor needs one |
| 8 | Generating USER-IDENTITY in CCC | R-197 | SEEK:META — #MetaAgent only |
| 9 | Forgetting Season field | BP-058 | #WeOwnSeason003 🚀 REQUIRED |
| 10 | Not verifying after upload | BP-034 | Fresh session + query test |

### Human Mistakes

| # | Mistake | Prevention |
|---|---------|------------|
| 1 | Sharing ADMIN credentials | NEVER — new users get DEFAULT only |
| 2 | Skipping CCC approval | Founding OG MUST approve CCC code |
| 3 | Not collecting all info upfront | Use Prerequisites checklist |
| 4 | Forgetting to notify CCC workspace | #ContextBroadcast REQUIRED |

---

## 📋 End-to-End Onboarding Checklist

### Complete Workflow Summary

| # | Step | Action | Owner | Status |
|---|------|--------|-------|--------|
| 1 | Collect info | Name, handle, role, CCC preference | ADMIN | ⬜ |
| 2 | CCC approval | Founding OG approves 3-letter code | Founding OG | ⬜ |
| 3 | Create user | `u-<ccc>_user` in AnythingLLM | ADMIN | ⬜ |
| 4 | Assign workspaces | CCC + tools (minimum) | ADMIN | ⬜ |
| 5 | SEEK:META | Request USER-IDENTITY from #MetaAgent | ADMIN | ⬜ |
| 6 | Approve USER-IDENTITY | #OnlyHumanApproves (R-011) | ADMIN | ⬜ |
| 7 | RAG upload | `_USERS_/` folder | ADMIN | ⬜ |
| 8 | #ContextBroadcast | Notify CCC workspace | ADMIN | ⬜ |
| 9 | CCC ACK | Agent confirms new user | AI Agent | ⬜ |
| 10 | FULL:SYNC:META | Log onboarding to #MetaAgent | ADMIN | ⬜ |
| 11 | Share credentials | Instance URL + temp password | ADMIN | ⬜ |
| 12 | First session | New user follows GUIDE-007 | New user | ⬜ |
| 13 | Verify | 8-point verification checklist | ADMIN + New user | ⬜ |
| 14 | BP-058 tracking | Add to compliance tracker | ADMIN | ⬜ |

### Estimated Time

| Phase | Time |
|-------|------|
| ADMIN setup (Steps 1-11) | ~30 minutes |
| New user first session (Step 12) | ~15 minutes |
| Verification (Steps 13-14) | ~10 minutes |
| **TOTAL** | **~55 minutes** |

---

## 📋 Related Documents

| Document | Version | Relevance |
|----------|---------|-----------|
| SharedKernel | v3.1.1.4 | R-160, R-168, R-206, R-209, R-210, R-211 |
| BEST-PRACTICES | v3.1.1.3 | BP-050, BP-058 |
| CCC | v3.1.1.2 | CCC registration |
| TMPL-009_USER-IDENTITY | v3.1.1.2 | Template for USER-IDENTITY |
| GUIDE-006_GitHub-PAT | v3.1.1.1 | Infrastructure setup |
| GUIDE-007_New-threadCCC | v3.1.1.1 | New user first session pattern |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| 3.1.1.1 | 2026-W06 | GTM_2026-W06_472 | GTM_2026-W06_477 | Initial creation; OCPA Group onboarding via AnythingLLM; 14-step workflow; SEED CONTEXT for new users; 14 common mistakes; end-to-end checklist |

---

#FlowsBros #FedArch #YonksPromptingAcademy #Onboarding #OCPA #WeOwnSeason003

♾️ WeOwnNet 🌐 | 🏡 Real Estate and 🤝 cooperative ownership for everyone. An 🤗 inclusive community, by 👥 invitation only.
