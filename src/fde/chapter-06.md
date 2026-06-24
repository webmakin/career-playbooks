# Forward Deployed Engineer Playbook
## Chapter 6

# Data Engineering for FDEs

> *"The FDE's first deployment task is almost always: get the customer's data into our platform. The FDE who owns data engineering — the 4 data patterns, the 3 ingestion modes, the 2 schema strategies — ships 2x faster than the FDE who treats data as a side concern."*

---

## 1. Epigraph

_The FDE's first deployment task is almost always: get the customer's data into our platform. The FDE who owns data engineering — the 4 data patterns, the 3 ingestion modes, the 2 schema strategies — ships 2x faster than the FDE who treats data as a side concern._

---

## 2. Problem

You are an FDE at acme-corp. The customer has 50M rows in Snowflake, 200 columns, and they want their data in your platform by Q4 2026. The data has PII (names, emails). The customer's warehouse is in us-east-1. They need daily incremental loads. The PM says: "Just use our standard connector." The customer says: "Standard connector takes 3 weeks for the first load." You have 8 weeks total.

You have 8 weeks to design the data pipeline, build it, and ship it. This chapter tells you what the 4 data patterns are, how to choose the right one, and how to ship in 8 weeks.

**Decision in one sentence:** _FDE data engineering is a 4-pattern system (full load, incremental, CDC, streaming) chosen per-customer, owned end-to-end by the FDE, with a 2-schema strategy (raw + curated) and a 3-mode ingestion model (batch, micro-batch, streaming); the FDE's job is to design the pipeline for the customer's data shape, ship in 3 weeks (not 8), and own the production data flow._

---

## 3. Why FDEs Fail Here

Five named failure modes of FDEs whose data pipeline produced zero results.

- **The 1-Schema Failure.** The FDE uses a single schema for raw and curated data. _The customer changes the schema, the pipeline breaks._
- **The No-Incremental Failure.** The FDE uses full load only. _50M rows take 12 hours. Daily loads are impossible._
- **The No-Ownership Failure.** The FDE builds the pipeline but doesn't own the production data flow. _The customer's data drifts, the FDE doesn't notice._
- **The No-PII-Handling Failure.** The FDE ships PII without encryption or masking. _The customer fails compliance review._
- **The 8-Week-Pipeline Failure.** The FDE spends 8 weeks building the pipeline. _The customer churns before the pipeline ships._

---

## 4. Mental Models

Four mental models that compress data engineering for FDEs.

**Mental model 1: The 4 Data Patterns.** 4 patterns for customer data ingestion.

```mermaid
%% Figure 6.1 — The 4 data patterns
flowchart TB
    P1[Pattern 1: Full load<br/>All data, every time<br/>Best for: small data (<10M rows)]
    P2[Pattern 2: Incremental<br/>Only new/updated rows<br/>Best for: medium data (10M-1B rows)]
    P3[Pattern 3: CDC<br/>Capture every change<br/>Best for: high-frequency updates]
    P4[Pattern 4: Streaming<br/>Real-time events<br/>Best for: real-time use cases]
    P1 --> P2
    P2 --> P3
    P3 --> P4
```

**The 4 patterns:**
- **Pattern 1: Full load.** All data, every time. Best for: small data (<10M rows).
- **Pattern 2: Incremental.** Only new/updated rows. Best for: medium data (10M-1B rows).
- **Pattern 3: CDC (Change Data Capture).** Capture every change. Best for: high-frequency updates.
- **Pattern 4: Streaming.** Real-time events. Best for: real-time use cases.

**Mental model 2: The 3 Ingestion Modes.** 3 modes for when data is loaded.

```
1. Batch: once per day (or week)
2. Micro-batch: every 5-15 minutes
3. Streaming: real-time (sub-second)

The 3 modes trade off latency vs cost:
- Batch: lowest cost, highest latency
- Micro-batch: medium cost, medium latency
- Streaming: highest cost, lowest latency

The customer's use case determines the mode.
- Daily reports: batch
- Near-real-time dashboards: micro-batch
- Real-time decisions: streaming
```

**Mental model 3: The 2-Schema Strategy.** 2 schemas: raw and curated.

```
Raw schema: 1:1 with the customer's source data
- Preserves the customer's column names
- Preserves the customer's data types
- Preserves the customer's null handling
- Updated when the customer changes their schema

Curated schema: optimized for our platform
- Standardized column names
- Standardized data types
- PII masked or encrypted
- Validated against our data contract

The 2-schema strategy is the discipline. The raw schema
absorbs the customer's schema changes. The curated schema
feeds the platform. The FDE owns the transformation from
raw to curated.
```

**Mental model 4: The 4-Week Data Pipeline Timeline.** Ship in 4 weeks.

```
Week 1: Schema discovery
- Customer's source schema documented
- Schema changes tracked (last 6 months)
- Data contract signed with customer

Week 2: Pipeline build
- Raw schema ingestion (Pattern 2/3)
- Curated schema transformation
- Initial load (1M sample rows)

Week 3: Production hardening
- Incremental loads (Pattern 2)
- Error handling + retry logic
- Observability + alerts

Week 4: Hand-off
- Production load (50M rows)
- Customer-facing dashboards
- Runbook + on-call rotation
```

---

## 5. Frameworks

Three frameworks for data engineering for FDEs.

### Framework 1: The 1-Page Data Pipeline Plan

```
# Data Pipeline Plan — [Customer] — [Date]

## Customer data
- Source: [Snowflake / BigQuery / Redshift / Postgres]
- Volume: [N rows, M columns]
- PII: [Yes / No] — [Names, emails, etc.]
- Cloud: [AWS / GCP / Azure]
- Update frequency: [Daily / Hourly / Real-time]

## Data pattern decision
[Pattern 1 / 2 / 3 / 4 — Full load / Incremental / CDC / Streaming]

## Ingestion mode
[Batch / Micro-batch / Streaming]

## The 2-schema strategy
- Raw schema: [Customer's column names + types]
- Curated schema: [Standardized names + types + PII handling]

## Timeline
- Week 1: Schema discovery + data contract
- Week 2: Pipeline build (raw + curated)
- Week 3: Production hardening
- Week 4: Production load + hand-off

## The 1 thing the FDE will push back on
[1 sentence on what the FDE will NOT do.]
```

### Framework 2: The Data Contract (1 page)

```
# Data Contract — [Customer] — [Date]

## Source schema (raw)
| Column | Type | Nullable | PII | Notes |
|--------|------|----------|-----|-------|
| [Col 1] | [Type] | [Y/N] | [Y/N] | [Notes] |
| [Col 2] | ... | ... | ... | ... |

## Curated schema (target)
| Column | Type | Nullable | PII (masked) | Notes |
|--------|------|----------|--------------|-------|
| [Col 1] | [Type] | [Y/N] | [Y/N] | [Notes] |
| [Col 2] | ... | ... | ... | ... |

## Schema change protocol
- Customer notifies FDE 7 days before schema change
- FDE updates raw schema within 24 hours
- Curated schema updates within 7 days
- Backward compatibility maintained for 30 days

## SLA
- Data freshness: [Daily / Hourly / Real-time]
- Data accuracy: 99.9%
- Pipeline availability: 99.5%
```

### Framework 3: The Pipeline Observability Dashboard

```
# Pipeline Observability — [Customer] — [Date]

## Key metrics
| Metric | Target | Alert threshold |
|--------|--------|-----------------|
| Pipeline success rate | 99.5% | <99% |
| Data freshness | [N hours] | >[2N hours] |
| Row count (daily) | [N rows ±5%] | ±10% |
| Schema drift events | 0 | >1 per week |
| PII detection | 0 unmasked PII | >0 |

## Dashboards
- Pipeline status (real-time)
- Data freshness (real-time)
- Row count trends (daily)
- Schema drift events (real-time)
- PII compliance (real-time)

## Alerts
- Pipeline failure → PagerDuty → FDE on-call
- Schema drift → Slack → FDE
- PII detected unmasked → PagerDuty + Slack → FDE + CISO
```

---

## 6. Drill

You are an FDE at **acme-corp**. Customer A has data in Snowflake.

```
Customer A data:
- Source: Snowflake, 50M rows, 200 columns
- PII: Yes (names, emails, phone numbers)
- Cloud: AWS us-east-1
- Update frequency: Daily incremental
- Compliance: SOC 2, GDPR (EU customers)
- Time: 8 weeks total deployment
```

You have **90 minutes**. Produce the **data pipeline plan** (`portfolio/chapter-06-data-engineering.md`) using Framework 1 (Pipeline Plan) + Framework 2 (Data Contract) + Framework 3 (Observability). Specify:

- The 1-page data pipeline plan (data pattern, ingestion mode, 2-schema strategy, timeline, the 1 pushback).
- The data contract (raw schema sample, curated schema sample, change protocol, SLA).
- The pipeline observability dashboard (5 metrics, 5 dashboards, 3 alerts).
- The 4-week timeline (week-by-week checklist).
- The 1 thing you'll say to the PM in the first data review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-06-data-engineering.md` — under 1500 words.

---

## 7. Worked Example

**The 1-page data pipeline plan:**

```
# Data Pipeline Plan — Customer A — 2026-09-01

## Customer data
- Source: Snowflake
- Volume: 50M rows, 200 columns
- PII: Yes (names, emails, phone numbers)
- Cloud: AWS us-east-1
- Update frequency: Daily incremental
- Compliance: SOC 2, GDPR

## Data pattern decision
Pattern 2 (Incremental) + Pattern 3 (CDC for high-frequency
tables). Hybrid: incremental for most tables, CDC for
the 5 high-frequency tables (events, transactions).

## Ingestion mode
Batch (daily) for incremental tables, streaming (5-min
micro-batch) for CDC tables.

## The 2-schema strategy
- Raw schema: Snowflake 1:1 (preserves customer column names)
- Curated schema: standardized names + PII masked

## Timeline
- Week 1: Schema discovery + data contract
- Week 2: Pipeline build (raw + curated, 1M sample rows)
- Week 3: Production hardening (incremental + CDC)
- Week 4: Production load (50M rows) + hand-off

## The 1 thing the FDE will push back on
Streaming (real-time). The customer's use case is daily
reports, not real-time decisions. Daily incremental is
sufficient. Streaming adds 4 weeks and 3x cost.
```

**The data contract (sample):**

```
# Data Contract — Customer A — 2026-09-01

## Source schema (raw, sample 5 of 200)
| Column | Type | Nullable | PII | Notes |
|--------|------|----------|-----|-------|
| customer_id | BIGINT | N | N | Primary key |
| customer_name | VARCHAR | N | Y | Full name |
| email | VARCHAR | N | Y | Email address |
| phone | VARCHAR | Y | Y | E.164 format |
| created_at | TIMESTAMP | N | N | UTC |

## Curated schema (target, sample 5)
| Column | Type | Nullable | PII (masked) | Notes |
|--------|------|----------|--------------|-------|
| customer_id | BIGINT | N | N | Primary key |
| customer_name | VARCHAR | N | masked | First letter + *** |
| email | VARCHAR | N | masked | Hash for join |
| phone | VARCHAR | Y | masked | Last 4 only |
| created_at | TIMESTAMP | N | N | UTC |

## Schema change protocol
- Customer notifies FDE 7 days before schema change
- FDE updates raw schema within 24 hours
- Curated schema updates within 7 days
- Backward compatibility maintained for 30 days

## SLA
- Data freshness: 24 hours (batch), 5 minutes (CDC)
- Data accuracy: 99.9%
- Pipeline availability: 99.5%
```

**The pipeline observability dashboard:**

```
# Pipeline Observability — Customer A — 2026-09-01

## Key metrics
| Metric | Target | Alert threshold |
|--------|--------|-----------------|
| Pipeline success rate | 99.5% | <99% |
| Data freshness | 24h batch, 5min CDC | >48h, >15min |
| Row count (daily) | 50M ±5% | ±10% |
| Schema drift events | 0 | >1 per week |
| PII detection | 0 unmasked PII | >0 |

## Dashboards
- Pipeline status (real-time, Datadog)
- Data freshness (real-time, Datadog)
- Row count trends (daily, Datadog)
- Schema drift events (real-time, Datadog)
- PII compliance (real-time, Datadog)

## Alerts
- Pipeline failure → PagerDuty → FDE on-call
- Schema drift → Slack → FDE
- PII detected unmasked → PagerDuty + Slack → FDE + CISO
```

**The 4-week timeline:**

```
# Data Pipeline Timeline — Customer A — 2026-09-01

## Week 1 (Sept 1-7): Schema discovery
- [x] Customer's source schema documented (200 columns)
- [x] Schema changes tracked (last 6 months: 12 changes)
- [x] Data contract signed

## Week 2 (Sept 8-14): Pipeline build
- [ ] Raw schema ingestion (Pattern 2 incremental)
- [ ] Curated schema transformation (PII masked)
- [ ] Initial load (1M sample rows)
- [ ] Integration tests

## Week 3 (Sept 15-21): Production hardening
- [ ] Incremental loads (Pattern 2)
- [ ] CDC for 5 high-frequency tables (Pattern 3)
- [ ] Error handling + retry logic
- [ ] Observability dashboards

## Week 4 (Sept 22-28): Production load + hand-off
- [ ] Production load (50M rows)
- [ ] Customer-facing dashboards
- [ ] Runbook + on-call rotation
- [ ] Hand-off to customer's ops team
```

**The 1 thing I'll say to the PM in the first data review:**

```
"Here's the data pipeline plan for Customer A:

  Pattern: Pattern 2 (Incremental) + Pattern 3 (CDC)
  Mode: Batch (daily) for incremental, micro-batch (5 min)
    for CDC
  Schemas: Raw (Snowflake 1:1) + Curated (standardized +
    PII masked)
  Timeline: 4 weeks (W1: schema, W2: build, W3: hardening,
    W4: production + hand-off)

  Top 3 risks:
  1. Customer's schema has changed 12 times in 6 months
     — mitigation: schema change protocol + raw schema
     absorbs changes
  2. 50M rows is at the upper end of Pattern 2 — mitigation:
     load test in W2 with 1M sample
  3. PII handling must be SOC 2 + GDPR compliant —
     mitigation: PII masked at curated schema level, not
     raw

  The 1 thing I'll push back on: streaming (real-time).
  The customer's use case is daily reports, not real-time
  decisions. Daily incremental is sufficient. Streaming
  adds 4 weeks and 3x cost.

  The data pipeline is the discipline. The customer's
  data is the truth."
```

**The 3 things I'll do to avoid the 5 failure modes:**

```
1. Use the 2-schema strategy (raw + curated).
   (Avoids the 1-Schema Failure.)
   - Raw schema absorbs customer's schema changes
   - Curated schema feeds the platform
   - Schema change protocol: 7-day notice

2. Use Pattern 2 (Incremental) + Pattern 3 (CDC) for
   high-frequency tables. (Avoids the No-Incremental
   Failure.)
   - 50M rows full load = 12 hours (daily impossible)
   - Incremental = 30 min (daily feasible)
   - CDC for 5 high-frequency tables

3. Mask PII at the curated schema level.
   (Avoids the No-PII-Handling Failure.)
   - Raw schema preserves customer data (for debugging)
   - Curated schema masks PII (for compliance)
   - PII detection in observability dashboard
```

---

## 8. Failure Mode Postmortem

An FDE at a 200-person B2B AI company built a data pipeline for a strategic customer. The FDE used a single schema (raw + curated merged). The customer's schema changed twice in 3 months. The pipeline broke both times. The customer churned.

The replacement FDE did 3 things:
1. Used the 2-schema strategy (raw absorbs changes, curated is stable).
2. Used Pattern 2 (Incremental) + Pattern 3 (CDC) for high-frequency tables.
3. Masked PII at the curated schema level (SOC 2 + GDPR compliant).

Within 6 months: 4 data pipelines shipped, 0 customer churn, 0 schema drift incidents. The pipelines were observable, owned end-to-end, and SOC 2 + GDPR compliant.

What the first FDE missed: data engineering is a system. The first FDE treated data as a side concern. The second FDE treated data as the foundation. The foundation is the leverage.

The lesson: the FDE who has the 2-schema strategy + Pattern 2/3 + PII masking has a data pipeline. The FDE who has a single schema has a fragile pipeline.

---

## 9. Self-Assessment Rubric

| # | Dimension | 1 (Novice) | 3 (Competent) | 5 (Expert) |
|---|---|---|---|---|
| 1 | **4 data patterns** | 1 pattern only | 2-3 patterns | 4 patterns, chooses per-customer |
| 2 | **3 ingestion modes** | 1 mode only | 2 modes | 3 modes, chooses per-customer |
| 3 | **2-schema strategy** | 1 schema | 2 schemas, partial | 2 schemas (raw + curated), schema change protocol |
| 4 | **PII handling** | No PII handling | PII exists but partial | PII masked at curated schema, SOC 2 + GDPR compliant |
| 5 | **Observability** | No observability | Dashboards exist | 5 metrics + 5 dashboards + 3 alerts, PII compliance |

**Disqualifier:** any 1 on dimension 3 or 4. An FDE who has 1 schema or no PII handling is in the 1-Schema or No-PII-Handling failure mode.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-06-data-engineering.md` — interview evidence for "How do you build a data pipeline for a customer?" (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through a data pipeline you've built.**
2. **The customer's schema changes 5 times in 3 months. What do you do?**
3. **The customer wants real-time streaming but the use case is daily reports. What do you do?**
4. **PII compliance review fails. What do you do?**
5. **Walk me through a pipeline you've shipped in 4 weeks.**