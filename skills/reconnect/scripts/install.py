#!/usr/bin/env python3
"""Install the skill into an explicit new directory. Never overwrite an installation."""
import argparse
from pathlib import Path
import shutil


FILES = (
    'SKILL.md', 'LICENSE', 'agents/openai.yaml', 'scripts/reconnect.py',
    'references/network-plan.md', 'references/discovery.md',
    'references/tracking.md', 'references/linkedin.md',
)


def install(source, target):
    source, target = Path(source).resolve(), Path(target).expanduser().absolute()
    if target.exists() or target.is_symlink():
        raise FileExistsError('Target exists; choose a new path or back up your installation first')
    if source == target or source in target.parents:
        raise ValueError('Install outside the release source directory')
    for name in FILES:
        path = source / name
        if not path.is_file() or path.is_symlink() or source not in path.resolve().parents:
            raise ValueError('Missing or unsafe source file: ' + name)
    target.parent.mkdir(parents=True, exist_ok=True)
    # Reserve the destination exclusively; never rename over a concurrently created target.
    target.mkdir()
    try:
        for name in FILES:
            dest = target / name
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source / name, dest)
    except Exception:
        # Retain partial content for inspection rather than deleting an uncertain target.
        raise RuntimeError('Installation incomplete; inspect the newly created target before retrying')
    return target


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target', required=True)
    args = parser.parse_args()
    try:
        print(install(Path(__file__).resolve().parents[1], args.target))
    except (ValueError, OSError, RuntimeError) as error:
        parser.exit(1, 'reconnect install: ' + str(error) + '\n')
