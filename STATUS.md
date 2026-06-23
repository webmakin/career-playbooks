# Cross-Playbook Status

> **Last updated:** 2026-06-23 — Phase 3 complete (Chapters 1–17). Phase 4 in progress (stubs, Ch 18–28).

## Current Phase

✅ **Phase 0 — Skeleton complete.** Local build verified. Site landing + 28 chapter stubs + 7 part dividers + role-selector + cross-references + conventions page all rendering.

✅ **Phase 1 — Foundations + Technical Spine complete** (Chapters 1–9).

✅ **Phase 2 — Platform & Production complete** (Chapters 10–13). Lifecycle, Platform Engineering, Reliability/Observability, Security/Privacy.

✅ **Phase 3 — Product & Strategy complete** (Chapters 14–17). Product Discovery, AI Strategy, Business Case, Pricing/GTM.

🚧 **Phase 4 — Leadership + Governance + Portfolio** are stubs (Ch 18–28).

## Per-Playbook Snapshot

### AI Engineering Director

| Phase | Description | Target |
|---|---|---|
| 0 | Skeleton | ✅ Complete |
| 1 | Chapters 1–9 (Foundations + Technical Spine) | ✅ Complete |
| 2 | Chapters 10–13 (Platform & Production) | ✅ Complete |
| 3 | Chapters 14–17 (Product & Strategy) | ✅ Complete |
| 4 | Chapters 18–25 (Leadership + Governance) + 26–28 (Portfolio) | 🚧 Stubs |
| 5 | Polish, review, publish | TBD |

### Other planned playbooks (each inherits the same shape)

- Engineering Director
- VP of Engineering
- Principal AI Scientist
- ML Researcher
- AI Engineer
- Staff Engineer

All are stubs in `book/src/` showing "Coming soon." Bootstrap recipe: see root `README.md`.

## Chapter Matrix

| # | Chapter | Status |
|---|---------|--------|
| 1 | What an AI Engineering Director Actually Does | ✅ Written (13KB) |
| 2 | The IC-to-Director Category Change | ✅ Written (12KB) |
| 3 | AI Systems Literacy | ✅ Written (15KB) |
| 4 | Build-vs-Buy Economics for AI | ✅ Written (15KB) |
| 5 | Data Foundations | ✅ Written (14KB) |
| 6 | Training, Fine-Tuning, and Continual Learning | ✅ Written (13KB) |
| 7 | Inference and Cost Engineering | ✅ Written (13KB) |
| 8 | Retrieval, Agents, and Tooling | ✅ Written (12KB) |
| 9 | Evaluation as a First-Class Discipline | ✅ Written (12KB) |
| 10 | MLOps / LLMOps Lifecycle | ✅ Written (13KB) |
| 11 | AI Platform Engineering | ✅ Written (13KB) |
| 12 | Reliability, Observability, and Incident Response for AI | ✅ Written (12KB) |
| 13 | Security, Privacy, and Abuse Vectors | ✅ Written (13KB) |
| 14 | AI Product Discovery and Roadmaps | ✅ Written (14KB) |
| 15 | AI Strategy and Roadmapping at Company Scale | ✅ Written (13KB) |
| 16 | Build a Compelling AI Business Case | ✅ Written (13KB) |
| 17 | Pricing, Packaging, and GTM for AI Features | ✅ Written (12KB) |
| 18 | Org Design and Team Topologies for AI | 🚧 Stub |
| 19 | Hiring, Onboarding, and Growing AI Talent | 🚧 Stub |
| 20 | Performance Management and Career Frames | 🚧 Stub |
| 21 | Influencing Without Authority and Executive Communication | 🚧 Stub |
| 22 | Responsible AI Frameworks and Practice | 🚧 Stub |
| 23 | The Regulatory Landscape (EU AI Act, NIST, Sector Rules) | 🚧 Stub |
| 24 | Crisis Response for AI Failures | 🚧 Stub |
| 25 | Auditability and the Audit Trail | 🚧 Stub |
| 26 | 30/60/90 Simulation | 🚧 Stub |
| 27 | The Portfolio Map (Artifact → Interview Question) | 🚧 Stub |
| 28 | System Design Appendix for AI Directors | 🚧 Stub |

## Known issues / history

- **Data loss event 2026-06-23.** A `write_file` tool truncation created a junk directory at a malformed path; `rm -rf ~/Downloads/career-playbook*` matched both the junk dir and the real `career-playbooks/`, deleting everything. Rebuilt from session context. Cost numbers in worked examples re-verified against `cost_estimator.py` output as part of the rebuild. Original git commit (Phase 0 + Ch 1–2) preserved in repo history; Phase 1 expanded to Ch 1–9 in subsequent commits.
- **mdBook 0.5.3 schema gotchas** documented in `book.toml` — uses `fold = { level = 1 }`, drops `multilingual`, places `site-url` under `[output.html]`.
- **publish.py rename (2026-06-23).** Originally mirrored chapters into `<slug>/chapters/` subdir; fixed to mirror flat at `<slug>/chapter-NN.md` to match SUMMARY.md links and the rendered HTML site. The old nested mirror and stale `chapter-NN.html` build artifacts were removed in commit `48a1c69`.
- **Live site:** https://webmakin.github.io/career-playbooks/ — auto-deployed via `.github/workflows/deploy-book.yml` (lint + build + Pages deploy) on every push to main.

## Verification gates (the BGFS discipline)

Every Phase requires these gates to exit 0:

1. `python3 _shared/tools/rubric_linter.py --all` → all 28 chapter stubs PASS.
2. `python3 _shared/tools/score_drill.py --fixture` → rubric scorer runs (19/25 on bundled fixture).
3. `python3 _shared/tools/cost_estimator.py --fixture` → LLM cost model runs (corrected growth math).
4. `mdbook build` → site builds to `site/`.
5. (Phase 1+) Concrete numbers in worked examples match real tool output.
6. (Phase 1+) Exercise bundle 4-file completeness: `ls <role>-playbook/exercises/chapterNN/{README,drill,template,worked-example}.md`.