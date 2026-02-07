# How To Create a GitHub Personal Access Token for AnythingLLM

## 📋 GUIDE-006_GitHub-PAT-for-AnythingLLM_v3.1.1.1.md
## ♾️ WeOwnNet 🌐 — Guide

| Field | Value |
|-------|-------|
| Document | GUIDE-006_GitHub-PAT-for-AnythingLLM.md |
| Version | 3.1.1.1 |
| CCC-ID | GTM_2026-W06_377 |
| Created | 2026-02-07 (W06) |
| Season | #WeOwnSeason003 🚀 |
| Status | 🔒 LOCKED |
| Source of Truth | [GitHub](https://github.com/CCCbotNet/fedarch/blob/main/_GUIDES_/GUIDE-006_GitHub-PAT-for-AnythingLLM.md) |
| Audience | All contributors (DEFAULT + ADMIN) |

---

## 📖 Table of Contents

1. [Overview](#-overview)
2. [Prerequisites](#-prerequisites)
3. [Step-by-Step: Create a Fine-Grained PAT](#-step-by-step-create-a-fine-grained-pat)
4. [Recommended Permissions](#-recommended-permissions)
5. [Configure in AnythingLLM](#-configure-in-anythingllm)
6. [Security Best Practices](#-security-best-practices)
7. [Troubleshooting](#-troubleshooting)
8. [Version History](#-version-history)

---

## 📋 Overview

### Why a GitHub PAT?

The #AnythingLLM **GitHub Repo** data connector pulls files from GitHub repositories into RAG. A Personal Access Token (PAT) authenticates these API requests.

### Why PAT for a PUBLIC Repo?

| Reason | Detail |
|--------|--------|
| **Rate Limits** | Unauthenticated: **60 req/hr** → Authenticated: **5,000 req/hr** |
| **Reliability** | Avoids 403 rate limit errors during multi-instance RAG sync |
| **Future-Proofing** | If CCCbotNet/fedarch ever goes private, no reconfiguration needed |
| **Audit Trail** | GitHub logs authenticated API access per token |
| **Best Practice** | BP-029 — security-first approach |

### PAT Types

| Type | Recommended | Why |
|------|-------------|-----|
| **Fine-grained** | ✅ YES | Scoped to specific repos + minimum permissions |
| Classic | ❌ NO | Overly broad scopes; legacy approach |

> ⚠️ Always use **Fine-grained** PATs. Classic PATs grant wider access than needed.

### Related Items

| Type | ID | Description |
|------|-----|-------------|
| Best Practice | BP-029 | Security-first approach |
| Best Practice | BP-044 | #PinnedDocs GH Push Workflow |
| Best Practice | BP-051 | #HomeInstance Setup |
| Learning | L-084 | GitHub Repo connector = PRIMARY data connector |
| Rule | R-204 | #HomeInstance MUST include #PinnedDocs |

---

## 📋 Prerequisites

| # | Requirement | Details |
|---|-------------|---------|
| 1 | GitHub account | [github.com](https://github.com) — free account is sufficient |
| 2 | Access to target repo | Must be able to view `CCCbotNet/fedarch` (public = ✅) |
| 3 | ADMIN role in #AnythingLLM | Required to configure data connectors |
| 4 | #AnythingLLM instance | Any instance (INT-P01, INT-OGx, INT-S0x) |

---

## 📋 Step-by-Step: Create a Fine-Grained PAT

### Step 1: Open GitHub Settings

| # | Action |
|---|--------|
| 1 | Go to [github.com](https://github.com) and sign in |
| 2 | Click your **profile avatar** (top-right corner) |
| 3 | Select **Settings** from the dropdown menu |

### Step 2: Navigate to Developer Settings

| # | Action |
|---|--------|
| 1 | Scroll down the left sidebar |
| 2 | Click **Developer settings** (bottom of sidebar) |

### Step 3: Select Fine-Grained Tokens

| # | Action |
|---|--------|
| 1 | In the left sidebar, click **Personal access tokens** |
| 2 | Click **Fine-grained tokens** |
| 3 | Click **Generate new token** |

### Step 4: Configure Token Details

| Field | Recommended Value | Notes |
|-------|-------------------|-------|
| **Token name** | `anythingllm-rag-readonly` | Descriptive name for easy identification |
| **Expiration** | 90 days | Balance security + convenience (see Best Practices) |
| **Description** | `Read-only access for AnythingLLM RAG connector — CCCbotNet/fedarch` | Optional but recommended |

### Step 5: Set Repository Access

| # | Action |
|---|--------|
| 1 | Select **Only select repositories** |
| 2 | From the dropdown, search for and select `CCCbotNet/fedarch` |
| 3 | Add additional repos if needed (e.g., `CCCbotNet/fedarch-private` in future) |

> ⚠️ Do NOT select "All repositories" — scope to only what's needed.

### Step 6: Set Permissions

| # | Action |
|---|--------|
| 1 | Expand **Repository permissions** |
| 2 | Set **Contents** → **Read-only** |
| 3 | Set **Metadata** → **Read-only** (auto-selected) |
| 4 | Leave ALL other permissions at **No access** |

> See [Recommended Permissions](#-recommended-permissions) for full table.

### Step 7: Generate and Copy

| # | Action |
|---|--------|
| 1 | Click **Generate token** |
| 2 | **IMMEDIATELY copy** the token value |
| 3 | Store securely (see Best Practices) |

> 🔴 **CRITICAL:** The token is shown ONLY ONCE. If you lose it, you must generate a new one.

---

## 📋 Recommended Permissions

### Repository Permissions (Minimum)

| Permission | Access | Required | Reason |
|------------|--------|----------|--------|
| **Contents** | Read-only | ✅ | Read repo files for RAG ingestion |
| **Metadata** | Read-only | ✅ | Required by GitHub API (auto-selected) |

### Permissions to LEAVE at No Access

| Permission | Access | Reason |
|------------|--------|--------|
| Actions | No access | Not needed for RAG |
| Administration | No access | Not needed for RAG |
| Code scanning alerts | No access | Not needed for RAG |
| Codespaces | No access | Not needed for RAG |
| Commit statuses | No access | Not needed for RAG |
| Dependabot | No access | Not needed for RAG |
| Deployments | No access | Not needed for RAG |
| Environments | No access | Not needed for RAG |
| Issues | No access | Not needed for RAG |
| Pages | No access | Not needed for RAG |
| Pull requests | No access | Not needed for RAG |
| Webhooks | No access | Not needed for RAG |
| Workflows | No access | Not needed for RAG |

### Account Permissions

| Permission | Access | Reason |
|------------|--------|--------|
| ALL | No access | Not needed for RAG |

> 💡 **Principle of Least Privilege** — only grant what's absolutely needed.

---

## 📋 Configure in AnythingLLM

### Step 1: Open Data Connector Settings

| # | Action |
|---|--------|
| 1 | Log in to your #AnythingLLM instance as ADMIN |
| 2 | Click the **wrench icon** (⚙️) in the left sidebar |
| 3 | Navigate to **Data Connectors** |
| 4 | Select **GitHub Repo** |

### Step 2: Enter Connection Details

| Field | Value | Notes |
|-------|-------|-------|
| **GitHub Repo URL** | `https://github.com/CCCbotNet/fedarch` | Full repo URL |
| **GitHub Access Token** | `github_pat_...` | Paste your Fine-grained PAT |
| **Branch** | `main` | Default branch |
| **Ignore Paths** | *(optional)* | Comma-separated paths to exclude |

### Step 3: Fetch and Select Files

| # | Action |
|---|--------|
| 1 | Click **Collect Data** (or equivalent button) |
| 2 | Wait for file tree to load |
| 3 | Select files/folders to ingest into RAG |
| 4 | Click **Save** or **Submit** |

### Step 4: Verify

| # | Check |
|---|-------|
| 1 | Files appear in your workspace document list |
| 2 | No 403 or 401 errors in console |
| 3 | Content is searchable via RAG queries |

### Multi-Instance Configuration

| Instance | Action |
|----------|--------|
| INT-P01 | Configure PAT in data connectors |
| INT-P02 | Configure SAME or SEPARATE PAT |
| INT-OGx | Configure PAT for #HomeInstance |
| INT-S0x | Configure PAT when deployed |

> 💡 Each instance needs its own data connector configuration. The SAME PAT can be used across multiple instances.

---

## 📋 Security Best Practices

### Token Management

| Practice | Description |
|----------|-------------|
| **Expiration** | Set 90-day expiration; rotate before expiry |
| **Naming** | Use descriptive names: `anythingllm-rag-readonly` |
| **Scope** | Fine-grained + specific repos only |
| **Permissions** | Contents + Metadata READ-ONLY — nothing else |
| **One Purpose** | One token per use case (don't reuse across tools) |

### Storage

| ✅ DO | ❌ DO NOT |
|--------|-----------|
| Store in Infisical (secrets manager) | Commit to any git repo |
| Store in password manager | Share in Signal/chat messages |
| Document token NAME (not value) in docs | Store in plain text files |
| Rotate before expiration | Use expired tokens |

### Rotation Schedule

| Interval | Action |
|----------|--------|
| Day 1 | Generate new PAT |
| Day 80 | ⚠️ Reminder: 10 days until expiry |
| Day 89 | Generate replacement PAT |
| Day 90 | Old PAT expires automatically |

### Revocation

| Scenario | Action |
|----------|--------|
| Token compromised | Revoke IMMEDIATELY via GitHub Settings → Developer Settings → Fine-grained tokens → Delete |
| Contributor leaves | Revoke all their PATs |
| Permission change | Revoke old, generate new with correct scope |

### GitHub Notification

GitHub will email you before token expiration. Monitor these emails.

---

## 📋 Troubleshooting

### Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `401 Unauthorized` | Invalid or expired PAT | Generate new PAT; verify it's copied correctly |
| `403 Forbidden` | Rate limited (unauthenticated) | Add PAT to data connector |
| `403 Forbidden` | PAT missing Contents permission | Edit token; add Contents → Read-only |
| `404 Not Found` | Wrong repo URL or PAT not scoped to repo | Verify repo URL; check token repository access |
| `422 Unprocessable` | PAT missing Metadata permission | Edit token; ensure Metadata → Read-only |
| No files loading | Branch name incorrect | Verify branch is `main` (not `master`) |
| Partial file sync | Ignore paths configured | Check ignore paths in data connector settings |

### Verification Checklist

| # | Check | Expected |
|---|-------|----------|
| 1 | PAT not expired | ✅ Valid date |
| 2 | PAT scoped to `CCCbotNet/fedarch` | ✅ Correct repo |
| 3 | Contents → Read-only | ✅ Enabled |
| 4 | Metadata → Read-only | ✅ Enabled |
| 5 | Repo URL correct | ✅ `https://github.com/CCCbotNet/fedarch` |
| 6 | Branch = `main` | ✅ Correct |
| 7 | #AnythingLLM logged in as ADMIN | ✅ Admin role |

### Still Having Issues?

| # | Step |
|---|------|
| 1 | Revoke current PAT |
| 2 | Generate fresh PAT following this guide from Step 1 |
| 3 | Clear browser cache / use incognito |
| 4 | Retry data connector configuration |
| 5 | If still failing → escalate via #ContextVolley to #MetaAgent |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| 3.1.1.1 | 2026-W06 | GTM_2026-W06_377 | GTM_2026-W06_380 | Initial creation; Fine-grained PAT guide for #AnythingLLM GitHub Repo data connector; 8 sections; minimum permissions (Contents + Metadata read-only); security best practices; troubleshooting; multi-instance guidance |

---

#FlowsBros #FedArch #AnythingLLM #GitHub #WeOwnSeason003

♾️ WeOwnNet 🌐 | 🏡 Real Estate and 🤝 cooperative ownership for everyone. An 🤗 inclusive community, by 👥 invitation only.
