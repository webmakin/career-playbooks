# Staff Engineer Playbook
## Chapter 6

# Code Review and Quality

> *"The SE owns code review + quality. The 4-quality-pillar framework (review + standards + testing + documentation), the 3-review templates (PR + design + architecture), and the 5-criterion quality bar are the SE's reference for quality at the principal IC level."*

---

## 1. Epigraph

_The SE owns code review + quality. The 4-quality-pillar framework (review + standards + testing + documentation), the 3-review templates (PR + design + architecture), and the 5-criterion quality bar are the SE's reference for quality at the principal IC level._

---

## 2. Problem

You are a Staff Engineer at acme-corp. The engineering director has just told you: "code review and quality. 30-day timeline."

This chapter tells you the 4 mental models, 3 frameworks, and 5-criterion quality bar.

**Decision in one sentence:** _SE code review is a 4-pillar framework + 3 review templates + 5-criterion bar; the SE's job is to design the review system, run the standards, and own the quality._

---

## 3. Why Staff Engineers Fail Here

Five named failure modes of Staff Engineers whose code review and quality produced zero results.

- **The No-Standards Failure.** No code standards.
- **The No-Review-Process Failure.** No review process. Ad-hoc.
- **The No-Testing Failure.** No testing standards.
- **The No-Documentation Failure.** No documentation standards.
- **The No-Mentorship Failure.** Doesn't mentor on review.

---

## 4. Mental Models

Four mental models that compress code review and quality.

**mental model 1: The 4 Quality Pillars:** 4 pillars: review + standards + testing + documentation.

**mental model 2: The 3 Review Templates:** 3 templates: PR + design + architecture.

**mental model 3: The 5-Criterion Bar:** 5 criteria: reviewed + standards + tested + documented + mentored.

**mental model 4: The Review Card:** 1-page review card.

---

## 5. Frameworks

Three frameworks for code review and quality.

### Framework 1: The 1-Page Plan

```
# Code Review and Quality - [Date]

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

You are a Staff Engineer at **acme-corp**. The engineering director has given you 30 days to design the code review and quality system.

You have **90 minutes**. Produce the **code review and quality redesign** using the 3 frameworks above. Specify:

- The 1-page plan.
- The implementation tracker.
- The retrospective review template.
- The 30-day timeline.
- The 1 thing you'll say to the engineering director in the first review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-06-se-se-quality.md` - under 1500 words.

---

## 7. Worked Example

**The 1-page review card:**

```
# Code Review Card

## Standards
- TypeScript strict mode
- 80%+ test coverage
```

---

## 8. Failure Mode Postmortem

An SE at a 200-person company had no code standards. Quality varied. The VP Eng said: 'No standards, no code.'

What the first Staff Engineer missed: code review and quality is a system. The first SE had no system. The second SE had 4 mental models + 3 frameworks + 5 criteria. The system is the leverage.

The lesson: the SE who has the system has code review and quality. The SE who has no system has the failure mode.

---

## 9. Self-Assessment Rubric

| 1 | **4 quality pillars** | 0-1 | 2-3 | 4 pillars |
| 2 | **3 review templates** | 1 | 2 | 3 templates |
| 3 | **5-criterion bar** | 0-2 | 3-4 | 5 criteria |
| 4 | **Test coverage** | <50% | 50-80% | 80%+ |
| 5 | **PR review SLA** | >48h | 12-48h | <12h |


**Disqualifier:** any 1 on dimension 1 or 3. An SE who has no standards or no review process is in the No-Standards or No-Review-Process failure mode.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-06-se-se-quality.md` - interview evidence for "Walk me through your code review process." (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through your code review process.**
2. **Code quality is low. What do you do?**
3. **The team is overwhelmed by reviews. What do you do?**
4. **You have 5 review strategies. How do you prioritize?**
5. **Walk me through a code review process you've designed.**
