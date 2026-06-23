# Rubric Specification

> Canonical specification for every self-assessment rubric in every playbook.
> Version: 1.0.0 — 2026-06-23.

Every chapter ships a 5-dimension, 1–5 scale self-assessment rubric. The format is not optional — the linter enforces it.

## Required format

```markdown
| # | Dimension | 1 (Novice) | 3 (Competent) | 5 (Expert) |
|---|---|---|---|---|
| 1 | Dimension name | Novice description | Competent description | Expert description |
| 2 | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... |
| 4 | ... | ... | ... | ... |
| 5 | ... | ... | ... | ... |

**Disqualifier:** any 1 on dimension N or M. Brief reason.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.
```

## Rules

1. **5 rows, exactly.** Not 3, not 7. Five.
2. **Each row names a specific competency**, not a category. "Applies the Eval-Gate" not "knowledge."
3. **The 1 / 3 / 5 columns describe observable behavior**, not vague aspirational statements. "Names all 4 cadences" beats "understands cadences."
4. **At least one Disqualifier line** that names which dimensions are safety-critical (a "1" is a hard fail).
5. **Pass threshold is 18/25** — i.e. average 3.6/5 with no single dimension below 3. Some chapters may tighten to 20/25.

## Scoring rubric answers

When a reader fills in their drill's rubric (Section 9), they score themselves 1–5 on each dimension and sum. Use `_shared/tools/score_drill.py` to validate the score sheet (handwritten or JSON).

## Common failure modes of rubrics

- **Rubrics with category labels not behaviors.** "Domain knowledge" is a category. "Names the 5 failure modes in this chapter by name" is a behavior. Use behaviors.
- **Rubrics with aspirational 5s.** "World-class domain expert" is unfalsifiable. "Has shipped a multi-vendor AI system at scale" is falsifiable. Use falsifiable.
- **Rubrics with no Disqualifier.** Every chapter has a safety-critical failure mode (e.g. "approves agents without reversibility analysis"). Name it.
- **Rubrics with thresholds that don't bite.** If everyone passes at 18/25, the threshold is too low. Calibrate against the worked example.