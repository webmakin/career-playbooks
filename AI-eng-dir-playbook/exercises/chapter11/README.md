# Chapter 11 — Exercise Bundle: AI Platform Engineering

> **Drill:** `drill.md`
> **Time budget:** 90 minutes (read chapter + produce drill output).
> **Rubric:** 25 points total; pass at 18+ with no dimension below 3.

## Files in this bundle

| File | Purpose |
|------|---------|
| `README.md` | This file — bundle overview, rubric, navigation. |
| `drill.md` | The drill prompt. Read this first. |
| `template.md` | A fillable template for the drill output. Use this as a starting point. |
| `worked-example.md` | A fully-worked example of the drill, with score breakdown. |

## Rubric (5 dimensions, 1-5 scale, 25 total)

| # | Dimension | Score (1-5) |
|---|-----------|------------|
| 5-capability audit | ___ |
| Quarter prioritization rationale | ___ |
| 12-month roadmap | ___ |
| Pilot feature selection | ___ |
| Vendor-switch drill design | ___ |

**Disqualifier:** any 1 on any dimension.

**Pass threshold:** 18/25 total, no dimension below 3.

## Self-assessment

After completing the drill, fill in your scores per dimension in the worked-example.md template, then run:

```bash
python3 _shared/tools/score_drill.py --rubric <your-output>.md
```

The script scores against the canonical rubric dimensions (the same 5 the chapter uses).

## Portfolio

Save your filled-in drill as `portfolio/chapter-11-platform-strategy.md` — interview evidence (see Portfolio Map in Chapter 27).
