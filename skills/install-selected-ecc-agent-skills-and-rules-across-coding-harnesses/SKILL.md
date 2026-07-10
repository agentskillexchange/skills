---
title: "Install selected ECC agent skills and rules across coding harnesses"
description: "Use Everything Claude Code to install curated skills, rules, hooks, and MCP configuration into Claude Code, Codex, Cursor, OpenCode, and related coding-agent harnesses without copying the whole repo blindly."
verification: "listed"
source: "https://github.com/affaan-m/ECC"
author: "affaan-m"
publisher_type: "individual"
category:
  - "Templates & Workflows"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "affaan-m/ECC"
  github_stars: 186751
  npm_package: "ecc-universal"
  npm_weekly_downloads: 3194
---

# Install selected ECC agent skills and rules across coding harnesses

Use Everything Claude Code to install curated skills, rules, hooks, and MCP configuration into Claude Code, Codex, Cursor, OpenCode, and related coding-agent harnesses without copying the whole repo blindly.

## Prerequisites

Claude Code, Codex, Cursor, OpenCode, or another supported harness; Node.js/npm for installer paths; optional MCP servers

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
For Claude Code, add the marketplace with `/plugin marketplace add https://github.com/affaan-m/everything-claude-code` and install `ecc@ecc`, or use the repo's selective installer such as `./install.sh --profile minimal --target claude` or `npx ecc-install --profile minimal --target claude`; for Codex, run `npm install && bash scripts/sync-ecc-to-codex.sh` from a checked-out repo.
```

## Documentation

- https://ecc.tools

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/install-selected-ecc-agent-skills-and-rules-across-coding-harnesses/)
