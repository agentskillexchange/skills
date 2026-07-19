---
name: "Operate an Obsidian vault as an agent-maintained second brain"
slug: "operate-an-obsidian-vault-as-an-agent-maintained-second-brain"
description: "Let agents ingest sources, update Obsidian notes, reconcile contradictions, search vault context, and maintain a living knowledge base through documented commands."
github_stars: 3399
verification: "security_reviewed"
source: "https://github.com/eugeniughelbur/obsidian-second-brain"
author: "Eugeniu Ghelbur"
publisher_type: "individual"
category: "Calendar, Email & Productivity"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "eugeniughelbur/obsidian-second-brain"
  github_stars: 3399
---

# Operate an Obsidian vault as an agent-maintained second brain

Let agents ingest sources, update Obsidian notes, reconcile contradictions, search vault context, and maintain a living knowledge base through documented commands.

## Prerequisites

Obsidian vault, Claude Code or another supported CLI agent, optional MCP server, optional research/API integrations for web and media commands

## Installation

Requirements and caveats from upstream:
- | /obsidian-projects | Live project status from git + local docs -- infers all context from vault notes, no config required |
- python bootstrap_vault.py --path ~/my-vault --name "Your Name" --preset builder

Basic usage or getting-started notes:
- Run both for high-stakes topics. <strong>Contradictions across the two are where the insight is.</strong></em>
- | /obsidian-architect | Scans a codebase and writes maintained architecture notes (overview, modules, decisions) into the vault; re-run to refresh |
- **Setup:** copy .env.example to ~/.config/obsidian-second-brain/.env, add your keys (xAI, Perplexity, YouTube optional, OpenAI optional for podcast Whisper). Run install.sh and answer "y" to the research prompt to do...

- Source: https://github.com/eugeniughelbur/obsidian-second-brain
- Extracted from upstream docs: https://raw.githubusercontent.com/eugeniughelbur/obsidian-second-brain/HEAD/README.md

## Documentation

- https://github.com/eugeniughelbur/obsidian-second-brain

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/operate-an-obsidian-vault-as-an-agent-maintained-second-brain/)
