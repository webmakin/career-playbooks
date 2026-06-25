# Staff Engineer Playbook
## Chapter 22

# Engineering Risk Management

> *"The SE participates in risk management. The 4 risk pillars, the 3 risk tiers, and the 5-criterion risk quality bar; the SE's job is to identify risks, own the mitigation, and contribute to the risk register."*

---

## 1. Epigraph

_The SE participates in risk management. The 4 risk pillars, the 3 risk tiers, and the 5-criterion risk quality bar; the SE's job is to identify risks, own the mitigation, and contribute to the risk register._

---

## 2. Problem

You are a Staff Engineer at acme-corp. The engineering director has just told you: "engineering risk management. 30-day timeline."

This chapter tells you the 4 mental models, 3 frameworks, and 5-criterion quality bar.

**Decision in one sentence:** _SE engineering risk participation is a 4-pillar system + 3 risk tiers + 5-criterion bar; the SE's job is to identify risks, own the mitigation, and contribute to the risk register._

---

## 3. Why Staff Engineers Fail Here

Five named failure modes of Staff Engineers whose engineering risk management produced zero results.

- **The No-Risk-Awareness Failure.** No risk awareness.
- **The No-Mitigation Failure.** Risks identified, no mitigation.
- **The No-Risk-Owner Failure.** No risk owner.
- **The Verbals-Only Failure.** Risks are verbal.
- **The No-Risk-Register Failure.** No register.

---

## 4. Mental Models

Four mental models that compress engineering risk management.

**mental model 1: The 4 Risk Pillars:** 4 pillars: architecture + reliability + migration + tech debt.

**mental model 2: The 3 Risk Tiers:** 3 tiers: HIGH + MEDIUM + LOW.

**mental model 3: The 5-Criterion Bar:** 5 criteria: tracked + owned + timed + mitigated + reviewed.

**mental model 4: The Risk Register Template:** Per-risk detail.

---

## 5. Frameworks

Three frameworks for engineering risk management.

### Framework 1: The 1-Page Plan

```
# Engineering Risk Management - [Date]

## Top 3 strategic inputs
1. [Input 1]
2. [Input 2]
3. [Input 3]

## The 5-criterion bar applied

## The 1 thing the SE will NOT compromise on
[1 sentence.]
```

### Framework 2: The Implementation Tracker

```
# Implementation Tracker - [Quarter]

| Item | Owner | Status | Date |
|------|-------|--------|------|
| [Item 1] | [Name] | [Status] | [Date] |
| [Item 2] | ... | | |
```

### Framework 3: The Retrospective Review

```
# Retrospective Review - [Date]

## Top 3 wins
1. [Win 1]
2. [Win 2]
3. [Win 3]

## Top 3 challenges
1. [Challenge 1]
2. [Challenge 2]
3. [Challenge 3]
```

---

## 6. Drill

You are a Staff Engineer at **acme-corp**. The engineering director has given you 30 days to design the engineering risk management system.

You have **90 minutes**. Produce the **engineering risk management redesign** using the 3 frameworks above. Specify:

- The 1-page plan.
- The implementation tracker.
- The retrospective review template.
- The 30-day timeline.
- The 1 thing you'll say to the engineering director in the first review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-22-se-se-risk.md` - under 1500 words.

---

## 7. Worked Example

**The 1-page risk register:**

```
# SE Risk Register - 2026

## Top 5 risks
1. Postgres migration failure (HIGH) - Owner: SE
```

---

## 8. Failure Mode Postmortem

An SE at a 200-person company had no risk awareness. Postgres migration failed. Customer data lost. The VP Eng said: 'No risk register, no migration.'

What the first Staff Engineer missed: engineering risk management is a system. The first SE had no system. The second SE had 4 mental models + 3 frameworks + 5 criteria. The system is the leverage.

The lesson: the SE who has the system has engineering risk management. The SE who has no system has the failure mode.

---

## 9. Self-Assessment Rubric

| 1 | **4 risk pillars** | 0-1 | 2-3 | 4 pillars |
| 2 | **3 risk tiers** | 1 | 2 | 3 tiers |
| 3 | **5-criterion bar** | 0-2 | 3-4 | 5 criteria |
| 4 | **Risks tracked** | <5 | 5-15 | 5+ per SE |
| 5 | **HIGH-tier mitigation** | None | Partial | 100% mitigated within 30 days |


**Disqualifier:** any 1 on dimension 1 or 3. An SE who has 0-1 pillars or 1 tier is in the No-Risk-Awareness or No-Risk-Owner failure mode.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-22-se-se-risk.md` - interview evidence for "Walk me through your risk participation." (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through your risk participation.**
2. **Architecture decision has unknown risk. What do you do?**
3. **Production is failing. What do you do?**
4. **A migration is at risk. What do you do?**
5. **Walk me through a HIGH-tier risk mitigation you've led.**
