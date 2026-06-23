#!/usr/bin/env python3
"""
score_drill.py — Score a self-assessment rubric against a filled-in drill.

Usage:
    python3 score_drill.py --rubric <chapter.md>
    python3 score_drill.py --scores <scores.json>
    python3 score_drill.py --fixture

Exit codes:
    0  score computed
    1  input could not be parsed
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIXTURES = HERE / "fixtures"

PASS_THRESHOLD = 18
MIN_DIMENSION = 3


def parse_rubric_from_chapter(chapter_path: Path) -> list[dict]:
    text = chapter_path.read_text(encoding="utf-8")
    sec9_match = re.search(
        r"^#{2,6}\s+9\s*\.\s+Self-Assessment Rubric\s*\n(.*?)(?=^#{2,6}\s+\d{1,2}\s*\.?\s+|\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    )
    if not sec9_match:
        raise ValueError(f"No Section 9 (Self-Assessment Rubric) found in {chapter_path}")
    sec9 = sec9_match.group(1)

    rows = []
    for line in sec9.splitlines():
        m = re.match(r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", line)
        if m:
            rows.append({
                "n": int(m.group(1)),
                "dimension": m.group(2).strip(),
                "anchor_1": m.group(3).strip(),
                "anchor_3": m.group(4).strip(),
                "anchor_5": m.group(5).strip(),
            })
    return rows


def load_scores_json(scores_path: Path) -> dict[str, int]:
    data = json.loads(scores_path.read_text(encoding="utf-8"))
    out = {}
    for k, v in data.items():
        if not isinstance(v, int) or v < 1 or v > 5:
            raise ValueError(f"Score for {k!r} must be an int 1-5; got {v!r}")
        out[k] = v
    return out


def score_against_rubric(rubric: list[dict], scores: dict[str, int]) -> tuple[int, list[tuple[dict, int | None]]]:
    per_dim: list[tuple[dict, int | None]] = []
    total = 0
    for r in rubric:
        matched = None
        for key, val in scores.items():
            if key.lower() in r["dimension"].lower() or r["dimension"].lower() in key.lower():
                matched = val
                break
        if matched is not None:
            total += matched
        per_dim.append((r, matched))
    return total, per_dim


def render_report(total: int, per_dim: list[tuple[dict, int | None]]) -> None:
    avg = total / len(per_dim) if per_dim else 0.0
    min_dim = min((s for _, s in per_dim if s is not None), default=0)
    result = "PASS" if total >= PASS_THRESHOLD and min_dim >= MIN_DIMENSION else "FAIL"
    print(f"Score breakdown (out of {len(per_dim) * 5}):")
    for r, s in per_dim:
        flag = "" if s is None else " (ok)" if s >= MIN_DIMENSION else " (BELOW MIN)"
        print(f"  {r['n']}. {r['dimension']}: {s if s is not None else 'unscored'}{flag}")
    print(f"\nTotal: {total}/{len(per_dim) * 5}")
    print(f"Average: {avg:.2f}/5")
    print(f"Result: {result} (pass: total >= {PASS_THRESHOLD} and no dimension < {MIN_DIMENSION})")


def main() -> int:
    parser = argparse.ArgumentParser(description="Score a self-assessment rubric.")
    parser.add_argument("--rubric", type=Path, help="Chapter .md file to parse the rubric from.")
    parser.add_argument("--scores", type=Path, help="JSON file with pre-filled scores.")
    parser.add_argument("--fixture", action="store_true", help="Use bundled fixtures.")
    args = parser.parse_args()

    if args.fixture:
        rubric_path = FIXTURES / "sample-chapter.md"
        scores_path = FIXTURES / "sample-scores.json"
    else:
        rubric_path = args.rubric
        scores_path = args.scores

    if not rubric_path:
        print("score_drill: must provide --rubric <chap.md> or --fixture", file=sys.stderr)
        return 1
    if not scores_path:
        print("score_drill: must provide --scores <scores.json> or --fixture", file=sys.stderr)
        return 1

    try:
        rubric = parse_rubric_from_chapter(rubric_path)
        scores = load_scores_json(scores_path)
    except (ValueError, json.JSONDecodeError) as e:
        print(f"score_drill: parse error: {e}", file=sys.stderr)
        return 1

    if not rubric:
        print(f"score_drill: no rubric rows found in {rubric_path}", file=sys.stderr)
        return 1

    total, per_dim = score_against_rubric(rubric, scores)
    render_report(total, per_dim)
    return 0


if __name__ == "__main__":
    sys.exit(main())