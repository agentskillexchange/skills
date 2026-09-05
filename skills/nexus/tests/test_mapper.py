"""Synthetic temporary fixtures only; no user repository data."""
import importlib.util
import os
import pathlib
import stat
import tempfile
import unittest

SCRIPT = pathlib.Path(__file__).resolve().parents[1] / "scripts" / "map_directory.py"
SPEC = importlib.util.spec_from_file_location("mapper", SCRIPT)
mapper = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mapper)


class MapperTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = pathlib.Path(self.temp.name)
        self.root = self.base / "synthetic"
        self.root.mkdir()
        self.output = self.base / "map.md"

    def test_top_level_only_and_no_values(self):
        (self.root / "a.py").write_text(
            "class Widget:\n    def hidden(self): pass\n"
            "async def go(a, /, b='PRIVATE_LITERAL', *, flag=True, **kw):\n"
            "    def nested(): pass\n", encoding="utf-8")
        mapper.map_directory_structure(self.root, self.output)
        result = self.output.read_text()
        self.assertIn("class Widget:", result)
        self.assertIn("go(a, b, *, flag, **kw)", result)
        for omitted in ("hidden(self)", "nested()", "PRIVATE_LITERAL"):
            self.assertNotIn(omitted, result)

    def test_exclusions_symlinks_sorting_and_connector(self):
        (self.root / "z.py").write_text("def last(): pass\n")
        (self.root / "a.py").write_text("def first(): pass\n")
        (self.root / "src").mkdir()
        (self.root / "src" / "ok.py").write_text("pass\n")
        (self.root / ".env").write_text("SYNTHETIC=hidden")
        (self.root / "secret_config.py").write_text("def private(): pass\n")
        (self.root / "node_modules").mkdir()
        (self.root / "linked").symlink_to(self.root, target_is_directory=True)
        mapper.map_directory_structure(self.root, self.output)
        result = self.output.read_text()
        self.assertLess(result.index("src/"), result.index("a.py"))
        self.assertLess(result.index("a.py"), result.index("z.py"))
        self.assertIn("└── z.py", result)
        for omitted in (".env", "secret_config", "node_modules", "linked"):
            self.assertNotIn(omitted, result)

    def test_parse_error_does_not_echo_source(self):
        (self.root / "broken.py").write_text("PRIVATE_MARKER = (\n")
        mapper.map_directory_structure(self.root, self.output)
        result = self.output.read_text()
        self.assertIn("SyntaxError", result)
        self.assertNotIn("PRIVATE_MARKER", result)

    def test_byte_limit_and_extra_exclusions(self):
        (self.root / "large.py").write_text("x = 1\n" * 10)
        (self.root / "omit.py").write_text("pass")
        mapper.map_directory_structure(self.root, self.output,
                                       ignore_files=["omit.py"], max_source_bytes=10)
        result = self.output.read_text()
        self.assertIn("exceeds byte limit", result)
        self.assertNotIn("omit.py", result)

    def test_output_must_be_new_and_outside_root(self):
        self.output.write_text("keep")
        with self.assertRaises(FileExistsError):
            mapper.map_directory_structure(self.root, self.output)
        self.assertEqual(self.output.read_text(), "keep")
        with self.assertRaises(ValueError):
            mapper.map_directory_structure(self.root, self.root / "map.md")

    def test_invalid_root_and_limit(self):
        with self.assertRaises(FileNotFoundError):
            mapper.map_directory_structure(self.root / "absent", self.output)
        with self.assertRaises(ValueError):
            mapper.map_directory_structure(self.root, self.output, max_source_bytes=0)

    @unittest.skipUnless(os.name == "posix", "POSIX permission semantics")
    def test_private_output_even_with_permissive_umask(self):
        previous_mask = os.umask(0o022)
        try:
            mapper.map_directory_structure(self.root, self.output)
        finally:
            os.umask(previous_mask)
        self.assertEqual(stat.S_IMODE(self.output.stat().st_mode), 0o600)


if __name__ == "__main__":
    unittest.main()
