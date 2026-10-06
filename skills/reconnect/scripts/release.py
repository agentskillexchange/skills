#!/usr/bin/env python3
"""Build a deterministic, allowlisted release ZIP with file and archive checksums."""
import argparse
import ast
import hashlib
import json
from pathlib import Path
import re
import zipfile


FILES = (
    '.gitignore', 'VERSION', 'README.md', 'LICENSE', 'SKILL.md',
    'agents/openai.yaml', 'references/network-plan.md', 'references/discovery.md',
    'references/tracking.md', 'references/linkedin.md', 'examples/candidates.json',
    'docs/release-notes.md', 'scripts/reconnect.py', 'scripts/test_reconnect.py',
    'scripts/install.py', 'scripts/release.py', 'tests/test_release.py',
)


def checked_files(root):
    root = Path(root).resolve()
    result = {}
    # Construct markers without embedding actual credentials or private paths in the package.
    forbidden = [r'/Us' + r'ers/[^\s]+', r'/ho' + r'me/[^\s]+',
                 r'archiv' + r'um://', r'-----BEGIN ' + r'(?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
                 r'gh' + r'[pousr]_[A-Za-z0-9]{30,}', r'github_' + r'pat_[A-Za-z0-9_]{30,}']
    for name in FILES:
        path = root / name
        if not path.is_file() or path.is_symlink() or root not in path.resolve().parents:
            raise ValueError('Missing or unsafe release input: ' + name)
        data = path.read_bytes()
        text = data.decode('utf-8')
        if '\x00' in text or any(re.search(pattern, text) for pattern in forbidden):
            raise ValueError('Private-data or credential marker in ' + name)
        if name.endswith('.py'):
            ast.parse(text, filename=name)
        elif name.endswith('.json'):
            json.loads(text)
        result[name] = data
    return result


def build(root, output):
    root, output = Path(root).resolve(), Path(output).resolve()
    payload = checked_files(root)
    version = payload['VERSION'].decode().strip()
    if not re.fullmatch(r'\d+\.\d+\.\d+(?:-[a-z0-9.]+)?', version):
        raise ValueError('Invalid VERSION')
    output.mkdir(parents=True, exist_ok=True)
    archive = output / ('reconnect-' + version + '.zip')
    manifest = ''.join(hashlib.sha256(data).hexdigest() + '  ' + name + '\n'
                       for name, data in sorted(payload.items())).encode()
    payload['MANIFEST.sha256'] = manifest
    with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for name, data in sorted(payload.items()):
            entry = zipfile.ZipInfo('reconnect/' + name, date_time=(2026, 1, 1, 0, 0, 0))
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            entry.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(entry, data)
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    checksum = archive.with_suffix('.zip.sha256')
    checksum.write_text(digest + '  ' + archive.name + '\n')
    return {'archive': str(archive), 'checksum': str(checksum), 'sha256': digest,
            'files': len(payload), 'bytes': archive.stat().st_size}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', required=True)
    args = parser.parse_args()
    try:
        print(json.dumps(build(Path(__file__).resolve().parents[1], args.output_dir), indent=2))
    except (ValueError, OSError) as error:
        parser.exit(1, 'reconnect release: ' + str(error) + '\n')
