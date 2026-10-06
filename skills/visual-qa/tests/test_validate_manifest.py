"""Tests for the dependency-free Visual QA manifest validator."""

from __future__ import annotations

import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout


SCRIPT = Path(__file__).parents[1] / "scripts" / "validate_manifest.py"
SPEC = importlib.util.spec_from_file_location("validate_manifest", SCRIPT)
assert SPEC is not None
assert SPEC.loader is not None
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


def _entry(**overrides: object) -> dict[str, object]:
    value: dict[str, object] = {
        "label": "checkout-error-mobile-dark",
        "path": "qa-shots/checkout-error-mobile-dark.png",
        "flow": "checkout",
        "state": "error",
        "breakpoint": 320,
        "theme": "dark",
    }
    value.update(overrides)
    return value


class ManifestValidationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.root = Path(self.temporary_directory.name)

    def test_valid_manifest(self) -> None:
        self.assertEqual(
            VALIDATOR.validate_manifest([_entry()], root=self.root),
            [],
        )

    def test_top_level_must_be_nonempty_array(self) -> None:
        self.assertEqual(
            VALIDATOR.validate_manifest({}, root=self.root),
            ["$: manifest must be a JSON array"],
        )
        self.assertEqual(
            VALIDATOR.validate_manifest([], root=self.root),
            ["$: manifest must contain at least one screenshot entry"],
        )

    def test_required_fields_and_types(self) -> None:
        errors = VALIDATOR.validate_manifest(
            [{"label": "shot", "breakpoint": True}],
            root=self.root,
        )

        self.assertTrue(any("missing fields" in error for error in errors))
        self.assertTrue(any("breakpoint: must be a positive integer" in error for error in errors))

    def test_rejects_absolute_traversal_and_windows_paths(self) -> None:
        for unsafe in (
            "/tmp/shot.png",
            "../shot.png",
            "qa-shots/../../shot.png",
            r"C:\\Users\\person\\shot.png",
            r"qa-shots\\shot.png",
        ):
            with self.subTest(path=unsafe):
                errors = VALIDATOR.validate_manifest(
                    [_entry(path=unsafe)],
                    root=self.root,
                )
                self.assertTrue(any("repository-relative" in error for error in errors))

    def test_rejects_non_image_suffix(self) -> None:
        errors = VALIDATOR.validate_manifest(
            [_entry(path="qa-shots/result.json")],
            root=self.root,
        )
        self.assertTrue(any("expected one of" in error for error in errors))

    def test_rejects_duplicate_label_and_path(self) -> None:
        errors = VALIDATOR.validate_manifest(
            [_entry(), _entry()],
            root=self.root,
        )

        self.assertTrue(any("duplicate label" in error for error in errors))
        self.assertTrue(any("duplicate path" in error for error in errors))

    def test_allows_multiple_images_for_one_state(self) -> None:
        errors = VALIDATOR.validate_manifest(
            [
                _entry(),
                _entry(
                    label="checkout-error-modal-mobile-dark",
                    path="qa-shots/checkout-error-modal-mobile-dark.png",
                ),
            ],
            root=self.root,
        )
        self.assertEqual(errors, [])

    def test_check_files_accepts_existing_screenshot(self) -> None:
        screenshot = self.root / "qa-shots" / "checkout-error-mobile-dark.png"
        screenshot.parent.mkdir()
        screenshot.touch()

        errors = VALIDATOR.validate_manifest(
            [_entry()],
            root=self.root,
            check_files=True,
        )
        self.assertEqual(errors, [])

    def test_check_files_rejects_missing_screenshot(self) -> None:
        errors = VALIDATOR.validate_manifest(
            [_entry()],
            root=self.root,
            check_files=True,
        )
        self.assertTrue(any("does not exist" in error for error in errors))

    def test_loader_reports_invalid_json_location(self) -> None:
        path = self.root / "manifest.json"
        path.write_text('[{"label": ]', encoding="utf-8")

        with self.assertRaisesRegex(ValueError, "line 1, column"):
            VALIDATOR.load_manifest(path)

    def test_cli_status(self) -> None:
        path = self.root / "manifest.json"
        path.write_text(json.dumps([_entry()]), encoding="utf-8")

        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            valid_status = VALIDATOR.main([str(path), "--root", str(self.root)])
            missing_status = VALIDATOR.main(
                [str(path), "--root", str(self.root), "--check-files"]
            )

        self.assertEqual(valid_status, 0)
        self.assertEqual(missing_status, 1)


if __name__ == "__main__":
    unittest.main()
