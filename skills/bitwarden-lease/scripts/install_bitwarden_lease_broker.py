#!/usr/bin/env python3
"""Install the Bitwarden lease broker as an owner-only macOS LaunchAgent."""

from __future__ import annotations

import argparse
import os
import plistlib
import shlex
import shutil
import subprocess
from pathlib import Path


LABEL = "io.github.antreasantoniou.bitwarden-lease"


def _atomic_copy(source: Path, target: Path, mode: int) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = target.with_suffix(target.suffix + ".new")
    shutil.copyfile(source, temporary)
    os.chmod(temporary, mode)
    os.replace(temporary, target)


def _atomic_plist(payload: dict[str, object], target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = target.with_suffix(".plist.new")
    temporary.write_bytes(plistlib.dumps(payload, sort_keys=True))
    os.chmod(temporary, 0o600)
    os.replace(temporary, target)


def install(python: Path) -> None:
    source_root = Path(__file__).resolve().parent
    home = Path.home()
    install_root = home / "Library/Application Support/BitwardenLease"
    cache_root = home / "Library/Caches/bitwarden-lease"
    launch_agents = home / "Library/LaunchAgents"
    local_bin = home / ".local/bin"
    for directory in (install_root, cache_root, launch_agents, local_bin):
        directory.mkdir(mode=0o700, parents=True, exist_ok=True)
    os.chmod(install_root, 0o700)
    os.chmod(cache_root, 0o700)

    installed_broker = install_root / "bitwarden_lease_broker.py"
    installed_client = install_root / "bitwarden_lease_client.py"
    _atomic_copy(source_root / installed_broker.name, installed_broker, 0o700)
    _atomic_copy(source_root / installed_client.name, installed_client, 0o700)

    socket_path = cache_root / "broker.sock"
    plist_path = launch_agents / f"{LABEL}.plist"
    plist = {
        "EnvironmentVariables": {
            "PATH": "/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin",
        },
        "KeepAlive": True,
        "Label": LABEL,
        "ProcessType": "Background",
        "ProgramArguments": [
            str(python),
            str(installed_broker),
            "serve",
            "--socket",
            str(socket_path),
            "--lease-seconds",
            "86400",
        ],
        "RunAtLoad": True,
        "StandardErrorPath": str(cache_root / "broker.stderr.log"),
        "StandardOutPath": str(cache_root / "broker.stdout.log"),
    }
    _atomic_plist(plist, plist_path)

    command_path = local_bin / "bw-lease"
    command = (
        "#!/bin/sh\n"
        f"exec {shlex.quote(str(python))} {shlex.quote(str(installed_client))} "
        f"--socket {shlex.quote(str(socket_path))} \"$@\"\n"
    )
    temporary_command = command_path.with_suffix(".new")
    temporary_command.write_text(command)
    os.chmod(temporary_command, 0o700)
    os.replace(temporary_command, command_path)

    domain = f"gui/{os.getuid()}"
    subprocess.run(
        ["launchctl", "bootout", domain, str(plist_path)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    subprocess.run(["launchctl", "bootstrap", domain, str(plist_path)], check=True)
    subprocess.run(["launchctl", "kickstart", "-k", f"{domain}/{LABEL}"], check=True)
    print(f"installed={plist_path}")
    print(f"client={command_path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    install_parser = subparsers.add_parser("install")
    install_parser.add_argument("--python", type=_absolute_executable, required=True)
    return parser.parse_args()


def _absolute_executable(value: str) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        raise argparse.ArgumentTypeError("--python must be an absolute path")
    if not path.is_file() or not os.access(path, os.X_OK):
        raise argparse.ArgumentTypeError("--python must name an executable file")
    return path


def main() -> None:
    options = parse_args()
    if options.command == "install":
        install(options.python)


if __name__ == "__main__":
    main()
