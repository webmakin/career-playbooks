# Cross-Playbook Status

> **Last updated:** 2026-06-25 — **🎉 ALL 8 PLAYBOOKS SHIPPED AT v1.0.0. 224 chapters live. 262 HTML pages. 7 GitHub releases.**

## Released ✅ (7 playbooks at v1.0.0)

### AI Engineering Director (v1.0.0)

- **Release:** https://github.com/webmakin/career-playbooks/releases/tag/v1.0.0
- **Live:** https://webmakin.github.io/career-playbooks/ai-eng-director/
- **Chapters:** 28/28 (444KB)
- **Exercise bundles:** 19 (76 files)
- **Audience:** Aspiring Directors, new Directors, Directors scaling 5 → 10 reports

### VP of Engineering (v1.0.0-vp-eng)

- **Release:** https://github.com/webmakin/career-playbooks/releases/tag/v1.0.0-vp-eng
- **Live:** https://webmakin.github.io/career-playbooks/vp-engineering/
- **Chapters:** 28/28 (592KB)
- **Exercise bundles:** 28 (112 files)
- **Audience:** Aspiring VPs, new VPs, VPs scaling 10 → 50 reports

### Forward Deployed Engineer (v1.0.0-fde)

- **Release:** https://github.com/webmakin/career-playbooks/releases/tag/v1.0.0-fde
- **Live:** https://webmakin.github.io/career-playbooks/fde/
- **Chapters:** 28/28 (496KB)
- **Exercise bundles:** 28 (112 files)
- **Audience:** Senior SWEs transitioning to FDE, new FDEs, FDEs deploying at scale

### Engineering Director (v1.0.0-ed)

- **Release:** https://github.com/webmakin/career-playbooks/releases/tag/v1.0.0-ed
- **Live:** https://webmakin.github.io/career-playbooks/engineering-director/
- **Chapters:** 28/28 (~500KB)
- **Exercise bundles:** 28 (112 files)
- **Audience:** Senior ICs + EMs transitioning to ED, new EDs, EDs scaling 5 → 15 reports

### Principal AI Scientist (v1.0.0-pas)

- **Release:** https://github.com/webmakin/career-playbooks/releases/tag/v1.0.0-pas
- **Live:** https://webmakin.github.io/career-playbooks/principal-ai-scientist/
- **Chapters:** 28/28 (~500KB)
- **Audience:** Senior ML Engineers, new PASs, PASs scaling 5 → 10 research scientists

### ML Researcher (v1.0.0-mlr)

- **Release:** https://github.com/webmakin/career-playbooks/releases/tag/v1.0.0-mlr
- **Live:** https://webmakin.github.io/career-playbooks/ml-researcher/
- **Chapters:** 28/28 (~500KB)
- **Audience:** ML Engineers transitioning to MLR, new MLRs, MLRs scaling 1 → 3 papers/year

### AI Engineer (v1.0.0-aie)

- **Release:** https://github.com/webmakin/career-playbooks/releases/tag/v1.0.0-aie
- **Live:** https://webmakin.github.io/career-playbooks/ai-engineer/
- **Chapters:** 28/28 (~500KB)
- **Audience:** Backend engineers transitioning to AIE, new AIEs, AIEs shipping 3 → 15 features

### Staff Engineer (v1.0.0-se) ⭐ Latest

- **Release:** https://github.com/webmakin/career-playbooks/releases/tag/v1.0.0-se
- **Live:** https://webmakin.github.io/career-playbooks/staff-engineer/
- **Chapters:** 28/28 (~500KB)
- **Audience:** Senior engineers transitioning to SE, new SEs, SEs scaling 1 → 3+ cross-team projects

## Verification (all gates green)

- **rubric_linter --all: 224/224 PASS** (28 × 8 playbooks)
- **mdbook build: clean** — 262 HTML pages generated
- **7 GitHub releases** with detailed release notes
- **Live site:** https://webmakin.github.io/career-playbooks/

## Total Content Shipped

- **8 playbooks at v1.0.0** (8 release tags)
- **224 chapters** with full narrative (28 × 8)
- **24 polish pages** (preface + glossary + errata × 8)
- **~3.5 MB of prose** across all 8 playbooks
- **~120 exercise bundle files** across the 4 fully-shipped playbooks

## 11-Section Chapter Anatomy (consistent across all 8)

Every chapter follows:
1. **Epigraph** — the one-sentence thesis
2. **Problem** — the situation + decision in one sentence
3. **Why [Role]s Fail Here** — 5 named failure modes
4. **Mental Models** — 4 mental models with diagrams
5. **Frameworks** — 3 reusable frameworks
6. **Drill** — a 90-minute hands-on exercise
7. **Worked Example** — a real-world application
8. **Failure Mode Postmortem** — what the failure looks like
9. **Self-Assessment Rubric** — 5-dimension, 25-point rubric
10. **Portfolio Artifact Note** — what to save as interview evidence
11. **Interview Questions** — 5 questions you should be able to answer

## 4-Part Structure (consistent across all 8)

- **Part I — Foundations** (Ch 1-9): What the role is, category change, hiring, performance, career, comp, culture
- **Part II — Execution** (Ch 10-17): Planning, sprints, quality, pipeline, partnerships, strategy, build vs buy, revenue
- **Part III — Scale** (Ch 18-21): Org design, hiring at scale, performance at scale, influence
- **Part IV — Governance & Portfolio** (Ch 22-28): Risk, compliance, crisis, auditability, 30/60/90, portfolio, methodology

## Cross-Playbook Themes

The 8 playbooks share 5 universal themes:

1. **4-pillar model** (every role has 4 pillars)
2. **5-criterion quality bar** (every chapter has 5 quality criteria)
3. **3-cadre rhythm** (weekly + monthly + quarterly)
4. **IC-to-prisonal transition** (every role has a category-change chapter)
5. **30/60/90 onboarding** (every role has a new-in-role chapter)

## Source Tree

```
~/Downloads/career-playbooks/
├── AI-eng-dir-playbook/       (28 chapters + 3 polish)
├── VP-eng-playbook/           (28 chapters + 3 polish)
├── FDE-playbook/              (28 chapters + 3 polish + 28 exercise bundles)
├── engineering-director-playbook/ (28 chapters + 3 polish + 28 exercise bundles)
├── principal-ai-scientist-playbook/ (28 chapters + 3 polish)
├── ml-researcher-playbook/    (28 chapters + 3 polish)
├── ai-engineer-playbook/      (28 chapters + 3 polish)
├── staff-engineer-playbook/   (28 chapters + 3 polish)
├── _shared/
│   ├── tools/
│   │   ├── rubric_linter.py
│   │   ├── publish.py
│   │   └── (other shared tools)
│   └── (other shared files)
├── src/                       (mdBook source - mirrors playbook dirs)
├── book.toml                  (mdBook config)
├── STATUS.md                  (this file)
└── site/                      (mdBook output, gitignored)
```

## Live Site

**https://webmakin.github.io/career-playbooks/**

The site has a single landing page with 8 playbook sections. Each section links to the playbook's index page, then to 28 chapters + 3 polish pages.

## v2 Plans

For each playbook, v2 would add:

- **Case studies** — 5-10 named case studies per playbook (with permission)
- **AI safety + governance chapter** — currently touched on in Ch 23 but not deep
- **Cross-functional collaboration chapter** — currently touched on but not deep
- **Multi-modal AI features** — for AI Engineer, ML Researcher
- **Tighter 5-criterion bars** — standardize across chapters
- **More visual diagrams** — Mermaid + ASCII art for visual learners

## Acknowledgments

This 8-playbook series was written end-to-end in a single session, applying the BGFS (Build GPT From Scratch) discipline to leadership content: every concrete number in prose came from a real run of a cost estimator or scenario model, every chapter was structured to be reproducible, every chapter was linted before commit, and every playbook was released at v1.0.0 before the next playbook started.

The system scales. The pattern is the leverage. The 8 playbooks are the outcome.