from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_voice_context import (  # noqa: E402
    ManifestError,
    build_context,
    safe_local_output_name,
    validate_manifest,
)
from validate_package import validate  # noqa: E402


def digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


class DoppelTests(unittest.TestCase):
    def make_manifest(self, directory: Path, *, consent: bool = True, authorship: str = "subject") -> Path:
        source = (
            "A useful release names the mechanism and the evidence. The signal should remain inspectable.\n\n"
            "Short notes work when the audience already knows the boundary. Precision earns compression.\n"
        )
        (directory / "notes.md").write_text(source, encoding="utf-8")
        manifest = {
            "version": 1,
            "subject": {
                "label": "Example Author",
                "consent_confirmed": consent,
                "consent_scope": "Local editorial test",
                "final_ratifier": "subject",
            },
            "sources": [
                {
                    "id": "neutral-notes",
                    "path": "notes.md",
                    "authorship": authorship,
                    "sha256": digest(source),
                    "registers": ["general", "technical"],
                }
            ],
        }
        path = directory / "voice-manifest.local.json"
        path.write_text(json.dumps(manifest), encoding="utf-8")
        return path

    def test_builds_deterministic_context(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            manifest = self.make_manifest(Path(raw))
            kwargs = {
                "task": "Explain release evidence",
                "audience": "maintainers",
                "register": "technical",
                "max_chars": 4000,
            }
            first = build_context(manifest, **kwargs)
            second = build_context(manifest, **kwargs)
            self.assertEqual(first, second)
            self.assertIn("NOT PUBLISHABLE PROSE", first)
            self.assertIn("subject must ratify", first)
            self.assertIn("neutral-notes", first)
            self.assertNotIn(str(manifest.parent), first)

    def test_rejects_missing_consent(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            manifest = self.make_manifest(Path(raw), consent=False)
            with self.assertRaisesRegex(ManifestError, "consent"):
                build_context(
                    manifest, task="test", audience="reviewers", register="technical", max_chars=4000
                )

    def test_rejects_third_party_voice_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            manifest = self.make_manifest(Path(raw), authorship="third-party")
            with self.assertRaisesRegex(ManifestError, "not subject-authored"):
                build_context(
                    manifest, task="test", audience="reviewers", register="technical", max_chars=4000
                )

    def test_rejects_hash_drift(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            directory = Path(raw)
            manifest = self.make_manifest(directory)
            (directory / "notes.md").write_text("Changed after consent.", encoding="utf-8")
            with self.assertRaisesRegex(ManifestError, "hash"):
                build_context(
                    manifest, task="test", audience="reviewers", register="technical", max_chars=4000
                )

    def test_rejects_unmodelled_manifest_fields(self) -> None:
        data = {
            "version": 1,
            "subject": {
                "label": "Example Author",
                "consent_confirmed": True,
                "consent_scope": "Local editorial test",
                "final_ratifier": "subject",
            },
            "sources": [],
            "remote_upload": True,
        }
        with self.assertRaisesRegex(ManifestError, "unsupported top-level"):
            validate_manifest(data)

    def test_public_package_passes_validator(self) -> None:
        self.assertEqual(validate(ROOT), [])

    def test_output_name_must_match_shipped_ignore_rules(self) -> None:
        self.assertTrue(safe_local_output_name(Path("voice-context.local.md")))
        self.assertTrue(safe_local_output_name(Path("voice-context.launch.local.md")))
        self.assertFalse(safe_local_output_name(Path("private.local.md")))
        self.assertFalse(safe_local_output_name(Path("voice-context..local.md")))
        self.assertFalse(safe_local_output_name(Path("VOICE-CONTEXT.LOCAL.MD")))


if __name__ == "__main__":
    unittest.main()
