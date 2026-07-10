---
title: "Scan agent repos for repo-poisoning, unsafe AI config files, and MCP attack surfaces with MEDUSA"
description: "Run a focused preflight scan over agent and MCP repositories to catch poisoned instruction files, dangerous configs, and AI-specific supply-chain risks before merge or deployment."
verification: "security_reviewed"
source: "https://github.com/Pantheon-Security/medusa"
author: "Pantheon Security"
publisher_type: "organization"
category:
  - "Security & Verification"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "Pantheon-Security/medusa"
  github_stars: 256
---

# Scan agent repos for repo-poisoning, unsafe AI config files, and MCP attack surfaces with MEDUSA

Run a focused preflight scan over agent and MCP repositories to catch poisoned instruction files, dangerous configs, and AI-specific supply-chain risks before merge or deployment.

## Prerequisites

Python 3 environment, pip, MEDUSA package, access to the local repo or target GitHub repository, and optional external linters for expanded coverage

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install the upstream package with pip install medusa-security, then run medusa scan against the target repository or use medusa scan --git against the remote GitHub repo to review AI security findings before merge or deployment.
```

## Documentation

- https://github.com/Pantheon-Security/medusa

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scan-agent-repos-for-repo-poisoning-unsafe-ai-config-files-and-mcp-attack-surfaces-with-medusa/)
