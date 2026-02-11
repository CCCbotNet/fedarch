# CASE-STUDY-006: #AnythingLLM Prompt Architecture — Layer Resolution & System Prompt Variables

## 📋 CASE-STUDY-006_AnythingLLM-Prompt-Architecture_v3.1.2.1.md
## ♾️ WeOwnNet 🌐

| Field | Value |
|-------|-------|
| Document | CASE-STUDY-006_AnythingLLM-Prompt-Architecture.md |
| Version | 3.1.2.1 |
| CCC-ID | GTM_2026-W07_200 |
| Created | 2026-02-10 (W07) |
| Season | #WeOwnSeason003 🚀 |
| Status | 📋 INVESTIGATION |
| Tags | #AnythingLLM #SystemPromptVariables #YonksPromptingAcademy |

---

## 📖 Table of Contents

1. [Problem Statement](#-problem-statement)
2. [Investigation Scope](#-investigation-scope)
3. [Topic 1: #DefaultSystemPrompt (Layer 1)](#-topic-1-defaultsystemprompt-layer-1)
4. [Topic 2: #WorkspaceSystemPrompt (Layer 2)](#-topic-2-workspacesystemprompt-layer-2)
5. [Topic 3: #SystemPromptVariables](#-topic-3-systempromptVariables)
6. [Topic 4: Variable Resolution Pipeline](#-topic-4-variable-resolution-pipeline)
7. [Topic 5: v1.9.1 vs v1.10.0](#-topic-5-v191-vs-v1100)
8. [Topic 6: Verification Methodology](#-topic-6-verification-methodology)
9. [Findings Summary](#-findings-summary)
10. [Recommendations for #FedArch](#-recommendations-for-fedarch)
11. [Test Plan — W07 Day 3 #DeepDive](#-test-plan--w07-day-3-deepdive)
12. [Discovered By](#-discovered-by)
13. [Related Documents](#-related-documents)
14. [Version History](#-version-history)

---

## 📋 Problem Statement

| Field | Value |
|-------|-------|
| Problem | System Prompt Variables (`{user.name}`, `{workspace.name}`, `{datetime}`) were discovered and integrated into INT-P01 prompts, but @GTM + @RMN are NOT CONVINCED they are resolving correctly |
| Evidence | Phase 1 Test 2 on INT-P01 (GTM_2026-W07_170-174) — variables appeared NOT to resolve |
| Risk | If variables don't resolve, R-194 + R-206 enforcement falls back to instructional (trust-based) |
| Impact | L-120 + L-121 governance may be premature |
| Action | Definitive investigation before relying on variable-based enforcement |

### What We THINK We Know

| Claim | Confidence | Source |
|-------|------------|--------|
| #AnythingLLM supports System Prompt Variables | 🟡 MEDIUM | [docs.anythingllm.com](https://docs.anythingllm.com/features/system-prompt-variables) |
| Variables resolve at runtime per-message | 🟡 MEDIUM | Docs page |
| Variables work in #DefaultSystemPrompt (Layer 1) | 🔴 LOW | Untested definitively |
| Variables work in #WorkspaceSystemPrompt (Layer 2) | 🔴 LOW | Untested definitively |
| v1.10.0 supports variables | 🟡 MEDIUM | Feature listed in docs |
| v1.9.1 supported variables | 🔴 UNKNOWN | Not confirmed |

### What We DON'T Know

| Question | Status |
|----------|--------|
| Do variables resolve in Layer 1, Layer 2, or both? | ❓ UNKNOWN |
| Are variables pre-merge or post-merge? | ❓ UNKNOWN |
| Does the LLM see `{user.name}` or the resolved value? | ❓ UNKNOWN |
| Were variables broken/absent in v1.9.1? | ❓ UNKNOWN |
| How to definitively verify resolution? | ❓ UNKNOWN |

---

## 📋 Investigation Scope

| # | Topic | Priority |
|---|-------|----------|
| 1 | #DefaultSystemPrompt (Layer 1) architecture | 🔴 P0 |
| 2 | #WorkspaceSystemPrompt (Layer 2) architecture | 🔴 P0 |
| 3 | #SystemPromptVariables — syntax + scope | 🔴 P0 |
| 4 | Variable Resolution Pipeline — when + where | 🔴 P0 |
| 5 | v1.9.1 vs v1.10.0 — what changed | 🟠 P1 |
| 6 | Verification Methodology — definitive testing | 🔴 P0 |

---

## 📋 Topic 1: #DefaultSystemPrompt (Layer 1)

### Architecture

| Field | Value |
|-------|-------|
| Location | Admin Panel → Settings → Default System Prompt |
| URL | `https://<domain>/settings/default-system-prompt` |
| Scope | **ENTIRE INSTANCE** — all workspaces, all users |
| Loaded | Every message, every workspace |
| Analogy | THE CONSTITUTION |

### How It Works

Per [AnythingLLM docs](https://docs.anythingllm.com/features/system-prompt-variables):

| Aspect | Behavior |
|--------|----------|
| Persistence | Stored in instance settings database |
| Loading | Prepended to EVERY LLM call |
| Override | Can be supplemented (NOT overridden) by workspace prompt |
| Visibility | ALL workspaces see this prompt |
| Variables | ✅ Supported (per docs) |

### Key Finding

The #DefaultSystemPrompt is the **FIRST** system-level instruction the LLM receives. It establishes baseline behavior for ALL interactions across ALL workspaces.

---

## 📋 Topic 2: #WorkspaceSystemPrompt (Layer 2)

### Architecture

| Field | Value |
|-------|-------|
| Location | Workspace → Settings → Chat Settings → System Prompt |
| URL | `https://<domain>/workspace/<name>/settings/chat-settings` |
| Scope | **ONE workspace only** |
| Loaded | Appended AFTER Layer 1 |
| Analogy | THE BYLAWS |

### How Layers Combine

```
┌────────────────────────────────────────────────┐
│ What the LLM actually receives:                │
│                                                │
│ 1. [Default System Prompt — Layer 1]           │
│ 2. [Workspace System Prompt — Layer 2]         │
│ 3. [RAG Context — per message]                 │
│ 4. [Chat History — accumulated]                │
│ 5. [User Message — current]                    │
└────────────────────────────────────────────────┘
```

### Critical Behavior

| Question | Answer |
|----------|--------|
| Does Layer 2 override Layer 1? | **NO** — Layer 2 APPENDS |
| Can Layer 2 contradict Layer 1? | YES — but unpredictable which the LLM follows |
| If no Layer 2 exists? | Layer 1 alone applies |
| If Layer 1 is empty? | Only Layer 2 applies |

### Implication for #FedArch

| Risk | Detail |
|------|--------|
| **CONFLICT** | If Layer 1 says "generate CCC-IDs always" and Layer 2 says "only in CCC workspace" — LLM may follow either |
| **SOLUTION** | Layer 1 = CONSTITUTION (rules). Layer 2 = BYLAWS (workspace behavior). NO contradictions. |

---

## 📋 Topic 3: #SystemPromptVariables

### Official Documentation

Per [docs.anythingllm.com/features/system-prompt-variables](https://docs.anythingllm.com/features/system-prompt-variables):

| Variable | Description | Type |
|----------|-------------|------|
| `{time}` | Current time | System |
| `{date}` | Current date | System |
| `{datetime}` | Current date and time | System |
| `{user.id}` | Current user's ID | User |
| `{user.name}` | Current user's username | User |
| `{user.bio}` | Current user's bio field | User |
| `{workspace.id}` | Current workspace's ID | Workspace |
| `{workspace.name}` | Current workspace's name | Workspace |

### Syntax

| Aspect | Detail |
|--------|--------|
| Format | `{variable.name}` — curly braces |
| Case | Lowercase |
| Nesting | Not supported |
| Escaping | Unknown — needs testing |

### Where Variables Are Documented to Work

| Location | Supported | Source |
|----------|-----------|--------|
| Default System Prompt (Layer 1) | ✅ Per docs | [docs.anythingllm.com](https://docs.anythingllm.com/features/system-prompt-variables) |
| Workspace System Prompt (Layer 2) | ⬜ UNCLEAR | Not explicitly stated |
| Chat messages | ❌ NO | Variables are system-prompt only |

### ⚠️ KEY UNCERTAINTY

The docs page shows variables in the context of "System Prompt" but does NOT explicitly distinguish between #DefaultSystemPrompt and #WorkspaceSystemPrompt. The question is:

| Question | Possible Answers |
|----------|-----------------|
| Which "System Prompt" supports variables? | A: Both layers |
| | B: Layer 1 only |
| | C: Layer 2 only |
| | D: Depends on version |

**This is the #1 question for the #DeepDive.**

---

## 📋 Topic 4: Variable Resolution Pipeline

### Hypothesized Pipeline

```
Step 1: Load Default System Prompt (Layer 1) from DB
Step 2: Load Workspace System Prompt (Layer 2) from DB
Step 3: MERGE — Layer 1 + Layer 2
Step 4: RESOLVE VARIABLES — replace {var} with runtime values
Step 5: APPEND RAG context (per-message vector search)
Step 6: APPEND Chat History
Step 7: APPEND User Message
Step 8: SEND to LLM
```

### Key Questions

| # | Question | Impact |
|---|----------|--------|
| 1 | Are variables resolved BEFORE or AFTER merge? | Determines which layer supports them |
| 2 | Are variables resolved by AnythingLLM or by the LLM? | If by LLM, they're just text |
| 3 | Is resolution per-message or per-session? | Determines freshness |
| 4 | What happens if variable can't resolve? | Literal `{user.name}` or empty? |

### Hypothesis A: Pre-Merge Resolution

```
Layer 1 text → resolve variables → merged text
Layer 2 text → resolve variables → merged text
Merged text → send to LLM
```
**Implication:** Variables work in BOTH layers.

### Hypothesis B: Post-Merge Resolution

```
Layer 1 text + Layer 2 text → merge → resolve variables → send to LLM
```
**Implication:** Variables work in BOTH layers (same result).

### Hypothesis C: Layer 1 Only Resolution

```
Layer 1 text → resolve variables → merge with Layer 2 (raw) → send to LLM
```
**Implication:** Variables ONLY work in Layer 1. Layer 2 `{user.name}` = literal text.

### Source Code Investigation

| File | Path (GitHub) | Purpose |
|------|---------------|---------|
| `systemPrompt.js` | `server/utils/helpers/` | Variable resolution logic |
| `workspaceThread.js` | `server/models/` | Thread/workspace prompt handling |
| `chatHandler.js` | `server/endpoints/` | Message pipeline |

> **Recommendation:** @RMN should inspect source code during #DeepDive to determine actual pipeline.

---

## 📋 Topic 5: v1.9.1 vs v1.10.0

### v1.10.0 Release — Key Changes

Per [newreleases.io](https://newreleases.io/project/github/Mintplex-Labs/anything-llm/release/v1.10.0) (released 2026-01-22):

| Feature | Description | #FedArch Relevance |
|---------|-------------|-------------------|
| **Desktop Assistant** | Drop-in replacement for Granola/Otter/Fireflies | 🟡 Awareness |
| **Mobile App** | Android on Google Play | 🟡 Awareness |
| Removed onboarding "Create workspace" page | UX change | 🟢 LOW |
| Refactored workspace file picker | Performance | 🟢 LOW |
| Azure OpenAI v1 API migration | Agent support | 🟢 LOW |
| Cohere as agent provider | New provider | 🟢 LOW |
| Docker base image → Ubuntu 24 | Security | 🟠 @RMN note |
| ExpressJS 4.18.2 → 4.21.2 | Security | 🟠 @RMN note |
| MCP fixes for non-Windows | MCP | 🟠 Future |

### Variable Support — Version Timeline

| Question | Finding |
|----------|---------|
| Were variables in v1.9.1? | ⬜ **UNCLEAR** — docs page exists but no version tag |
| Were variables added in v1.10.0? | ⬜ **UNCLEAR** — not explicitly in changelog |
| Is this a pre-existing feature? | 🟡 LIKELY — docs page has no "new in v1.10.0" label |

### ⚠️ Critical Finding

The [System Prompt Variables docs page](https://docs.anythingllm.com/features/system-prompt-variables) shows a banner: "🚀 AnythingLLM v1.10.0 is live! Update now →" — but this is a SITE-WIDE banner, NOT a feature-specific tag. The variables feature may have existed in earlier versions.

### What @GTM Observed (v1.9.1 → v1.10.0)

| Test | v1.9.1 | v1.10.0 |
|------|--------|---------|
| Variables in Layer 1 | ❌ NOT TESTED | ❌ NOT RESOLVING (GTM_2026-W07_174) |
| Variables in Layer 2 | ❌ NOT TESTED | ⬜ NOT YET TESTED |

> **Conclusion:** The version upgrade alone may NOT be the fix. The issue may be syntax, layer placement, or pipeline behavior.

---

## 📋 Topic 6: Verification Methodology

### Method 1: Direct Prompt Test (RECOMMENDED — FIRST)

| Step | Action | Expected |
|------|--------|----------|
| 1 | Add to Layer 1: `Current user is: {user.name}` | |
| 2 | Add to Layer 1: `Current workspace is: {workspace.name}` | |
| 3 | Login as `u-gtm_user` in CCC workspace | |
| 4 | Ask: "What is my username?" | Should respond with `u-gtm_user` |
| 5 | Ask: "What workspace am I in?" | Should respond with `CCC` |
| 6 | If literal `{user.name}` → variables NOT resolving | |

### Method 2: Chat Logs (DEFINITIVE)

| Step | Action | What to Look For |
|------|--------|-----------------|
| 1 | Enable Chat Logs (if available) | Admin → Event Logs |
| 2 | Send a message | |
| 3 | Inspect the ACTUAL prompt sent to LLM | |
| 4 | Check if `{user.name}` was replaced with `u-gtm_user` | |

> Chat Logs show the EXACT prompt the LLM received. If `{user.name}` appears literally → NOT resolved.

### Method 3: API Debug

| Step | Action | What to Look For |
|------|--------|-----------------|
| 1 | Use AnythingLLM API directly | `/api/v1/workspace/<slug>/chat` |
| 2 | Send message with auth token | |
| 3 | Inspect response metadata | |
| 4 | Check if system prompt in response contains resolved values | |

### Method 4: Source Code Inspection

| Step | Action |
|------|--------|
| 1 | Clone `Mintplex-Labs/anything-llm` repo |
| 2 | Search for `{user.name}` or variable resolution logic |
| 3 | Trace the prompt assembly pipeline |
| 4 | Identify WHERE and WHEN variables are resolved |

### Method 5: Canary Test (SIMPLEST)

| Step | Action |
|------|--------|
| 1 | Add to Layer 1: `CANARY: The current user is {user.name} in workspace {workspace.name} at {datetime}` |
| 2 | Ask: "What does the CANARY line say?" |
| 3 | If response includes `u-gtm_user` → ✅ RESOLVED |
| 4 | If response includes `{user.name}` → ❌ NOT RESOLVED |

**Recommendation: Start with Method 5 (Canary) → then Method 2 (Chat Logs) for definitive proof.**

---

## 📋 Findings Summary

| # | Topic | Finding | Confidence |
|---|-------|---------|------------|
| 1 | Layer 1 (#DefaultSystemPrompt) | Instance-wide, loaded first | ✅ HIGH |
| 2 | Layer 2 (#WorkspaceSystemPrompt) | Workspace-specific, APPENDS to Layer 1 | ✅ HIGH |
| 3 | Variables — syntax | `{user.name}`, `{workspace.name}`, `{datetime}` | ✅ HIGH |
| 4 | Variables — which layer | ⬜ **UNKNOWN** — docs unclear, needs testing | 🔴 LOW |
| 5 | Variables — resolution timing | ⬜ **UNKNOWN** — pre-merge vs post-merge | 🔴 LOW |
| 6 | v1.9.1 vs v1.10.0 | Variables may be pre-existing feature, NOT v1.10.0 specific | 🟡 MEDIUM |
| 7 | Verification | Canary test + Chat Logs = definitive | ✅ HIGH |

### Overall Assessment

| Field | Value |
|-------|-------|
| Variables EXIST in docs | ✅ CONFIRMED |
| Variables WORK on INT-P01 | ❓ **UNCONFIRMED** — needs #DeepDive |
| L-120 + L-121 status | ✅ APPROVED — but may need REVISION if variables don't resolve |
| Risk | If variables fail → enforcement falls back to trust-based (still functional, less structural) |

---

## 📋 Recommendations for #FedArch

### Immediate (W07 Day 3)

| # | Action | Owner | Priority |
|---|--------|-------|----------|
| 1 | Run Canary Test on INT-P01 | @GTM | 🔴 P0 |
| 2 | Check Chat Logs for resolved values | @GTM | 🔴 P0 |
| 3 | Source code inspection | @RMN | 🟠 P1 |
| 4 | Test variables in Layer 2 separately | @GTM | 🟠 P1 |

### If Variables WORK ✅

| Action | Detail |
|--------|--------|
| Confirm L-120 + L-121 | ✅ Governance valid |
| Roll out to all instances | Phase 2 deployment |
| Update BP-054 | Add variable-based enforcement |
| Update ISC | Add variable verification check |

### If Variables DON'T WORK ❌

| Action | Detail |
|--------|--------|
| L-120 + L-121 | REVISE — note as "documented but unverified" |
| Enforcement model | Falls back to trust-based (still functional) |
| File GitHub issue | Report to Mintplex-Labs |
| Monitor v1.11.0 | Check if fixed in future release |
| Workaround | Agent can ask "What is your username?" — less elegant but functional |

### Regardless of Outcome

| Action | Detail |
|--------|--------|
| Layer 1/Layer 2 separation | ✅ KEEP — clean architecture regardless of variables |
| CONSTITUTION / BYLAWS model | ✅ KEEP — good separation of concerns |
| R-194 + R-206 | ✅ STILL ENFORCED — via instructional prompts (Layer 1 + Layer 2) |

---

## 📋 Test Plan — W07 Day 3 #DeepDive

### Pre-Requisites

| # | Item | Status |
|---|------|--------|
| 1 | INT-P01 back online (post @RMN maintenance) | ⬜ PENDING |
| 2 | v1.10.0 confirmed deployed | ⬜ PENDING |
| 3 | Layer 1 CONSTITUTION deployed | ✅ READY |
| 4 | Layer 2 CCC BYLAWS deployed | ✅ READY |

### Test Sequence

| # | Test | Method | Expected | Time |
|---|------|--------|----------|------|
| 1 | **Canary Test — Layer 1** | Add CANARY line to Layer 1, ask about it | Resolved values | 5 min |
| 2 | **Canary Test — Layer 2** | Add CANARY line to Layer 2, ask about it | Resolved values | 5 min |
| 3 | **Chat Logs** | Check Event Logs for actual prompt sent | Resolved in prompt | 5 min |
| 4 | **Multi-user test** | Login as u-gtm_user, u-thy_user, u-lfg_user | Different CCC per user | 15 min |
| 5 | **ADMIN test** | Login as a-gtm_dev, request CCC-ID | REFUSE | 5 min |
| 6 | **Cross-workspace test** | u-gtm_user in tools, request CCC-ID | REFUSE | 5 min |
| 7 | **API debug** (if needed) | Direct API call with inspection | Prompt metadata | 10 min |
| 8 | **Source code** (if needed) | @RMN inspects pipeline | Resolution logic | 30 min |

### Decision Matrix

| Canary Result | Chat Logs | Decision |
|---------------|-----------|----------|
| ✅ Resolved | ✅ Resolved | **CONFIRMED — L-120/L-121 valid** |
| ✅ Resolved | ❌ Literal | ⚠️ LLM inferring, not platform resolving — investigate |
| ❌ Literal | ❌ Literal | **NOT WORKING — file GH issue, revise L-120/L-121** |
| ❌ Literal | ✅ Resolved | ⚠️ Display issue only — variables work at prompt level |

---

## 📋 Discovered By (BP-047)

| CCC | Contributor | Role | Context |
|-----|-------------|------|---------|
| GTM | [yonks](https://GitHub.com/YonksTEAM) | Co-Founder / Chief Digital Alchemist | W07 Day 2 — #SystemPromptVariables discovery + failed Phase 1 test |
| RMN | Roman Di Domizio | AI Platform Engineer | W07 Day 2 — @RMN call, emergency maintenance, shared skepticism |

---

## 📋 Related Documents

| Document | Version | Relevance |
|----------|---------|-----------|
| SharedKernel | v3.1.2.1 | L-120, L-121, BP-054 |
| GUIDE-009 | v3.1.1.1 | Post-restart smoke test |
| CASE-STUDY-003 | v2.4.0 | MAIT Thread Identity (similar investigation pattern) |

### External Sources

| Source | URL |
|--------|-----|
| AnythingLLM Docs — System Prompt Variables | [docs.anythingllm.com](https://docs.anythingllm.com/features/system-prompt-variables) |
| AnythingLLM GitHub | [github.com/Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm) |
| AnythingLLM v1.10.0 Release | [newreleases.io](https://newreleases.io/project/github/Mintplex-Labs/anything-llm/release/v1.10.0) |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| 3.1.2.1 | 2026-W07 | GTM_2026-W07_200 | GTM_2026-W07_202 | Initial case study; 6 investigation topics; 5 verification methods; 8-test plan for W07 Day 3; decision matrix; 3 hypotheses for variable resolution pipeline |

---

#FlowsBros #FedArch #AnythingLLM #YonksPromptingAcademy #WeOwnSeason003

♾️ WeOwnNet 🌐 | 🏡 Real Estate and 🤝 cooperative ownership for everyone. An 🤗 inclusive community, by 👥 invitation only.
