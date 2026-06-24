# Forward Deployed Engineer Playbook

## Glossary

> **The terminology reference for the Forward Deployed Engineer role.** 60+ terms across 12 categories, plus 16 acronyms. Use this when an interview question uses unfamiliar terminology, or when you're onboarding to a new FDE role.

---

## 1. The FDE Role (Chapter 1)

**FDE (Forward Deployed Engineer).** A senior IC hybrid role that combines senior SWE skills with customer-edge deployment and product-edge feedback. The FDE lives at two edges: customer edge + product edge.

**Customer edge.** Where the company's product meets the customer's problem. The FDE ships deployments, runs customer success, and owns crisis response at the customer edge.

**Product edge.** Where the customer's feedback meets the company's roadmap. The FDE drives the FDE-PM partnership, owns 1-page PRFAs, and influences product strategy.

**IC (Individual Contributor).** A role that does not manage people. FDEs are IC-track roles; they don't have direct reports. Senior FDEs (FDE 3, FDE 4) may have indirect reports (mentoring, leadership).

**FDE charter.** A 1-page document that defines the FDE's scope, customers, success metrics, and stakeholder relationships. Signed with the Director on Day 1.

**PSE (Professional Services Engineer) / CSM (Customer Success Manager).** Adjacent roles. PSEs are paid by the customer to do custom work. CSMs own customer relationships and renewals. FDEs are different: FDEs are paid by the company, embedded with customers, and own the deployment end-to-end.

---

## 2. The 4-Level FDE Ladder (Chapter 18)

**FDE 1 (Mid).** 0-3 years experience. 1-2 customers. 6-12 week deployments. Feedback themes tracked. Promotion criteria: 1+ customer deployed, 5+ themes/month.

**FDE 2 (Senior).** 3-6 years experience. 2-3 customers. 6-week deployments. PRFAs owned. Promotion criteria: 5+ customers deployed, 3+ PRFAs in review.

**FDE 3 (Lead).** 6-10 years experience. 3-5 customers. 4-week deployments. Product roadmap input. Promotion criteria: 10+ customers, 5+ PRFAs merged, 1+ cross-functional initiative.

**FDE 4 (Principal).** 10+ years experience. 5+ customers OR 1 product area. Cross-customer patterns. Strategic product input. Promotion criteria: FDE team leadership, FDE ladder definition, industry influence.

---

## 3. Customer Edge Terms (Chapters 3, 10-13)

**6-phase customer deployment methodology.** The structured FDE deployment process: Pre-deployment → Kickoff → Build → Pilot → Production → Stabilize. Each phase has defined artifacts and exit criteria.

**Crisis playbook.** The 4-phase response (Detect → Contain → Resolve → Learn) for when a customer's deployment goes down or fails. Documented and drilled before the crisis.

**Customer health scorecard.** A 1-page scorecard tracking 5 dimensions: NPS, retention, adoption, ROI, relationship. Updated quarterly per customer.

**Champion.** The person inside the customer organization who advocates for your product. The FDE's primary contact for feedback and escalations.

**Decision-maker.** The person inside the customer organization with budget authority. Different from the champion; the FDE cultivates both.

**End-user lead.** The person inside the customer organization who represents the end users. Important for adoption metrics and rollout strategy.

**NPS (Net Promoter Score).** A measure of customer satisfaction on a -100 to +100 scale. +30 is good. +50 is excellent.

**Retention.** The percentage of customers who renew. 95%+ retention is the FDE target.

---

## 4. Product Edge Terms (Chapters 4, 14-17)

**1-page PRFA (Product Request for Action).** A 1-page document that captures a customer feedback theme, quantifies the impact, proposes a solution, lists alternatives, and recommends an action. Used for FDE-PM communication.

**FDE-PM partnership.** The relationship between the FDE and the Product Manager. Defined by 4 ownership boundaries (FDE = customer feedback + 1-page PRFAs; PM = prioritization + roadmap) and 3 cadences (weekly sync, biweekly retro, quarterly roadmap review).

**3-layer feedback funnel.** 60 themes/year → 5 themes/quarter → 3 PRFAs/quarter. The FDE's discipline for converting raw feedback into actionable roadmap input.

**Top-3 + deferred rule.** The rule that the FDE picks TOP 3 themes for the quarter and 2-3 themes to DEFER (with reasons). No middle ground.

**2-quarter lag.** The expected lag between customer feedback and roadmap ship. The FDE plans for 2-3 quarters.

**Quarterly synthesis.** A 1-page synthesis of 5 themes per quarter. The FDE's primary product edge artifact.

**Customer advisory board (CAB).** A quarterly meeting with top 5-10 customers where the FDE + PM + Director gather strategic input.

---

## 5. Technical Spine Terms (Chapters 5-9)

**5-layer deployment stack.** The 5 layers the FDE ships: Data layer (data pipeline + storage), ML layer (training + serving), API layer (REST/GraphQL + auth), Application layer (UI + business logic), Operations layer (monitoring + alerting + DR).

**Data engineering.** The work of getting customer data into the platform: ingestion, transformation, storage, governance. The FDE's first deployment task.

**ML serving.** The work of deploying ML models: feature store, model registry, inference API, drift monitoring. The FDE's most leveraged technical work.

**API integration.** The work of integrating with customer APIs: REST/GraphQL, webhooks, OAuth, rate limiting. The FDE's connective tissue.

**Observability stack.** The work of monitoring customer deployments: logs, metrics, traces, dashboards, alerting. The FDE's operational discipline.

**Security architecture.** The work of securing customer deployments: auth, encryption, audit trail, compliance. The FDE's compliance foundation.

**Multi-tenant isolation.** The work of isolating customer data and workloads in shared deployments: tenant ID, scoped DB, tenant-aware processing. The FDE's scaling discipline.

---

## 6. Governance & Compliance Terms (Chapters 22-25)

**4-pillar data governance.** Data classification + Access control + Encryption + Audit trail. The FDE's governance framework.

**3-tier data classification.** Public / Internal / Restricted. PII and PHI are restricted by default.

**5-region compliance map.** US (HIPAA, SOC 2, CCPA), EU (GDPR, EU AI Act), UK (UK GDPR, DPA 2018), APAC (PDPA, APPI), Canada (PIPEDA).

**GDPR (General Data Protection Regulation).** EU privacy regulation. 72-hour breach notification. 4% of global revenue fine for violations.

**HIPAA (Health Insurance Portability and Accountability Act).** US healthcare regulation. 60-day breach notification for PHI.

**SOC 2 (Service Organization Control Type 2).** US/global security audit framework. Annual. Type II is more rigorous than Type I.

**EU AI Act.** EU regulation for AI systems. Enforcement begins 2026-2027. Risk-classified (unacceptable, high, limited, minimal).

**DPIA (Data Protection Impact Assessment).** Required for GDPR high-risk processing. 1-page document, refreshed annually.

**72-hour breach notification.** GDPR requirement: notify regulator within 72 hours of breach detection. The FDE's crisis-management deadline.

**Immutable S3.** AWS S3 with Object Lock, which prevents deletion or modification. Used for audit trail.

**7-year retention.** Standard retention period for audit logs in regulated industries (healthcare, finance, EU).

---

## 7. Performance & Career Terms (Chapters 19-21)

**5 FDE-hire traits.** Customer empathy + Technical depth + Product instinct + Communication. The FDE profile.

**Customer simulation.** A 1-hour mock customer call in the FDE interview loop. Tests 4 dimensions: crisis response, stakeholder comms, technical depth, customer empathy.

**5-step FDE onboarding.** Pre-boarding → Week 1 → Month 1 → Month 3 → Month 6. The FDE's onboarding methodology.

**30/60/90 plan.** The new-FDE plan: Days 1-30 Assess, Days 31-60 Plan, Days 61-90 Execute. The FDE's first-90-days structure.

**5-dimension FDE rubric.** Customer outcomes + Deployment velocity + Product feedback + Cross-functional alignment + FDE leadership. The FDE's performance measurement.

**3-tier calibration.** Exceeds / Meets / Below. The FDE's performance classification.

**12-month development plan.** 1 plan per FDE per year. Top 3 development areas. Quarterly actions.

**PIP (Performance Improvement Plan).** A 90-day plan for an FDE who is far below bar. Measurable goals. Decision at day 90.

---

## 8. Influence Without Authority Terms (Chapter 21)

**4 influence channels.** 1-page PRFAs + Customer escalations + Cross-functional alliances + Executive narratives.

**3 influence styles.** Rational (data, evidence, ROI) + Emotional (customer story, mission, urgency) + Political (alliances, trade-offs, face-saving).

**5 influence moments.** 1-page PRFA + Customer escalation + Cross-functional alliance + Executive narrative + Win.

**6-stakeholder influence map.** PM + EM + CSO + Director + CEO + CPO.

---

## 9. Architecture & System Design Terms (Chapter 28)

**5-component design pattern.** Ingest → Store → Process → Serve → Monitor. The FDE's system design template.

**3 deployment topologies.** Single-tenant (1 customer per deployment) + Multi-tenant (N customers per deployment) + Hybrid (mixed).

**8-item production scorecard.** Monitoring + Alerting + Logging + Tracing + DR + Scaling + Security + Documentation. The FDE's production-ready check.

**Single-tenant vs multi-tenant.** Single-tenant = strong isolation, higher cost. Multi-tenant = shared infrastructure, lower cost. Hybrid = mixed.

---

## 10. Portfolio & Promotion Terms (Chapter 27)

**28-artifact portfolio.** The 28 chapters × 1 artifact each = 28 portfolio artifacts. The FDE's promotion evidence.

**5 portfolio layers.** Deployed code + Customer work + Product feedback + Cross-functional leadership + FDE leadership.

**3 promotion levels.** FDE 2 → FDE 3 + FDE 3 → FDE 4 + FDE 4 → PM.

**5-criterion quality bar.** 1-page + 1 worked example + 1 failure mode postmortem + 1 self-assessment rubric + 5+ interview questions.

---

## 11. Acronyms (Reference)

| Acronym | Meaning |
|---------|---------|
| **FDE** | Forward Deployed Engineer |
| **SWE** | Software Engineer |
| **PM** | Product Manager |
| **EM** | Engineering Manager |
| **CSO** | Customer Success Officer / Customer Success Organization |
| **CFO** | Chief Financial Officer |
| **CEO** | Chief Executive Officer |
| **CPO** | Chief Product Officer |
| **CTO** | Chief Technology Officer |
| **CISO** | Chief Information Security Officer |
| **DPO** | Data Protection Officer |
| **IC** | Individual Contributor |
| **PSE** | Professional Services Engineer |
| **CSM** | Customer Success Manager |
| **PRFA** | Product Request for Action |
| **NPS** | Net Promoter Score |
| **ARR** | Annual Recurring Revenue |
| **PII** | Personally Identifiable Information |
| **PHI** | Protected Health Information |
| **DPIA** | Data Protection Impact Assessment |
| **GDPR** | General Data Protection Regulation (EU) |
| **HIPAA** | Health Insurance Portability and Accountability Act (US) |
| **SOC 2** | Service Organization Control Type 2 |
| **CCPA** | California Consumer Privacy Act |
| **EU AI Act** | EU regulation for AI systems |
| **PDPA** | Personal Data Protection Act (Singapore) |
| **APPI** | Act on the Protection of Personal Information (Japan) |
| **PIPEDA** | Personal Information Protection and Electronic Documents Act (Canada) |
| **PIP** | Performance Improvement Plan |
| **CAB** | Customer Advisory Board |
| **DR** | Disaster Recovery |
| **MTTR** | Mean Time To Recover |
| **MTBF** | Mean Time Between Failures |
| **ML** | Machine Learning |
| **AI** | Artificial Intelligence |
| **JIT** | Just-In-Time (access) |
| **MFA** | Multi-Factor Authentication |
| **SSO** | Single Sign-On |
| **RBAC** | Role-Based Access Control |
| **OWASP** | Open Web Application Security Project |
| **SAST** | Static Application Security Testing |
| **DAST** | Dynamic Application Security Testing |
| **RASP** | Runtime Application Self-Protection |
| **WAF** | Web Application Firewall |
| **IDS/IPS** | Intrusion Detection/Prevention System |
| **SBOM** | Software Bill of Materials |
| **IaC** | Infrastructure as Code |
| **API** | Application Programming Interface |
| **REST** | Representational State Transfer |
| **GraphQL** | Graph Query Language |
| **SDK** | Software Development Kit |
| **KPI** | Key Performance Indicator |
| **OKR** | Objectives and Key Results |
| **QBR** | Quarterly Business Review |
| **CFR** | Code Federal Regulations (US) |

---

**Total: 60+ terms across 11 categories + 50+ acronyms.** The FDE vocabulary.

— Glossary compiled September 2026
