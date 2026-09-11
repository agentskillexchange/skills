#!/usr/bin/env python3
"""Diagnose keyless GCP routes without emitting credential material."""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import urllib.error
import urllib.request


def _run(argv: list[str], timeout: float = 8.0) -> subprocess.CompletedProcess[str] | None:
    try:
        return subprocess.run(
            argv,
            check=False,
            capture_output=True,
            text=True,
            timeout=timeout,
            env={**os.environ, "CLOUDSDK_CORE_DISABLE_PROMPTS": "1"},
        )
    except (OSError, subprocess.SubprocessError):
        return None


def metadata_identity() -> str | None:
    request = urllib.request.Request(
        "http://metadata.google.internal/computeMetadata/v1/instance/"
        "service-accounts/default/email",
        headers={"Metadata-Flavor": "Google"},
    )
    try:
        with urllib.request.urlopen(request, timeout=0.4) as response:
            if response.headers.get("Metadata-Flavor") != "Google":
                return None
            email = response.read(512).decode("utf-8", "replace").strip()
            return email if "@" in email else None
    except (OSError, urllib.error.URLError, TimeoutError):
        return None


def github_dispatch_ready(repo: str, workflow: str) -> bool:
    if not shutil.which("gh") or not repo or not workflow:
        return False
    auth = _run(["gh", "auth", "status", "--hostname", "github.com"])
    if auth is None or auth.returncode != 0:
        return False
    view = _run(["gh", "workflow", "view", workflow, "--repo", repo, "--yaml"])
    return view is not None and view.returncode == 0


def gcloud_state() -> tuple[str | None, bool]:
    if not shutil.which("gcloud"):
        return None, False
    account = _run([
        "gcloud", "auth", "list", "--filter=status:ACTIVE",
        "--format=value(account)", "--limit=1",
    ])
    active = (account.stdout.strip().splitlines()[0]
              if account and account.returncode == 0 and account.stdout.strip() else None)
    # The token is captured in memory only and never returned or printed.
    probe = _run(["gcloud", "auth", "print-access-token", "--quiet"])
    valid = bool(probe and probe.returncode == 0 and probe.stdout.strip())
    return active, valid


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default="", help="GitHub OWNER/REPO")
    parser.add_argument("--workflow", default="gcp-keyless-observe.yml")
    args = parser.parse_args()

    metadata_email = metadata_identity()
    github_ready = github_dispatch_ready(args.repo, args.workflow)
    account, gcloud_valid = gcloud_state()

    if metadata_email:
        route, status = "managed-metadata", "ready"
    elif github_ready:
        route, status = "github-dispatch", "ready"
    elif gcloud_valid:
        route, status = "human-oauth-fallback", "degraded"
    else:
        route, status = "bootstrap-required", "blocked"

    print(json.dumps({
        "schema": "gcp-keyless-doctor-v1",
        "status": status,
        "recommended_route": route,
        "managed_metadata": {
            "available": metadata_email is not None,
            "service_account_email": metadata_email,
        },
        "github_dispatch": {
            "available": github_ready,
            "repo": args.repo or None,
            "workflow": args.workflow,
        },
        "human_gcloud": {
            "installed": shutil.which("gcloud") is not None,
            "active_account": account,
            "credential_valid": gcloud_valid,
            "steady_state_authority": False,
        },
        "service_account_keys_allowed": False,
    }, sort_keys=True, indent=2))
    return 0 if status == "ready" else 3 if status == "degraded" else 4


if __name__ == "__main__":
    raise SystemExit(main())
