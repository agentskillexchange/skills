#!/usr/bin/env python3
"""Keep a Bitwarden CLI session in one local process for a bounded lease."""

from __future__ import annotations

import argparse
import json
import os
import socketserver
import subprocess
import threading
import time
from pathlib import Path
from typing import Any


DEFAULT_LEASE_SECONDS = 24 * 60 * 60
DEFAULT_BW_TIMEOUT_SECONDS = 30
ALLOWED_BW_COMMANDS = {"get", "list", "sync", "status"}
CREDENTIAL_OPTION_PREFIXES = ("--session", "--passwordfile", "--passwordenv")


def _json_line(payload: dict[str, Any]) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":")).encode() + b"\n"


class VaultLease:
    def __init__(self, lease_seconds: int) -> None:
        self._lease_seconds = lease_seconds
        self._session: str | None = None
        self._expires_at = 0.0
        self._lock = threading.Lock()

    def _valid(self) -> bool:
        return bool(self._session) and time.monotonic() < self._expires_at

    def _clear_locked(self) -> None:
        self._session = None
        self._expires_at = 0.0

    def expire_if_needed(self) -> None:
        """Remove an expired session even when no client is making requests."""
        with self._lock:
            if not self._valid():
                self._clear_locked()

    def status(self) -> dict[str, Any]:
        with self._lock:
            if not self._valid():
                self._clear_locked()
                return {"remaining_seconds": 0, "status": "locked"}
            return {
                "remaining_seconds": max(0, int(self._expires_at - time.monotonic())),
                "status": "unlocked",
            }

    def unlock(self) -> dict[str, Any]:
        with self._lock:
            if self._valid():
                return {
                    "remaining_seconds": max(0, int(self._expires_at - time.monotonic())),
                    "status": "unlocked",
                }
            self._clear_locked()
            for attempt in range(1, 4):
                password = self._prompt(attempt)
                if password is None:
                    return {"error": "unlock cancelled", "status": "locked"}
                try:
                    completed = subprocess.run(
                        [
                            "bw",
                            "unlock",
                            "--raw",
                            "--passwordfile",
                            "/dev/stdin",
                        ],
                        capture_output=True,
                        text=True,
                        input=password,
                        check=False,
                        timeout=DEFAULT_BW_TIMEOUT_SECONDS,
                    )
                except subprocess.TimeoutExpired:
                    password = ""
                    self._clear_locked()
                    return {"error": "Bitwarden CLI unlock timed out", "status": "locked"}
                password = ""
                candidate = completed.stdout.strip()
                if completed.returncode == 0 and candidate:
                    self._session = candidate
                    self._expires_at = time.monotonic() + self._lease_seconds
                    return {
                        "remaining_seconds": self._lease_seconds,
                        "status": "unlocked",
                    }
            return {"error": "three unlock attempts failed", "status": "locked"}

    @staticmethod
    def _prompt(attempt: int) -> str | None:
        script = (
            "try\n"
            f'display dialog "Unlock Bitwarden for the next 24 hours. Attempt {attempt} of 3." '
            'default answer "" with hidden answer buttons {"Cancel", "Unlock"} '
            'default button "Unlock" cancel button "Cancel" with title "Bitwarden Lease"\n'
            "text returned of result\n"
            "on error number -128\n"
            'return "__BW_BROKER_CANCELLED__"\n'
            "end try\n"
        )
        completed = subprocess.run(
            ["osascript", "-e", script],
            capture_output=True,
            text=True,
            check=False,
        )
        if completed.returncode != 0:
            return None
        password = completed.stdout.rstrip("\r\n")
        if password == "__BW_BROKER_CANCELLED__":
            return None
        return password

    def run_bw(self, argv: list[str]) -> dict[str, Any]:
        if not argv or argv[0] not in ALLOWED_BW_COMMANDS:
            return {"exit_code": 64, "stderr": "Bitwarden command is not allowed", "stdout": ""}
        if any(
            value == prefix or value.startswith(prefix + "=")
            for value in argv
            for prefix in CREDENTIAL_OPTION_PREFIXES
        ):
            return {"exit_code": 64, "stderr": "credential-bearing options are not allowed", "stdout": ""}
        state = self.unlock()
        if state["status"] != "unlocked":
            return {"exit_code": 77, "stderr": str(state.get("error", "vault locked")), "stdout": ""}
        environment = os.environ.copy()
        environment["BW_SESSION"] = self._session or ""
        try:
            completed = subprocess.run(
                ["bw", *argv],
                env=environment,
                capture_output=True,
                text=True,
                check=False,
                timeout=DEFAULT_BW_TIMEOUT_SECONDS,
            )
        except subprocess.TimeoutExpired:
            return {
                "exit_code": 75,
                "stderr": "Bitwarden CLI operation timed out",
                "stdout": "",
            }
        if completed.returncode != 0:
            self._clear_if_cli_reports_locked(environment)
        elif argv[0] == "status":
            self._clear_if_status_is_locked(completed.stdout)
        return {
            "exit_code": completed.returncode,
            "stderr": completed.stderr,
            "stdout": completed.stdout,
        }

    def _clear_if_cli_reports_locked(self, environment: dict[str, str]) -> None:
        try:
            completed = subprocess.run(
                ["bw", "status"],
                env=environment,
                capture_output=True,
                text=True,
                check=False,
                timeout=DEFAULT_BW_TIMEOUT_SECONDS,
            )
        except subprocess.TimeoutExpired:
            return
        if completed.returncode == 0:
            self._clear_if_status_is_locked(completed.stdout)

    def _clear_if_status_is_locked(self, stdout: str) -> None:
        try:
            status = json.loads(stdout).get("status")
        except (json.JSONDecodeError, AttributeError):
            return
        if status != "unlocked":
            with self._lock:
                self._clear_locked()


class BrokerHandler(socketserver.StreamRequestHandler):
    def handle(self) -> None:
        try:
            request = json.loads(self.rfile.readline())
            if not isinstance(request, dict):
                raise ValueError("request must be a JSON object")
            operation = request.get("op")
            if operation == "status":
                response = self.server.lease.status()  # type: ignore[attr-defined]
            elif operation == "unlock":
                response = self.server.lease.unlock()  # type: ignore[attr-defined]
            elif operation == "bw":
                argv = request.get("argv")
                if not isinstance(argv, list) or not all(isinstance(v, str) for v in argv):
                    raise ValueError("argv must be an array of strings")
                response = self.server.lease.run_bw(argv)  # type: ignore[attr-defined]
            else:
                response = {"error": "unknown operation", "status": "error"}
        except (json.JSONDecodeError, ValueError) as error:
            response = {"error": str(error), "status": "error"}
        self.wfile.write(_json_line(response))


class BrokerServer(socketserver.ThreadingUnixStreamServer):
    daemon_threads = True
    allow_reuse_address = True

    def __init__(self, socket_path: Path, lease_seconds: int) -> None:
        if socket_path.exists():
            socket_path.unlink()
        socket_path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
        os.chmod(socket_path.parent, 0o700)
        self.lease = VaultLease(lease_seconds)
        super().__init__(str(socket_path), BrokerHandler)
        os.chmod(socket_path, 0o600)

    def service_actions(self) -> None:
        self.lease.expire_if_needed()


def serve(socket_path: Path, lease_seconds: int) -> None:
    with BrokerServer(socket_path, lease_seconds) as server:
        server.serve_forever(poll_interval=0.25)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    server = subparsers.add_parser("serve")
    server.add_argument("--socket", type=Path, required=True)
    server.add_argument("--lease-seconds", type=int, default=DEFAULT_LEASE_SECONDS)
    return parser.parse_args()


def main() -> None:
    arguments = parse_args()
    if arguments.command == "serve":
        serve(arguments.socket, arguments.lease_seconds)


if __name__ == "__main__":
    main()
