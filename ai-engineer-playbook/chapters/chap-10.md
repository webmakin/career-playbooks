# AI Engineer Playbook
## Chapter 10

# LLM Serving and Latency

> *"The AIE owns LLM serving. The 4-serving-pillar framework (latency + throughput + cost + quality), the 3-serving templates (batched + streaming + cached), and the 5-criterion serving quality bar are the AIE's reference for LLM serving at the contributor level."*

---

## 1. Epigraph

_The AIE owns LLM serving. The 4-serving-pillar framework (latency + throughput + cost + quality), the 3-serving templates (batched + streaming + cached), and the 5-criterion serving quality bar are the AIE's reference for LLM serving at the contributor level._

---

## 2. Problem

You are an AIE at acme-corp. The engineering manager has just told you: "llm serving and latency. 30-day timeline."

This chapter tells you the 4 mental models, 3 frameworks, and 5-criterion quality bar.

**Decision in one sentence:** _AIE LLM serving is a 4-pillar framework + 3 serving templates + 5-criterion bar; the AIE's job is to design LLM serving pipelines, validate them, and own the serving quality._

---

## 3. Why AIEs Fail Here

Five named failure modes of AIEs whose llm serving and latency produced zero results.

- **The Latency-Issue Failure.** p99 latency > 1s.
- **The Throughput-Issue Failure.** Throughput too low.
- **The No-Caching Failure.** No caching.
- **The No-Streaming Failure.** No streaming. Bad UX.
- **The No-Quality-Monitoring Failure.** No quality monitoring.

---

## 4. Mental Models

Four mental models that compress llm serving and latency.

**mental model 1: The 4 Serving Pillars:** 4 pillars: latency + throughput + cost + quality.

**mental model 2: The 3 Serving Templates:** 3 templates: batched + streaming + cached.

**mental model 3: The 5-Criterion Bar:** 5 criteria: low-latency + high-throughput + cost-effective + accurate + monitored.

**mental model 4: The Serving Card:** 1-page serving card.

---

## 5. Frameworks

Three frameworks for llm serving and latency.

### Framework 1: The 1-Page Plan

```
# LLM Serving and Latency - [Date]

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

You are an AIE at **acme-corp**. The engineering manager has given you 30 days to design the llm serving and latency system.

You have **90 minutes**. Produce the **llm serving and latency redesign** using the 3 frameworks above. Specify:

- The 1-page plan.
- The implementation tracker.
- The retrospective review template.
- The 30-day timeline.
- The 1 thing you'll say to the engineering manager in the first review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-10-aie-aie-serving.md` - under 1500 words.

---

## 7. Worked Example

**The 1-page serving card:**

```
# LLM Serving Card - GPT-4

## Latency
- p50: 200ms
- p99: 500ms
```

---

## 8. Failure Mode Postmortem

An AIE at a 200-person B2B AI company shipped LLM with p99 > 5s. Customers churned. The PM said: 'p99 < 1s, or no production.'

What the first AIE missed: llm serving and latency is a system. The first AIE had no system. The second AIE had 4 mental models + 3 frameworks + 5 criteria. The system is the leverage.

The lesson: the AIE who has the system has llm serving and latency. The AIE who has no system has the failure mode.

---

## 9. Self-Assessment Rubric

| 1 | **4 serving pillars** | 0-1 | 2-3 | 4 pillars |
| 2 | **3 templates** | 1 | 2 | 3 templates |
| 3 | **5-criterion bar** | 0-2 | 3-4 | 5 criteria |
| 4 | **p99 latency** | >1s | 200ms-1s | <200ms |
| 5 | **Throughput** | <100 req/s | 100-1K req/s | 1K+ req/s |


**Disqualifier:** any 1 on dimension 1 or 3. An AIE who has latency issue or no streaming is in the Latency-Issue or No-Streaming failure mode.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-10-aie-aie-serving.md` - interview evidence for "Walk me through your LLM serving." (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through your LLM serving pipeline.**
2. **p99 latency is too high. What do you do?**
3. **Throughput is too low. What do you do?**
4. **You have 3 serving strategies. How do you prioritize?**
5. **Walk me through a serving optimization you've led.**
