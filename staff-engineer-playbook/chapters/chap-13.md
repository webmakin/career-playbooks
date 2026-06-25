# Staff Engineer Playbook
## Chapter 13

# Production Operations Excellence

> *"The SE owns production operations. The 4-ops-pillar framework (deployment + monitoring + incident + post-mortem), the 3-ops templates (deploy + monitor + respond), and the 5-criterion ops quality bar are the SE's reference for ops at the principal IC level."*

---

## 1. Epigraph

_The SE owns production operations. The 4-ops-pillar framework (deployment + monitoring + incident + post-mortem), the 3-ops templates (deploy + monitor + respond), and the 5-criterion ops quality bar are the SE's reference for ops at the principal IC level._

---

## 2. Problem

You are a Staff Engineer at acme-corp. The engineering director has just told you: "production operations excellence. 30-day timeline."

This chapter tells you the 4 mental models, 3 frameworks, and 5-criterion quality bar.

**Decision in one sentence:** _SE production ops is a 4-pillar framework + 3 templates + 5-criterion bar; the SE's job is to design ops, run the cadence, and own the production quality._

---

## 3. Why Staff Engineers Fail Here

Five named failure modes of Staff Engineers whose production operations excellence produced zero results.

- **The Manual-Deploy Failure.** Manual deploys.
- **The No-Monitoring Failure.** No monitoring.
- **The No-Incident-Response Failure.** No incident response.
- **The No-Post-Mortem Failure.** No post-mortem.
- **The Repeat-Incidents Failure.** Repeat incidents.

---

## 4. Mental Models

Four mental models that compress production operations excellence.

**mental model 1: The 4 Ops Pillars:** 4 pillars: deployment + monitoring + incident + post-mortem.

**mental model 2: The 3 Ops Templates:** 3 templates: deploy + monitor + respond.

**mental model 3: The 5-Criterion Bar:** 5 criteria: deployed + monitored + responded + post-mortemed + improved.

**mental model 4: The Ops Card:** 1-page ops card.

---

## 5. Frameworks

Three frameworks for production operations excellence.

### Framework 1: The 1-Page Plan

```
# Production Operations Excellence - [Date]

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

You are a Staff Engineer at **acme-corp**. The engineering director has given you 30 days to design the production operations excellence system.

You have **90 minutes**. Produce the **production operations excellence redesign** using the 3 frameworks above. Specify:

- The 1-page plan.
- The implementation tracker.
- The retrospective review template.
- The 30-day timeline.
- The 1 thing you'll say to the engineering director in the first review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-13-se-se-ops.md` - under 1500 words.

---

## 7. Worked Example

**The 1-page ops card:**

```
# Ops Card - Q3 2026

## Deployment
- ArgoCD
- Canary rollout
```

---

## 8. Failure Mode Postmortem

An SE at a 200-person company had manual deploys. 6-hour outage. The VP Eng said: 'No manual deploys, no production.'

What the first Staff Engineer missed: production operations excellence is a system. The first SE had no system. The second SE had 4 mental models + 3 frameworks + 5 criteria. The system is the leverage.

The lesson: the SE who has the system has production operations excellence. The SE who has no system has the failure mode.

---

## 9. Self-Assessment Rubric

| 1 | **4 ops pillars** | 0-1 | 2-3 | 4 pillars |
| 2 | **3 templates** | 1 | 2 | 3 templates |
| 3 | **5-criterion bar** | 0-2 | 3-4 | 5 criteria |
| 4 | **Deploy frequency** | <1/week | 1-5/week | 5+/week |
| 5 | **Repeat incidents** | >2/quarter | 0-2/quarter | 0 |


**Disqualifier:** any 1 on dimension 1 or 3. An SE who has manual deploys or no monitoring is in the Manual-Deploy or No-Monitoring failure mode.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-13-se-se-ops.md` - interview evidence for "Walk me through your ops process." (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through your ops process.**
2. **Production is failing. What do you do?**
3. **The team is overwhelmed by incidents. What do you do?**
4. **Repeat incidents happen. What do you do?**
5. **Walk me through an ops improvement you've led.**
