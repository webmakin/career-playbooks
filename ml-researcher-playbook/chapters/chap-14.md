# ML Researcher Playbook
## Chapter 14

# MLR-Engineering Collaboration

> *"The MLR partners with engineering. The 4-ownership-boundary model (MLR owns research + experiments + paper; Eng owns production + serving + monitoring), the 3 cadence patterns, and the 5-criterion collaboration quality bar are the MLR's reference for collaboration at the contributor level."*

---

## 1. Epigraph

_The MLR partners with engineering. The 4-ownership-boundary model (MLR owns research + experiments + paper; Eng owns production + serving + monitoring), the 3 cadence patterns, and the 5-criterion collaboration quality bar are the MLR's reference for collaboration at the contributor level._

---

## 2. Problem

You are an MLR at acme-corp. The senior scientist has just told you: "mlr-engineering collaboration. 30-day timeline."

This chapter tells you the 4 mental models, 3 frameworks, and 5-criterion quality bar.

**Decision in one sentence:** _MLR-eng collaboration is a 4-ownership-boundary model + 3 cadence patterns + 5-criterion bar; the MLR's job is to provide high-quality research output, accept eng's production decisions, and own the research-to-production handoff._

---

## 3. Why MLRs Fail Here

Five named failure modes of MLRs whose mlr-engineering collaboration produced zero results.

- **The Throwing-Over-Wall Failure.** MLR hands model to eng with no support.
- **The No-Handoff Failure.** No handoff process.
- **The MLR-Tells-Eng-What-To-Build Failure.** MLR dictates production.
- **The Eng-Tells-MLR-What-To-Research Failure.** Eng dictates research.
- **The No-Cadence Failure.** No sync.

---

## 4. Mental Models

Four mental models that compress mlr-engineering collaboration.

**mental model 1: The 4 Ownership Boundaries:** 4 boundaries: MLR (research + experiments + paper) + Eng (production + serving + monitoring).

**mental model 2: The 3 Cadence Patterns:** 3 cadences: weekly 30 min + monthly 60 min + quarterly 90 min.

**mental model 3: The 5-Criterion Bar:** 5 criteria: aligned + specific + measured + owned + reusable.

**mental model 4: The Handoff Checklist:** 8-step handoff.

---

## 5. Frameworks

Three frameworks for mlr-engineering collaboration.

### Framework 1: The 1-Page Plan

```
# MLR-Engineering Collaboration - [Date]

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

You are an MLR at **acme-corp**. The senior scientist has given you 30 days to design the mlr-engineering collaboration system.

You have **90 minutes**. Produce the **mlr-engineering collaboration redesign** using the 3 frameworks above. Specify:

- The 1-page plan.
- The implementation tracker.
- The retrospective review template.
- The 30-day timeline.
- The 1 thing you'll say to the senior scientist in the first review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-14-mlr-mlr-eng-collab.md` - under 1500 words.

---

## 7. Worked Example

**The 1-page handoff checklist:**

```
# Research-to-Production Handoff

## MLR provides
- Code (GitHub repo)
- Weights
- Evaluation results
- Reproduction guide
```

---

## 8. Failure Mode Postmortem

An MLR at a 200-person B2B AI company threw models over the wall to eng. Eng struggled. Production diverged 5%. The senior scientist said: 'No handoff, no production.'

What the first MLR missed: mlr-engineering collaboration is a system. The first MLR had no system. The second MLR had 4 mental models + 3 frameworks + 5 criteria. The system is the leverage.

The lesson: the MLR who has the system has mlr-engineering collaboration. The MLR who has no system has the failure mode.

---

## 9. Self-Assessment Rubric

| 1 | **4 ownership boundaries** | 0-1 | 2-3 | 4 boundaries |
| 2 | **3 cadences** | 1 | 2 | 3 cadences |
| 3 | **5-criterion bar** | 0-2 | 3-4 | 5 criteria |
| 4 | **Handoff checklist** | None | Partial | 8-step checklist |
| 5 | **Production parity** | 5%+ drop | 1-5% drop | <1% drop |


**Disqualifier:** any 1 on dimension 1 or 3. An MLR who throws over the wall or has no cadence is in the Throwing-Over-Wall or No-Cadence failure mode.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-14-mlr-mlr-eng-collab.md` - interview evidence for "Walk me through your MLR-eng collaboration." (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through your MLR-eng collaboration.**
2. **Eng can't reproduce your model. What do you do?**
3. **Production diverges 5%. What do you do?**
4. **The eng team is overwhelmed. What do you do?**
5. **Walk me through a research-to-production handoff you've done.**
