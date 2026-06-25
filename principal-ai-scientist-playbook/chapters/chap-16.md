# Principal AI Scientist Playbook
## Chapter 16

# PAS Build vs Buy for Research Tools

> *"The PAS owns research tool build vs buy. The 4-factor decision framework (cost + differentiation + timeline + maintenance), the 3 buy scenarios, and the 5-criterion build quality bar are the PAS's reference for research tool decisions at the principal level."*

---

## 1. Epigraph

_The PAS owns research tool build vs buy. The 4-factor decision framework (cost + differentiation + timeline + maintenance), the 3 buy scenarios, and the 5-criterion build quality bar are the PAS's reference for research tool decisions at the principal level._

---

## 2. Problem

You are a PAS at acme-corp. The CTO has just told you: "5 build vs buy decisions for research tools: experiment tracking (build vs W&B), data labeling (build vs Scale), hyperparameter tuning (build vs Optuna), serving (build vs HF Inference Endpoints), paper writing (build vs Overleaf). $2M budget, 90 days."

This chapter tells you the 4 mental models, 3 frameworks, and 5-criterion quality bar.

**Decision in one sentence:** _PAS build vs buy for research tools is a 4-factor framework (cost + differentiation + timeline + maintenance) with 3 buy scenarios (commodity + leader + parity) and 5-criterion build quality bar; the PAS's job is to design the framework, evaluate each decision, and own the build vs buy choice._

---

## 3. Why PASs Fail Here

Five named failure modes of PASs whose pas build vs buy for research tools produced zero results.

- **The Not-Invented-Here Failure.** PAS always builds. Misses commodity buys.
- **The Always-Buy Failure.** PAS always buys. Misses differentiation.
- **The No-TCO Failure.** PAS doesn't calculate total cost of ownership.
- **The No-Differentiation Failure.** PAS doesn't assess differentiation.
- **The No-Maintenance Failure.** PAS ignores maintenance cost.

---

## 4. Mental Models

Four mental models that compress pas build vs buy for research tools.

**mental model 1: The 4-Factor Decision Framework:** 4 factors: cost + differentiation + timeline + maintenance.

**mental model 2: The 3 Buy Scenarios:** 3 scenarios: commodity (always buy), clear leader (usually buy), parity (case-by-case).

**mental model 3: The 5-Criterion Build Quality Bar:** 5 criteria: differentiation + cost + timeline + maintenance + talent.

**mental model 4: The TCO Calculator:** 3-year total cost: build IC cost + ongoing maintenance vs buy license + integration.

---

## 5. Frameworks

Three frameworks for pas build vs buy for research tools.

### Framework 1: The 1-Page Plan

```
# PAS Build vs Buy for Research Tools — [Date]

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
# Implementation Tracker — [Quarter]

| Item | Owner | Status | Date |
|------|-------|--------|------|
| [Item 1] | [Name] | [Status] | [Date] |
| [Item 2] | ... | | |
```

### Framework 3: The Retrospective Review

```
# Retrospective Review — [Date]

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

You are a PAS at **acme-corp**. The CTO has given you 30 days to design the pas build vs buy for research tools system.

5 build vs buy decisions for research tools: experiment tracking (build vs W&B), data labeling (build vs Scale), hyperparameter tuning (build vs Optuna), serving (build vs HF Inference Endpoints), paper writing (build vs Overleaf). $2M budget, 90 days.

You have **90 minutes**. Produce the **pas build vs buy for research tools redesign** using the 3 frameworks above. Specify:

- The 1-page plan.
- The implementation tracker.
- The retrospective review template.
- The 30-day timeline.
- The 1 thing you'll say to the CTO in the first review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-16-pas-pas-build-vs-buy.md` — under 1500 words.

---

## 7. Worked Example

**The 4-factor decision matrix:**

```
# Build vs Buy Decision Matrix - Q4 2026

| Decision | Build TCO | Buy TCO | Diff | Time | Maint | Winner |
|----------|-----------|---------|------|------|-------|--------|
| Experiment tracking | $500K | $100K | LOW | Now | Vendor | BUY (W&B) |
| Hyperparameter tuning | $300K | $50K | LOW | Now | Vendor | BUY (Optuna) |
| Serving | $800K | $200K | HIGH | Q1-Q2 | 0.5 RS | BUILD |
| Paper writing | $100K | $20K | LOW | Now | Vendor | BUY (Overleaf) |
| Data labeling | $600K | $400K | LOW | Now | Vendor | BUY (Scale) |
```

**The 1 thing I'll say to the CTO in the first review:**

```
"1. **Walk me through your build vs buy framework.**
2. **The PAS always builds. What do you do?**
3. **You have a $2M budget and 5 decisions. How do you prioritize?**
4. **A buy decision has hidden integration costs. What do you do?**
5. **Walk me through a build vs buy decision you've made.**

  Top 3 outcomes:
  1. [Outcome 1]
  2. [Outcome 2]
  3. [Outcome 3]

  Top 3 risks:
  1. [Risk 1]
  2. [Risk 2]
  3. [Risk 3]

  The 1 thing I want to focus on: [focus].

  The 1 thing I will NOT compromise on: [non-negotiable].

  PAS Build vs Buy for Research Tools is the discipline. [Outcome] is the outcome."
```

**The 3 things I'll do to avoid the 5 failure modes:**

```
1. [Avoidance 1]
   (Avoids the [failure 1].)
   - [Specific action]

2. [Avoidance 2]
   (Avoids the [failure 2].)
   - [Specific action]

3. [Avoidance 3]
   (Avoids the [failure 3].)
   - [Specific action]
```

---

## 8. Failure Mode Postmortem

A PAS at a 200-person B2B AI company had no build vs buy framework. Always built. Experiment tracking was built (4 RSs × 2 quarters = $400K + maintenance) when W&B was $50K/year.

What the first PAS missed: pas build vs buy for research tools is a system. The first PAS had no system. The second PAS had 4 mental models + 3 frameworks + 5 criteria. The system is the leverage.

The lesson: the PAS who has [system] has pas build vs buy for research tools. The PAS who has [no system] has [bad outcome].

---

## 9. Self-Assessment Rubric

How do you make research tool build vs buy decisions?

**Disqualifier:**

| 1 | **4-factor framework** | 1 factor | 2-3 | 4 factors |
| 2 | **3 buy scenarios** | 1 | 2 | 3 (commodity + leader + parity) |
| 3 | **5-criterion bar** | 0-2 | 3-4 | 5 (differentiation + cost + time + maint + talent) |
| 4 | **TCO calculator** | None | TCO exists | 3-year TCO per decision |
| 5 | **Build vs buy track record** | Always build or buy | Mixed | 60-70% buy, 30-40% build |

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-16-pas-pas-build-vs-buy.md` — interview evidence for "1. **Walk me through your build vs buy framework.**
2. **The PAS always builds. What do you do?**
3. **You have a $2M budget and 5 decisions. How do you prioritize?**
4. **A buy decision has hidden integration costs. What do you do?**
5. **Walk me through a build vs buy decision you've made.**" (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

any 1 on dimension 1 or 3. A PAS who has 1 factor or 0-2 criteria is in the Not-Invented-Here or No-Differentiation failure mode.
