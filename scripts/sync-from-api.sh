#!/usr/bin/env bash
# sync-from-api.sh — Portable public API sync script for ASE repo
# Fetches live skills from ASE API and regenerates all endpoint artifacts.
# Usage: ASE_API_BASE=https://agentskillexchange.com ./scripts/sync-from-api.sh [repo_dir]
#
# Environment:
#   ASE_API_BASE  — base URL of the ASE site (default: https://agentskillexchange.com)
#
# Outputs (written to repo_dir):
#   skills.json        — full skill catalog for agents
#   openclaw.json      — OpenClaw-formatted endpoint artifact
#   codex.json         — Codex-formatted endpoint artifact
#   llms.txt           — plain-text LLM-readable skill list
#   sync-metadata.json — provenance/validation record

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="${1:-$(dirname "$SCRIPT_DIR")}"
ASE_API_BASE="${ASE_API_BASE:-https://agentskillexchange.com}"

echo "[sync-from-api] Starting sync from ${ASE_API_BASE} → ${REPO_DIR}"

python3 - "$REPO_DIR" "$ASE_API_BASE" << 'PYEOF'
import datetime as dt
import hashlib
import html
import json
import sys
import urllib.request
from pathlib import Path

REPO_DIR = Path(sys.argv[1])
ASE_API_BASE = sys.argv[2].rstrip("/")
BROWSE_API = f"{ASE_API_BASE}/wp-json/ase-marketplace/v1/browse"
SKILLS_JSON_URL = f"{ASE_API_BASE}/skills.json"

def fetch_json(url, method="GET"):
    req = urllib.request.Request(url, headers={"User-Agent": "ASE Repo sync-from-api/1.0"}, method=method)
    with urllib.request.urlopen(req, timeout=60) as resp:
        body = resp.read().decode("utf-8")
        return json.loads(body), dict(resp.headers), body

def display_name(item):
    return html.unescape(item.get("name") or item.get("title") or "")

# ── Fetch live skills ────────────────────────────────────────────────────────
items = []
page = 1
raw_body = ""
while True:
    batch, headers, body = fetch_json(f"{BROWSE_API}?per_page=100&page={page}")
    items.extend(batch)
    raw_body += body
    total_pages = int(headers.get("X-WP-TotalPages", "1"))
    print(f"  Page {page}/{total_pages}: +{len(batch)} items")
    if page >= total_pages:
        break
    page += 1

print(f"  Total items fetched: {len(items)}")

# ── Build canonical skills list ──────────────────────────────────────────────
def normalize_ver(v):
    if v in ("security_reviewed",):
        return "security_reviewed"
    return "listed"

skills = []
for item in items:
    cats = [html.unescape(x) for x in item.get("categories", [])]
    fws  = [html.unescape(x) for x in item.get("frameworks", [])]
    ver  = normalize_ver(item.get("verification", "listed"))

    entry = {
        "slug":         item.get("slug", ""),
        "name":         display_name(item),
        "title":        display_name(item),
        "description":  html.unescape((item.get("excerpt") or "").strip()),
        "category":     cats[0] if len(cats) == 1 else cats,
        "framework":    fws[0]  if len(fws)  == 1 else fws,
        "verification": ver,
    }

    # real signals only — no faking
    signals = {}
    stars = int(item.get("github_stars") or 0)
    if stars:
        signals["github_stars"] = stars
    dl = int(item.get("npm_downloads") or 0)
    if dl:
        signals["npm_weekly_downloads"] = dl
    lic = item.get("tool_license") or ""
    if lic and lic not in ("Unknown", "NOASSERTION", ""):
        signals["license"] = lic
    if signals:
        entry["signals"] = signals

    skills.append(entry)

today = dt.datetime.utcnow().strftime("%Y-%m-%d")

# ── skills.json ──────────────────────────────────────────────────────────────
skills_payload = {
    "version":   "2.0",
    "total":     len(skills),
    "generated": today,
    "skills":    skills,
}
skills_json_text = json.dumps(skills_payload, indent=2, ensure_ascii=False) + "\n"
(REPO_DIR / "skills.json").write_text(skills_json_text, encoding="utf-8")
print(f"  skills.json written — {len(skills)} skills")

# ── openclaw.json ─────────────────────────────────────────────────────────────
openclaw_payload = {
    "schema":     "openclaw-skills/1.0",
    "source":     ASE_API_BASE,
    "generated":  today,
    "total":      len(skills),
    "skills": [
        {
            "slug":         s["slug"],
            "name":         s["name"],
            "title":        s["name"],
            "description":  s["description"],
            "category":     s["category"],
            "framework":    s["framework"],
            "verification": s["verification"],
        }
        for s in skills
    ],
}
(REPO_DIR / "openclaw.json").write_text(
    json.dumps(openclaw_payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
)
print(f"  openclaw.json written — {len(skills)} skills")

# ── codex.json ────────────────────────────────────────────────────────────────
codex_payload = {
    "schema":    "codex-skills/1.0",
    "source":    ASE_API_BASE,
    "generated": today,
    "total":     len(skills),
    "skills": [
        {
            "slug":         s["slug"],
            "name":         s["name"],
            "title":        s["name"],
            "description":  s["description"],
            "category":     s["category"],
            "framework":    s["framework"],
            "verification": s["verification"],
        }
        for s in skills
    ],
}
(REPO_DIR / "codex.json").write_text(
    json.dumps(codex_payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
)
print(f"  codex.json written — {len(skills)} skills")

# ── llms.txt ──────────────────────────────────────────────────────────────────
lines = [
    "# Agent Skill Exchange — Full Skill Catalog",
    f"# Source: {ASE_API_BASE}",
    f"# Generated: {today}",
    f"# Total: {len(skills)} skills",
    "",
]
for s in skills:
    cat  = s["category"] if isinstance(s["category"], str) else ", ".join(s["category"])
    fw   = s["framework"] if isinstance(s["framework"], str) else ", ".join(s["framework"])
    ver  = "Security Reviewed" if s["verification"] == "security_reviewed" else "Published"
    lines.append(f"## {s['name']}")
    lines.append(f"slug: {s['slug']}")
    lines.append(f"category: {cat}")
    lines.append(f"framework: {fw}")
    lines.append(f"verification: {ver}")
    lines.append(f"description: {s['description']}")
    lines.append(f"url: {ASE_API_BASE}/skills/{s['slug']}/")
    lines.append("")

(REPO_DIR / "llms.txt").write_text("\n".join(lines), encoding="utf-8")
print(f"  llms.txt written — {len(skills)} skills")

# ── sync-metadata.json ────────────────────────────────────────────────────────
body_hash = "sha256:" + hashlib.sha256(raw_body.encode()).hexdigest()
meta = {
    "source_api_base":     ASE_API_BASE,
    "source_total":        len(skills),
    "source_etag_or_hash": body_hash,
    "generated":           today,
    "generated_files":     ["skills.json", "openclaw.json", "codex.json", "llms.txt"],
    "generator":           "scripts/sync-from-api.sh",
}
(REPO_DIR / "sync-metadata.json").write_text(
    json.dumps(meta, indent=2) + "\n", encoding="utf-8"
)
print(f"  sync-metadata.json written")
print(f"  hash: {body_hash}")
PYEOF

echo "[sync-from-api] Done."
