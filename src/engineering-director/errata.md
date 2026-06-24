# Engineering Director Playbook

## Errata & Known Issues

> **Honest accounting of what's incomplete, what might be wrong, and what the author would change in v2.** This page lists the things in this book that are known to be imperfect, incomplete, or wrong. Treat the rest of the book as accurate.

### What's incomplete

- **Chapter 28 (System Design Appendix) is an appendix, not a full chapter.** It introduces the 4-layer model + 3 quality attributes + 5-criterion bar + 11-step design review, but doesn't go deep on each. The VP-eng playbook has a fuller system design treatment. The ED should pair this appendix with system-design-specific reading (e.g., Alex Xu's *System Design Interview* series).

- **No case studies of real ED transitions.** The chapters describe what good EDs do, but don't include specific named case studies (e.g., "ED X did Y at company Z"). The author would add 5-10 named case studies in v2.

- **No coverage of remote vs in-person ED work.** All chapters assume a hybrid or in-person team. The book doesn't address remote-first ED-specific patterns. The author would add a chapter on remote ED leadership in v2.

### What might be wrong

- **The 60-20-20 org split is a heuristic, not a law.** Some EDs report 70-20-10 or 50-30-20 as better for their context. The book uses 60-20-20 because it's the most common ratio in team-topology literature, but it's not universal.

- **The 5-criterion quality bar (specific + measured + owned + timed + aligned) appears in many chapters with slightly different framings.** Some chapters add a 6th criterion (e.g., outcome, owned). The book uses 5 criteria consistently for the rubric, but the 5-criterion bar varies by chapter. This is intentional (different bars for different contexts) but could be confusing.

- **The 30/60/90 plan is one ED's approach, not THE ED approach.** Other EDs prefer 60/60/60 or 90-day sprint. The book uses 30/60/90 because it's the most common pattern, but readers should adapt.

### What the author would change in v2

- **Add a chapter on remote + hybrid ED leadership.** The book assumes in-person. v2 would add a chapter on remote-first EDs, distributed teams, async communication, and remote hiring.

- **Add a chapter on AI/ML-specific ED leadership.** This book is for any ED, not AI-specific. v2 would have a chapter on AI/ML org design, ML platform engineering, model lifecycle, and AI safety + governance.

- **Add case studies.** 5-10 named case studies of real ED transitions (with permission), including both successes and failures.

- **Tighten the 5-criterion bar.** The book uses different 5-criterion bars in different chapters. v2 would standardize on 1 of 3 bars (people bar, system bar, outcome bar) and apply consistently.

- **Add a chapter on ED-as-coach.** The book covers ED-as-system-builder but not ED-as-coach. Coaching EMs, coaching senior ICs, coaching the VP — these are different skills that deserve their own chapter.

- **Add a chapter on platform-specific ED patterns.** Some EDs run platform teams; others run product teams; some run both. v2 would have a chapter on platform-specific ED leadership.

### Known inaccuracies

- **Some chapter titles use slightly different terminology.** "Engineering Org Design at Scale" vs "Engineering Org Design" — both refer to the same concept (org design at the function level). The book uses "at scale" in the chapter title to signal the chapter's scope.

- **The TCO calculator in Chapter 16 uses sample numbers.** Real TCO depends on the specific decision. Use the calculator as a framework, not as a precise estimate.

- **Some Mermaid diagrams have visual artifacts.** mdBook's Mermaid renderer occasionally has issues with complex diagrams. The diagrams are correct in concept; the visual rendering may vary.

### Reporting errors

If you find an error, please open an issue at:
https://github.com/webmakin/career-playbooks/issues

Or submit a PR with the fix. The book is open source and community-maintained.

### Versioning

- **v1.0.0-ed** (2026-09-01) — Initial release. 28 chapters + preface + glossary + errata. 84 exercise bundle files.

Future versions:
- v1.1.0-ed — Bug fixes + community contributions.
- v1.2.0-ed — 5-10 named case studies.
- v2.0.0-ed — Remote + AI/ML chapters + tightened 5-criterion bar.

### Acknowledgments

This book was written by an ED (the author) for EDs (the readers). The author is not anonymous; the author is one of many EDs who have learned by doing, by failing, and by reading. The book is the synthesis of that learning.

If you're an ED who has read this far: thank you. The ED role is hard. The leverage is in the system, not in the heroics. Build the system. Hire the team. Run the playbook. The rest is execution.
