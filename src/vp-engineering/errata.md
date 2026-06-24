# VP of Engineering Playbook

## Errata & Known Issues

> **Honest accounting of what's incomplete, what might be wrong, and what the author would change in v2.** This page lists the things in v1.0.0 that the author knows are imperfect.

### What's incomplete

1. **No runnable code examples.** The VPE role is not a coding role. The "code" in the playbook is frameworks, templates, and 1-page memos. For runnable code examples of the underlying systems (e.g., auth, data pipeline, observability), see the [Staff Engineer Playbook](https://github.com/webmakin/career-playbooks) (planned).

2. **Some cost numbers are illustrative.** The dollar amounts in the chapters (e.g., "IC:Manager ratio costs $XXM") are based on industry-standard comp ranges and acme-corp's fictional 1,200-person size. Real-world costs vary by region, level, and company. For real numbers, use the `_shared/tools/headcount_model.py` tool with your own inputs.

3. **No specific company case studies.** The chapter worked examples use "acme-corp," a fictional 1,200-person B2B SaaS company. The "Failure Mode Postmortem" sections use anonymized composites, not real companies. For real-world case studies, the reader should pair this book with their own experience.

4. **Regulatory framework citations are US + EU-centric.** The regulatory chapter (Ch 23) covers SOC 2, ISO 27001, GDPR, EU AI Act, HIPAA, FedRAMP, PCI-DSS, HITRUST. APAC-specific regulations (Singapore PDPA, Japan APPI, Australia Privacy Act) are mentioned in passing but not detailed. For APAC-specific guidance, supplement with local counsel.

5. **Crisis response chapter (Ch 24) assumes a war room in 30 minutes.** This works for a 1,000+ person company. For smaller companies (<100), the war room is 3-5 people, not 7. The framework scales down but isn't fully detailed for sub-100-person companies.

### What might be wrong

1. **The 5-dimension perf rubric may not fit every company.** Some companies use a 4-dimension rubric (dropping one of the 5). Some use a 6-dimension rubric. The 5-dimension rubric is the most common pattern in mid-size tech companies but not universal.

2. **The IC:Manager ratio of 6:1 to 10:1 is industry-specific.** Some industries (e.g., finance) run at 4:1. Some (e.g., infrastructure) run at 12:1. The 6-10 range is a target for B2B SaaS, not a universal rule.

3. **The 30/60/90 framework assumes the VPE has full CEO support.** If the CEO is not aligned with the VPE, the 30/60/90 won't work. The 5 early wins depend on CEO support. Without it, the VPE will fail in year 1.

4. **The C-suite relationship system assumes a 4-person C-suite (CEO, CFO, CTO, CPO).** Smaller companies may have only 2-3 C-suite members. The 4-relationship system collapses to 2-3 in that case.

5. **The 4-quadrant risk model is not a substitute for a formal risk management framework (e.g., NIST, ISO 31000).** The 4-quadrant model is a simplification for VPE-level decision-making. For audit-grade risk management, supplement with formal frameworks.

### What the author would change in v2

1. **Add specific company case studies.** 5-10 real (anonymized) case studies of VPE-level decisions. Each with: company size, the decision, the alternatives, the outcome.

2. **Add a chapter on VPE-CEO relationship design.** The 4-relationship system (Ch 21) treats CEO as one of 4. The CEO relationship is the most important. A dedicated chapter would cover: how to design the weekly 1:1, how to align on strategy, how to escalate conflict, how to read the CEO's communication style.

3. **Add a chapter on the VPE's "second 90 days" (day 91-180).** The first 90 days are well-covered. The second 90 days (the VPE's first 6 months) are about: shipping the 5 early wins, building the next 6-month plan, hiring the first 2 Directors, designing the first quarterly review. A dedicated chapter would cover these.

4. **Add a chapter on VPE compensation.** How VPEs are paid (base + bonus + equity), how to negotiate the VPE offer, how to design the comp review. This is missing.

5. **Add a chapter on VPE-PM partnership.** The VPE-CPO chapter (Ch 14) covers the VPE-CPO relationship. The VPE-PM relationship (the VPE and the senior PMs reporting to the CPO) is a separate, important relationship. A dedicated chapter would cover: how to design the VPE-PM partnership, the 3 PM archetypes, the VPE's role in PM career growth.

6. **Add a chapter on VPE-founder / VPE-CEO succession.** Some VPEs become CEOs. Some VPEs are replaced by a CTO who reports to the CEO. The VPE's career path is more varied than the playbook suggests. A dedicated chapter would cover: when to stay VPE, when to pivot to CTO, when to pivot to CEO.

7. **Update the 12 systems list.** The 12 systems in Ch 28 are accurate for 2026. By 2028, AI-native systems (e.g., LLM serving, vector databases, agent platforms) will likely be 5+ of the 12 systems. The list needs periodic updates.

8. **Add a chapter on engineering org transformation.** Some VPEs inherit an org that needs fundamental change (e.g., from feature factory to platform-led). The playbook covers incremental change (Ch 18) but not transformation.

### Feedback

If you find a bug, an error, or a missing topic, please file an issue at https://github.com/webmakin/career-playbooks/issues.

— *The author*