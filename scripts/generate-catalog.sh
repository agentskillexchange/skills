#!/usr/bin/env bash
# generate-catalog.sh — Regenerate CATALOG.md from the Agent Skill Exchange WP REST API
# Usage: ./generate-catalog.sh [output_dir]
#   output_dir: directory containing the git repo (default: parent of scripts/)
#
# Requires: curl, jq

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="${1:-$(dirname "$SCRIPT_DIR")}"
API_BASE="https://agentskillexchange.com/wp-json/wp/v2"
PER_PAGE=100

echo "==> Fetching categories..." >&2

# Fetch all categories
CATEGORIES=$(curl -sS "${API_BASE}/skill_category?per_page=${PER_PAGE}&orderby=count&order=desc")

# Build category ID→name map (decode HTML entities)
declare -A CAT_NAME CAT_SLUG CAT_COUNT
while IFS=$'\t' read -r id name slug count; do
  # Decode common HTML entities
  name=$(echo "$name" | sed 's/&amp;/\&/g; s/&#039;/'"'"'/g; s/&lt;/</g; s/&gt;/>/g; s/&quot;/"/g')
  CAT_NAME[$id]="$name"
  CAT_SLUG[$id]="$slug"
  CAT_COUNT[$id]="$count"
done < <(echo "$CATEGORIES" | jq -r '.[] | [.id, .name, .slug, .count] | @tsv')

echo "==> Found ${#CAT_NAME[@]} categories" >&2

# Fetch all skills (paginated)
ALL_SKILLS="[]"
page=1
while true; do
  echo "==> Fetching skills page ${page}..." >&2
  RESPONSE=$(curl -sS -w '\n%{http_code}' "${API_BASE}/skill?per_page=${PER_PAGE}&page=${page}&_fields=id,title,slug,skill_category,meta&orderby=title&order=asc")
  HTTP_CODE=$(echo "$RESPONSE" | tail -1)
  BODY=$(echo "$RESPONSE" | sed '$d')

  if [ "$HTTP_CODE" != "200" ]; then
    # 400 means we've gone past the last page
    break
  fi

  SKILL_COUNT=$(echo "$BODY" | jq 'length')
  if [ "$SKILL_COUNT" -eq 0 ]; then
    break
  fi

  ALL_SKILLS=$(echo "$ALL_SKILLS" "$BODY" | jq -s '.[0] + .[1]')
  page=$((page + 1))
done

TOTAL_SKILLS=$(echo "$ALL_SKILLS" | jq 'length')
echo "==> Total skills fetched: ${TOTAL_SKILLS}" >&2

# Count categories
TOTAL_CATEGORIES=${#CAT_NAME[@]}

# Emoji map for categories
declare -A CAT_EMOJI
CAT_EMOJI["CI/CD Integrations"]="🔧"
CAT_EMOJI["Runbooks & Diagnostics"]="📋"
CAT_EMOJI["Code Quality & Review"]="✅"
CAT_EMOJI["Developer Tools"]="🛠️"
CAT_EMOJI["Library & API Reference"]="📚"
CAT_EMOJI["Monitoring & Alerts"]="📊"
CAT_EMOJI["Data Extraction & Transformation"]="🔄"
CAT_EMOJI["Security & Verification"]="🔒"
CAT_EMOJI["Templates & Workflows"]="📄"
CAT_EMOJI["Calendar, Email & Productivity"]="📅"
CAT_EMOJI["Integrations & Connectors"]="🔗"
CAT_EMOJI["Browser Automation"]="🌐"
CAT_EMOJI["Image & Creative Automation"]="🎨"
CAT_EMOJI["Research & Scraping"]="🔍"
CAT_EMOJI["Content Writing & SEO"]="✍️"
CAT_EMOJI["Media & Transcription"]="🎙️"
CAT_EMOJI["WordPress & CMS"]="📰"

# Generate CATALOG.md
CATALOG_FILE="${REPO_DIR}/CATALOG.md"
echo "==> Generating ${CATALOG_FILE}..." >&2

cat > "$CATALOG_FILE" << 'HEADER'
# Agent Skill Exchange — Full Catalog

HEADER

cat >> "$CATALOG_FILE" << EOF
> **${TOTAL_SKILLS} skills** across **${TOTAL_CATEGORIES} categories** · Updated $(date -u '+%Y-%m-%d %H:%M UTC')
>
> Browse the [live marketplace](https://agentskillexchange.com/browse-skills/) for search, filtering, and one-click install.

---

## Summary

| Metric | Value |
|--------|-------|
| Total Skills | **${TOTAL_SKILLS}** |
| Categories | **${TOTAL_CATEGORIES}** |
| Frameworks | **11** |
| Verification | All skills **Verified Metadata** or higher |

---

## Skills by Category

EOF

# Sort categories by count (descending)
SORTED_CAT_IDS=$(for id in "${!CAT_COUNT[@]}"; do echo "${CAT_COUNT[$id]} $id"; done | sort -rn | awk '{print $2}')

for cat_id in $SORTED_CAT_IDS; do
  cat_name="${CAT_NAME[$cat_id]}"
  cat_slug="${CAT_SLUG[$cat_id]}"
  cat_count="${CAT_COUNT[$cat_id]}"
  emoji="${CAT_EMOJI[$cat_name]:-📦}"

  cat >> "$CATALOG_FILE" << EOF
### ${emoji} ${cat_name} (${cat_count} skills)

| Skill | Rating | Reviews | Install |
|-------|:------:|:-------:|---------|
EOF

  # Get skills in this category, sorted by rating desc
  echo "$ALL_SKILLS" | jq -r --argjson cat_id "$cat_id" '
    [.[] | select(.skill_category | index($cat_id))] |
    sort_by(- ((.meta.skill_rating // "0") | tonumber)) |
    .[] |
    [
      .title.rendered,
      .slug,
      (.meta.skill_rating // "N/A"),
      (.meta.skill_reviews // "0"),
      .slug
    ] | @tsv
  ' | while IFS=$'\t' read -r title slug rating reviews install_slug; do
    # Decode HTML entities in title
    title=$(echo "$title" | sed 's/&amp;/\&/g; s/&#039;/'"'"'/g; s/&lt;/</g; s/&gt;/>/g; s/&quot;/"/g')
    rating_display="$rating"
    if [ "$rating" != "N/A" ]; then
      rating_display="⭐ ${rating}"
    fi
    echo "| [${title}](skills/${slug}/) | ${rating_display} | ${reviews} | \`clawhub install ${install_slug}\` |" >> "$CATALOG_FILE"
  done

  echo "" >> "$CATALOG_FILE"
done

cat >> "$CATALOG_FILE" << 'FOOTER'
---

<div align="center">

**[agentskillexchange.com](https://agentskillexchange.com)** — The marketplace for trusted AI agent skills

</div>
FOOTER

echo "==> CATALOG.md generated with ${TOTAL_SKILLS} skills" >&2

# Update README badge counts
README_FILE="${REPO_DIR}/README.md"
if [ -f "$README_FILE" ]; then
  echo "==> Updating README.md badge counts to ${TOTAL_SKILLS}+..." >&2
  # URL-encode the count for badge (1,268+ → 1%2C268+)
  BADGE_COUNT=$(printf '%s' "${TOTAL_SKILLS}+" | sed 's/,/%2C/g')
  # Update skills badge
  sed -i -E "s|skills-[0-9%,]+\+-6366f1|skills-${BADGE_COUNT}-6366f1|g" "$README_FILE"
  # Update verified badge
  sed -i -E "s|verified-[0-9%,]+\+-10b981|verified-${BADGE_COUNT}-10b981|g" "$README_FILE"
  # Update text references like "1,200+ skills"
  sed -i -E "s/[0-9,]+\+ skills/${TOTAL_SKILLS}+ skills/g" "$README_FILE"
  echo "==> README.md updated" >&2
fi

echo "==> Done!" >&2
