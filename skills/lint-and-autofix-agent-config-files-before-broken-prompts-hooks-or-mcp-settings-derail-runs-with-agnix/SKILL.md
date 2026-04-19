---
title: "Lint and autofix agent config files before broken prompts, hooks, or MCP settings derail runs with agnix"
description: "Agnix is a bounded preflight skill for agent operators who need to validate configuration files before an agent run, repo share, or CI check. Use it when the job is to catch malformed or weak agent instructions, invalid skill metadata, broken hook definitions, and bad MCP configuration before those issues turn into confusing runtime failures. The value is not &#8220;browse agent docs&#8221; or &#8220;use a generic linter&#8221;. The value is a concrete operator loop: scan agent config files, review findings, apply safe fixes, and rerun until the workspace is clean. Invoke this instead of using the product normally when you are working with repository-resident agent config files and want a repeatable guardrail around them. The scope boundary is narrow and skill-shaped: Agnix linting and autofix for agent configuration artifacts. It is not a general agent platform listing, not a generic security scanner, and not a catch-all coding assistant."
source: "https://github.com/agent-sh/agnix"
verification: "security_reviewed"
category:
  - "Security &amp; Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "agent-sh/agnix"
  github_stars: 179
  npm_package: "agnix"
  npm_weekly_downloads: 6006
---

# Lint and autofix agent config files before broken prompts, hooks, or MCP settings derail runs with agnix

Agnix is a bounded preflight skill for agent operators who need to validate configuration files before an agent run, repo share, or CI check. Use it when the job is to catch malformed or weak agent instructions, invalid skill metadata, broken hook definitions, and bad MCP configuration before those issues turn into confusing runtime failures. The value is not &#8220;browse agent docs&#8221; or &#8220;use a generic linter&#8221;. The value is a concrete operator loop: scan agent config files, review findings, apply safe fixes, and rerun until the workspace is clean. Invoke this instead of using the product normally when you are working with repository-resident agent config files and want a repeatable guardrail around them. The scope boundary is narrow and skill-shaped: Agnix linting and autofix for agent configuration artifacts. It is not a general agent platform listing, not a generic security scanner, and not a catch-all coding assistant.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-and-autofix-agent-config-files-before-broken-prompts-hooks-or-mcp-settings-derail-runs-with-agnix/)
