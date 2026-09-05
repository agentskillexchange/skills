"""Synthetic integration fixtures; only TemporaryDirectory state and ephemeral ports."""
import importlib.util
import json
import os
import stat
from pathlib import Path
import sys
import tempfile
import threading
import unittest
import urllib.request
import urllib.error
from http.server import ThreadingHTTPServer
from unittest.mock import patch

PACKAGE = Path(__file__).resolve().parents[1]

class RuntimeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.setup_runtime()
        self.http = ThreadingHTTPServer(("127.0.0.1", 0), self.handler)
        self.port = self.http.server_address[1]
        self.url = f"http://127.0.0.1:{self.port}"
        self.thread = threading.Thread(target=self.http.serve_forever, daemon=True)
        self.thread.start()
        self.addCleanup(self.stop)

    def stop(self):
        self.http.shutdown()
        self.http.server_close()
        self.thread.join()

    def request(self, path="/api/state", payload=None, headers=None, raw=None):
        data = raw if raw is not None else (json.dumps(payload).encode() if payload is not None else None)
        hdr = {"Content-Type": "application/json"}
        hdr.update(headers or {})
        req = urllib.request.Request(self.url + path, data=data, headers=hdr)
        try:
            with urllib.request.urlopen(req, timeout=5) as response:
                return response.status, response.read()
        except urllib.error.HTTPError as error:
            return error.code, error.read()

    def test_empty_bootstrap(self):
        status, data = self.request()
        self.assertEqual(status, 200, data)
        self.assert_empty(json.loads(data))

    def test_host_and_origin_guards(self):
        self.assertEqual(self.request(headers={"Host": "evil.example"})[0], 403)
        self.assertEqual(self.request(self.mutation, {}, {"Origin": "https://evil.example"})[0], 403)
        self.assertEqual(self.request(self.mutation, {}, {"Content-Type": "text/plain"})[0], 415)

    def test_bounded_json_object(self):
        self.assertEqual(self.request(self.mutation, raw=b"[]")[0], 400)
        self.assertEqual(self.request(self.mutation, raw=b"{}" * 40000)[0], 413)

    def test_html_surfaces(self):
        for route in self.pages:
            code, body = self.request(route)
            self.assertEqual(code, 200)
            self.assertIn(b"<html", body.lower())

    def setup_runtime(self):
        sys.path.insert(0, str(PACKAGE / "scripts"))
        self.addCleanup(lambda: sys.path.remove(str(PACKAGE / "scripts")))
        with patch.dict(os.environ, {"BUTLER_ROOT": str(self.root / "data")}, clear=False):
            spec = importlib.util.spec_from_file_location("butler", PACKAGE / "scripts/butler.py")
            self.module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(self.module)
            sys.modules["butler"] = self.module
            spec = importlib.util.spec_from_file_location("butler_ui_isolated", PACKAGE / "scripts/webui.py")
            self.ui = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(self.ui)
        self.handler = self.ui.H
        self.mutation = "/api/event"
        self.pages = ["/"]

    def assert_empty(self, state):
        self.assertEqual(state["projects"], [])
        self.assertEqual(state["accounts"], [])
        self.assertEqual(state["fleet"], [])
        self.assertIsNone(state["real"])
        self.assertEqual(self.module.DEFAULT_CONFIG["accounts"], {})

    def test_traversal_and_nonfinite_gpu_rejected(self):
        with self.assertRaises(ValueError):
            self.module.project_path("../../escape")
        code, body = self.request("/api/gpu-log", {"project": "../../escape", "gpus": 1, "hours": 1})
        self.assertEqual(code, 400, body)
        code, body = self.request("/api/gpu-log", {"project": "fixture", "job": "fixture", "gpus": float("inf"), "hours": 1})
        self.assertEqual(code, 400, body)

    def test_browser_never_runs_remote_collection(self):
        synthetic_config = {**self.module.DEFAULT_CONFIG,
                            "machines": {"synthetic-remote": {"enabled": True,
                                         "ssh": "synthetic.invalid"}}}
        with patch.object(self.module, "config", return_value=synthetic_config), \
             patch.object(self.module, "collect_machine", return_value={"data": {"weighted": 0}}) as collector:
            for route, expected in (("/api/collect", 403), ("/disabled/collect", 404),
                                    ("/disabled/refresh", 404), ("/disabled/event", 404)):
                with self.subTest(route=route):
                    status, body = self.request(route, {})
                    self.assertEqual(status, expected, body)
                    collector.assert_not_called()

    def test_nonfinite_and_boolean_numeric_requests_never_mutate(self):
        self.module.save_json(self.module.ROOT / "config.json", {
            **self.module.DEFAULT_CONFIG,
            "accounts": {"synthetic": {"weekly_weighted_budget": 1000000}}})
        self.module.save_json(self.module.project_path("synthetic") / "project.json", {
            "budget_pct_weekly": 20, "status": "active", "gpu_hours": {}})
        before = {str(p): p.read_bytes() for p in self.module.ROOT.rglob("*") if p.is_file()}
        for value in (float("nan"), float("inf"), -float("inf"), True):
            cases = [("/api/normalize", {"target": value}),
                     ("/api/alloc", {"project": "synthetic", "pct": value}),
                     ("/api/config", {"account": "synthetic", "weekly_m": value}),
                     ("/api/gpu-log", {"project": "synthetic", "job": "synthetic", "gpus": value, "hours": 1})]
            for route, body in cases:
                with self.subTest(route=route, value=value):
                    self.assertEqual(self.request(route, body)[0], 400)
                    after = {str(p): p.read_bytes() for p in self.module.ROOT.rglob("*") if p.is_file()}
                    self.assertEqual(before, after)
        for route, body in [("/api/config", {"account": "synthetic", "weekly_m": 1e308}),
                            ("/api/gpu-log", {"project": "synthetic", "job": "synthetic", "gpus": 1e200, "hours": 1e200})]:
            self.assertEqual(self.request(route, body)[0], 400)
        self.assertEqual(self.request("/api/normalize", raw=b'{"target":1e999}')[0], 400)

    def test_private_state_modes_under_permissive_umask(self):
        previous = os.umask(0o022)
        try:
            code, body = self.request("/api/event", {"type": "note", "note": "synthetic private note"})
            self.assertEqual(code, 200, body)
            self.module.save_json(self.module.project_path("synthetic") / "project.json", {"budget_pct_weekly": 1})
            with self.module.gpu_ledger_lock():
                self.module.append_jsonl(self.module.GPU_LEDGER, {"type": "synthetic"})
        finally:
            os.umask(previous)
        self.assertEqual(stat.S_IMODE(self.module.ROOT.stat().st_mode), 0o700)
        for path in self.module.ROOT.rglob("*"):
            self.assertEqual(stat.S_IMODE(path.stat().st_mode), 0o700 if path.is_dir() else 0o600, path)

    def test_non_state_directory_is_not_chmodded_or_written(self):
        unrelated = self.root / "unrelated-workspace"
        unrelated.mkdir(mode=0o755)
        sentinel = unrelated / "unrelated.txt"
        sentinel.write_text("synthetic unrelated data")
        before = stat.S_IMODE(unrelated.stat().st_mode)
        with patch.object(self.module, "ROOT", unrelated):
            with self.assertRaises(ValueError):
                self.module.save_json(unrelated / "config.json", {})
        self.assertEqual(stat.S_IMODE(unrelated.stat().st_mode), before)
        self.assertEqual(list(unrelated.iterdir()), [sentinel])

    def test_html_security_headers(self):
        with urllib.request.urlopen(self.url + "/", timeout=5) as response:
            self.assertEqual(response.headers.get("X-Frame-Options"), "DENY")
            self.assertEqual(response.headers.get("X-Content-Type-Options"), "nosniff")
            self.assertIn("frame-ancestors 'none'", response.headers.get("Content-Security-Policy", ""))

if __name__ == "__main__": unittest.main()
