#!/usr/bin/env python3
"""Fail on unsafe unqualified ASE npm skill-installer commands.

The npm package named "skills" is maintained outside AgentSkillExchange. ASE-owned
docs may mention it only as a pinned optional third-party installer via:
  npm exec --package=skills@1.5.7 -- skills add agentskillexchange/skills ...
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

UNQUALIFIED = re.compile(r'\bnpx\s+skills\s+add\s+agentskillexchange/skills\b')
SKIP_PARTS = {
    '.git', 'node_modules', '.trash', '__pycache__',
    'skills',  # upstream skill bodies may document their own third-party installers
}
DEFAULT_EXTS = {'.md', '.py', '.sh', '.js', '.json', '.txt'}


def should_scan(path: Path) -> bool:
    if any(part in SKIP_PARTS for part in path.parts):
        return False
    return path.is_file() and path.suffix in DEFAULT_EXTS


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('roots', nargs='*', default=['.'])
    args = parser.parse_args()

    failures: list[str] = []
    for root_arg in args.roots:
        root = Path(root_arg)
        if not root.exists():
            continue
        for path in root.rglob('*'):
            if not should_scan(path):
                continue
            try:
                text = path.read_text(errors='replace')
            except Exception:
                continue
            for lineno, line in enumerate(text.splitlines(), 1):
                if UNQUALIFIED.search(line):
                    failures.append(f'{path}:{lineno}: {line.strip()}')

    if failures:
        print('Unsafe unqualified ASE npx skills installer command(s) found:', file=sys.stderr)
        print('\n'.join(failures), file=sys.stderr)
        print(
            '\nUse OpenClaw clawhub install <slug>, direct repo/manual instructions, or the pinned '
            'optional third-party form: npm exec --package=skills@1.5.7 -- skills add ...',
            file=sys.stderr,
        )
        return 1

    print('Install command check passed: no unsafe unqualified ASE npm installer commands found.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

