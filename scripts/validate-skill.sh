#!/usr/bin/env bash
# validate-skill.sh — compatibility wrapper for the parser-backed ASE validator.
# Usage: ./scripts/validate-skill.sh <path-to-SKILL.md>

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
exec python3 "$SCRIPT_DIR/validate_skills.py" "$@"
