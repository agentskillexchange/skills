---
title: "Investigate production issues from Slack with runbooks and monitoring MCPs using DIY AI Debugging Agent Toolkit"
description: "Handle alerts and debugging questions from Slack, query connected monitoring MCP servers, and follow runbook-guided investigation steps for live incidents."
verification: "security_reviewed"
source: "https://github.com/DrDroidLab/sample-debug-agent"
author: "DrDroidLab"
publisher_type: "open_source_project"
category:
  - "Runbooks & Diagnostics"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "DrDroidLab/sample-debug-agent"
  github_stars: 6
---

# Investigate production issues from Slack with runbooks and monitoring MCPs using DIY AI Debugging Agent Toolkit

Handle alerts and debugging questions from Slack, query connected monitoring MCP servers, and follow runbook-guided investigation steps for live incidents.

## Prerequisites

Slack app, MCP server connections for monitoring tools, Python runtime, OpenAI key, optional runbooks or prompts for incident workflows

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
pip install uv && uv sync && uv run python app.py
```

## Documentation

- https://github.com/DrDroidLab/sample-debug-agent

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/investigate-production-issues-from-slack-with-runbooks-and-monitoring-mcps-using-diy-ai-debugging-agent-toolkit/)
