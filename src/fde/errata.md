# Forward Deployed Engineer Playbook

## Errata & Known Issues

> **Honest accounting of what's incomplete, what might be wrong, and what the author would change in v2.** This page lists the things in v1.0.0 that the author knows are imperfect, incomplete, or potentially wrong.

---

## 1. Things I Know Are Imperfect

### Chapter 1: What a Forward Deployed Engineer Actually Does

- The "FDE vs SWE vs PSE vs CSM" comparison table is simplified. In practice, the boundaries blur — some FDEs do PSE-style work; some PSWs do FDE-style work. The 4-role distinction is the ideal type, not the reality.

- The "FDE in 6 weeks" timeline is aggressive. Most real FDE deployments take 8-12 weeks. The 6-week number assumes a mature FDE with established patterns; a new FDE will take longer.

### Chapter 5: The FDE Deployment Stack

- The 5-layer stack (Data, ML, API, Application, Operations) is one valid decomposition. Other decompositions are valid (e.g., 3-tier: presentation, business logic, data; or 4-layer: edge, application, data, infrastructure). The 5-layer is opinionated.

- The "8-week per layer" timeline assumes a small FDE team (1-2 FDEs) and a mature deployment pattern. Larger deployments take longer.

### Chapter 14: FDE-PM Partnership

- The "4 ownership boundaries" model assumes a mature PM-FDE relationship. In practice, the boundaries are negotiated; some PMs want more ownership of feedback, some less.

- The "weekly Tuesday 30 min" cadence is opinionated. Some teams do weekly Wednesday, some do twice-weekly 15 min. The cadence matters less than the consistency.

### Chapter 18: FDE Career Ladder

- The "4-level FDE ladder" is one valid model. Some companies use 5 levels (FDE 1, 2, 3, 4, 5). Some use 3 levels (Junior, Senior, Principal). The 4-level is opinionated.

- The "60% stall at FDE 2" statistic is anecdotal, drawn from observation across 10+ companies. It is not a rigorously studied number.

### Chapter 22: Customer Data Governance

- The "4-pillar governance" model is one valid framework. NIST and ISO 27001 use different decompositions. The 4-pillar is opinionated.

- The "7-day breach response" assumes the customer has a documented incident response plan. Many customers don't. The FDE may need to create the plan from scratch.

### Chapter 27: FDE Portfolio Map

- The "28 artifacts" count assumes the FDE produces 1 artifact per chapter. In practice, some chapters produce multiple artifacts (e.g., the worked example + the failure mode postmortem). The 28 count is the floor, not the ceiling.

- The "5-criterion quality bar" is opinionated. Some portfolios use a different bar (e.g., 3-criterion, 7-criterion). The 5-criterion is the author's preference.

### Chapter 28: System Design Appendix

- The "5-component design pattern" is one valid pattern. Lambda architecture, Kappa architecture, and other patterns are valid for specific use cases. The 5-component is opinionated.

- The "8-item production scorecard" is opinionated. Some teams use 5-item or 10-item scorecards. The 8-item is the author's preference.

---

## 2. Things I Might Be Wrong About

### The FDE Role is a 4-Level Ladder

Some FDE organizations use 5 levels (with a "Staff FDE" between FDE 3 and FDE 4). Some use 3 levels (Junior, Senior, Principal). The 4-level is the most common but not universal.

### The Top-3 + Deferred Rule for Themes

The rule that the FDE picks TOP 3 themes and 2-3 deferred themes per quarter is opinionated. Some FDEs produce top-5 + deferred-5 lists. The top-3 forces sharper prioritization but may miss important themes.

### The 1-Page PRFA

The 1-page PRFA is opinionated. Some PMs prefer 2-page PRFAs with more detail. The 1-page forces concision but may lose nuance.

### The 6-Phase Customer Deployment Methodology

The 6-phase methodology (Pre-deployment → Kickoff → Build → Pilot → Production → Stabilize) is one valid decomposition. Some FDEs use 4-phase (Pre-deployment → Build → Production → Stabilize) or 8-phase (with sub-phases). The 6-phase is the most common.

### The 2-Quarter Lag for Roadmap

The "feedback ships in 2 quarters" rule assumes a fast-moving startup. In larger companies, the lag is 4-6 quarters. The 2-quarter rule applies to AI-first B2B startups.

### The 4 Security Pillars

The "Network + Identity + Data + Application" decomposition is one valid framework. Some security frameworks use 5 or 6 pillars. The 4-pillar is opinionated.

### The 5-Customer-Call-Sequence in the First 30 Days

The "5 customer calls in 5 days" assumes the FDE has 5 customers and can book 1 call per day. In practice, customers have limited availability. The 5-day sequence is the ideal; the FDE may need 10-15 days.

---

## 3. Things That Are Incomplete in v1.0.0

### Real Customer Case Studies

The book uses hypothetical scenarios (acme-corp, Customer A, etc.) for worked examples. Real customer case studies would be more valuable but require customer permission. v2 should include 3-5 anonymized real case studies.

### Industry-Specific Adaptations

The book treats FDE work as universal across industries. In practice, healthcare FDEs have different compliance requirements than financial FDEs, which have different requirements than B2B SaaS FDEs. v2 should include industry-specific adaptations for healthcare, finance, B2B SaaS, and consumer.

### Quantitative Benchmarks

The book uses qualitative frameworks (4-pillar, 5-component, etc.) rather than quantitative benchmarks (e.g., "FDEs should ship 5-7 deployments per year"). v2 should include quantitative benchmarks from real FDE data.

### Cross-Playbook Comparisons

This book is part of an 8-playbook series. The cross-playbook comparisons (FDE vs PM vs SWE vs ML Researcher) are missing from this book. v2 should include a comparison chapter.

### Multi-Language Support

The book is written in English. v2 should consider translations (Chinese, Japanese, Spanish, French, German) for international FDEs.

---

## 4. Things I Would Change in v2

### Add a "FDE On-Call" Chapter

FDE on-call is its own discipline (different from SWE on-call). v2 should add a chapter on FDE on-call: rotation, escalation, customer communication, runbook management.

### Add a "FDE Comp & Promo" Chapter

The book covers the FDE ladder (Chapter 18) and FDE performance (Chapter 20) but not comp (base, bonus, equity) or the specific promotion packet format. v2 should add this.

### Add a "FDE Tools" Chapter

FDEs use specific tools (Slack, Jira, Notion, Figma, Linear, etc.). v2 should add a chapter on the FDE toolset.

### Add a "FDE in AI-First Companies" Chapter

The book covers ML/AI deployment (Chapter 7) but not the specific challenges of FDEs in AI-first companies (model drift, hallucination management, prompt engineering). v2 should add this.

### Reframe the 28-Chapter Structure

The 7-part / 28-chapter structure is the author's preference. v2 should consider whether 6 parts (merging Parts VI and VII) or 8 parts (splitting Part II) would be more readable.

---

## 5. Acknowledgments to Future Readers

If you find errors, omissions, or improvements, please open an issue at the GitHub repository (linked from the GitHub Pages site). The author reads every issue and incorporates feedback into v2.

If you have a real-world FDE scenario that would make a great worked example or failure mode postmortem, please open an issue with the "case-study" label. v2 should include 3-5 real case studies.

If you want to translate this book into another language, please open an issue with the "translation" label. The author can provide Markdown source files for translation.

---

**v1.0.0 was released September 2026.** v2 is planned for 2027.

— The Author
September 2026
