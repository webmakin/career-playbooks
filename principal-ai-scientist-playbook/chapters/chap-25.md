# Principal AI Scientist Playbook
## Chapter 25

# PAS Research Auditability and Decision Logs

> *"The PAS owns research auditability. The 4 decision-log pillars, the 3 audit cycles, and the 5-criterion audit quality bar are the PAS's reference for research auditability at the principal level."*

---

## 1. Epigraph

_The PAS owns research auditability. The 4 decision-log pillars, the 3 audit cycles, and the 5-criterion audit quality bar are the PAS's reference for research auditability at the principal level._

---

## 2. Problem

You are a PAS at acme-corp. The CTO has just told you: "FY33 pas research auditability and decision logs. 30-day timeline."

This chapter tells you the 4 mental models, 3 frameworks, and 5-criterion quality bar.

**Decision in one sentence:** _PAS research auditability is a 4-pillar system (paper ADRs + experiment logs + risk register + compliance tracker) with 3 audit cycles and 5-criterion bar; the PAS's job is to design the decision-log system, run the audits, and own the documentation._

---

## 3. Why PASs Fail Here

Five named failure modes of PASs whose pas research auditability and decision logs produced zero results.

- **The No-ADR Failure.** No paper ADRs.
- **The No-Experiment-Log Failure.** No experiment logs.
- **The No-Risk-Register Failure.** No risk register.
- **The No-Compliance-Tracker Failure.** No compliance tracker.
- **The Verbals-Only Failure.** Decisions are verbal.

---

## 4. Mental Models

Four mental models that compress pas research auditability and decision logs.

**mental model 1: The 4 Decision-Log Pillars:** 4 pillars: paper ADRs + experiment logs + risk register + compliance.

**mental model 2: The 3 Audit Cycles:** 3 cycles: real-time + quarterly + annual.

**mental model 3: The 5-Criterion Bar:** 5 criteria: documented + owned + reviewed + archived + auditable.

**mental model 4: The Paper ADR Template:** 7 sections.

---

## 5. Frameworks

Three frameworks for pas research auditability and decision logs.

### Framework 1: The 1-Page Plan

```
# PAS Research Auditability and Decision Logs - [Date]

## Top 3 strategic inputs
1. [Input 1]
2. [Input 2]
3. [Input 3]

## The 5-criterion bar applied

## The 1 thing the PAS will NOT compromise on
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

You are a PAS at **acme-corp**. The CTO has given you 30 days to design the pas research auditability and decision logs system.

You have **90 minutes**. Produce the **pas research auditability and decision logs redesign** using the 3 frameworks above. Specify:

- The 1-page plan.
- The implementation tracker.
- The retrospective review template.
- The 30-day timeline.
- The 1 thing you'll say to the CTO in the first review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-25-pas-pas-research-auditability.md` - under 1500 words.

---

## 7. Worked Example

**The 1-page auditability system:**

```
# Research Auditability System - 2026-09-01

## The 4 pillars
1. Paper ADRs (every paper decision)
2. Experiment logs (every experiment)
3. Risk register (20+ risks)
4. Compliance tracker
```

---

## 8. Failure Mode Postmortem

A PAS at a 200-person B2B AI company had no auditability system. ADRs were verbal. Experiment logs missing. Risk register didn't exist. Audit failed.

What the first PAS missed: pas research auditability and decision logs is a system. The first PAS had no system. The second PAS had 4 mental models + 3 frameworks + 5 criteria. The system is the leverage.

The lesson: the PAS who has the system has pas research auditability and decision logs. The PAS who has no system has the failure mode.

---

## 9. Self-Assessment Rubric

| 1 | **4 decision-log pillars** | 0-1 | 2-3 | 4 pillars |
| 2 | **3 audit cycles** | 1 | 2 | 3 cycles |
| 3 | **5-criterion bar** | 0-2 | 3-4 | 5 criteria |
| 4 | **ADR coverage** | <50% | 50-90% | 100% of paper decisions |
| 5 | **Experiment log coverage** | <50% | 50-90% | 100% of experiments |

**Disqualifier:** any 1 on dimension 1 or 2. A PAS who has 0-1 pillars or 1 cycle is in the No-ADR or Verbals-Only failure mode.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-25-pas-pas-research-auditability.md` - interview evidence for "How do you run research auditability?" (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through your research auditability system.**
2. **The board wants decision logs. What do you do?**
3. **AI safety audit failed. What do you do?**
4. **An experiment decision was verbal. What do you do?**
5. **Walk me through an ADR you've written.**
