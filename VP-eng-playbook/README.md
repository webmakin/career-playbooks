# VP of Engineering Playbook

> **The Practice-First Guide to Becoming a VP of Engineering**

![Status: Stubs](https://img.shields.io/badge/status-stubs-yellow)
![Chapters: 0/28](https://img.shields.io/badge/chapters-0%2F28-yellow)
![In progress](https://img.shields.io/badge/in%20progress-Phase%200-blue)

This is the canonical source for the VP of Engineering playbook. The published version (mdBook site) is auto-generated from these chapters via `_shared/tools/publish.py`.

## Status

**Phase 0 — Skeleton complete (2026-06-23).** 28 stub chapters generated and linter-clean. No prose yet.

Phases 1-8 (writing the 28 chapters) are next. Estimated 30 weeks to v1.0.0.

See the [plan](../.hermes/plans/2026-06-23_1530-vp-engineering-playbook-plan.md) for the full breakdown of chapters, parts, and 8 VPE-exclusive decisions.

## Who this is for

A new or aspiring VP of Engineering at a 200–2,000-person company. You are 30–90 days from a VPE interview, or you are 0–12 months into the seat. (Engineering Managers, ICs, and startup CTOs of <50-person companies will find different playbooks more useful — see the [role selector](https://github.com/webmakin/career-playbooks/blob/main/src/index/role-selector.md).)

## The 7 parts

| Part | Chapters | Theme |
|------|----------|-------|
| I — Foundations | 1–4 | What a VPE actually does, the Director-to-VP category change, leadership literacy, the org at scale |
| II — The Engineering Spine | 5–9 | Engineering strategy, architecture governance, tech debt, productivity (DORA/SPACE), quality |
| III — Platform & Production | 10–13 | Engineering lifecycle, IDP, reliability/SLOs, security/compliance at scale |
| IV — Product & Strategy | 14–17 | Engineering-Product partnership, strategy, build-vs-buy, engineering-as-revenue |
| V — Leadership | 18–21 | Org design at scale, hiring, performance management, C-suite influence |
| VI — Governance & Risk | 22–25 | Risk management, regulatory, crisis response, auditability |
| VII — The VPE's Portfolio | 26–28 | 30/60/90 at VPE level, portfolio map, system design |

## 8 VPE-exclusive decisions

The VPE role has 8 decisions that a Director simply does not face:

1. **Org-shape at 100+ engineers** (Director org design collapses past 100).
2. **Engineering budget allocation** (Director doesn't own budget across teams).
3. **Board reporting** (Director never writes board memos).
4. **M&A technical due diligence** (Director never evaluates an acquisition).
5. **Engineering strategy at company scale** (Director strategy is product-scoped; VPE strategy is company-scoped).
6. **Public speaking as engineering leader** (Director speaks to engineers; VPE speaks to the world).
7. **Performance management of other Directors** (Director manages ICs+EMs; VPE manages Directors).
8. **Engineering culture at scale** (Director culture is team; VPE culture is company).

## Cross-references

The VPE playbook cross-references the [AI Engineering Director playbook](../AI-eng-dir-playbook/) for AI-specific topics. See the [cross-references index](https://github.com/webmakin/career-playbooks/blob/main/src/index/cross-references.md) for the full map.

## Repo layout

```
VP-eng-playbook/
├── README.md             # this file
├── chapters/chap-N.md    # canonical chapter source (28 files)
├── exercises/chapterNN/  # drill + template + worked-example + README per chapter
├── resources/            # topic outline, references, plans
├── templates/            # role-specific templates (30-60-90, board memo, etc.)
└── diagrams/             # SVG/PNG diagrams (Mermaid renders inline in MD)
```

## Conventions

This playbook follows the contracts in [`_shared/`](https://github.com/webmakin/career-playbooks/tree/main/_shared/). See [Conventions](https://github.com/webmakin/career-playbooks/blob/main/book/src/index/conventions.md) for the full rule set.

## Contributing

PRs welcome. Follow the [plan](../.hermes/plans/2026-06-23_1530-vp-engineering-playbook-plan.md) for the chapter order. Each chapter should be 30–45 min of reading + ~90 min for the drill. Pace: 4 chapters per Part with check-in between Parts.