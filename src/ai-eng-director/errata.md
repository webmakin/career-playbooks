# Errata & Known Issues

> **Honest accounting of what's incomplete, what might be wrong, and what the author would change in v2.**

This page lists the things in the v1.0.0 release that the author knows are imperfect. The goal is **transparency** — the reader should know what to double-check and where to apply their own judgment.

## Incomplete

### Exercise bundles

19 of 28 chapters have full exercise bundles (drill + template + worked-example + README). The 9 chapters without bundles are:

- **Ch 1, Ch 2, Ch 5, Ch 6, Ch 8, Ch 9** (Part I–II): these were written first under time pressure; the drills are inline in Section 6 but no separate `exercises/chapterNN/` bundle was generated.
- **Ch 26, Ch 27, Ch 28** (Part VII): these are capstone/integration chapters; the drills are complex enough that a single bundle is insufficient. Future versions will ship a 2-bundle sequence per chapter.

The inline drills in those chapters are still runnable. The bundle is a convenience.

### Code examples in chapters 5, 6, 7, 8

The technical chapters (5–8) describe Python patterns for data pipelines, training, inference, and RAG. v1.0.0 has prose only — no executable Python files in `code/`. The book mirrors the build-gpt-from-scratch style, but the BGFS reference ships runnable code per chapter (e.g. `code/chapter03/tokenizer.py`).

A future v1.1.0 will add a parallel `code/` directory with runnable examples. The prose is correct; the runnability is what changes.

## Known imprecisions

### Cost numbers

The worked examples in Chapters 3, 4, 6, 7 cite specific dollar figures from `_shared/tools/cost_estimator.py`. These are based on the model's pricing as of June 2026. **AI vendor pricing changes frequently.** The numbers will drift.

- Verify the current cost by re-running `python3 _shared/tools/cost_estimator.py --fixture` before relying on the worked example.
- The growth-rate formula assumes a 25% quarterly growth rate. Different orgs see different growth; the formula generalizes.

### EU AI Act timeline

Chapter 23 references the EU AI Act's staged implementation. The full act entered into force in August 2024, with most provisions applying from August 2025–August 2027. **Verify the current status** of any specific provision before relying on the chapter's date framing.

### Vendor pricing (specific)

Chapters 3, 4, 6, 7 cite OpenAI, Anthropic, and DeepSeek pricing. These vendors change pricing periodically. The pricing in the worked examples is from June 2026. **Verify current pricing** before publishing a business case based on the worked example.

### Mermaid diagrams

The book uses Mermaid for mental-model and framework illustrations. mdBook renders Mermaid via inline JavaScript. If a diagram fails to render in your browser:

1. Check that your browser supports JavaScript (Mermaid runs client-side).
2. Refresh the page (Mermaid re-renders on load).
3. Open the browser console for syntax errors. If you find a broken diagram, please open a PR.

## Editorial

### Voice consistency

The book is written in first person, opinionated, direct. The voice varies slightly across chapters — some chapters are more conversational (early chapters, written first), others are more clinical (later chapters, written under batch pressure). A future pass will normalize the voice. The substance is consistent; the tone is uneven.

### Anchor links

The book uses many cross-references (`[Ch 4](../ai-eng-director/chapter-04.html)`). All cross-references are absolute within the published site. mdBook anchors are auto-generated from headings. If a heading is renamed, the anchor changes — and any cross-reference to the old anchor breaks. The book has been tested end-to-end, but if you find a broken link, please open a PR.

## Areas the author would change in v2

1. **Add a "Director's Day in the Life" chapter.** The book describes decisions and frameworks, but not the texture of the day. A v2 chapter would describe a typical Monday at a Director seat.
2. **Add a "First 90 Days: A Real Story" chapter.** The 30/60/90 chapter (Ch 26) is a simulation. A real story with real names (anonymized) would be more memorable.
3. **Add a "Reading List" chapter.** The book has internal cross-references but no external reading list. A v2 chapter would list the books, papers, and blogs the author found most useful in writing this book.
4. **Add a "Common Objections" chapter.** The book makes recommendations. A v2 chapter would list the 10 most common objections a Director will hear from CEO/CTO/board and how to address them.
5. **Refresh Chapters 5–9 every 6 months.** AI models, eval practices, and platform tooling move fast. The fundamentals in Ch 5–9 are durable, but specific tool recommendations will drift.
6. **Add a "M&A and AI" chapter.** When companies acquire AI features, the integration patterns are different. The book doesn't cover this.

## Contributing corrections

To report an erratum or propose a correction:

1. Open an issue at https://github.com/webmakin/career-playbooks/issues with the tag `errata`.
2. Include the chapter number, the specific claim, and the source of your correction.
3. PRs that fix errata are merged on a fast track.

The author reviews errata weekly.

— Mohammed Asif, June 2026