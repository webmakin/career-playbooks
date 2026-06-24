# Forward Deployed Engineer Playbook

> **The Practice-First Guide to Becoming a Forward Deployed Engineer (FDE)**

![Status: Stubs](https://img.shields.io/badge/status-stubs-yellow)
![Chapters: 0/28](https://img.shields.io/badge/chapters-0%2F28-lightgrey)
![Parts: 7](https://img.shields.io/badge/parts-7-blue)

A practice-first guide for Forward Deployed Engineers — the senior-IC role that sits at the intersection of engineering, product, and customer success. The FDE embeds with strategic customers, owns the end-to-end deployment, and turns customer feedback into product requirements.

## Who this is for

**Primary reader:**
- 0-6 months into an FDE role, or
- 30-90 days from an FDE interview, or
- A Staff/Principal SWE considering a pivot to FDE.

**Secondary readers:**
- Engineering Directors who manage FDE teams.
- Founders/CEOs hiring their first 5 FDEs.
- PMs who work with FDEs on the customer feedback loop.

## What this is not

This is **not**:
- A customer success playbook (relationship management, not engineering).
- A professional services playbook (deployment methodology, not product feedback).
- A staff engineer playbook (technical depth, not customer integration).
- A sales engineer playbook (demos, not deployments).

The FDE role is a hybrid of all four. This playbook covers the hybrid — the customer-embedded senior IC who writes code daily AND owns the customer outcome AND drives product feedback.

## The 7 parts

| Part | Chapters | Theme |
|------|----------|-------|
| I — Foundations | 1–4 | The FDE category. The IC-to-FDE shift. The customer edge. The product edge. |
| II — FDE Technical Spine | 5–9 | Deployment stack, data eng, ML/AI, integration patterns, perf/cost. |
| III — Customer & Deployment | 10–13 | 6-phase methodology, customer relationship, crisis, hand-off. |
| IV — Product & Strategy | 14–17 | FDE-PM partnership, feedback loop, strategy influence, FDE-as-product-leader. |
| V — Career & Leadership | 18–21 | FDE ladder (4 levels), FDE hiring, FDE perf, influence without authority. |
| VI — Governance & Risk | 22–25 | Customer data, security, crisis response, audit trail. |
| VII — The FDE's Portfolio | 26–28 | 30/60/90, portfolio map, system design for FDEs. |

## The 8 FDE-exclusive decisions

A regular SWE does not face these decisions. The FDE does, weekly.

1. **Time allocation** (3-5 customers, 1-2 deployments each, 60% on customer, 40% on product feedback).
2. **Customer priorities** (which customer gets the FDE this week when 3 customers are blocked).
3. **Deployment trade-offs** (the FDE's "good enough" vs the engineer's "perfect").
4. **Product feedback priority** (which feedback gets pushed to the PM and which gets deferred).
5. **Customer escalation** (when to escalate to the Director vs handle it yourself).
6. **Customer-side technical decisions** (architecture choices the FDE makes on the customer's behalf, in the customer's environment).
7. **Hand-off timing** (when to hand off the deployment to the customer success team).
8. **FDE career path** (when to stay in FDE, when to pivot to PM, when to pivot to Eng Manager).

## Tooling

FDE-specific tools (in addition to the shared `rubric_linter.py`, `score_drill.py`, `cost_estimator.py`, `publish.py`):

- `headcount_model.py` — Engineering org cost, retention, hiring funnel modeling.
- `deployment_economics.py` — FDE deployment cost, time-to-deployment, customer ROI.

## Status

Stubs (28 chapters) generated. Phase 1 (Part I, Ch 1-4) next, awaiting user go. See root [STATUS.md](https://github.com/webmakin/career-playbooks/blob/main/STATUS.md) and the [FDE plan](https://github.com/webmakin/career-playbooks/blob/main/.hermes/plans/2026-06-24_0911-fde-playbook-plan.md).