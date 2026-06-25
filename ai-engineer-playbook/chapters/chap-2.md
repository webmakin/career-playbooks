# AI Engineer Playbook
## Chapter 2

# The IC-to-AIE Category Change

> *"The AIE is a category change. The IC-to-AIE transition requires 4 mindset shifts: from backend services to LLM calls, from deterministic to probabilistic, from unit tests to eval harnesses, and from feature ownership to prompt ownership."*

---

## 1. Epigraph

_The AIE is a category change. The IC-to-AIE transition requires 4 mindset shifts: from backend services to LLM calls, from deterministic to probabilistic, from unit tests to eval harnesses, and from feature ownership to prompt ownership._

---

## 2. Problem

You are an AIE at acme-corp. The engineering manager has just told you: "the ic-to-aie category change. 30-day timeline."

This chapter tells you the 4 mental models, 3 frameworks, and 5-criterion quality bar.

**Decision in one sentence:** _IC-to-AIE is a 4-mindset-shift category change (backend -> LLM, deterministic -> probabilistic, unit tests -> eval harnesses, feature ownership -> prompt ownership) with 3-month transition and 5-criterion bar._

---

## 3. Why AIEs Fail Here

Five named failure modes of AIEs whose the ic-to-aie category change produced zero results.

- **The Same-as-Backend Failure.** AIE works like backend. No LLM features.
- **The Deterministic-Thinking Failure.** Expects deterministic outputs.
- **The No-Eval-Harness Failure.** No eval harness. Manual testing.
- **The No-Prompt-Ownership Failure.** Prompts in notebooks.
- **The No-Cost-Thinking Failure.** No cost analysis.

---

## 4. Mental Models

Four mental models that compress the ic-to-aie category change.

**mental model 1: The 4 Mindset Shifts:** 4 shifts: backend -> LLM, deterministic -> probabilistic, unit tests -> eval harnesses, feature -> prompt.

**mental model 2: The 3-Month Transition:** 3 months: month 1 read LLM docs, month 2 first LLM feature, month 3 first prompt.

**mental model 3: The 5-Criterion Transition Bar:** 5 criteria: LLM features + eval harness + prompt versioning + cost + safety.

**mental model 4: The AIE vs Backend Comparison:** Side-by-side comparison.

---

## 5. Frameworks

Three frameworks for the ic-to-aie category change.

### Framework 1: The 1-Page Plan

```
# The IC-to-AIE Category Change - [Date]

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

You are an AIE at **acme-corp**. The engineering manager has given you 30 days to design the the ic-to-aie category change system.

You have **90 minutes**. Produce the **the ic-to-aie category change redesign** using the 3 frameworks above. Specify:

- The 1-page plan.
- The implementation tracker.
- The retrospective review template.
- The 30-day timeline.
- The 1 thing you'll say to the engineering manager in the first review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-02-aie-aie-category-change.md` - under 1500 words.

---

## 7. Worked Example

**The 1-page IC-to-AIE transition plan:**

```
# IC-to-AIE Transition - 2026-09-01

## Month 1: Read LLM docs
- 30 LLM papers (RAG, agents, eval)

## Month 2: First LLM feature
- RAG pipeline
```

---

## 8. Failure Mode Postmortem

An ML engineer at a 200-person B2B AI company tried to become an AIE. Worked like backend. 0 AI features. The PM said: 'You're still a backend engineer.'

What the first AIE missed: the ic-to-aie category change is a system. The first AIE had no system. The second AIE had 4 mental models + 3 frameworks + 5 criteria. The system is the leverage.

The lesson: the AIE who has the system has the ic-to-aie category change. The AIE who has no system has the failure mode.

---

## 9. Self-Assessment Rubric

| 1 | **4 mindset shifts** | 0-1 | 2-3 | 4 shifts |
| 2 | **3-month transition** | None | Partial | 3-month plan |
| 3 | **5-criterion bar** | 0-2 | 3-4 | 5 criteria |
| 4 | **AI features per quarter** | 0 | 1-2 | 3+ |
| 5 | **Prompt versions in repo** | 0 | 1-2 | 5+ |


**Disqualifier:** any 1 on dimension 1 or 3. An AIE who has 0-1 shifts or 0-2 criteria is in the Same-as-Backend or No-Prompt-Ownership failure mode.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-02-aie-aie-category-change.md` - interview evidence for "Walk me through your IC-to-AIE transition." (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through your IC-to-AIE transition.**
2. **0 AI features in the first 6 months. What do you do?**
3. **You spend 80% of time on infra. What do you do?**
4. **The PM says you're still a backend engineer. What do you do?**
5. **Walk me through your first AI feature as an AIE.**
