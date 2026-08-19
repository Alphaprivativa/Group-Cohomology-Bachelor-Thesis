#!/usr/bin/env python3
"""Mark links that point outside the export as unresolved.

The web edition is exported from an Obsidian vault that is much larger than the
thesis. Notes in the thesis link out to notes that were not exported, so the
plugin emits <a class="internal-link"> anchors whose href resolves to nothing
and which return 404 when clicked.

This script rewrites exactly those anchors into Obsidian's own "unresolved
link" form: the href, target and rel attributes are dropped and the class gains
"is-unresolved", which the exported obsidian.css already styles as dimmed,
non-clickable text. The link text and the tooltip are kept, so the reader still
sees which notion is being referenced.

Anchors whose target exists are left untouched, so the script is idempotent and
safe to re-run after every export:

    python tools/mark-unresolved-links.py main_HTML_ENG
"""

import re
import sys
import urllib.parse
from pathlib import Path

ANCHOR = re.compile(r'<a\b[^>]*\bclass="internal-link"[^>]*>', re.IGNORECASE)
HREF = re.compile(r'\shref="([^"]*)"', re.IGNORECASE)
DROP = re.compile(r'\s(?:href|target|rel)="[^"]*"', re.IGNORECASE)


def resolves(href: str, root: Path) -> bool:
    """True if href points at a file that actually exists in the export."""
    if not href or href.startswith(("http://", "https://", "#", "mailto:", "data:")):
        return True
    path = urllib.parse.unquote(href.split("#")[0].split("?")[0])
    return not path or (root / path).exists()


def rewrite(tag: str, root: Path) -> str:
    match = HREF.search(tag)
    if not match or resolves(match.group(1), root):
        return tag
    tag = DROP.sub("", tag)
    return tag.replace('class="internal-link"', 'class="internal-link is-unresolved"')


def main(argv: list[str]) -> int:
    root = Path(argv[1] if len(argv) > 1 else "main_HTML_ENG")
    if not root.is_dir():
        print(f"error: {root} is not a directory", file=sys.stderr)
        return 1

    changed_files = 0
    changed_links = 0
    for page in sorted(root.glob("*.html")):
        source = page.read_text(encoding="utf-8")
        count = 0

        def replace(match: re.Match) -> str:
            nonlocal count
            new = rewrite(match.group(0), root)
            if new != match.group(0):
                count += 1
            return new

        result = ANCHOR.sub(replace, source)
        if count:
            page.write_text(result, encoding="utf-8", newline="")
            changed_files += 1
            changed_links += count
            print(f"  {count:3d}  {page.name}")

    print(f"marked {changed_links} unresolved link(s) in {changed_files} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
