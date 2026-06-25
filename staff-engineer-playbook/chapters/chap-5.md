# Staff Engineer Playbook
## Chapter 5

# Architecture Design for Staff Engineers

> *"The SE designs architecture. The 4-design-pillar framework (requirements + trade-offs + decisions + validation), the 3-design templates (monolith + microservices + event-driven), and the 5-criterion architecture quality bar are the SE's reference for architecture at the principal IC level."*

---

## 1. Epigraph

_The SE designs architecture. The 4-design-pillar framework (requirements + trade-offs + decisions + validation), the 3-design templates (monolith + microservices + event-driven), and the 5-criterion architecture quality bar are the SE's reference for architecture at the principal IC level._

---

## 2. Problem

You are a Staff Engineer at acme-corp. The engineering director has just told you: "architecture design for staff engineers. 30-day timeline."

This chapter tells you the 4 mental models, 3 frameworks, and 5-criterion quality bar.

**Decision in one sentence:** _SE architecture design is a 4-pillar framework + 3 design templates + 5-criterion bar; the SE's job is to design architectures, validate them, and own the architecture quality._

---

## 3. Why Staff Engineers Fail Here

Five named failure modes of Staff Engineers whose architecture design for staff engineers produced zero results.

- **The No-Requirements Failure.** No requirements. Ad-hoc design.
- **The No-Trade-Offs Failure.** No trade-off analysis.
- **The No-Decision-Log Failure.** Decisions not documented.
- **The No-Validation Failure.** Architecture not validated.
- **The Stake-Not-Ballast Failure.** Architecture chosen without evidence.

---

## 4. Mental Models

Four mental models that compress architecture design for staff engineers.

**mental model 1: The 4 Architecture Pillars:** 4 pillars: requirements + trade-offs + decisions + validation.

**mental model 2: The 3 Design Templates:** 3 templates: monolith + microservices + event-driven.

**mental model 3: The 5-Criterion Bar:** 5 criteria: simple + scalable + cost-effective + reliable + documented.

**mental model 4: The Architecture ADR:** Architecture Decision Record template.

---

## 5. Frameworks

Three frameworks for architecture design for staff engineers.

### Framework 1: The 1-Page Plan

```
# Architecture Design for Staff Engineers - [Date]

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

You are a Staff Engineer at **acme-corp**. The engineering director has given you 30 days to design the architecture design for staff engineers system.

You have **90 minutes**. Produce the **architecture design for staff engineers redesign** using the 3 frameworks above. Specify:

- The 1-page plan.
- The implementation tracker.
- The retrospective review template.
- The 30-day timeline.
- The 1 thing you'll say to the engineering director in the first review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-05-se-se-architecture.md` - under 1500 words.

---

## 7. Worked Example

**The 1-page architecture ADR:**

```
# Architecture ADR - 2026-09-01

## Decision
Microservices on Kubernetes

## Trade-offs
- Cost: $50K/mo infra
- Scalability: 10x current
```

---

## 8. Failure Mode Postmortem

An SE at a 200-person company designed architectures without ADRs. Decisions lost. The VP Eng asked: 'Why microservices?' The SE had no answer.

What the first Staff Engineer missed: architecture design for staff engineers is a system. The first SE had no system. The second SE had 4 mental models + 3 frameworks + 5 criteria. The system is the leverage.

The lesson: the SE who has the system has architecture design for staff engineers. The SE who has no system has the failure mode.

---

## 9. Self-Assessment Rubric

| 1 | **4 architecture pillars** | 0-1 | 2-3 | 4 pillars |
| 2 | **3 templates** | 1 | 2 | 3 templates |
| 3 | **5-criterion bar** | 0-2 | 3-4 | 5 criteria |
| 4 | **ADRs per quarter** | 0 | 1-2 | 3+ |
| 5 | **Architecture validation** | None | Partial | 100% with tests |


**Disqualifier:** any 1 on dimension 1 or 3. An SE who has no requirements or no trade-offs is in the No-Requirements or No-Trade-Offs failure mode.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-05-se-se-architecture.md` - interview evidence for "Walk me through your architecture decisions." (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through your architecture design process.**
2. **Your architecture is too complex. What do you do?**
3. **The cost is too high. What do you do?**
4. **You have 3 architecture options. How do you prioritize?**
5. **Walk me through an architecture decision you've made.**
