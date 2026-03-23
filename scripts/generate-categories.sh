#!/usr/bin/env bash
# generate-categories.sh — Regenerate per-category README.md files from the WP REST API
# Usage: ./generate-categories.sh [output_dir]
#   output_dir: directory containing the git repo (default: parent of scripts/)
#
# Requires: curl, jq

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="${1:-$(dirname "$SCRIPT_DIR")}"
API_BASE="https://agentskillexchange.com/wp-json/wp/v2"
PER_PAGE=100
CATEGORIES_DIR="${REPO_DIR}/categories"

echo "==> Fetching categories..." >&2

# Fetch all categories
CATEGORIES=$(curl -sS "${API_BASE}/skill_category?per_page=${PER_PAGE}&orderby=count&order=desc")

# Build category arrays
declare -A CAT_NAME CAT_SLUG CAT_COUNT CAT_ID_BY_SLUG
CAT_IDS=()
while IFS=$'\t' read -r id name slug count; do
  name=$(echo "$name" | sed 's/&amp;/\&/g; s/&#039;/'"'"'/g; s/&lt;/</g; s/&gt;/>/g; s/&quot;/"/g')
  CAT_NAME[$id]="$name"
  CAT_SLUG[$id]="$slug"
  CAT_COUNT[$id]="$count"
  CAT_ID_BY_SLUG[$slug]="$id"
  CAT_IDS+=("$id")
done < <(echo "$CATEGORIES" | jq -r '.[] | [.id, .name, .slug, .count] | @tsv')

echo "==> Found ${#CAT_IDS[@]} categories" >&2

# Emoji map
declare -A CAT_EMOJI CAT_DESC
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

CAT_DESC["CI/CD Integrations"]="Pipeline configs, deployment automation, build tooling, and continuous integration/delivery skills."
CAT_DESC["Runbooks & Diagnostics"]="Incident response, troubleshooting guides, system diagnostics, and operational runbooks."
CAT_DESC["Code Quality & Review"]="Linting rules, review checklists, code standards enforcement, and quality gates."
CAT_DESC["Developer Tools"]="CLI helpers, dev environment setup, productivity utilities, and developer workflows."
CAT_DESC["Library & API Reference"]="SDK documentation, API guides, framework reference material, and library usage patterns."
CAT_DESC["Monitoring & Alerts"]="Metrics collection, alerting rules, observability setup, and system monitoring."
CAT_DESC["Data Extraction & Transformation"]="Parsing, ETL pipelines, format conversion, data wrangling, and transformation utilities."
CAT_DESC["Security & Verification"]="Auth setup, vulnerability scanning, compliance checks, and security automation."
CAT_DESC["Templates & Workflows"]="Project scaffolding, boilerplate generators, workflow templates, and starter kits."
CAT_DESC["Calendar, Email & Productivity"]="Email automation, calendar management, task coordination, and productivity tools."
CAT_DESC["Integrations & Connectors"]="Third-party API bridges, webhook handlers, service connectors, and platform integrations."
CAT_DESC["Browser Automation"]="Web scraping, UI testing, headless browser control, and browser-based automation."
CAT_DESC["Image & Creative Automation"]="Image generation, asset processing, design automation, and creative tooling."
CAT_DESC["Research & Scraping"]="Web research, data collection, content aggregation, and information gathering."
CAT_DESC["Content Writing & SEO"]="Blog posts, SEO optimization, content strategy, and writing assistance."
CAT_DESC["Media & Transcription"]="Audio/video processing, speech-to-text, media conversion, and transcription."
CAT_DESC["WordPress & CMS"]="Theme/plugin development, WP-CLI automation, CMS management, and WordPress skills."

# Fetch all skills (paginated)
ALL_SKILLS="[]"
page=1
while true; do
  echo "==> Fetching skills page ${page}..." >&2
  RESPONSE=$(curl -sS -w '\n%{http_code}' "${API_BASE}/skill?per_page=${PER_PAGE}&page=${page}&_fields=id,title,slug,skill_category,meta&orderby=title&order=asc")
  HTTP_CODE=$(echo "$RESPONSE" | tail -1)
  BODY=$(echo "$RESPONSE" | sed '$d')

  if [ "$HTTP_CODE" != "200" ]; then
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

# Generate categories/ root README
mkdir -p "$CATEGORIES_DIR"
cat > "${CATEGORIES_DIR}/README.md" << EOF
# Skill Categories

Browse skills by category. Each category contains a curated list of verified skills.

> **${TOTAL_SKILLS} skills** across **${#CAT_IDS[@]} categories**

| | Category | Skills | Description |
|---|---|:---:|---|
EOF

# Sort categories by count
SORTED_CAT_IDS=$(for id in "${CAT_IDS[@]}"; do echo "${CAT_COUNT[$id]} $id"; done | sort -rn | awk '{print $2}')

for cat_id in $SORTED_CAT_IDS; do
  cat_name="${CAT_NAME[$cat_id]}"
  cat_slug="${CAT_SLUG[$cat_id]}"
  cat_count="${CAT_COUNT[$cat_id]}"
  emoji="${CAT_EMOJI[$cat_name]:-📦}"
  desc="${CAT_DESC[$cat_name]:-Skills in this category.}"

  # Truncate desc for table
  short_desc=$(echo "$desc" | cut -c1-60)
  if [ ${#desc} -gt 60 ]; then
    short_desc="${short_desc}..."
  fi

  echo "| ${emoji} | [**${cat_name}**](${cat_slug}/) | **${cat_count}** | ${short_desc} |" >> "${CATEGORIES_DIR}/README.md"
done

cat >> "${CATEGORIES_DIR}/README.md" << 'EOF'

---

<div align="center">

**[Browse all skills on agentskillexchange.com →](https://agentskillexchange.com/browse-skills/)**

</div>
EOF

echo "==> Generated categories/README.md" >&2

# Generate per-category README files
for cat_id in $SORTED_CAT_IDS; do
  cat_name="${CAT_NAME[$cat_id]}"
  cat_slug="${CAT_SLUG[$cat_id]}"
  cat_count="${CAT_COUNT[$cat_id]}"
  emoji="${CAT_EMOJI[$cat_name]:-📦}"
  desc="${CAT_DESC[$cat_name]:-Skills in this category.}"

  cat_dir="${CATEGORIES_DIR}/${cat_slug}"
  mkdir -p "$cat_dir"

  echo "==> Generating ${cat_slug}/README.md (${cat_count} skills)..." >&2

  # Find related categories (categories with similar skills, or adjacent by count)
  # Simple: pick 3 categories that are closest in count
  RELATED_CATS=""
  for other_id in $SORTED_CAT_IDS; do
    if [ "$other_id" != "$cat_id" ]; then
      other_name="${CAT_NAME[$other_id]}"
      other_slug="${CAT_SLUG[$other_id]}"
      other_emoji="${CAT_EMOJI[$other_name]:-📦}"
      other_count="${CAT_COUNT[$other_id]}"
      if [ -z "$RELATED_CATS" ]; then
        RELATED_CATS="- ${other_emoji} [${other_name}](../${other_slug}/) (${other_count} skills)"
      else
        RELATED_CATS="${RELATED_CATS}
- ${other_emoji} [${other_name}](../${other_slug}/) (${other_count} skills)"
      fi
    fi
  done
  # Take first 4 related categories
  RELATED_CATS=$(echo "$RELATED_CATS" | head -4)

  cat > "${cat_dir}/README.md" << EOF
# ${emoji} ${cat_name}

> **${cat_count} skills** · [Browse on agentskillexchange.com →](https://agentskillexchange.com/browse-skills/?category=${cat_slug})

${desc}

---

## Skills

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
      (.meta.skill_reviews // "0")
    ] | @tsv
  ' | while IFS=$'\t' read -r title slug rating reviews; do
    title=$(echo "$title" | sed 's/&amp;/\&/g; s/&#039;/'"'"'/g; s/&lt;/</g; s/&gt;/>/g; s/&quot;/"/g')
    rating_display="$rating"
    if [ "$rating" != "N/A" ]; then
      rating_display="⭐ ${rating}"
    fi
    echo "| [${title}](../../skills/${slug}/) | ${rating_display} | ${reviews} | \`clawhub install ${slug}\` |" >> "${cat_dir}/README.md"
  done

  cat >> "${cat_dir}/README.md" << EOF

---

## Quick Install

\`\`\`bash
# Install any skill from this category
clawhub install <slug>

# Or using npx
npx skills add agentskillexchange/skills --skill <slug>

# For a specific agent
npx skills add agentskillexchange/skills --skill <slug> -a claude-code
npx skills add agentskillexchange/skills --skill <slug> -a cursor
npx skills add agentskillexchange/skills --skill <slug> -a codex
\`\`\`

---

## Related Categories

${RELATED_CATS}

---

[← Back to all categories](../)

EOF

done

echo "==> Done! Generated READMEs for ${#CAT_IDS[@]} categories" >&2
