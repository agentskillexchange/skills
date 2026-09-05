import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from install import install
from release import build, checked_files, FILES


class ReleaseTests(unittest.TestCase):
    def test_archive_repeatable_and_manifest_valid(self):
        with tempfile.TemporaryDirectory() as d:
            first = build(ROOT, Path(d) / 'first')
            second = build(ROOT, Path(d) / 'second')
            self.assertEqual(first['sha256'], second['sha256'])
            with zipfile.ZipFile(first['archive']) as z:
                self.assertEqual(set(z.namelist()), {'reconnect/' + n for n in FILES} | {'reconnect/MANIFEST.sha256'})
                for line in z.read('reconnect/MANIFEST.sha256').decode().splitlines():
                    sha, name = line.split('  ', 1)
                    self.assertEqual(sha, hashlib.sha256(z.read('reconnect/' + name)).hexdigest())

    def test_extracted_release_installs_and_demo_runs(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            package = build(ROOT, d / 'dist')
            with zipfile.ZipFile(package['archive']) as z:
                z.extractall(d / 'unpacked')
            source = d / 'unpacked/reconnect'
            target = d / 'skills/reconnect'
            subprocess.run([sys.executable, str(source / 'scripts/install.py'), '--target', str(target)], check=True, capture_output=True)
            def command(*args):
                p = subprocess.run([sys.executable, str(target / 'scripts/reconnect.py'), '--db', str(d / 'demo.sqlite3'), *args], check=True, capture_output=True, text=True)
                return json.loads(p.stdout)
            self.assertEqual(command('import', '--input', str(source / 'examples/candidates.json'))['imported_rows'], 2)
            self.assertEqual(command('prepare', '--batch', 'demo', '--size', '2')['count'], 2)
            self.assertEqual(command('prepare', '--batch', 'next', '--size', '2')['count'], 0)
            self.assertEqual(command('status')['active_reservations'], 2)
            self.assertTrue((target / 'LICENSE').is_file())

    def test_install_refuses_existing_directory(self):
        with tempfile.TemporaryDirectory() as d:
            target = Path(d) / 'installed'
            install(ROOT, target)
            before = (target / 'SKILL.md').read_bytes()
            with self.assertRaises(FileExistsError):
                install(ROOT, target)
            self.assertEqual(before, (target / 'SKILL.md').read_bytes())

    def test_unlisted_data_never_enters_archive(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            source = d / 'source'
            source.mkdir()
            for name in FILES:
                path = source / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes((ROOT / name).read_bytes())
            (source / 'private.sqlite3').write_bytes(b'private fixture')
            package = build(source, d / 'dist')
            with zipfile.ZipFile(package['archive']) as z:
                self.assertFalse(any('private.sqlite3' in n for n in z.namelist()))

    def test_private_path_and_symlink_are_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            source = Path(d) / 'source'
            source.mkdir()
            for name in FILES:
                path = source / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes((ROOT / name).read_bytes())
            readme = source / 'README.md'
            readme.write_text('Private fixture: /Us' + 'ers/example/private-data')
            with self.assertRaises(ValueError):
                checked_files(source)
            readme.unlink()
            readme.symlink_to(ROOT / 'README.md')
            with self.assertRaises(ValueError):
                checked_files(source)


if __name__ == '__main__':
    unittest.main()
