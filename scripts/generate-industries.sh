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
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (compatible; ASE Industry Generator/1.0)",
        "Accept": "application/json,text/plain,*/*",
    })
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

def display_name(item):
    return html.unescape(item.get("name") or item.get("title") or "")

def list_lines(values):
    values = [str(v).strip() for v in (values or []) if str(v).strip()]
    return [f"- {v}" for v in values] if values else ["- Not specified."]

def workflow_lines(stacks):
    lines = []
    for stack in stacks or []:
        if isinstance(stack, dict):
            name = str(stack.get("name") or "Workflow").strip()
            steps = [str(s).strip() for s in (stack.get("steps") or []) if str(s).strip()]
            if steps:
                lines.append(f"- **{name}:** " + " → ".join(steps))
            else:
                lines.append(f"- **{name}**")
        elif str(stack).strip():
            lines.append(f"- {str(stack).strip()}")
    return lines if lines else ["- Not specified."]

def adjacent_lines(collection, by_collection):
    lines = []
    for adjacent_slug in collection.get("adjacent_collections") or []:
        adjacent = by_collection.get(adjacent_slug)
        if adjacent:
            lines.append(f"- [{adjacent['title']}]({adjacent_slug}.md)")
    return lines if lines else ["- None listed."]


manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
collections = manifest.get("collections", [])
if not collections:
    raise SystemExit("industry-collections.json has no collections")
by_collection = {c["slug"]: c for c in collections}

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
    item["name"] = display_name(item)
    item["title"] = item["name"]
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
    "| | Collection | Picks | Summary |",
    "|---|---|---:|---|",
]

for collection in collections:
    slug = collection["slug"]
    title = collection["title"]
    description = collection["description"]
    skill_slugs = collection.get("skill_slugs", [])
    emoji = EMOJI.get(slug, "📦")

    missing_repo = [s for s in skill_slugs if not (REPO_DIR / "skills" / s / "SKILL.md").exists()]
    if missing_repo:
        raise SystemExit(f"Missing skill files for collection {slug}: {', '.join(missing_repo)}")

    missing_browse = [s for s in skill_slugs if s not in by_slug]
    if missing_browse:
        raise SystemExit(f"Missing browse records for collection {slug}: {', '.join(missing_browse)}")

    picks = [by_slug[s] for s in skill_slugs]
    skill_meta = collection.get("skill_meta") or {}

    lines = [
        f"# {emoji} {title}",
        "",
        description,
        "",
        f"- Live page: {SITE_BASE}/industry-skills/#{slug}",
        f"- Homepage access: Curated Collections on {SITE_BASE}/",
        "",
        "## Who this is for",
        "",
        *list_lines(collection.get("who_for")),
        "",
        "## Jobs covered",
        "",
        *list_lines(collection.get("jobs_covered")),
        "",
        "## Workflow Stacks",
        "",
        *workflow_lines(collection.get("workflow_stacks")),
        "",
        "## Recommended Picks",
        "",
        "| Skill | What it does here | Persona | Install | Stars |",
        "|---|---|---|---|---:|",
    ]
    for item in picks:
        meta = skill_meta.get(item["slug"]) or {}
        why_here = str(meta.get("why_here") or "").strip()
        persona = str(meta.get("persona") or "").strip()
        install = str(meta.get("install_complexity") or "").strip()
        if not (why_here and persona and install):
            raise SystemExit(f"Missing skill_meta for {slug}:{item['slug']}")
        stars = fmt_num(item.get("github_stars") or 0)
        lines.append(
            f"| [{item['name']}](../skills/{item['slug']}/) | {why_here} | {persona} | {install} | {stars} |"
        )


    notes = list(collection.get("editorial_notes") or [])
    caution = collection.get("editorial_caution")
    if caution and caution not in notes:
        notes.append(caution)
    lines += [
        "",
        "## Editorial Notes",
        "",
        *list_lines(notes),
        "",
        "## Adjacent Collections",
        "",
        *adjacent_lines(collection, by_collection),
    ]

    lines += [
        "",
        "---",
        "",
        "[← Back to industry collections](README.md)",
        "",
    ]

    (INDUSTRIES_DIR / f"{slug}.md").write_text("\n".join(lines), encoding="utf-8")
    index_lines.append(f"| {emoji} | [**{title}**]({slug}.md) | {len(skill_slugs)} | {description} |")

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
