"""Synthetic regression fixtures; no real transcript or claimed model output."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
import segment_transcript as segment
import validate_output as validator


class SegmentTests(unittest.TestCase):
    def test_line_ranges_hashes_and_maximum(self):
        source = "A: first\nB: next\n\nA: " + "é" * 1200
        chunks = segment.make_chunks(segment.make_blocks(source, 500), 500)
        self.assertEqual(chunks[0].start_line, 1)
        self.assertEqual(chunks[-1].end_line, 4)
        self.assertTrue(all(c.char_count <= 500 for c in chunks))
        for chunk in chunks:
            self.assertEqual(chunk.sha256, hashlib.sha256(chunk.text.encode()).hexdigest())
        self.assertEqual(sum(c.text.count("é") for c in chunks), 1200)

    def test_empty_source(self):
        self.assertEqual(segment.make_blocks("\n \n", 500), [])

    def test_cli_stdin_newlines_and_label(self):
        result = subprocess.run([sys.executable, str(SCRIPTS / "segment_transcript.py"), "-", "--source-label", "synthetic-01"], input="A\r\nB\rC", text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["source"], "synthetic-01")
        self.assertEqual(payload["line_count"], 3)
        self.assertEqual(payload["source_sha256"], hashlib.sha256(b"A\nB\nC").hexdigest())

    def test_reject_small_chunk_bound(self):
        result = subprocess.run([sys.executable, str(SCRIPTS / "segment_transcript.py"), "--max-chars", "0"], input="test", text=True, capture_output=True)
        self.assertEqual(result.returncode, 2)


class ValidatorTests(unittest.TestCase):
    def evidence(self):
        return dict(id="E01", type="proposal", claim="Maybe test locally", speaker="Speaker A", locator="L1", status="explicit", sensitivity="private")

    def check(self, payload, profile="custom", sources=True):
        return validator.validate_json(json.dumps(payload), profile, sources)[0]

    def test_valid_memory_and_missing_sources(self):
        payload = dict(meta={"profile": "memory"}, evidence=[self.evidence()], decisions=[], commitments=[], institutional_memory=[])
        self.assertEqual(self.check(payload, "memory"), [])
        payload["evidence"] = []
        self.assertTrue(self.check(payload, "memory"))

    def test_unknown_and_malformed_reference(self):
        for refs in (["missing"], [{}], [None]):
            payload = dict(meta={}, evidence=[self.evidence()], recommendations=[dict(recommendation="Test", status="recommendation", rationale="Uncertain", evidence_ids=refs, strongest_alternative="Wait", change_conditions=[])])
            self.assertTrue(self.check(payload))

    def test_duplicate_ids_and_unhashable_enums(self):
        item = self.evidence()
        self.assertTrue(self.check(dict(meta={}, evidence=[item, item])))
        for field in ("type", "status", "sensitivity"):
            broken = dict(item, **{field: {}})
            self.assertTrue(self.check(dict(meta={}, evidence=[broken])))

    def test_recommendation_cannot_claim_explicit_status(self):
        payload = dict(meta={}, evidence=[self.evidence()], recommendations=[dict(recommendation="Test", status="explicit", rationale="Uncertain", evidence_ids=["E01"], strongest_alternative="Wait", change_conditions=[])])
        self.assertTrue(self.check(payload))

    def test_markdown_missing_columns_and_sources(self):
        errors, _ = validator.validate_markdown("## Recommendation\n## Why This\n## Ranked Action Plan\n| Action |\n## Validation Plan\n", "next", True)
        self.assertTrue(any("columns" in e for e in errors))
        self.assertTrue(any("locator" in e for e in errors))

    def test_invalid_json_and_cli_failure(self):
        self.assertTrue(validator.validate_json("[]", "custom", False)[0])
        result = subprocess.run([sys.executable, str(SCRIPTS / "validate_output.py"), "-", "--format", "json"], input="{", text=True, capture_output=True)
        self.assertEqual(result.returncode, 1)
        self.assertNotIn("Traceback", result.stderr)

    def test_rejects_malformed_memory_schema(self):
        payload = dict(meta={"profile": "memory"}, evidence=[dict(self.evidence(), claim=[], speaker={}, locator={"not": "a locator"})], decisions="not an array", commitments=42, institutional_memory=False)
        errors = self.check(payload, "memory")
        for field in ("decisions", "commitments", "institutional_memory", "claim", "speaker", "locator"):
            self.assertTrue(any(field in error for error in errors), field)

    def test_remaining_top_level_types_and_metadata(self):
        for field in ("open_questions", "validation_plan", "risks", "insights", "opportunities", "nonlinear_potential"):
            self.assertTrue(self.check(dict(meta={}, evidence=[self.evidence()], **{field: {}})))
        for field in ("executive_brief", "shareable_report", "follow_up_draft"):
            self.assertTrue(self.check(dict(meta={}, evidence=[self.evidence()], **{field: []})))
        for field in ("profile", "purpose", "audience", "limitations", "source_hash"):
            self.assertTrue(self.check(dict(meta={field: {}}, evidence=[self.evidence()])))

    def test_action_and_recommendation_field_types(self):
        action = dict(action="Test", owner="Unassigned", priority="P1", feasibility="Easy", impact="Low", effort="S", dependencies=[], risks=[], next_step="Inspect", evidence_ids=["E01"])
        self.assertEqual(self.check(dict(meta={}, evidence=[self.evidence()], actions=[action])), [])
        for field in ("action", "owner", "next_step", "dependencies", "risks"):
            self.assertTrue(self.check(dict(meta={}, evidence=[self.evidence()], actions=[dict(action, **{field: {}})])))
        recommendation = dict(recommendation="Inspect", status="recommendation", rationale="Check evidence", evidence_ids=["E01"], strongest_alternative="Wait", change_conditions=[])
        for field in ("recommendation", "rationale", "strongest_alternative", "change_conditions"):
            self.assertTrue(self.check(dict(meta={}, evidence=[self.evidence()], recommendations=[dict(recommendation, **{field: {}})])))

    def test_duplicate_keys_nonfinite_and_empty_locator(self):
        for source in ('{"meta": {}, "meta": {}}', '{"meta": {}, "extension": NaN}'):
            self.assertTrue(validator.validate_json(source, "custom", False)[0])
        self.assertTrue(self.check(dict(meta={}, evidence=[dict(self.evidence(), locator=" ")])))

    def test_malformed_schema_cli_is_clear_failure(self):
        payload = dict(meta={"profile": "memory"}, evidence=[dict(self.evidence(), locator={})], decisions=False, commitments=42, institutional_memory="not an array")
        result = subprocess.run([sys.executable, str(SCRIPTS / "validate_output.py"), "-", "--format", "json", "--profile", "memory", "--require-sources"], input=json.dumps(payload), text=True, capture_output=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn("must be an array", result.stdout)
        self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
