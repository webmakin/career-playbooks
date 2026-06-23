# Preface: How to Read This Book

> *"The book is not the destination. The book is the map. The territory is your first 90 days in the seat."*

## Why this book exists

The job of an AI Engineering Director is not well-defined. The title is new. The org charts vary. The product surface is shifting. The half-life of any "best practice" is shrinking. Most existing resources are either too general (a leadership book that doesn't know AI) or too narrow (a research paper that doesn't know management). This book is a third path: **practice-first, decision-shaped, evidence-graded.**

## What the book is

- **28 chapters, 7 parts.** The progression is intentional: foundations first (who you are, what you own), then the technical spine (what the system is), then platform and product (what you build with it), then leadership and governance (how you grow the team and the company safely), and finally the portfolio (how you prove you can do the job).
- **5 named failure modes per chapter.** Every chapter names what bad looks like — concretely, with named failure modes. The Failure Mode Postmortem in Section 8 then shows a real (anonymized) case where someone got it wrong.
- **3 frameworks per chapter.** The frameworks are templates, not theories. They are designed to be filled in on Monday morning, not to be admired from a distance.
- **1 executable drill per chapter.** Each drill is a 90-minute scenario with a fictional company (acme-corp) and a specific deliverable. The deliverable is portfolio evidence you can bring into an interview.
- **1 worked example per chapter.** Section 7 shows what good looks like for the drill, scored against the rubric in Section 9.

## What the book is not

- **Not a research survey.** The chapters cite specifics, not literature reviews. If you want a comprehensive review of the AI lifecycle, see MLPerf, Stanford AI Index, or the EU AI Act itself.
- **Not a get-rich-quick guide.** The book assumes you are operating in a real org with real constraints. If you are looking for AI hype, this is the wrong book.
- **Not jurisdiction-specific.** Chapters 22 and 23 discuss the EU AI Act, NIST AI RMF, US Executive Orders, and sector rules (HIPAA, FCRA, ECOA). They are illustrative, not legal advice. Run your compliance posture past counsel before shipping anything that touches these regulations.
- **Not the only book you'll ever need.** A Director's job is multi-disciplinary. This book covers AI, leadership, governance, and strategy. It does not cover finance, legal, marketing, or other functions you'll need to be conversant in.

## How to use the book

**Path A — Director aspirant (30–90 days from interview).**

1. Read in order. Cover ~3–4 chapters per week.
2. Do the drill for every chapter. Save the artifact in `portfolio/chapter-NN-<artifact>.md`.
3. Score yourself against the rubric in Section 9. Aim for 18+/25 on each.
4. After Ch 27 (Portfolio Map), assemble your portfolio into a 1-page "evidence bank" for interviews.
5. Use Ch 28 (System Design Appendix) to practice the 45-minute system design round.

**Path B — Director already in the seat.**

1. Read Ch 27 (Portfolio Map) first to see what you should already have evidence of.
2. Go back and fill the gaps. The chapters map to the decisions you've already made or will make soon.
3. Pay special attention to Part VI (Governance & Risk) — most Directors under-invest here.
4. Re-read Ch 21 (Influencing Without Authority) and Ch 26 (30/60/90) every 6 months as a calibration.

**Path C — Engineering Manager targeting Director.**

1. Skim Part I (Foundations) and Part V (Leadership). You already know parts of these.
2. Focus on Part II (Technical Spine) — Directors need a stronger technical base than EMs.
3. Spend time on Part III (Platform & Production) and Part IV (Product & Strategy). EMs often skip these.
4. Part VI (Governance & Risk) is a high-leverage investment — most Directors have never seen this content.

**Path D — AI Engineer or Staff Engineer targeting Director.**

1. Read Part I (Foundations) and Part II (Technical Spine) — you're already strong on the technical side.
2. Focus on Part V (Leadership). The IC-to-Director category change is the hardest transition.
3. Part IV (Product & Strategy) is the highest-leverage gap for ICs. Most ICs under-invest here.
4. Part VI (Governance & Risk) is increasingly important for senior ICs. Read it.

## What you should have after reading

- A written point of view on each of the 28 chapters, with concrete artifacts.
- A portfolio of 25+ graded artifacts you can reference in interviews.
- A 30/60/90-day plan tailored to the org you join.
- A defensible set of mental models for the decisions you'll face.
- A clear sense of which questions you don't have answers to (and what to do about them).

## How the book is graded

Every chapter ends with a 5-dimension rubric (Section 9). The dimensions are:
1. Framework application
2. Specificity (names, dollar figures, named decisions)
3. Risk consideration
4. Actionability
5. Writing quality

Each dimension is scored 1–5. Total is out of 25. Pass at 18+, with no dimension below 3. The rubric is enforced by `_shared/tools/rubric_linter.py` — if a chapter doesn't meet the bar, the build fails.

The same rubric is what you use to grade your own drill outputs. A drill output that scores 18+/25 is interview-ready. A drill output that scores <18 needs another pass.

## A note on voice

The book is written in first person, opinionated, direct. The author has shipped AI features, made the mistakes, and tried to learn from them. The book does not pretend to know what's right — it tells you what the author has seen work and what hasn't. Your org is different. The book is a starting point, not the final word.

If something in the book feels wrong for your context, the right move is to do the drill anyway, score yourself, and then adapt the framework. The discipline of "fill the template, then critique it" is more valuable than the template itself.

— Mohammed Asif, June 2026