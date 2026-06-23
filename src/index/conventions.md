# Conventions Shared Across All Playbooks

These are the contracts every chapter in every playbook follows. Living documents — pinned at the repo root in [`_shared/`](https://github.com/webmakin/career-playbooks/tree/main/_shared/), updated through the `CHANGELOG.md`.

## The 11-Section Chapter Anatomy

Every chapter has exactly 11 sections, in order:

1. Epigraph
2. Problem
3. Why [Role]s Fail Here
4. Mental Models
5. Frameworks
6. Drill
7. Worked Example
8. Failure Mode Postmortem
9. Self-Assessment Rubric
10. Portfolio Artifact Note
11. Interview Questions

Full contract: [`_shared/chapter-anatomy.md`](https://github.com/webmakin/career-playbooks/blob/main/_shared/chapter-anatomy.md).

The order is not optional — it forces the writer to surface failure modes before showing the framework.

## Rubrics

Every chapter ships a 5-dimension, 1–5 scale self-assessment rubric. Pass threshold: 18/25 with no dimension below 3. At least one "Disqualifier" dimension is named (a "1" there is a hard fail).

Full contract: [`_shared/rubric-spec.md`](https://github.com/webmakin/career-playbooks/blob/main/_shared/rubric-spec.md).

## Figures

Diagrams use Mermaid (renders inline as SVG in mdBook). Naming convention: `%% Figure N.M — short title` comment above each diagram. Default theme; no color customization. Max ~10 nodes per diagram.

Full contract: [`_shared/figure-style-guide.md`](https://github.com/webmakin/career-playbooks/blob/main/_shared/figure-style-guide.md).

## Tone

Direct, opinionated, first-person plural ("we" when referring to Director practice). Citations are inline; sources live in `references/` where applicable. No "5 tips for X" lists. No "in this chapter we'll learn" throat-clearing.

## Verification

Every chapter is validated by `_shared/tools/rubric_linter.py`. Concrete numbers in worked examples are validated by running the relevant tool (`cost_estimator.py`, etc.) and matching the output to the prose. Exercise bundles are validated for 4-file completeness.

This discipline is what makes the playbook *trustable*. A worked example with a stale cost number is worse than no example.