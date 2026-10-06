from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_workflow", ROOT / "scripts" / "validate_workflow.py")
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)
BASE = (ROOT / "assets" / "gcp-keyless-observe.yml").read_text()


def test_supplied_observer_workflow_passes() -> None:
    assert VALIDATOR.validate(BASE) == []


def test_action_tag_is_refused() -> None:
    changed = BASE.replace(
        "actions/checkout@11d5960a326750d5838078e36cf38b85af677262",
        "actions/checkout@v4",
    )
    assert any("full commit SHA" in failure for failure in VALIDATOR.validate(changed))


def test_command_input_and_direct_shell_interpolation_are_refused() -> None:
    changed = BASE.replace(
        "      operation:\n",
        "      command:\n        type: string\n      operation:\n",
    ).replace("          set -euo pipefail", "          ${{ inputs.command }}\n          set -euo pipefail")
    failures = VALIDATOR.validate(changed)
    assert any("command-like" in failure for failure in failures)
    assert any("interpolated directly" in failure for failure in failures)


def test_key_configuration_and_extra_write_permission_are_refused() -> None:
    changed = BASE.replace(
        "  id-token: write",
        "  id-token: write\n  packages: write",
    ).replace(
        "          service_account:",
        "          credentials_json: ${{ secrets.GCP_KEY }}\n          service_account:",
    )
    failures = VALIDATOR.validate(changed)
    assert any("credential pattern" in failure for failure in failures)
    assert any("write permissions" in failure for failure in failures)
