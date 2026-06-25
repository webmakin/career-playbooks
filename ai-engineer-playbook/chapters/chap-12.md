# AI Engineer Playbook
## Chapter 12

# Safety and Guardrails

> *"The AIE owns safety. The 4-safety-pillar framework (input filter + output filter + jailbreak detection + PII detection), the 3-safety templates (regex + classifier + LLM-as-judge), and the 5-criterion safety quality bar are the AIE's reference for safety at the contributor level."*

---

## 1. Epigraph

_The AIE owns safety. The 4-safety-pillar framework (input filter + output filter + jailbreak detection + PII detection), the 3-safety templates (regex + classifier + LLM-as-judge), and the 5-criterion safety quality bar are the AIE's reference for safety at the contributor level._

---

## 2. Problem

You are an AIE at acme-corp. The engineering manager has just told you: "safety and guardrails. 30-day timeline."

This chapter tells you the 4 mental models, 3 frameworks, and 5-criterion quality bar.

**Decision in one sentence:** _AIE safety design is a 4-pillar framework + 3 safety templates + 5-criterion bar; the AIE's job is to design safety guardrails, validate them, and own the safety quality._

---

## 3. Why AIEs Fail Here

Five named failure modes of AIEs whose safety and guardrails produced zero results.

- **The No-Input-Filter Failure.** No input filter.
- **The No-Output-Filter Failure.** No output filter. Toxic content.
- **The No-Jailbreak-Detection Failure.** No jailbreak detection.
- **The No-PII-Detection Failure.** No PII detection.
- **The No-Safety-Eval Failure.** No safety eval.

---

## 4. Mental Models

Four mental models that compress safety and guardrails.

**mental model 1: The 4 Safety Pillars:** 4 pillars: input filter + output filter + jailbreak detection + PII detection.

**mental model 2: The 3 Safety Templates:** 3 templates: regex + classifier + LLM-as-judge.

**mental model 3: The 5-Criterion Bar:** 5 criteria: filtered + jailbreak-detected + PII-redacted + tested + monitored.

**mental model 4: The Safety Card:** 1-page safety card.

---

## 5. Frameworks

Three frameworks for safety and guardrails.

### Framework 1: The 1-Page Plan

```
# Safety and Guardrails - [Date]

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

You are an AIE at **acme-corp**. The engineering manager has given you 30 days to design the safety and guardrails system.

You have **90 minutes**. Produce the **safety and guardrails redesign** using the 3 frameworks above. Specify:

- The 1-page plan.
- The implementation tracker.
- The retrospective review template.
- The 30-day timeline.
- The 1 thing you'll say to the engineering manager in the first review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-12-aie-aie-safety.md` - under 1500 words.

---

## 7. Worked Example

**The 1-page safety card:**

```
# Safety Card - B2B AI

## Input filter
- Profanity regex
- PII detector
```

---

## 8. Failure Mode Postmortem

An AIE at a 200-person B2B AI company had no safety guardrails. Customer PII leaked. The CTO said: 'No safety, no LLM in production.'

What the first AIE missed: safety and guardrails is a system. The first AIE had no system. The second AIE had 4 mental models + 3 frameworks + 5 criteria. The system is the leverage.

The lesson: the AIE who has the system has safety and guardrails. The AIE who has no system has the failure mode.

---

## 9. Self-Assessment Rubric

| 1 | **4 safety pillars** | 0-1 | 2-3 | 4 pillars |
| 2 | **3 templates** | 1 | 2 | 3 templates |
| 3 | **5-criterion bar** | 0-2 | 3-4 | 5 criteria |
| 4 | **Jailbreak success rate** | >5% | 1-5% | <1% |
| 5 | **PII leak incidents** | >1/quarter | 0-1/quarter | 0 |


**Disqualifier:** any 1 on dimension 1 or 3. An AIE who has no input filter or no PII detection is in the No-Input-Filter or No-PII-Detection failure mode.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-12-aie-aie-safety.md` - interview evidence for "Walk me through your safety system." (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through your safety system.**
2. **A jailbreak was successful. What do you do?**
3. **Customer PII leaked. What do you do?**
4. **You have 3 safety strategies. How do you prioritize?**
5. **Walk me through a safety incident you've resolved.**
