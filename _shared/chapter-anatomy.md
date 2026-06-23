# Chapter Anatomy — The 11-Section Template

> Canonical source of truth for every chapter in every playbook.
> Version: 1.0.0 — 2026-06-23.

Every chapter in every playbook in this repo MUST follow this template. The order is not optional — it forces the writer to surface failure modes before showing the framework.

## The 11 sections

1. **Epigraph** — one-line quote, tone-setter.
2. **Problem** — the specific decision a Director (or target role) faces this week that this chapter sharpens. A real scenario in the first paragraph.
3. **Why [Role]s Fail Here** — 3–5 named failure modes with real-world flavor.
4. **Mental Models** — 2–4 reusable lenses (one paragraph each + one Mermaid diagram where appropriate).
5. **Frameworks** — the actual decision-making tools. Always presented as a fillable template.
6. **Drill** — the executable core. Concrete fictional company (acme-corp), specific scenario, time-boxed instructions, deliverable.
7. **Worked Example** — fully completed drill. Shows what good looks like.
8. **Failure Mode Postmortem** — real (anonymized) or realistic case where a [role] got this wrong.
9. **Self-Assessment Rubric** — 5-dimension, 25-point scoring grid per `_shared/rubric-spec.md`.
10. **Portfolio Artifact Note** — maps the drill to interview evidence.
11. **Interview Questions** — 3–5 interview Qs that probe this material, with grading notes.

## Section contracts

**Section 2 (Problem)** must contain a "Decision in one sentence:" line. This is the chapter's spine.

**Section 3 (Why [Role]s Fail Here)** must list 3–5 named failure modes. Each must be a real pattern, not "if you ignore the basics." Use the format: **Name of Failure Mode.** One-paragraph explanation with a concrete example.

**Section 6 (Drill)** must specify a time budget (regex matchable: `\b\d+\s*[\*_]?\s*(?:min|minute|hour|hr|h)s?\b`). Must end with `**Deliverable:**` and a path like `portfolio/chapter-NN-<artifact>.md`.

**Section 9 (Self-Assessment Rubric)** must be a 5-row, 4-column table with the format from `rubric-spec.md`. Each row: `# | Dimension | 1 (Novice) | 3 (Competent) | 5 (Expert)`. Total possible: 25. Pass threshold: 18/25 with no dimension below 3.

## Validation

Run `_shared/tools/rubric_linter.py <chapter>.md`. Exit 0 = passes. Non-zero = fails with line-numbered issues. See `_shared/rubric-spec.md` for the rubric format contract.

## What this is NOT

Not a survey. Not a tutorial. Not a "5 tips for X" article. The 11-section anatomy forces concrete failure modes and concrete drills. A chapter that passes the linter is structurally complete; whether the prose is *good* is a separate review.