#!/usr/bin/env python3
"""Exercise the bundled broker and installer without touching a real vault."""

from __future__ import annotations

import json
import importlib.util
import os
import plistlib
import shlex
import shutil
import socket
import stat
import subprocess
import sys
import tempfile
import time
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
BROKER = SKILL_ROOT / "scripts/bitwarden_lease_broker.py"
INSTALLER = SKILL_ROOT / "scripts/install_bitwarden_lease_broker.py"


def load_broker_module():
    spec = importlib.util.spec_from_file_location("bitwarden_lease_broker", BROKER)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_executable(path: Path, text: str) -> None:
    path.write_text(text)
    path.chmod(path.stat().st_mode | stat.S_IXUSR)


def request(socket_path: Path, payload: object) -> dict[str, object]:
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as connection:
        connection.connect(str(socket_path))
        connection.sendall(json.dumps(payload).encode() + b"\n")
        response = b""
        while not response.endswith(b"\n"):
            chunk = connection.recv(65536)
            if not chunk:
                break
            response += chunk
    return json.loads(response)


def run_broker_test(root: Path) -> None:
    bin_dir = root / "bin"
    bin_dir.mkdir()
    events = root / "events.jsonl"
    passwords = root / "passwords"
    passwords.write_text("wrong\nwrong-again\ncorrect\n")
    write_executable(
        bin_dir / "osascript",
        """#!/bin/sh
set -eu
attempt="$(($(grep -c '\"event\":\"prompt\"' "$BROKER_TEST_EVENTS" 2>/dev/null || true) + 1))"
printf '{\"event\":\"prompt\"}\\n' >>"$BROKER_TEST_EVENTS"
sed -n "${attempt}p" "$BROKER_TEST_PASSWORDS"
""",
    )
    write_executable(
        bin_dir / "bw",
        """#!/bin/sh
set -eu
if [ "$1" = unlock ]; then
  [ -z "${BW_BROKER_MASTER_PASSWORD:-}" ]
  password="$(cat)"
  printf '{\"event\":\"unlock\"}\\n' >>"$BROKER_TEST_EVENTS"
  [ "$password" = correct ] || exit 1
  printf session-test-value
  exit 0
fi
if [ "$1" = get ] && [ "$2" = password ]; then
  [ "${BW_SESSION:-}" = session-test-value ]
  printf 'secret-for-%s' "$3"
  exit 0
fi
exit 64
""",
    )
    socket_root = Path("/tmp") / f"bwls-{os.getpid()}"
    socket_root.mkdir(mode=0o700)
    socket_path = socket_root / "broker.sock"
    environment = os.environ.copy()
    environment.update(
        {
            "BROKER_TEST_EVENTS": str(events),
            "BROKER_TEST_PASSWORDS": str(passwords),
            "PATH": f"{bin_dir}:{environment['PATH']}",
        }
    )
    process = subprocess.Popen(
        [
            sys.executable,
            str(BROKER),
            "serve",
            "--socket",
            str(socket_path),
            "--lease-seconds",
            "86400",
        ],
        env=environment,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
        text=True,
    )
    try:
        for _ in range(100):
            if socket_path.exists():
                break
            if process.poll() is not None:
                raise AssertionError(f"broker exited: {process.stderr.read()}")
            time.sleep(0.02)
        else:
            raise AssertionError("broker socket did not appear")
        assert stat.S_IMODE(socket_path.parent.stat().st_mode) == 0o700
        assert stat.S_IMODE(socket_path.stat().st_mode) == 0o600
        initial_status = request(socket_path, {"op": "status"})
        assert initial_status == {"remaining_seconds": 0, "status": "locked"}
        assert not events.exists(), "status must not trigger a prompt or Bitwarden command"
        malformed = request(socket_path, ["not", "an", "object"])
        assert malformed["status"] == "error"
        assert "object" in str(malformed["error"])
        response = request(socket_path, {"op": "bw", "argv": ["get", "password", "item"]})
        assert response == {"exit_code": 0, "stderr": "", "stdout": "secret-for-item"}
        status = request(socket_path, {"op": "status"})
        assert status["status"] == "unlocked"
        assert 86390 <= status["remaining_seconds"] <= 86400
        assert "session" not in json.dumps(status).lower()
        rows = [json.loads(row) for row in events.read_text().splitlines()]
        assert [row["event"] for row in rows] == [
            "prompt",
            "unlock",
            "prompt",
            "unlock",
            "prompt",
            "unlock",
        ]
    finally:
        process.terminate()
        process.wait(timeout=5)
        socket_path.unlink(missing_ok=True)
        socket_root.rmdir()


def run_installer_test(root: Path) -> None:
    home = root / "home"
    home.mkdir()
    bin_dir = root / "installer-bin"
    bin_dir.mkdir()
    events = root / "launchctl-events"
    write_executable(
        bin_dir / "launchctl",
        """#!/bin/sh
printf '%s\\n' "$*" >>"$BROKER_TEST_LAUNCHCTL_EVENTS"
""",
    )
    environment = os.environ.copy()
    environment.update(
        {
            "BROKER_TEST_LAUNCHCTL_EVENTS": str(events),
            "HOME": str(home),
            "PATH": f"{bin_dir}:{environment['PATH']}",
        }
    )
    python_dir = root / "Python Runtimes"
    python_dir.mkdir()
    python_path = python_dir / "python3"
    python_path.symlink_to(sys.executable)
    completed = subprocess.run(
        [sys.executable, str(INSTALLER), "install", "--python", str(python_path)],
        env=environment,
        capture_output=True,
        text=True,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr
    plist_path = home / "Library/LaunchAgents/io.github.antreasantoniou.bitwarden-lease.plist"
    command_path = home / ".local/bin/bw-lease"
    plist = plistlib.loads(plist_path.read_bytes())
    assert plist["RunAtLoad"] is True
    assert plist["KeepAlive"] is True
    assert plist["EnvironmentVariables"]["PATH"].startswith("/opt/homebrew/bin:")
    assert stat.S_IMODE(plist_path.stat().st_mode) == 0o600
    assert stat.S_IMODE(command_path.stat().st_mode) == 0o700
    assert str(SKILL_ROOT) not in plist_path.read_text()
    installed_root = home / "Library/Application Support/BitwardenLease"
    assert (installed_root / "bitwarden_lease_broker.py").is_file()
    assert (installed_root / "bitwarden_lease_client.py").is_file()
    installed_text = plist_path.read_text() + command_path.read_text()
    assert ("axi" + "otic") not in installed_text.lower()
    command_argv = shlex.split(command_path.read_text().splitlines()[1])
    assert command_argv[:2] == ["exec", str(python_path)]


def run_installer_rejects_relative_python(root: Path) -> None:
    home = root / "relative-python-home"
    home.mkdir()
    completed = subprocess.run(
        [sys.executable, str(INSTALLER), "install", "--python", "python3"],
        env={**os.environ, "HOME": str(home)},
        capture_output=True,
        text=True,
        check=False,
    )
    assert completed.returncode != 0
    assert "absolute" in completed.stderr.lower()
    assert not (home / "Library/LaunchAgents").exists()


def run_timeout_test() -> None:
    broker = load_broker_module()
    lease = broker.VaultLease(86400)
    lease._session = "session-test-value"
    lease._expires_at = time.monotonic() + 86400
    real_run = broker.subprocess.run

    def timeout(*_args, **_kwargs):
        raise broker.subprocess.TimeoutExpired(cmd=["bw", "get"], timeout=30)

    broker.subprocess.run = timeout
    try:
        response = lease.run_bw(["get", "password", "item"])
    finally:
        broker.subprocess.run = real_run
    assert response == {
        "exit_code": 75,
        "stderr": "Bitwarden CLI operation timed out",
        "stdout": "",
    }


def run_unlock_timeout_test() -> None:
    broker = load_broker_module()
    lease = broker.VaultLease(86400)
    lease._prompt = lambda _attempt: "synthetic-password"
    real_run = broker.subprocess.run

    def timeout(*_args, **_kwargs):
        raise broker.subprocess.TimeoutExpired(cmd=["bw", "unlock"], timeout=30)

    broker.subprocess.run = timeout
    try:
        response = lease.unlock()
    finally:
        broker.subprocess.run = real_run
    assert response == {"error": "Bitwarden CLI unlock timed out", "status": "locked"}
    assert lease._session is None


def run_expiry_test() -> None:
    broker = load_broker_module()
    lease = broker.VaultLease(1)
    lease._session = "synthetic-session"
    lease._expires_at = time.monotonic() - 1
    lease.expire_if_needed()
    assert lease._session is None
    assert lease._expires_at == 0.0


def run_credential_option_rejection_test() -> None:
    broker = load_broker_module()
    lease = broker.VaultLease(86400)

    def must_not_unlock():
        raise AssertionError("credential-bearing caller options must fail before unlock")

    lease.unlock = must_not_unlock
    rejected = (
        ["get", "password", "item", "--session=value"],
        ["get", "password", "item", "--passwordfile=/tmp/input"],
        ["list", "items", "--passwordenv=NAME"],
    )
    for argv in rejected:
        response = lease.run_bw(argv)
        assert response == {
            "exit_code": 64,
            "stderr": "credential-bearing options are not allowed",
            "stdout": "",
        }


def run_invalid_session_test() -> None:
    broker = load_broker_module()
    lease = broker.VaultLease(86400)
    lease._session = "expired-synthetic-session"
    lease._expires_at = time.monotonic() + 86400
    real_run = broker.subprocess.run

    def fake_run(argv, **_kwargs):
        if argv == ["bw", "status"]:
            return subprocess.CompletedProcess(
                argv,
                0,
                stdout='{"status":"locked"}\n',
                stderr="",
            )
        return subprocess.CompletedProcess(
            argv,
            1,
            stdout="",
            stderr="Vault is locked.",
        )

    broker.subprocess.run = fake_run
    try:
        response = lease.run_bw(["get", "password", "item"])
    finally:
        broker.subprocess.run = real_run
    assert response["exit_code"] == 1
    assert lease.status() == {"remaining_seconds": 0, "status": "locked"}


def main() -> None:
    root = Path(tempfile.mkdtemp(prefix="bitwarden-lease-self-test-"))
    try:
        run_broker_test(root)
        run_timeout_test()
        run_unlock_timeout_test()
        run_expiry_test()
        run_credential_option_rejection_test()
        run_invalid_session_test()
        run_installer_test(root)
        run_installer_rejects_relative_python(root)
    finally:
        shutil.rmtree(root)
    print("bitwarden_lease_self_test=pass")


if __name__ == "__main__":
    main()
