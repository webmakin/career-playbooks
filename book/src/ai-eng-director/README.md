# AI Engineering Director Playbook

> **The Practice-First Guide to Becoming an AI Engineering Director or Head of AI**

This is the canonical source for the AI Engineering Director playbook. The published version (mdBook HTML site) is auto-generated from these chapters via `_shared/tools/publish.py`.

## Who this is for

You are a senior engineer, staff engineer, or new manager targeting Director or Head of AI in an organization. You are 30–90 days from a Director interview, or already in the seat and looking for the operating manual you wish you'd had.

## What you'll have when you're done

- 25+ portfolio artifacts (`portfolio/chapter-NN-*.md`) covering every chapter.
- A 90-day Director plan, a Decision Memo library, a Build-vs-Buy toolkit, and an eval-system upgrade plan.
- A clear map from each artifact to the interview question it answers.

## Structure: 7 parts, 28 chapters

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

## Repo layout

```
AI-eng-dir-playbook/
├── README.md             # this file
├── chapters/chap-N.md    # canonical chapter source
├── exercises/chapterNN/  # drill + template + worked-example + README per chapter
├── resources/            # topic outline, references, legacy plan
├── templates/            # role-specific templates (30-60-90, decision memo)
└── diagrams/             # SVG/PNG diagrams (Mermaid renders inline in MD)
```

## Conventions

This playbook follows the contracts in [`_shared/`](https://github.com/webmakin/career-playbooks/tree/main/_shared/). See [Conventions](../index/conventions.md) for the full rule set.

## Status

Phase 0 (skeleton) complete. Phase 1 (Ch 1–9) being rebuilt. See root `STATUS.md`.

## Contributing

PRs welcome once the first 9 chapters are re-published. Until then, the author is writing solo; review will open after Chapter 9 lands.