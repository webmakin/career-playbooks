#!/usr/bin/env python3
"""
publish.py — Mirror a role playbook's chapters/ into src/<slug>/.

Usage:
    python3 publish.py --role <role-name>
    python3 publish.py --all
    python3 publish.py --all --only chapters,templates

Exit codes:
    0  all bootstrapped roles mirrored successfully
    1  a bootstrapped role failed to mirror

Not-yet-bootstrapped roles (e.g. staff-engineer-playbook before its
chapters dir exists) are gracefully skipped. This is intentional.

The mirror operation:
  - Reads <role>/chapters/chap-N.md (canonical)
  - Writes to src/<slug>/chapter-NN.md (zero-padded, mdBook convention)
  - Mirrors <role>/templates/ and <role>/diagrams/ as-is
  - Mirrors <role>/README.md → src/<slug>/README.md

Why zero-pad? mdBook's SUMMARY.md and the rendered HTML use `chapter-NN.html`
(two-digit). The canonical source uses `chap-N.md` (one-digit) for typing-speed
reasons. publish.py is the seam.
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
BOOK_SRC = REPO_ROOT / "src"

SLUG_MAP: dict[str, str] = {
    "AI-eng-dir-playbook":              "ai-eng-director",
    "engineering-director-playbook":    "engineering-director",
    "VP-eng-playbook":                  "vp-engineering",
    "vp-engineering-playbook":          "vp-engineering",
    "principal-ai-scientist-playbook":  "principal-ai-scientist",
    "ml-researcher-playbook":           "ml-researcher",
    "ai-engineer-playbook":             "ai-engineer",
    "staff-engineer-playbook":          "staff-engineer",
}

# Subdirs to mirror as-is (no rename, no zero-padding)
PASSTHROUGH_SUBDIRS = ["templates", "diagrams"]


def chapter_dest_name(src_name: str) -> str | None:
    """Map canonical `chap-N.md` -> rendered `chapter-NN.md`. Returns None if not a chapter."""
    m = re.match(r"^chap-(\d+)\.md$", src_name)
    if not m:
        return None
    n = int(m.group(1))
    return f"chapter-{n:02d}.md"


def mirror_role(role_name: str, only: list[str] | None) -> tuple[int, int, bool]:
    role_dir = REPO_ROOT / role_name
    if not role_dir.exists():
        print(f"publish: role dir not found: {role_dir} (skipped)")
        return 0, 0, True

    slug = SLUG_MAP.get(role_name)
    if not slug:
        print(f"publish: unknown role {role_name!r} (skipped)", file=sys.stderr)
        return 0, 0, True

    dest_root = BOOK_SRC / slug
    dest_root.mkdir(parents=True, exist_ok=True)

    copied = 0
    failed = 0

    # Mirror chapters: chap-N.md -> chapter-NN.md at the dest root.
    if only is None or "chapters" in only:
        src_chapters = role_dir / "chapters"
        if src_chapters.exists():
            for src_file in sorted(src_chapters.glob("chap-*.md")):
                dst_name = chapter_dest_name(src_file.name)
                if dst_name is None:
                    continue
                dst_file = dest_root / dst_name
                try:
                    shutil.copy2(src_file, dst_file)
                    copied += 1
                except OSError as e:
                    print(f"publish: failed to copy {src_file} -> {dst_file}: {e}", file=sys.stderr)
                    failed += 1
            print(f"publish: {role_name}/chapters -> {slug}/  ({copied} chapters copied)")
        else:
            print(f"publish: {role_name}/chapters -> {slug}/  (no chapters dir, skipped)")

    # Passthrough subdirs (templates, diagrams)
    for sub in PASSTHROUGH_SUBDIRS:
        if only is not None and sub not in only:
            continue
        src_sub = role_dir / sub
        if not src_sub.exists():
            continue
        dest_sub = dest_root / sub
        dest_sub.mkdir(parents=True, exist_ok=True)
        sub_copied = 0
        for src_file in src_sub.rglob("*"):
            if not src_file.is_file():
                continue
            rel = src_file.relative_to(src_sub)
            dst_file = dest_sub / rel
            dst_file.parent.mkdir(parents=True, exist_ok=True)
            try:
                shutil.copy2(src_file, dst_file)
                sub_copied += 1
            except OSError as e:
                print(f"publish: failed to copy {src_file} -> {dst_file}: {e}", file=sys.stderr)
                failed += 1
        copied += sub_copied
        print(f"publish: {role_name}/{sub} -> {slug}/{sub}/  ({sub_copied} copied)")

    # Mirror README.md
    src_readme = role_dir / "README.md"
    if src_readme.exists():
        dst_readme = dest_root / "README.md"
        try:
            shutil.copy2(src_readme, dst_readme)
            copied += 1
        except OSError as e:
            print(f"publish: failed to copy README: {e}", file=sys.stderr)
            failed += 1

    return copied, failed, False


def main() -> int:
    parser = argparse.ArgumentParser(description="Mirror playbook prose into the mdBook source tree.")
    parser.add_argument("--role", type=str, help="Mirror a specific role (e.g. AI-eng-dir-playbook).")
    parser.add_argument("--all", action="store_true", help="Mirror every bootstrapped role.")
    parser.add_argument("--only", type=str, help="Comma-separated subdirs to mirror (default: all).")
    args = parser.parse_args()

    if not args.role and not args.all:
        print("publish: provide --role <name> or --all", file=sys.stderr)
        return 1

    only = [s.strip() for s in args.only.split(",")] if args.only else None
    roles = list(SLUG_MAP) if args.all else [args.role]

    total_copied = 0
    total_failed = 0
    for role in roles:
        c, f, _skipped = mirror_role(role, only)
        total_copied += c
        total_failed += f

    print(f"\npublish: {total_copied} file(s) copied, {total_failed} failed")
    return 0 if total_failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())