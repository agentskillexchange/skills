---
title: "Generate and continuously refresh CLAUDE.md, AGENTS.md, MCP config, and editor rules from the live codebase with Caliber"
description: "Use Caliber when agent-facing repo instructions have started drifting from the actual codebase and you want one workflow to audit, generate, review, and keep those files fresh across multiple coding agents."
verification: "security_reviewed"
source: "https://github.com/caliber-ai-org/ai-setup"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "caliber-ai-org/ai-setup"
  github_stars: 717
---

# Generate and continuously refresh CLAUDE.md, AGENTS.md, MCP config, and editor rules from the live codebase with Caliber

Caliber is a repo-grounded setup and refresh workflow for agent-facing project instructions. It audits your current CLAUDE.md, AGENTS.md, Cursor rules, MCP config, and related files against the real filesystem, proposes changes as diffs, and can keep them refreshed as the codebase evolves.

Invoke this instead of editing each config file by hand when your team uses multiple coding agents and stale instructions are causing bad paths, missing dependencies, or inconsistent guidance. The scope boundary is tight: this skill is about generating and syncing agent instruction artifacts from a codebase, not acting as a general IDE, model, or agent platform.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/generate-and-continuously-refresh-claude-md-agents-md-mcp-config-and-editor-rules-from-the-live-codebase-with-caliber/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/generate-and-continuously-refresh-claude-md-agents-md-mcp-config-and-editor-rules-from-the-live-codebase-with-caliber
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/generate-and-continuously-refresh-claude-md-agents-md-mcp-config-and-editor-rules-from-the-live-codebase-with-caliber`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-and-continuously-refresh-claude-md-agents-md-mcp-config-and-editor-rules-from-the-live-codebase-with-caliber/)
