# AI Engineer Playbook
## Chapter 22

# AIE Risk Management

> *"The AIE participates in risk management. The 4 risk pillars, the 3 risk tiers, and the 5-criterion risk quality bar; the AIE's job is to identify risks, own the mitigation, and contribute to the risk register."*

---

## 1. Epigraph

_The AIE participates in risk management. The 4 risk pillars, the 3 risk tiers, and the 5-criterion risk quality bar; the AIE's job is to identify risks, own the mitigation, and contribute to the risk register._

---

## 2. Problem

You are an AIE at acme-corp. The engineering manager has just told you: "aie risk management. 30-day timeline."

This chapter tells you the 4 mental models, 3 frameworks, and 5-criterion quality bar.

**Decision in one sentence:** _AIE risk participation is a 4-pillar system + 3 risk tiers + 5-criterion bar; the AIE's job is to identify risks, own the mitigation, and contribute to the risk register._

---

## 3. Why AIEs Fail Here

Five named failure modes of AIEs whose aie risk management produced zero results.

- **The No-Risk-Awareness Failure.** No risk awareness.
- **The No-Mitigation Failure.** Risks identified, no mitigation.
- **The No-Risk-Owner Failure.** No risk owner.
- **The Verbals-Only Failure.** Risks are verbal.
- **The No-Risk-Register Failure.** No register.

---

## 4. Mental Models

Four mental models that compress aie risk management.

**mental model 1: The 4 Risk Pillars:** 4 pillars: feature + eval + safety + cost.

**mental model 2: The 3 Risk Tiers:** 3 tiers: HIGH + MEDIUM + LOW.

**mental model 3: The 5-Criterion Bar:** 5 criteria: tracked + owned + timed + mitigated + reviewed.

**mental model 4: The Risk Register Template:** Per-risk detail.

---

## 5. Frameworks

Three frameworks for aie risk management.

### Framework 1: The 1-Page Plan

```
# AIE Risk Management - [Date]

## Top 3 strategic inputs
1. [Input 1]
2. [Input 2]
3. [Input 3]

## The 5-criterion bar applied

## The 1 thing the AIE will NOT compromise on
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

You are an AIE at **acme-corp**. The engineering manager has given you 30 days to design the aie risk management system.

You have **90 minutes**. Produce the **aie risk management redesign** using the 3 frameworks above. Specify:

- The 1-page plan.
- The implementation tracker.
- The retrospective review template.
- The 30-day timeline.
- The 1 thing you'll say to the engineering manager in the first review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-22-aie-aie-risk.md` - under 1500 words.

---

## 7. Worked Example

**The 1-page risk register:**

```
# AIE Risk Register - 2026

## Top 5 risks
1. Jailbreak success (HIGH) - Owner: AIE
```

---

## 8. Failure Mode Postmortem

An AIE at a 200-person B2B AI company had no risk awareness. Jailbreak successful. Customer data leaked. The CTO said: 'No risk register, no LLM in production.'

What the first AIE missed: aie risk management is a system. The first AIE had no system. The second AIE had 4 mental models + 3 frameworks + 5 criteria. The system is the leverage.

The lesson: the AIE who has the system has aie risk management. The AIE who has no system has the failure mode.

---

## 9. Self-Assessment Rubric

| 1 | **4 risk pillars** | 0-1 | 2-3 | 4 pillars |
| 2 | **3 risk tiers** | 1 | 2 | 3 tiers |
| 3 | **5-criterion bar** | 0-2 | 3-4 | 5 criteria |
| 4 | **Risks tracked** | <5 | 5-15 | 5+ per AIE |
| 5 | **HIGH-tier mitigation** | None | Partial | 100% mitigated within 30 days |


**Disqualifier:** any 1 on dimension 1 or 3. An AIE who has 0-1 pillars or 1 tier is in the No-Risk-Awareness or No-Risk-Owner failure mode.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-22-aie-aie-risk.md` - interview evidence for "Walk me through your risk participation." (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through your risk participation.**
2. **Jailbreak was successful. What do you do?**
3. **Eval is not catching quality issues. What do you do?**
4. **Cost overrun. What do you do?**
5. **Walk me through a HIGH-tier risk mitigation you've led.**
