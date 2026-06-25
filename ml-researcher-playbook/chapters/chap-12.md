# ML Researcher Playbook
## Chapter 12

# Training Methodology for MLRs

> *"The MLR designs training methodology. The 4-training-pillar framework (data + objective + optimization + regularization), the 3-training templates (pretraining + finetuning + RLHF), and the 5-criterion training quality bar are the MLR's reference for training at the contributor level."*

---

## 1. Epigraph

_The MLR designs training methodology. The 4-training-pillar framework (data + objective + optimization + regularization), the 3-training templates (pretraining + finetuning + RLHF), and the 5-criterion training quality bar are the MLR's reference for training at the contributor level._

---

## 2. Problem

You are an MLR at acme-corp. The senior scientist has just told you: "training methodology for mlrs. 30-day timeline."

This chapter tells you the 4 mental models, 3 frameworks, and 5-criterion quality bar.

**Decision in one sentence:** _MLR training methodology is a 4-pillar framework + 3 training templates + 5-criterion bar; the MLR's job is to design training pipelines, validate them, and own the training quality._

---

## 3. Why MLRs Fail Here

Five named failure modes of MLRs whose training methodology for mlrs produced zero results.

- **The No-Data-Quality Failure.** Bad data. Garbage in, garbage out.
- **The No-Objective Failure.** No clear objective.
- **The No-Optimization Failure.** No optimization analysis.
- **The No-Regularization Failure.** Overfitting. No regularization.
- **The No-Reproducibility Failure.** Training not reproducible.

---

## 4. Mental Models

Four mental models that compress training methodology for mlrs.

**mental model 1: The 4 Training Pillars:** 4 pillars: data + objective + optimization + regularization.

**mental model 2: The 3 Training Templates:** 3 templates: pretraining + finetuning + RLHF.

**mental model 3: The 5-Criterion Bar:** 5 criteria: novel + rigorous + reproducible + impactful + well-tuned.

**mental model 4: The Training Card:** 1-page training card.

---

## 5. Frameworks

Three frameworks for training methodology for mlrs.

### Framework 1: The 1-Page Plan

```
# Training Methodology for MLRs - [Date]

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

You are an MLR at **acme-corp**. The senior scientist has given you 30 days to design the training methodology for mlrs system.

You have **90 minutes**. Produce the **training methodology for mlrs redesign** using the 3 frameworks above. Specify:

- The 1-page plan.
- The implementation tracker.
- The retrospective review template.
- The 30-day timeline.
- The 1 thing you'll say to the senior scientist in the first review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-12-mlr-mlr-training.md` - under 1500 words.

---

## 7. Worked Example

**The 1-page training card:**

```
# Training Card - Mamba B2B pretraining

## Data
- 1M B2B examples
- Tokenization: BPE

## Objective
- Causal LM
- Loss: cross-entropy
```

---

## 8. Failure Mode Postmortem

An MLR at a 200-person B2B AI company trained models without reproducibility. Training runs differed. The senior scientist said: 'Reproducibility is non-negotiable.'

What the first MLR missed: training methodology for mlrs is a system. The first MLR had no system. The second MLR had 4 mental models + 3 frameworks + 5 criteria. The system is the leverage.

The lesson: the MLR who has the system has training methodology for mlrs. The MLR who has no system has the failure mode.

---

## 9. Self-Assessment Rubric

| 1 | **4 training pillars** | 0-1 | 2-3 | 4 pillars |
| 2 | **3 templates** | 1 | 2 | 3 templates |
| 3 | **5-criterion bar** | 0-2 | 3-4 | 5 criteria |
| 4 | **Reproducibility** | <50% | 50-90% | 100% documented |
| 5 | **Training runs per quarter** | <5 | 5-10 | 10+ |


**Disqualifier:** any 1 on dimension 1 or 3. An MLR who has bad data or no objective is in the No-Data-Quality or No-Objective failure mode.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-12-mlr-mlr-training.md` - interview evidence for "Walk me through your training methodology." (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through your training methodology.**
2. **Your training is not reproducible. What do you do?**
3. **The model overfits. What do you do?**
4. **You have 3 training strategies. How do you prioritize?**
5. **Walk me through a training run you've led.**
