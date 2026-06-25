# Staff Engineer Playbook
## Chapter 7

# Tooling and Developer Experience

> *"The SE owns tooling + DX. The 4-tooling-pillar framework (CI/CD + observability + testing + IDE), the 3-tooling templates (build + deploy + monitor), and the 5-criterion tooling quality bar are the SE's reference for tooling at the principal IC level."*

---

## 1. Epigraph

_The SE owns tooling + DX. The 4-tooling-pillar framework (CI/CD + observability + testing + IDE), the 3-tooling templates (build + deploy + monitor), and the 5-criterion tooling quality bar are the SE's reference for tooling at the principal IC level._

---

## 2. Problem

You are a Staff Engineer at acme-corp. The engineering director has just told you: "tooling and developer experience. 30-day timeline."

This chapter tells you the 4 mental models, 3 frameworks, and 5-criterion quality bar.

**Decision in one sentence:** _SE tooling + DX is a 4-pillar framework + 3 tooling templates + 5-criterion bar; the SE's job is to design tooling, validate them, and own the DX._

---

## 3. Why Staff Engineers Fail Here

Five named failure modes of Staff Engineers whose tooling and developer experience produced zero results.

- **The No-CI/CD Failure.** No CI/CD.
- **The No-Observability Failure.** No observability.
- **The No-Testing-Tools Failure.** No testing tools.
- **The No-IDE-Setup Failure.** No IDE setup.
- **The No-DX-Measurement Failure.** No DX measurement.

---

## 4. Mental Models

Four mental models that compress tooling and developer experience.

**mental model 1: The 4 Tooling Pillars:** 4 pillars: CI/CD + observability + testing + IDE.

**mental model 2: The 3 Tooling Templates:** 3 templates: build + deploy + monitor.

**mental model 3: The 5-Criterion Bar:** 5 criteria: CI/CD + observed + tested + IDE + measured.

**mental model 4: The Tooling Card:** 1-page tooling card.

---

## 5. Frameworks

Three frameworks for tooling and developer experience.

### Framework 1: The 1-Page Plan

```
# Tooling and Developer Experience - [Date]

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

You are a Staff Engineer at **acme-corp**. The engineering director has given you 30 days to design the tooling and developer experience system.

You have **90 minutes**. Produce the **tooling and developer experience redesign** using the 3 frameworks above. Specify:

- The 1-page plan.
- The implementation tracker.
- The retrospective review template.
- The 30-day timeline.
- The 1 thing you'll say to the engineering director in the first review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-07-se-se-tooling.md` - under 1500 words.

---

## 7. Worked Example

**The 1-page tooling card:**

```
# Tooling Card - FY26

## CI/CD
- GitHub Actions
- ArgoCD
```

---

## 8. Failure Mode Postmortem

An SE at a 200-person company had no CI/CD. Deploys were manual. The VP Eng said: 'No CI/CD, no production.'

What the first Staff Engineer missed: tooling and developer experience is a system. The first SE had no system. The second SE had 4 mental models + 3 frameworks + 5 criteria. The system is the leverage.

The lesson: the SE who has the system has tooling and developer experience. The SE who has no system has the failure mode.

---

## 9. Self-Assessment Rubric

| 1 | **4 tooling pillars** | 0-1 | 2-3 | 4 pillars |
| 2 | **3 tooling templates** | 1 | 2 | 3 templates |
| 3 | **5-criterion bar** | 0-2 | 3-4 | 5 criteria |
| 4 | **Build time** | >10 min | 5-10 min | <5 min |
| 5 | **DX score** | <3/5 | 3-4/5 | 4+/5 |


**Disqualifier:** any 1 on dimension 1 or 3. An SE who has no CI/CD or no observability is in the No-CI/CD or No-Observability failure mode.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-07-se-se-tooling.md` - interview evidence for "Walk me through your tooling strategy." (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through your tooling strategy.**
2. **DX is low. What do you do?**
3. **The team is overwhelmed by manual processes. What do you do?**
4. **You have 3 tooling strategies. How do you prioritize?**
5. **Walk me through a tooling decision you've made.**
