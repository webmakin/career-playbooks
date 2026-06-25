# AI Engineer Playbook
## Chapter 9

# Cost Management for AI

> *"The AIE owns LLM cost. The 4-cost-pillar framework (model + caching + batching + routing), the 3-cost templates (per-token + per-request + per-feature), and the 5-criterion cost quality bar are the AIE's reference for cost management at the contributor level."*

---

## 1. Epigraph

_The AIE owns LLM cost. The 4-cost-pillar framework (model + caching + batching + routing), the 3-cost templates (per-token + per-request + per-feature), and the 5-criterion cost quality bar are the AIE's reference for cost management at the contributor level._

---

## 2. Problem

You are an AIE at acme-corp. The engineering manager has just told you: "cost management for ai. 30-day timeline."

This chapter tells you the 4 mental models, 3 frameworks, and 5-criterion quality bar.

**Decision in one sentence:** _AIE LLM cost management is a 4-pillar framework + 3 cost templates + 5-criterion bar; the AIE's job is to design cost controls, track spend, and own the cost quality._

---

## 3. Why AIEs Fail Here

Five named failure modes of AIEs whose cost management for ai produced zero results.

- **The No-Cost-Tracking Failure.** No cost tracking. Bill surprise.
- **The Wrong-Model-Tier Failure.** Using GPT-4 for simple tasks.
- **The No-Caching Failure.** No caching. Repeated calls.
- **The No-Batching Failure.** No batching. Inefficient.
- **The No-Routing Failure.** No model routing.

---

## 4. Mental Models

Four mental models that compress cost management for ai.

**mental model 1: The 4 Cost Pillars:** 4 pillars: model + caching + batching + routing.

**mental model 2: The 3 Cost Templates:** 3 templates: per-token + per-request + per-feature.

**mental model 3: The 5-Criterion Bar:** 5 criteria: tracked + tiered + cached + batched + routed.

**mental model 4: The Cost Tracker:** Per-feature tracker.

---

## 5. Frameworks

Three frameworks for cost management for ai.

### Framework 1: The 1-Page Plan

```
# Cost Management for AI - [Date]

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

You are an AIE at **acme-corp**. The engineering manager has given you 30 days to design the cost management for ai system.

You have **90 minutes**. Produce the **cost management for ai redesign** using the 3 frameworks above. Specify:

- The 1-page plan.
- The implementation tracker.
- The retrospective review template.
- The 30-day timeline.
- The 1 thing you'll say to the engineering manager in the first review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-09-aie-aie-cost.md` - under 1500 words.

---

## 7. Worked Example

**The 1-page cost tracker:**

```
# LLM Cost Tracker - Q3 2026

| Feature | Spend | Target | Status |
|---------|-------|--------|--------|
| RAG Q&A | $5K/mo | $3K/mo | OVER |
```

---

## 8. Failure Mode Postmortem

An AIE at a 200-person B2B AI company had no cost tracking. Monthly bill was $50K, target was $10K. The CFO said: 'No cost control, no LLM.'

What the first AIE missed: cost management for ai is a system. The first AIE had no system. The second AIE had 4 mental models + 3 frameworks + 5 criteria. The system is the leverage.

The lesson: the AIE who has the system has cost management for ai. The AIE who has no system has the failure mode.

---

## 9. Self-Assessment Rubric

| 1 | **4 cost pillars** | 0-1 | 2-3 | 4 pillars |
| 2 | **3 templates** | 1 | 2 | 3 templates |
| 3 | **5-criterion bar** | 0-2 | 3-4 | 5 criteria |
| 4 | **Cost per request** | >$0.10 | $0.01-0.10 | <$0.01 |
| 5 | **Cache hit rate** | <30% | 30-70% | 70%+ |


**Disqualifier:** any 1 on dimension 1 or 3. An AIE who has no tracking or wrong model tier is in the No-Cost-Tracking or Wrong-Model-Tier failure mode.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-09-aie-aie-cost.md` - interview evidence for "Walk me through your LLM cost management." (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through your LLM cost management.**
2. **The monthly bill is too high. What do you do?**
3. **The CFO rejects the LLM spend. What do you do?**
4. **You have 5 LLM features. How do you prioritize cost?**
5. **Walk me through a cost optimization you've led.**
