"""Behavioral tests for aggregate Butler GPU admission scopes."""

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


class ButlerGpuScopeTests(unittest.TestCase):
    """Exercise scoped GPU admission through the public CLI."""

    def setUp(self) -> None:
        """Create an isolated two-project Synthetic scope ledger."""
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.env = {**os.environ, "BUTLER_ROOT": str(self.root)}
        self.write_project(ADMISSION_PROJECT, {"day": 10, "week": 10, "month": 10})
        self.write_project(LEGACY_PROJECT, {"day": 1, "week": 1, "month": 1})
        self.write_config(
            {
                "shared-scope": {
                    "members": [ADMISSION_PROJECT, LEGACY_PROJECT],
                    "admission_project": ADMISSION_PROJECT,
                }
            }
        )

    def tearDown(self) -> None:
        """Remove the isolated Butler root."""
        self.tmp.cleanup()

    def write_config(self, scopes: dict[str, Any] | None) -> None:
        """Write only the global configuration needed by GPU scope tests."""
        config: dict[str, Any] = {}
        if scopes is not None:
            config["gpu_scopes"] = scopes
        (self.root / "config.json").write_text(json.dumps(config))

    def write_project(
        self,
        slug: str,
        hours: dict[str, float],
        policy: dict[str, Any] | None = None,
    ) -> None:
        """Create a registered project with controlled GPU limits."""
        project: dict[str, Any] = {
            "slug": slug,
            "roots": [str(self.root / "work" / slug)],
            "budget_pct_weekly": 10,
            "accounts": ["personal"],
            "gpu_hours": hours,
            "status": "active",
        }
        if policy is not None:
            project["gpu_policy"] = policy
        path = self.root / "projects" / slug / "project.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(project))

    def write_events(self, *events: dict[str, Any]) -> None:
        """Seed exact historical ledger rows."""
        path = self.root / "gpu" / "ledger.jsonl"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("".join(json.dumps(event) + "\n" for event in events))

    def run_cli(self, *args: str) -> subprocess.CompletedProcess[str]:
        """Run Butler against the isolated root."""
        return subprocess.run(
            [sys.executable, str(CLI), *args],
            env=self.env,
            text=True,
            capture_output=True,
        )

    def ledger(self) -> list[dict[str, Any]]:
        """Read the isolated ledger, if one exists."""
        path = self.root / "gpu" / "ledger.jsonl"
        if not path.exists():
            return []
        return [json.loads(line) for line in path.read_text().splitlines()]

    @staticmethod
    def reservation(
        project: str, reservation_id: str, **overrides: Any
    ) -> dict[str, Any]:
        """Build a literal-compatible v2 reservation row."""
        event: dict[str, Any] = {
            "type": "reservation",
            "schema_version": 2,
            "ts": dt.datetime.now(dt.timezone.utc).isoformat(),
            "project": project,
            "reservation_id": reservation_id,
            "job": reservation_id,
            "gpus": 1.0,
            "hours": 2.0,
            "gpu_hours": 2.0,
            "estimated_cost": None,
            "currency": "GBP",
            "disk_gb": 0.0,
            "note": "",
        }
        event.update(overrides)
        return event

    def test_owner_uses_aggregate_usage_and_only_owner_limits(self) -> None:
        """A member's burn counts, while its local budget does not govern admission."""
        self.write_events(
            {
                "type": "legacy_usage",
                "ts": dt.datetime.now(dt.timezone.utc).isoformat(),
                "project": LEGACY_PROJECT,
                "job": "legacy-burn",
                "gpu_hours": 6.0,
            }
        )

        allowed = self.run_cli(
            "gpu-gate", "--project", ADMISSION_PROJECT, "--request", "4"
        )
        denied = self.run_cli(
            "gpu-gate", "--project", ADMISSION_PROJECT, "--request", "4.1"
        )

        self.assertEqual(allowed.returncode, 0, allowed.stdout + allowed.stderr)
        payload = json.loads(allowed.stdout)
        self.assertEqual(payload["windows"]["day"]["committed"], 6.0)
        self.assertEqual(payload["windows"]["day"]["budget"], 10)
        self.assertEqual(payload["windows"]["day"]["after_request"], 10.0)
        self.assertEqual(denied.returncode, 1, denied.stdout + denied.stderr)
        self.assertIn("gpu day budget", denied.stdout)

    def test_unlimited_scope_overrides_every_member_capacity_ceiling(self) -> None:
        """Scope policy applies to current and future members, not one project file."""
        self.write_project(
            ADMISSION_PROJECT,
            {"day": 1, "week": 1, "month": 1},
            {
                "max_concurrent_gpus": 1,
                "max_grant_gpu_hours": 1,
                "max_grant_wall_hours": 1,
                "cash": {"currency": "GBP", "month": 1},
                "disk": {"max_per_job_gb": 1, "max_active_gb": 1},
            },
        )
        self.write_config(
            {
                "shared-scope": {
                    "members": [ADMISSION_PROJECT, LEGACY_PROJECT],
                    "admission_project": ADMISSION_PROJECT,
                    "capacity_mode": "unlimited",
                    "authorized_by": "fixture-operator",
                    "authorization_note": "Synthetic scope has infinite capacity",
                }
            }
        )

        gate = self.run_cli(
            "gpu-gate",
            "--project",
            ADMISSION_PROJECT,
            "--request",
            "1000000",
            "--gpus",
            "1000",
            "--hours",
            "1000",
            "--disk-gb",
            "1000000000",
        )

        self.assertEqual(gate.returncode, 0, gate.stdout + gate.stderr)
        payload = json.loads(gate.stdout)
        self.assertEqual(payload["verdict"], "proceed")
        self.assertTrue(
            all(window["budget"] is None for window in payload["windows"].values())
        )
        self.assertIsNone(payload["checks"]["concurrency"]["limit"])
        self.assertIsNone(payload["checks"]["disk"]["per_job_limit_gb"])
        self.assertIsNone(payload["checks"]["disk"]["active_limit_gb"])
        self.assertIsNone(payload["checks"]["cash"]["month_limit"])

    def test_member_holds_count_against_owner_policy(self) -> None:
        """Scoped concurrency, cash, and disk checks include every member hold."""
        self.write_project(
            ADMISSION_PROJECT,
            {"day": 100, "week": 100, "month": 100},
            {
                "max_concurrent_gpus": 2,
                "cash": {"currency": "GBP", "month": 5},
                "disk": {"max_active_gb": 50},
            },
        )
        self.write_events(
            self.reservation(
                LEGACY_PROJECT,
                "legacy-active",
                gpus=2.0,
                hours=1.0,
                gpu_hours=2.0,
                estimated_cost=4.0,
                disk_gb=40.0,
            )
        )

        gate = self.run_cli(
            "gpu-gate",
            "--project",
            ADMISSION_PROJECT,
            "--request",
            "1",
            "--gpus",
            "1",
            "--hours",
            "1",
            "--estimated-cost",
            "2",
            "--disk-gb",
            "20",
        )

        self.assertEqual(gate.returncode, 1, gate.stdout + gate.stderr)
        self.assertIn("concurrent GPU limit", gate.stdout)
        self.assertIn("monthly cash limit", gate.stdout)
        self.assertIn("active disk limit", gate.stdout)

    def test_parallel_owner_reservations_aggregate_members_atomically(self) -> None:
        """Concurrent admissions cannot reuse the same scoped capacity."""
        self.write_events(
            {
                "type": "legacy_usage",
                "ts": dt.datetime.now(dt.timezone.utc).isoformat(),
                "project": LEGACY_PROJECT,
                "job": "legacy-burn",
                "gpu_hours": 9.0,
            }
        )
        base = [
            sys.executable,
            str(CLI),
            "gpu-reserve",
            "--project",
            ADMISSION_PROJECT,
            "--gpus",
            "1",
            "--hours",
            "1",
        ]
        processes = [
            subprocess.Popen(
                base + ["--job", f"scoped-{index}"],
                env=self.env,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            for index in range(4)
        ]
        results = [
            process.communicate() + (process.returncode,) for process in processes
        ]

        self.assertEqual([result[2] for result in results].count(0), 1, results)
        owner_rows = [
            event
            for event in self.ledger()
            if event.get("type") == "reservation"
            and event.get("project") == ADMISSION_PROJECT
        ]
        self.assertEqual(len(owner_rows), 1)

    def test_legacy_member_rejects_preview_and_new_reservation(self) -> None:
        """Only the configured admission project may create scoped commitments."""
        gate = self.run_cli("gpu-gate", "--project", LEGACY_PROJECT, "--request", "1")
        reserve = self.run_cli(
            "gpu-reserve",
            "--project",
            LEGACY_PROJECT,
            "--job",
            "new-legacy",
            "--gpus",
            "1",
            "--hours",
            "1",
        )

        self.assertEqual(gate.returncode, 1, gate.stdout + gate.stderr)
        self.assertEqual(json.loads(gate.stdout)["verdict"], "invalid")
        self.assertIn(ADMISSION_PROJECT, gate.stdout)
        self.assertEqual(reserve.returncode, 1, reserve.stdout + reserve.stderr)
        self.assertEqual(json.loads(reserve.stdout)["verdict"], "invalid")
        self.assertEqual(self.ledger(), [])

    def test_exact_legacy_replay_precedes_admission_rejection(self) -> None:
        """A retry of an old member reservation remains safely idempotent."""
        old = self.reservation(LEGACY_PROJECT, "old-run")
        self.write_events(old)

        replay = self.run_cli(
            "gpu-reserve",
            "--project",
            LEGACY_PROJECT,
            "--job",
            "old-run",
            "--gpus",
            "1",
            "--hours",
            "2",
        )
        renamed = self.run_cli(
            "gpu-reserve",
            "--project",
            LEGACY_PROJECT,
            "--job",
            "renamed-run",
            "--reservation-id",
            "old-run",
            "--gpus",
            "1",
            "--hours",
            "2",
        )
        renoted = self.run_cli(
            "gpu-reserve",
            "--project",
            LEGACY_PROJECT,
            "--job",
            "old-run",
            "--gpus",
            "1",
            "--hours",
            "2",
            "--note",
            "changed",
        )
        conflict = self.run_cli(
            "gpu-reserve",
            "--project",
            LEGACY_PROJECT,
            "--job",
            "old-run",
            "--gpus",
            "1",
            "--hours",
            "3",
        )

        self.assertEqual(replay.returncode, 0, replay.stdout + replay.stderr)
        self.assertEqual(json.loads(replay.stdout)["verdict"], "already_reserved")
        self.assertEqual(renamed.returncode, 1, renamed.stdout + renamed.stderr)
        self.assertEqual(renoted.returncode, 1, renoted.stdout + renoted.stderr)
        self.assertEqual(conflict.returncode, 1, conflict.stdout + conflict.stderr)
        self.assertEqual(len(self.ledger()), 1)

    def test_reconcile_and_disk_release_remain_exact_project_operations(self) -> None:
        """Legacy reservations still finish and release disk through their own slug."""
        old = self.reservation(LEGACY_PROJECT, "old-disk", disk_gb=10.0)
        self.write_events(old)

        wrong_project = self.run_cli(
            "gpu-reconcile",
            "--project",
            ADMISSION_PROJECT,
            "--reservation-id",
            "old-disk",
            "--actual-gpu-hours",
            "1",
            "--retained-disk-gb",
            "10",
        )
        reconciled = self.run_cli(
            "gpu-reconcile",
            "--project",
            LEGACY_PROJECT,
            "--reservation-id",
            "old-disk",
            "--actual-gpu-hours",
            "1",
            "--retained-disk-gb",
            "10",
        )
        wrong_release = self.run_cli(
            "gpu-disk-release",
            "--project",
            ADMISSION_PROJECT,
            "--reservation-id",
            "old-disk",
            "--evidence",
            "provider://receipt/must-not-release",
        )
        released = self.run_cli(
            "gpu-disk-release",
            "--project",
            LEGACY_PROJECT,
            "--reservation-id",
            "old-disk",
            "--evidence",
            "provider://receipt/disk-deleted",
        )

        self.assertEqual(wrong_project.returncode, 1, wrong_project.stdout)
        self.assertIn("unknown reservation id", wrong_project.stdout)
        self.assertEqual(
            reconciled.returncode, 0, reconciled.stdout + reconciled.stderr
        )
        self.assertEqual(wrong_release.returncode, 1, wrong_release.stdout)
        self.assertIn("requires a reconciled reservation", wrong_release.stdout)
        self.assertEqual(released.returncode, 0, released.stdout + released.stderr)

    def test_scope_configuration_rejects_invalid_topology(self) -> None:
        """Malformed scope topology fails closed before GPU admission."""
        invalid_scopes = {
            "overlap": {
                "shared-scope": {
                    "members": [ADMISSION_PROJECT, LEGACY_PROJECT],
                    "admission_project": ADMISSION_PROJECT,
                },
                "other": {
                    "members": [LEGACY_PROJECT],
                    "admission_project": LEGACY_PROJECT,
                },
            },
            "missing_member": {
                "shared-scope": {
                    "members": [ADMISSION_PROJECT, "missing-project"],
                    "admission_project": ADMISSION_PROJECT,
                }
            },
            "invalid_owner": {
                "shared-scope": {
                    "members": [ADMISSION_PROJECT, LEGACY_PROJECT],
                    "admission_project": "outside-project",
                }
            },
        }

        for case, scopes in invalid_scopes.items():
            with self.subTest(case=case):
                self.write_config(scopes)
                gate = self.run_cli(
                    "gpu-gate", "--project", ADMISSION_PROJECT, "--request", "1"
                )
                self.assertEqual(gate.returncode, 1, gate.stdout + gate.stderr)
                self.assertEqual(json.loads(gate.stdout)["verdict"], "invalid")

    def test_malformed_config_json_fails_closed(self) -> None:
        """A damaged config cannot silently disable an intended GPU scope."""
        (self.root / "config.json").write_text('{"gpu_scopes":')

        gate = self.run_cli(
            "gpu-gate", "--project", ADMISSION_PROJECT, "--request", "1"
        )
        reserve = self.run_cli(
            "gpu-reserve",
            "--project",
            ADMISSION_PROJECT,
            "--job",
            "must-not-admit",
            "--gpus",
            "1",
            "--hours",
            "1",
        )

        self.assertEqual(gate.returncode, 1, gate.stdout + gate.stderr)
        self.assertEqual(json.loads(gate.stdout)["verdict"], "invalid")
        self.assertEqual(reserve.returncode, 1, reserve.stdout + reserve.stderr)
        self.assertEqual(json.loads(reserve.stdout)["verdict"], "invalid")
        self.assertEqual(self.ledger(), [])

    def test_cross_member_duplicate_reservation_ids_fail_closed(self) -> None:
        """A corrupted scope cannot double-count one reservation identity."""
        for reservation_id in ("duplicate", 7):
            with self.subTest(reservation_id=reservation_id):
                owner = self.reservation(ADMISSION_PROJECT, "placeholder")
                legacy = self.reservation(LEGACY_PROJECT, "placeholder")
                owner["reservation_id"] = reservation_id
                legacy["reservation_id"] = reservation_id
                self.write_events(owner, legacy)

                gate = self.run_cli(
                    "gpu-gate", "--project", ADMISSION_PROJECT, "--request", "1"
                )
                reserve = self.run_cli(
                    "gpu-reserve",
                    "--project",
                    ADMISSION_PROJECT,
                    "--job",
                    "fresh",
                    "--gpus",
                    "1",
                    "--hours",
                    "1",
                )

                self.assertEqual(gate.returncode, 1, gate.stdout + gate.stderr)
                self.assertEqual(json.loads(gate.stdout)["verdict"], "invalid")
                self.assertEqual(reserve.returncode, 1, reserve.stdout + reserve.stderr)
                self.assertEqual(len(self.ledger()), 2)

    def test_owner_cannot_reuse_reservation_id_owned_by_legacy_member(self) -> None:
        """Admission prevents creating a cross-member identity collision."""
        self.write_events(self.reservation(LEGACY_PROJECT, "legacy-owned"))

        reserve = self.run_cli(
            "gpu-reserve",
            "--project",
            ADMISSION_PROJECT,
            "--job",
            "owner-job",
            "--reservation-id",
            "legacy-owned",
            "--gpus",
            "1",
            "--hours",
            "2",
        )

        self.assertEqual(reserve.returncode, 1, reserve.stdout + reserve.stderr)
        self.assertEqual(json.loads(reserve.stdout)["verdict"], "invalid")
        self.assertIn(LEGACY_PROJECT, reserve.stdout)
        self.assertEqual(len(self.ledger()), 1)

    def test_absent_gpu_scopes_preserves_project_local_admission(self) -> None:
        """Projects retain legacy behavior when aggregate scopes are not configured."""
        self.write_config(None)

        gate = self.run_cli("gpu-gate", "--project", LEGACY_PROJECT, "--request", "1")
        reserve = self.run_cli(
            "gpu-reserve",
            "--project",
            LEGACY_PROJECT,
            "--job",
            "unscoped",
            "--gpus",
            "1",
            "--hours",
            "1",
        )

        self.assertEqual(gate.returncode, 0, gate.stdout + gate.stderr)
        self.assertEqual(reserve.returncode, 0, reserve.stdout + reserve.stderr)
        self.assertEqual(json.loads(reserve.stdout)["verdict"], "reserved")


if __name__ == "__main__":
    unittest.main()
