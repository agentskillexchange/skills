#!/usr/bin/env python3
"""Regression cover for `butler gpu-reconcile --outcome`, and for failed_infrastructure.

Every butler process started here runs against a throwaway BUTLER_ROOT and HOME, and each
test re-checks the ledger path the child actually resolved. A butler that ignored
BUTLER_ROOT would otherwise quietly append fixture rows to the real cellar at
~/.butler/gpu/ledger.jsonl, so the isolation check is a precondition of every case rather
than a test of its own.
"""
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
BUTLER = SCRIPTS / "butler.py"

# Resolved from the real environment at import time, before any test rewrites HOME.
REAL_BUTLER_ROOT = Path(tempfile.gettempdir()) / "synthetic-nonexistent-butler-sentinel"
REAL_BUTLER_LEDGER = REAL_BUTLER_ROOT / "gpu" / "ledger.jsonl"

PROJECT = "temp-reconcile-fixture"
EPOCH = "1970-01-01T00:00:00+00:00"
EXPECTED_OUTCOMES = (
    "completed",
    "failed",
    "failed_infrastructure",
    "killed",
    "cancelled",
    "launch_failed",
)


def real_ledger_fingerprint():
    """Size and mtime of the operator's real ledger, or None when it does not exist."""
    try:
        stat = REAL_BUTLER_LEDGER.stat()
    except OSError:
        return None
    return (stat.st_size, stat.st_mtime_ns)


class GpuReconcileOutcomeTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        base = Path(self.temporary.name)
        self.butler_root = base / "butler-root"
        self.home = base / "home"
        self.home.mkdir(parents=True)
        self.ledger = self.butler_root / "gpu" / "ledger.jsonl"
        self.real_ledger_before = real_ledger_fingerprint()
        # Cleanups run last-in-first-out: the cellar check outlives the temp directory.
        self.addCleanup(self.temporary.cleanup)
        self.addCleanup(self.assert_real_cellar_untouched)
        self.assert_isolated()
        self.butler("register", "--project", PROJECT,
                    "--root", str(base / "sources"), "--weekly-pct", "1")

    # -- harness ---------------------------------------------------------------

    def env(self):
        environment = dict(os.environ)
        environment["BUTLER_ROOT"] = str(self.butler_root)
        environment["HOME"] = str(self.home)
        return environment

    def butler(self, *args, expect=0):
        proc = subprocess.run([sys.executable, str(BUTLER), *args],
                              env=self.env(), capture_output=True, text=True)
        self.assertEqual(proc.returncode, expect,
                         f"butler {' '.join(args)}\n{proc.stdout}\n{proc.stderr}")
        return proc

    def butler_json(self, *args, expect=0):
        return json.loads(self.butler(*args, expect=expect).stdout)

    def probe(self, expression):
        """Evaluate an expression inside butler's module namespace, under the temp root."""
        source = (f"import json, sys; sys.path.insert(0, {str(SCRIPTS)!r}); "
                  f"import butler; print(json.dumps({expression}))")
        proc = subprocess.run([sys.executable, "-c", source],
                              env=self.env(), capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        return json.loads(proc.stdout)

    def assert_isolated(self):
        resolved = Path(self.probe("str(butler.GPU_LEDGER)"))
        self.assertEqual(resolved, self.ledger)
        self.assertNotEqual(resolved.resolve(), REAL_BUTLER_LEDGER)
        self.assertFalse(str(resolved.resolve()).startswith(f"{REAL_BUTLER_ROOT}{os.sep}"),
                         f"fixture ledger {resolved} sits inside the real cellar")

    def assert_real_cellar_untouched(self):
        self.assertEqual(real_ledger_fingerprint(), self.real_ledger_before,
                         "the real ~/.butler ledger changed during an isolated test")

    def snapshot(self):
        return self.probe(
            "butler._gpu_snapshot("
            f"{PROJECT!r}, __import__('datetime').datetime.fromisoformat({EPOCH!r}))"
        )

    def events(self):
        if not self.ledger.exists():
            return []
        return [json.loads(line) for line in self.ledger.read_text().splitlines()
                if line.strip()]

    def reconciliation(self, reservation_id):
        matches = [e for e in self.events()
                   if e.get("type") == "reconcile"
                   and e.get("reservation_id") == reservation_id]
        self.assertEqual(len(matches), 1, f"expected exactly one reconcile for {reservation_id}")
        return matches[0]

    def reserve(self, reservation_id, *, gpus="2", hours="4", cost="40", disk="100"):
        return self.butler_json(
            "gpu-reserve", "--project", PROJECT, "--job", reservation_id,
            "--reservation-id", reservation_id, "--gpus", gpus, "--hours", hours,
            "--estimated-cost", cost, "--currency", "GBP", "--disk-gb", disk)

    def reconcile(self, reservation_id, outcome, *, hours="5.5", cost="27.5",
                  disk="40", expect=0):
        return self.butler_json(
            "gpu-reconcile", "--project", PROJECT, "--reservation-id", reservation_id,
            "--actual-gpu-hours", hours, "--actual-cost", cost,
            "--retained-disk-gb", disk, "--outcome", outcome, expect=expect)

    # -- cases -----------------------------------------------------------------

    def test_isolation_guard_points_away_from_the_real_cellar(self):
        self.assertNotEqual(self.ledger.resolve(), REAL_BUTLER_LEDGER)
        self.assertEqual(self.probe("str(butler.ROOT)"), str(self.butler_root))
        self.assertEqual(self.probe("butler.GPU_RECONCILE_OUTCOMES"), list(EXPECTED_OUTCOMES))

    def test_failed_infrastructure_is_accepted_and_recorded_verbatim(self):
        self.reserve("infra-job")
        verdict = self.reconcile("infra-job", "failed_infrastructure")
        self.assertEqual(verdict["verdict"], "reconciled")
        self.assertEqual(verdict["reconciliation"]["outcome"], "failed_infrastructure")

        event = self.reconciliation("infra-job")
        self.assertEqual(event["outcome"], "failed_infrastructure")
        self.assertNotEqual(event["outcome"], "failed")
        self.assertEqual(event["reservation_id"], "infra-job")
        self.assertEqual(event["job"], "infra-job")
        self.assertEqual(event["project"], PROJECT)
        self.assertEqual(event["actual_gpu_hours"], 5.5)
        self.assertEqual(event["actual_cost"], 27.5)
        self.assertEqual(event["currency"], "GBP")
        self.assertEqual(event["retained_disk_gb"], 40.0)
        self.assertEqual(event["schema_version"], 2)

    def test_failed_infrastructure_accounts_the_actual_burn_and_releases_the_hold(self):
        self.reserve("infra-job")
        held = self.snapshot()
        self.assertEqual(held["reserved_gpu_hours"], 8.0)
        self.assertEqual(held["active_reservations"], 1)
        self.assertEqual(held["active_disk_gb"], 100.0)

        self.reconcile("infra-job", "failed_infrastructure")
        settled = self.snapshot()
        self.assertEqual(settled["completed_gpu_hours"], 5.5)
        self.assertEqual(settled["completed_cost"], 27.5)
        self.assertEqual(settled["reserved_gpu_hours"], 0.0)
        self.assertEqual(settled["reserved_cost"], 0.0)
        self.assertEqual(settled["committed_gpu_hours"], 5.5)
        self.assertEqual(settled["active_reservations"], 0)
        self.assertEqual(settled["active_gpus"], 0.0)
        # Only the disk the operator declared as retained keeps consuming the ceiling.
        self.assertEqual(settled["active_disk_gb"], 40.0)
        self.assertEqual(settled["anomalies"], [])

        gate = self.butler_json("gpu-gate", "--project", PROJECT, "--request", "1",
                                expect=0)
        self.assertEqual(gate["windows"]["month"]["completed"], 5.5)
        self.assertEqual(gate["windows"]["month"]["reserved"], 0.0)
        self.assertEqual(gate["checks"]["disk"]["active_gb"], 40.0)
        self.assertEqual(gate["checks"]["cash"]["completed"], 27.5)

    def test_exact_replay_is_already_reconciled_and_appends_nothing(self):
        self.reserve("infra-job")
        first = self.reconcile("infra-job", "failed_infrastructure")
        before = self.events()

        replay = self.reconcile("infra-job", "failed_infrastructure")
        self.assertEqual(replay["verdict"], "already_reconciled")
        self.assertEqual(replay["reconciliation"]["outcome"], "failed_infrastructure")
        self.assertEqual(replay["reconciliation"]["ts"], first["reconciliation"]["ts"])
        self.assertEqual(self.events(), before)
        self.assertEqual(self.snapshot()["completed_gpu_hours"], 5.5)

    def test_replaying_with_failed_conflicts_instead_of_aliasing(self):
        self.reserve("infra-job")
        self.reconcile("infra-job", "failed_infrastructure")
        before = self.events()

        conflict = self.reconcile("infra-job", "failed", expect=1)
        self.assertEqual(conflict["verdict"], "invalid")
        self.assertEqual(conflict["reason"], "conflicting reconciliation")
        self.assertEqual(self.events(), before)
        self.assertEqual(self.reconciliation("infra-job")["outcome"], "failed_infrastructure")

    def test_failed_does_not_absorb_failed_infrastructure_in_the_other_direction(self):
        self.reserve("workload-job")
        self.reconcile("workload-job", "failed")
        conflict = self.reconcile("workload-job", "failed_infrastructure", expect=1)
        self.assertEqual(conflict["reason"], "conflicting reconciliation")
        self.assertEqual(self.reconciliation("workload-job")["outcome"], "failed")

    def test_every_outcome_remains_accepted(self):
        for outcome in EXPECTED_OUTCOMES:
            with self.subTest(outcome=outcome):
                reservation_id = f"job-{outcome}"
                self.reserve(reservation_id, gpus="1", hours="1", cost="5", disk="10")
                verdict = self.reconcile(reservation_id, outcome, hours="1", cost="5",
                                         disk="0")
                self.assertEqual(verdict["verdict"], "reconciled")
                self.assertEqual(self.reconciliation(reservation_id)["outcome"], outcome)
        self.assertEqual(self.snapshot()["active_reservations"], 0)

    def test_unknown_outcomes_are_still_refused(self):
        self.reserve("infra-job")
        proc = subprocess.run(
            [sys.executable, str(BUTLER), "gpu-reconcile", "--project", PROJECT,
             "--reservation-id", "infra-job", "--actual-gpu-hours", "1",
             "--outcome", "infrastructure"],
            env=self.env(), capture_output=True, text=True)
        self.assertEqual(proc.returncode, 2)
        self.assertIn("invalid choice", proc.stderr)
        self.assertEqual([e for e in self.events() if e.get("type") == "reconcile"], [])

    def test_help_documents_the_outcome_split(self):
        help_text = self.butler("gpu-reconcile", "--help").stdout
        for outcome in EXPECTED_OUTCOMES:
            self.assertIn(outcome, help_text)
        self.assertIn("failed_infrastructure", help_text)


if __name__ == "__main__":
    unittest.main()
