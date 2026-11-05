#!/usr/bin/env python3
"""Small client for the local in-memory Bitwarden lease broker."""

from __future__ import annotations

import argparse
import json
import os
import socket
import sys
from pathlib import Path


DEFAULT_SOCKET = Path.home() / "Library/Caches/bitwarden-lease/broker.sock"


def request(socket_path: Path, payload: dict[str, object]) -> dict[str, object]:
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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--socket", type=Path, default=DEFAULT_SOCKET)
    parser.add_argument("operation", choices=("status", "unlock", "bw"))
    parser.add_argument("arguments", nargs=argparse.REMAINDER)
    options = parser.parse_args()
    payload: dict[str, object] = {"op": options.operation}
    if options.operation == "bw":
        payload["argv"] = options.arguments
    response = request(options.socket, payload)
    if options.operation == "bw":
        sys.stdout.write(str(response.get("stdout", "")))
        sys.stderr.write(str(response.get("stderr", "")))
        raise SystemExit(int(response.get("exit_code", 1)))
    json.dump(response, sys.stdout, sort_keys=True)
    sys.stdout.write("\n")
    raise SystemExit(0 if response.get("status") == "unlocked" else 1)


if __name__ == "__main__":
    main()
