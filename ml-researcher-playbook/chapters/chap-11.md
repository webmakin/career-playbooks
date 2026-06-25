# ML Researcher Playbook
## Chapter 11

# Architecture Decisions for MLRs

> *"The MLR makes architecture decisions. The 4-factor decision framework (novelty + complexity + cost + reproducibility), the 3-decision templates (model + training + inference), and the 5-criterion architecture quality bar are the MLR's reference for architecture decisions at the contributor level."*

---

## 1. Epigraph

_The MLR makes architecture decisions. The 4-factor decision framework (novelty + complexity + cost + reproducibility), the 3-decision templates (model + training + inference), and the 5-criterion architecture quality bar are the MLR's reference for architecture decisions at the contributor level._

---

## 2. Problem

You are an MLR at acme-corp. The senior scientist has just told you: "architecture decisions for mlrs. 30-day timeline."

This chapter tells you the 4 mental models, 3 frameworks, and 5-criterion quality bar.

**Decision in one sentence:** _MLR architecture decisions is a 4-factor framework + 3 decision templates + 5-criterion bar; the MLR's job is to design architectures, validate them with experiments, and own the architecture quality._

---

## 3. Why MLRs Fail Here

Five named failure modes of MLRs whose architecture decisions for mlrs produced zero results.

- **The No-Novelty Failure.** Re-inventing Transformer. No novelty.
- **The Over-Complex Failure.** Architecture too complex. Can't reproduce.
- **The No-Cost-Analysis Failure.** No cost analysis.
- **The No-Decision-Log Failure.** Decisions not documented.
- **The Stake-Not-Ballast Failure.** Architecture chosen without experiments.

---

## 4. Mental Models

Four mental models that compress architecture decisions for mlrs.

**mental model 1: The 4 Architecture Factors:** 4 factors: novelty + complexity + cost + reproducibility.

**mental model 2: The 3 Decision Templates:** 3 templates: model + training + inference.

**mental model 3: The 5-Criterion Bar:** 5 criteria: novel + simple + cost-effective + reproducible + validated.

**mental model 4: The Architecture ADR:** Architecture Decision Record template.

---

## 5. Frameworks

Three frameworks for architecture decisions for mlrs.

### Framework 1: The 1-Page Plan

```
# Architecture Decisions for MLRs - [Date]

## Top 3 strategic inputs
1. [Input 1]
2. [Input 2]
3. [Input 3]

## The 5-criterion bar applied

## The 1 thing the MLR will NOT compromise on
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

You are an MLR at **acme-corp**. The senior scientist has given you 30 days to design the architecture decisions for mlrs system.

You have **90 minutes**. Produce the **architecture decisions for mlrs redesign** using the 3 frameworks above. Specify:

- The 1-page plan.
- The implementation tracker.
- The retrospective review template.
- The 30-day timeline.
- The 1 thing you'll say to the senior scientist in the first review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-11-mlr-mlr-architecture.md` - under 1500 words.

---

## 7. Worked Example

**The 1-page architecture ADR:**

```
# Architecture ADR - 2026-09-01

## Decision
Use Mamba over Transformer for B2B AI

## Factors
- Novelty: HIGH
- Complexity: MEDIUM
- Cost: 5x reduction
```

---

## 8. Failure Mode Postmortem

An MLR at a 200-person B2B AI company made architecture decisions without experiments. The senior scientist asked: 'Why Mamba?' The MLR had no answer.

What the first MLR missed: architecture decisions for mlrs is a system. The first MLR had no system. The second MLR had 4 mental models + 3 frameworks + 5 criteria. The system is the leverage.

The lesson: the MLR who has the system has architecture decisions for mlrs. The MLR who has no system has the failure mode.

---

## 9. Self-Assessment Rubric

| 1 | **4 architecture factors** | 0-1 | 2-3 | 4 factors |
| 2 | **3 templates** | 1 | 2 | 3 templates |
| 3 | **5-criterion bar** | 0-2 | 3-4 | 5 criteria |
| 4 | **ADRs per year** | 0 | 1-2 | 5+ |
| 5 | **Architecture validation** | None | Partial | 100% with experiments |


**Disqualifier:** any 1 on dimension 1 or 3. An MLR who has no novelty or over-complex is in the No-Novelty or Over-Complex failure mode.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-11-mlr-mlr-architecture.md` - interview evidence for "Walk me through your architecture decisions." (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through your architecture decision process.**
2. **Your architecture is too complex. What do you do?**
3. **The cost is too high. What do you do?**
4. **You have 3 architecture options. How do you prioritize?**
5. **Walk me through an architecture decision you've made.**
