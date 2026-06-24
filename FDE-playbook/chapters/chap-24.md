# Forward Deployed Engineer Playbook
## Chapter 24

# Regulatory Compliance for FDEs

> *"The FDE deploys to customers in regulated industries. The 4-tier compliance model, the 5-regulation landscape, the 3 documentation artifacts, and the 12-month compliance roadmap are the FDE's reference for regulatory compliance."*

---

## 1. Epigraph

_The FDE deploys to customers in regulated industries. The 4-tier compliance model, the 5-regulation landscape, the 3 documentation artifacts, and the 12-month compliance roadmap are the FDE's reference for regulatory compliance._

---

## 2. Problem

You are an FDE at acme-corp. The customer's CCO has just told you: "We have 4 regulatory frameworks (GDPR, HIPAA, SOC 2, EU AI Act). We have 60 days to demonstrate compliance. The 4-tier compliance model is unclear. The 5-regulation landscape is undecided. We need 3 documentation artifacts. What do you do?"

This chapter tells you the 4 tiers, the 5 regulations, the 3 artifacts, and the 12-month roadmap.

**Decision in one sentence:** _FDE regulatory compliance is a 4-tier model (must-have-now, must-have-next-market, nice-to-have-future, no-need) applied to 5 regulations (GDPR, HIPAA, SOC 2, EU AI Act, ISO 27001) with 3 documentation artifacts (DPIA, audit trail, compliance report) and a 12-month roadmap; the FDE's job is to design the compliance framework, implement the must-have tiers, and document for audit._

---

## 3. Why FDEs Fail Here

Five named failure modes of FDEs whose compliance produced zero results.

- **The All-At-Once Failure.** The FDE tries to comply with all frameworks at once. _Nothing is compliant._
- **The No-Tier-Prioritization Failure.** The FDE treats all frameworks equally. _Wastes time on nice-to-haves._
- **The No-Documentation Failure.** The FDE builds compliance but doesn't document. _Audit fails._
- **The 1-Time-Compliance Failure.** The FDE only complies at audit time. _Audit fails annually._
- **The No-Ownership Failure.** The FDE doesn't own the compliance. _No one owns it._

---

## 4. Mental Models

Four mental models that compress regulatory compliance.

**mental model 1: The 4-Tier Compliance Model.** 4 tiers.

```mermaid
%% Figure 24.1 — The 4-tier compliance model
flowchart TB
    T1[Tier 1: Must-have NOW<br/>Current business<br/>SOC 2, GDPR, HIPAA]
    T2[Tier 2: Must-have NEXT market<br/>Next 12-18 months<br/>ISO 27001, EU AI Act]
    T3[Tier 3: Nice-to-have FUTURE<br/>Future business<br/>PCI-DSS, HITRUST]
    T4[Tier 4: NO NEED<br/>Not relevant<br/>FedRAMP (for non-US-gov)]
    T1 --> Compliance
    T2 --> Compliance
    T3 --> Compliance
    T4 --> Compliance
    Compliance{Compliance<br/>4-tier system}
```

**The 4 tiers:**
- **Tier 1: Must-have NOW.** Current business. SOC 2, GDPR, HIPAA.
- **Tier 2: Must-have NEXT market.** Next 12-18 months. ISO 27001, EU AI Act.
- **Tier 3: Nice-to-have FUTURE.** Future business. PCI-DSS, HITRUST.
- **Tier 4: NO NEED.** Not relevant. FedRAMP (for non-US-gov).

**mental model 2: The 5-Regulation Landscape.** 5 regulations.

```
1. GDPR (EU, privacy, 72-hour breach notification)
2. HIPAA (US, healthcare PHI, 60-day breach notification)
3. SOC 2 (US/global, security audit, annual)
4. EU AI Act (EU, AI systems, 2026-2027 enforcement)
5. ISO 27001 (global, information security, annual)

The 5 regulations cover most customer requirements.
APAC-specific (PDPA, APPI) and other are extensions.
```

**mental model 3: The 3 Documentation Artifacts.** 3 artifacts.

```
Artifact 1: Data Protection Impact Assessment (DPIA)
- Required for GDPR high-risk processing
- 1 page, refreshed annually
- Owned by: FDE + DPO

Artifact 2: Audit Trail
- Every access + every change
- Immutable, 7-year retention
- Owned by: FDE + CISO

Artifact 3: Compliance Report
- Per regulation, refreshed quarterly
- 1 page per regulation (SOC 2, GDPR, etc.)
- Owned by: FDE + Compliance team
```

**mental model 4: The 12-Month Compliance Roadmap.** Roadmap.

```
Month 1-3: Tier 1 must-have
- SOC 2 Type II: kickoff + evidence collection
- GDPR DPIA: drafted
- HIPAA risk assessment: drafted

Month 4-6: Tier 1 audit prep
- SOC 2 Type II: audit week
- GDPR: documented
- HIPAA: validated

Month 7-9: Tier 2 next market
- ISO 27001: kickoff
- EU AI Act: AI risk classification

Month 10-12: Tier 2 audit prep
- ISO 27001: audit week
- EU AI Act: documented
```

---

## 5. Frameworks

Three frameworks for regulatory compliance.

### Framework 1: The 1-Page Compliance Plan

```
# Compliance Plan — [Customer] — [Date]

## The 4 tiers
- Tier 1 (Must-have NOW): [Frameworks]
- Tier 2 (Must-have NEXT market): [Frameworks]
- Tier 3 (Nice-to-have FUTURE): [Frameworks]
- Tier 4 (NO NEED): [Frameworks]

## The 5 regulations
1. GDPR: [Status]
2. HIPAA: [Status]
3. SOC 2: [Status]
4. EU AI Act: [Status]
5. ISO 27001: [Status]

## The 3 documentation artifacts
1. DPIA: [Status]
2. Audit trail: [Status]
3. Compliance report: [Status]

## The 1 thing the FDE will push back on
[1 sentence.]
```

### Framework 2: The Tier-by-Tier Compliance Matrix

```
# Compliance Matrix — [Customer] — [Date]

| Framework | Tier | Status | Owner | Audit date |
|-----------|------|--------|-------|------------|
| GDPR | T1 | [Status] | [Owner] | [Date] |
| HIPAA | T1 | [Status] | [Owner] | [Date] |
| SOC 2 | T1 | [Status] | [Owner] | [Date] |
| EU AI Act | T2 | [Status] | [Owner] | [Date] |
| ISO 27001 | T2 | [Status] | [Owner] | [Date] |
| PCI-DSS | T3 | [Status] | [Owner] | [Date] |
| HITRUST | T3 | [Status] | [Owner] | [Date] |
| FedRAMP | T4 | N/A | N/A | N/A |

## The 1 thing the FDE will focus on this quarter
[1 sentence.]
```

### Framework 3: The 12-Month Compliance Roadmap

```
# 12-Month Compliance Roadmap — [Customer] — [Date]

## Month 1-3: Tier 1 must-have
- [Framework 1]: kickoff + evidence collection
- [Framework 2]: kickoff + DPIA drafted
- [Framework 3]: kickoff + risk assessment

## Month 4-6: Tier 1 audit prep
- [Framework 1]: audit week
- [Framework 2]: documented
- [Framework 3]: validated

## Month 7-9: Tier 2 next market
- [Framework 4]: kickoff
- [Framework 5]: AI risk classification

## Month 10-12: Tier 2 audit prep
- [Framework 4]: audit week
- [Framework 5]: documented

## The 1 thing the FDE will NOT delay
[1 sentence.]
```

---

## 6. Drill

You are an FDE at **acme-corp**. The customer's CCO has given you 60 days.

```
Customer:
- 4 frameworks: GDPR, HIPAA, SOC 2, EU AI Act
- 60 days
- 3 documentation artifacts needed
- Audit week: Day 60

You have 60 days.
```

You have **90 minutes**. Produce the **compliance plan** (`portfolio/chapter-24-regulatory-compliance.md`) using Framework 1 (Compliance Plan) + Framework 2 (Compliance Matrix) + Framework 3 (12-Month Roadmap). Specify:

- The 1-page compliance plan (4 tiers, 5 regulations, 3 artifacts, the 1 pushback).
- The compliance matrix (8 frameworks, tier, status, owner, audit date).
- The 12-month roadmap (4 quarters, the 1 not delay).
- The 60-day timeline (week-by-week).
- The 1 thing you'll say to the CCO in the first review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-24-regulatory-compliance.md` — under 1500 words.

---

## 7. Worked Example

**The 1-page compliance plan:**

```
# Compliance Plan — Customer A — 2026-09-01

## The 4 tiers
- Tier 1 (Must-have NOW): SOC 2, GDPR, HIPAA
- Tier 2 (Must-have NEXT market): EU AI Act, ISO 27001
- Tier 3 (Nice-to-have FUTURE): PCI-DSS, HITRUST
- Tier 4 (NO NEED): FedRAMP (not US gov)

## The 5 regulations
1. GDPR: Tier 1 — In progress (DPIA drafted)
2. HIPAA: Tier 1 — In progress (risk assessment drafted)
3. SOC 2: Tier 1 — Audit week Q4 2026
4. EU AI Act: Tier 2 — AI risk classification in progress
5. ISO 27001: Tier 2 — Kickoff Q1 2027

## The 3 documentation artifacts
1. DPIA: GDPR — drafted, Q4 2026
2. Audit trail: SOC 2 — automated, daily
3. Compliance report: SOC 2 + GDPR — quarterly

## The 1 thing the FDE will push back on
EU AI Act Tier 2 timing. The customer wants Tier 2
EU AI Act compliance by Q4 2026. The FDE will push
for Q2 2027 (the EU AI Act enforcement date is 2027).
```

**The compliance matrix:**

```
# Compliance Matrix — Customer A — 2026-09-01

| Framework | Tier | Status | Owner | Audit date |
|-----------|------|--------|-------|------------|
| GDPR | T1 | In progress | FDE + DPO | Q4 2026 |
| HIPAA | T1 | In progress | FDE + Compliance | Q4 2026 |
| SOC 2 | T1 | Audit prep | FDE + CISO | Q4 2026 |
| EU AI Act | T2 | Planning | FDE + Legal | Q2 2027 |
| ISO 27001 | T2 | Kickoff Q1 | FDE + CISO | Q4 2027 |
| PCI-DSS | T3 | Not started | TBD | Q1 2028 |
| HITRUST | T3 | Not started | TBD | Q2 2028 |
| FedRAMP | T4 | N/A | N/A | N/A |

## The 1 thing the FDE will focus on this quarter
SOC 2 Type II audit prep. The audit is in 60 days.
SOC 2 is the highest-priority Tier 1 framework.
```

**The 12-month roadmap:**

```
# 12-Month Compliance Roadmap — Customer A — 2026-09-01

## Month 1-3 (Q4 2026): Tier 1 must-have
- SOC 2 Type II: kickoff + evidence collection
- GDPR DPIA: drafted + reviewed
- HIPAA risk assessment: drafted + reviewed

## Month 4-6 (Q1 2027): Tier 1 audit prep
- SOC 2 Type II: audit week (Dec 2026)
- GDPR: documented + DPIA refreshed
- HIPAA: validated

## Month 7-9 (Q2 2027): Tier 2 next market
- EU AI Act: AI risk classification + documentation
- ISO 27001: kickoff + gap analysis

## Month 10-12 (Q3 2027): Tier 2 audit prep
- ISO 27001: audit week (Q4 2027)
- EU AI Act: documented for 2027 enforcement

## The 1 thing the FDE will NOT delay
SOC 2 audit prep. The audit is in 60 days. Tier 1
audit slip = customer trust loss + deal slip.
```

**The 60-day timeline:**

```
# 60-Day Compliance Timeline — Customer A — 2026-09-01

## Week 1-2: Assessment
- [x] 4 tiers defined
- [x] 5 regulations scoped
- [x] 3 artifacts identified
- [x] Compliance matrix built

## Week 3-6: Tier 1 documentation
- [ ] SOC 2 evidence collection (automated)
- [ ] GDPR DPIA drafted + reviewed
- [ ] HIPAA risk assessment drafted + reviewed

## Week 7-9: Audit prep
- [ ] SOC 2 audit week (Dec 2026)
- [ ] GDPR compliance report
- [ ] HIPAA compliance report

## Week 10: Audit
- [ ] SOC 2 Type II audit (Dec 2026)
```

**The 1 thing I'll say to the CCO in the first review:**

```
"Here's the compliance plan for Customer A:

  4 tiers:
  - Tier 1 (NOW): SOC 2, GDPR, HIPAA
  - Tier 2 (NEXT): EU AI Act, ISO 27001
  - Tier 3 (FUTURE): PCI-DSS, HITRUST
  - Tier 4 (NO NEED): FedRAMP

  5 regulations:
  - SOC 2: Tier 1, audit Q4 2026
  - GDPR: Tier 1, DPIA drafted
  - HIPAA: Tier 1, risk assessment drafted
  - EU AI Act: Tier 2, AI risk classification Q2 2027
  - ISO 27001: Tier 2, audit Q4 2027

  3 artifacts:
  - DPIA: drafted, refreshed Q4 2026
  - Audit trail: automated, daily
  - Compliance report: quarterly

  The 1 thing I want to push back on: EU AI Act Tier 2
  timing. The customer wants Q4 2026. The FDE wants
  Q2 2027 (the EU AI Act enforcement date is 2027).

  The 12-month roadmap is on track. The 60-day audit
  prep is the priority. Tier 1 is the focus.

  Compliance is the discipline. Customer trust is the
  outcome."
```

**The 3 things I'll do to avoid the 5 failure modes:**

```
1. Prioritize Tier 1 (must-have NOW).
   (Avoids the All-At-Once Failure.)
   - Tier 1: SOC 2 + GDPR + HIPAA (60-day focus)
   - Tier 2: Q1 2027 (after Tier 1 validated)
   - Tier 3: Q1 2028 (after Tier 2 validated)

2. Document continuously (not just at audit).
   (Avoids the 1-Time-Compliance Failure.)
   - Daily: audit trail automated
   - Quarterly: compliance report
   - Annually: DPIA + risk assessment refreshed

3. Own the compliance (FDE + Compliance team).
   (Avoids the No-Ownership Failure.)
   - FDE owns Tier 1 implementation
   - Compliance team owns audit prep
   - DPO owns DPIA
   - CISO owns security controls
```

---

## 8. Failure Mode Postmortem

An FDE at a 200-person B2B AI company had a customer with 4 compliance frameworks. The FDE tried to comply with all 4 at once. Within 6 months: 0 frameworks compliant. The customer's enterprise customers churned. The customer's audit failed.

The replacement FDE did 3 things:
1. Prioritized Tier 1 (SOC 2 + GDPR + HIPAA) over Tier 2 (ISO 27001 + EU AI Act) over Tier 3 (PCI-DSS + HITRUST).
2. Documented continuously (daily audit trail, quarterly compliance report, annual DPIA).
3. Owned the compliance (FDE + Compliance team + DPO + CISO).

Within 12 months: SOC 2 Type II passed, GDPR DPIA documented, HIPAA risk assessment validated. 0 customer churn due to compliance.

What the first FDE missed: compliance is a tier system. The first FDE tried all-at-once. The second FDE prioritized Tier 1 → Tier 2 → Tier 3. The tier system is the leverage.

The lesson: the FDE who has the 4-tier model + 5-regulation landscape + 3 artifacts has a compliance system. The FDE who tries all-at-once has audit failure.

---

## 9. Self-Assessment Rubric

| # | Dimension | 1 (Novice) | 3 (Competent) | 5 (Expert) |
|---|---|---|---|---|
| 1 | **4-tier compliance model** | No tiers | 2-3 tiers | 4 tiers (must-have NOW / NEXT / FUTURE / NO NEED), per-customer |
| 2 | **5-regulation landscape** | 1-2 regulations | 3-4 regulations | 5 regulations (GDPR, HIPAA, SOC 2, EU AI Act, ISO 27001) |
| 3 | **3 documentation artifacts** | 0-1 artifacts | 2 artifacts | 3 artifacts (DPIA, audit trail, compliance report), continuously maintained |
| 4 | **12-month roadmap** | No roadmap | Roadmap exists | 4 quarters, Tier 1 → Tier 2 → Tier 3, with audit dates |
| 5 | **Compliance ownership** | No owner | Single owner | FDE + Compliance team + DPO + CISO, each owning their part |

**Disqualifier:** any 1 on dimension 1 or 3. An FDE who has no tiers or 0-1 artifacts is in the All-At-Once or No-Documentation failure mode.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-24-regulatory-compliance.md` — interview evidence for "How do you design regulatory compliance?" (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through a compliance framework you've designed.**
2. **The customer has 4 frameworks. How do you prioritize?**
3. **The audit is in 60 days. What do you do?**
4. **A new regulation (EU AI Act) is added. How do you tier it?**
5. **Walk me through a compliance audit you've passed.**
