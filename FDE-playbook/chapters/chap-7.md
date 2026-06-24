# Forward Deployed Engineer Playbook
## Chapter 7

# ML/AI Deployment for FDEs

> *"The FDE who ships ML/AI features ships differently. The 3 deployment modes (batch, real-time, edge), the 4 model serving patterns, the 2 feedback loops, and the 5 evaluation metrics are the FDE's reference for ML/AI deployments."*

---

## 1. Epigraph

_The FDE who ships ML/AI features ships differently. The 3 deployment modes (batch, real-time, edge), the 4 model serving patterns, the 2 feedback loops, and the 5 evaluation metrics are the FDE's reference for ML/AI deployments._

---

## 2. Problem

You are an FDE at acme-corp. The customer wants an LLM-powered recommendation feature in their product. They have 50K end users. They want sub-second latency. They have compliance requirements (no PII sent to third-party LLMs). The PM says: "Just call OpenAI." The Director says: "We need to evaluate 3 vendors." You have 8 weeks.

This chapter tells you the 3 deployment modes, the 4 serving patterns, the 2 feedback loops, and the 5 evaluation metrics.

**Decision in one sentence:** _FDE ML/AI deployment is a 4-pattern system (third-party API, self-hosted open-source, self-hosted fine-tuned, custom-trained) chosen per-customer, deployed in 6-12 weeks, with a 3-mode serving architecture (batch, real-time, edge) and 5 evaluation metrics; the FDE's job is to design the ML architecture for the customer's constraints, ship in 8 weeks, and own the production model._

---

## 3. Why FDEs Fail Here

Five named failure modes of FDEs whose ML/AI deployment produced zero results.

- **The 1-Vendor Failure.** The FDE picks one vendor (e.g., OpenAI) without evaluating alternatives. _The customer has constraints that rule out the vendor._
- **The No-Evaluation Failure.** The FDE ships without evaluating accuracy, latency, or cost. _The model degrades in production._
- **The No-Feedback-Loop Failure.** The FDE ships the model without collecting user feedback. _The model drifts, no one notices._
- **The PII-In-LLM-Prompt Failure.** The FDE sends customer PII to a third-party LLM. _The customer fails compliance review._
- **The 6-Month-ML-Deployment Failure.** The FDE spends 6 months building a custom model. _The customer churns before the model ships._

---

## 4. Mental Models

Four mental models that compress ML/AI deployment for FDEs.

**Mental model 1: The 4 ML Serving Patterns.** 4 patterns for serving ML models.

```mermaid
%% Figure 7.1 — The 4 ML serving patterns
flowchart LR
    P1[Pattern 1: Third-party API<br/>OpenAI, Anthropic, etc.<br/>Fastest (1-2 weeks)]
    P2[Pattern 2: Self-hosted open-source<br/>Llama, Mistral, etc.<br/>4-6 weeks]
    P3[Pattern 3: Self-hosted fine-tuned<br/>Open-source + fine-tuning<br/>8-12 weeks]
    P4[Pattern 4: Custom-trained<br/>From scratch<br/>12-24 weeks]
    P1 --> P2
    P2 --> P3
    P3 --> P4
```

**The 4 patterns:**
- **Pattern 1: Third-party API.** OpenAI, Anthropic, etc. Fastest (1-2 weeks).
- **Pattern 2: Self-hosted open-source.** Llama, Mistral, etc. 4-6 weeks.
- **Pattern 3: Self-hosted fine-tuned.** Open-source + fine-tuning on customer data. 8-12 weeks.
- **Pattern 4: Custom-trained.** From scratch. 12-24 weeks.

**Mental model 2: The 3 Deployment Modes.** 3 modes for serving ML models.

```
1. Batch: model runs on a schedule (e.g., nightly)
   - Best for: offline scoring, recommendation pre-compute
   - Latency: minutes to hours
   - Cost: lowest

2. Real-time: model runs per request
   - Best for: chat, search, recommendations
   - Latency: sub-second to 1 second
   - Cost: medium

3. Edge: model runs on the device
   - Best for: mobile, IoT, low-latency
   - Latency: 10-100ms
   - Cost: highest (model size limits)

The 3 modes trade off latency vs cost vs complexity.
```

**Mental model 3: The 2 Feedback Loops.** 2 loops for model improvement.

```
Loop 1: Implicit feedback
- User behavior (clicks, dwell time, conversions)
- Used for: online evaluation, drift detection
- Latency: real-time

Loop 2: Explicit feedback
- User ratings, thumbs up/down, corrections
- Used for: model retraining, evaluation set
- Latency: weekly to monthly

The FDE owns both loops. The implicit loop is built
into the product. The explicit loop is built into the
deployment. The 2 loops feed the model improvement
cadence.
```

**Mental model 4: The 5 Evaluation Metrics.** 5 metrics for ML model quality.

```
1. Accuracy: % correct predictions (target: 90%+)
2. Latency: time per prediction (target: <500ms real-time)
3. Cost: $ per 1K predictions (target: varies)
4. Bias: fairness across user segments (target: <5% gap)
5. Drift: model degradation over time (target: <2% per month)

The 5 metrics are the FDE's reference. The FDE who
tracks all 5 has a model. The FDE who tracks 1-2 has
a fragile model.
```

---

## 5. Frameworks

Three frameworks for ML/AI deployment for FDEs.

### Framework 1: The 1-Page ML Architecture

```
# ML Architecture — [Customer] — [Date]

## Customer constraints
- Use case: [Chat / Search / Recommendation / Classification]
- Scale: [N end users, M requests/day]
- Latency: [Real-time / Batch / Edge]
- Compliance: [PII / GDPR / HIPAA / None]
- Cost target: $[X]/1K predictions

## Serving pattern decision
[Pattern 1 / 2 / 3 / 4 — Third-party / Open-source / Fine-tuned / Custom]

## Deployment mode
[Batch / Real-time / Edge]

## The 2 feedback loops
- Implicit: [User behavior tracked via X]
- Explicit: [User ratings via X]

## The 5 evaluation metrics
- Accuracy: [Target]
- Latency: [Target]
- Cost: [Target]
- Bias: [Target]
- Drift: [Target]

## The 1 thing the FDE will push back on
[1 sentence.]
```

### Framework 2: The Vendor Evaluation Matrix

```
# Vendor Evaluation — [Use Case] — [Date]

## The 4 vendors (example for LLM)
| Vendor | Accuracy | Latency | Cost/1K | PII | Notes |
|--------|----------|---------|---------|-----|-------|
| OpenAI | 95% | 200ms | $0.03 | Yes | Most popular |
| Anthropic | 94% | 250ms | $0.025 | Yes | Better reasoning |
| Self-hosted Llama | 90% | 100ms | $0.005 | No | Data sovereignty |
| Self-hosted fine-tuned | 92% | 150ms | $0.01 | No | Customer-specific |

## The recommendation
[Vendor + 1 sentence on why]

## The 3 trade-offs
1. Accuracy vs cost
2. Latency vs data sovereignty
3. Vendor lock-in vs build effort
```

### Framework 3: The Model Observability Dashboard

```
# Model Observability — [Customer] — [Date]

## The 5 metrics
| Metric | Target | Alert threshold |
|--------|--------|-----------------|
| Accuracy | 90%+ | <85% |
| Latency (p99) | <500ms | >1s |
| Cost / 1K | $[X] | >$[2X] |
| Bias gap | <5% | >10% |
| Drift | <2%/month | >5%/month |

## Dashboards
- Model performance (real-time)
- Latency (real-time)
- Cost (daily)
- Bias by segment (weekly)
- Drift detection (daily)

## Alerts
- Accuracy drop → Slack → FDE + ML team
- Latency spike → PagerDuty → FDE on-call
- Cost spike → Slack → FDE + Finance
- Bias gap > 10% → PagerDuty + Slack → FDE + ML team + CISO
- Drift > 5%/month → Slack → FDE + ML team
```

---

## 6. Drill

You are an FDE at **acme-corp**. Customer A wants an LLM-powered recommendation feature.

```
Customer A:
- Use case: Real-time recommendations (sub-second latency)
- Scale: 50K end users, 5M requests/day
- Compliance: GDPR + no PII to third-party LLMs
- Cost target: <$0.01 per 1K predictions
- Time: 8 weeks
```

You have **90 minutes**. Produce the **ML architecture** (`portfolio/chapter-07-ml-deployment.md`) using Framework 1 (ML Architecture) + Framework 2 (Vendor Evaluation) + Framework 3 (Observability). Specify:

- The 1-page ML architecture (serving pattern, deployment mode, 2 loops, 5 metrics, the 1 pushback).
- The vendor evaluation matrix (4 vendors, recommendation, 3 trade-offs).
- The model observability dashboard (5 metrics, 5 dashboards, 3 alerts).
- The 8-week timeline (week-by-week checklist).
- The 1 thing you'll say to the PM in the first ML review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-07-ml-deployment.md` — under 1500 words.

---

## 7. Worked Example

**The 1-page ML architecture:**

```
# ML Architecture — Customer A — 2026-09-01

## Customer constraints
- Use case: Real-time recommendations
- Scale: 50K end users, 5M requests/day
- Latency: <500ms (real-time)
- Compliance: GDPR + no PII to third-party LLMs
- Cost target: <$0.01 per 1K predictions

## Serving pattern decision
Pattern 2 (Self-hosted open-source, Llama 3 70B) +
Pattern 3 (Fine-tuned on customer data, ~10K examples).

## Deployment mode
Real-time (sub-second latency)

## The 2 feedback loops
- Implicit: User behavior (clicks, dwell time, conversions)
  tracked via Segment
- Explicit: User ratings (1-5 stars) via in-app prompt

## The 5 evaluation metrics
- Accuracy: 90%+ (recommendation click-through rate)
- Latency: <300ms p99
- Cost: <$0.008 per 1K predictions (GPU cost amortized)
- Bias: <5% gap across user segments
- Drift: <2% per month

## The 1 thing the FDE will push back on
Pattern 4 (custom-trained). The customer's use case is
recommendations, not novel ML. Pattern 2 + 3 is
sufficient. Custom training adds 12 weeks and $500K.
```

**The vendor evaluation matrix:**

```
# Vendor Evaluation — Real-time recommendations — 2026-09-01

## The 4 vendors
| Vendor | Accuracy | Latency | Cost/1K | PII | Notes |
|--------|----------|---------|---------|-----|-------|
| OpenAI | 92% | 200ms | $0.03 | Yes | Most popular, but PII risk |
| Anthropic | 91% | 250ms | $0.025 | Yes | Better reasoning, PII risk |
| Self-hosted Llama | 88% | 100ms | $0.005 | No | Data sovereignty ✓ |
| Self-hosted fine-tuned | 90% | 150ms | $0.01 | No | Customer-specific |

## The recommendation
Self-hosted fine-tuned (Pattern 3) — meets accuracy target
(90%), meets latency target (<500ms), meets cost target
($0.01/1K), meets GDPR (no PII to third-party).

## The 3 trade-offs
1. Accuracy vs cost: 90% (fine-tuned) vs 92% (OpenAI) —
   trade 2% accuracy for $0.02/1K cost savings
2. Latency vs data sovereignty: 150ms (self-hosted) vs
   200ms (OpenAI) — trade 50ms for data sovereignty
3. Vendor lock-in vs build effort: self-hosted = more
   build effort, but no vendor lock-in
```

**The model observability dashboard:**

```
# Model Observability — Customer A — 2026-09-01

## The 5 metrics
| Metric | Target | Alert threshold |
|--------|--------|-----------------|
| Accuracy (CTR) | 90%+ | <85% |
| Latency (p99) | <300ms | >500ms |
| Cost / 1K | <$0.01 | >$0.015 |
| Bias gap | <5% | >10% |
| Drift | <2%/month | >5%/month |

## Dashboards
- Model performance (real-time, Datadog)
- Latency p99 (real-time, Datadog)
- Cost (daily, Datadog)
- Bias by segment (weekly, Datadog)
- Drift detection (daily, Datadog)

## Alerts
- CTR drop → Slack → FDE + ML team
- Latency spike → PagerDuty → FDE on-call
- Cost spike → Slack → FDE + Finance
- Bias gap > 10% → PagerDuty + Slack → FDE + ML team + CISO
- Drift > 5%/month → Slack → FDE + ML team
```

**The 8-week timeline:**

```
# ML Deployment Timeline — Customer A — 2026-09-01

## Week 1-2: Architecture decision
- [x] Vendor evaluation (4 vendors)
- [x] Serving pattern decision (Pattern 2 + 3)
- [x] Customer sign-off

## Week 3-4: Fine-tuning setup
- [ ] Customer data preparation (10K examples)
- [ ] Fine-tuning pipeline (Llama 3 70B)
- [ ] Initial model evaluation

## Week 5-6: Deployment
- [ ] Self-hosted inference (GPU cluster)
- [ ] Real-time serving (<300ms p99)
- [ ] Integration with customer's product

## Week 7-8: Observability + Hand-off
- [ ] Observability dashboards (5 metrics)
- [ ] Implicit + explicit feedback loops
- [ ] Runbook + on-call rotation
- [ ] Hand-off to customer's ML team
```

**The 1 thing I'll say to the PM in the first ML review:**

```
"Here's the ML architecture for Customer A:

  Serving: Pattern 2 (Self-hosted Llama) + Pattern 3
    (Fine-tuned on 10K customer examples)
  Deployment: Real-time (sub-second latency)
  Compliance: GDPR + no PII to third-party (self-hosted)
  Cost: $0.008 per 1K predictions (vs. $0.03 OpenAI)

  The 5 metrics:
  - Accuracy: 90%+ (CTR)
  - Latency: <300ms p99
  - Cost: <$0.01 per 1K
  - Bias: <5% gap
  - Drift: <2%/month

  Top 3 risks:
  1. Self-hosted GPU cost — mitigation: amortize across
     3 customers (3x utilization)
  2. Fine-tuning quality — mitigation: 10K labeled
     examples, weekly retraining
  3. Real-time latency — mitigation: GPU cluster with
     auto-scaling

  The 1 thing I'll push back on: custom-trained model.
  Customer's use case is recommendations, not novel ML.
  Pattern 2 + 3 is sufficient. Custom training adds
  12 weeks and $500K.

  The ML architecture is the discipline. The customer's
  data is the truth."
```

**The 3 things I'll do to avoid the 5 failure modes:**

```
1. Use Pattern 2 + 3 (not 1 vendor only).
   (Avoids the 1-Vendor Failure.)
   - 4 vendors evaluated
   - Self-hosted + fine-tuned meets GDPR + cost + latency

2. Track all 5 evaluation metrics.
   (Avoids the No-Evaluation Failure.)
   - Accuracy + latency + cost + bias + drift
   - 5 dashboards + 3 alerts

3. Build both feedback loops (implicit + explicit).
   (Avoids the No-Feedback-Loop Failure.)
   - Implicit: clicks, dwell time, conversions
   - Explicit: user ratings
   - Both feed weekly retraining cadence
```

---

## 8. Failure Mode Postmortem

An FDE at a 200-person B2B AI company shipped an LLM-powered recommendation feature. The FDE used OpenAI without evaluating alternatives. The customer had GDPR + no-PII constraints. The deployment failed compliance review. The customer churned.

The replacement FDE did 3 things:
1. Evaluated 4 vendors (OpenAI, Anthropic, self-hosted Llama, self-hosted fine-tuned).
2. Tracked all 5 evaluation metrics (accuracy, latency, cost, bias, drift).
3. Built both feedback loops (implicit + explicit).

Within 6 months: 3 ML deployments shipped, 0 customer churn. The deployments met GDPR + cost + latency targets.

What the first FDE missed: ML deployment is a system. The first FDE picked one vendor. The second FDE evaluated 4. The evaluation is the leverage.

The lesson: the FDE who has a vendor matrix + 5 metrics + 2 feedback loops has an ML deployment. The FDE who picks one vendor has a fragile deployment.

---

## 9. Self-Assessment Rubric

| # | Dimension | 1 (Novice) | 3 (Competent) | 5 (Expert) |
|---|---|---|---|---|
| 1 | **4 serving patterns** | 1 pattern only | 2-3 patterns | 4 patterns, chooses per-customer |
| 2 | **3 deployment modes** | 1 mode only | 2 modes | 3 modes, chooses per-customer |
| 3 | **2 feedback loops** | 0-1 loops | 1 loop | 2 loops (implicit + explicit), feeds retraining |
| 4 | **5 evaluation metrics** | 1-2 metrics | 3-4 metrics | 5 metrics (accuracy + latency + cost + bias + drift) |
| 5 | **Vendor evaluation** | 1 vendor | 2-3 vendors | 4 vendors evaluated, recommendation documented |

**Disqualifier:** any 1 on dimension 1 or 4. An FDE who uses 1 pattern or tracks 1-2 metrics is in the 1-Vendor or No-Evaluation failure mode.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-07-ml-deployment.md` — interview evidence for "How do you ship ML/AI features?" (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through an ML deployment you've shipped.**
2. **The customer wants OpenAI but has GDPR constraints. What do you do?**
3. **The model accuracy drops from 92% to 85% in production. What do you do?**
4. **The customer wants sub-100ms latency but the model is too large. What do you do?**
5. **Walk me through an ML feedback loop you've built.**
