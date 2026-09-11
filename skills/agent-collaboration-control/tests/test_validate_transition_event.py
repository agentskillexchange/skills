"""Tests for the project-agnostic transition-event validator."""

from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path
from types import ModuleType

SKILL_ROOT = Path(__file__).parents[1]
SCRIPT_PATH = SKILL_ROOT / "scripts" / "validate_transition_event.py"
POLICY_PATH = SKILL_ROOT / "assets" / "collaboration-policy.example.json"
EVENT_PATH = SKILL_ROOT / "assets" / "transition-event.example.json"


def _load_validator() -> ModuleType:
    """Load the validator without a package installation."""
    spec = importlib.util.spec_from_file_location(
        "validate_transition_event",
        SCRIPT_PATH,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load validator at {SCRIPT_PATH}.")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _load_fixture(path: Path) -> dict[str, object]:
    """Load a JSON fixture."""
    with path.open(encoding="utf-8") as fixture_file:
        return json.load(fixture_file)


VALIDATOR = _load_validator()


class ValidateTransitionEventTest(unittest.TestCase):
    """Exercise configurable, fail-closed event validation."""

    def setUp(self) -> None:
        """Load pristine policy and event fixtures."""
        self.policy = _load_fixture(POLICY_PATH)
        self.event = _load_fixture(EVENT_PATH)

    def test_example_policy_and_event_are_valid(self) -> None:
        """Bundled assets must work together without customization."""
        self.assertEqual(VALIDATOR.validate_policy(self.policy), [])
        self.assertEqual(
            VALIDATOR.validate_event(self.event, self.policy),
            [],
        )

    def test_policy_rejects_schema_drift_and_bad_regex(self) -> None:
        """Invalid policy cannot weaken event validation."""
        self.policy["unexpected"] = True
        self.policy["event_id_pattern"] = "["

        errors = VALIDATOR.validate_policy(self.policy)

        self.assertIn("policy unknown keys: unexpected", errors)
        self.assertTrue(
            any("event_id_pattern is invalid" in error for error in errors)
        )

    def test_policy_rejects_duplicate_or_empty_enums(self) -> None:
        """Every configured identity and state must be unambiguous."""
        self.policy["actors"] = ["controller", "controller"]
        self.policy["states"] = []

        errors = VALIDATOR.validate_policy(self.policy)

        self.assertIn(
            "policy actors must not contain duplicates",
            errors,
        )
        self.assertIn(
            "policy states must be a non-empty list of strings",
            errors,
        )

    def test_event_rejects_missing_and_unknown_keys(self) -> None:
        """Event schema drift must fail closed."""
        del self.event["type"]
        self.event["extra"] = True

        errors = VALIDATOR.validate_event(self.event, self.policy)

        self.assertIn("missing keys: type", errors)
        self.assertIn("unknown keys: extra", errors)

    def test_event_rejects_bad_identity_timestamp_and_enums(self) -> None:
        """Identity and lifecycle values must match project policy."""
        self.event.update(
            {
                "id": "control-1",
                "ts": "2026-07-27Z",
                "actor": "unbound-agent",
                "state": "running",
            }
        )

        errors = VALIDATOR.validate_event(self.event, self.policy)

        self.assertTrue(any(error.startswith("id does") for error in errors))
        self.assertTrue(any(error.startswith("ts must") for error in errors))
        self.assertTrue(
            any(error.startswith("actor must") for error in errors)
        )
        self.assertTrue(
            any(error.startswith("state must") for error in errors)
        )

    def test_event_rejects_empty_or_mistyped_evidence(self) -> None:
        """Receipts require typed evidence and hold collections."""
        self.event["evidence_refs"] = []
        self.event["holds"] = "none"
        self.event["cost"] = 1

        errors = VALIDATOR.validate_event(self.event, self.policy)

        self.assertTrue(
            any(error.startswith("evidence_refs must") for error in errors)
        )
        self.assertTrue(
            any(error.startswith("holds must") for error in errors)
        )
        self.assertIn("cost must be a string or null", errors)


if __name__ == "__main__":
    unittest.main()
