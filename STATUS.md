# Cross-Playbook Status

> **Last updated:** 2026-06-23 — **AI Eng Director v1.0.0 RELEASED.** **VP of Engineering Phase 1 (Part I) complete.**

## Released

### AI Engineering Director Playbook — v1.0.0 SHIPPED ✅

Released 2026-06-23. 28 chapters, 7 parts, ~360KB prose, 19 exercise bundles (76 files), 56 Mermaid diagrams, 4 verification gates green. Live on GitHub Pages: https://webmakin.github.io/career-playbooks/ai-eng-director/

## In Progress

### VP of Engineering Playbook — Phase 1 in progress

| Phase | Description | Status |
|---|---|---|
| 0 | Skeleton (28 stub chapters + bootstrap) | ✅ Complete (2026-06-23) |
| 1 | Chapters 1–4 (Foundations) | ✅ Complete (2026-06-23) |
| 2 | Chapters 5–9 (The Engineering Spine) | 🚧 Next |
| 3 | Chapters 10–13 (Platform & Production) | ⏳ Pending |
| 4 | Chapters 14–17 (Product & Strategy) | ⏳ Pending |
| 5 | Chapters 18–21 (Leadership at scale) | ⏳ Pending |
| 6 | Chapters 22–25 (Governance & Risk) | ⏳ Pending |
| 7 | Chapters 26–28 (The VPE's Portfolio) | ⏳ Pending |
| 8 | Polish, review, publish | ⏳ Pending |

**Phase 1 deliverables (just shipped):**
- Ch 1: What a VP of Engineering Actually Does (5 failure modes, 4 mental models, 3 frameworks, 90-min drill + worked example + rubric)
- Ch 2: The Director-to-VP Category Change (5 failure modes, 4 mental models, 3 frameworks, 90-min drill)
- Ch 3: Engineering Leadership Literacy (5 failure modes, 4 mental models, 3 frameworks, 90-min drill)
- Ch 4: The Engineering Org at Scale (5 failure modes, 4 mental models, 3 frameworks, 90-min drill)
- 4 exercise bundles (drill + template + worked-example + README each) = 16 exercise files
- `rubric_linter --all`: 56/56 PASS (28 AI + 28 VP, all linter-clean)
- mdbook build: clean, 4 VP chapters render at 43-45KB each (vs 30KB stubs)

**Target:** v1.0.0 in ~30 weeks at the current pace (4 chapters per Phase batch, with Part check-ins).

## Planned (no work started)

| Role | Slug | Notes |
|---|---|---|
| Engineering Director (non-AI) | engineering-director | Most overlap with AI Eng Director |
| Principal AI Scientist | principal-ai-scientist | Research-track, less people-mgmt |
| ML Researcher | ml-researcher | Research-track, mostly IC |
| AI Engineer (IC) | ai-engineer | IC track for senior AI builders |
| Staff Engineer (general) | staff-engineer | Generalist Staff-level ICs |

## Verification gates (every playbook)

1. `python3 _shared/tools/rubric_linter.py --all` → 100% PASS.
2. `python3 _shared/tools/score_drill.py --fixture` → exit 0.
3. `python3 _shared/tools/cost_estimator.py --fixture` → exit 0.
4. `mdbook build` → exit 0, site renders.

Cross-playbook linter now scans every bootstrapped role's chapters (was hardcoded to AI-eng-dir).

## Tools inherited from AI Eng Director

- `_shared/tools/rubric_linter.py` — 11-section anatomy enforcement (updated to multi-role)
- `_shared/tools/score_drill.py` — drill grading
- `_shared/tools/cost_estimator.py` — financial modeling
- `_shared/tools/publish.py` — chapter mirror (updated to multi-role)

**New tool needed for VPE Phase 2+:** `headcount_model.py` (engineering org cost, ramp time, retention, hiring funnel). Planned for Ch 18-21 (Leadership at scale).

## Cross-references

The VPE playbook cross-references the AI Eng Director playbook for AI-specific topics. See `src/index/cross-references.md` for the full map.

## Conventions

All playbooks follow `_shared/chapter-anatomy.md`, `_shared/rubric-spec.md`, `_shared/figure-style-guide.md`, and `_shared/CHANGELOG.md`. See `src/index/conventions.md` for the full rule set.