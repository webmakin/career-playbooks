# AI Engineer Playbook
## Chapter 6

# RAG and Vector Search

> *"The AIE designs RAG pipelines. The 4-RAG-pillar framework (chunking + embedding + retrieval + generation), the 3-RAG templates (naive + hybrid + agentic), and the 5-criterion RAG quality bar are the AIE's reference for RAG at the contributor level."*

---

## 1. Epigraph

_The AIE designs RAG pipelines. The 4-RAG-pillar framework (chunking + embedding + retrieval + generation), the 3-RAG templates (naive + hybrid + agentic), and the 5-criterion RAG quality bar are the AIE's reference for RAG at the contributor level._

---

## 2. Problem

You are an AIE at acme-corp. The engineering manager has just told you: "rag and vector search. 30-day timeline."

This chapter tells you the 4 mental models, 3 frameworks, and 5-criterion quality bar.

**Decision in one sentence:** _AIE RAG design is a 4-pillar framework + 3 RAG templates + 5-criterion bar; the AIE's job is to design RAG pipelines, validate them, and own the RAG quality._

---

## 3. Why AIEs Fail Here

Five named failure modes of AIEs whose rag and vector search produced zero results.

- **The No-Chunking-Strategy Failure.** No chunking strategy. Bad retrieval.
- **The No-Embedding-Model Failure.** Wrong embedding model.
- **The No-Hybrid-Search Failure.** No hybrid search. Misses semantic.
- **The No-Reranking Failure.** No reranking. Top-k too low.
- **The No-Eval Failure.** No RAG eval.

---

## 4. Mental Models

Four mental models that compress rag and vector search.

**mental model 1: The 4 RAG Pillars:** 4 pillars: chunking + embedding + retrieval + generation.

**mental model 2: The 3 RAG Templates:** 3 templates: naive + hybrid + agentic.

**mental model 3: The 5-Criterion Bar:** 5 criteria: chunked + embedded + retrieved + generated + evaluated.

**mental model 4: The RAG Card:** 1-page RAG card.

---

## 5. Frameworks

Three frameworks for rag and vector search.

### Framework 1: The 1-Page Plan

```
# RAG and Vector Search - [Date]

## Top 3 strategic inputs
1. [Input 1]
2. [Input 2]
3. [Input 3]

## The 5-criterion bar applied

## The 1 thing the AIE will NOT compromise on
[1 sentence.]
```

### Framework 2: The Implementation Tracker

```
# Implementation Tracker - [Quarter]

| Item | Owner | Status | Date |
|------|-------|--------|------|
| [Item 1] | [Name] | [Status] | [Date] |
| [Item 2] | ... | | |
```

### Framework 3: The Retrospective Review

```
# Retrospective Review - [Date]

## Top 3 wins
1. [Win 1]
2. [Win 2]
3. [Win 3]

## Top 3 challenges
1. [Challenge 1]
2. [Challenge 2]
3. [Challenge 3]
```

---

## 6. Drill

You are an AIE at **acme-corp**. The engineering manager has given you 30 days to design the rag and vector search system.

You have **90 minutes**. Produce the **rag and vector search redesign** using the 3 frameworks above. Specify:

- The 1-page plan.
- The implementation tracker.
- The retrospective review template.
- The 30-day timeline.
- The 1 thing you'll say to the engineering manager in the first review.
- The 3 things you'll do to avoid the 5 failure modes.

**Deliverable:** `portfolio/chapter-06-aie-aie-rag.md` - under 1500 words.

---

## 7. Worked Example

**The 1-page RAG card:**

```
# RAG Card - B2B Docs

## Chunking
- 512 tokens, 50 overlap

## Embedding
- OpenAI text-embedding-3-large
```

---

## 8. Failure Mode Postmortem

An AIE at a 200-person B2B AI company shipped RAG with no chunking strategy. Bad retrieval. The PM said: 'Bad retrieval, bad answers.'

What the first AIE missed: rag and vector search is a system. The first AIE had no system. The second AIE had 4 mental models + 3 frameworks + 5 criteria. The system is the leverage.

The lesson: the AIE who has the system has rag and vector search. The AIE who has no system has the failure mode.

---

## 9. Self-Assessment Rubric

| 1 | **4 RAG pillars** | 0-1 | 2-3 | 4 pillars |
| 2 | **3 templates** | 1 | 2 | 3 templates |
| 3 | **5-criterion bar** | 0-2 | 3-4 | 5 criteria |
| 4 | **Retrieval recall** | <70% | 70-90% | 90%+ |
| 5 | **Eval coverage** | <50% | 50-90% | 100% |


**Disqualifier:** any 1 on dimension 1 or 3. An AIE who has no chunking or no eval is in the No-Chunking-Strategy or No-Eval failure mode.

**Total:** ___ / 25. **Pass threshold:** 18/25, no dimension below 3.

---

## 10. Portfolio Artifact Note

Save your filled-in drill as `portfolio/chapter-06-aie-aie-rag.md` - interview evidence for "Walk me through your RAG design." (see Portfolio Map in Chapter 27).

---

## 11. Interview Questions

1. **Walk me through your RAG design process.**
2. **Retrieval quality is low. What do you do?**
3. **The PM rejects the RAG answers. What do you do?**
4. **You have 3 RAG strategies. How do you prioritize?**
5. **Walk me through a RAG eval you've led.**
