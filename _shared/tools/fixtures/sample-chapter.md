# Building GPT From Scratch
## Chapter 99

# What Is a Director-Grade Decision?

> *"A decision is not the moment of choice. It is the chain of reasoning that made the choice obvious in hindsight."*

---

## 1. Epigraph

A decision is not the moment of choice. It is the chain of reasoning that made the choice obvious in hindsight.

---

## 2. Problem

The CEO has just asked for a $5M AI investment decision by Friday. You have three proposals on your desk. The board wants a recommendation. The CEO wants a number. Your staff wants a runway. This is the canonical Director decision: scope, alternatives, and risk.

**Decision in one sentence:** A director-grade decision is one whose reasoning is auditable, whose reversibility is known, and whose downstream consequences are bounded before the call is made.

---

## 3. Why AI Engineering Directors Fail Here

Five failure modes of director-grade decisions.

- **The Cargo-Cult Memo.** The decision memo is structured to look rigorous (alternatives considered, NPV computed) but does not engage with the strongest objection. It is cargo-cult rigor.
- **The Hidden-Constraint Game.** The director agrees to a decision frame set by the proposer, missing the constraint that would have flipped the answer.
- **The Irreversible-Bet Bluff.** The director signs off on a high-stakes bet believing it is reversible. It is not.
- **The Expert-Amnesia Trap.** The director defers to the loudest expert in the room instead of testing their claims against first-principles.
- **The De-Risking Theater.** The director approves a de-risking plan that is actually a runway extension. The risk has not been reduced; it has been deferred.

---

## 4. Mental Models

Three lenses for the decision.

**Mental model 1: Decision Stack.** Every decision has 3 layers: the frame (what question are we answering?), the alternatives (what are we choosing between?), and the criteria (how will we judge?). Most decision failures are frame failures, not alternatives failures.

**Mental model 2: Reversibility Ladder.** Type-1 decisions are reversible (hire a contractor); Type-2 are reversible-with-cost (rebuild a service); Type-3 are irreversible (acquire a company). Type-1 decisions deserve speed. Type-3 deserve slowness.

**Mental model 3: The Pre-Mortem.** Imagine the decision failed catastrophically in 18 months. Write the post-mortem now, before signing. The Pre-Mortem surfaces the strongest objection without anyone having to voice it.

---

## 5. Frameworks

Three reusable scaffolds.

### Framework 1: The Decision Memo (7 questions)

```
1. What decision are we making?
2. What is the cost of NOT deciding?
3. What alternatives did we consider?
4. Why are we rejecting each alternative?
5. What is the reversibility profile?
6. What is the de-risking plan?
7. What would change our mind in 6 months?
```

### Framework 2: The Pre-Mortem

```
Imagine we shipped this 18 months ago and it failed.
What does the post-mortem say?
What early signal did we ignore?
What would we have done differently?
```

### Framework 3: The Reversibility Audit

For each irreversible component of the decision: what is the rollback plan? Time to rollback? Cost of rollback?

---

## 6. Drill

You are the Director of AI at acme-corp. The CEO has asked you to sign off on a $5M AI investment by Friday. Three proposals are on your desk.

You have **90 minutes**. Produce a 1-page decision memo using Framework 1, with a Pre-Mortem (Framework 2) and Reversibility Audit (Framework 3) attached.

**Deliverable:** `portfolio/chapter-99-decision-memo.md`.

---

## 7. Worked Example

A fully filled-in version of the drill is provided as the answer key. The memo ends with: **Decision: Proposal B, conditional on the 3 conditions below.**

---

## 8. Failure Mode Postmortem

A Director of AI at a 2,000-person retailer approved a $30M AI vendor contract based on a 12-page memo. Eighteen months later the vendor's accuracy regressed by 14 points and the retailer was locked in. The Director had not run a Reversibility Audit. The contract had a $20M exit clause. The Director had not read it.

---

## 9. Self-Assessment Rubric

| # | Dimension | 1 (Novice) | 3 (Competent) | 5 (Expert) |
|---|---|---|---|---|
| 1 | Decision scope stated | Vague | Names decision + constraints | Names scope, frame, alternatives |
| 2 | Constraints identified | Lists "must-haves" | Names 3-5 hard constraints | Names hidden + revealed constraints |
| 3 | Alternatives considered | Single option | 2-3 alternatives | 3+ alternatives with rejection rationale |
| 4 | De-risking plan | "We'll iterate" | Names 1-2 kill criteria | Names flip rules + monitoring signals |
| 5 | Reversibility discussed | Not discussed | Names reversibility class | Names rollback time + cost per class |

**Disqualifier:** any 1 on dimension 1 or 5. A decision memo without scope or reversibility analysis is theater.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-99-decision-memo.md` — this is interview evidence for "Walk me through the most consequential decision you've made as a Director."

---

## 11. Interview Questions

1. **A $5M AI investment decision is on your desk Friday. What do you do Monday morning?**
2. **Walk me through a decision you got wrong. What guardrail would have prevented it?**
3. **What's the difference between a reversible and an irreversible decision, and how does it change your process?**
4. **Your CEO wants speed; your CTO wants rigor; your staff wants a runway. How do you balance?**
5. **Describe the most rigorous decision memo you've seen, and what made it rigorous.**