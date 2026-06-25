# AI Engineer Playbook

## Errata & Known Issues

> **Honest accounting of what's incomplete, what might be wrong, and what the author would change in v2.**

### What's incomplete

- **Chapter 28 (LLM Methodology Appendix) is an appendix.** It introduces the 4-method model + 3 quality attributes but doesn't go deep on each method. The AIE should pair this with LLM-engineering-specific reading.

- **No case studies of named AIE transitions.** The chapters describe what good AIEs do, but don't include specific named case studies. v2 would add 5-10 named case studies.

- **No coverage of multi-modal AI features.** All chapters assume text-only LLM features. v2 would add a chapter on multi-modal (vision + speech + text).

### What might be wrong

- **The 4-pillar AIE model is one AIE's framework.** Some AIEs prefer 3-pillar (LLM integration + prompt engineering + AI feature delivery) or 5-pillar (with cost as a separate pillar). The book uses 4-pillar because it's the most common.

- **The 3 AI features per quarter target.** Some AIEs ship 1 feature per quarter, others ship 10+. The book uses 3 because it's the median for an AIE at a 200-person AI company.

- **Some Mermaid diagrams have visual artifacts.** mdBook's Mermaid renderer occasionally has issues with complex diagrams.

### What the author would change in v2

- **Add a chapter on multi-modal AI features.** Vision + speech + text integration.
- **Add a chapter on AI feature cost optimization.** Deep dive on cost reduction.
- **Add case studies.** 5-10 named case studies with permission.
- **Tighten the 5-criterion bar.** The book uses different 5-criterion bars in different chapters. v2 would standardize.

### Versioning

- **v1.0.0-aie** (2026-09-01) — Initial release. 28 chapters + preface + glossary + errata.

### Acknowledgments

This book was written by an AIE for AIEs. The book is the synthesis of AI engineering practice. If you're an AIE who has read this far: thank you. The AIE role is hard. The leverage is in the system. Build the system. Ship the features. Own the LLM stack.