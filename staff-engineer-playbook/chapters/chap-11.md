# Staff Engineer Playbook
## Chapter 11

# Technical Debt Management

> *"The SE manages tech debt. The 4-tech-debt-pillar framework (catalog + prioritize + paydown + prevent), the 3-tech-debt templates (code + architecture + test), and the 5-criterion tech debt quality bar are the SE's reference for tech debt at the principal IC level."*

---

## 1. Epigraph

_The SE manages tech debt. The 4-tech-debt-pillar framework (catalog + prioritize + paydown + prevent), the 3-tech-debt templates (code + architecture + test), and the 5-criterion tech debt quality bar are the SE's reference for tech debt at the principal IC level._

---

## 2. Problem

You are a Staff Engineer at acme-corp. The engineering director has just told you: "technical debt management. 30-day timeline."

This chapter tells you the 4 mental models, 3 frameworks, and 5-criterion quality bar.

**Decision in one sentence:** _SE tech debt management is a 4-pillar framework + 3 templates + 5-criterion bar; the SE's job is to catalog tech debt, prioritize, paydown, and prevent new debt._

---

## 3. Why Staff Engineers Fail Here

Five named failure modes of Staff Engineers whose technical debt management produced zero results.

- **The No-Tech-Debt-Catalog Failure.** No tech debt catalog.
- **The No-Prioritization Failure.** No prioritization.
- **The No-Paydown Failure.** No paydown.
- **The No-Prevention Failure.** No prevention.
- **The Accumulating Failure.** Tech debt accumulating.

---

## 4. Mental Models

Four mental models that compress technical debt management.

**mental model 1: The 4 Tech Debt Pillars:** 4 pillars: catalog + prioritize + paydown + prevent.

**mental model 2: The 3 Tech Debt Templates:** 3 templates: code + architecture + test.

**mental model 3: The 5-Criterion Bar:** 5 criteria: cataloged + prioritized + paid-down + prevented + measured.

**mental model 4: The Tech Debt Tracker:** Per-item tracker.

---

## 5. Frameworks

Three frameworks for technical debt management.

### Framework 1: The 1-Page Plan

```
# Technical Debt Management - [Date]

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

You are a Staff Engineer at **acme-corp**. The engineering director has given you 30 days to design the technical debt management system.

You have **90 minutes**. Produce the **technical debt management redesign** using the 3 frameworks above. Specify:

- The 1-page plan.
- The implementation tracker.
- The retrospective review template.
- The 30-day timeline.
- The 1 thing you'll say to the engineering director in the first review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-11-se-se-tech-debt.md` - under 1500 words.

---

## 7. Worked Example

**The 1-page tech debt tracker:**

```
# Tech Debt Tracker - Q3 2026

| Item | Priority | Owner | Status |
|------|----------|-------|--------|
| Migrate to TS | HIGH | SE-A | TODO |
```

---

## 8. Failure Mode Postmortem

An SE at a 200-person company had no tech debt catalog. Velocity dropped 30%. The VP Eng said: 'No debt catalog, no velocity.'

What the first Staff Engineer missed: technical debt management is a system. The first SE had no system. The second SE had 4 mental models + 3 frameworks + 5 criteria. The system is the leverage.

The lesson: the SE who has the system has technical debt management. The SE who has no system has the failure mode.

---

## 9. Self-Assessment Rubric

| 1 | **4 tech debt pillars** | 0-1 | 2-3 | 4 pillars |
| 2 | **3 templates** | 1 | 2 | 3 templates |
| 3 | **5-criterion bar** | 0-2 | 3-4 | 5 criteria |
| 4 | **Tech debt items tracked** | <10 | 10-50 | 50+ |
| 5 | **Paydown rate** | 0/year | 1-5/year | 10+/year |


**Disqualifier:** any 1 on dimension 1 or 3. An SE who has no catalog or no paydown is in the No-Tech-Debt-Catalog or No-Paydown failure mode.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-11-se-se-tech-debt.md` - interview evidence for "Walk me through your tech debt management." (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through your tech debt management.**
2. **Velocity is dropping. What do you do?**
3. **You have 10 tech debt items. How do you prioritize?**
4. **The team is overwhelmed by tech debt. What do you do?**
5. **Walk me through a tech debt paydown you've led.**
