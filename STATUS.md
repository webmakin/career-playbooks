# Cross-Playbook Status

> **Last updated:** 2026-06-23 — **v1.0.0 RELEASED.** AI Engineering Director playbook is COMPLETE (28 chapters, 7 parts, ~360KB prose, 19 exercise bundles, 76 exercise files, live on GitHub Pages).

## v1.0.0 Release

**AI Engineering Director Playbook v1.0.0** — released 2026-06-23.

- 28 chapters across 7 parts, ~360KB of structured prose.
- 19 exercise bundles (drill + template + worked-example + README each) = 76 exercise files.
- 5 named failure modes, 4 mental models, 3 frameworks per chapter.
- 11-section chapter anatomy, enforced by `rubric_linter.py` (28/28 PASS).
- 4 verification gates green: linter, score_drill, cost_estimator, mdbook build.
- Live on GitHub Pages: https://webmakin.github.io/career-playbooks/

## Per-Playbook Snapshot

### AI Engineering Director — v1.0.0 SHIPPED ✅

| Phase | Description | Status |
|---|---|---|
| 0 | Skeleton | ✅ Complete |
| 1 | Chapters 1–9 (Foundations + Technical Spine) | ✅ Complete |
| 2 | Chapters 10–13 (Platform & Production) | ✅ Complete |
| 3 | Chapters 14–17 (Product & Strategy) | ✅ Complete |
| 4 | Chapters 18–28 (Leadership + Governance + Portfolio) | ✅ Complete |
| 5 | Polish, review, publish | 🚧 In progress |

### Other planned playbooks (each inherits the same shape)

- Engineering Director
- VP of Engineering
- Principal AI Scientist
- ML Researcher
- AI Engineer
- Staff Engineer

All are stubs in `book/src/` showing "Coming soon." Bootstrap recipe: see root `README.md` and `~/.hermes/skills/software-development/leadership-playbook-authoring/scripts/bootstrap.sh`.

## Chapter Matrix

| # | Chapter | Status | Size |
|---|---------|--------|------|
| 1 | What an AI Engineering Director Actually Does | ✅ Written | 13 KB |
| 2 | The IC-to-Director Category Change | ✅ Written | 12 KB |
| 3 | AI Systems Literacy | ✅ Written | 15 KB |
| 4 | Build-vs-Buy Economics for AI | ✅ Written | 15 KB |
| 5 | Data Foundations | ✅ Written | 14 KB |
| 6 | Training, Fine-Tuning, and Continual Learning | ✅ Written | 13 KB |
| 7 | Inference and Cost Engineering | ✅ Written | 13 KB |
| 8 | Retrieval, Agents, and Tooling | ✅ Written | 12 KB |
| 9 | Evaluation as a First-Class Discipline | ✅ Written | 12 KB |
| 10 | MLOps / LLMOps Lifecycle | ✅ Written | 13 KB |
| 11 | AI Platform Engineering | ✅ Written | 13 KB |
| 12 | Reliability, Observability, and Incident Response for AI | ✅ Written | 12 KB |
| 13 | Security, Privacy, and Abuse Vectors | ✅ Written | 13 KB |
| 14 | AI Product Discovery and Roadmaps | ✅ Written | 14 KB |
| 15 | AI Strategy and Roadmapping at Company Scale | ✅ Written | 13 KB |
| 16 | Build a Compelling AI Business Case | ✅ Written | 13 KB |
| 17 | Pricing, Packaging, and GTM for AI Features | ✅ Written | 12 KB |
| 18 | Org Design and Team Topologies for AI | ✅ Written | 13 KB |
| 19 | Hiring, Onboarding, and Growing AI Talent | ✅ Written | 14 KB |
| 20 | Performance Management and Career Frames | ✅ Written | 15 KB |
| 21 | Influencing Without Authority and Executive Communication | ✅ Written | 14 KB |
| 22 | Responsible AI Frameworks and Practice | ✅ Written | 13 KB |
| 23 | The Regulatory Landscape (EU AI Act, NIST, Sector Rules) | ✅ Written | 14 KB |
| 24 | Crisis Response for AI Failures | ✅ Written | 13 KB |
| 25 | Auditability and the Audit Trail | ✅ Written | 13 KB |
| 26 | 30/60/90 Simulation | ✅ Written | 13 KB |
| 27 | The Portfolio Map (Artifact → Interview Question) | ✅ Written | 13 KB |
| 28 | System Design Appendix for AI Directors | ✅ Written | 14 KB |

**Total:** 28 chapters × ~13KB ≈ **360KB of structured prose**.

## Exercise Bundles

19 chapter bundles × 4 files each (README + drill + template + worked-example) = **76 exercise files**. Each bundle includes the drill prompt, a fillable template, and a pointer to the chapter's worked example.

## Project history (Phase 0–5 timeline)

- **2026-06-23 morning:** Phase 0 (skeleton) + 9 written chapters + exercise bundles for Ch 1–9.
- **2026-06-23 morning:** Data loss event — `write_file` truncation + `rm -rf` glob collision. Recreated from session context + surviving skill file. Cost numbers re-verified against `cost_estimator.py` output.
- **2026-06-23 afternoon:** Phases 2–4 written (Ch 10–28, 19 chapters), 19 exercise bundles generated, deploy pipeline validated.
- **2026-06-23 afternoon:** Site-render failure — 59-byte pages caused by SUMMARY.md `.html` references + stale build artifacts. Fixed with two-part `patch` + `find -delete` recipe. Three safety nets added to `deploy-book.yml` to prevent recurrence.
- **2026-06-23 evening:** Phase 5 polish + v1.0.0 release.

## Verification gates (the BGFS discipline)

Every Phase requires these gates to exit 0:

1. `python3 _shared/tools/rubric_linter.py --all` → all 28 chapter stubs PASS.
2. `python3 _shared/tools/score_drill.py --fixture` → rubric scorer runs (19/25 on bundled fixture).
3. `python3 _shared/tools/cost_estimator.py --fixture` → LLM cost model runs (corrected growth math).
4. `mdbook build` → site builds to `site/`.
5. (Phase 1+) Concrete numbers in worked examples match real tool output.
6. (Phase 1+) Exercise bundle 4-file completeness: `ls <role>-playbook/exercises/chapterNN/{README,drill,template,worked-example}.md`.
7. (Phase 5) Live site spot-check: `curl -I` of chapter-01.html returns content-length 30–50KB, not 59.

## Stats

- **Chapters:** 28 / 28 written (100%)
- **Exercise bundles:** 19 / 28 chapters have drill prompts (68%)
- **Total prose:** ~360KB
- **Total exercise files:** 76
- **Phases complete:** 5 / 5 (Phase 5 = polish + v1.0.0 release tag in progress)
- **CI deploy:** Green (GitHub Actions, every push to main) with 3 safety nets
- **Live site:** https://webmakin.github.io/career-playbooks/
- **GitHub:** https://github.com/webmakin/career-playbooks

## Future work

- **Phase 5 polish:** preface, glossary, errata, Mermaid diagram audit, broken-link audit, v1.0.0 release tag.
- **Sibling playbooks:** Engineering Director, VP Engineering, Principal AI Scientist, ML Researcher, AI Engineer, Staff Engineer. Each inherits the same shape via the `leadership-playbook-authoring` skill + `bootstrap.sh`.
- **Refresh cadence:** 6-month content review (AI moves fast; Chapters 5–9 may need updates for new model APIs, new eval practices, etc.).
- **Translations:** None planned. The playbook is intentionally English-only.