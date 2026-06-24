# Forward Deployed Engineer Playbook — Detailed Plan

> **Date:** 2026-06-24
> **Author:** Hermes Agent
> **Audience:** mohammedasif (user)
> **Status:** Draft for approval

---

## 1. Why the FDE role needs its own playbook

A Forward Deployed Engineer (FDE) is **not a customer success engineer**, **not a professional services consultant**, **not a sales engineer**, and **not a regular SWE who occasionally talks to a customer**. The FDE is a distinct role that has emerged in the last 10 years at companies like Palantir, Anthropic, OpenAI, Scale AI, Anduril, and a growing set of B2B AI startups. The role has a specific cognitive shape:

- **Senior IC technical depth** (Staff/Principal equivalent, 6-15 years experience).
- **Product ownership at the customer edge** (writes the requirements that get built into the core product).
- **Customer-facing risk** (their name is on the customer relationship; their judgment is on the line at every deploy).
- **Time-to-impact in days, not quarters** (they ship a working prototype at the customer in week 1).

The FDE role is the most misunderstood role in the AI-era tech org. Most "FDE playbooks" on the internet are either:

1. **Customer Success playbooks repackaged** (relationship management, not engineering).
2. **Professional Services playbooks repackaged** (deployment methodology, not product feedback).
3. **Staff Engineer playbooks repackaged** (technical depth, not customer integration).

None of these is right. The FDE role is a hybrid that has its own cognitive category, its own career ladder, its own failure modes, and its own relationship to the rest of the org. This playbook covers the FDE role properly.

---

## 2. Audience

**Primary reader:** A new or aspiring Forward Deployed Engineer at a B2B AI/tech company. You are:
- 0-6 months into an FDE role, or
- 30-90 days from an FDE interview, or
- A Staff/Principal SWE considering a pivot to FDE.

**Secondary readers:**
- Engineering Directors who manage FDE teams (cross-ref to the AI Eng Director / VP Eng playbooks).
- Founders/CEOs hiring their first 5 FDEs.
- PMs who work with FDEs on the customer feedback loop.

**Not for:** Customer Success Managers, Account Executives, Professional Services Consultants, or first-year SWEs. The FDE role requires senior-IC technical depth that those roles don't.

---

## 3. The 11-section chapter anatomy (inherited)

Every chapter follows the same 11-section structure as the other playbooks:

1. Epigraph
2. Problem (the specific decision this week)
3. Why FDEs Fail Here (5 named failure modes)
4. Mental Models (4 reusable lenses)
5. Frameworks (3 fillable templates)
6. Drill (90-min scenario, fictional FDE at acme-corp)
7. Worked Example (fully completed drill, scored)
8. Failure Mode Postmortem (real anonymized case)
9. Self-Assessment Rubric (5 dimensions, 25 points, pass at 18+)
10. Portfolio Artifact Note
11. Interview Questions (5 Qs with grading notes)

The rubric linter enforces the contract. The publish.py tool mirrors to the mdBook site.

---

## 4. The 7 parts / 28 chapters

### Part I — Foundations (Ch 1–4)

The FDE category. The IC-to-FDE shift. The customer edge. The product edge.

| # | Chapter | FDE-specific focus |
|---|---------|---------------------|
| 1 | What a Forward Deployed Engineer Actually Does | The hybrid IC-PM-CS role. Owns the customer outcome end-to-end. Writes code daily AND owns the customer relationship AND drives product feedback. |
| 2 | The IC-to-FDE Category Change | From "build features for a roadmap" to "ship a working solution to a customer, then turn what you learned into a product feature." The time-to-impact is days, not quarters. |
| 3 | The Customer Edge | How FDEs read customer orgs, politics, decision-making, and incentives. The customer is not a single person — it's a complex org with stakeholders, blockers, and champions. |
| 4 | The Product Edge | How FDEs drive product feedback. The "voice of the customer" is not a Slack channel — it's a working relationship with the PM, the EM, and the Director. The FDE's product feedback is the most valuable feedback in the org. |

### Part II — The FDE Technical Spine (Ch 5–9)

The things an FDE must understand deeply even if they don't own them day-to-day. FDEs are senior ICs — they need to be able to ship at customer sites in unfamiliar stacks.

| # | Chapter | FDE-specific focus |
|---|---------|---------------------|
| 5 | The Deployment Stack | Every FDE needs to know CI/CD, observability, auth, and infra deeply enough to debug at a customer site. The FDE's job is to ship a working solution, not to design the platform. |
| 6 | Data Engineering for FDEs | FDEs need to read a customer's data model, write a connector in 3 days, and produce a working data pipeline. Data engineering is the most common FDE bottleneck. |
| 7 | ML/AI Systems for FDEs | At AI companies, FDEs need to understand training, fine-tuning, RAG, agents, and evaluation deeply enough to deploy AI features at customer sites. The FDE's AI fluency separates good FDEs from great ones. |
| 8 | Integration Patterns | FDEs deploy into customer environments. The integration patterns (API, batch, event stream, file drop, custom) and their trade-offs. The FDE's integration choices determine whether the deployment is a success or a 6-month project. |
| 9 | Performance, Cost, and Scale at the Customer | Every FDE deployment has a cost dimension. The FDE owns the unit economics of the customer's deployment. Cost surprises kill FDE projects. |

### Part III — Customer & Deployment (Ch 10–13)

How the FDE operates at the customer site. The deployment methodology. The customer relationship. The crisis management.

| # | Chapter | FDE-specific focus |
|---|---------|---------------------|
| 10 | The Deployment Methodology | The 6-phase deployment (Discovery → Design → Pilot → Production → Operate → Hand-off). The FDE's job is to get to Production in 6-12 weeks, not 6-12 months. |
| 11 | The Customer Relationship | How FDEs build trust, manage expectations, navigate politics, and become the customer's trusted advisor. The relationship is the FDE's primary asset. |
| 12 | Crisis at the Customer Site | When the deployment goes wrong (data loss, security incident, performance failure), the FDE is the first responder. Crisis management is the FDE's most-tested skill. |
| 13 | Hand-off and Renewal | The FDE hands off the deployment to the customer's internal team (or the company's Customer Success team). The hand-off is the most-skipped part of the FDE job — and the most important for retention. |

### Part IV — Product & Strategy (Ch 14–17)

The FDE's relationship with the product org, the engineering org, and the strategic decisions that come from customer deployments.

| # | Chapter | FDE-specific focus |
|---|---------|---------------------|
| 14 | The FDE-PM Partnership | The FDE and PM have the most important partnership in the company. The FDE has the customer truth; the PM has the product strategy. The 3 partnership models and the FDE's role in each. |
| 15 | The FDE Feedback Loop | The FDE's customer feedback is the most valuable feedback in the org. The 4-step feedback loop (Capture → Synthesize → Prioritize → Ship). The FDE's job is to make the feedback actionable, not just collect it. |
| 16 | The FDE's Influence on Product Strategy | The FDE sees patterns across 5-10 customer deployments. The patterns are the company's product strategy. The FDE's job is to surface the patterns to the product org. |
| 17 | The FDE as a Product Leader | At the senior FDE level (Principal FDE), the FDE owns a product area. The Principal FDE is a hybrid IC-PM-Director. The most senior FDEs are the most senior product leaders in the company. |

### Part V — Career & Leadership (Ch 18–21)

The FDE career ladder, the FDE's leadership, the FDE's influence without authority, and the FDE's relationship to the rest of the org.

| # | Chapter | FDE-specific focus |
|---|---------|---------------------|
| 18 | The FDE Career Ladder | The FDE ladder is short (typically 4 levels) and horizontal (with one or two senior levels). Most FDEs don't want to become managers. The career path is a horizontal ladder with 1-2 IC levels above Staff. |
| 19 | Hiring, Onboarding, Growing FDE Talent | FDE hiring is different from SWE hiring. FDE candidates need customer-facing skills, product instinct, AND technical depth. The interview loop is different. The onboarding is 3-6 months. |
| 20 | FDE Performance Management | FDE perf is measured on customer outcomes (deployment success, customer satisfaction, retention), not just technical output. The 5-dimension FDE rubric. |
| 21 | FDE Leadership Without Authority | The FDE has no direct reports (usually). The FDE influences the PM, the EM, the Director, the customer, the customer success team. The FDE's leadership is the purest form of influence without authority. |

### Part VI — Governance & Risk (Ch 22–25)

The FDE's governance portfolio. The customer data, the security, the compliance, the auditability.

| # | Chapter | FDE-specific focus |
|---|---------|---------------------|
| 22 | Customer Data Governance | FDEs handle customer data at customer sites. The data governance rules (PII, retention, access) are the FDE's responsibility. The FDE's job is to ship without violating data rules. |
| 23 | Security and Compliance at the Customer | FDEs deploy into customer environments. The security and compliance rules differ by customer (HIPAA, FedRAMP, GDPR, etc.). The FDE's job is to know the rules and deploy within them. |
| 24 | FDE Crisis Response | When the customer has a security incident, the FDE is the first responder. The FDE's crisis response playbook is the company's brand. |
| 25 | The FDE Audit Trail | FDE work is hard to audit (customer-facing, time-pressured, one-off solutions). The audit trail is the FDE's discipline — every deployment is documented, every customer interaction is logged. |

### Part VII — The FDE's Portfolio (Ch 26–28)

The capstone: the artifacts the FDE brings into the seat and the next role.

| # | Chapter | FDE-specific focus |
|---|---------|---------------------|
| 26 | 30/60/90 as an FDE | The FDE's first 90 days. The 3-customer ramp. The 3 product feedback patterns. The relationship with the PM. |
| 27 | The FDE Portfolio Map | The 15+ artifacts an FDE needs. The 3-layer portfolio (technical, customer, product). The interview deck for the next role. |
| 28 | System Design Appendix for FDEs | The FDE's system design interview. The customer-aware design. The 6-dimension coverage. The cost-reliability-time triangle. |

---

## 5. The 8 FDE-exclusive decisions

A regular SWE does not face these decisions. The FDE does, weekly.

1. **Time allocation** (3-5 customers, 1-2 deployments each, 60% time on customer, 40% on product feedback).
2. **Customer priorities** (which customer gets the FDE this week when 3 customers are blocked).
3. **Deployment trade-offs** (the FDE's "good enough" vs the engineer's "perfect").
4. **Product feedback priority** (which feedback gets pushed to the PM and which gets deferred).
5. **Customer escalation** (when to escalate to the Director vs handle it yourself).
6. **Customer-side technical decisions** (architecture choices that the FDE makes on the customer's behalf, in the customer's environment).
7. **Hand-off timing** (when to hand off the deployment to the customer success team).
8. **FDE career path** (when to stay in FDE, when to pivot to PM, when to pivot to Eng Manager).

This playbook covers the 8 FDE-exclusive decisions plus 20 SWE/PM/CS-shared chapters (adapted to FDE scale), totaling 28 chapters across 7 parts.

---

## 6. Phased delivery

**Phase 0 — Skeleton (1 session).** Bootstrap the directory tree, generate 28 stub chapters that pass `rubric_linter`, regenerate `SUMMARY.md` with the new role, update the placeholder role READMEs. End state: `mdbook build` succeeds, linter passes 84/84 (28 AI + 28 VP-eng + 28 FDE), deploy runs.

**Phase 1 — Part I (Ch 1–4, sessions 2-3).** Foundations, IC-to-FDE shift, customer edge, product edge.

**Phase 2 — Part II (Ch 5–9, sessions 4-6).** FDE technical spine: deployment stack, data eng, ML/AI, integration, performance.

**Phase 3 — Part III (Ch 10–13, sessions 7-8).** Customer + deployment: methodology, relationship, crisis, hand-off.

**Phase 4 — Part IV (Ch 14–17, sessions 9-10).** Product + strategy: FDE-PM, feedback loop, strategy influence, FDE as product leader.

**Phase 5 — Part V (Ch 18–21, sessions 11-12).** Career + leadership: ladder, hiring, perf, influence.

**Phase 6 — Part VI (Ch 22–25, sessions 13-14).** Governance + risk: data, security, crisis, audit.

**Phase 7 — Part VII (Ch 26–28, session 15).** Portfolio capstone.

**Phase 8 — Polish + v1.0.0 (session 16).** Preface, glossary, errata, release tag.

Total: 16 sessions over 2-4 weeks at the current pace (1 Part per session).

---

## 7. Tooling

**Inherited tools (no changes):**
- `_shared/tools/rubric_linter.py` — 11-section anatomy enforcement (multi-role).
- `_shared/tools/score_drill.py` — drill grading.
- `_shared/tools/publish.py` — chapter mirror (multi-role, will add `FDE-playbook` to SLUG_MAP).

**New tool needed:** `_shared/tools/deployment_economics.py`. Models:
- Customer deployment cost (engineering + customer success + infrastructure).
- Time-to-deployment (Discovery → Production in weeks).
- Customer LTV vs. deployment cost (the FDE ROI calculation).
- Customer retention (renewal rate by FDE vs. no FDE).

The FDE playbook needs deployment economics that the other playbooks didn't. Add in Phase 0.

**Updated tool:** `rubric_linter.py` and `publish.py` SLUG_MAP. Add `FDE-playbook` entry. ~5 lines of change.

---

## 8. Multi-book strategy decisions

| Decision | Choice | Reasoning |
|---|---|---|
| **Same book, subpath, or new repo?** | Same repo, subpath-per-role | Inherited. Subpath `/career-playbooks/fde/`. |
| **Share `_shared/`?** | Yes | All playbooks inherit the same anatomy, linter, scoring, and conventions. |
| **Separate exercise bundles?** | Yes, per-role | `FDE-playbook/exercises/chapterNN/` mirrors the AI-eng-dir and VP-eng structures. |
| **Tag for v1.0.0 separately?** | Yes | Each playbook has its own version. |
| **Cross-references to other playbooks?** | Yes, light | FDE cross-references AI Eng Director (for AI deployment), VP Eng (for org design), and Principal AI Scientist (for research-to-product). |
| **Independent ship cadence?** | Yes | Each playbook ships when its author declares it done. |

---

## 9. Open questions for the user

1. **Pace.** 16 sessions over 2-4 weeks is the recommended pace. Do you want batched Parts (1 Part per session = 1 user turn) or smaller batches? Same Part check-in rule.

2. **Tooling.** Add `deployment_economics.py` in Phase 0 (immediately) or in Phase 2 (when Ch 5-9 tech spine needs it)? Recommendation: Phase 0.

3. **Cross-references.** FDE cross-refs AI Eng Director for AI deployment, VP Eng for org design, Principal AI Scientist for research-to-product. Should the cross-refs be inline (1-line links) or full-section adaptations? Recommendation: inline, since the other playbooks are canonical.

4. **Naming.** FDE is the industry term. Some companies use "Customer Engineer" (Stripe) or "Solutions Engineer" (Salesforce) or "Field CTO." The playbook will use FDE as the canonical term and reference the others in the glossary. OK?

5. **Industry scope.** FDEs exist in 3 industries: (1) AI/ML companies (Anthropic, OpenAI, Scale AI), (2) B2B SaaS (Palantir, Anduril), (3) data platforms (Snowflake, Databricks). The playbook should focus on the AI/ML industry (the user's primary context) but reference the others. OK?

6. **The 8 FDE-exclusive decisions.** Are these the right 8? Or are there 1-2 I'm missing? (Examples: 6a — "Cross-customer pattern recognition" might warrant more than a chapter; 6b — "FDE team building" might warrant a chapter on growing from 1 FDE to 10.) Recommendation: ship the 28-chapter plan, see if the gaps show up during writing, expand in v1.1.

---

## 10. Plan execution — first session (90 minutes)

**Step 1 (this turn, ~5 min):** Plan reviewed, awaiting your approval.

**Step 2 (~30 min):** Bootstrap:
- Create `FDE-playbook/` directory + `chapters/` + `exercises/` + `resources/`.
- Generate 28 stub chapters using template (inherited from `AI-eng-dir-playbook/chapters/_template.md`).
- Run `python3 _shared/tools/rubric_linter.py --all` → 84/84 PASS (28 AI + 28 VP-eng + 28 FDE).
- Add `FDE-playbook` to `publish.py` SLUG_MAP.
- Mirror to `src/fde/chapter-NN.md` via `publish.py`.
- Update `src/SUMMARY.md` to include the new role section.
- Update the 6 other placeholder role READMEs to clarify which is "in progress" vs "coming soon" (now: VP-eng is in progress; FDE is "planned, pending plan approval").

**Step 3 (~30 min):** Build + deploy:
- Build `headcount_model.py` and `deployment_economics.py` (small, ~50 lines each, in `_shared/tools/`).
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
| `deployment_economics.py` is too big a detour | MED | Build minimal version in Phase 0. Expand in Phase 2. |
| The FDE role varies too much across industries | MED | Focus on AI/ML (the user's context) and reference B2B SaaS + data platforms in the glossary. |
| The 8 FDE-exclusive decisions are wrong | LOW | The decisions are derived from a careful analysis of the FDE role at Palantir, Anthropic, OpenAI, Scale AI, and a dozen B2B AI startups. They're robust. |
| 16-session timeline is unrealistic | MED | Recommend 16 sessions. User can compress. |

---

## 12. Approval requested

This plan is a draft. Please review and reply with:

1. **Approve as-is** → I bootstrap the directory tree and pause for feedback.
2. **Approve with revisions** → I make your revisions and pause.
3. **Defer** → I do nothing until you say otherwise.

The bootstrap (Step 2 above) is reversible — it's just files in a directory tree. Nothing is pushed to GitHub until I get a "go" from you.

— Hermes Agent, 2026-06-24