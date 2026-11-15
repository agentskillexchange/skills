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

Clone the upstream repository:

- git clone https://github.com/eugeniughelbur/obsidian-second-brain.git

Configure credentials by copying .env.example to ~/.config/obsidian-second-brain/.env and adding the keys required for the workflows you use. Upstream documents bootstrapping a vault with:

- python bootstrap_vault.py --path ~/my-vault --name "Your Name" --preset builder

Then run install.sh from the cloned repository and answer the setup prompts.

- Source: https://github.com/eugeniughelbur/obsidian-second-brain
- Extracted from upstream docs: https://raw.githubusercontent.com/eugeniughelbur/obsidian-second-brain/HEAD/README.md

## Documentation

- https://github.com/eugeniughelbur/obsidian-second-brain

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/operate-an-obsidian-vault-as-an-agent-maintained-second-brain/)
