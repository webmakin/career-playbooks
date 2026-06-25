# ML Researcher Playbook
## Chapter 7

# Benchmarking and Evaluation

> *"The MLR designs benchmarks. The 4-benchmarking-pillar framework (datasets + metrics + baselines + analysis), the 3 benchmark types (SOTA + ablation + production), and the 5-criterion benchmarking quality bar are the MLR's reference for benchmarking at the contributor level."*

---

## 1. Epigraph

_The MLR designs benchmarks. The 4-benchmarking-pillar framework (datasets + metrics + baselines + analysis), the 3 benchmark types (SOTA + ablation + production), and the 5-criterion benchmarking quality bar are the MLR's reference for benchmarking at the contributor level._

---

## 2. Problem

You are an MLR at acme-corp. The senior scientist has just told you: "benchmarking and evaluation. 30-day timeline."

This chapter tells you the 4 mental models, 3 frameworks, and 5-criterion quality bar.

**Decision in one sentence:** _MLR benchmarking is a 4-pillar framework + 3 benchmark types + 5-criterion bar; the MLR's job is to design benchmarks, run evaluations, and own the benchmarking quality._

---

## 3. Why MLRs Fail Here

Five named failure modes of MLRs whose benchmarking and evaluation produced zero results.

- **The No-Datasets Failure.** No standard datasets.
- **The Vanity-Metrics Failure.** Vanity metrics only.
- **The No-Baselines Failure.** No baseline comparisons.
- **The No-Analysis Failure.** No result analysis.
- **The No-Production-Benchmarks Failure.** No production benchmarks.

---

## 4. Mental Models

Four mental models that compress benchmarking and evaluation.

**mental model 1: The 4 Benchmarking Pillars:** 4 pillars: datasets + metrics + baselines + analysis.

**mental model 2: The 3 Benchmark Types:** 3 types: SOTA + ablation + production.

**mental model 3: The 5-Criterion Bar:** 5 criteria: standard + comprehensive + reproducible + meaningful + actionable.

**mental model 4: The Benchmark Card:** 1-page benchmark card.

---

## 5. Frameworks

Three frameworks for benchmarking and evaluation.

### Framework 1: The 1-Page Plan

```
# Benchmarking and Evaluation - [Date]

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

You are an MLR at **acme-corp**. The senior scientist has given you 30 days to design the benchmarking and evaluation system.

You have **90 minutes**. Produce the **benchmarking and evaluation redesign** using the 3 frameworks above. Specify:

- The 1-page plan.
- The implementation tracker.
- The retrospective review template.
- The 30-day timeline.
- The 1 thing you'll say to the senior scientist in the first review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-07-mlr-mlr-benchmarking.md` - under 1500 words.

---

## 7. Worked Example

**The 1-page benchmark card:**

```
# Benchmark Card - Mamba for B2B AI

## Datasets
- Custom B2B corpus (1M examples)
- Public dataset X

## Metrics
- Accuracy (within 1% of baseline)
- Cost (5x reduction)
```

---

## 8. Failure Mode Postmortem

An MLR at a 200-person B2B AI company used vanity metrics. NeurIPS submission rejected for no standard benchmarks. The senior scientist said: 'Standard benchmarks, or no paper.'

What the first MLR missed: benchmarking and evaluation is a system. The first MLR had no system. The second MLR had 4 mental models + 3 frameworks + 5 criteria. The system is the leverage.

The lesson: the MLR who has the system has benchmarking and evaluation. The MLR who has no system has the failure mode.

---

## 9. Self-Assessment Rubric

| 1 | **4 benchmarking pillars** | 0-1 | 2-3 | 4 pillars |
| 2 | **3 benchmark types** | 1 | 2 | 3 types |
| 3 | **5-criterion bar** | 0-2 | 3-4 | 5 criteria |
| 4 | **Standard benchmarks used** | 0 | 1-2 | 3+ |
| 5 | **Production benchmarks** | 0 | 1 | 2+ |


**Disqualifier:** any 1 on dimension 1 or 3. An MLR who has no datasets or no baselines is in the No-Datasets or No-Baselines failure mode.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-07-mlr-mlr-benchmarking.md` - interview evidence for "Walk me through your benchmarking." (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through your benchmarking process.**
2. **Your paper got rejected for no standard benchmarks. What do you do?**
3. **The production model diverges from research. What do you do?**
4. **You have 5 benchmarks. How do you prioritize?**
5. **Walk me through a benchmark submission you've led.**
