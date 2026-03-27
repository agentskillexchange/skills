#!/usr/bin/env bash
# generate-all.sh — Regenerate ALL auto-generated repo files from live ASE data
# Usage: ./generate-all.sh [repo_dir]
#
# Regenerates: README.md, CATALOG.md, categories/, TOP-STARS.md, TOP-DOWNLOADS.md,
#              skills.json, .claude-plugin, .codex, .cursor-plugin, .opencode

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="${1:-$(dirname "$SCRIPT_DIR")}"

echo "=== Generating README.md ==="
bash "$SCRIPT_DIR/generate-readme.sh" "$REPO_DIR"

echo "=== Generating CATALOG.md ==="
bash "$SCRIPT_DIR/generate-catalog.sh" "$REPO_DIR"

echo "=== Generating categories/ ==="
bash "$SCRIPT_DIR/generate-categories.sh" "$REPO_DIR"

echo "=== Generating TOP-STARS.md and TOP-DOWNLOADS.md ==="
bash "$SCRIPT_DIR/generate-top-lists.sh" "$REPO_DIR"

echo "=== Generating skills.json ==="
bash "$SCRIPT_DIR/generate-skills-json.sh" "$REPO_DIR"

echo "=== Updating agent integration files ==="
bash "$SCRIPT_DIR/generate-agent-files.sh" "$REPO_DIR"

echo "=== All files regenerated ==="
