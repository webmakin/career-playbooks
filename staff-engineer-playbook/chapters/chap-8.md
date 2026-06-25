# Staff Engineer Playbook
## Chapter 8

# Production Reliability and Observability

> *"The SE owns production reliability. The 4-reliability-pillar framework (SLOs + monitoring + alerting + incident response), the 3-reliability templates (logs + metrics + traces), and the 5-criterion reliability quality bar are the SE's reference for reliability at the principal IC level."*

---

## 1. Epigraph

_The SE owns production reliability. The 4-reliability-pillar framework (SLOs + monitoring + alerting + incident response), the 3-reliability templates (logs + metrics + traces), and the 5-criterion reliability quality bar are the SE's reference for reliability at the principal IC level._

---

## 2. Problem

You are a Staff Engineer at acme-corp. The engineering director has just told you: "production reliability and observability. 30-day timeline."

This chapter tells you the 4 mental models, 3 frameworks, and 5-criterion quality bar.

**Decision in one sentence:** _SE production reliability is a 4-pillar framework + 3 reliability templates + 5-criterion bar; the SE's job is to design reliability, validate them, and own the production quality._

---

## 3. Why Staff Engineers Fail Here

Five named failure modes of Staff Engineers whose production reliability and observability produced zero results.

- **The No-SLOs Failure.** No SLOs. No reliability target.
- **The No-Monitoring Failure.** No monitoring. Can't measure.
- **The No-Alerting Failure.** No alerting. Silent failures.
- **The No-Incident-Response Failure.** No incident response.
- **The No-RCA Failure.** No root cause analysis.

---

## 4. Mental Models

Four mental models that compress production reliability and observability.

**mental model 1: The 4 Reliability Pillars:** 4 pillars: SLOs + monitoring + alerting + incident response.

**mental model 2: The 3 Reliability Templates:** 3 templates: logs + metrics + traces.

**mental model 3: The 5-Criterion Bar:** 5 criteria: SLO-defined + monitored + alerted + responded + RCA'd.

**mental model 4: The SLO Card:** 1-page SLO card.

---

## 5. Frameworks

Three frameworks for production reliability and observability.

### Framework 1: The 1-Page Plan

```
# Production Reliability and Observability - [Date]

## Top 3 strategic inputs
1. [Input 1]
2. [Input 2]
3. [Input 3]

## The 5-criterion bar applied

## The 1 thing the SE will NOT compromise on
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

You are a Staff Engineer at **acme-corp**. The engineering director has given you 30 days to design the production reliability and observability system.

You have **90 minutes**. Produce the **production reliability and observability redesign** using the 3 frameworks above. Specify:

- The 1-page plan.
- The implementation tracker.
- The retrospective review template.
- The 30-day timeline.
- The 1 thing you'll say to the engineering director in the first review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-08-se-se-reliability.md` - under 1500 words.

---

## 7. Worked Example

**The 1-page SLO card:**

```
# SLO Card - B2B API

## Availability
- 99.9% monthly

## Latency
- p99 < 200ms
```

---

## 8. Failure Mode Postmortem

An SE at a 200-person company had no SLOs. Production failures invisible. Customer churned. The VP Eng said: 'No SLOs, no production.'

What the first Staff Engineer missed: production reliability and observability is a system. The first SE had no system. The second SE had 4 mental models + 3 frameworks + 5 criteria. The system is the leverage.

The lesson: the SE who has the system has production reliability and observability. The SE who has no system has the failure mode.

---

## 9. Self-Assessment Rubric

| 1 | **4 reliability pillars** | 0-1 | 2-3 | 4 pillars |
| 2 | **3 reliability templates** | 1 | 2 | 3 templates |
| 3 | **5-criterion bar** | 0-2 | 3-4 | 5 criteria |
| 4 | **Availability** | <99.5% | 99.5-99.9% | 99.9%+ |
| 5 | **MTTR** | >4 hours | 1-4 hours | <1 hour |


**Disqualifier:** any 1 on dimension 1 or 3. An SE who has no SLOs or no monitoring is in the No-SLOs or No-Monitoring failure mode.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-08-se-se-reliability.md` - interview evidence for "Walk me through your reliability system." (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through your reliability system.**
2. **Production is failing. What do you do?**
3. **Customer A churned. What do you do?**
4. **You have 3 reliability strategies. How do you prioritize?**
5. **Walk me through an incident response you've led.**
