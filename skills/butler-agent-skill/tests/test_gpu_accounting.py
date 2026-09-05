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


class ButlerGpuAccountingTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.env = {**os.environ, "BUTLER_ROOT": str(self.root)}
        self.write_project()

    def tearDown(self):
        self.tmp.cleanup()

    def write_project(self, *, hours=None, policy=None):
        project = {
            "slug": "synthetic-project",
            "roots": [str(self.root / "work")],
            "budget_pct_weekly": 10,
            "accounts": ["personal"],
            "gpu_hours": hours or {"day": 8, "week": 8, "month": 8},
            "status": "active",
        }
        if policy:
            project["gpu_policy"] = policy
        path = self.root / "projects" / "synthetic-project" / "project.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(project))

    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, str(CLI), *args], env=self.env,
            text=True, capture_output=True,
        )

    def reserve(self, job, *, gpus=1, hours=8, cost=None, disk=0):
        args = ["gpu-reserve", "--project", "synthetic-project", "--job", job,
                "--gpus", str(gpus), "--hours", str(hours), "--disk-gb", str(disk)]
        if cost is not None:
            args += ["--estimated-cost", str(cost)]
        return self.run_cli(*args)

    def reconcile(self, job, actual, cost=None, retained_disk=0):
        args = ["gpu-reconcile", "--project", "synthetic-project",
                "--reservation-id", job, "--actual-gpu-hours", str(actual),
                "--retained-disk-gb", str(retained_disk)]
        if cost is not None:
            args += ["--actual-cost", str(cost)]
        return self.run_cli(*args)

    def ledger(self):
        path = self.root / "gpu" / "ledger.jsonl"
        return [json.loads(line) for line in path.read_text().splitlines()] if path.exists() else []

    def test_parallel_reservations_are_admitted_atomically(self):
        base = [sys.executable, str(CLI), "gpu-reserve", "--project", "synthetic-project",
                "--gpus", "1", "--hours", "8"]
        procs = [subprocess.Popen(base + ["--job", f"job-{i}"], env=self.env,
                                  text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                 for i in range(6)]
        results = [p.communicate() + (p.returncode,) for p in procs]
        self.assertEqual([r[2] for r in results].count(0), 1, results)
        reservations = [e for e in self.ledger() if e.get("type") == "reservation"]
        self.assertEqual(len(reservations), 1)

    def test_reconciliation_replaces_hold_with_non_negative_actual(self):
        self.assertEqual(self.reserve("run-1").returncode, 0)
        result = self.reconcile("run-1", 4)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

        allowed = self.run_cli("gpu-gate", "--project", "synthetic-project", "--request", "4")
        denied = self.run_cli("gpu-gate", "--project", "synthetic-project", "--request", "4.1")
        self.assertEqual(allowed.returncode, 0, allowed.stdout)
        self.assertEqual(denied.returncode, 1, denied.stdout)
        self.assertTrue(all(e.get("gpu_hours", 0) >= 0 for e in self.ledger()))

    def test_negative_legacy_usage_is_rejected_and_old_corrections_are_clamped(self):
        rejected = self.run_cli("gpu-log", "--project", "synthetic-project", "--job", "bad",
                                "--gpus", "-1", "--hours", "2")
        self.assertEqual(rejected.returncode, 1)
        self.assertFalse((self.root / "gpu" / "ledger.jsonl").exists())

        ledger = self.root / "gpu" / "ledger.jsonl"
        ledger.parent.mkdir(parents=True)
        now = dt.datetime.now(dt.timezone.utc).isoformat()
        ledger.write_text(json.dumps({"ts": now, "project": "synthetic-project",
                                      "job": "old-correction", "gpu_hours": -19.3}) + "\n")
        gate = self.run_cli("gpu-gate", "--project", "synthetic-project", "--request", "1")
        payload = json.loads(gate.stdout)
        self.assertEqual(payload["windows"]["day"]["committed"], 0)
        self.assertIn("legacy rolling usage clamped at zero", payload["ledger_anomalies"])

    def test_torn_final_jsonl_row_does_not_erase_prior_usage(self):
        ledger = self.root / "gpu" / "ledger.jsonl"
        ledger.parent.mkdir(parents=True)
        now = dt.datetime.now(dt.timezone.utc).isoformat()
        valid = {"ts": now, "project": "synthetic-project", "job": "valid", "gpu_hours": 3}
        ledger.write_text(json.dumps(valid) + "\n" + '{"torn":')
        gate = self.run_cli("gpu-gate", "--project", "synthetic-project", "--request", "5")
        payload = json.loads(gate.stdout)
        self.assertEqual(gate.returncode, 0)
        self.assertEqual(payload["windows"]["day"]["committed"], 3)

    def test_concurrency_cash_and_disk_are_independent_limits(self):
        self.write_project(
            hours={"day": 100, "week": 100, "month": 100},
            policy={
                "max_concurrent_gpus": 2,
                "max_grant_gpu_hours": 20,
                "max_grant_wall_hours": 10,
                "cash": {"currency": "GBP", "month": 10},
                "disk": {"max_per_job_gb": 100, "max_active_gb": 120},
            },
        )
        first = self.reserve("first", gpus=2, hours=4, cost=5, disk=80)
        self.assertEqual(first.returncode, 0, first.stdout)
        concurrency = self.reserve("too-many", gpus=1, hours=1, cost=1, disk=1)
        self.assertIn("concurrent GPU limit", concurrency.stdout)

        self.assertEqual(
            self.reconcile("first", 8, cost=5, retained_disk=80).returncode, 0
        )
        cash = self.reserve("too-costly", gpus=1, hours=1, cost=6, disk=1)
        self.assertIn("monthly cash limit", cash.stdout)
        disk = self.reserve("too-large", gpus=1, hours=1, cost=1, disk=101)
        self.assertIn("per-job disk limit", disk.stdout)
        retained = self.reserve("retained-limit", gpus=1, hours=1, cost=1, disk=50)
        self.assertIn("active disk limit", retained.stdout)

        released = self.run_cli(
            "gpu-disk-release", "--project", "synthetic-project",
            "--reservation-id", "first",
            "--evidence", "provider://disk/delete/receipt-1",
        )
        self.assertEqual(released.returncode, 0, released.stdout)
        after_release = self.reserve("after-release", gpus=1, hours=1, cost=1, disk=50)
        self.assertEqual(after_release.returncode, 0, after_release.stdout)

    def test_reserve_and_reconcile_are_idempotent_but_conflicts_fail(self):
        first = self.reserve("same", gpus=1, hours=2)
        second = self.reserve("same", gpus=1, hours=2)
        conflict = self.reserve("same", gpus=1, hours=3)
        self.assertEqual(first.returncode, 0)
        self.assertEqual(second.returncode, 0)
        self.assertIn("already_reserved", second.stdout)
        self.assertEqual(conflict.returncode, 1)

        first_rec = self.reconcile("same", 1)
        second_rec = self.reconcile("same", 1)
        conflict_rec = self.reconcile("same", 2)
        self.assertEqual(first_rec.returncode, 0)
        self.assertEqual(second_rec.returncode, 0)
        self.assertIn("already_reconciled", second_rec.stdout)
        self.assertEqual(conflict_rec.returncode, 1)

    def test_portfolio_audit_surfaces_overallocation(self):
        for slug, pct in (("one", 50), ("two", 40)):
            path = self.root / "projects" / slug / "project.json"
            path.parent.mkdir(parents=True)
            path.write_text(json.dumps({"slug": slug, "status": "active",
                                        "budget_pct_weekly": pct}))
        audit = self.run_cli("portfolio-audit")
        payload = json.loads(audit.stdout)
        self.assertEqual(audit.returncode, 1)
        self.assertEqual(payload["verdict"], "overallocated")
        self.assertEqual(payload["active_total_pct"], 100)

    def test_zero_token_budget_is_a_stop_not_free_access(self):
        path = self.root / "projects" / "synthetic-project" / "project.json"
        project = json.loads(path.read_text())
        project["budget_pct_weekly"] = 0
        path.write_text(json.dumps(project))
        gate = self.run_cli("gate", "--project", "synthetic-project")
        payload = json.loads(gate.stdout)
        self.assertEqual(gate.returncode, 1)
        self.assertEqual(payload["verdict"], "soft_stop")
        self.assertIn("no active weekly budget", payload["reason"])

    def test_unlimited_policy_clears_every_gpu_ceiling_but_keeps_accounting(self):
        self.write_project(
            hours={"day": 8, "week": 16, "month": 32},
            policy={
                "max_concurrent_gpus": 2,
                "max_grant_gpu_hours": 4,
                "max_grant_wall_hours": 4,
                "cash": {"currency": "GBP", "month": 10},
                "disk": {"max_per_job_gb": 20, "max_active_gb": 30},
            },
        )
        changed = self.run_cli(
            "gpu-policy",
            "--project",
            "synthetic-project",
            "--unlimited",
            "--authorized-by",
            "fixture-operator",
            "--note",
            "Synthetic scopes have infinite capacity",
        )
        self.assertEqual(changed.returncode, 0, changed.stdout + changed.stderr)

        project_path = self.root / "projects" / "synthetic-project" / "project.json"
        project = json.loads(project_path.read_text())
        self.assertEqual(
            project["gpu_hours"],
            {"day": None, "week": None, "month": None},
        )
        policy = project["gpu_policy"]
        self.assertEqual(policy["mode"], "unlimited")
        self.assertEqual(policy["authorized_by"], "fixture-operator")
        self.assertEqual(
            policy["authorization_note"],
            "Synthetic scopes have infinite capacity",
        )
        self.assertIsNone(policy["max_concurrent_gpus"])
        self.assertIsNone(policy["max_grant_gpu_hours"])
        self.assertIsNone(policy["max_grant_wall_hours"])
        self.assertEqual(
            policy["cash"],
            {"currency": "GBP", "month": None},
        )
        self.assertEqual(
            policy["disk"],
            {"max_per_job_gb": None, "max_active_gb": None},
        )

        admitted = self.run_cli(
            "gpu-reserve",
            "--project",
            "synthetic-project",
            "--job",
            "large-accounted-job",
            "--gpus",
            "1000",
            "--hours",
            "1000",
            "--disk-gb",
            "1000000000",
        )
        self.assertEqual(admitted.returncode, 0, admitted.stdout + admitted.stderr)
        receipt = json.loads(admitted.stdout)
        self.assertEqual(receipt["verdict"], "reserved")
        self.assertEqual(receipt["reservation"]["gpu_hours"], 1_000_000)

    def test_unlimited_policy_requires_attribution_and_no_mixed_limits(self):
        missing_attribution = self.run_cli(
            "gpu-policy",
            "--project",
            "synthetic-project",
            "--unlimited",
        )
        self.assertEqual(missing_attribution.returncode, 1)
        self.assertIn("requires --authorized-by and --note", missing_attribution.stdout)

        mixed = self.run_cli(
            "gpu-policy",
            "--project",
            "synthetic-project",
            "--unlimited",
            "--authorized-by",
            "fixture-operator",
            "--note",
            "explicit",
            "--max-concurrent-gpus",
            "8",
        )
        self.assertEqual(mixed.returncode, 1)
        self.assertIn("cannot be combined", mixed.stdout)


if __name__ == "__main__":
    unittest.main()
