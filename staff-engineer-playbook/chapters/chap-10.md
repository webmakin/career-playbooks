# Staff Engineer Playbook
## Chapter 10

# System Design for Staff Engineers

> *"The SE designs systems. The 4-system-design-pillar framework (requirements + trade-offs + patterns + scaling), the 3-system-design templates (web app + data pipeline + distributed system), and the 5-criterion system design quality bar are the SE's reference for system design at the principal IC level."*

---

## 1. Epigraph

_The SE designs systems. The 4-system-design-pillar framework (requirements + trade-offs + patterns + scaling), the 3-system-design templates (web app + data pipeline + distributed system), and the 5-criterion system design quality bar are the SE's reference for system design at the principal IC level._

---

## 2. Problem

You are a Staff Engineer at acme-corp. The engineering director has just told you: "system design for staff engineers. 30-day timeline."

This chapter tells you the 4 mental models, 3 frameworks, and 5-criterion quality bar.

**Decision in one sentence:** _SE system design is a 4-pillar framework + 3 design templates + 5-criterion bar; the SE's job is to design systems, validate them, and own the system design quality._

---

## 3. Why Staff Engineers Fail Here

Five named failure modes of Staff Engineers whose system design for staff engineers produced zero results.

- **The No-Requirements Failure.** No requirements.
- **The No-Trade-Offs Failure.** No trade-off analysis.
- **The No-Patterns Failure.** No design patterns.
- **The No-Scaling Failure.** No scaling analysis.
- **The No-Documentation Failure.** No design documentation.

---

## 4. Mental Models

Four mental models that compress system design for staff engineers.

**mental model 1: The 4 System Design Pillars:** 4 pillars: requirements + trade-offs + patterns + scaling.

**mental model 2: The 3 System Design Templates:** 3 templates: web app + data pipeline + distributed system.

**mental model 3: The 5-Criterion Bar:** 5 criteria: requirement-clear + trade-off-aware + pattern-aligned + scalable + documented.

**mental model 4: The Design Doc:** Design doc template.

---

## 5. Frameworks

Three frameworks for system design for staff engineers.

### Framework 1: The 1-Page Plan

```
# System Design for Staff Engineers - [Date]

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

You are a Staff Engineer at **acme-corp**. The engineering director has given you 30 days to design the system design for staff engineers system.

You have **90 minutes**. Produce the **system design for staff engineers redesign** using the 3 frameworks above. Specify:

- The 1-page plan.
- The implementation tracker.
- The retrospective review template.
- The 30-day timeline.
- The 1 thing you'll say to the engineering director in the first review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-10-se-se-system-design.md` - under 1500 words.

---

## 7. Worked Example

**The 1-page design doc:**

```
# System Design Doc - B2B API

## Requirements
- 1M req/day
- p99 < 200ms
```

---

## 8. Failure Mode Postmortem

An SE at a 200-person company designed systems without trade-off analysis. Over-engineered. The VP Eng said: 'Trade-offs are the design.'

What the first Staff Engineer missed: system design for staff engineers is a system. The first SE had no system. The second SE had 4 mental models + 3 frameworks + 5 criteria. The system is the leverage.

The lesson: the SE who has the system has system design for staff engineers. The SE who has no system has the failure mode.

---

## 9. Self-Assessment Rubric

| 1 | **4 design pillars** | 0-1 | 2-3 | 4 pillars |
| 2 | **3 templates** | 1 | 2 | 3 templates |
| 3 | **5-criterion bar** | 0-2 | 3-4 | 5 criteria |
| 4 | **Design docs per quarter** | 0 | 1-2 | 3+ |
| 5 | **Scaling analysis** | None | Partial | 100% of designs |


**Disqualifier:** any 1 on dimension 1 or 3. An SE who has no requirements or no trade-offs is in the No-Requirements or No-Trade-Offs failure mode.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-10-se-se-system-design.md` - interview evidence for "Walk me through your system design." (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through your system design process.**
2. **The design is over-engineered. What do you do?**
3. **The system doesn't scale. What do you do?**
4. **You have 3 design options. How do you prioritize?**
5. **Walk me through a system design you've led.**
