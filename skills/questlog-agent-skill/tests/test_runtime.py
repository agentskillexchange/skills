"""Synthetic integration fixtures; only TemporaryDirectory state and ephemeral ports."""
import importlib.util
import json
import os
from pathlib import Path
import sys
import tempfile
import threading
import subprocess
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
        with patch.dict(os.environ, {"QUESTLOG_ROOT": str(self.root / "data")}):
            spec = importlib.util.spec_from_file_location("questlog_isolated", PACKAGE / "ui/server.py")
            self.module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(self.module)
        self.assertFalse(self.module.REPO.exists(), "import must not create state")
        self.module.initialize()
        self.handler = self.module.Handler
        self.mutation = "/api/capture"
        self.pages = ["/", "/bar", "/quickadd"]

    def assert_empty(self, state):
        self.assertEqual(state["workstreams"], [])
        self.assertEqual(state["inbox"], [])
        self.assertIsNone(state["now"])
        self.assertEqual(state["journal"], [])

    def test_optimistic_lock_rejects_stale_content(self):
        revision = json.loads(self.request()[1])["head"]
        hdr = {"If-Match": revision}
        self.assertEqual(self.request("/api/capture", {"text": "synthetic first"}, hdr)[0], 200)
        self.assertEqual(self.request("/api/capture", {"text": "synthetic stale"}, hdr)[0], 409)
        state = json.loads(self.request()[1])
        self.assertEqual(len(state["inbox"]), 1)
        self.assertNotIn("synthetic stale", self.module.LEDGER.read_text())
        self.assertEqual(self.request("/api/capture", {"text": "missing revision"})[0], 428)

    def test_structured_mutation_and_input_boundaries(self):
        revision = json.loads(self.request()[1])["head"]
        code, body = self.request("/api/new", {"title": "Synthetic <img onerror=alert(1)>\n## injected"}, {"If-Match": revision})
        self.assertEqual(code, 200, body)
        state = json.loads(self.request()[1])
        self.assertEqual(len(state["workstreams"]), 1)
        self.assertNotIn("\n", state["workstreams"][0]["goal"])
        slug = state["workstreams"][0]["slug"]
        code, body = self.request("/api/mutate", {"slug": slug, "op": "state", "value": "hot"}, {"If-Match": state["head"]})
        self.assertEqual(code, 200, body)
        self.assertEqual(json.loads(self.request()[1])["workstreams"][0]["state"], "hot")

    def test_parallel_capture_keeps_all_notes(self):
        errors = []
        def capture(i):
            err = self.module.do_capture(f"synthetic concurrent {i}")
            if err:
                errors.append(err)
        workers = [threading.Thread(target=capture, args=(i,)) for i in range(20)]
        for worker in workers: worker.start()
        for worker in workers: worker.join()
        self.assertEqual(errors, [])
        self.assertEqual(len(self.module.full_state()["inbox"]), 20)

    def test_instructions_are_local_only(self):
        code, body = self.request("/api/action", {"slug": "../../escape", "text": "synthetic instruction"})
        self.assertEqual(code, 200, body)
        queue = json.loads(self.request("/api/queue")[1])
        self.assertEqual(len(queue["pending"]), 1)
        self.assertEqual(queue["done"], [])
        self.assertEqual(queue["pending"][0]["status"], "pending")

    def test_waiting_reports_are_local_and_preserve_waiting_date(self):
        fixture = "\n## synthetic-wait [life] [warm]\nWAITING: Example Person — synthetic item — since 2000-01-01 — chase 3d\n"
        self.assertIsNone(self.module.cas_commit(lambda content: (content + fixture, None), "synthetic waiting fixture"))
        before = self.module.full_state()["workstreams"][0]["waitings"]
        for tag in ("replied", "chased"):
            self.assertIsNone(self.module.do_capture("synthetic-wait: Example Person", tag))
            self.assertEqual(self.module.full_state()["workstreams"][0]["waitings"], before)
        self.assertEqual(len(self.module.full_state()["inbox"]), 2)
        code, page = self.request("/")
        self.assertEqual(code, 200)
        text = page.decode()
        self.assertIn("reply reported locally — review waiting item", text)
        self.assertIn("chase reported locally — waiting date unchanged", text)
        self.assertNotIn("replied — resolving", text)
        self.assertNotIn("chased — clock resets", text)

    def test_git_history_is_opt_in_and_commits_only_ledger(self):
        self.assertFalse((self.module.REPO / ".git").exists())
        self.assertIsNone(self.module.initialize_git())
        before = self.module.full_state()
        self.assertEqual(len(before["journal"]), 1)
        unrelated = self.module.REPO / "synthetic-unrelated.txt"
        unrelated.write_text("synthetic staged file")
        self.assertEqual(self.module.git("add", "--", unrelated.name).returncode, 0)
        self.assertIsNone(self.module.do_capture("synthetic history note"))
        after = self.module.full_state()
        self.assertEqual(len(after["journal"]), 2)
        self.assertNotEqual(before["git_head"], after["git_head"])
        changed = self.module.git("show", "--format=", "--name-only", "HEAD").stdout.splitlines()
        self.assertEqual(changed, ["LEDGER.md"])
        self.assertIn(unrelated.name, self.module.git("diff", "--cached", "--name-only").stdout)
        code, _ = self.request("/api/capture", {"text": "synthetic stale history"}, {"If-Match": before["head"]})
        self.assertEqual(code, 409)
        self.assertEqual(after["git_head"], self.module.full_state()["git_head"])

    def test_git_failure_reports_saved_but_uncommitted(self):
        self.assertIsNone(self.module.initialize_git())
        original_git = self.module.git
        def fail_commit(*args):
            if "commit" in args:
                return subprocess.CompletedProcess(args, 1, "", "synthetic failure")
            return original_git(*args)
        with patch.object(self.module, "git", side_effect=fail_commit):
            error = self.module.do_capture("synthetic saved note")
        self.assertIn("ledger saved but Git commit failed", error)
        self.assertIn("synthetic saved note", self.module.LEDGER.read_text())
        self.assertTrue(self.module.full_state()["dirty"])

    def test_cross_process_capture_preserves_history(self):
        self.assertIsNone(self.module.initialize_git())
        children = [subprocess.Popen([sys.executable, str(PACKAGE / "scripts/ledger.py"),
                    "capture", f"synthetic process {i}"], stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE, text=True,
                    env={**os.environ, "QUESTLOG_ROOT": str(self.module.REPO)}) for i in range(6)]
        completed = [(child, child.communicate(timeout=20)) for child in children]
        for child, (output, error) in completed:
            self.assertEqual(child.returncode, 0, output + error)
        state = self.module.full_state()
        self.assertEqual(len(state["inbox"]), 6)
        self.assertEqual(len(state["journal"]), 7)

if __name__ == "__main__": unittest.main()
