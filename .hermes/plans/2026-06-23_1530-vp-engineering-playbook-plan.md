# VP of Engineering Playbook — Detailed Plan

> **Date:** 2026-06-23
> **Author:** Hermes Agent
> **Audience:** mohammedasif (user)
> **Status:** Draft for approval

---

## 1. Why VP of Engineering is its own playbook

A VP of Engineering is **not a Director of Engineering with more reports**. The cognitive category is different. The VPE:

- Owns a **portfolio of teams** (50–500+ engineers, 5–15 Director reports), not a function.
- Sits at the **C-suite table** with the CEO/CFO/CMO/CTO, not just below it.
- Owns **budgets in the $10M–$100M/year range** with quarterly commitments to the board.
- Is the **last technical person in the chain of command** — every technical decision they defer to a Director is a Director's decision; every decision they keep is a VPE's decision.
- Has **public board presence** and **investor-facing communication** obligations.
- Owns **M&A technical due diligence**, **engineering org design at scale**, and **technical strategy at company scale**.

Most "VPE playbook" content on the internet is just a stretched EM/Director playbook with "scale it up" advice. That's wrong. The VPE has 8+ decisions that a Director simply does not face:

1. **Org-shape at 100+ engineers** (Director org design collapses past 100).
2. **Engineering budget allocation** (Director doesn't own budget allocation across teams).
3. **Board reporting** (Director never writes board memos).
4. **M&A technical due diligence** (Director never evaluates an acquisition).
5. **Engineering strategy at company scale** (Director strategy is product-scoped; VPE strategy is company-scoped).
6. **Public speaking as engineering leader** (Director speaks to engineers; VPE speaks to the world).
7. **Performance management of other Directors** (Director manages ICs+EMs; VPE manages Directors).
8. **Engineering culture at scale** (Director culture is team; VPE culture is company).

This playbook covers the **8 VPE-exclusive decisions** plus 20 Director-shared chapters (adapted to VPE scale), totaling 28 chapters across 7 parts.

---

## 2. Audience

**Primary reader:** A new or aspiring VP of Engineering at a 200–2,000-person company. You are 30–90 days from a VPE interview, or you are 0–12 months into the seat.

**Secondary readers:**
- CTOs who want to understand the VPE role.
- CEOs hiring a VPE — gives them a shared vocabulary.
- Engineering Directors targeting the VPE role.

**Not for:** Engineering Managers, ICs, or startup CTOs of <50-person companies. The VPE role is meaningful at scale; at <50 the role is more like a Director with extra hats.

---

## 3. The 11-section chapter anatomy (inherited)

Every chapter follows the same 11-section structure as the AI Engineering Director playbook:

1. Epigraph (one-line quote, tone-setter)
2. Problem (the specific decision this week)
3. Why VPEs Fail Here (3–5 named failure modes)
4. Mental Models (2–4 reusable lenses)
5. Frameworks (3 fillable templates)
6. Drill (90-min scenario, fictional VPE corp, deliverable)
7. Worked Example (fully completed drill, scored)
8. Failure Mode Postmortem (real anonymized case)
9. Self-Assessment Rubric (5 dimensions, 25 points, pass at 18+)
10. Portfolio Artifact Note (maps drill to interview evidence)
11. Interview Questions (3–5 Qs with grading notes)

The rubric linter (`_shared/tools/rubric_linter.py`) enforces the contract. Stubs must pass linter (3+ named failure modes, real `.md` deliverable path).

---

## 4. The 7 parts / 28 chapters

This is the **structure**. The content within each chapter is written in a separate phase.

### Part I — Foundations (Ch 1–4)

The VPE category change. The technical literacy a VPE needs. The org-scale problem. The strategic-context problem.

| # | Chapter | VPE-specific focus |
|---|---------|---------------------|
| 1 | What a VP of Engineering Actually Does | Owns a portfolio of teams, not a function. Sits at C-suite. Owns budget, strategy, and culture at company scale. |
| 2 | The Director-to-VP Category Change | From "make the team great" to "make the engineering org great." The locus of decisions shifts from product to company. |
| 3 | Engineering Leadership Literacy | Not coding literacy — leadership literacy. The 5 systems every VPE reads fluently: engineering org, technical strategy, financial, people, market. |
| 4 | The Engineering Org at Scale | How orgs evolve from 10 → 50 → 200 → 1,000 engineers. Conway's Law inversions. The 5 topology transitions that kill or save companies. |

### Part II — The Engineering Spine (Ch 5–9)

The things a VPE must understand deeply even if they don't do them day-to-day. The VPE is the last technical person; the buck stops here on technical calls.

| # | Chapter | VPE-specific focus |
|---|---------|---------------------|
| 5 | Engineering Strategy at Company Scale | The VPE's strategy is company-scoped, not product-scoped. The 5-Question Frame at scale. Decline lists. |
| 6 | Architecture Governance at Scale | The VPE's role on the Architecture Review Board. Standards vs. autonomy. The 4 review-board patterns that work. |
| 7 | Technical Debt Management | The VPE owns the technical-debt portfolio. The 4-debt-quadrant model. When to pay it down vs. leave it. |
| 8 | Engineering Productivity (DORA / SPACE) | The VPE's measurement system. What to measure. What not to measure. The 3-metric rule. |
| 9 | Engineering Quality at Scale | The VPE owns the quality system. The 3-tier quality bar. The 4-quality-debt traps. |

### Part III — Platform & Production (Ch 10–13)

How the VPE operates the platform, the production system, and the reliability posture. These are mostly Director chapters scaled up.

| # | Chapter | VPE-specific focus |
|---|---------|---------------------|
| 10 | Engineering Lifecycle (Discovery → Decom) | The VPE owns the lifecycle across the portfolio. The 6 stages, the gates, the named owners. |
| 11 | Platform Engineering (Internal Developer Platform) | The VPE's IDP ownership. The platform-product duality. The 4-platform-org-patterns. |
| 12 | Reliability, SLOs, and Incident Response at Scale | The VPE owns the SLO system. The cross-team incident command. The page-tier rules. |
| 13 | Security, Privacy, Compliance at Scale | The VPE's relationship with the CISO. The 4 security postures. The compliance framework. |

### Part IV — Product & Strategy (Ch 14–17)

The VPE's relationship with the CPO, the CEO, and the product organization. The VPE is a co-equal of the CPO at the C-suite.

| # | Chapter | VPE-specific focus |
|---|---------|---------------------|
| 14 | Engineering ↔ Product Partnership | The VPE-CPO relationship. The 3-partnership-models. The conflict-resolution pattern. |
| 15 | Engineering Strategy & Roadmaps at Company Scale | The VPE's strategy is 3-year, not quarterly. The portfolio roadmap. The 5-Question Frame. |
| 16 | Build vs. Buy at the Engineering Layer | The VPE's portfolio-level build-vs-buy. The 5-dimension matrix. The 4-skip-build patterns. |
| 17 | Engineering Pricing, GTM, and Engineering-as-Revenue | The VPE's role when engineering is a product. The 3-engineering-revenue models. |

### Part V — Leadership (Ch 18–21)

The VPE's people leadership. The Director chapters on hiring, performance, influence, org design — adapted to VPE scale (50–500 reports, multi-team, C-suite presence).

| # | Chapter | VPE-specific focus |
|---|---------|---------------------|
| 18 | Engineering Org Design at Scale | The VPE's org architecture. The 5-topology-decision model. The scale transitions. |
| 19 | Hiring, Onboarding, and Growing Engineering Talent | The VPE's hiring system for senior leaders. The 3-round loop. The 30-60-90 onboarding for Directors. |
| 20 | Performance Management and Career Frames | The VPE's Director-level perf system. The 5-level Director ladder. The "promote out of role" pattern. |
| 21 | Influencing at the C-Suite | The VPE's relationship with the CEO, CFO, CTO, CPO. The 4-influence-channels. The board-communication skill. |

### Part VI — Governance & Risk (Ch 22–25)

The VPE's governance portfolio. The Director chapters on Responsible AI, regulatory, crisis, auditability — adapted to VPE scale (multi-team, public-facing, board-reportable).

| # | Chapter | VPE-specific focus |
|---|---------|---------------------|
| 22 | Engineering Risk Management | The VPE's risk portfolio. The 4-risk-tier model. The risk-acceptance process. |
| 23 | Regulatory Landscape for Engineering | The VPE's regulatory exposure. The 4-regulation-stack. The sector-specific rules. |
| 24 | Crisis Response at Scale | The VPE's crisis leadership. The 5-level severity ladder at scale. The public-statement discipline. |
| 25 | Engineering Auditability | The VPE's audit system. The 7-element audit trail. The compliance posture. |

### Part VII — The VPE's Portfolio (Ch 26–28)

The capstone: the artifacts the VPE brings into the seat and the board.

| # | Chapter | VPE-specific focus |
|---|---------|---------------------|
| 26 | 30/60/90 at the VPE Level | The VPE's first 90 days. The 5-window strategy. The board-readiness plan. |
| 27 | The VPE Portfolio Map | The 25+ artifacts a VPE needs. The 3-layer portfolio. The board-deck. |
| 28 | System Design Appendix for VPEs | The VPE's system design interview. The 8-dimension coverage. The cost-quality-headcount triangle. |

---

## 5. Phased delivery

**Phase 0 — Skeleton (1 week).** Bootstrap the directory tree, generate 28 stub chapters that pass `rubric_linter`, regenerate `SUMMARY.md` with the new role, update the placeholder role READMEs to reflect "in progress." End state: `mdbook build` succeeds, linter passes 28/28, deploy runs.

**Phase 1 — Part I (Ch 1–4, weeks 2–5).** Foundations, Director-to-VP category change, leadership literacy, org at scale.

**Phase 2 — Part II (Ch 5–9, weeks 6–10).** Engineering spine: strategy, architecture, tech debt, productivity, quality.

**Phase 3 — Part III (Ch 10–13, weeks 11–14).** Platform + production at scale.

**Phase 4 — Part IV (Ch 14–17, weeks 15–18).** Product partnership + strategy.

**Phase 5 — Part V (Ch 18–21, weeks 19–22).** Leadership at scale.

**Phase 6 — Part VI (Ch 22–25, weeks 23–26).** Governance and risk.

**Phase 7 — Part VII (Ch 26–28, weeks 27–29).** Portfolio capstone.

**Phase 8 — Polish + v1.0.0 (week 30).** Preface, glossary, errata, release tag.

Total: 30 weeks. The AI Eng Director playbook took ~12 hours in a single session; this one will be similar in scope but each chapter will be more focused on VPE scale (not AI-specific).

---

## 6. Verification gates (inherited from AI Eng Director playbook)

Same 4 gates, same scripts:

1. `python3 _shared/tools/rubric_linter.py --all` → 28/28 PASS.
2. `python3 _shared/tools/score_drill.py --fixture` → exit 0.
3. `python3 _shared/tools/cost_estimator.py --fixture` → exit 0 (some VPE chapters will need a different cost model — engineering headcount cost, infra cost — add `engineering_economics.py` to `_shared/tools/` in Phase 1).
4. `mdbook build` → exit 0, site renders.

**New gate for VPE:** a `headcount_model.py` tool that models engineering org cost (avg comp, ramp time, retention). The VPE playbook needs headcount math the AI Eng Director playbook didn't. Add in Phase 1.

---

## 7. Tooling additions

**New tool:** `_shared/tools/headcount_model.py`. Models:
- Engineering headcount cost (base + bonus + equity + benefits + on-costs).
- Ramp time (months to full productivity per level).
- Retention risk (probability of leaving per level per quarter).
- Hiring funnel (reqs → offers → accept → ramp).
- Org-shape cost (cost ratio Director:EM:IC).

**Updated tool:** `_shared/tools/publish.py`. Add `vp-engineering` to the SLUG_MAP. The current `publish.py` already supports multi-role, so this is a 1-line addition.

**Updated file:** `_shared/CHANGELOG.md`. Add VP-eng entry.

---

## 8. Multi-book strategy decisions

| Decision | Choice | Reasoning |
|---|---|---|
| **Same book, subpath, or new repo?** | Same repo, subpath-per-role | Inherited from AI Eng Director. Subpath `/career-playbooks/vp-engineering/` is the URL. |
| **Share `_shared/`?** | Yes | All playbooks inherit the same anatomy, linter, scoring, and conventions. |
| **Separate exercise bundles?** | Yes, per-role | `VP-eng-playbook/exercises/chapterNN/` mirrors the AI-eng-dir structure. |
| **Tag for v1.0.0 separately?** | Yes | Each playbook has its own version. v1.0.0 of AI-eng-dir is independent of v0.0.1 of vp-engineering. |
| **Cross-references between playbooks?** | Yes, light | Some chapters cite the AI Eng Director playbook explicitly (e.g., "for AI-specific cost modeling, see AI-eng-dir Ch 7"). |
| **Independent ship cadence?** | Yes | Each playbook ships when its author declares it done. v1.0.0 of AI-eng-dir shipped 2026-06-23; vp-engineering will ship ~7 months later at the current pace. |

---

## 9. Open questions for the user

1. **Pace.** 30 weeks is the recommended pace. Do you want 4-chapter batches (option b from AI-eng-dir) or larger batches? Same "check-in at Part boundary" rule.

2. **Tooling.** Add `headcount_model.py` in Phase 1 (immediately) or in Phase 5 (when Ch 18-21 org-design chapters need it)? Recommendation: Phase 1, so the foundations chapters can cite it.

3. **Cross-references to AI-eng-dir.** The VPE playbook will reference the AI Eng Director playbook for AI-specific topics. Should the cross-references be inline (e.g., "see AI-eng-dir Ch 7") or full sections adapted? Recommendation: inline cross-references, since the AI Eng Director is the canonical source.

4. **VPE name conventions.** The playbook will use "VPE" as shorthand. The full role titles to reference are "VP of Engineering" and "EVP of Engineering." Should I distinguish? Recommendation: VPE is the standard shorthand; I'll define the difference in the glossary.

5. **CTO overlap.** VPE and CTO often overlap. The playbook will assume VPE reports to CEO (with CTO as a separate role above or alongside). Alternative: VPE reports to CTO. Recommendation: I default to VPE reports to CEO (the more common modern structure), but Ch 2 (Director-to-VP category change) will discuss both.

6. **The 8 VPE-exclusive decisions.** Are these the right 8? Or are there 1-2 I'm missing? (Examples: 6a — "Engineering culture at scale" might be a Part on its own; 6b — "Acquisitions" might warrant more than a chapter; 6c — "Engineering org design during hypergrowth" is implicit in Ch 18 but might warrant its own chapter.) Recommendation: ship the 28-chapter plan, see if the gaps show up during writing, expand in v1.1.

---

## 10. Plan execution — first 90 minutes

**Step 1 (this turn, ~30 min):** User approves the plan (or sends revisions).

**Step 2 (~30 min):** Bootstrap:
- Create `VP-eng-playbook/` directory + `chapters/` + `exercises/` + `resources/`.
- Generate 28 stub chapters using `_template.md` (inherited from `AI-eng-dir-playbook/chapters/_template.md`).
- Run `python3 _shared/tools/rubric_linter.py --all` → 28/28 PASS.
- Mirror to `src/vp-engineering/chapter-NN.md` via updated `publish.py`.
- Update `src/SUMMARY.md` to include the new role.
- Update `src/vp-engineering/README.md` from "coming soon" to "in progress."
- Update the other 5 placeholder role READMEs to clarify which is in-progress vs. truly "coming soon."

**Step 3 (~30 min):** Build + deploy:
- `mdbook build` → exit 0.
- Commit + push.
- Wait for GitHub Actions deploy (~1 min).
- Verify live site shows the new role in the sidebar.

**Step 4:** Pause for user feedback before starting to write Ch 1.

---

## 11. Risks and mitigations

| Risk | Severity | Mitigation |
|---|---|---|
| User doesn't want another 28-chapter build | HIGH | Stop-and-look after bootstrap. If user wants 15 chapters instead, restructure. |
| `headcount_model.py` is too big a detour | MED | Build minimal version in Phase 1. Expand in Phase 5. |
| Cross-references to AI-eng-dir are confusing | LOW | Cross-refs only point to chapter + title, not deep details. |
| The VPE playbook overlaps too much with AI-eng-dir | MED | Each VPE chapter explicitly names the AI-eng-dir chapter it differs from. The 8 VPE-exclusive decisions are the spine. |
| 30-week timeline is unrealistic | MED | Recommend 30 weeks. User can compress. |

---

## 12. Approval requested

This plan is a draft. Please review and reply with:

1. **Approve as-is** → I bootstrap the directory tree and pause for feedback.
2. **Approve with revisions** → I make your revisions and pause.
3. **Defer** → I do nothing until you say otherwise.

The bootstrap (Step 2 above) is reversible — it's just files in a directory tree. Nothing is pushed to GitHub until I get a "go" from you.

— Hermes Agent, 2026-06-23