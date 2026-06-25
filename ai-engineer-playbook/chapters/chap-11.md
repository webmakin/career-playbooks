# AI Engineer Playbook
## Chapter 11

# Evaluation Harnesses

> *"The AIE designs eval harnesses. The 4-eval-pillar framework (test cases + metrics + LLM-as-judge + ground truth), the 3-eval templates (unit + integration + production), and the 5-criterion eval quality bar are the AIE's reference for evals at the contributor level."*

---

## 1. Epigraph

_The AIE designs eval harnesses. The 4-eval-pillar framework (test cases + metrics + LLM-as-judge + ground truth), the 3-eval templates (unit + integration + production), and the 5-criterion eval quality bar are the AIE's reference for evals at the contributor level._

---

## 2. Problem

You are an AIE at acme-corp. The engineering manager has just told you: "evaluation harnesses. 30-day timeline."

This chapter tells you the 4 mental models, 3 frameworks, and 5-criterion quality bar.

**Decision in one sentence:** _AIE eval harness design is a 4-pillar framework + 3 eval templates + 5-criterion bar; the AIE's job is to design eval harnesses, run them, and own the eval quality._

---

## 3. Why AIEs Fail Here

Five named failure modes of AIEs whose evaluation harnesses produced zero results.

- **The No-Eval Failure.** No eval harness.
- **The Manual-Testing Failure.** Manual testing only.
- **The No-Ground-Truth Failure.** No ground truth.
- **The No-LLM-as-Judge Failure.** No LLM-as-judge.
- **The No-Production-Eval Failure.** No production eval.

---

## 4. Mental Models

Four mental models that compress evaluation harnesses.

**mental model 1: The 4 Eval Pillars:** 4 pillars: test cases + metrics + LLM-as-judge + ground truth.

**mental model 2: The 3 Eval Templates:** 3 templates: unit + integration + production.

**mental model 3: The 5-Criterion Bar:** 5 criteria: tested + measured + judged + grounded + monitored.

**mental model 4: The Eval Card:** 1-page eval card.

---

## 5. Frameworks

Three frameworks for evaluation harnesses.

### Framework 1: The 1-Page Plan

```
# Evaluation Harnesses - [Date]

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

You are an AIE at **acme-corp**. The engineering manager has given you 30 days to design the evaluation harnesses system.

You have **90 minutes**. Produce the **evaluation harnesses redesign** using the 3 frameworks above. Specify:

- The 1-page plan.
- The implementation tracker.
- The retrospective review template.
- The 30-day timeline.
- The 1 thing you'll say to the engineering manager in the first review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-11-aie-aie-eval.md` - under 1500 words.

---

## 7. Worked Example

**The 1-page eval card:**

```
# Eval Card - RAG Q&A

## Test cases
- 100 hand-curated
- 500 production logs

## Metrics
- Accuracy (target 90%+)
```

---

## 8. Failure Mode Postmortem

An AIE at a 200-person B2B AI company had no eval harness. Manual testing only. Quality varied. The PM said: 'No eval, no LLM.'

What the first AIE missed: evaluation harnesses is a system. The first AIE had no system. The second AIE had 4 mental models + 3 frameworks + 5 criteria. The system is the leverage.

The lesson: the AIE who has the system has evaluation harnesses. The AIE who has no system has the failure mode.

---

## 9. Self-Assessment Rubric

| 1 | **4 eval pillars** | 0-1 | 2-3 | 4 pillars |
| 2 | **3 templates** | 1 | 2 | 3 templates |
| 3 | **5-criterion bar** | 0-2 | 3-4 | 5 criteria |
| 4 | **Test cases** | <100 | 100-500 | 500+ |
| 5 | **Eval coverage** | <50% | 50-90% | 100% of features |


**Disqualifier:** any 1 on dimension 1 or 3. An AIE who has no eval or manual testing is in the No-Eval or Manual-Testing failure mode.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-11-aie-aie-eval.md` - interview evidence for "Walk me through your eval harness." (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through your eval harness process.**
2. **Quality varies across runs. What do you do?**
3. **The PM rejects the eval. What do you do?**
4. **You have 3 eval strategies. How do you prioritize?**
5. **Walk me through an eval harness you've built.**
