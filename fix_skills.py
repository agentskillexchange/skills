from pathlib import Path
from urllib.parse import urlparse
import re
import yaml
import json

ROOT = Path(__file__).resolve().parent
SKILLS = sorted(ROOT.glob('skills/*/SKILL.md'))

STANDARD_INSTALL = """## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment
"""

REQUIRED_ORDER = [
    'title',
    'description',
    'verification',
    'source',
    'category',
    'framework',
    'tool_ecosystem',
]

NUMERIC_SIGNAL_FIELDS = {'github_stars', 'npm_weekly_downloads'}


def parse_frontmatter(text: str):
    m = re.match(r'^---\n(.*?)\n---\n?', text, re.S)
    if not m:
        raise ValueError('missing frontmatter')
    fm = yaml.safe_load(m.group(1)) or {}
    body = text[m.end():]
    return fm, body


def dump_frontmatter(data):
    ordered = {}
    for key in REQUIRED_ORDER:
        if key in data and data[key] not in (None, {}, []):
            ordered[key] = data[key]
    for key, value in data.items():
        if key not in ordered and value not in (None, {}, []):
            ordered[key] = value
    rendered = yaml.safe_dump(ordered, sort_keys=False, allow_unicode=True).strip()
    return f"---\n{rendered}\n---\n\n"


def classify_source(url: str):
    try:
        parsed = urlparse(url)
    except Exception:
        return {'kind': 'other', 'url': url}
    host = (parsed.netloc or '').lower()
    path = parsed.path or ''
    parts = [p for p in path.split('/') if p]
    if host in {'github.com', 'www.github.com'} and len(parts) >= 2:
        repo = f"{parts[0]}/{parts[1]}"
        is_subpath = len(parts) > 2
        return {'kind': 'github', 'url': url, 'repo': repo, 'is_subpath': is_subpath}
    if host in {'www.npmjs.com', 'npmjs.com'} and '/package/' in path:
        pkg = path.split('/package/', 1)[1].strip('/')
        return {'kind': 'npm', 'url': url, 'package': pkg}
    if 'agentskillexchange.com' in host:
        return {'kind': 'ase', 'url': url}
    return {'kind': 'other', 'url': url}


def normalize_list(value):
    if isinstance(value, list):
        return [str(v).strip() for v in value if str(v).strip()]
    if value is None:
        return []
    s = str(value).strip()
    return [s] if s else []


def source_block(url: str):
    meta = classify_source(url)
    if meta['kind'] == 'github':
        label = 'GitHub'
    elif meta['kind'] == 'npm':
        label = 'npm'
    elif meta['kind'] == 'ase':
        label = 'Agent Skill Exchange'
    else:
        label = 'Source'
    return f"## Source\n\n- [{label}]({url})\n"


stats = {
    'files_changed': 0,
    'verification_mapped_to_listed': 0,
    'install_normalized': 0,
    'source_section_normalized': 0,
    'signal_integrity_mismatches_removed': 0,
    'source_aligned_npm_download_blocks_preserved': 0,
    'tool_ecosystem_removed': 0,
}

for path in SKILLS:
    original = path.read_text()
    fm, body = parse_frontmatter(original)

    changed = False
    source = str(fm.get('source', '')).strip()
    source_meta = classify_source(source)

    verification = str(fm.get('verification', '')).strip()
    if verification == 'verified_metadata':
        fm['verification'] = 'listed'
        stats['verification_mapped_to_listed'] += 1
        changed = True

    for key in ('category', 'framework'):
        normalized = normalize_list(fm.get(key))
        if fm.get(key) != normalized:
            fm[key] = normalized
            changed = True

    te = fm.get('tool_ecosystem')
    if te is not None and not isinstance(te, dict):
        te = {}
        fm['tool_ecosystem'] = te
        changed = True

    if isinstance(te, dict):
        github_repo = te.get('github_repo')
        npm_package = te.get('npm_package')
        preserved_npm_download_block = False
        mismatch = False

        if source_meta['kind'] == 'github':
            source_repo = source_meta['repo']
            if github_repo and github_repo != source_repo:
                mismatch = True
                for key in ['github_repo', 'github_stars', 'npm_weekly_downloads']:
                    if key in te:
                        te.pop(key, None)
                        changed = True
                stats['signal_integrity_mismatches_removed'] += 1
            else:
                if source_meta['is_subpath'] and 'npm_weekly_downloads' in te:
                    te.pop('npm_weekly_downloads', None)
                    changed = True
                    stats['signal_integrity_mismatches_removed'] += 1
                elif (not source_meta['is_subpath']) and github_repo == source_repo and npm_package and 'npm_weekly_downloads' in te:
                    preserved_npm_download_block = True
        elif source_meta['kind'] == 'npm':
            source_pkg = source_meta['package']
            if npm_package and npm_package != source_pkg:
                mismatch = True
                removed_any = False
                for key in ['npm_package', 'npm_weekly_downloads']:
                    if key in te:
                        te.pop(key, None)
                        changed = True
                        removed_any = True
                if removed_any:
                    stats['signal_integrity_mismatches_removed'] += 1
        else:
            if 'npm_weekly_downloads' in te and ('npm_package' not in te or source_meta['kind'] != 'ase'):
                # Prefer omission when the numeric source is unclear outside ASE/root-repo cases.
                te.pop('npm_weekly_downloads', None)
                changed = True
                stats['signal_integrity_mismatches_removed'] += 1

        if preserved_npm_download_block:
            stats['source_aligned_npm_download_blocks_preserved'] += 1

        if not te:
            fm.pop('tool_ecosystem', None)
            stats['tool_ecosystem_removed'] += 1
            changed = True

    title = str(fm.get('title', '')).strip()
    description = str(fm.get('description', '')).strip()
    heading_match = re.search(r'^#\s+(.+?)\s*$', body, re.M)
    if heading_match and heading_match.group(1).strip() != title:
        body = body[:heading_match.start()] + f"# {title}" + body[heading_match.end():]
        changed = True

    para_match = re.search(r'^#\s+.+?\n\n(.+?)\n(?=##\s)', body, re.S | re.M)
    if para_match and para_match.group(1).strip() != description:
        body = body[:para_match.start(1)] + description + body[para_match.end(1):]
        changed = True

    install_re = re.compile(r'## Installation\n.*?(?=\n## |\Z)', re.S)
    install_match = install_re.search(body)
    if not install_match or install_match.group(0).strip() != STANDARD_INSTALL.strip():
        replacement = STANDARD_INSTALL.rstrip() + '\n\n'
        if install_match:
            body = body[:install_match.start()] + replacement + body[install_match.end():]
        else:
            if not body.endswith('\n'):
                body += '\n'
            body += '\n' + replacement
        stats['install_normalized'] += 1
        changed = True

    source_re = re.compile(r'## Source\n.*?(?=\n## |\Z)', re.S)
    desired_source = source_block(source).rstrip() + '\n'
    source_match = source_re.search(body)
    if not source_match or source_match.group(0).strip() != desired_source.strip():
        if source_match:
            body = body[:source_match.start()] + desired_source + body[source_match.end():]
        else:
            if not body.endswith('\n'):
                body += '\n'
            body += '\n' + desired_source
        stats['source_section_normalized'] += 1
        changed = True

    body = re.sub(r'\n{3,}', '\n\n', body).rstrip() + '\n'
    new_text = dump_frontmatter(fm) + body
    if new_text != original:
        path.write_text(new_text)
        stats['files_changed'] += 1

print(json.dumps(stats, indent=2, sort_keys=True))
