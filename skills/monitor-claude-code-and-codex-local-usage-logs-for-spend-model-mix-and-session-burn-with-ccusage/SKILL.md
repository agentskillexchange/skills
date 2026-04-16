---
title: "Monitor Claude Code and Codex local usage logs for spend, model mix, and session burn with ccusage"
description: "Use ccusage when an agent operator needs to turn local Claude Code or Codex usage logs into spend and usage reports instead of manually reading raw JSONL files."
verification: "security_reviewed"
source: "https://github.com/ryoppippi/ccusage"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "ryoppippi/ccusage"
  github_stars: 12900
  ase_npm_package: "ccusage"
  npm_weekly_downloads: 154142
---

# Monitor Claude Code and Codex local usage logs for spend, model mix, and session burn with ccusage

Tool: ccusage. This skill gives an agent a concrete reporting job: read local coding-agent usage logs and summarize cost hotspots, model mix, and session burn patterns into something a human can act on.

When to use it: invoke this when you need budget reviews, local usage audits, or per-session cost triage for Claude Code or Codex runs. Using this skill is different from using the product normally because the workflow is operational rather than exploratory: ingest the logs, generate the report, and surface the sessions or models that deserve follow-up.

Scope boundary: this is not a generic analytics dashboard listing and not a broad coding-agent platform entry. Its boundary is specific: analyze locally stored agent usage logs and turn them into cost and usage diagnostics with ccusage.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/monitor-claude-code-and-codex-local-usage-logs-for-spend-model-mix-and-session-burn-with-ccusage/)
