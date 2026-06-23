# VP of Engineering Playbook
## Chapter 3

# Engineering Leadership Literacy

> *"A VPE is the last technical person in the chain. The VPE does not write code. The VPE decides what code gets written, by whom, on what timeline, with what quality bar, at what cost."*

---

## 1. Epigraph

A VPE is the last technical person in the chain. The VPE does not write code. The VPE decides what code gets written, by whom, on what timeline, with what quality bar, at what cost.

---

## 2. Problem

You are the VPE at a 1,200-person company. In the last 30 days, you have been asked to evaluate: (1) a $4M investment in a new platform team, (2) a buy-vs-build for a feature that affects 80% of customer-facing code, (3) a board update on engineering health, (4) a security incident that triggered a customer data exposure, and (5) a CFO proposal to outsource 30% of engineering capacity. Each decision requires a different literacy: financial, technical, board, security, and strategic. You don't have time to be an expert in all of them. You do need to be literate in all of them.

This chapter is the operating manual for the **5 literacies** a VPE must read fluently to make good decisions at the C-suite and board level.

**Decision in one sentence:** A VPE's primary literacy is not coding — it's reading and writing the 5 systems that surround the engineering org: financial (capex, opex, headcount cost), technical (architecture, debt, productivity), people (hiring, retention, perf), market (competitive, customer-driven), and board (governance, narrative, numbers).

---

## 3. Why VPEs Fail Here

Five named failure modes of VPEs who failed the literacy test.

- **The Technical Expert VPE.** The VPE is the deepest technical person in the room and makes every decision as a technical decision. The VPE who won't approve a $4M investment because the technical ROI is "uncertain" is a VPE who is reading the decision wrong. The decision is a financial decision with a technical component. A VPE who can only read the technical part is a VPE who will be overruled by the CFO.
- **The Cost-Blind VPE.** The VPE focuses on engineering quality, hiring, and architecture and does not know the company's financial state. The VPE who proposes a $10M investment without knowing the company's cash position is a VPE who will be shot down in the exec meeting. The VPE's job includes the financial state.
- **The Board-Stage-Phobic VPE.** The VPE is comfortable in 1:1s and small meetings and freezes in front of the board. The VPE who sends a Director to present to the board is a VPE who has not transitioned. The VPE presents to the board. The Director supports.
- **The People-Vague VPE.** The VPE knows the team is "great" but cannot articulate who is great, what they are great at, and what they cost. The VPE who can't answer "how many engineers do we have, what is the average cost, what is the attrition rate" is a VPE who is reading the people system wrong. The people system has numbers; the VPE knows the numbers.
- **The Market-Ignorant VPE.** The VPE focuses on engineering and does not read the market, the competitors, the customers, or the product roadmap. The VPE who doesn't know what the competitors are shipping is a VPE who is making engineering decisions in a vacuum. The VPE's job includes the market context.

---

## 4. Mental Models

Four mental models that compress the 5 literacies into something you can defend.

**Mental model 1: The 5 Literacies.** A VPE reads fluently in 5 systems. Each has its own language, its own metrics, its own decisions.

```mermaid
%% Figure 3.1 — The 5 literacies
flowchart TB
    FIN[Financial Literacy<br/>$ / quarter / engineer<br/>$ / feature / customer]
    TECH[Technical Literacy<br/>Architecture / Debt / Productivity]
    PEOPLE[People Literacy<br/>Hiring / Retention / Perf / Comp]
    MARKET[Market Literacy<br/>Competition / Customer / Roadmap]
    BOARD[Board Literacy<br/>Governance / Narrative / Numbers]
    VPE[VP of Engineering<br/>(reads fluently in all 5)]
    FIN --> VPE
    TECH --> VPE
    PEOPLE --> VPE
    MARKET --> VPE
    BOARD --> VPE
```

Each literacy is a separate muscle. The VPE's job is to keep all 5 fit. The VPE who is fit in 1 and weak in 4 is a VPE who will be overruled by the people who are fit in those 4.

**Mental model 2: The Decision Lens.** Every decision the VPE faces is best read through one of the 5 literacies. Misreading the lens produces a bad decision.

```
Decision: "Should we invest $4M in a new platform team?"

Wrong lens: Technical — "is the technical ROI there?"
            (Most technical investments have uncertain ROI; this
            lens produces a "no" because the technical case is
            rarely airtight.)

Right lens: Financial + People — "what's the cost of NOT investing?
            How much engineering capacity is currently spent on
            platform work? What's the attrition risk of overloaded
            engineers? What does the CFO's view of headcount cost
            say about the trade-off?"

The right lens surfaces the trade-off. The wrong lens
makes the decision a coin flip.
```

**Mental model 3: The 3 Questions for Every Decision.** Before a VPE makes a major decision, the VPE asks 3 questions — one from each of 3 of the 5 literacies.

```
1. FINANCIAL:  What's the dollar cost over 12 months? 24 months?
               What's the cost of NOT doing this?

2. PEOPLE:     Who's affected? How many? How does this change
               their work? Their careers? Their retention?

3. MARKET:     How does this affect the product? The customer?
               The competitive position?

If the VPE can't answer one of these, the VPE doesn't have
enough information to make the decision. Stop and gather
information.
```

**Mental model 4: The Board Deck Anatomy.** A VPE's board update is a 1-page artifact with 3 sections.

```
Section 1 (top):  The 3 numbers that matter.
                  Throughput, quality, cost — at the company level.
                  Trend over the last 3 quarters.
                  Forecast for the next quarter.

Section 2 (middle): The 1-3 things that need board awareness.
                  Headcount gaps, major project changes, risks
                  the board should know about.

Section 3 (bottom): The 1 ask.
                    What the VPE needs from the board (usually:
                    approve a budget, support a hire, advise on
                    a strategic question).
```

The VPE who sends a 30-page deck to the board is a VPE who doesn't know how to prioritize. The VPE who sends a 1-page deck with the 3 numbers + 1 ask is a VPE who knows the board's job (governance, not operations).

---

## 5. Frameworks

Three frameworks for the 5 literacies.

### Framework 1: The 5-Literacy Self-Assessment

A VPE should rate themselves on each of the 5 literacies, on a 1-5 scale, every 6 months. The goal: keep all 5 at 3+.

```
Financial:    ___ / 5
Technical:    ___ / 5
People:       ___ / 5
Market:       ___ / 5
Board:        ___ / 5

If any literacy is at 1-2: hire a coach or take a course.
If any literacy is at 4-5: you're a candidate for the next role
(CFO, CTO, CEO). Plan your succession.
```

### Framework 2: The Decision-Lens Test

Before making a major decision, run this test.

```
Decision: ___

1. Which of the 5 literacies is the PRIMARY lens? (one only)
2. Which of the 5 literacies is the SECONDARY lens? (one or two)
3. Which of the 5 literacies am I IGNORING? (this is where the
   risk is)

If the primary lens is wrong, the decision is wrong.
If the secondary lens is right, the decision is supported.
If the ignored literacy is important, the decision is risky.

Run the test. The cost of running it is 5 minutes. The cost
of a wrong-lens decision is millions of dollars and years of
career damage.
```

### Framework 3: The Board Update Template

A 1-page board update, used quarterly.

```
# Engineering Board Update — Q[N] [YEAR]

## Top 3 numbers
| Metric          | Q-2 | Q-1 | Q[N] | Target Q+1 |
|-----------------|-----|-----|------|------------|
| Throughput      |     |     |      |            |
| Quality (MTTR)  |     |     |      |            |
| Cost ($/eng)    |     |     |      |            |

## What the board should know
1. [Major change / risk / opportunity]
2. [Major change / risk / opportunity]
3. [Major change / risk / opportunity]

## What I need from the board
[1 ask. Make it concrete.]

## Appendix (only if asked)
- 5-metric dashboard
- Hiring funnel
- Top 3 risks
```

---

## 6. Drill

You are the VPE at **acme-corp**. In the last 30 days, the following 5 decisions have been put on your desk:

1. **$4M investment in a new platform team** (financial + people literacy).
2. **Buy-vs-build for a feature that affects 80% of customer-facing code** (technical + financial + market).
3. **Board update on engineering health** (board literacy).
4. **Security incident: customer data exposure, 12K customers affected** (security/regulatory + people + board).
5. **CFO proposal to outsource 30% of engineering capacity** (financial + technical + people).

You have **90 minutes**. Produce a **5-literacy decision package** (`portfolio/chapter-03-5-literacy-decision-package.md`) using Framework 1 (Self-Assessment) + Framework 2 (Decision-Lens Test) + Framework 3 (Board Update Template). Specify:

- Your self-assessment (rate yourself on all 5 literacies).
- For each of the 5 decisions: the primary lens, the secondary lens, the ignored lens, the risk in the ignored lens.
- The 1-page board update (covering Q[N] + the security incident).
- The 1 ask you'd make of the board.
- The 1 thing you'd push back on the CFO on.

**Deliverable:** `portfolio/chapter-03-5-literacy-decision-package.md` — under 1500 words.

---

## 7. Worked Example

**My self-assessment (5 literacies):**

```
Financial:    4 / 5  (read every P&L, know the cost structure)
Technical:    5 / 5  (was a Director of platform for 4 years)
People:       4 / 5  (good on hiring, weaker on comp strategy)
Market:       2 / 5  (this is my gap — I've been heads-down in
                       engineering, not reading the market)
Board:        3 / 5  (have presented twice, mostly small boards)
```

**The 5 decisions, with primary / secondary / ignored lens:**

```
Decision 1: $4M platform team investment
  Primary lens:   People (which teams are overloaded? what's the
                   attrition risk?)
  Secondary lens: Financial (4M cost, 12-month payback?)
  Ignored lens:   Market (do we need this to ship faster, or is
                   this engineering-driven and customer-neutral?)
  Risk:           We build a platform nobody uses because we didn't
                   ask the product org.

Decision 2: Buy-vs-build for 80% of customer-facing code
  Primary lens:   Technical (can we even build it? at what cost?)
  Secondary lens: Financial (build cost vs. license cost over 5 years)
  Ignored lens:   People (will the team be motivated to maintain
                   third-party code? what's the retention impact?)
  Risk:           We buy something the team resents. The team
                   quietly bypasses the vendor. We pay the cost
                   AND the build cost.

Decision 3: Board update on engineering health
  Primary lens:   Board (what does the board need to know?)
  Ignored lens:   People (the team is doing better than the numbers
                   suggest because of the unmeasured human work)
  Risk:           The board sees numbers that underrepresent us.
                   They may overreact.

Decision 4: Security incident: 12K customers affected
  Primary lens:   Regulatory (GDPR? CCPA? state breach laws?)
  Secondary lens: People (customer trust, team morale)
  Ignored lens:   Board (the board needs to know NOW, not in the
                   next scheduled update)
  Risk:           The board finds out from the press instead of
                   from us. Trust destroyed.

Decision 5: CFO proposal to outsource 30% of engineering capacity
  Primary lens:   Financial (CFO's view: $20M/year savings)
  Secondary lens: Technical (which work can be outsourced?
                   which work cannot?)
  Ignored lens:   People (the in-house team will be devastated by
                   the message; attrition will spike regardless
                   of the decision)
  Risk:           The CFO gets the savings on paper, but loses
                   30% of the in-house team in 6 months. The
                   savings evaporate.
```

**The 1-page board update:**

```
# Engineering Board Update — Q3 2026

## Top 3 numbers
| Metric          | Q1   | Q2   | Q3   | Target Q4 |
|-----------------|------|------|------|-----------|
| Throughput      | 12   | 14   | 16   | 18        |
| Quality (MTTR)  | 6 hr | 5 hr | 4 hr | 3 hr      |
| Cost ($/eng)    | 245K | 240K | 232K | 220K      |

## What the board should know
1. **Security incident**: 12K customer records exposed via a third-
   party vendor (vendor-driven, not our code). Affected customers
   notified. Vendor terminated. Full postmortem at next board
   meeting.
2. **Platform team investment**: requesting $4M over 18 months
   to consolidate 8 platform teams into 1. Payback: 14 months.
3. **Hiring**: 12 of 30 open reqs filled this quarter. Director-
   level hiring remains the bottleneck. Two senior Director-level
   candidates in pipeline.

## What I need from the board
- Approve the $4M platform team investment. This is the biggest
  leverage point in the org right now.
- Support a public statement on the security incident. I'm
  drafting; need CEO sign-off by Friday.

## Appendix (only if asked)
- 5-metric dashboard
- Hiring funnel
- Top 3 risks
```

**The 1 ask:** Approve the $4M platform team investment.

**The 1 thing I'd push back on the CFO on:**

```
The CFO's outsourcing proposal is right that there's a financial
case. It's wrong on what the case ignores.

What's right: 30% of our work is "feature factory" work that
could be done by a vendor. The CFO's $20M/year savings is real.

What's wrong: the in-house team will read the message as "we
are being replaced." Attrition will spike regardless of the
decision. We'll lose 20% of the in-house team in 6 months.

Counter-proposal: Instead of outsourcing 30%, restructure the
in-house team to focus on the 70% that is core (architecture,
product features, AI). Outsource the 30% but commit to no
in-house layoffs. The 30% in-house people move to the core 70%.

Financial outcome: same savings, no attrition shock, no press
risk. The CFO gets the savings. The team gets the security.
```

---

## 8. Failure Mode Postmortem

A VPE at a 1,400-person fintech was asked by the CEO to take over a struggling product engineering org. The VPE was the deepest technical person in the company but had not been on a board, had not read a P&L, and did not know the company's customer churn numbers.

The VPE made every decision as a technical decision. The board update was 30 pages of technical detail. The CFO's outsourcing proposal was rejected because the VPE didn't have the financial literacy to counter-propose. The board stopped asking the VPE for input. Within 18 months, the VPE was reassigned to a CTO-track role and the engineering org was split.

What the VPE missed: 4 of the 5 literacies. The VPE was fit in Technical, weak in Financial, weak in People, weak in Market, and weak in Board. The CEO needed a VPE who could read the board and the P&L, not a CTO who could read the architecture.

The lesson: a VPE's primary literacy is not coding. The VPE's job is to read 5 systems. The VPE who can only read 1 system is a VPE who can be replaced by a Director (or, in this case, should be).

---

## 9. Self-Assessment Rubric

| # | Dimension | 1 (Novice) | 3 (Competent) | 5 (Expert) |
|---|---|---|---|---|
| 1 | **5 literacies** | Fit in 1 of 5 | Fit in 3 of 5 | Fit in 5 of 5 |
| 2 | **Decision lens** | Always uses one lens (usually technical) | Names primary/secondary lens per decision | Runs Decision-Lens Test before every major decision |
| 3 | **3 questions** | Asks 1 of 3 (the obvious one) | Asks 2 of 3 | Asks all 3 (financial, people, market) |
| 4 | **Board update** | 30-page deck | 5-page deck with 3 numbers | 1-page deck with 3 numbers + 1 ask |
| 5 | **Self-assessment discipline** | No self-assessment | Annual self-assessment | 6-month self-assessment + 1 coach per weak literacy |

**Disqualifier:** any 1 on dimension 1 or 4. A VPE fit in only 1 of 5 literacies or who sends 30-page board decks is in the Technical-Expert-VPE trap or the Board-Stage-Phobic trap.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-03-5-literacy-decision-package.md` — interview evidence for "How do you read the financial / board / people systems?" (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through the 5 literacies a VPE needs.**
2. **A CFO proposes to outsource 30% of engineering. What do you do?**
3. **Your company has a security incident. Walk me through the first 24 hours.**
4. **Walk me through your last board update.**
5. **What's the difference between a VPE and a CTO?**