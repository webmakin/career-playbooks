# AI Engineer Playbook
## Chapter 5

# Prompt Engineering

> *"The AIE owns prompt engineering. The 4-prompt-pillar framework (template + variables + examples + tests), the 3-prompt templates (zero-shot + few-shot + chain-of-thought), and the 5-criterion prompt quality bar are the AIE's reference for prompt engineering at the contributor level."*

---

## 1. Epigraph

_The AIE owns prompt engineering. The 4-prompt-pillar framework (template + variables + examples + tests), the 3-prompt templates (zero-shot + few-shot + chain-of-thought), and the 5-criterion prompt quality bar are the AIE's reference for prompt engineering at the contributor level._

---

## 2. Problem

You are an AIE at acme-corp. The engineering manager has just told you: "prompt engineering. 30-day timeline."

This chapter tells you the 4 mental models, 3 frameworks, and 5-criterion quality bar.

**Decision in one sentence:** _AIE prompt engineering is a 4-pillar framework + 3 prompt templates + 5-criterion bar; the AIE's job is to design prompts, version them, eval them, and own the prompt quality._

---

## 3. Why AIEs Fail Here

Five named failure modes of AIEs whose prompt engineering produced zero results.

- **The Prompts-in-Notebooks Failure.** Prompts in notebooks. Not versioned.
- **The No-Few-Shot Failure.** No examples. Quality drops.
- **The No-CoT Failure.** No chain-of-thought. Reasoning broken.
- **The No-Eval Failure.** No prompt eval harness.
- **The No-Version-Control Failure.** No version control.

---

## 4. Mental Models

Four mental models that compress prompt engineering.

**mental model 1: The 4 Prompt Pillars:** 4 pillars: template + variables + examples + tests.

**mental model 2: The 3 Prompt Templates:** 3 templates: zero-shot + few-shot + chain-of-thought.

**mental model 3: The 5-Criterion Bar:** 5 criteria: versioned + tested + evaluated + monitored + safe.

**mental model 4: The Prompt Template:** Reusable template.

---

## 5. Frameworks

Three frameworks for prompt engineering.

### Framework 1: The 1-Page Plan

```
# Prompt Engineering - [Date]

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

You are an AIE at **acme-corp**. The engineering manager has given you 30 days to design the prompt engineering system.

You have **90 minutes**. Produce the **prompt engineering redesign** using the 3 frameworks above. Specify:

- The 1-page plan.
- The implementation tracker.
- The retrospective review template.
- The 30-day timeline.
- The 1 thing you'll say to the engineering manager in the first review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-05-aie-aie-prompt.md` - under 1500 words.

---

## 7. Worked Example

**The 1-page prompt template:**

```
# Prompt Template - RAG Q&A

## System
You are a B2B AI assistant. Use the following context.

## Variables
{context}
{question}

## Examples
Q: [Example 1]
A: [Example 1]
```

---

## 8. Failure Mode Postmortem

An AIE at a 200-person B2B AI company kept prompts in notebooks. Quality varied. The PM said: 'Prompts in repo, or no LLM features.'

What the first AIE missed: prompt engineering is a system. The first AIE had no system. The second AIE had 4 mental models + 3 frameworks + 5 criteria. The system is the leverage.

The lesson: the AIE who has the system has prompt engineering. The AIE who has no system has the failure mode.

---

## 9. Self-Assessment Rubric

| 1 | **4 prompt pillars** | 0-1 | 2-3 | 4 pillars |
| 2 | **3 templates** | 1 | 2 | 3 templates |
| 3 | **5-criterion bar** | 0-2 | 3-4 | 5 criteria |
| 4 | **Prompt versions in repo** | 0 | 1-2 | 5+ |
| 5 | **Eval coverage** | <50% | 50-90% | 100% |


**Disqualifier:** any 1 on dimension 1 or 3. An AIE who has prompts in notebooks or no version control is in the Prompts-in-Notebooks or No-Version-Control failure mode.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-05-aie-aie-prompt.md` - interview evidence for "Walk me through your prompt engineering." (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through your prompt engineering process.**
2. **Quality varies across runs. What do you do?**
3. **The PM rejects the prompt. What do you do?**
4. **You have 5 prompts in flight. How do you prioritize?**
5. **Walk me through a prompt eval you've led.**
