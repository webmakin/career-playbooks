# Figure Style Guide

> Conventions for every diagram in every playbook.
> Version: 1.0.0 — 2026-06-23.

Diagrams are first-class content. A chapter without a figure is incomplete. This guide is the contract every diagram follows.

## When to include a figure

- Section 4 (Mental Models): **always** at least one Mermaid diagram.
- Section 5 (Frameworks): include if the framework has a flow or decision tree.
- Section 7 (Worked Example): optional, but a comparison diagram (before/after) is high-leverage.
- Section 8 (Failure Mode Postmortem): optional, a timeline or flow chart helps.

## Mermaid conventions

All diagrams use Mermaid (renders inline as SVG in mdBook).

**Naming:** `%% Figure N.M — short title` comment on the line above the diagram. N = chapter, M = figure number within the chapter.

**Style:** default Mermaid theme is fine. Avoid heavy color customization (mdBook's CSS may override).

**Layout:**
- Use `flowchart TB` or `flowchart LR` (not `graph`).
- Use square brackets for nodes, parentheses for rounded, double-square for subroutines.
- Keep node labels short (≤5 words).
- Maximum ~10 nodes per diagram. If you need more, split into multiple diagrams.

**Forbidden:** pie charts with >7 slices (unreadable), sequence diagrams with >5 participants (noisy), state machines with >8 states (use multiple diagrams).

## ASCII art (fallback)

If Mermaid can't express the diagram, use a fenced ` ``` ` block with monospace ASCII. Keep it ≤20 lines and ≤80 columns.

## Color and styling

mdBook renders the Mermaid SVGs. Don't override colors — let the theme handle it.

## Examples of "good figure" vs "bad figure"

**Bad figure:** a 25-node graph of "AI capabilities." Unreadable.
**Good figure:** a 5-node Mermaid flowchart of "The 5-layer data stack."

**Bad figure:** a pie chart of cost percentages with 12 slices.
**Good figure:** a 5-bar chart showing cost per request across 5 vendors.

## Versioning

Figures are tied to the chapter version. Don't reuse a Mermaid diagram across chapters without naming it explicitly in each chapter's "Mental Models" section.