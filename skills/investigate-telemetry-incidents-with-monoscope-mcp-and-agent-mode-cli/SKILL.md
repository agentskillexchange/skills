---
title: "Investigate telemetry incidents with Monoscope MCP and agent-mode CLI"
description: "Connect agents to Monoscope so they can query logs, traces, metrics, monitors, and issues through stable JSON CLI output or MCP tools for incident triage."
verification: "security_reviewed"
source: "https://github.com/monoscope-tech/monoscope"
author: "monoscope-tech"
publisher_type: "open_source"
category:
  - "Monitoring & Alerts"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "monoscope-tech/monoscope"
  github_stars: 1130
---

# Investigate telemetry incidents with Monoscope MCP and agent-mode CLI

Connect agents to Monoscope so they can query logs, traces, metrics, monitors, and issues through stable JSON CLI output or MCP tools for incident triage.

## Prerequisites

Monoscope cloud or self-hosted stack, S3-compatible storage, OpenTelemetry or test telemetry data, Monoscope CLI or MCP-capable client, API key for MCP access

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Clone https://github.com/monoscope-tech/monoscope and run docker-compose up for self-hosting, or use Monoscope cloud. Install the CLI with the upstream install script and set MONOSCOPE_AGENT_MODE=1 for JSON output, or configure the MCP endpoint at https://api.monoscope.tech/api/v1/mcp with an Authorization header.
```

## Documentation

- https://docs.monoscope.tech

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/investigate-telemetry-incidents-with-monoscope-mcp-and-agent-mode-cli/)
