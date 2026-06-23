# Cross-Playbook Status

> **Last updated:** 2026-06-23 — Phase 0 complete; Phase 1 (Foundations + Technical Spine, Ch 1–9) being rebuilt after data loss.

## Current Phase

🚧 **Phase 0 — Skeleton complete.** Local build verified. Site landing + 28 chapter stubs + 7 part dividers + role-selector + cross-references + conventions page all rendering.

🚧 **Phase 1 — Being rebuilt.** Chapters 1–4 (Foundations) and Chapters 5–9 (Technical Spine) previously complete and reviewed; recreating from session context.

## Per-Playbook Snapshot

### AI Engineering Director

| Phase | Description | Target |
|---|---|---|
| 0 | Skeleton | ✅ Complete |
| 1 | Chapters 1–9 + foundational templates | 🚧 Rebuilding |
| 2 | Chapters 10–17 | TBD |
| 3 | Chapters 18–25 | TBD |
| 4 | Chapters 26–28 + appendices + portfolio map | TBD |
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
| 1 | What an AI Engineering Director Actually Does | 🚧 Rebuilding |
| 2 | The IC-to-Director Category Change | 🚧 Rebuilding |
| 3 | AI Systems Literacy | 🚧 Rebuilding |
| 4 | Build-vs-Buy Economics for AI | 🚧 Rebuilding |
| 5 | Data Foundations | 🚧 Rebuilding |
| 6 | Training, Fine-Tuning, and Continual Learning | 🚧 Rebuilding |
| 7 | Inference and Cost Engineering | 🚧 Rebuilding |
| 8 | Retrieval, Agents, and Tooling | 🚧 Rebuilding |
| 9 | Evaluation as a First-Class Discipline | 🚧 Rebuilding |
| 10–28 | (see `SUMMARY.md`) | 🚧 Stub |

## Known issues

- **Data loss event 2026-06-23.** A `write_file` tool truncation created a junk directory at a malformed path; `rm -rf ~/Downloads/career-playbook*` matched both the junk dir and the real `career-playbooks/`, deleting everything. Rebuilt from session context. Cost numbers in worked examples are being re-verified against `cost_estimator.py` output as part of the rebuild.

## Verification gates (the BGFS discipline)

Every Phase requires these gates to exit 0:

1. `python3 _shared/tools/rubric_linter.py --all` → all chapter stubs PASS.
2. `python3 _shared/tools/score_drill.py --fixture` → rubric scorer runs.
3. `python3 _shared/tools/cost_estimator.py --fixture` → LLM cost model runs.
4. `mdbook build` → site builds to `book/dist/`.
5. (Phase 1+) Concrete numbers in worked examples match real tool output.
6. (Phase 1+) Exercise bundle 4-file completeness: `ls <role>-playbook/exercises/chapterNN/{README,drill,template,worked-example}.md`.