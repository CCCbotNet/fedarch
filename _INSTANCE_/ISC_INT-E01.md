# ISC: INT-E01 — Instance Season Certification

## 📋 ISC_INT-E01_v3.1.2.1.md
## ♾️ WeOwnNet 🌐

| Field | Value |
|-------|-------|
| Document | ISC_INT-E01.md |
| Version | 3.1.2.1 |
| CCC-ID | GTM_2026-W07_285 |
| Created | 2026-02-13 (W07) |
| Season | #WeOwnSeason003 🚀 |
| Status | ✅ CERTIFIED |
| Tags | #ISC #ETHDenver2026 #FedArch |

---

## 📋 Instance Identity

| Field | Value |
|-------|-------|
| Instance ID | **INT-E01** |
| Name | ETHDenver.CCC.bot |
| Type | 🎪 Event Instance (ephemeral) |
| Organization | ♾️ WeOwnNet 🌐 |
| Domain | https://ethdenver.ccc.bot |
| Owner(s) | @GTM |
| Legacy ID | N/A (new instance) |
| Platform | AnythingLLM |

---

## 📋 Certification Details

| Field | Value |
|-------|-------|
| Season | #WeOwnSeason003 🚀 |
| Season Start | W06 (Mon 02 Feb 2026) |
| Certification Deadline | Sun 15 Feb 2026 (BP-059) |
| Certifier | @GTM |
| Witnessed By | LiveStream audience |
| Date | 2026-02-13 |
| REF | GTM_2026-W07_277 |

---

## 📋 Ecosystem Approved Models

| Type | Model | API ID | Approved |
|------|-------|--------|----------|
| Embedder | Qwen3 Embedding 4B | — | GTM_2026-W06_175 |
| LLM | Claude Opus 4.6 | `claude-opus-4-6` | GTM_2026-W06_257 |

---

## 📋 ISC 8-Point Checklist

### Check 1: EMBEDDER

| Field | Value |
|-------|-------|
| Check | Embedding model verified |
| Pass Criteria | Qwen3 Embedding 4B |
| Location | Admin Panel → Settings → Embedding Preference |
| Actual | **Qwen3 Embedding 4B** |
| Result | ✅ **PASS** |

---

### Check 2: LLM MODEL

| Field | Value |
|-------|-------|
| Check | LLM model verified |
| Pass Criteria | Claude Opus 4.6 (`claude-opus-4-6`) |
| Location | Admin Panel → Settings → LLM Preference |
| Actual | **Anthropic: Claude Opus 4.6 (OpenRouter)** |
| Result | ✅ **PASS** |

---

### Check 3: #PinnedDocs

| Field | Value |
|-------|-------|
| Check | 4 documents present at current season version |
| Pass Criteria | SharedKernel, BEST-PRACTICES, PROTOCOLS, CCC @ v3.X.X.X |
| Location | Workspace settings → Pinned documents |

| # | Document | Expected | Actual | Result |
|---|----------|----------|--------|--------|
| 1 | SharedKernel | v3.X.X.X | **v3.1.2.1** | ✅ PASS |
| 2 | BEST-PRACTICES | v3.X.X.X | **v3.1.2.1** | ✅ PASS |
| 3 | PROTOCOLS | v3.X.X.X | **v3.1.1.2** | ✅ PASS |
| 4 | CCC | v3.X.X.X | **v3.1.2.1** | ✅ PASS |

| Result | ✅ **PASS** |
|--------|------------|

---

### Check 4: SYSTEM PROMPT

| Field | Value |
|-------|-------|
| Check | Season tag + INSTANCE IDENTITY block present |
| Pass Criteria | `#WeOwnSeason003 🚀` + INSTANCE IDENTITY as FIRST section (R-213) |
| Location | Admin Panel → System Prompt |

| Sub-Check | Expected | Actual | Result |
|-----------|----------|--------|--------|
| Season tag | `#WeOwnSeason003 🚀` | ✅ Present | ✅ PASS |
| INSTANCE IDENTITY block (R-213) | Instance ID, Name, Type, Owner(s), Season | ✅ INT-E01, ETHDenver.CCC.bot, Event, @GTM, S003 | ✅ PASS |
| INSTANCE IDENTITY = FIRST section | Before Ecosystem Identity | ✅ First section | ✅ PASS |

| Result | ✅ **PASS** |
|--------|------------|

---

### Check 5: WORKSPACE PROMPTS + CONFIG

| Field | Value |
|-------|-------|
| Check | Workspace prompts + config verified |
| Pass Criteria | BP-053 (Non-CCC restriction) + BP-054 (CCC-ID logic) + BP-061 (#WorkspaceChatHistory = 40) |

| Sub-Check | Workspace | Expected | Actual | Result |
|-----------|-----------|----------|--------|--------|
| BP-054 | CCC | CCC-ID logic present | ✅ Present | ✅ PASS |
| BP-053 | events | Restriction block present | ✅ Present | ✅ PASS |
| BP-061 | CCC | ChatHistory = 40 | ✅ **40** | ✅ PASS |
| BP-061 | events | ChatHistory = 40 | ✅ **40** | ✅ PASS |

> INT-E01 = Event instance. ALL workspaces enforced (same scoping as INT-Pxx per BP-062).

| Result | ✅ **PASS** |
|--------|------------|

---

### Check 6: USER-IDENTITY

| Field | Value |
|-------|-------|
| Check | Owner(s) USER-IDENTITY current for season |
| Pass Criteria | BP-058 — current season field |
| Location | `_USERS_/` in RAG |

| CCC | Document | Version | Season | Result |
|-----|----------|---------|--------|--------|
| N/A | N/A — Event instance | N/A | N/A | ✅ PASS |

> **Ruling:** INT-E01 = ephemeral event instance (R-214). Users are demo accounts only (DMO, ETH). BP-058 USER-IDENTITY requirement = N/A for event instances with demo-only users.

| Result | ✅ **PASS** |
|--------|------------|

---

### Check 7: RAG SYNC

| Field | Value |
|-------|-------|
| Check | Documents current and accessible |
| Pass Criteria | Core docs accessible + current version |
| Location | RAG embedded documents |

| Connector | Source | Last Refresh | Result |
|-----------|-------|-------------|--------|
| Manual upload | #PinnedDocs (4 docs) | 2026-02-13 | ✅ PASS |
| Verification | SharedKernel v3.1.2.1 confirmed via #ContextVolley | DMO_2026-W07_004 | ✅ PASS |

| Result | ✅ **PASS** |
|--------|------------|

---

### Check 8: #ContextVolley

| Field | Value |
|-------|-------|
| Check | Can send/receive #ContextVolley |
| Pass Criteria | Successful #ContextVolley delivery + ACK |
| Method | INT-OG1 → INT-E01 → ACK |

| Sub-Check | Expected | Actual | Result |
|-----------|----------|--------|--------|
| Volley sent | ✅ Delivered | ✅ INT-OG1 → INT-E01 | ✅ PASS |
| ACK received | ✅ From INT-E01 | ✅ DMO_2026-W07_004 | ✅ PASS |

| Result | ✅ **PASS** |
|--------|------------|

---

## 📋 Results Summary

| # | Check | Result |
|---|-------|--------|
| 1 | EMBEDDER | ✅ PASS |
| 2 | LLM MODEL | ✅ PASS |
| 3 | #PinnedDocs | ✅ PASS |
| 4 | SYSTEM PROMPT | ✅ PASS |
| 5 | WORKSPACE PROMPTS + CONFIG | ✅ PASS |
| 6 | USER-IDENTITY | ✅ PASS (N/A — event instance) |
| 7 | RAG SYNC | ✅ PASS |
| 8 | #ContextVolley | ✅ PASS |

| Field | Value |
|-------|-------|
| PASSED | **8/8** |
| FAILED | **0/8** |
| **STATUS** | ✅ **CERTIFIED** |

---

## 📋 Attestation

| Field | Value |
|-------|-------|
| **RESULT** | ✅ **CERTIFIED — 8/8** |
| Score | **100%** |
| Certifier | @GTM |
| Witnessed By | LiveStream audience |
| Date | 2026-02-13 |
| REF | GTM_2026-W07_277 |
| Instance | INT-E01 |

### Attestation Chain

| Step | Actor | CCC-ID | Action |
|------|-------|--------|--------|
| 1 | @GTM | GTM_2026-W07_216 | PRJ-009 #masterCCC |
| 2 | @SHD | — | Droplet + Docker + DNS + SSL (Signal) |
| 3 | @GTM | GTM_2026-W07_256 | Embedder configured |
| 4 | @GTM | GTM_2026-W07_266 | System Prompt + CCC Prompt APPROVED |
| 5 | @GTM | GTM_2026-W07_269 | #PinnedDocs uploaded |
| 6 | @GTM | GTM_2026-W07_271 | events Prompt APPROVED |
| 7 | @GTM | GTM_2026-W07_276 | Demo users created |
| 8 | @GTM | GTM_2026-W07_277 | #SmokeTest + ISC call start |
| 9 | @GTM | GTM_2026-W07_279 | ISC Checks 1-2 VERIFIED |
| 10 | @GTM | GTM_2026-W07_280 | ISC Checks 3-6 BATCH CONFIRMED |
| 11 | AI:@DMO | DMO_2026-W07_004 | #ContextVolley ACK (Check 7+8) |
| 12 | AI:@DMO | DMO_2026-W07_004 | DEEP FULL VSA — #PinnedDocs (27/27) |
| 13 | @GTM | GTM_2026-W07_285 | ISC ATTESTATION generated |

---

## 📋 Additional Notes

| Field | Value |
|-------|-------|
| Workspaces | CCC (🤝) + events (📆) |
| Users | a-gtm_dev, a-rmn_dev, u-demo_user, u-eth_user |
| First CCC-ID | DMO_2026-W07_004 |
| First VSA | 27/27 PASS (advisory: 6 stale cross-refs — cosmetic) |
| Mobile verified | iPhone 12 + Chrome ✅ |
| LiveStreamed | ✅ |
| Event | ETHDenver 2026 (Feb 17-22) |
| Decommission | R-214 — Sun 08 Mar 2026 |

---

## 📋 Related Documents

| Document | Version | Relevance |
|----------|---------|-----------|
| PRJ-009_FedArchExpansion_ETHDenver-CCC-bot | v3.1.2.1 | Project document |
| TMPL-010_ISC | v3.1.2.1 | ISC template |
| GUIDE-009_SmokeTest | v3.1.1.1 | Post-deployment verification |
| SharedKernel | v3.1.2.1 | Governance source of truth |

---

## 📋 Version History

| Version | Date | #masterCCC | Approval | Changes |
|---------|------|------------|----------|---------|
| 3.1.2.1 | 2026-W07 | GTM_2026-W07_277 | GTM_2026-W07_287 | Initial ISC attestation; 8/8 CERTIFIED; Event instance (INT-Exx); Check #6 N/A ruling for demo-only users; 13-step attestation chain; LiveStream witnessed; mobile verified |

---

#FlowsBros #FedArch #ISC #ETHDenver2026 #WeOwnSeason003

♾️ WeOwnNet 🌐 | 🏡 Real Estate and 🤝 cooperative ownership for everyone. An 🤗 inclusive community, by 👥 invitation only.
