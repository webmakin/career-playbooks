# ML Researcher Playbook
## Chapter 13

# Inference and Serving for MLRs

> *"The MLR designs inference + serving. The 4-inference-pillar framework (latency + throughput + cost + accuracy), the 3-serving templates (batched + streaming + quantized), and the 5-criterion inference quality bar are the MLR's reference for inference at the contributor level."*

---

## 1. Epigraph

_The MLR designs inference + serving. The 4-inference-pillar framework (latency + throughput + cost + accuracy), the 3-serving templates (batched + streaming + quantized), and the 5-criterion inference quality bar are the MLR's reference for inference at the contributor level._

---

## 2. Problem

You are an MLR at acme-corp. The senior scientist has just told you: "inference and serving for mlrs. 30-day timeline."

This chapter tells you the 4 mental models, 3 frameworks, and 5-criterion quality bar.

**Decision in one sentence:** _MLR inference is a 4-pillar framework + 3 serving templates + 5-criterion bar; the MLR's job is to design inference pipelines, validate them, and own the inference quality._

---

## 3. Why MLRs Fail Here

Five named failure modes of MLRs whose inference and serving for mlrs produced zero results.

- **The Latency-Issue Failure.** p99 latency > 1s. Customer churn.
- **The Throughput-Issue Failure.** Throughput too low. Cost too high.
- **The No-Quantization Failure.** No quantization analysis.
- **The No-Production-Parity Failure.** Research != production.
- **The No-Monitoring Failure.** No inference monitoring.

---

## 4. Mental Models

Four mental models that compress inference and serving for mlrs.

**mental model 1: The 4 Inference Pillars:** 4 pillars: latency + throughput + cost + accuracy.

**mental model 2: The 3 Serving Templates:** 3 templates: batched + streaming + quantized.

**mental model 3: The 5-Criterion Bar:** 5 criteria: low-latency + high-throughput + cost-effective + accurate + monitored.

**mental model 4: The Inference Card:** 1-page inference card.

---

## 5. Frameworks

Three frameworks for inference and serving for mlrs.

### Framework 1: The 1-Page Plan

```
# Inference and Serving for MLRs - [Date]

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

You are an MLR at **acme-corp**. The senior scientist has given you 30 days to design the inference and serving for mlrs system.

You have **90 minutes**. Produce the **inference and serving for mlrs redesign** using the 3 frameworks above. Specify:

- The 1-page plan.
- The implementation tracker.
- The retrospective review template.
- The 30-day timeline.
- The 1 thing you'll say to the senior scientist in the first review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-13-mlr-mlr-inference.md` - under 1500 words.

---

## 7. Worked Example

**The 1-page inference card:**

```
# Inference Card - Mamba serving

## Latency
- p50: 50ms
- p99: 100ms

## Throughput
- 1000 req/s/GPU
```

---

## 8. Failure Mode Postmortem

An MLR at a 200-person B2B AI company shipped inference with p99 > 1s. Customers churned. The senior scientist said: 'p99 < 100ms, or no production.'

What the first MLR missed: inference and serving for mlrs is a system. The first MLR had no system. The second MLR had 4 mental models + 3 frameworks + 5 criteria. The system is the leverage.

The lesson: the MLR who has the system has inference and serving for mlrs. The MLR who has no system has the failure mode.

---

## 9. Self-Assessment Rubric

| 1 | **4 inference pillars** | 0-1 | 2-3 | 4 pillars |
| 2 | **3 serving templates** | 1 | 2 | 3 templates |
| 3 | **5-criterion bar** | 0-2 | 3-4 | 5 criteria |
| 4 | **p99 latency** | >500ms | 100-500ms | <100ms |
| 5 | **Production parity** | 5%+ drop | 1-5% drop | <1% drop |


**Disqualifier:** any 1 on dimension 1 or 3. An MLR who has latency issue or no quantization is in the Latency-Issue or No-Quantization failure mode.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-13-mlr-mlr-inference.md` - interview evidence for "Walk me through your inference pipeline." (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through your inference pipeline.**
2. **p99 latency is too high. What do you do?**
3. **Throughput is too low. What do you do?**
4. **You have 3 inference strategies. How do you prioritize?**
5. **Walk me through an inference deployment you've led.**
