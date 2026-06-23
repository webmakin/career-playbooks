# Worked Example: The Engineering Org at Scale

> **Source:** VP of Engineering Playbook, Chapter 4
> **Scored: 22/25** (1 dimension at 3, all others 4+; passes the 18/25 threshold)

## Scenario

Same as the drill: 1,200-person B2B SaaS, "engineering is the bottleneck."

## 1-page diagnosis

1. **Org-shape mismatch**: 5 Directors, 200 engineers, but Director:IC ratio is 1:18. Industry standard at this scale is 1:8-12. Result: Directors are doing IC work + manager work, not Director work.

2. **No platform team**: 8 product teams each maintain their own CI/CD, observability, auth, deploy. Duplicated work, inconsistent quality, 30% of each team's capacity is "platform work" not product work.

3. **Hiring lag**: 30 open reqs, 18 months to fill, 25% attrition in last 12 months. Result: 30% of capacity is constantly ramping.

## 24-month strategy (3 horizons)

**Horizon 1 (Now - 6 months): Stabilize + Diagnose**
- Hire 3 senior Directors (backfill 2, new 1)
- Stand up a 4-person Platform team
- Stop the hiring lag (faster funnel, better comp, retention plan)

**Horizon 2 (6-18 months): Build the multiplier**
- 80% of teams on shared platform (CI/CD, observability, auth)
- Director:IC ratio to 1:10
- Attrition to <12%
- Cycle time halved

**Horizon 3 (18-36 months): Change the company**
- AI Engineering Director hire (see AI-eng-dir playbook)
- New product surface (e.g., AI features)
- Org shape: 350 engineers, 7 Directors, 1 CTO above VPE

## 30/60/90

- **Days 1-30**: Meet every Director, 3 board members, 5 senior EMs. Read every strategy doc, postmortem, RFC from last 12 months. NO changes.
- **Days 31-60**: Diagnosis memo (1 page) to CEO. 24-month plan (1 page) to CEO + board. Sign-off on Platform team charter. First Director hire (backfill #1).
- **Days 61-90**: Platform team stands up (4 people from existing teams). First shared CI/CD adoption (2 teams). Hiring funnel redesigned. First board update.

## 5-metric dashboard

1. Throughput: Features per quarter per team — target +30% in 6 months
2. Quality (MTTR): Mean time to recover — target -40% in 6 months
3. Velocity (cycle time): Commit to deploy — target -50% in 12 months
4. Health (attrition): Annual attrition rate — target -25% in 12 months
5. Cost ($/eng): $ per engineer per quarter — target -10% in 18 months

## 3 things I will NOT do

1. Ship a complete org reshuffle in the first 90 days. (Org changes take 6-12 months to settle; doing them fast destroys trust.)
2. Make major architecture decisions before the architecture review board is staffed. (Most VPE architecture decisions should go through the ARB once it exists.)
3. Hire my friends or people from my last company. (The first 5 hires define the VPE's reputation. They should be the best in their discipline, not the most familiar.)

## Grading notes

- 5/5 on the org-multiplier lens (the diagnosis correctly identifies the multiplier gap).
- 5/5 on the three horizons (each horizon has clear priorities with target dates).
- 4/5 on the C-suite triangle (the plan addresses the CEO and CFO implicitly but doesn't explicitly map the CPO relationship).
- 4/5 on the decision stack (clear which decisions are VPE-level vs Director-level).
- 4/5 on the health dashboard (5 metrics, no more; each with a target).
- **Total: 22/25** — pass.
