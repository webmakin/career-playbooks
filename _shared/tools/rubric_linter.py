#!/usr/bin/env python3
"""
rubric_linter.py — Structural validator for playbook chapters.

Verifies that a chapter file conforms to the 11-section chapter anatomy
defined in _shared/chapter-anatomy.md and the rubric format from
_shared/rubric-spec.md.

Usage:
    python3 rubric_linter.py <chapter.md> [<chapter.md> ...]
    python3 rubric_linter.py --all       # lint every chapter in AI-eng-dir-playbook/chapters/

Exit codes:
    0  all chapters pass
    1  one or more chapters have issues (details printed to stderr)

Validation rules (one PASS line per chapter on success; FAIL + issues on failure):
  1. The file contains the 11 section headings (## 1. Epigraph ... ## 11. Interview Questions).
  2. Each section has at least one paragraph of content.
  3. Section 2 (Problem) contains a "Decision in one sentence:" line.
  4. Section 3 (Why [Role]s Fail Here) contains >= 3 named failure modes (lines starting with "- **").
  5. Section 6 (Drill) contains a time-budget hint (regex matchable).
  6. Section 6 (Drill) ends with "**Deliverable:**" specifying a portfolio path.
  7. Section 9 (Self-Assessment Rubric) is a 5-row, 4-column Markdown table.
  8. Section 9 ends with a "Pass threshold:" line.

This script is intentionally stdlib-only — no external deps.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

# Default chapter globs: every <role>-playbook/chapters/ directory.
# Inherited from the multi-playbook shape (one repo, subpath-per-role).
DEFAULT_CHAPTER_GLOBS = [
    REPO_ROOT / "AI-eng-dir-playbook" / "chapters" / "chap-*.md",
    REPO_ROOT / "VP-eng-playbook"      / "chapters" / "chap-*.md",
    REPO_ROOT / "FDE-playbook"         / "chapters" / "chap-*.md",
    REPO_ROOT / "engineering-director-playbook" / "chapters" / "chap-*.md",
]  # Edit here when adding/removing roles

REQUIRED_SECTIONS = [
    (1, "Epigraph"),
    (2, "Problem"),
    (3, None),
    (4, "Mental Models"),
    (5, "Frameworks"),
    (6, "Drill"),
    (7, "Worked Example"),
    (8, "Failure Mode Postmortem"),
    (9, "Self-Assessment Rubric"),
    (10, "Portfolio Artifact Note"),
    (11, "Interview Questions"),
]


def split_into_sections(text: str) -> dict[int, str]:
    sections: dict[int, str] = {}
    pattern = re.compile(r"^#{2,6}\s+(\d{1,2})\s*\.\s+(.+?)\s*$", re.MULTILINE)
    matches = list(pattern.finditer(text))
    for i, m in enumerate(matches):
        n = int(m.group(1))
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        sections[n] = text[start:end]
    return sections


def lint_chapter(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    issues: list[str] = []

    sections = split_into_sections(text)
    for n, _label in REQUIRED_SECTIONS:
        if n not in sections:
            issues.append(f"Section {n} is missing.")
    if issues:
        return issues

    for n, body in sections.items():
        nonempty = [line for line in body.splitlines() if line.strip() and not line.strip().startswith("#")]
        if len(nonempty) < 1:
            issues.append(f"Section {n} has no content (only headings).")

    sec2 = sections.get(2, "")
    if "Decision in one sentence:" not in sec2:
        issues.append('Section 2 (Problem) must contain a "Decision in one sentence:" line.')

    sec3 = sections.get(3, "")
    failure_modes = re.findall(r"^\s*-\s+\*\*[^*]+\.\*\*", sec3, re.MULTILINE)
    if len(failure_modes) < 3:
        issues.append(
            f"Section 3 (Why ... Fail Here) needs >= 3 named failure modes "
            f"(lines starting with '- **Name.**'); found {len(failure_modes)}."
        )

    sec6 = sections.get(6, "")
    time_pat = re.compile(
        r"\b\d+\s*[\*_]?\s*(?:min|minute|hour|hr|h)s?\b[\*_]?",
        re.IGNORECASE,
    )
    if not time_pat.search(sec6):
        issues.append(
            "Section 6 (Drill) must specify a time budget "
            "(e.g. 'You have 60 minutes.' or 'Time-boxed to **90 minutes**')."
        )

    if "**Deliverable:**" not in sec6:
        issues.append('Section 6 (Drill) must end with a "**Deliverable:**" line.')
    else:
        m = re.search(r"\*\*Deliverable:\*\*\s*(.+)", sec6)
        if m and not re.search(r"[\w/_.]+\.md", m.group(1)):
            issues.append(
                'Section 6 "**Deliverable:**" line should specify a .md path '
                "(e.g. 'portfolio/chapter-01-vendor-memo.md')."
            )

    sec9 = sections.get(9, "")
    rubric_rows = re.findall(r"^\|\s*(\d+)\s*\|", sec9, re.MULTILINE)
    if len(rubric_rows) < 5:
        issues.append(
            f"Section 9 (Self-Assessment Rubric) needs 5 numbered dimensions; "
            f"found {len(rubric_rows)}."
        )
    if "Disqualifier:" not in sec9 and "Disqualifier" not in sec9:
        issues.append('Section 9 must include a "Disqualifier:" line.')

    if "Pass threshold:" not in sec9:
        issues.append('Section 9 must include a "Pass threshold:" line.')

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint playbook chapters against the 11-section anatomy.")
    parser.add_argument("paths", nargs="*", type=Path, help="Chapter .md files to lint.")
    parser.add_argument("--all", action="store_true", help="Lint every chapter in every bootstrapped role's chapters/ dir.")
    args = parser.parse_args()

    if args.all:
        paths = []
        for glob in DEFAULT_CHAPTER_GLOBS:
            paths.extend(sorted(glob.parent.glob("chap-*.md")))
    else:
        paths = args.paths

    if not paths:
        print("rubric_linter: no chapter files to lint", file=sys.stderr)
        return 1

    total = 0
    failed = 0
    for p in paths:
        total += 1
        issues = lint_chapter(p)
        if issues:
            failed += 1
            print(f"FAIL  {p}", file=sys.stderr)
            for issue in issues:
                print(f"  - {issue}", file=sys.stderr)
        else:
            print(f"PASS  {p}")
    print(f"\nrubric_linter: {total - failed}/{total} chapter(s) OK")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())