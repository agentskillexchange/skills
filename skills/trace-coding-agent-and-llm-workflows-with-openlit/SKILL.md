---
title: "Trace coding-agent and LLM workflows with OpenLIT"
description: "Use OpenLIT to instrument coding agents and LLM applications with OpenTelemetry traces, metrics, costs, prompts, tool calls, and evaluation signals."
verification: "security_reviewed"
source: "https://github.com/openlit/openlit"
author: "OpenLIT"
publisher_type: "organization"
category:
  - "Monitoring & Alerts"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "openlit/openlit"
  github_stars: 2532
  npm_package: "openlit"
  npm_weekly_downloads: 8382
---

# Trace coding-agent and LLM workflows with OpenLIT

Use OpenLIT to instrument coding agents and LLM applications with OpenTelemetry traces, metrics, costs, prompts, tool calls, and evaluation signals.

## Prerequisites

OpenLIT stack, OpenLIT SDK or CLI, OTLP endpoint or local OpenLIT dashboard

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Self-host with `git clone https://github.com/openlit/openlit.git` and `docker compose up -d`; install the Python SDK with `pip install openlit`; for coding-agent hooks run the OpenLIT CLI installer, then `openlit configure --endpoint http://127.0.0.1:4318` and `openlit coding install --vendor=all`.
```

## Documentation

- https://docs.openlit.io

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/trace-coding-agent-and-llm-workflows-with-openlit/)
