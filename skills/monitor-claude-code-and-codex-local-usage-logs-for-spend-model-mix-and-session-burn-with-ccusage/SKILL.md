---
title: "Monitor Claude Code and Codex local usage logs for spend, model mix, and session burn with ccusage"
description: "Use ccusage when an agent operator needs to turn local Claude Code or Codex usage logs into spend and usage reports instead of manually reading raw JSONL files."
verification: security_reviewed
source: "https://github.com/ryoppippi/ccusage"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "ryoppippi/ccusage"
  github_stars: 12900
  npm_package: "ccusage"
  npm_weekly_downloads: 154142
---

# Monitor Claude Code and Codex local usage logs for spend, model mix, and session burn with ccusage

Tool: ccusage. This skill gives an agent a concrete reporting job: read local coding-agent usage logs and summarize cost hotspots, model mix, and session burn patterns into something a human can act on.

When to use it: invoke this when you need budget reviews, local usage audits, or per-session cost triage for Claude Code or Codex runs. Using this skill is different from using the product normally because the workflow is operational rather than exploratory: ingest the logs, generate the report, and surface the sessions or models that deserve follow-up.

Scope boundary: this is not a generic analytics dashboard listing and not a broad coding-agent platform entry. Its boundary is specific: analyze locally stored agent usage logs and turn them into cost and usage diagnostics with ccusage.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/monitor-claude-code-and-codex-local-usage-logs-for-spend-model-mix-and-session-burn-with-ccusage
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/monitor-claude-code-and-codex-local-usage-logs-for-spend-model-mix-and-session-burn-with-ccusage` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/monitor-claude-code-and-codex-local-usage-logs-for-spend-model-mix-and-session-burn-with-ccusage/)
