# Staff Engineer Playbook
## Chapter 12

# Migration and Modernization

> *"The SE owns migrations. The 4-migration-pillar framework (assessment + plan + execute + verify), the 3-migration templates (strangler + parallel + big-bang), and the 5-criterion migration quality bar are the SE's reference for migrations at the principal IC level."*

---

## 1. Epigraph

_The SE owns migrations. The 4-migration-pillar framework (assessment + plan + execute + verify), the 3-migration templates (strangler + parallel + big-bang), and the 5-criterion migration quality bar are the SE's reference for migrations at the principal IC level._

---

## 2. Problem

You are a Staff Engineer at acme-corp. The engineering director has just told you: "migration and modernization. 30-day timeline."

This chapter tells you the 4 mental models, 3 frameworks, and 5-criterion quality bar.

**Decision in one sentence:** _SE migration is a 4-pillar framework + 3 templates + 5-criterion bar; the SE's job is to assess, plan, execute, and verify migrations._

---

## 3. Why Staff Engineers Fail Here

Five named failure modes of Staff Engineers whose migration and modernization produced zero results.

- **The No-Assessment Failure.** No assessment.
- **The Big-Bang Failure.** Big-bang migration. Risky.
- **The No-Plan Failure.** No plan. Ad-hoc.
- **The No-Rollback Failure.** No rollback plan.
- **The No-Verification Failure.** No verification.

---

## 4. Mental Models

Four mental models that compress migration and modernization.

**mental model 1: The 4 Migration Pillars:** 4 pillars: assessment + plan + execute + verify.

**mental model 2: The 3 Migration Templates:** 3 templates: strangler + parallel + big-bang.

**mental model 3: The 5-Criterion Bar:** 5 criteria: assessed + planned + executed + verified + rolled-back-if-needed.

**mental model 4: The Migration Card:** 1-page migration card.

---

## 5. Frameworks

Three frameworks for migration and modernization.

### Framework 1: The 1-Page Plan

```
# Migration and Modernization - [Date]

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

You are a Staff Engineer at **acme-corp**. The engineering director has given you 30 days to design the migration and modernization system.

You have **90 minutes**. Produce the **migration and modernization redesign** using the 3 frameworks above. Specify:

- The 1-page plan.
- The implementation tracker.
- The retrospective review template.
- The 30-day timeline.
- The 1 thing you'll say to the engineering director in the first review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-12-se-se-migration.md` - under 1500 words.

---

## 7. Worked Example

**The 1-page migration card:**

```
# Migration Card - DB to Postgres

## Strategy
Strangler

## Rollback
Read-only fallback
```

---

## 8. Failure Mode Postmortem

An SE at a 200-person company did a big-bang migration. 4-hour outage. Customer churned. The VP Eng said: 'No big-bang migrations.'

What the first Staff Engineer missed: migration and modernization is a system. The first SE had no system. The second SE had 4 mental models + 3 frameworks + 5 criteria. The system is the leverage.

The lesson: the SE who has the system has migration and modernization. The SE who has no system has the failure mode.

---

## 9. Self-Assessment Rubric

| 1 | **4 migration pillars** | 0-1 | 2-3 | 4 pillars |
| 2 | **3 templates** | 1 | 2 | 3 templates |
| 3 | **5-criterion bar** | 0-2 | 3-4 | 5 criteria |
| 4 | **Migration rollbacks** | >1/year | 0-1/year | 0 |
| 5 | **Migration time** | >6 months | 3-6 months | <3 months |


**Disqualifier:** any 1 on dimension 1 or 3. An SE who has no assessment or no rollback is in the No-Assessment or No-Rollback failure mode.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-12-se-se-migration.md` - interview evidence for "Walk me through your migration process." (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through your migration process.**
2. **The migration is failing. What do you do?**
3. **You have 3 migration options. How do you prioritize?**
4. **Customer A is impacted. What do you do?**
5. **Walk me through a migration you've led.**
