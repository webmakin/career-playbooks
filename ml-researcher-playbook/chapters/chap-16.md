# ML Researcher Playbook
## Chapter 16

# MLR Build vs Buy for Tools

> *"The MLR owns tool build vs buy. The 4-factor decision framework (cost + differentiation + timeline + maintenance), the 3 buy scenarios, and the 5-criterion build quality bar are the MLR's reference for tool decisions at the contributor level."*

---

## 1. Epigraph

_The MLR owns tool build vs buy. The 4-factor decision framework (cost + differentiation + timeline + maintenance), the 3 buy scenarios, and the 5-criterion build quality bar are the MLR's reference for tool decisions at the contributor level._

---

## 2. Problem

You are an MLR at acme-corp. The senior scientist has just told you: "mlr build vs buy for tools. 30-day timeline."

This chapter tells you the 4 mental models, 3 frameworks, and 5-criterion quality bar.

**Decision in one sentence:** _MLR tool build vs buy is a 4-factor framework + 3 buy scenarios + 5-criterion bar; the MLR's job is to design the framework, evaluate each decision, and own the build vs buy choice._

---

## 3. Why MLRs Fail Here

Five named failure modes of MLRs whose mlr build vs buy for tools produced zero results.

- **The Not-Invented-Here Failure.** Always builds.
- **The Always-Buy Failure.** Always buys.
- **The No-TCO Failure.** No total cost analysis.
- **The No-Differentiation Failure.** No differentiation analysis.
- **The No-Maintenance Failure.** Ignores maintenance.

---

## 4. Mental Models

Four mental models that compress mlr build vs buy for tools.

**mental model 1: The 4-Factor Decision Framework:** 4 factors: cost + differentiation + timeline + maintenance.

**mental model 2: The 3 Buy Scenarios:** 3 scenarios: commodity + leader + parity.

**mental model 3: The 5-Criterion Bar:** 5 criteria: differentiation + cost + timeline + maintenance + talent.

**mental model 4: The TCO Calculator:** 3-year total cost.

---

## 5. Frameworks

Three frameworks for mlr build vs buy for tools.

### Framework 1: The 1-Page Plan

```
# MLR Build vs Buy for Tools - [Date]

## Top 3 strategic inputs
1. [Input 1]
2. [Input 2]
3. [Input 3]

## The 5-criterion bar applied

## The 1 thing the MLR will NOT compromise on
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

You are an MLR at **acme-corp**. The senior scientist has given you 30 days to design the mlr build vs buy for tools system.

You have **90 minutes**. Produce the **mlr build vs buy for tools redesign** using the 3 frameworks above. Specify:

- The 1-page plan.
- The implementation tracker.
- The retrospective review template.
- The 30-day timeline.
- The 1 thing you'll say to the senior scientist in the first review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-16-mlr-mlr-build-vs-buy.md` - under 1500 words.

---

## 7. Worked Example

**The 4-factor decision matrix:**

```
# Build vs Buy - Q4 2026

| Tool | Build TCO | Buy TCO | Winner |
|------|-----------|---------|--------|
| Exp tracking | $500K | $100K | BUY (W&B) |
| HP tuning | $300K | $50K | BUY (Optuna) |
```

---

## 8. Failure Mode Postmortem

An MLR at a 200-person B2B AI company always built. Wasted 6 months building experiment tracking. The senior scientist said: 'Build vs buy is a decision.'

What the first MLR missed: mlr build vs buy for tools is a system. The first MLR had no system. The second MLR had 4 mental models + 3 frameworks + 5 criteria. The system is the leverage.

The lesson: the MLR who has the system has mlr build vs buy for tools. The MLR who has no system has the failure mode.

---

## 9. Self-Assessment Rubric

| 1 | **4-factor framework** | 1 | 2-3 | 4 factors |
| 2 | **3 buy scenarios** | 1 | 2 | 3 scenarios |
| 3 | **5-criterion bar** | 0-2 | 3-4 | 5 criteria |
| 4 | **TCO calculator** | None | TCO exists | 3-year TCO per decision |
| 5 | **Track record** | Always build/buy | Mixed | 60-70% buy, 30-40% build |


**Disqualifier:** any 1 on dimension 1 or 3. An MLR who always builds or always buys is in the Not-Invented-Here or Always-Buy failure mode.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-16-mlr-mlr-build-vs-buy.md` - interview evidence for "Walk me through your build vs buy framework." (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through your build vs buy framework.**
2. **You always build. What do you do?**
3. **You have a $500K budget and 5 decisions. How do you prioritize?**
4. **A buy decision has hidden costs. What do you do?**
5. **Walk me through a build vs buy decision you've made.**
