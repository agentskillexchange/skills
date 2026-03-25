#!/usr/bin/env bash
# validate-skill.sh — Validate a SKILL.md file against the Agent Skill Exchange spec
# Usage: ./scripts/validate-skill.sh <path-to-SKILL.md>
# Exit 0 on pass, 1 on fail with descriptive errors.

set -euo pipefail

ERRORS=()

usage() {
  echo "Usage: $0 <path-to-SKILL.md>"
  exit 1
}

error() {
  ERRORS+=("❌ $1")
}

if [ $# -lt 1 ]; then
  usage
fi

SKILL_FILE="$1"

if [ ! -f "$SKILL_FILE" ]; then
  echo "❌ FAIL: File not found: ${SKILL_FILE}"
  exit 1
fi

if [ ! -s "$SKILL_FILE" ]; then
  echo "❌ FAIL: File is empty: ${SKILL_FILE}"
  exit 1
fi

# Check for YAML frontmatter delimiters
FIRST_LINE=$(head -1 "$SKILL_FILE")
if [ "$FIRST_LINE" != "---" ]; then
  error "Missing YAML frontmatter (file must start with ---)"
fi

# Extract frontmatter (between first and second ---)
FRONTMATTER=$(awk '/^---$/{n++;next} n==1{print} n>=2{exit}' "$SKILL_FILE")

if [ -z "$FRONTMATTER" ]; then
  error "Empty or missing YAML frontmatter"
  echo ""
  echo "Validation result for: ${SKILL_FILE}"
  echo "========================"
  for err in "${ERRORS[@]}"; do
    echo "$err"
  done
  echo ""
  echo "FAIL (${#ERRORS[@]} error(s))"
  exit 1
fi

# Check required fields
for field in name description category framework verification; do
  if ! echo "$FRONTMATTER" | grep -qE "^${field}:"; then
    error "Missing required field: ${field}"
  fi
done

# Validate verification value
VERIFICATION=$(echo "$FRONTMATTER" | grep -E "^verification:" | head -1 | sed 's/verification:\s*//' | tr -d '[:space:]"'"'"'')
if [ -n "$VERIFICATION" ]; then
  case "$VERIFICATION" in
    listed|security_reviewed) ;;
    *) error "Invalid verification value: '${VERIFICATION}' (must be 'listed' or 'security_reviewed')" ;;
  esac
fi

# Check for H1 heading in body (after frontmatter)
BODY=$(awk '/^---$/{n++; next} n>=2{print}' "$SKILL_FILE")
if [ -z "$BODY" ]; then
  error "No content body found after frontmatter"
elif ! echo "$BODY" | grep -qE '^# '; then
  error "Missing H1 heading (# ) in body content"
fi

# Report results
echo ""
echo "Validation result for: ${SKILL_FILE}"
echo "========================"

if [ ${#ERRORS[@]} -eq 0 ]; then
  echo "✅ PASS — All checks passed"
  exit 0
else
  for err in "${ERRORS[@]}"; do
    echo "$err"
  done
  echo ""
  echo "FAIL (${#ERRORS[@]} error(s))"
  exit 1
fi
