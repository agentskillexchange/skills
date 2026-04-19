---
title: "Monitor Claude Code and Codex local usage logs for spend, model mix, and session burn with ccusage"
description: "Tool: ccusage. This skill gives an agent a concrete reporting job: read local coding-agent usage logs and summarize cost hotspots, model mix, and session burn patterns into something a human can act on. When to use it: invoke this when you need budget reviews, local usage audits, or per-session cost triage for Claude Code or Codex runs. Using this skill is different from using the product normally because the workflow is operational rather than exploratory: ingest the logs, generate the report, and surface the sessions or models that deserve follow-up. Scope boundary: this is not a generic analytics dashboard listing and not a broad coding-agent platform entry. Its boundary is specific: analyze locally stored agent usage logs and turn them into cost and usage diagnostics with ccusage."
source: "https://github.com/ryoppippi/ccusage"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "ryoppippi/ccusage"
  github_stars: 12900
  npm_package: "ccusage"
  npm_weekly_downloads: 154142
---

# Monitor Claude Code and Codex local usage logs for spend, model mix, and session burn with ccusage

Tool: ccusage. This skill gives an agent a concrete reporting job: read local coding-agent usage logs and summarize cost hotspots, model mix, and session burn patterns into something a human can act on. When to use it: invoke this when you need budget reviews, local usage audits, or per-session cost triage for Claude Code or Codex runs. Using this skill is different from using the product normally because the workflow is operational rather than exploratory: ingest the logs, generate the report, and surface the sessions or models that deserve follow-up. Scope boundary: this is not a generic analytics dashboard listing and not a broad coding-agent platform entry. Its boundary is specific: analyze locally stored agent usage logs and turn them into cost and usage diagnostics with ccusage.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/monitor-claude-code-and-codex-local-usage-logs-for-spend-model-mix-and-session-burn-with-ccusage/)
