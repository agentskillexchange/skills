---
title: "Test Claude Code plugin and skill triggering with staged eval runs using cc-plugin-eval"
description: "Run staged evaluations against a Claude Code plugin to verify that skills, agents, commands, hooks, and MCP components trigger when they should."
verification: "security_reviewed"
source: "https://github.com/sjnims/cc-plugin-eval"
author: "sjnims"
publisher_type: "individual"
category:
  - "Code Quality & Review"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "sjnims/cc-plugin-eval"
  github_stars: 16
---

# Test Claude Code plugin and skill triggering with staged eval runs using cc-plugin-eval

Run staged evaluations against a Claude Code plugin to verify that skills, agents, commands, hooks, and MCP components trigger when they should.

## Prerequisites

Node.js 20+, Anthropic API key, Claude Code plugin directory

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Clone the repo, run `npm install` and `npm run build`, set `ANTHROPIC_API_KEY` in `.env`, then run `npx cc-plugin-eval run -p ./path/to/your/plugin` or start with `--dry-run` for an estimate.
```

## Documentation

- https://github.com/sjnims/cc-plugin-eval

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/test-claude-code-plugin-and-skill-triggering-with-staged-eval-runs-using-cc-plugin-eval/)
