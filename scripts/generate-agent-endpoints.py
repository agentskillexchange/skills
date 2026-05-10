#!/usr/bin/env python3
"""Generate public agent-readable endpoint files from canonical skills.json."""

from __future__ import annotations

import datetime as dt
import json
import os
import sys
from pathlib import Path
from typing import Any

REPO_DIR = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
SITE_BASE = os.environ.get("ASE_SITE_BASE", os.environ.get("ASE_API_BASE", "https://agentskillexchange.com")).rstrip("/")
REPO_URL = os.environ.get("ASE_REPO_URL", "https://github.com/agentskillexchange/skills")
SCHEMA_VERSION = os.environ.get("ASE_SCHEMA_VERSION", "2.0")
GENERATOR_VERSION = "2026-05-10.agent-endpoints-v1"


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


skills_index = load_json(REPO_DIR / "skills.json")
skills = skills_index.get("skills", [])
generated_at = now_iso()
security_reviewed = sum(1 for item in skills if item.get("verification") == "security_reviewed")
categories = sorted({cat for item in skills for cat in item.get("category", [])})

common_endpoints = {
    "skills_json": f"{SITE_BASE}/skills.json",
    "openclaw_manifest": f"{SITE_BASE}/openclaw.json",
    "codex_manifest": f"{SITE_BASE}/codex.json",
    "llms_txt": f"{SITE_BASE}/llms.txt",
    "browse_api": f"{SITE_BASE}/wp-json/ase-marketplace/v1/browse",
    "homepage_picks": f"{SITE_BASE}/wp-json/ase-marketplace/v1/homepage-picks",
}

openclaw = {
    "name": "Agent Skill Exchange",
    "description": "Canonical public catalog of reusable AI agent skills backed by real tools, repos, packages, or documented APIs.",
    "schema_version": SCHEMA_VERSION,
    "generated_at": generated_at,
    "generator_version": GENERATOR_VERSION,
    "site": SITE_BASE,
    "repository": REPO_URL,
    "catalog": {
        "total": len(skills),
        "security_reviewed": security_reviewed,
        "categories": len(categories),
        "skills_url": common_endpoints["skills_json"],
    },
    "trust_tiers": {
        "listed": "Published",
        "security_reviewed": "Security Reviewed",
    },
    "install": {
        "openclaw": "clawhub install <slug>",
        "npx": "npx skills add agentskillexchange/skills --skill <slug>",
    },
    "endpoints": common_endpoints,
}

codex = {
    "name": "Agent Skill Exchange Codex Manifest",
    "description": "Machine-readable index for coding agents that need reusable skill instructions from agentskillexchange/skills.",
    "schema_version": SCHEMA_VERSION,
    "generated_at": generated_at,
    "generator_version": GENERATOR_VERSION,
    "repository": REPO_URL,
    "skill_directory": "skills/<slug>/SKILL.md",
    "canonical_frontmatter": {
        "required": ["title", "slug", "description", "category", "framework", "verification"],
        "verification_values": ["listed", "security_reviewed"],
        "optional": ["source", "tool_ecosystem"],
    },
    "catalog": {
        "total": len(skills),
        "security_reviewed": security_reviewed,
        "categories": categories,
        "skills_url": common_endpoints["skills_json"],
    },
    "usage": {
        "search": "Read skills.json, choose a slug, then inspect skills/<slug>/SKILL.md in the GitHub repo.",
        "install": "npx skills add agentskillexchange/skills --skill <slug> -a codex",
    },
    "endpoints": common_endpoints,
}

llms_lines = [
    "# Agent Skill Exchange",
    "",
    "Agent Skill Exchange is a public catalog of reusable AI agent skills. Each skill wraps a real upstream tool, repository, package, API, or workflow into instructions agents can install and use.",
    "",
    "## Canonical machine-readable files",
    "",
    f"- Full catalog JSON: {SITE_BASE}/skills.json",
    f"- OpenClaw manifest: {SITE_BASE}/openclaw.json",
    f"- Codex manifest: {SITE_BASE}/codex.json",
    f"- GitHub repository: {REPO_URL}",
    f"- Live browse API: {SITE_BASE}/wp-json/ase-marketplace/v1/browse",
    "",
    "## Catalog summary",
    "",
    f"- Published skills: {len(skills):,}",
    f"- Security Reviewed skills: {security_reviewed:,}",
    f"- Categories: {len(categories):,}",
    "- Public trust tiers: Published, Security Reviewed",
    "- Canonical verification values: listed, security_reviewed",
    "",
    "## Installation",
    "",
    "```bash",
    "# Any agent using the npx skill installer",
    "npx skills add agentskillexchange/skills --skill <slug>",
    "",
    "# OpenClaw",
    "clawhub install <slug>",
    "```",
    "",
    "## Human entry points",
    "",
    f"- Browse skills: {SITE_BASE}/browse-skills/",
    f"- Categories: {REPO_URL}/tree/main/categories",
    f"- Industry collections: {REPO_URL}/tree/main/industries",
    f"- Verification model: {SITE_BASE}/how-we-verify-skills/",
    "",
    "## Notes for agents",
    "",
    "Use skills.json as the canonical catalog index. Use the GitHub repo path skills/<slug>/SKILL.md for the actual skill instructions. Do not treat internal WordPress fields such as verification_status or verified_metadata as public schema.",
    "",
    f"Generated: {generated_at}",
]

for filename, data in [("openclaw.json", openclaw), ("codex.json", codex)]:
    (REPO_DIR / filename).write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
(REPO_DIR / "llms.txt").write_text("\n".join(llms_lines) + "\n", encoding="utf-8")
print(f"Generated agent endpoints — skills={len(skills)}, security_reviewed={security_reviewed}.")
