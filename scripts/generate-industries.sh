#!/usr/bin/env bash
# generate-industries.sh — Regenerate industry collection markdown from curated ASE manifest

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="${1:-$(dirname "$SCRIPT_DIR")}"

python3 - "$REPO_DIR" << 'PY'
import html
import json
import os
import sys
import urllib.request
from pathlib import Path

REPO_DIR = Path(sys.argv[1])
INDUSTRIES_DIR = REPO_DIR / "industries"
MANIFEST_PATH = REPO_DIR / "scripts" / "industry-collections.json"
SITE_BASE = os.environ.get("ASE_SITE_BASE", os.environ.get("ASE_API_BASE", "https://agentskillexchange.com")).rstrip("/")
BROWSE_BASE = f"{SITE_BASE}/wp-json/ase-marketplace/v1/browse"

EMOJI = {
    "media-publishing-systems": "🎙️",
    "finance-filings": "💼",
    "ecommerce-retail-operations": "🛒",
    "legal-ops-compliance": "⚖️",
    "healthcare-documentation-intake": "🩺",
    "product-analytics-growth-ops": "📈",
    "devrel-api-documentation": "📚",
    "customer-support-success": "🎧",
    "real-estate-workflows": "🏠",
}


def fetch_json(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": "ASE Industry Generator"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8")), dict(resp.headers)


def fmt_num(n):
    n = int(n or 0)
    if n >= 1_000_000:
        return f"{n/1_000_000:.1f}".rstrip("0").rstrip(".") + "M"
    if n >= 1_000:
        return f"{n/1_000:.1f}".rstrip("0").rstrip(".") + "k"
    return str(n) if n else "—"


def downloads_str(n):
    n = int(n or 0)
    return f"{fmt_num(n)}/wk" if n else "—"


def stage_label(raw):
    raw = (raw or "planned").strip().lower()
    mapping = {
        "wave-1": "Wave 1",
        "wave-2": "Wave 2",
        "wave-3": "Wave 3",
        "wave-4": "Wave 4",
        "pilot": "Pilot",
        "planned": "Planned",
    }
    return mapping.get(raw, raw.replace("-", " ").title())


manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
collections = manifest.get("collections", [])
if not collections:
    raise SystemExit("industry-collections.json has no collections")

items = []
page = 1
while True:
    batch, headers = fetch_json(f"{BROWSE_BASE}?per_page=100&page={page}")
    items.extend(batch)
    if page >= int(headers.get("X-WP-TotalPages", "1")):
        break
    page += 1

by_slug = {}
for item in items:
    slug = item.get("slug")
    if not slug:
        continue
    item["title"] = html.unescape(item.get("title", ""))
    item["description"] = html.unescape(item.get("description", ""))
    item["categories"] = [html.unescape(x) for x in item.get("categories", [])]
    item["frameworks"] = [html.unescape(x) for x in item.get("frameworks", [])]
    by_slug[slug] = item

INDUSTRIES_DIR.mkdir(parents=True, exist_ok=True)

index_lines = [
    "# Industry Collections",
    "",
    "> Curated editorial overlays for real workflow clusters. These are intentionally not a replacement for categories.",
    "",
    "| | Collection | Stage | Picks | Summary |",
    "|---|---|---|---:|---|",
]

for collection in collections:
    slug = collection["slug"]
    title = collection["title"]
    description = collection["description"]
    stage = collection.get("launch_stage", "planned")
    stage_text = stage_label(stage)
    skill_slugs = collection.get("skill_slugs", [])
    backup_slugs = collection.get("backup_skill_slugs", [])
    emoji = EMOJI.get(slug, "📦")

    missing_repo = [s for s in skill_slugs + backup_slugs if not (REPO_DIR / "skills" / s / "SKILL.md").exists()]
    if missing_repo:
        raise SystemExit(f"Missing skill files for collection {slug}: {', '.join(missing_repo)}")

    missing_browse = [s for s in skill_slugs + backup_slugs if s not in by_slug]
    if missing_browse:
        raise SystemExit(f"Missing browse records for collection {slug}: {', '.join(missing_browse)}")

    picks = [by_slug[s] for s in skill_slugs]
    backups = [by_slug[s] for s in backup_slugs]

    lines = [
        f"# {emoji} {title}",
        "",
        description,
        "",
        f"- Launch stage: **{stage_text}**",
        f"- Live page: {SITE_BASE}/industry-skills/#{slug}",
        f"- Homepage access: Curated Collections on {SITE_BASE}/",
        "",
        "## Recommended Picks",
        "",
        "| Skill | Category | Stars | Downloads |",
        "|---|---|---:|---:|",
    ]
    for item in picks:
        category = (item.get("categories") or ["Uncategorized"])[0]
        stars = fmt_num(item.get("github_stars") or 0)
        downloads = downloads_str(item.get("npm_downloads") or 0)
        lines.append(f"| [{item['title']}](../skills/{item['slug']}/) | {category} | {stars} | {downloads} |")

    if backups:
        lines += [
            "",
            "## Backup Picks",
            "",
            "| Skill | Why keep it nearby |",
            "|---|---|",
        ]
        for item in backups:
            lines.append(f"| [{item['title']}](../skills/{item['slug']}/) | Useful alternate or overflow pick for this collection. |")

    caution = collection.get("editorial_caution")
    if caution:
        lines += [
            "",
            "## Editorial Caution",
            "",
            caution,
        ]

    lines += [
        "",
        "---",
        "",
        "[← Back to industry collections](README.md)",
        "",
    ]

    (INDUSTRIES_DIR / f"{slug}.md").write_text("\n".join(lines), encoding="utf-8")
    index_lines.append(f"| {emoji} | [**{title}**]({slug}.md) | {stage_text} | {len(skill_slugs)} | {description} |")

index_lines += [
    "",
    "---",
    "",
    "Industry collections are curated manually and generated from `scripts/industry-collections.json`.",
    "",
    f"[Browse all live collections on agentskillexchange.com →]({SITE_BASE}/industry-skills/)",
    "",
]

(INDUSTRIES_DIR / "README.md").write_text("\n".join(index_lines), encoding="utf-8")
print(f"Generated {len(collections)} industry collection pages.")
PY
