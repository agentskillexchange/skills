#!/usr/bin/env bash
# validate-skill.sh — Validate a SKILL.md file against the Agent Skill Exchange spec
# Usage: ./validate-skill.sh <path-to-SKILL.md>
# Exit 0 on pass, 1 on fail with descriptive errors.
#
# Checks:
#   - File exists and is non-empty
#   - YAML frontmatter present (delimited by ---)
#   - Required fields: name, description, category, framework,
#     verification.verified_metadata, verification.security_reviewed,
#     rating, reviews, creator.name
#   - Rating is between 1.0 and 5.0
#   - Has an H1 heading in the body

set -euo pipefail

ERRORS=()

usage() {
  echo "Usage: $0 <path-to-SKILL.md>"
  exit 1
}

error() {
  ERRORS+=("❌ $1")
}

# Check arguments
if [ $# -lt 1 ]; then
  usage
fi

SKILL_FILE="$1"

# Check file exists
if [ ! -f "$SKILL_FILE" ]; then
  echo "❌ FAIL: File not found: ${SKILL_FILE}"
  exit 1
fi

# Check file is non-empty
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
  # Can't continue without frontmatter
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

# Helper: check if a key exists in frontmatter
check_field() {
  local field="$1"
  local label="${2:-$1}"

  # Handle nested fields (e.g., verification.verified_metadata → look for indented key)
  if [[ "$field" == *.* ]]; then
    local parent="${field%%.*}"
    local child="${field#*.}"

    # Check parent exists
    if ! echo "$FRONTMATTER" | grep -qE "^${parent}:"; then
      error "Missing required field: ${label} (parent '${parent}' not found)"
      return
    fi

    # Check child exists (indented under parent)
    if ! echo "$FRONTMATTER" | awk "/^${parent}:/,/^[^ ]/" | grep -qE "^  ${child}:"; then
      error "Missing required field: ${label}"
      return
    fi
  else
    if ! echo "$FRONTMATTER" | grep -qE "^${field}:"; then
      error "Missing required field: ${label}"
    fi
  fi
}

# Check required fields
check_field "name" "name"
check_field "description" "description"
check_field "category" "category"
check_field "framework" "framework"
check_field "verification.verified_metadata" "verification.verified_metadata"
check_field "verification.security_reviewed" "verification.security_reviewed"
check_field "rating" "rating"
check_field "reviews" "reviews"
check_field "creator.name" "creator.name"

# Validate rating range (1.0-5.0)
RATING=$(echo "$FRONTMATTER" | grep -E "^rating:" | head -1 | sed 's/rating:\s*//' | tr -d '[:space:]"'"'"'')
if [ -n "$RATING" ]; then
  # Check if it's a valid number
  if echo "$RATING" | grep -qE '^[0-9]+(\.[0-9]+)?$'; then
    # Compare using awk for float comparison
    VALID=$(awk "BEGIN { print ($RATING >= 1.0 && $RATING <= 5.0) ? 1 : 0 }")
    if [ "$VALID" -eq 0 ]; then
      error "Rating ${RATING} is out of range (must be 1.0-5.0)"
    fi
  else
    error "Rating '${RATING}' is not a valid number"
  fi
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
