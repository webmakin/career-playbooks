# Forward Deployed Engineer Playbook

## Preface: How to Read This Book

> **The FDE role is a category change, not a title change.** This book is for the senior SWE who wants to make the shift to FDE, the FDE 2 who wants to grow to FDE 3, or the FDE 3 who wants to move to Principal FDE or PM.

---

## Who This Book Is For

This book is for **four kinds of readers**:

1. **Senior SWEs considering the FDE transition.** The book shows what FDE work actually looks like (Chapter 1), why the role is a category change (Chapter 2), and the customer edge + product edge as the two defining characteristics (Chapters 3-4).

2. **FDE 1s (0-3 years experience) looking to grow.** The book provides the technical spine (Chapters 5-9), the customer deployment methodology (Chapters 10-13), and the FDE-PM partnership (Chapter 14).

3. **FDE 2s (3-6 years experience) targeting FDE 3.** The book provides the feedback synthesis system (Chapter 15), product strategy influence (Chapter 16), product leadership (Chapter 17), and the FDE career ladder (Chapter 18).

4. **FDE 3s (6-10 years experience) targeting Principal FDE or PM.** The book provides FDE hiring (Chapter 19), performance management (Chapter 20), influence without authority (Chapter 21), and the FDE portfolio map (Chapter 27).

---

## How to Read This Book

This book is structured as **7 Parts, 28 chapters, ~250 pages**.

**Part I — Foundations (Chapters 1-4).** What an FDE actually does. The customer edge and product edge. The IC-to-FDE category change. **Read first.**

**Part II — FDE Technical Spine (Chapters 5-9).** The 5-layer deployment stack. Data engineering, ML serving, and ML/AI for the customer edge. **Read in order if you're new to FDE work.**

**Part III — Customer & Deployment (Chapters 10-13).** The 6-phase customer deployment methodology. Customer success playbook. Crisis response. Customer ops. **Skim if you have customer deployment experience; read carefully if you don't.**

**Part IV — Product & Strategy (Chapters 14-17).** The FDE-PM partnership. Feedback synthesis. Product strategy influence. FDE as product leader. **Read all of these — they're the leverage for FDE 3 promotion.**

**Part V — Career & Leadership (Chapters 18-21).** The FDE ladder. FDE hiring and onboarding. Performance management. Influence without authority. **Read all of these — they're the leverage for Principal FDE promotion.**

**Part VI — Governance & Risk (Chapters 22-25).** Customer data governance. Security in customer deployments. Regulatory compliance. Audit trail. **Read for the regulated industries (healthcare, finance, EU).**

**Part VII — The FDE's Portfolio (Chapters 26-28).** The 30/60/90 plan for new FDEs. The portfolio map. System design appendix. **Read all of these — they're the proof for promotion.**

---

## What This Book Is Not

This book is **not** a textbook on FDE work. It does not cover every customer deployment pattern, every ML serving framework, or every regulatory framework. It is a **field guide for the senior IC who is becoming an FDE**.

This book is also **not** a PM playbook. PMs have their own discipline (roadmap management, product strategy, product ops). This book shows the FDE's slice of the FDE-PM partnership.

This book is also **not** an SWE playbook. SWEs have a different discipline (system design, code quality, on-call). This book shows the FDE's slice of the technical work.

This book is **for FDEs and aspiring FDEs**.

---

## The 5-Criterion Quality Bar

Every chapter in this book meets 5 criteria:

1. **1 page** of decision context (no more, no less).
2. **1 worked example** showing the framework in action.
3. **1 failure mode postmortem** from a real-world FDE scenario.
4. **1 self-assessment rubric** to score your understanding.
5. **5+ interview questions** for promotion or hiring.

If a chapter fails any of these 5 criteria, the chapter is not done. The FDE who reads this book should be able to **answer the interview questions** in any chapter without re-reading the chapter.

---

## The 11-Section Chapter Anatomy

Every chapter follows the same 11-section structure:

1. **Epigraph** — 1 sentence on the chapter's core insight.
2. **Problem** — A real-world FDE scenario. Decision in one sentence.
3. **Why FDEs Fail Here** — 5 named failure modes.
4. **Mental Models** — 4 mental models with diagrams.
5. **Frameworks** — 3 reusable frameworks with templates.
6. **Drill** — 90-minute hands-on exercise with deliverable.
7. **Worked Example** — Real example showing the framework applied.
8. **Failure Mode Postmortem** — Real scenario from a real FDE.
9. **Self-Assessment Rubric** — 5 dimensions, 1-5 scoring.
10. **Portfolio Artifact Note** — Where this chapter's artifact fits in the 28-artifact portfolio.
11. **Interview Questions** — 5+ questions for promotion or hiring.

This 11-section structure is the discipline. **Every chapter uses it.**

---

## The 28-Artifact Portfolio

Every chapter produces 1 artifact. The 28 artifacts are the FDE's portfolio for promotion.

| Part | Chapters | Artifacts |
|------|----------|-----------|
| I — Foundations | 1-4 | FDE charter, IC-to-FDE memo, customer edge, product edge |
| II — Technical Spine | 5-9 | 5 deployment patterns |
| III — Customer & Deployment | 10-13 | 4 deployment playbooks |
| IV — Product & Strategy | 14-17 | 4 product artifacts |
| V — Career & Leadership | 18-21 | 4 career artifacts |
| VI — Governance & Risk | 22-25 | 4 governance artifacts |
| VII — Portfolio | 26-28 | 3 portfolio artifacts |

**Total: 28 artifacts.** Chapter 27 is the portfolio map. Chapter 28 is the system design appendix.

---

## Acknowledgments

This book is the work of a Principal FDE with 10+ years of customer-edge experience across enterprise software, AI/ML platforms, and B2B SaaS. It draws from real deployments at companies like Palantir, Anduril, and the many AI-first B2B startups where the FDE role is now standard.

Special thanks to:
- The FDEs who shared their failure mode postmortems (anonymized in Chapters 8, 11, 18, 20, 22, 25, 28).
- The PMs who co-designed the FDE-PM partnership framework (Chapter 14).
- The Directors who co-designed the FDE performance system (Chapter 20).
- The customers who shared their compliance and security requirements (Chapters 22-25).

---

## How to Use This Book

**If you're an aspiring FDE:** Read Part I (Chapters 1-4) first. Understand the customer edge + product edge. Then read Chapter 5 (deployment stack) + Chapter 10 (deployment methodology). Decide if FDE work is for you.

**If you're an FDE 1:** Read all of Parts I-III. Build the technical spine + customer edge. Skip Parts IV-VII for now.

**If you're an FDE 2:** Read Part IV (Product & Strategy). Build the FDE-PM partnership + feedback synthesis. Start preparing for FDE 3 promotion.

**If you're an FDE 3:** Read Parts V-VII. Build the FDE leadership + portfolio. Prepare for Principal FDE promotion or PM pivot.

**If you're a Director:** Read Chapters 18 (ladder), 19 (hiring), 20 (performance). Use this book as the reference for managing an FDE team.

**If you're a PM:** Read Chapters 14 (FDE-PM partnership), 15 (feedback synthesis), 16 (product strategy), 17 (FDE-as-product-leader). Use this book as the reference for partnering with FDEs.

---

**The FDE role is the most leveraged role in B2B AI.** The FDE lives at two edges — the customer edge (where the company's product meets the customer's problem) and the product edge (where the customer's feedback meets the company's roadmap). The FDE who masters both edges has a 5-year career at the top of the leverage curve.

This book is your field guide.

— The Author
September 2026
