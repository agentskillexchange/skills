---
title: "Scan agent repos for repo-poisoning, unsafe AI config files, and MCP attack surfaces with MEDUSA"
description: "Run a focused preflight scan over agent and MCP repositories to catch poisoned instruction files, dangerous configs, and AI-specific supply-chain risks before merge or deployment."
verification: "listed"
source: "https://github.com/Pantheon-Security/medusa"
category:
  - "Security & Verification"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "Pantheon-Security/medusa"
  github_stars: 256
---

# Scan agent repos for repo-poisoning, unsafe AI config files, and MCP attack surfaces with MEDUSA

Use MEDUSA when an agent or security reviewer needs one preflight scan over an agent-oriented repository to surface AI-specific attack paths before the repo is trusted or shipped. The point is not general vulnerability management. The bounded operator workflow is to scan a local or remote repo for poisoned AI editor files, prompt-injection surfaces, unsafe MCP configurations, and related supply-chain issues, then review the resulting findings before merge, deployment, or onboarding the repo into an agent workflow. That boundary, repo-level AI security screening with explicit repo-poisoning and MCP coverage, keeps this narrower than a plain scanner listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/scan-agent-repos-for-repo-poisoning-unsafe-ai-config-files-and-mcp-attack-surfaces-with-medusa/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/scan-agent-repos-for-repo-poisoning-unsafe-ai-config-files-and-mcp-attack-surfaces-with-medusa
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/scan-agent-repos-for-repo-poisoning-unsafe-ai-config-files-and-mcp-attack-surfaces-with-medusa`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scan-agent-repos-for-repo-poisoning-unsafe-ai-config-files-and-mcp-attack-surfaces-with-medusa/)
