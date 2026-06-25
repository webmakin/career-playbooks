# ML Researcher Playbook
## Chapter 8

# Open-Source Releases

> *"The MLR ships open-source releases. The 4-OSS-pillar framework (code + docs + tests + license), the 3 release types (library + benchmark + checkpoint), and the 5-criterion OSS quality bar are the MLR's reference for open-source releases at the contributor level."*

---

## 1. Epigraph

_The MLR ships open-source releases. The 4-OSS-pillar framework (code + docs + tests + license), the 3 release types (library + benchmark + checkpoint), and the 5-criterion OSS quality bar are the MLR's reference for open-source releases at the contributor level._

---

## 2. Problem

You are an MLR at acme-corp. The senior scientist has just told you: "open-source releases. 30-day timeline."

This chapter tells you the 4 mental models, 3 frameworks, and 5-criterion quality bar.

**Decision in one sentence:** _MLR open-source is a 4-pillar framework + 3 release types + 5-criterion bar; the MLR's job is to ship libraries, run the release pipeline, and own the open-source quality._

---

## 3. Why MLRs Fail Here

Five named failure modes of MLRs whose open-source releases produced zero results.

- **The Throwaway-Code Failure.** Throwaway code. Not reusable.
- **The No-Docs Failure.** No documentation.
- **The No-Tests Failure.** No tests.
- **The No-License Failure.** No license. Legal risk.
- **The Low-Adoption Failure.** 0 stars, 0 forks.

---

## 4. Mental Models

Four mental models that compress open-source releases.

**mental model 1: The 4 OSS Pillars:** 4 pillars: code + docs + tests + license.

**mental model 2: The 3 Release Types:** 3 types: library + benchmark + checkpoint.

**mental model 3: The 5-Criterion OSS Bar:** 5 criteria: documented + tested + licensed + adoptable + maintained.

**mental model 4: The Release Checklist:** Per-release checklist.

---

## 5. Frameworks

Three frameworks for open-source releases.

### Framework 1: The 1-Page Plan

```
# Open-Source Releases - [Date]

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

You are an MLR at **acme-corp**. The senior scientist has given you 30 days to design the open-source releases system.

You have **90 minutes**. Produce the **open-source releases redesign** using the 3 frameworks above. Specify:

- The 1-page plan.
- The implementation tracker.
- The retrospective review template.
- The 30-day timeline.
- The 1 thing you'll say to the senior scientist in the first review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-08-mlr-mlr-open-source.md` - under 1500 words.

---

## 7. Worked Example

**The 1-page release checklist:**

```
# OSS Release Checklist

## Code
- [ ] README
- [ ] Examples
- [ ] Tests (80%+ coverage)
- [ ] License (Apache 2.0)
- [ ] CI/CD
```

---

## 8. Failure Mode Postmortem

An MLR at a 200-person B2B AI company shipped throwaway code. 0 stars. The senior scientist said: 'No tests, no library.'

What the first MLR missed: open-source releases is a system. The first MLR had no system. The second MLR had 4 mental models + 3 frameworks + 5 criteria. The system is the leverage.

The lesson: the MLR who has the system has open-source releases. The MLR who has no system has the failure mode.

---

## 9. Self-Assessment Rubric

| 1 | **4 OSS pillars** | 0-1 | 2-3 | 4 pillars |
| 2 | **3 release types** | 1 | 2 | 3 types |
| 3 | **5-criterion bar** | 0-2 | 3-4 | 5 criteria |
| 4 | **Stars** | <10 | 10-100 | 100+ |
| 5 | **Test coverage** | <50% | 50-80% | 80%+ |


**Disqualifier:** any 1 on dimension 1 or 3. An MLR who has throwaway code or no docs is in the Throwaway-Code or No-Docs failure mode.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-08-mlr-mlr-open-source.md` - interview evidence for "Walk me through your open-source releases." (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through your open-source release process.**
2. **Your library has 0 stars. What do you do?**
3. **A user reports a bug. What do you do?**
4. **The license is wrong. What do you do?**
5. **Walk me through an OSS release you've shipped.**
