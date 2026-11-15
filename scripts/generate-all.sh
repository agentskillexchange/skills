#!/usr/bin/env bash
# generate-all.sh — Regenerate ALL auto-generated repo files from live ASE data
# Usage: ASE_API_BASE=https://agentskillexchange.com ./generate-all.sh [repo_dir]
#
# Regenerates: README.md, CATALOG.md, categories/, TOP-STARS.md, TOP-DOWNLOADS.md,
#              skills.json, sync-metadata.json, .claude-plugin, .codex, .cursor-plugin, .opencode

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="${1:-$(dirname "$SCRIPT_DIR")}"

echo "=== Generating README.md ==="
bash "$SCRIPT_DIR/generate-readme.sh" "$REPO_DIR"

echo "=== Generating CATALOG.md ==="
bash "$SCRIPT_DIR/generate-catalog.sh" "$REPO_DIR"

echo "=== Generating categories/ ==="
bash "$SCRIPT_DIR/generate-categories.sh" "$REPO_DIR"

echo "=== Generating industries/ ==="
bash "$SCRIPT_DIR/generate-industries.sh" "$REPO_DIR"

echo "=== Generating TOP-STARS.md and TOP-DOWNLOADS.md ==="
bash "$SCRIPT_DIR/generate-top-lists.sh" "$REPO_DIR"

echo "=== Generating skills.json ==="
bash "$SCRIPT_DIR/generate-skills-json.sh" "$REPO_DIR"

echo "=== Cleaning generated skill install boilerplate ==="
python3 "$SCRIPT_DIR/ase_replace_install_boilerplate.py"

echo "=== Applying cleaned frontmatter verification overlay ==="
python3 "$SCRIPT_DIR/apply-frontmatter-verification-overlay.py" "$REPO_DIR"
python3 "$SCRIPT_DIR/apply-frontmatter-verification-overlay.py" "$REPO_DIR" --check

echo "=== Checking skill body quality ==="
python3 "$SCRIPT_DIR/ase_body_quality_gate.py" --all

echo "=== Validating cleaned skill frontmatter ==="
python3 "$SCRIPT_DIR/validate_skills.py" --all --quiet

echo "=== Updating agent integration files ==="
bash "$SCRIPT_DIR/generate-agent-files.sh" "$REPO_DIR"

echo "=== Generating public agent endpoints ==="
python3 "$SCRIPT_DIR/generate-agent-endpoints.py" "$REPO_DIR"

echo "=== Re-applying cleaned frontmatter verification overlay ==="
python3 "$SCRIPT_DIR/apply-frontmatter-verification-overlay.py" "$REPO_DIR"
python3 "$SCRIPT_DIR/apply-frontmatter-verification-overlay.py" "$REPO_DIR" --check

echo "=== Re-checking skill body quality ==="
python3 "$SCRIPT_DIR/ase_body_quality_gate.py" --all

echo "=== Checking install command safety ==="
python3 "$SCRIPT_DIR/check-install-commands.py" "$REPO_DIR"

echo "=== Writing sync metadata ==="
python3 "$SCRIPT_DIR/write-sync-metadata.py" "$REPO_DIR"

echo "=== All files regenerated ==="
