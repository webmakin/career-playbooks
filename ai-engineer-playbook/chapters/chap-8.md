# AI Engineer Playbook
## Chapter 8

# AI Observability

> *"The AIE owns AI observability. The 4-observability-pillar framework (logging + tracing + metrics + eval), the 3-observability templates (logs + traces + dashboards), and the 5-criterion observability quality bar are the AIE's reference for observability at the contributor level."*

---

## 1. Epigraph

_The AIE owns AI observability. The 4-observability-pillar framework (logging + tracing + metrics + eval), the 3-observability templates (logs + traces + dashboards), and the 5-criterion observability quality bar are the AIE's reference for observability at the contributor level._

---

## 2. Problem

You are an AIE at acme-corp. The engineering manager has just told you: "ai observability. 30-day timeline."

This chapter tells you the 4 mental models, 3 frameworks, and 5-criterion quality bar.

**Decision in one sentence:** _AIE AI observability is a 4-pillar framework + 3 observability templates + 5-criterion bar; the AIE's job is to design observability, run the dashboards, and own the observability quality._

---

## 3. Why AIEs Fail Here

Five named failure modes of AIEs whose ai observability produced zero results.

- **The No-Logs Failure.** No LLM logs.
- **The No-Tracing Failure.** No tracing. Can't debug.
- **The No-Metrics Failure.** No metrics. Can't measure.
- **The No-Eval-Metrics Failure.** No eval metrics. Quality invisible.
- **The No-Dashboards Failure.** No dashboards.

---

## 4. Mental Models

Four mental models that compress ai observability.

**mental model 1: The 4 Observability Pillars:** 4 pillars: logging + tracing + metrics + eval.

**mental model 2: The 3 Observability Templates:** 3 templates: logs + traces + dashboards.

**mental model 3: The 5-Criterion Bar:** 5 criteria: logged + traced + measured + evaluated + dashboarded.

**mental model 4: The Observability Stack:** Per-stack detail.

---

## 5. Frameworks

Three frameworks for ai observability.

### Framework 1: The 1-Page Plan

```
# AI Observability - [Date]

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

You are an AIE at **acme-corp**. The engineering manager has given you 30 days to design the ai observability system.

You have **90 minutes**. Produce the **ai observability redesign** using the 3 frameworks above. Specify:

- The 1-page plan.
- The implementation tracker.
- The retrospective review template.
- The 30-day timeline.
- The 1 thing you'll say to the engineering manager in the first review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-08-aie-aie-observability.md` - under 1500 words.

---

## 7. Worked Example

**The 1-page observability stack:**

```
# AI Observability Stack - 2026-09-01

## Logging
- LangSmith

## Tracing
- OpenTelemetry
```

---

## 8. Failure Mode Postmortem

An AIE at a 200-person B2B AI company had no observability. Production LLM issues invisible. Customer churned. The CTO said: 'No observability, no LLM in production.'

What the first AIE missed: ai observability is a system. The first AIE had no system. The second AIE had 4 mental models + 3 frameworks + 5 criteria. The system is the leverage.

The lesson: the AIE who has the system has ai observability. The AIE who has no system has the failure mode.

---

## 9. Self-Assessment Rubric

| 1 | **4 observability pillars** | 0-1 | 2-3 | 4 pillars |
| 2 | **3 templates** | 1 | 2 | 3 templates |
| 3 | **5-criterion bar** | 0-2 | 3-4 | 5 criteria |
| 4 | **Traced requests** | <50% | 50-90% | 100% |
| 5 | **Eval metrics** | 0 | 1-2 | 5+ |


**Disqualifier:** any 1 on dimension 1 or 3. An AIE who has no logs or no eval metrics is in the No-Logs or No-Eval-Metrics failure mode.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-08-aie-aie-observability.md` - interview evidence for "Walk me through your AI observability." (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through your AI observability system.**
2. **Production LLM is failing. What do you do?**
3. **The customer can't debug. What do you do?**
4. **You have 5 LLM features. How do you prioritize observability?**
5. **Walk me through an observability incident you've resolved.**
