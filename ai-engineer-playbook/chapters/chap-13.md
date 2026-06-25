# AI Engineer Playbook
## Chapter 13

# Fine-Tuning and Custom Models

> *"The AIE owns fine-tuning. The 4-fine-tuning-pillar framework (data + objective + training + evaluation), the 3-fine-tuning templates (LoRA + full + RLHF), and the 5-criterion fine-tuning quality bar are the AIE's reference for fine-tuning at the contributor level."*

---

## 1. Epigraph

_The AIE owns fine-tuning. The 4-fine-tuning-pillar framework (data + objective + training + evaluation), the 3-fine-tuning templates (LoRA + full + RLHF), and the 5-criterion fine-tuning quality bar are the AIE's reference for fine-tuning at the contributor level._

---

## 2. Problem

You are an AIE at acme-corp. The engineering manager has just told you: "fine-tuning and custom models. 30-day timeline."

This chapter tells you the 4 mental models, 3 frameworks, and 5-criterion quality bar.

**Decision in one sentence:** _AIE fine-tuning is a 4-pillar framework + 3 fine-tuning templates + 5-criterion bar; the AIE's job is to design fine-tuning pipelines, validate them, and own the fine-tuning quality._

---

## 3. Why AIEs Fail Here

Five named failure modes of AIEs whose fine-tuning and custom models produced zero results.

- **The No-Data-Quality Failure.** Bad data.
- **The No-Objective Failure.** No clear objective.
- **The No-Eval Failure.** No eval harness.
- **The No-Production-Parity Failure.** Research != production.
- **The Over-Fit Failure.** Over-fit on training data.

---

## 4. Mental Models

Four mental models that compress fine-tuning and custom models.

**mental model 1: The 4 Fine-Tuning Pillars:** 4 pillars: data + objective + training + evaluation.

**mental model 2: The 3 Fine-Tuning Templates:** 3 templates: LoRA + full + RLHF.

**mental model 3: The 5-Criterion Bar:** 5 criteria: data-quality + objective-clear + trained + evaluated + monitored.

**mental model 4: The Fine-Tuning Card:** 1-page card.

---

## 5. Frameworks

Three frameworks for fine-tuning and custom models.

### Framework 1: The 1-Page Plan

```
# Fine-Tuning and Custom Models - [Date]

## Top 3 strategic inputs
1. [Input 1]
2. [Input 2]
3. [Input 3]

## The 5-criterion bar applied

## The 1 thing the AIE will NOT compromise on
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

You are an AIE at **acme-corp**. The engineering manager has given you 30 days to design the fine-tuning and custom models system.

You have **90 minutes**. Produce the **fine-tuning and custom models redesign** using the 3 frameworks above. Specify:

- The 1-page plan.
- The implementation tracker.
- The retrospective review template.
- The 30-day timeline.
- The 1 thing you'll say to the engineering manager in the first review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-13-aie-aie-fine-tuning.md` - under 1500 words.

---

## 7. Worked Example

**The 1-page fine-tuning card:**

```
# Fine-Tuning Card - B2B AI

## Data
- 10K B2B examples

## Method
- LoRA
```

---

## 8. Failure Mode Postmortem

An AIE at a 200-person B2B AI company fine-tuned on bad data. Quality dropped. The PM said: 'Bad data, bad model.'

What the first AIE missed: fine-tuning and custom models is a system. The first AIE had no system. The second AIE had 4 mental models + 3 frameworks + 5 criteria. The system is the leverage.

The lesson: the AIE who has the system has fine-tuning and custom models. The AIE who has no system has the failure mode.

---

## 9. Self-Assessment Rubric

| 1 | **4 fine-tuning pillars** | 0-1 | 2-3 | 4 pillars |
| 2 | **3 templates** | 1 | 2 | 3 templates |
| 3 | **5-criterion bar** | 0-2 | 3-4 | 5 criteria |
| 4 | **Eval coverage** | <50% | 50-90% | 100% |
| 5 | **Production parity** | 5%+ drop | 1-5% drop | <1% drop |


**Disqualifier:** any 1 on dimension 1 or 3. An AIE who has bad data or no eval is in the No-Data-Quality or No-Eval failure mode.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-13-aie-aie-fine-tuning.md` - interview evidence for "Walk me through your fine-tuning." (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through your fine-tuning process.**
2. **Quality dropped after fine-tuning. What do you do?**
3. **The model over-fits. What do you do?**
4. **You have 3 fine-tuning strategies. How do you prioritize?**
5. **Walk me through a fine-tuning run you've led.**
