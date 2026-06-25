# AI Engineer Playbook
## Chapter 7

# Agent Design and Tool Use

> *"The AIE designs agents. The 4-agent-pillar framework (planning + tool use + memory + reflection), the 3-agent templates (single + multi + hierarchical), and the 5-criterion agent quality bar are the AIE's reference for agent design at the contributor level."*

---

## 1. Epigraph

_The AIE designs agents. The 4-agent-pillar framework (planning + tool use + memory + reflection), the 3-agent templates (single + multi + hierarchical), and the 5-criterion agent quality bar are the AIE's reference for agent design at the contributor level._

---

## 2. Problem

You are an AIE at acme-corp. The engineering manager has just told you: "agent design and tool use. 30-day timeline."

This chapter tells you the 4 mental models, 3 frameworks, and 5-criterion quality bar.

**Decision in one sentence:** _AIE agent design is a 4-pillar framework + 3 agent templates + 5-criterion bar; the AIE's job is to design agents, validate them, and own the agent quality._

---

## 3. Why AIEs Fail Here

Five named failure modes of AIEs whose agent design and tool use produced zero results.

- **The No-Planning Failure.** No planning. Agent confused.
- **The No-Tools Failure.** No tool integration. Useless agent.
- **The No-Memory Failure.** No memory. Forgets context.
- **The No-Reflection Failure.** No self-correction. Hallucinates.
- **The No-Eval Failure.** No agent eval.

---

## 4. Mental Models

Four mental models that compress agent design and tool use.

**mental model 1: The 4 Agent Pillars:** 4 pillars: planning + tool use + memory + reflection.

**mental model 2: The 3 Agent Templates:** 3 templates: single + multi + hierarchical.

**mental model 3: The 5-Criterion Bar:** 5 criteria: planned + tooled + memorized + reflected + evaluated.

**mental model 4: The Agent Card:** 1-page agent card.

---

## 5. Frameworks

Three frameworks for agent design and tool use.

### Framework 1: The 1-Page Plan

```
# Agent Design and Tool Use - [Date]

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

You are an AIE at **acme-corp**. The engineering manager has given you 30 days to design the agent design and tool use system.

You have **90 minutes**. Produce the **agent design and tool use redesign** using the 3 frameworks above. Specify:

- The 1-page plan.
- The implementation tracker.
- The retrospective review template.
- The 30-day timeline.
- The 1 thing you'll say to the engineering manager in the first review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-07-aie-aie-agents.md` - under 1500 words.

---

## 7. Worked Example

**The 1-page agent card:**

```
# Agent Card - B2B Research Agent

## Planning
- ReAct

## Tools
- Web search
- DB query
```

---

## 8. Failure Mode Postmortem

An AIE at a 200-person B2B AI company shipped an agent with no planning. The agent hallucinated. The PM said: 'No planning, no agent.'

What the first AIE missed: agent design and tool use is a system. The first AIE had no system. The second AIE had 4 mental models + 3 frameworks + 5 criteria. The system is the leverage.

The lesson: the AIE who has the system has agent design and tool use. The AIE who has no system has the failure mode.

---

## 9. Self-Assessment Rubric

| 1 | **4 agent pillars** | 0-1 | 2-3 | 4 pillars |
| 2 | **3 templates** | 1 | 2 | 3 templates |
| 3 | **5-criterion bar** | 0-2 | 3-4 | 5 criteria |
| 4 | **Tool count** | 0 | 1-2 | 5+ |
| 5 | **Eval coverage** | <50% | 50-90% | 100% |


**Disqualifier:** any 1 on dimension 1 or 3. An AIE who has no planning or no memory is in the No-Planning or No-Memory failure mode.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-07-aie-aie-agents.md` - interview evidence for "Walk me through your agent design." (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through your agent design process.**
2. **The agent hallucinates. What do you do?**
3. **The PM rejects the agent. What do you do?**
4. **You have 3 agent strategies. How do you prioritize?**
5. **Walk me through an agent eval you've led.**
