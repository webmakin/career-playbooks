# AI Engineer Playbook
## Chapter 1

# What an AI Engineer Actually Does

> *"The AIE is not a Backend Engineer. The AIE is a category change - a hybrid who owns LLM integration, prompt engineering, and AI feature delivery at the product layer."*

---

## 1. Epigraph

_The AIE is not a Backend Engineer. The AIE is a category change - a hybrid who owns LLM integration, prompt engineering, and AI feature delivery at the product layer._

---

## 2. Problem

You are an AIE at acme-corp. The engineering manager has just told you: "what an ai engineer actually does. 30-day timeline."

This chapter tells you the 4 mental models, 3 frameworks, and 5-criterion quality bar.

**Decision in one sentence:** _AIE is a 4-pillar system (LLM integration + prompt engineering + AI feature delivery + AI observability) with 3 metrics (latency + cost + quality) and 5-criterion bar; the AIE's job is to ship AI features, own the LLM stack, and deliver measurable product outcomes._

---

## 3. Why AIEs Fail Here

Five named failure modes of AIEs whose what an ai engineer actually does produced zero results.

- **The SWE-Only Failure.** AIE works as backend engineer. No AI features.
- **The No-LLM-Stack Failure.** No LLM stack. Ad-hoc calls.
- **The No-Prompt-Engineering Failure.** No prompt versioning. Quality drops.
- **The No-Observability Failure.** No AI observability. No debugging.
- **The No-Cost-Tracking Failure.** No cost tracking. Bill surprise.

---

## 4. Mental Models

Four mental models that compress what an ai engineer actually does.

**mental model 1: The 4 AIE Pillars:** 4 pillars: LLM integration + prompt engineering + AI feature delivery + AI observability.

**mental model 2: The 3 AIE Metrics:** 3 metrics: latency + cost + quality.

**mental model 3: The 5-Criterion Bar:** 5 criteria: latency + cost + quality + reliability + safety.

**mental model 4: The AIE Weekly Cadence:** Mon-Fri LLM calls + prompts + reviews.

---

## 5. Frameworks

Three frameworks for what an ai engineer actually does.

### Framework 1: The 1-Page Plan

```
# What an AI Engineer Actually Does - [Date]

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

You are an AIE at **acme-corp**. The engineering manager has given you 30 days to design the what an ai engineer actually does system.

You have **90 minutes**. Produce the **what an ai engineer actually does redesign** using the 3 frameworks above. Specify:

- The 1-page plan.
- The implementation tracker.
- The retrospective review template.
- The 30-day timeline.
- The 1 thing you'll say to the engineering manager in the first review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-01-aie-aie-role.md` - under 1500 words.

---

## 7. Worked Example

**The 1-page AIE weekly plan:**

```
# AIE Weekly Plan - Week 1

## Top 3 priorities
1. RAG pipeline (Mon-Wed)
2. Prompt v2 deployment (Wed-Fri)
3. Latency review (Fri)
```

---

## 8. Failure Mode Postmortem

An AIE at a 200-person B2B AI company worked as backend engineer. No LLM stack. No AI features. The PM asked: 'Where's our AI strategy?' The AIE had no answer.

What the first AIE missed: what an ai engineer actually does is a system. The first AIE had no system. The second AIE had 4 mental models + 3 frameworks + 5 criteria. The system is the leverage.

The lesson: the AIE who has the system has what an ai engineer actually does. The AIE who has no system has the failure mode.

---

## 9. Self-Assessment Rubric

| 1 | **4 AIE pillars** | 0-1 | 2-3 | 4 pillars |
| 2 | **3 AIE metrics** | 0-1 | 2 | 3 metrics |
| 3 | **5-criterion bar** | 0-2 | 3-4 | 5 criteria |
| 4 | **AI features per quarter** | 0 | 1-2 | 3+ |
| 5 | **Latency p99** | >1s | 200ms-1s | <200ms |


**Disqualifier:** any 1 on dimension 1 or 3. An AIE who has 0-1 pillars or 0-2 criteria is in the SWE-Only or No-LLM-Stack failure mode.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-01-aie-aie-role.md` - interview evidence for "Walk me through your AI feature output." (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through your AIE weekly cadence.**
2. **No AI features shipped. What do you do?**
3. **The PM questions your LLM choice. What do you do?**
4. **You spend 80% of time on infra. What do you do?**
5. **Walk me through an AI feature you've shipped.**
