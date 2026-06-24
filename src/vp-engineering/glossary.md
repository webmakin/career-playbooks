# VP of Engineering Playbook

## Glossary

> **The terminology reference for the VP of Engineering role.** 60+ terms across 11 categories, plus 18 acronyms. Use this when an interview question uses unfamiliar language, or when an industry term has multiple definitions.

### A. Role & Title

- **VPE (VP of Engineering).** The senior-most engineering leader in a single-org company. Reports to CEO or CTO. Owns the engineering org (typically 50-1,000 engineers). Owns engineering strategy, delivery, org design, hiring, perf, risk, audit, and C-suite influence.
- **CTO (Chief Technology Officer).** The senior-most technical leader. Owns tech strategy (architecture, AI/ML, infra). May or may not manage the engineering org (depends on org structure).
- **VP Eng vs. CTO.** VPE = engineering execution (delivery, org, perf, risk). CTO = technical strategy (architecture, AI/ML, infra). Some companies have both (Structure 2 in Ch 21). Some have only VPE (Structure 1). Some have only CTO (Structure 3).
- **Director.** Senior leader reporting to VPE. Owns a domain (Platform, Product, AI, Data, EngOps). Typically 4-7 EMs reporting in, 30-50 ICs.
- **EM (Engineering Manager).** People-management track. Owns a team (5-8 ICs). Performance management, career coaching, project execution.
- **IC (Individual Contributor).** Technical track. 5 levels: IC1 (Junior) → IC5 (Principal). Owns tasks, features, projects, domains, or org-wide impact.
- **Director-to-VP Shift.** A category change, not a title change. The Director owns a domain. The VPE owns a portfolio. Different skills, different relationships, different time horizons.

### B. Org Design

- **IC:Manager Ratio.** The ratio of ICs to managers (Directors + EMs). Target: 6:1 to 10:1. Below 6:1 = bloated management. Above 10:1 = under-supported ICs.
- **Span of Control.** Director:reports (target 6-10) or EM:reports (target 5-8). Below 4 = underutilized. Above 10 = burnout.
- **Layer Count.** IC → EM → Director → VP → CTO. Target: 4 layers between IC and the C-suite. Above 5 = slow decisions.
- **Functional Structure.** Centers of excellence (e.g., all backend engineers report to the Backend Director). Best for <200 engineers.
- **Divisional Structure.** Per product line (e.g., Consumer + Enterprise each have their own engineering org). Best for >500 engineers with multiple products.
- **Matrix Structure.** Dual reporting (e.g., engineer reports to functional manager + product manager). Best for cross-functional work.
- **Platform-Led Structure.** Internal Developer Platform (IDP) at the top, product teams below. Best for >500 engineers with strong platform investment.
- **Product-Led Structure.** Product teams own everything, platform teams are service providers. Best for >500 engineers with product focus.
- **Cross-Team Coordination.** Mechanisms for coordinating across product teams. 3 types: guilds (cross-team communities), platforms (shared services), standards (shared rules via ARB).

### C. Engineering Strategy & Roadmaps

- **Strategy Memo (1-page).** The 3-year strategy in 1 page. 3-5 bets, decline list, measurable outcomes, 12-month milestones. Signed by VPE + CEO.
- **Roadmap (1-page per quarter).** The 12-month roadmap in 1 page per quarter. Top 5 features per quarter, decline list, risks. Signed by VPE + CPO + CEO.
- **Quarterly OKRs (1-page).** The 3-month OKRs in 1 page. 3-5 VPE OKRs, 3-5 per Director. Ladder up to roadmap items.
- **Ladder-Up Rule.** Every OKR ladders up to a roadmap item. Every roadmap item ladders up to a strategy bet. The org can answer "why are we doing this?" at any layer.
- **Decline List.** Things we will NOT do. Every strategy memo, roadmap, and OKR set has a decline list. The discipline is the trade-off.

### D. Build vs Buy

- **5-Dimension Matrix.** Every build-vs-buy decision is scored on 5 dimensions: strategic differentiation, time-to-impact, total cost of ownership, talent cost, vendor maturity. Total ≥ 18 = Build. Total 15-18 = Hybrid. Total < 15 = Buy.
- **Skip-Build Check.** 4 patterns where the default is always Buy: commodity, mature market (3+ vendors), talent unavailable, build-vs-maintain ratio (3+ engineers for 2+ years). Skip-build overrides the 5-dimension score.
- **1-Page Build-Buy Memo.** The decision documented in 1 page. 5-dimension score, skip-build check, 5-year TCO, recommendation. Signed by VPE + CFO + CEO.

### E. Engineering as Revenue

- **Engineering as Cost Center.** Engineering builds the product that the GTM team sells. VPE optimizes cost per engineer.
- **Engineering as Product.** Engineering IS the product (e.g., AI feature is the product). VPE optimizes ARR contribution, customer satisfaction, unit economics.
- **Engineering as Platform.** Engineering builds a platform that 3rd parties build on. VPE optimizes ecosystem health, developer adoption, partner ARR.
- **Unit Economics.** Per-customer revenue, cost, and gross margin. For AI features: revenue per customer per month, cost per customer per month (LLM API + infra + support), gross margin %. Target: 70%+ gross margin.
- **VPE-CFO-CMO Triangle.** When engineering is a product, the VPE co-owns pricing, GTM, and customer narrative with the CFO and CMO.

### F. Performance Management

- **5-Level IC Ladder.** IC1 (Junior, 0-2 years) → IC2 (Mid, 2-5) → IC3 (Senior, 5-8) → IC4 (Staff, 8-12) → IC5 (Principal, 12+). Public, with promotion criteria and comp.
- **5-Dimension Rubric.** Every level is scored on 5 dimensions: technical depth, ownership, collaboration, impact, growth. 0-5 per dimension, 0-25 total, pass at 18+.
- **Cross-Director Calibration.** Quarterly 2-hour meeting where VPE + 5 Directors discuss promotion candidates. Calibrates promotions org-wide, not Director-wide.
- **PIP (Performance Improvement Plan).** 90-day process for below-expectations engineers. 3-5 measurable goals, 30/60/90 check-ins, decision at day 90 (back to good standing OR managed out).
- **Managed-Out.** The end of a 90-day PIP. 2-4 weeks severance, knowledge transfer, hand-off. ~$100K total cost per managed-out.

### G. Hiring & Onboarding

- **3-Layer Hiring System.** Layer 1: 6-month reqs plan (1 page, signed by VPE + CFO). Layer 2: weekly reqs ladder (1 page per Director). Layer 3: interview loop + onboarding system.
- **6-Stage Hiring Funnel.** Req → Sourced → Screened → Onsite → Offer → Accept. Conversion rates: 30% / 50% / 40% / 70% = 4.2% overall.
- **Time-to-Fill.** Days from req open to offer accepted. Target: <60 days.
- **Offer-Accept Rate.** % of offers that result in accepted offers. Target: 75%+.
- **6-Month Retention.** % of new hires still employed at month 6. Target: 90%+.
- **5-Step Onboarding.** Pre-boarding (week before) → Week 1 orientation → Week 2-4 first task → Month 2-3 first project → Month 3-6 full productivity.
- **Cost-of-Hire.** Total Year 1 cost of a senior engineer: ~$480K (loaded + recruiting + onboarding + ramp loss).

### H. C-Suite Influence

- **4-Relationship System.** VPE-CEO (strategy + risk), VPE-CFO (cost + ROI), VPE-CTO (technology + trade-offs), VPE-Board (headline + risk + ask). Each with cadence, format, narrative.
- **Narrative Translation.** The same engineering story has 4 versions: CEO (3 sentences), CFO (1 sentence + 5 numbers), CTO (2 paragraphs), Board (1 sentence + 1 ask).
- **5-Slide Board Deck.** Headline + 3 Wins + 3 Risks + 3 Asks + Next Quarter. 5 slides, not 30.
- **VPE-CTO Charter.** Decision rights, cadence, conflict resolution, joint OKRs. Signed by VPE + CTO.

### I. Risk & Compliance

- **4-Quadrant Risk Model.** Risk = likelihood × impact. 4 quadrants: HIGH-HIGH (mitigate now), LOW-HIGH (plan + insurance), HIGH-LOW (accept + monitor), LOW-LOW (ignore).
- **4 Risk Responses.** Mitigate (reduce likelihood/impact), Accept (live with it), Transfer (insurance, SLA), Avoid (don't do the thing).
- **Risk Register (1 page).** 47 risks → 1 page. Top 5 VPE-owned, top 5 Director-owned, top 5 IC-owned. Owners, responses, status.
- **3-Tier Compliance Model.** Tier 1 (must-have for current business: SOC 2, GDPR, HIPAA), Tier 2 (must-have for next market: ISO 27001, EU AI Act), Tier 3 (nice-to-have for future: PCI-DSS, HITRUST).
- **Compliance-by-Default.** Compliance as a design constraint, not a bolt-on. 5 patterns: data minimization, encryption by default, access logging, right-to-deletion, audit trail.
- **5-Pillar Audit Framework.** Change management, access management, incident response, vulnerability management, business continuity. Each owned, daily evidence, 7-year retention.
- **SOC 2 / ISO 27001 / GDPR / EU AI Act / HIPAA / FedRAMP / PCI-DSS / HITRUST.** The 8 most common compliance frameworks. Tier 1: SOC 2, GDPR, HIPAA. Tier 2: ISO 27001, EU AI Act, FedRAMP. Tier 3: PCI-DSS, HITRUST.

### J. Crisis Response

- **4-Phase Crisis Playbook.** Phase 1: 0-30 min (war room + containment). Phase 2: 30 min-24 hours (public statement + customer notification). Phase 3: 24-72 hours (GDPR notification + remediation). Phase 4: 72 hours-7 days (full containment + postmortem + 5 action items).
- **7-Person War Room.** CEO + VPE + CISO + Legal + Comms/PR + CX + CFO. Pre-assembled. Activated on P0.
- **4-Tier Severity.** P0 (data breach, full outage, war room), P1 (partial outage, security incident, subset war room), P2 (degraded service, on-call only), P3 (minor bug, no impact).
- **Blameless Postmortem.** 5-fact postmortem: what happened, when did we know, what did we do, what was the impact, what was the root cause. System-focused, not person-focused.
- **5 Action Items.** Every postmortem produces 5 action items with owner + date. Tracked quarterly.

### K. System Design (VPE Reference)

- **6-Dimension Coverage.** Every system design scores 0-3 on 6 dimensions: functionality, reliability, scalability, security, cost, time-to-build. Total 0-18, pass at 14/18.
- **Cost-Reliability-Time Triangle.** Every system design picks 2 of 3: cost, reliability, time-to-build. The 3rd is sacrificed. The trade-off is communicated.
- **12 Systems the VPE Owns.** Auth, data pipeline, API platform, observability, CI/CD, AI/ML platform, IDP, event streaming, search, notification, identity, billing.
- **7-Part System Design Review.** Problem, non-goals, architecture, 6-dim coverage, cost-reliability-time trade-off, open questions, decision.

### L. 30/60/90

- **Phase 1: 0-30 days (Assess).** 10 stakeholder conversations, 5 docs read, 1-page assessment memo.
- **Phase 2: 30-60 days (Plan).** 1-page VPE plan, 5 early wins, 3-month OKRs.
- **Phase 3: 60-90 days (Execute).** 3 of 5 wins delivered, 1-page 90-day report, board narrative.
- **5 Early Wins.** Fix reliability, sign VPE-CPO charter, hire 1 critical Director, fix top customer complaint, sign VPE-CEO 1:1 cadence.

### M. Portfolio

- **3-Layer Portfolio.** Layer 1: 28 artifacts (one per chapter). Layer 2: artifact → interview question map (1 page). Layer 3: 5-slide interview deck.
- **5-Criterion Quality Bar.** Concrete numbers, specific decisions, trade-offs named, owners named, 1 pushback. 0-2 per criterion, 0-10 total, pass at 8/10.
- **5-Slide Interview Deck.** Headline + Org design + Hiring + Perf + Risk. 3 numbers per slide.

### N. Acronyms

- **VPE:** VP of Engineering
- **CTO:** Chief Technology Officer
- **CPO:** Chief Product Officer
- **CFO:** Chief Financial Officer
- **CMO:** Chief Marketing Officer
- **CISO:** Chief Information Security Officer
- **EM:** Engineering Manager
- **IC:** Individual Contributor
- **IDP:** Internal Developer Platform
- **DORA:** DevOps Research and Assessment (4 metrics: deploy frequency, lead time, MTTR, change fail rate)
- **SPACE:** Satisfaction, Performance, Activity, Communication, Efficiency (developer productivity framework)
- **SLO:** Service Level Objective (e.g., 99.9% availability)
- **MTTR:** Mean Time To Recover (incident recovery)
- **ARB:** Architecture Review Board
- **CSAT:** Customer Satisfaction
- **NPS:** Net Promoter Score
- **ARR:** Annual Recurring Revenue
- **IC:Manager Ratio:** Individual Contributors to Managers ratio
- **GDPR:** General Data Protection Regulation (EU)
- **SOC 2:** Service Organization Control 2 (security audit)
- **ISO 27001:** Information Security Management System standard
- **EU AI Act:** EU regulation on AI systems
- **HIPAA:** Health Insurance Portability and Accountability Act (US)
- **FedRAMP:** Federal Risk and Authorization Management Program (US gov)
- **PCI-DSS:** Payment Card Industry Data Security Standard
- **HITRUST:** Health Information Trust Alliance security framework
- **PIP:** Performance Improvement Plan
- **IC5:** Principal Engineer (level 5 of the IC track)
- **CSPO:** Certified Scrum Product Owner
- **DRI:** Directly Responsible Individual
- **DR:** Disaster Recovery
- **RTO:** Recovery Time Objective
- **RPO:** Recovery Point Objective
- **TCO:** Total Cost of Ownership
- **RACI:** Responsible, Accountable, Consulted, Informed