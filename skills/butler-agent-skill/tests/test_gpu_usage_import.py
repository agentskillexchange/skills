#!/usr/bin/env python3
"""Regression tests for idempotent retroactive GPU usage imports."""

import datetime as dt
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CLI = REPO / "scripts" / "butler.py"
REAL_LEDGER = Path(tempfile.gettempdir()) / "synthetic-nonexistent-butler-sentinel" / "ledger.jsonl"


def ledger_fingerprint(path: Path):
    try:
        stat = path.stat()
    except OSError:
        return None
    return stat.st_size, stat.st_mtime_ns


class ButlerGpuUsageImportTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        base = Path(self.temporary.name)
        self.root = base / "butler"
        self.home = base / "home"
        self.home.mkdir(parents=True)
        self.env = {
            **os.environ,
            "BUTLER_ROOT": str(self.root),
            "HOME": str(self.home),
        }
        self.occurred_at = dt.datetime.now(dt.timezone.utc).isoformat()
        self.real_ledger_before = ledger_fingerprint(REAL_LEDGER)
        self.write_project()

    def tearDown(self):
        self.assertEqual(
            ledger_fingerprint(REAL_LEDGER),
            self.real_ledger_before,
            "test mutated the production Butler GPU ledger",
        )
        self.temporary.cleanup()

    def write_project(self, *, cash_month=1000):
        policy = {
            "max_concurrent_gpus": 8,
            "cash": {"currency": "GBP", "month": cash_month},
        }
        project = {
            "slug": "import-test",
            "roots": [str(self.root / "work")],
            "budget_pct_weekly": 1,
            "accounts": ["personal"],
            "gpu_hours": {"day": 100, "week": 100, "month": 100},
            "gpu_policy": policy,
            "status": "active",
        }
        path = self.root / "projects" / "import-test" / "project.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(project))

    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, str(CLI), *args],
            env=self.env,
            text=True,
            capture_output=True,
        )

    def import_usage(
        self,
        *,
        usage_id="provider:run-1:attempt-1",
        hours="2.5",
        cost="7.5",
        occurred_at=None,
        outcome="failed",
        evidence="provider://terminal/run-1",
        note="historical settlement",
    ):
        occurred_at = occurred_at or self.occurred_at
        args = [
            "gpu-import-usage",
            "--project",
            "import-test",
            "--usage-id",
            usage_id,
            "--job",
            "run-1",
            "--occurred-at",
            occurred_at,
            "--actual-gpu-hours",
            hours,
            "--currency",
            "GBP",
            "--outcome",
            outcome,
            "--evidence",
            evidence,
            "--note",
            note,
        ]
        if cost is not None:
            args.extend(["--actual-cost", cost])
        return self.run_cli(*args)

    def ledger(self):
        path = self.root / "gpu" / "ledger.jsonl"
        if not path.exists():
            return []
        return [json.loads(line) for line in path.read_text().splitlines()]

    def test_import_records_hours_and_cash_without_creating_a_hold(self):
        result = self.import_usage()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(json.loads(result.stdout)["verdict"], "imported")

        gate = self.run_cli(
            "gpu-gate", "--project", "import-test", "--request", "1",
            "--gpus", "1", "--hours", "1", "--estimated-cost", "3",
        )
        payload = json.loads(gate.stdout)
        self.assertEqual(payload["windows"]["day"]["completed"], 2.5)
        self.assertEqual(payload["checks"]["cash"]["completed"], 7.5)
        self.assertEqual(payload["checks"]["concurrency"]["active"], 0)

    def test_exact_replay_is_noop_but_conflicting_replay_fails(self):
        first = self.import_usage()
        replay = self.import_usage()
        conflict = self.import_usage(hours="2.75")

        self.assertEqual(first.returncode, 0, first.stdout)
        self.assertEqual(replay.returncode, 0, replay.stdout)
        self.assertEqual(json.loads(replay.stdout)["verdict"], "already_imported")
        self.assertEqual(conflict.returncode, 1, conflict.stdout)
        self.assertEqual(json.loads(conflict.stdout)["verdict"], "invalid")
        self.assertEqual(len(self.ledger()), 1)

    def test_equivalent_timestamp_offsets_canonicalize_for_replay(self):
        first = self.import_usage(occurred_at="2026-08-22T12:00:00+00:00")
        replay = self.import_usage(occurred_at="2026-08-22T13:00:00+01:00")

        self.assertEqual(first.returncode, 0, first.stdout)
        self.assertEqual(replay.returncode, 0, replay.stdout)
        self.assertEqual(json.loads(replay.stdout)["verdict"], "already_imported")
        self.assertEqual(len(self.ledger()), 1)

    def test_occurrence_time_controls_rolling_window_not_import_time(self):
        old = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=40)).isoformat()
        result = self.import_usage(occurred_at=old)
        self.assertEqual(result.returncode, 0, result.stdout)

        gate = self.run_cli(
            "gpu-gate", "--project", "import-test", "--request", "1",
            "--gpus", "1", "--hours", "1", "--estimated-cost", "3",
        )
        payload = json.loads(gate.stdout)
        self.assertEqual(payload["windows"]["month"]["completed"], 0)
        self.assertEqual(payload["checks"]["cash"]["completed"], 0)

    def test_cash_controlled_project_requires_cost(self):
        result = self.import_usage(cost=None)
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("requires --actual-cost", result.stdout)
        self.assertEqual(self.ledger(), [])

    def test_invalid_future_time_and_missing_evidence_do_not_append(self):
        future = (dt.datetime.now(dt.timezone.utc) + dt.timedelta(days=1)).isoformat()
        invalid_time = self.import_usage(occurred_at=future)
        missing_evidence = self.import_usage(evidence=" ")

        self.assertEqual(invalid_time.returncode, 1, invalid_time.stdout)
        self.assertEqual(missing_evidence.returncode, 1, missing_evidence.stdout)
        self.assertEqual(self.ledger(), [])

    def test_duplicate_raw_usage_ids_make_admission_fail_closed(self):
        event = {
            "type": "usage_import",
            "schema_version": 3,
            "ts": dt.datetime.now(dt.timezone.utc).isoformat(),
            "occurred_at": dt.datetime.now(dt.timezone.utc).isoformat(),
            "project": "import-test",
            "usage_id": "provider:duplicate",
            "job": "run-1",
            "actual_gpu_hours": 1.0,
            "actual_cost": 3.0,
            "currency": "GBP",
            "outcome": "failed",
            "evidence": "provider://terminal/run-1",
            "note": "",
        }
        ledger = self.root / "gpu" / "ledger.jsonl"
        ledger.parent.mkdir(parents=True)
        ledger.write_text(json.dumps(event) + "\n" + json.dumps(event) + "\n")
        before = ledger.read_bytes()

        gate = self.run_cli(
            "gpu-gate", "--project", "import-test", "--request", "1",
            "--gpus", "1", "--hours", "1", "--estimated-cost", "3",
        )
        self.assertEqual(gate.returncode, 1, gate.stdout)
        self.assertEqual(json.loads(gate.stdout)["verdict"], "invalid")
        self.assertIn("duplicate usage import", gate.stdout)
        self.assertEqual(ledger.read_bytes(), before)

    def test_cross_member_duplicate_usage_ids_fail_closed(self):
        member_path = self.root / "projects" / "legacy-member" / "project.json"
        member_path.parent.mkdir(parents=True)
        member_path.write_text(json.dumps({
            "slug": "legacy-member",
            "roots": [str(self.root / "legacy-work")],
            "budget_pct_weekly": 1,
            "accounts": ["personal"],
            "gpu_hours": {"day": 100, "week": 100, "month": 100},
            "status": "active",
        }))
        (self.root / "config.json").write_text(json.dumps({
            "gpu_scopes": {
                "shared-scope": {
                    "members": ["import-test", "legacy-member"],
                    "admission_project": "import-test",
                }
            }
        }))
        base = {
            "type": "usage_import",
            "schema_version": 3,
            "ts": dt.datetime.now(dt.timezone.utc).isoformat(),
            "occurred_at": dt.datetime.now(dt.timezone.utc).isoformat(),
            "usage_id": "provider:cross-member",
            "job": "run-1",
            "actual_gpu_hours": 1.0,
            "actual_cost": 3.0,
            "currency": "GBP",
            "outcome": "failed",
            "evidence": "provider://terminal/run-1",
            "note": "",
        }
        ledger = self.root / "gpu" / "ledger.jsonl"
        ledger.parent.mkdir(parents=True)
        ledger.write_text(
            json.dumps({**base, "project": "import-test"}) + "\n"
            + json.dumps({**base, "project": "legacy-member"}) + "\n"
        )

        gate = self.run_cli(
            "gpu-gate", "--project", "import-test", "--request", "1",
            "--gpus", "1", "--hours", "1", "--estimated-cost", "3",
        )
        self.assertEqual(gate.returncode, 1, gate.stdout)
        self.assertEqual(json.loads(gate.stdout)["verdict"], "invalid")
        self.assertIn("cross-member duplicate usage import", gate.stdout)


if __name__ == "__main__":
    unittest.main()
