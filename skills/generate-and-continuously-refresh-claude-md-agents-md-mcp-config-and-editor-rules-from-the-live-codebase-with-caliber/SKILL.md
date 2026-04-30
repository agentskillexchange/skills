---
title: "Generate and continuously refresh CLAUDE.md, AGENTS.md, MCP config, and editor rules from the live codebase with Caliber"
description: "Use Caliber when agent-facing repo instructions have started drifting from the actual codebase and you want one workflow to audit, generate, review, and keep those files fresh across multiple coding agents."
verification: "security_reviewed"
source: "https://github.com/caliber-ai-org/ai-setup"
author: "Caliber AI"
publisher_type: "organization"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "caliber-ai-org/ai-setup"
  github_stars: 717
---

# Generate and continuously refresh CLAUDE.md, AGENTS.md, MCP config, and editor rules from the live codebase with Caliber

Use Caliber when agent-facing repo instructions have started drifting from the actual codebase and you want one workflow to audit, generate, review, and keep those files fresh across multiple coding agents.

## Prerequisites

Node.js 20+, terminal access, and either Claude Code or Cursor CLI for /setup-caliber, or the Caliber CLI workflow for other supported agents.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Run `npx @rely-ai/caliber bootstrap`, then start a supported coding-agent session and run `/setup-caliber`, or use `caliber init` if you are not using Claude Code or Cursor CLI.
```

## Documentation

- https://caliber-ai.dev

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-and-continuously-refresh-claude-md-agents-md-mcp-config-and-editor-rules-from-the-live-codebase-with-caliber/)
