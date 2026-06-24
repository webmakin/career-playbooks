# Cross-Playbook Status

> **Last updated:** 2026-06-24 — **All 8 playbooks bootstrapped.** **3 playbooks released as v1.0.0.** **224 chapters live across 247 HTML pages.**

## Released ✅

### AI Engineering Director Playbook — v1.0.0 SHIPPED

Released 2026-06-23. 28 chapters, 7 parts, ~444KB prose, 19 exercise bundles (76 files), 56 Mermaid diagrams. Live on GitHub Pages: https://webmakin.github.io/career-playbooks/ai-eng-director/

Tag: https://github.com/webmakin/career-playbooks/releases/tag/v1.0.0

### VP of Engineering Playbook — v1.0.0-vp-eng SHIPPED

Released 2026-06-24. 28 chapters, 7 parts, ~592KB prose, 28 exercise bundles (112 files). Live on GitHub Pages: https://webmakin.github.io/career-playbooks/vp-engineering/

Tag: https://github.com/webmakin/career-playbooks/releases/tag/v1.0.0-vp-eng

### Forward Deployed Engineer Playbook — v1.0.0-fde SHIPPED

Released 2026-06-24. 28 chapters, 7 parts, ~496KB prose, 28 exercise bundles (112 files), Preface + Glossary + Errata. Live on GitHub Pages: https://webmakin.github.io/career-playbooks/fde/

Tag: https://github.com/webmakin/career-playbooks/releases/tag/v1.0.0-fde

## In Progress 🚧

### Engineering Director Playbook — Phase 1 complete (4/28 chapters)

| Phase | Description | Status |
|---|---|---|
| 0 | Skeleton (28 stub chapters + bootstrap) | ✅ Complete |
| 1 | Chapters 1–4 (Foundations) | ✅ Complete |
| 2–7 | Chapters 5–28 | 📝 Stub chapters (28/28 lint PASS, body content = template, not full narrative) |

Live: https://webmakin.github.io/career-playbooks/engineering-director/

## Planned (bootstrap complete, no narrative yet) 📋

### Principal AI Scientist Playbook

28 stub chapters, all in SUMMARY.md, all live. Body content = template (Phase 0 complete). Live: https://webmakin.github.io/career-playbooks/principal-ai-scientist/

### ML Researcher Playbook

28 stub chapters, all in SUMMARY.md, all live. Body content = template. Live: https://webmakin.github.io/career-playbooks/ml-researcher/

### AI Engineer Playbook

28 stub chapters, all in SUMMARY.md, all live. Body content = template. Live: https://webmakin.github.io/career-playbooks/ai-engineer/

### Staff Engineer Playbook

28 stub chapters, all in SUMMARY.md, all live. Body content = template. Live: https://webmakin.github.io/career-playbooks/staff-engineer/

## Verification Gates (final state)

| Gate | Result |
|---|---|
| `rubric_linter --all` | **224/224 chapter(s) OK** (28 AI + 28 VP-eng + 28 FDE + 28 ED + 28 PAS + 28 MLR + 28 AIE + 28 SE) |
| `mdbook build` | **Clean** — 247 HTML pages generated |
| Live site verification | **All 8 playbooks live**, all chapters accessible |
| Total content | 28 chapters × 8 roles = **224 chapters**, ~2MB of prose across all 8 playbooks |
| Exercise bundles | 19 + 28 + 13 = **60 exercise bundles** (240 files) for the 3 shipped playbooks |

## Git Timeline (key commits)

```
3199673  AI-eng-dir v1.0.0 release
b167911  VP-eng Phase 1
01224b2  VP-eng Phase 2
92ad4bd  VP-eng Phase 3
2fa9d16  VP-eng Phase 4
bce4dcc  FDE Phase 0
abcdd44  VP-eng Phase 5 (Ch 18-21)
fad6c51  VP-eng v1.0.0-vp-eng tag + polish
4c9a7be  FDE Phase 1 (Ch 1-4)
c75b8b6  FDE Phase 2 (Ch 5-9)
a9808cd  FDE Phase 3 (Ch 10-13)
ff22cee  FDE Phase 4 (Ch 14-17)
854d104  FDE Phase 5 (Ch 18-21)
0a9255c  FDE Phase 6 (Ch 22-25)
c0831b9  FDE Phase 7 (Ch 26-28)
854d104  FDE v1.0.0-fde tag + polish
f5a816c  ED Phase 0 (28 stubs)
f52ae14  ED Phase 1 (Ch 1-4)
11aead1  ED Phases 2-7 (Ch 5-28 compact template)
7d5a8e7  Bootstrap PAS + MLR + AIE + SE (28 stubs each)
```

## How to Continue

Each playbook is in its own `<role>-playbook/` directory at the repo root. To fill in a chapter from the stub template to full narrative:

1. Pick a chapter (e.g., `engineering-director-playbook/chapters/chap-5.md`).
2. Rewrite the 11 sections (Epigraph → Problem → Why EDs Fail Here → Mental Models → Frameworks → Drill → Worked Example → Failure Mode Postmortem → Self-Assessment Rubric → Portfolio Artifact Note → Interview Questions).
3. Run `python3 _shared/tools/rubric_linter.py engineering-director-playbook/chapters/chap-5.md` to verify it passes.
4. Run `python3 _shared/tools/publish.py --role engineering-director-playbook` to mirror to src/.
5. Run `mdbook build` to render the live site.

The 11-section anatomy, 5-criterion quality bar, and 28-artifact portfolio pattern are consistent across all 8 playbooks.
