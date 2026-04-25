---
title: "Lint and autofix agent config files before broken prompts, hooks, or MCP settings derail runs with agnix"
description: "Validate and optionally autofix SKILL.md, CLAUDE.md, AGENTS.md, hooks, and MCP config files before bad agent metadata or wiring silently breaks a workflow."
verification: "security_reviewed"
source: "https://github.com/agent-sh/agnix"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "agent-sh/agnix"
  github_stars: 179
  npm_package: "agnix"
  npm_weekly_downloads: 6006
---

# Lint and autofix agent config files before broken prompts, hooks, or MCP settings derail runs with agnix

Agnix is a bounded preflight skill for agent operators who need to validate configuration files before an agent run, repo share, or CI check. Use it when the job is to catch malformed or weak agent instructions, invalid skill metadata, broken hook definitions, and bad MCP configuration before those issues turn into confusing runtime failures. The value is not “browse agent docs” or “use a generic linter”. The value is a concrete operator loop: scan agent config files, review findings, apply safe fixes, and rerun until the workspace is clean. Invoke this instead of using the product normally when you are working with repository-resident agent config files and want a repeatable guardrail around them. The scope boundary is narrow and skill-shaped: Agnix linting and autofix for agent configuration artifacts. It is not a general agent platform listing, not a generic security scanner, and not a catch-all coding assistant.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/lint-and-autofix-agent-config-files-before-broken-prompts-hooks-or-mcp-settings-derail-runs-with-agnix/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/lint-and-autofix-agent-config-files-before-broken-prompts-hooks-or-mcp-settings-derail-runs-with-agnix
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/lint-and-autofix-agent-config-files-before-broken-prompts-hooks-or-mcp-settings-derail-runs-with-agnix`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-and-autofix-agent-config-files-before-broken-prompts-hooks-or-mcp-settings-derail-runs-with-agnix/)
