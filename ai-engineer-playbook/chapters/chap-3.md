# AI Engineer Playbook
## Chapter 3

# LLM Stack Selection

> *"The AIE selects the LLM stack. The 4-stack-pillar framework (model + serving + orchestration + observability), the 3-decision templates (OpenAI + Anthropic + open-source), and the 5-criterion stack quality bar are the AIE's reference for LLM stack at the contributor level."*

---

## 1. Epigraph

_The AIE selects the LLM stack. The 4-stack-pillar framework (model + serving + orchestration + observability), the 3-decision templates (OpenAI + Anthropic + open-source), and the 5-criterion stack quality bar are the AIE's reference for LLM stack at the contributor level._

---

## 2. Problem

You are an AIE at acme-corp. The engineering manager has just told you: "llm stack selection. 30-day timeline."

This chapter tells you the 4 mental models, 3 frameworks, and 5-criterion quality bar.

**Decision in one sentence:** _AIE LLM stack selection is a 4-pillar framework + 3 decision templates + 5-criterion bar; the AIE's job is to design the LLM stack, validate with eval, and own the stack quality._

---

## 3. Why AIEs Fail Here

Five named failure modes of AIEs whose llm stack selection produced zero results.

- **The No-Stack Failure.** No LLM stack. Ad-hoc API calls.
- **The Vendor-Lock-In Failure.** 100% vendor lock-in.
- **The No-Eval Failure.** No eval harness. Quality varies.
- **The No-Observability Failure.** No observability. No debugging.
- **The No-Cost-Control Failure.** No cost control.

---

## 4. Mental Models

Four mental models that compress llm stack selection.

**mental model 1: The 4 Stack Pillars:** 4 pillars: model + serving + orchestration + observability.

**mental model 2: The 3 Decision Templates:** 3 templates: OpenAI + Anthropic + open-source.

**mental model 3: The 5-Criterion Bar:** 5 criteria: latency + cost + quality + reliability + safety.

**mental model 4: The Stack Comparison:** Side-by-side comparison.

---

## 5. Frameworks

Three frameworks for llm stack selection.

### Framework 1: The 1-Page Plan

```
# LLM Stack Selection - [Date]

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

You are an AIE at **acme-corp**. The engineering manager has given you 30 days to design the llm stack selection system.

You have **90 minutes**. Produce the **llm stack selection redesign** using the 3 frameworks above. Specify:

- The 1-page plan.
- The implementation tracker.
- The retrospective review template.
- The 30-day timeline.
- The 1 thing you'll say to the engineering manager in the first review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-03-aie-aie-llm-stack.md` - under 1500 words.

---

## 7. Worked Example

**The 1-page stack decision:**

```
# LLM Stack Decision - 2026-09-01

## Models
- GPT-4 (primary)
- Claude (secondary)
- OSS Llama (fallback)
```

---

## 8. Failure Mode Postmortem

An AIE at a 200-person B2B AI company had no LLM stack. Ad-hoc OpenAI calls. Vendor lock-in. The CTO asked: 'What's our LLM strategy?' The AIE had no answer.

What the first AIE missed: llm stack selection is a system. The first AIE had no system. The second AIE had 4 mental models + 3 frameworks + 5 criteria. The system is the leverage.

The lesson: the AIE who has the system has llm stack selection. The AIE who has no system has the failure mode.

---

## 9. Self-Assessment Rubric

| 1 | **4 stack pillars** | 0-1 | 2-3 | 4 pillars |
| 2 | **3 decision templates** | 1 | 2 | 3 templates |
| 3 | **5-criterion bar** | 0-2 | 3-4 | 5 criteria |
| 4 | **LLM vendors in stack** | 1 | 2 | 3+ |
| 5 | **Eval coverage** | <50% | 50-90% | 100% of LLM features |


**Disqualifier:** any 1 on dimension 1 or 3. An AIE who has no stack or vendor lock-in is in the No-Stack or Vendor-Lock-In failure mode.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-03-aie-aie-llm-stack.md` - interview evidence for "Walk me through your LLM stack." (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through your LLM stack decision.**
2. **Vendor lock-in is too high. What do you do?**
3. **Quality varies across runs. What do you do?**
4. **You have 3 LLM options. How do you prioritize?**
5. **Walk me through a stack decision you've made.**
