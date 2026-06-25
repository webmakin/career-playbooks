# Staff Engineer Playbook
## Chapter 3

# Technical Direction and Vision

> *"The SE sets technical direction. The 4-direction-input framework (vision + architecture + tooling + standards), the 3-horizon model, and the 5-criterion direction quality bar are the SE's reference for technical direction at the principal IC level."*

---

## 1. Epigraph

_The SE sets technical direction. The 4-direction-input framework (vision + architecture + tooling + standards), the 3-horizon model, and the 5-criterion direction quality bar are the SE's reference for technical direction at the principal IC level._

---

## 2. Problem

You are a Staff Engineer at acme-corp. The engineering director has just told you: "technical direction and vision. 30-day timeline."

This chapter tells you the 4 mental models, 3 frameworks, and 5-criterion quality bar.

**Decision in one sentence:** _SE technical direction is a 4-input framework (vision + architecture + tooling + standards) + 3-horizon model (NOW + NEXT + BEYOND) + 5-criterion bar; the SE's job is to set technical direction, contribute to the engineering roadmap, and own the direction execution._

---

## 3. Why Staff Engineers Fail Here

Five named failure modes of Staff Engineers whose technical direction and vision produced zero results.

- **The No-Direction-Input Failure.** SE has no direction input.
- **The 1-Horizon Failure.** NOW only. No NEXT + BEYOND.
- **The No-Vision Failure.** No vision. Ad-hoc decisions.
- **The No-Standards Failure.** No engineering standards.
- **The No-Execution Failure.** Direction not executed.

---

## 4. Mental Models

Four mental models that compress technical direction and vision.

**mental model 1: The 4 Direction Inputs:** 4 inputs: vision + architecture + tooling + standards.

**mental model 2: The 3-Horizon Model:** 3 horizons: NOW (this quarter) + NEXT (next 4) + BEYOND (next 4 years).

**mental model 3: The 5-Criterion Direction Bar:** 5 criteria: novel + rigorous + impactful + actionable + owned.

**mental model 4: The Direction Memo:** 1-page memo template.

---

## 5. Frameworks

Three frameworks for technical direction and vision.

### Framework 1: The 1-Page Plan

```
# Technical Direction and Vision - [Date]

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

You are a Staff Engineer at **acme-corp**. The engineering director has given you 30 days to design the technical direction and vision system.

You have **90 minutes**. Produce the **technical direction and vision redesign** using the 3 frameworks above. Specify:

- The 1-page plan.
- The implementation tracker.
- The retrospective review template.
- The 30-day timeline.
- The 1 thing you'll say to the engineering director in the first review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-03-se-se-direction.md` - under 1500 words.

---

## 7. Worked Example

**The 1-page direction memo:**

```
# SE Direction Memo - FY27 - 2026-09-01

## Vision
Microservices on Kubernetes for B2B scale

## Architecture
Service mesh + gRPC + Postgres
```

---

## 8. Failure Mode Postmortem

An SE at a 200-person company had no direction input. The architecture drifted. The VP Eng asked: 'Where is our architecture going?' The SE had no answer.

What the first Staff Engineer missed: technical direction and vision is a system. The first SE had no system. The second SE had 4 mental models + 3 frameworks + 5 criteria. The system is the leverage.

The lesson: the SE who has the system has technical direction and vision. The SE who has no system has the failure mode.

---

## 9. Self-Assessment Rubric

| 1 | **4 direction inputs** | 0-1 | 2-3 | 4 inputs |
| 2 | **3 horizons** | 1 | 2 | 3 horizons |
| 3 | **5-criterion bar** | 0-2 | 3-4 | 5 criteria |
| 4 | **Architecture decisions** | 0 | 1-2 | 3+ |
| 5 | **Direction alignment** | None | Partial | Every project tied to direction |


**Disqualifier:** any 1 on dimension 1 or 3. An SE who has 0-1 inputs or 0-2 criteria is in the No-Direction-Input or No-Vision failure mode.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-03-se-se-direction.md` - interview evidence for "Walk me through your technical direction." (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through your technical direction input.**
2. **The VP Eng ignores your input. What do you do?**
3. **You have 1 quarter to influence direction. What do you do?**
4. **Your vision was wrong. What do you do?**
5. **Walk me through a direction memo you've written.**
