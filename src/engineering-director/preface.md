# Engineering Director Playbook

## Preface: How to Read This Book

> **The Engineering Director role is the operating layer between senior IC and VP.** This book is for the senior IC + EM who wants to make the leap to ED, the new ED in their first 90 days, the ED scaling from 30 to 60 engineers, or the ED interviewing for a Senior ED role.

The book treats the ED as a **system-builder**, not a manager. An ED who has 28 chapters of curated artifacts — each tied to a measurable outcome — can run engineering at the function level. An ED who has Slack messages and verbal decisions cannot.

### How the book is organized

The book has **4 parts and 28 chapters**, plus this preface, glossary, and errata:

- **Part I — Foundations (Ch 1-9).** What an ED is, the role, the IC-to-ED category change, hiring, performance, career, comp, culture.
- **Part II — Execution (Ch 10-17).** Planning, sprint execution, quality, incidents, ED-PM partnership, strategy, build vs buy, engineering-as-revenue.
- **Part III — Scale (Ch 18-21).** Org design at scale, hiring at scale, performance at scale, influence.
- **Part IV — Governance & Portfolio (Ch 22-28).** Risk, compliance, crisis, auditability, the 30/60/90, the portfolio map, system design appendix.

### How to read it

1. **If you're aspiring to be an ED:** Read Part I (Foundations) + Part IV Chapter 26 (30/60/90) + Chapter 27 (Portfolio Map). This gives you the ED lens.
2. **If you're a new ED in your first 90 days:** Read Part I + Part IV Chapter 26 in week 1. Then Part II chapters as you encounter the topics.
3. **If you're an ED scaling 30 → 60 engineers:** Read Part III (Scale) first.
4. **If you're an ED interviewing for a Senior ED role:** Read Chapter 27 (Portfolio Map) + Part IV Chapter 26 (30/60/90). Curate your portfolio.

### The 11-section chapter anatomy

Every chapter follows the same 11-section structure. This is the discipline.

1. **Epigraph** — the one-sentence thesis.
2. **Problem** — the situation + decision in one sentence.
3. **Why EDs Fail Here** — 5 named failure modes.
4. **Mental Models** — 4 mental models with diagrams.
5. **Frameworks** — 3 reusable frameworks (templates, matrices, scorecards).
6. **Drill** — a 90-minute hands-on exercise.
7. **Worked Example** — a real-world application of each framework.
8. **Failure Mode Postmortem** — what the failure looks like and how to fix it.
9. **Self-Assessment Rubric** — 5-dimension, 25-point rubric.
10. **Portfolio Artifact Note** — what to save as interview evidence.
11. **Interview Questions** — 5 questions you should be able to answer.

### The tools

The book references 6 tools in `_shared/tools/`:

- `rubric_linter.py` — chapter quality linter.
- `score_drill.py` — drill score aggregator.
- `cost_estimator.py` — LLM API cost model.
- `headcount_model.py` — engineering org cost model.
- `deployment_economics.py` — engineering deployment cost model.
- `publish.py` — chapter-to-src mirror.

### The 4-part structure of every chapter

The book uses 4 mental models, 3 frameworks, and 5-criterion quality bars in every chapter. This is not arbitrary. The 4-3-5 system is the discipline. The ED who uses 4-3-5 has a curated playbook. The ED who uses opinion has a Slack dump.

### What's not in this book

- **AI/ML-specific engineering.** This book is for any ED, not AI-specific. The AI Engineering Director playbook covers AI/ML leadership.
- **VP-level strategy.** This book is for ED-level, not VP-level. The VP of Engineering playbook covers VP leadership.
- **FDE-specific patterns.** This book is for in-house EDs, not deployed engineers. The FDE playbook covers FDE.

### How to use this book with your team

1. **Read a chapter.** Take 90 minutes.
2. **Run the drill.** Fill in the frameworks with your context.
3. **Save the artifact.** Add it to your portfolio.
4. **Share with your team.** Use the worked example as a starting point.
5. **Iterate.** Update the artifact every quarter.

The book is not a one-time read. It's a 28-chapter operating system for the ED role.

### A note on opinion

This book is opinionated. Where the literature disagrees, this book picks a side. Where the literature is silent, this book invents. Where the literature is settled, this book summarizes. Read it as one ED's playbook, not as the ED's playbook. Adapt what doesn't fit your context. Discard what doesn't serve your team.

### A note on completeness

This book is incomplete. The ED role changes as the company scales, the technology shifts, and the team grows. The 28 chapters cover the most common ED scenarios. They do not cover every scenario. If you encounter a scenario this book doesn't address, design your own framework. The discipline is to build a system, not to follow one.

### Let's go.

The ED role is one of the most leveraged roles in any company. An ED who runs 60 engineers at 99.9% uptime with 92% retention and 6 launches per year is a force multiplier. An ED who runs 60 engineers at 99.5% uptime with 80% retention and 2 launches per year is a bottleneck.

The 28 chapters in this book are the leverage. The system is the discipline. The outcome is the engineering org.
