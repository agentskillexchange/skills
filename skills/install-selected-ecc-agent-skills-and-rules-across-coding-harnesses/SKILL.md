---
name: "Install selected ECC agent skills and rules across coding harnesses"
slug: "install-selected-ecc-agent-skills-and-rules-across-coding-harnesses"
description: "Use Everything Claude Code to install curated skills, rules, hooks, and MCP configuration into Claude Code, Codex, Cursor, OpenCode, and related coding-agent harnesses without copying the whole repo blindly."
github_stars: 186751
verification: "listed"
source: "https://github.com/affaan-m/ECC"
author: "affaan-m"
publisher_type: "individual"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "affaan-m/ECC"
  github_stars: 186751
  npm_package: "ecc-universal"
  npm_weekly_downloads: 0
---

# Install selected ECC agent skills and rules across coding harnesses

Use Everything Claude Code to install curated skills, rules, hooks, and MCP configuration into Claude Code, Codex, Cursor, OpenCode, and related coding-agent harnesses without copying the whole repo blindly.

## Prerequisites

Claude Code, Codex, Cursor, OpenCode, or another supported harness; Node.js/npm for installer paths; optional MCP servers

## Installation

Use the upstream install or setup path that matches your environment:
- npx ecc-install --profile minimal --target claude
- npx ecc consult "security reviews" --target claude
- npx ecc consult "mlops training model deployment" --target claude
- npx ecc install --profile minimal --target claude --with capability:machine-learning

Requirements and caveats from upstream:
- ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)
- If your local Claude setup was wiped or reset, that does not mean you need to repurchase ECC. Start with node scripts/ecc.js list-installed, then run node scripts/ecc.js doctor and node scripts/ecc.js repair before re...

Basic usage or getting-started notes:
- Get up and running in under 2 minutes:
- ### Pick one path only
- Most Claude Code users should use exactly one install path:

- Source: https://github.com/affaan-m/ECC
- Extracted from upstream docs: https://raw.githubusercontent.com/affaan-m/ECC/HEAD/README.md

## Documentation

- https://ecc.tools

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/install-selected-ecc-agent-skills-and-rules-across-coding-harnesses/)
