"""Synthetic records solely for validator behavior; no real experimental claims."""
import importlib.util
import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

SCRIPT = pathlib.Path(__file__).resolve().parents[1] / "scripts" / "validate_metadata.py"
SPEC = importlib.util.spec_from_file_location("metadata", SCRIPT)
metadata = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(metadata)


def synthetic_record():
    record = {key: "synthetic-test-only" for key in metadata.TEXT_FIELDS}
    record.update(schema_version=1, run_id="synthetic-test", seed=0, dirty=False,
                  created_at="2026-01-01T00:00:00+00:00", recorded_at="2026-01-01T00:00:01Z",
                  metadata_origin="birth", notes="", tags=["synthetic-test"], missing=[])
    return record


class MetadataTests(unittest.TestCase):
    def test_complete_record(self):
        self.assertEqual(metadata.validate(synthetic_record(), strict=True), ([], []))

    def test_explicit_gaps_accepted_not_strict(self):
        record = synthetic_record()
        record.update(commit=None, missing=["commit"])
        errors, warnings = metadata.validate(record)
        self.assertEqual(errors, [])
        self.assertTrue(warnings)
        self.assertTrue(metadata.validate(record, strict=True)[0])

    def test_false_completeness_and_invalid_types(self):
        for key, value in (("phase", ""), ("seed", True), ("dirty", "false"),
                           ("schema_version", True), ("tags", ["same", "same"]),
                           ("missing", ["invented"])):
            with self.subTest(key=key):
                record = synthetic_record()
                record[key] = value
                self.assertTrue(metadata.validate(record)[0])

    def test_backfill_keeps_birth_unknown(self):
        record = synthetic_record()
        record.update(metadata_origin="backfill", created_at=None, missing=["created_at"])
        self.assertEqual(metadata.validate(record)[0], [])
        record["metadata_origin"] = "birth"
        self.assertTrue(metadata.validate(record)[0])

    def test_dirty_snapshot_strict(self):
        record = synthetic_record()
        record.update(dirty=True, code_snapshot=None, missing=["code_snapshot"])
        self.assertEqual(metadata.validate(record)[0], [])
        self.assertTrue(metadata.validate(record, strict=True)[0])

    def test_timestamps(self):
        for value in ("not-a-date", "2026-01-01T00:00:00", "2027-01-01T00:00:00Z", 42):
            record = synthetic_record()
            record["created_at"] = value
            self.assertTrue(metadata.validate(record)[0])

    def test_missing_keys_and_input_types(self):
        for record in (None, [], {}, {"seed": 0}):
            self.assertTrue(metadata.validate(record)[0])

    def test_cli_exit_codes_and_read_only(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = pathlib.Path(temporary) / "record.json"
            content = json.dumps(synthetic_record())
            path.write_text(content)
            result = subprocess.run([sys.executable, str(SCRIPT), str(path), "--strict"], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(path.read_text(), content)
            path.write_text('{"run_id":"PRIVATE_TEST_VALUE", "run_id":"duplicate"}')
            result = subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertNotIn("PRIVATE_TEST_VALUE", result.stderr)
            path.write_text("{}")
            result = subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)


if __name__ == "__main__":
    unittest.main()
