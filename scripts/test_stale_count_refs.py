"""Regression coverage for obsolete count matching in generated files."""
import runpy
import tempfile
import unittest
from pathlib import Path


CHECK = runpy.run_path(str(Path(__file__).with_name("apply-frontmatter-verification-overlay.py")))["stale_count_refs"]


class StaleCountTests(unittest.TestCase):
    def test_stale_counts_remain_blocked(self):
        for text in ('Published: 2466 skills', '2,466 skills', 'badge/2%2C466', '{"total": 2466}'):
            with self.subTest(text=text), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                (root / 'README.md').write_text(text)
                self.assertEqual(len(CHECK(root)), 1)

    def test_larger_metrics_do_not_match(self):
        for value in (32466313, 12466, 24660, 124660):
            with self.subTest(value=value), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                (root / 'skills.json').write_text('{"npm_weekly_downloads": %d}' % value)
                self.assertEqual(CHECK(root), [])

    def test_reports_file_and_line(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'CATALOG.md').write_text('Catalog\nPublished: 2,466 skills\n')
            self.assertEqual(CHECK(root), ['CATALOG.md:2:Published: 2,466 skills'])


if __name__ == '__main__':
    unittest.main()
