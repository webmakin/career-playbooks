# ML Researcher Playbook
## Chapter 10

# Hypothesis Generation and Validation

> *"The MLR generates and validates hypotheses. The 4-pillar hypothesis framework (observation + insight + falsification + impact), the 3-hypothesis templates (architecture + training + inference), and the 5-criterion hypothesis quality bar are the MLR's reference for hypothesis at the contributor level."*

---

## 1. Epigraph

_The MLR generates and validates hypotheses. The 4-pillar hypothesis framework (observation + insight + falsification + impact), the 3-hypothesis templates (architecture + training + inference), and the 5-criterion hypothesis quality bar are the MLR's reference for hypothesis at the contributor level._

---

## 2. Problem

You are an MLR at acme-corp. The senior scientist has just told you: "hypothesis generation and validation. 30-day timeline."

This chapter tells you the 4 mental models, 3 frameworks, and 5-criterion quality bar.

**Decision in one sentence:** _MLR hypothesis generation is a 4-pillar framework + 3 hypothesis templates + 5-criterion bar; the MLR's job is to generate hypotheses, validate them with experiments, and own the hypothesis quality._

---

## 3. Why MLRs Fail Here

Five named failure modes of MLRs whose hypothesis generation and validation produced zero results.

- **The No-Hypothesis Failure.** Ad-hoc experiments. No hypothesis.
- **The Non-Falsifiable Failure.** Hypothesis can't be falsified.
- **The No-Insight Failure.** No novel insight. Just engineering.
- **The No-Validation Failure.** Hypothesis never validated.
- **The Hypothesis-Stacking Failure.** 5 hypotheses at once. None ship.

---

## 4. Mental Models

Four mental models that compress hypothesis generation and validation.

**mental model 1: The 4 Hypothesis Pillars:** 4 pillars: observation + insight + falsification + impact.

**mental model 2: The 3 Hypothesis Templates:** 3 templates: architecture + training + inference.

**mental model 3: The 5-Criterion Bar:** 5 criteria: novel + falsifiable + testable + impactful + owned.

**mental model 4: The Hypothesis Card:** 1-page hypothesis card.

---

## 5. Frameworks

Three frameworks for hypothesis generation and validation.

### Framework 1: The 1-Page Plan

```
# Hypothesis Generation and Validation - [Date]

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

You are an MLR at **acme-corp**. The senior scientist has given you 30 days to design the hypothesis generation and validation system.

You have **90 minutes**. Produce the **hypothesis generation and validation redesign** using the 3 frameworks above. Specify:

- The 1-page plan.
- The implementation tracker.
- The retrospective review template.
- The 30-day timeline.
- The 1 thing you'll say to the senior scientist in the first review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-10-mlr-mlr-hypothesis.md` - under 1500 words.

---

## 7. Worked Example

**The 1-page hypothesis card:**

```
# Hypothesis Card - Mamba for B2B AI

## Observation
Transformer cost is 5x Mamba on B2B corpus

## Insight
Selective state-space captures B2B context better

## Falsification
Accuracy drop > 5% vs Transformer
```

---

## 8. Failure Mode Postmortem

An MLR at a 200-person B2B AI company ran experiments without hypotheses. 0 paper acceptances. The senior scientist said: 'No hypothesis, no experiment.'

What the first MLR missed: hypothesis generation and validation is a system. The first MLR had no system. The second MLR had 4 mental models + 3 frameworks + 5 criteria. The system is the leverage.

The lesson: the MLR who has the system has hypothesis generation and validation. The MLR who has no system has the failure mode.

---

## 9. Self-Assessment Rubric

| 1 | **4 hypothesis pillars** | 0-1 | 2-3 | 4 pillars |
| 2 | **3 templates** | 1 | 2 | 3 templates |
| 3 | **5-criterion bar** | 0-2 | 3-4 | 5 criteria |
| 4 | **Validated hypotheses/year** | 0 | 1 | 3+ |
| 5 | **Hypothesis-to-paper ratio** | <10% | 10-30% | 30%+ |


**Disqualifier:** any 1 on dimension 1 or 3. An MLR who has no hypothesis or non-falsifiable is in the No-Hypothesis or Non-Falsifiable failure mode.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-10-mlr-mlr-hypothesis.md` - interview evidence for "Walk me through your hypothesis generation." (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through your hypothesis generation process.**
2. **Your hypothesis can't be falsified. What do you do?**
3. **You have 5 hypotheses. How do you prioritize?**
4. **The hypothesis is wrong. What do you do?**
5. **Walk me through a hypothesis you've validated.**
