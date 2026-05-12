---
title: "Monitor Claude Code and Codex local usage logs for spend, model mix, and session burn with ccusage"
slug: "monitor-claude-code-and-codex-local-usage-logs-for-spend-model-mix-and-session-burn-with-ccusage"
description: "Use ccusage when an agent operator needs to turn local Claude Code or Codex usage logs into spend and usage reports instead of manually reading raw JSONL files."
verification: "security_reviewed"
source: "https://github.com/ryoppippi/ccusage"
author: "ryoppippi"
publisher_type: "individual"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "ryoppippi/ccusage"
  github_stars: 12900
  npm_package: "ccusage"
  npm_weekly_downloads: 154142
---

# Monitor Claude Code and Codex local usage logs for spend, model mix, and session burn with ccusage

Use ccusage when an agent operator needs to turn local Claude Code or Codex usage logs into spend and usage reports instead of manually reading raw JSONL files.

## Prerequisites

Local Claude Code or Codex usage logs, ccusage, and shell access on the machine that stores the logs.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install ccusage using the package or binary method documented in the repository, point it at the local usage-log location for your coding agent, then run the report commands you need to summarize spend, model mix, and session usage.
```

## Documentation

- https://github.com/ryoppippi/ccusage#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/monitor-claude-code-and-codex-local-usage-logs-for-spend-model-mix-and-session-burn-with-ccusage/)
