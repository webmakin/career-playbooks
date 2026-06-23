# AI Engineering Director Playbook

> **The Practice-First Guide to Becoming an AI Engineering Director or Head of AI**

![v1.0.0 Released](https://img.shields.io/badge/v1.0.0-released-brightgreen)
![Chapters: 28/28](https://img.shields.io/badge/chapters-28%2F28-brightgreen)
![Exercise Bundles: 19/28](https://img.shields.io/badge/exercise%20bundles-19%2F28-blue)
![Live Site](https://img.shields.io/badge/live%20site-active-brightgreen)

This is the canonical source for the AI Engineering Director playbook. The published version (mdBook site) is auto-generated from these chapters via `_shared/tools/publish.py`.

## TL;DR

You're 30–90 days from a Director-of-AI interview, or already in the seat looking for the operating manual you wish you'd had. This book is that manual. By the end you'll have:

- 28 chapters of decision frameworks, mental models, and failure modes across 7 parts.
- 19 executable drills with worked examples, each producing a portfolio artifact.
- A 5-dimension rubric per chapter (25 points, pass at 18+) for self-calibration.
- A Portfolio Map (Ch 27) that maps each artifact to the interview question it answers.
- A 30/60/90 simulation (Ch 26) for the first 90 days in the seat.
- A System Design Appendix (Ch 28) covering the AI-flavored system design interview.

## Who this is for

You are a senior engineer, staff engineer, or new manager targeting Director or Head of AI in an organization. You are 30–90 days from a Director interview, or already in the seat and looking for the operating manual you wish you'd had.

## What you'll have when you're done

- 25+ portfolio artifacts (`portfolio/chapter-NN-*.md`) covering every chapter.
- A 90-day Director plan, a Decision Memo library, a Build-vs-Buy toolkit, and an eval-system upgrade plan.
- A clear map from each artifact to the interview question it answers.
- A reusable set of mental models for AI economics, lifecycle, governance, and team design.

## Reading order

The book is structured in 7 parts. **Read in order if this is your first read.** Jump to a part if you have a specific gap.

- **Part I — Foundations** (Ch 1–4): the role, the category change, AI literacy, build-vs-buy economics.
- **Part II — The Technical Spine** (Ch 5–9): data, training, inference, retrieval/agents, evaluation.
- **Part III — Platform & Production** (Ch 10–13): MLOps/LLMOps, AI platform engineering, reliability, security.
- **Part IV — Product & Strategy** (Ch 14–17): product discovery, AI strategy, business case, pricing/GTM.
- **Part V — Leadership** (Ch 18–21): org design, hiring, perf management, executive influence.
- **Part VI — Governance & Risk** (Ch 22–25): responsible AI, regulatory landscape, crisis response, auditability.
- **Part VII — The Director's Portfolio** (Ch 26–28): 30/60/90 simulation, portfolio map, system design appendix.

## How to use this playbook

1. **Read the chapter.** Section 2 tells you the decision; Section 3 tells you the failure modes.
2. **Run the drill.** Section 6 gives a fictional scenario; you produce `portfolio/chapter-NN-*.md`.
3. **Compare to the worked example.** Section 7 shows what good looks like.
4. **Score yourself.** Section 9 rubric, 5 dimensions, pass at 18/25.
5. **Use the artifact.** Section 10 maps the drill to interview evidence.

If you're a Director already in the seat, you can do **Chapter 27 (Portfolio Map) first** to see what you should already have evidence of, then go back and fill the gaps.

If you're 30–90 days from an interview, do the 28 chapters in order. Each chapter is ~30–45 min of reading + ~90 min for the drill. Total: ~50–70 hours of work. Pace it over 4–8 weeks.

## Conventions

This playbook follows the contracts in [`_shared/`](https://github.com/webmakin/career-playbooks/tree/main/_shared/). See [Conventions](https://github.com/webmakin/career-playbooks/blob/main/book/src/index/conventions.md) for the full rule set.

## Status

**v1.0.0 RELEASED 2026-06-23.** All 28 chapters written, all 7 parts complete, 19 exercise bundles delivered, 4 verification gates green. Live on GitHub Pages.

## Contributing

PRs welcome. The author's chapters are committed in priority order (Foundations → Technical Spine → Platform → Product → Leadership → Governance → Portfolio).

To open a PR:
1. Fork the repo.
2. Edit the canonical source in `AI-eng-dir-playbook/chapters/chap-N.md`.
3. Run the verification gates (see `STATUS.md` for the recipe).
4. Run `python3 _shared/tools/publish.py --role AI-eng-dir-playbook` to mirror to `src/`.
5. Open the PR with the chapter number in the title.