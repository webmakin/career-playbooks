# Glossary

> Terminology used throughout the playbook. The glossary is opinionated — these are the working definitions the author uses. If a definition differs from your org's, prefer your org's and note the divergence.

---

## A

**AI feature** — A product capability that uses an AI model (LLM, classifier, recommendation system) as part of its user-facing surface. Distinct from "AI infrastructure" (the platform that supports AI features) and "AI research" (the lab work that produces new techniques).

**AI Engineering Director** — The single accountable owner of how a company invests in, builds with, and is changed by AI, across engineering, product, and the business. Distinct from "Head of AI Research" (research-only) and "VP of AI" (larger org, more executives reporting in).

**AI Engineering Manager** — Manager of an AI team (5–10 reports). Reports to Director. Distinct from "AI Tech Lead" (senior IC) and "Director of AI" (above this role).

**AI literacy** — The ability to read an AI system's behavior, evaluate it against business and user goals, and make informed decisions about cost, quality, latency, and risk. A Director's literacy is broader than an IC's — the Director reads the system as a whole, not the parts.

**Audit trail** — The complete, reproducible record of an AI feature's inputs, outputs, and decisions over time. Composed of 7 elements (see Ch 25): training data lineage, model versions, prompt versions, request/response logs, eval results, deployment history, incident history.

**Auto-eval** — An automated evaluation of AI feature quality, typically run on a sampled set of production traffic. Distinct from "offline eval" (run on a held-out eval set) and "human eval" (run by humans on a sampled set).

---

## B

**Build-vs-buy** — The decision between building an AI capability in-house vs. buying it from a vendor. The decision is multi-dimensional (cost, time, reversibility, moat, team capacity) — see Ch 4.

**Black-box evaluation** — Evaluation against a metric the model does not see during training. Distinct from "white-box evaluation" (where the model has access to its own training data, which biases the eval).

---

## C

**Cost-quality-latency triangle** — The three competing constraints on an AI feature. You can optimize for two of the three, but not all three. See Ch 7.

**Chokepoint** — A specific point in an AI system's flow where most of the cost, latency, or failure modes concentrate. The Director's job is to identify the chokepoint, not to spread attention evenly across the system.

**Cost estimation** — The discipline of modeling an AI feature's cost per request, per day, per month, and per year (with growth). The book uses `_shared/tools/cost_estimator.py` for this — see Ch 7.

**Cost per request** — The dollar cost of one inference call. Includes input tokens, output tokens, and any retrieval cost. Distinct from "cost per user" (which divides cost per request by the number of requests per user).

**Context window** — The maximum number of tokens (input + output) a model can process in one call. Larger windows are more expensive per call.

---

## D

**Director** — A senior individual contributor or manager who owns a function, a product line, or a cross-functional capability. In the AI Engineering Director role, the Director owns the company's AI function (engineering, product, governance) and reports to a VP, CTO, or CEO.

**Drift** — A change in the input or output distribution of an AI feature over time. Drift can be benign (seasonal) or harmful (quality regression). The book distinguishes "input drift," "output drift," and "outcome drift" — see Ch 12.

**Domain shift** — A specific type of drift where the input distribution changes in a way the model was not trained for. Often appears as a new customer type, a new product feature, or a new market.

**Decision memo** — A 1-page document that lays out a decision, the context, the options considered, the recommendation rationale, the risks, and the decision needed by date. The Director's primary written artifact. See Ch 21.

**Deploy gate** — A check that must pass before an AI feature is deployed to production. Common gates: Responsible AI review (Ch 22), compliance check (Ch 23), eval pass rate (Ch 9), quality SLO (Ch 12), audit trail (Ch 25).

**Discovery** — The first stage of the AI feature lifecycle, where the feature is identified and scoped. Distinct from "build" (where the feature is implemented) and "deploy" (where the feature ships).

---

## E

**Eval set** — A held-out set of inputs and expected outputs used to measure an AI feature's quality. Distinct from "training set" (data the model learns from) and "test set" (data used for model selection).

**Eval-driven iteration** — The practice of using eval results to decide what to improve next. Distinct from "vibes-driven iteration" (where the team improves based on anecdotal feedback).

**Embedding** — A vector representation of text (or image, audio) used for similarity search. Embeddings are the foundation of RAG systems.

**EU AI Act** — The European Union's regulation on AI systems, in force from 2024–2026. Categorizes AI systems into 4 risk tiers (Unacceptable, High, Limited, Minimal) with different obligations per tier. See Ch 23.

**Evidence-based promotion** — A promotion system where each level's expectations are explicit and promotions are linked to documented evidence (not tenure or manager preference). See Ch 20.

---

## F

**Failure mode** — A specific, named way an AI feature can fail. The book uses 5 named failure modes per chapter. A failure mode is more specific than a "risk" — it includes the mechanism, the trigger, and the consequence.

**Failure mode postmortem** — A case study in Section 8 of every chapter, showing a real (anonymized) case where someone got the decision wrong. Includes what they missed and what they should have done.

**Fine-tuning** — The process of further training a base model on a smaller, task-specific dataset. Distinct from "prompting" (no training, just context) and "continued pretraining" (large-scale training on a different domain).

**Framework** — A fillable template for a recurring decision. The book uses 3 frameworks per chapter. A framework is more specific than a "principle" and more reusable than a "rule of thumb."

**Full-stack observability** — The discipline of tracking every layer of an AI feature (data, model, retrieval, eval, cost, latency, business outcome) and tying them together so failures are diagnosable. See Ch 12.

---

## G

**GenAI** — Generative AI. Models that produce text, image, audio, or video outputs (as opposed to discriminative models that produce classifications or scores). The book focuses primarily on GenAI (specifically LLMs) but the frameworks apply to discriminative AI as well.

**Ground truth** — The correct answer for an eval input. Distinct from "label" (which can be wrong) and "synthetic label" (generated by another model).

**Guardrail** — A specific, implemented constraint on an AI feature's behavior. Examples: input filters (block PII), output filters (block unsafe content), rate limits, refusal categories. Distinct from "guideline" (which is advisory, not enforced).

---

## H

**Hallucination** — A confident, fluent, wrong answer from a model. Distinguished from "uncertainty" (the model says "I don't know") and "errors" (the model gives a wrong answer with low confidence). See Ch 9 for the eval categories.

**Hub-and-spoke topology** — An org design where a central AI platform team (the hub) supports embedded engineers in product teams (the spokes). Distinct from "fully embedded" (no central team) and "fully centralized" (no embedded engineers). See Ch 18.

**Hub model** — A centralized AI platform team that owns the gateway, eval system, and lifecycle. The hub serves the spokes. See Ch 18.

---

## I

**Incident** — Any unplanned event that degrades an AI feature's quality, availability, or safety. The book uses a 5-level severity ladder (SEV-1 through SEV-5). See Ch 24.

**Incident Commander (IC)** — The named person who owns a crisis response. The IC has authority to make the stop-the-bleed decision (keep running, reduce traffic, disable, rollback). See Ch 24.

**Inference** — The act of running a model to produce an output. The book distinguishes "training-time" (one-time cost) from "inference-time" (recurring cost per call). Inference is usually 80%+ of an AI feature's lifetime cost.

**Inference cost** — The dollar cost of running the model. Includes input tokens, output tokens, model choice, and any caching or batching. See Ch 7.

**IC-to-Director category change** — The cognitive shift from being an expert (knowing the answer) to being a system (knowing which answer to ask for, by whom, and when). See Ch 2.

---

## L

**Latency** — The time between a user request and the model's first token (time to first token, TTFT) or the full response (end-to-end latency). Distinct from "throughput" (requests per second the system can handle).

**Lifecycle** — The end-to-end process of an AI feature: discover → build → eval → deploy → operate → decommission. See Ch 10.

**LLM** — Large Language Model. A model trained on a large corpus of text to predict the next token. The most common form of GenAI in production today.

**LLMOps** — The discipline of operating LLM-based systems in production. Distinct from "MLOps" (which historically focused on classical ML). See Ch 10.

**Locked-in (high-reversibility-class)** — A vendor or architecture choice that is expensive or impossible to reverse. See Ch 1 for the 4 reversibility classes.

---

## M

**MLOps** — The discipline of operating ML systems in production. Pre-dates LLMOps. See Ch 10.

**Mental model** — A reusable lens for thinking about a class of decisions. The book uses 4 mental models per chapter. A mental model is more general than a framework and more specific than a principle.

**Mermaid diagram** — A text-based diagram syntax that renders as SVG. Used throughout the book for mental-model and framework illustrations. See `_shared/figure-style-guide.md` for the convention.

**Multi-vendor gateway** — A model-agnostic serving layer that can route requests to multiple model vendors (OpenAI, Anthropic, open-source) without changing application code. The book's recommended architecture for production AI features. See Ch 11.

**Multi-tenant isolation** — The discipline of ensuring that data and context for one customer are never leaked to another customer in a multi-tenant AI system. See Ch 8.

---

## N

**NIST AI RMF** — The National Institute of Standards and Technology's AI Risk Management Framework. A voluntary US framework. See Ch 23.

**No-decision discipline** — The practice of saying "no" to stakeholder requests that don't serve the strategy, in order to protect the team's focus. See Ch 21.

---

## O

**Observability** — The ability to understand a system's behavior from its outputs. In AI systems, this includes the model's outputs, the retrieval context, the eval results, and the production metrics. See Ch 12.

**Online eval** — Evaluation that runs against production traffic (a sampled subset). Distinct from "offline eval" (run against a held-out set).

**Org topology** — The structure of the AI org: centralized, embedded, hub-and-spoke, platform-led, federated. See Ch 18.

---

## P

**PII** — Personally Identifiable Information. The book uses a 4-tier classification (P0 public, P1 internal, P2 sensitive, P3 highly sensitive). See Ch 13.

**Platform team** — A team that owns shared infrastructure used by multiple product teams. In AI contexts, the platform team typically owns the model gateway, the eval system, the lifecycle tooling, and the observability stack. See Ch 11.

**Portfolio artifact** — A concrete deliverable produced by a drill, saved as `portfolio/chapter-NN-<artifact>.md`. The artifact is interview evidence. See Ch 27 for the map from artifact to interview question.

**Prompt** — The input to an LLM at inference time. Composed of a system message, a user message, and (optionally) tool/function definitions. The book distinguishes "system prompt" (developer-controlled), "user prompt" (user-controlled), and "context" (retrieved documents).

**Prompt versioning** — The discipline of version-controlling every prompt change (with git SHA or equivalent) and being able to roll back. The book treats prompts as production code. See Ch 25.

---

## Q

**Quality SLO** — A Service Level Objective for an AI feature's quality (e.g., "95% of responses must pass the eval set"). Distinct from "availability SLO" (uptime) and "latency SLO" (response time). See Ch 12.

---

## R

**RAG** — Retrieval-Augmented Generation. The pattern of retrieving relevant documents at inference time and including them in the prompt. See Ch 8.

**Reasoning class** — A model's reasoning capability (test-time compute, chain-of-thought, etc.). Models with stronger reasoning are typically more expensive. See Ch 6.

**Responsible AI** — The discipline of building AI features that are fair, accountable, transparent, and safe. The book uses a 5-dimension review (Fairness, Privacy, Transparency, Safety, Accountability) per Ch 22.

**Reversibility class** — A classification of how reversible a decision is. Type 1 = fully reversible (revert in <1 day). Type 4 = irreversible (years of work to change). See Ch 1.

**Rubric** — A scoring grid for grading work. The book uses a 5-dimension rubric per chapter. See `_shared/rubric-spec.md` for the convention.

---

## S

**Scope-of-decision (SOD)** — The scope of a single decision's impact. A Director's decisions typically have a wider SOD than an IC's. See Ch 2.

**Spoke** — A product team that consumes the AI platform. In hub-and-spoke, spokes have embedded engineers who build product-specific features on top of the platform. See Ch 18.

**System design interview** — A Director-level interview round where the candidate designs a system in 45 minutes. The book has a structured 8-dimension coverage pattern in Ch 28.

**Stakeholder** — Any person or group whose goals affect or are affected by the AI function. Includes CEO, CTO, CFO, product VPs, customers, regulators, and the team. See Ch 21.

**Stop-the-bleed decision** — The first 30 minutes of crisis response, where the IC chooses between 4 options: keep running, reduce traffic, disable, rollback. See Ch 24.

---

## T

**Team topology** — Same as org topology. See Ch 18.

**TCO (Total Cost of Ownership)** — The total dollar cost over a feature's lifetime, including initial build, ongoing operations, and decommission. See Ch 7 and Ch 16.

**Test set** — A held-out set of inputs used during model training to compare candidate models. Distinct from "eval set" (used post-training) and "production traffic" (real users).

**30/60/90 plan** — A written plan for the first 90 days in a new role. The book uses a window strategy: Days 1–30 diagnose, Days 31–60 plan, Days 61–90 execute. See Ch 26.

**Token** — A unit of text (roughly 4 characters in English) used by LLMs. Costs are typically priced per 1K or 1M tokens.

**Token-cost amnesia** — The tendency of vendors and customers to forget that token costs scale with usage. A common source of "we thought this was free" surprises. See Ch 3.

---

## U

**Unit economics** — The cost and revenue per unit (per request, per user, per feature). The book uses this as the primary lens for cost engineering. See Ch 7 and Ch 16.

---

## V

**Vendor lock-in** — A situation where switching vendors is expensive or impossible due to technical, contractual, or organizational reasons. The book recommends multi-vendor gateways to reduce lock-in. See Ch 4.

**Vector database** — A database optimized for similarity search over embeddings. Examples: Pinecone, Weaviate, Qdrant, Milvus.

**Vibes-driven iteration** — Improving a feature based on anecdotal feedback ("users like it more") rather than evals. The book treats this as a failure mode. See Ch 9.

---

## W

**Worked example** — A fully-completed version of a drill, included in Section 7 of every chapter. The reader uses the worked example to compare their own output.

---

## Y

**Yak-shaving** — The pattern of solving a problem by solving a sequence of related sub-problems, each of which seems necessary but none of which is the actual goal. The book warns against yak-shaving in the MLOps lifecycle. See Ch 10.

---

## Acronyms (quick reference)

- **AI** — Artificial Intelligence
- **DPI** — Director of Product / Director of Platform (context-dependent)
- **DPO** — Data Protection Officer
- **EM** — Engineering Manager
- **GDPR** — General Data Protection Regulation (EU)
- **HIPAA** — Health Insurance Portability and Accountability Act (US)
- **IC** — Individual Contributor (also: Incident Commander, in Ch 24)
- **LLM** — Large Language Model
- **NIST** — National Institute of Standards and Technology (US)
- **OECD** — Organisation for Economic Co-operation and Development
- **PII** — Personally Identifiable Information
- **PM** — Product Manager
- **RAG** — Retrieval-Augmented Generation
- **SEV** — Severity (in incident response)
- **SLA** — Service Level Agreement
- **SLO** — Service Level Objective
- **SOC 2** — Service Organization Control 2 (security compliance)
- **SWE** — Software Engineer
- **TCO** — Total Cost of Ownership
- **TTFT** — Time to First Token
- **VPE** — VP of Engineering