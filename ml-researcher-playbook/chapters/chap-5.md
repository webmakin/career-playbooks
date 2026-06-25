# ML Researcher Playbook
## Chapter 5

# Experimental Design for MLRs

> *"The MLR designs rigorous experiments. The 4-design-pillar framework (hypothesis + variables + controls + metrics), the 3-design templates (ablation + comparison + scaling), and the 5-criterion design quality bar are the MLR's reference for experimental design at the contributor level."*

---

## 1. Epigraph

_The MLR designs rigorous experiments. The 4-design-pillar framework (hypothesis + variables + controls + metrics), the 3-design templates (ablation + comparison + scaling), and the 5-criterion design quality bar are the MLR's reference for experimental design at the contributor level._

---

## 2. Problem

You are an MLR at acme-corp. The senior scientist has just told you: "experimental design for mlrs. 30-day timeline."

This chapter tells you the 4 mental models, 3 frameworks, and 5-criterion quality bar.

**Decision in one sentence:** _MLR experimental design is a 4-pillar framework + 3 design templates + 5-criterion bar; the MLR's job is to design rigorous experiments, validate hypotheses, and own the experimental design quality._

---

## 3. Why MLRs Fail Here

Five named failure modes of MLRs whose experimental design for mlrs produced zero results.

- **The No-Hypothesis Failure.** No clear hypothesis. Ad-hoc experiments.
- **The No-Baselines Failure.** No baseline comparisons.
- **The No-Ablations Failure.** No ablation studies.
- **The No-Reproducibility Failure.** Experiments not reproducible.
- **The No-Metrics Failure.** Vanity metrics only.

---

## 4. Mental Models

Four mental models that compress experimental design for mlrs.

**mental model 1: The 4 Design Pillars:** 4 pillars: hypothesis + variables + controls + metrics.

**mental model 2: The 3 Design Templates:** 3 templates: ablation + comparison + scaling.

**mental model 3: The 5-Criterion Bar:** 5 criteria: novel + rigorous + reproducible + impactful + honest.

**mental model 4: The Experiment Card:** 1-page experiment card.

---

## 5. Frameworks

Three frameworks for experimental design for mlrs.

### Framework 1: The 1-Page Plan

```
# Experimental Design for MLRs - [Date]

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

You are an MLR at **acme-corp**. The senior scientist has given you 30 days to design the experimental design for mlrs system.

You have **90 minutes**. Produce the **experimental design for mlrs redesign** using the 3 frameworks above. Specify:

- The 1-page plan.
- The implementation tracker.
- The retrospective review template.
- The 30-day timeline.
- The 1 thing you'll say to the senior scientist in the first review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-05-mlr-mlr-experimental-design.md` - under 1500 words.

---

## 7. Worked Example

**The 1-page experiment card:**

```
# Experiment Card - Mamba ablation

## Hypothesis
Removing selective state-space reduces B2B accuracy by <5%

## Variables
Mamba vs Mamba w/o SSM

## Controls
Random seed 42, batch 32, 10 epochs
```

---

## 8. Failure Mode Postmortem

An MLR at a 200-person B2B AI company designed experiments without baselines. NeurIPS submission rejected. The senior scientist said: 'No baselines, no paper.'

What the first MLR missed: experimental design for mlrs is a system. The first MLR had no system. The second MLR had 4 mental models + 3 frameworks + 5 criteria. The system is the leverage.

The lesson: the MLR who has the system has experimental design for mlrs. The MLR who has no system has the failure mode.

---

## 9. Self-Assessment Rubric

| 1 | **4 design pillars** | 0-1 | 2-3 | 4 pillars |
| 2 | **3 templates** | 1 | 2 | 3 templates |
| 3 | **5-criterion bar** | 0-2 | 3-4 | 5 criteria |
| 4 | **Baselines per experiment** | 0 | 1 | 3+ |
| 5 | **Reproducibility** | <50% | 50-90% | 100% documented |


**Disqualifier:** any 1 on dimension 1 or 3. An MLR who has no hypothesis or no baselines is in the No-Hypothesis or No-Baselines failure mode.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-05-mlr-mlr-experimental-design.md` - interview evidence for "Walk me through your experimental design." (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through your experimental design process.**
2. **Your paper got rejected for no baselines. What do you do?**
3. **The experiment is not reproducible. What do you do?**
4. **You have 5 experiments in flight. How do you prioritize?**
5. **Walk me through an ablation study you've led.**
