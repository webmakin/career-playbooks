# Career Playbooks

> **Practice-first guides for becoming a senior engineer, manager, or AI leader — every chapter produces a graded artifact.**

This is a series of playbooks. Each one is the canonical guide for a specific role, structured the same way: a multi-chapter book with an 11-section anatomy per chapter, executable drills, worked examples, failure-mode postmortems, self-assessment rubrics, and interview-question banks.

## Pick the playbook that matches your goal

- **AI Engineering Director** — heading toward Director or Head of AI? Start here. (28 chapters, 7 parts, full.)
- Engineering Director (non-AI) — coming soon.
- VP of Engineering — coming soon.
- Principal AI Scientist — coming soon.
- ML Researcher — coming soon.
- AI Engineer (IC) — coming soon.
- Staff Engineer (general) — coming soon.

A decision tree lives at [Which Playbook Is For You?](index/role-selector.md).

## How the playbooks work

Every playbook follows the same contract, defined in [`_shared/chapter-anatomy.md`](https://github.com/webmakin/career-playbooks/blob/main/_shared/chapter-anatomy.md):

1. **Epigraph** — one-line quote.
2. **Problem** — the specific decision you face this week.
3. **Why [Role]s Fail Here** — 3–5 named failure modes.
4. **Mental Models** — 2–4 reusable lenses.
5. **Frameworks** — fillable templates.
6. **Drill** — executable scenario with a time budget.
7. **Worked Example** — fully-completed drill.
8. **Failure Mode Postmortem** — what the wrong call looks like.
9. **Self-Assessment Rubric** — 5 dimensions, 25 points, pass at 18+.
10. **Portfolio Artifact Note** — maps the drill to interview evidence.
11. **Interview Questions** — 3–5 questions with grading notes.

Every chapter ships a portfolio artifact (`portfolio/chapter-NN-<artifact>.md`). By the end of a playbook you have 25+ graded artifacts you can bring into interviews or your first 30/60/90 days.

## What every playbook has in common

- **No black boxes.** Every claim is sourced, every framework has a fillable template, every cost number comes from a real run of `_shared/tools/cost_estimator.py`.
- **Recursive depth.** Each chapter's mental models cite the deeper chapters where the underlying mechanics live.
- **Failure-mode literacy.** 5 named failure modes per chapter — what good looks like *and* what bad looks like.
- **Executable drills.** Each drill has a fictional company (acme-corp), a specific scenario, a time budget, and a deliverable.

See [Conventions](index/conventions.md) for the full contract.

## Status

🚧 Phase 0 (skeleton) complete. Phase 1 (Foundations + Technical Spine, Ch 1–9) being rebuilt after data loss 2026-06-23.

See [`STATUS.md`](https://github.com/webmakin/career-playbooks/blob/main/STATUS.md) for the per-chapter matrix.

## About the author

Mohammed Asif. Engineer building production AI systems. Style inspired by `build-gpt-from-scratch` (recursive depth, no black boxes, executable code per chapter).