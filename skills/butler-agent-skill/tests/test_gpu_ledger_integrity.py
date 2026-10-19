"""Fail-closed admission tests for malformed or structurally invalid GPU ledgers."""

import datetime as dt
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any


REPO = Path(__file__).resolve().parents[1]
CLI = REPO / "scripts" / "butler.py"
ADMISSION_PROJECT = "owner-project"
LEGACY_PROJECT = "legacy-project"


class ButlerGpuLedgerIntegrityTests(unittest.TestCase):
    """Exercise ledger integrity through isolated public CLI calls."""

    def setUp(self) -> None:
        """Create a registered aggregate scope under a disposable Butler root."""
        self.tmp = tempfile.TemporaryDirectory()
        base = Path(self.tmp.name)
        self.root = base / "butler"
        home = base / "home"
        home.mkdir(parents=True)
        self.env = {
            **os.environ,
            "BUTLER_ROOT": str(self.root),
            "HOME": str(home),
        }
        self.write_project(ADMISSION_PROJECT)
        self.write_project(LEGACY_PROJECT)
        (self.root / "config.json").write_text(json.dumps({
            "gpu_scopes": {
                "shared-scope": {
                    "members": [ADMISSION_PROJECT, LEGACY_PROJECT],
                    "admission_project": ADMISSION_PROJECT,
                }
            }
        }))

    def tearDown(self) -> None:
        """Remove the disposable Butler root."""
        self.tmp.cleanup()

    @property
    def ledger_path(self) -> Path:
        """Return the isolated GPU ledger path."""
        return self.root / "gpu" / "ledger.jsonl"

    def write_project(self, slug: str) -> None:
        """Register a project with deliberately roomy GPU budgets."""
        path = self.root / "projects" / slug / "project.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({
            "slug": slug,
            "roots": [str(self.root / "work" / slug)],
            "budget_pct_weekly": 1,
            "accounts": ["personal"],
            "gpu_hours": {"day": 100, "week": 100, "month": 100},
            "status": "active",
        }))

    def run_cli(self, *args: str) -> subprocess.CompletedProcess[str]:
        """Run canonical Butler against the isolated root."""
        return subprocess.run(
            [sys.executable, str(CLI), *args],
            env=self.env,
            text=True,
            capture_output=True,
        )

    def write_raw_ledger(self, content: str) -> None:
        """Write exact ledger bytes, including deliberate malformed tails."""
        self.ledger_path.parent.mkdir(parents=True, exist_ok=True)
        self.ledger_path.write_text(content)

    def write_events(self, *events: dict[str, Any]) -> None:
        """Write valid newline-terminated JSONL events."""
        self.write_raw_ledger(
            "".join(json.dumps(event) + "\n" for event in events)
        )

    @staticmethod
    def reservation(reservation_id: str, **updates: Any) -> dict[str, Any]:
        """Build one valid reservation row."""
        event: dict[str, Any] = {
            "type": "reservation",
            "schema_version": 2,
            "ts": dt.datetime.now(dt.timezone.utc).isoformat(),
            "project": ADMISSION_PROJECT,
            "reservation_id": reservation_id,
            "job": reservation_id,
            "gpus": 1.0,
            "hours": 2.0,
            "gpu_hours": 2.0,
            "estimated_cost": None,
            "currency": "GBP",
            "disk_gb": 10.0,
            "note": "",
        }
        event.update(updates)
        return event

    @staticmethod
    def reconcile(reservation_id: str, **updates: Any) -> dict[str, Any]:
        """Build one valid reconciliation row."""
        event: dict[str, Any] = {
            "type": "reconcile",
            "schema_version": 2,
            "ts": dt.datetime.now(dt.timezone.utc).isoformat(),
            "project": ADMISSION_PROJECT,
            "reservation_id": reservation_id,
            "job": reservation_id,
            "actual_gpu_hours": 1.0,
            "actual_cost": 0.0,
            "currency": "GBP",
            "retained_disk_gb": 10.0,
            "outcome": "completed",
            "note": "",
        }
        event.update(updates)
        return event

    @staticmethod
    def disk_release(reservation_id: str) -> dict[str, Any]:
        """Build one valid retained-disk release row."""
        return {
            "type": "disk_release",
            "schema_version": 2,
            "ts": dt.datetime.now(dt.timezone.utc).isoformat(),
            "project": ADMISSION_PROJECT,
            "reservation_id": reservation_id,
            "job": reservation_id,
            "released_disk_gb": 10.0,
            "evidence": "provider://receipt/disk-deleted",
            "note": "",
        }

    def assert_corruption_rejected_without_append(self) -> None:
        """Assert both admission commands reject and preserve exact ledger bytes."""
        before = self.ledger_path.read_bytes()

        gate = self.run_cli(
            "gpu-gate", "--project", ADMISSION_PROJECT, "--request", "1"
        )
        self.assertEqual(gate.returncode, 1, gate.stdout + gate.stderr)
        self.assertEqual(json.loads(gate.stdout)["verdict"], "invalid")
        self.assertNotIn("Traceback", gate.stdout + gate.stderr)
        self.assertEqual(self.ledger_path.read_bytes(), before)

        reserve = self.run_cli(
            "gpu-reserve",
            "--project",
            ADMISSION_PROJECT,
            "--job",
            "must-not-append",
            "--gpus",
            "1",
            "--hours",
            "1",
        )
        self.assertEqual(reserve.returncode, 1, reserve.stdout + reserve.stderr)
        self.assertEqual(json.loads(reserve.stdout)["verdict"], "invalid")
        self.assertNotIn("Traceback", reserve.stdout + reserve.stderr)
        self.assertEqual(self.ledger_path.read_bytes(), before)

    def test_unterminated_torn_final_row_preserves_prior_usage(self) -> None:
        """Only an incomplete final row without a line terminator is tolerated."""
        usage = {
            "type": "legacy_usage",
            "ts": dt.datetime.now(dt.timezone.utc).isoformat(),
            "project": ADMISSION_PROJECT,
            "job": "completed",
            "gpu_hours": 3.0,
        }
        self.write_raw_ledger(json.dumps(usage) + "\n" + '{"torn":')
        before = self.ledger_path.read_bytes()

        gate = self.run_cli(
            "gpu-gate", "--project", ADMISSION_PROJECT, "--request", "1"
        )

        self.assertEqual(gate.returncode, 0, gate.stdout + gate.stderr)
        self.assertEqual(json.loads(gate.stdout)["windows"]["day"]["committed"], 3.0)
        self.assertEqual(self.ledger_path.read_bytes(), before)

        reserve = self.run_cli(
            "gpu-reserve",
            "--project",
            ADMISSION_PROJECT,
            "--job",
            "must-not-follow-torn-tail",
            "--gpus",
            "1",
            "--hours",
            "1",
        )
        self.assertEqual(reserve.returncode, 1, reserve.stdout + reserve.stderr)
        self.assertEqual(json.loads(reserve.stdout)["verdict"], "invalid")
        self.assertNotIn("Traceback", reserve.stdout + reserve.stderr)
        self.assertEqual(self.ledger_path.read_bytes(), before)

    def test_malformed_interior_row_fails_closed_without_append(self) -> None:
        """A malformed row before a later valid row is never treated as torn."""
        first = self.reservation("first")
        last = self.reservation("last")
        self.write_raw_ledger(
            json.dumps(first) + "\n" + '{"broken":\n' + json.dumps(last) + "\n"
        )

        self.assert_corruption_rejected_without_append()

    def test_reserve_rejects_valid_but_unterminated_final_row(self) -> None:
        """Reserve cannot append safely until a valid final row is terminated."""
        self.write_raw_ledger(json.dumps(self.reservation("held")))
        before = self.ledger_path.read_bytes()

        reserve = self.run_cli(
            "gpu-reserve",
            "--project",
            ADMISSION_PROJECT,
            "--job",
            "must-not-concatenate",
            "--gpus",
            "1",
            "--hours",
            "1",
        )

        self.assertEqual(reserve.returncode, 1, reserve.stdout + reserve.stderr)
        self.assertEqual(json.loads(reserve.stdout)["verdict"], "invalid")
        self.assertEqual(self.ledger_path.read_bytes(), before)

    def test_malformed_terminated_final_row_fails_closed_without_append(self) -> None:
        """A malformed final row ending in a newline is durable corruption."""
        self.write_raw_ledger(
            json.dumps(self.reservation("first")) + "\n" + '{"broken": true,}\n'
        )

        self.assert_corruption_rejected_without_append()

    def test_structural_anomalies_fail_closed_without_append(self) -> None:
        """Duplicate, orphan, and invalid numeric rows block all admission."""
        reservation = self.reservation("held")
        reconciliation = self.reconcile("held")
        release = self.disk_release("held")
        cases = {
            "duplicate_reservation": [reservation, reservation],
            "duplicate_reconciliation": [
                reservation,
                reconciliation,
                reconciliation,
            ],
            "duplicate_disk_release": [
                reservation,
                reconciliation,
                release,
                release,
            ],
            "orphan_reconciliation": [self.reconcile("orphan")],
            "orphan_disk_release": [self.disk_release("orphan")],
            "invalid_numeric_row": [
                self.reservation("invalid-number", gpu_hours="not-a-number")
            ],
        }

        for case, events in cases.items():
            with self.subTest(case=case):
                self.write_events(*events)
                self.assert_corruption_rejected_without_append()

    def test_duplicate_exact_replay_is_rejected_before_idempotency(self) -> None:
        """Same-project duplicate IDs cannot masquerade as an idempotent replay."""
        held = self.reservation("held")
        self.write_events(held, held)
        before = self.ledger_path.read_bytes()

        replay = self.run_cli(
            "gpu-reserve",
            "--project",
            ADMISSION_PROJECT,
            "--job",
            "held",
            "--gpus",
            "1",
            "--hours",
            "2",
            "--disk-gb",
            "10",
        )

        self.assertEqual(replay.returncode, 1, replay.stdout + replay.stderr)
        self.assertEqual(json.loads(replay.stdout)["verdict"], "invalid")
        self.assertNotIn("Traceback", replay.stdout + replay.stderr)
        self.assertEqual(self.ledger_path.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
