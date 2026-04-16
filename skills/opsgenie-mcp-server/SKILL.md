---
title: "OpsGenie MCP Server"
description: "OpsGenie MCP Server is built around Opsgenie incident and on-call platform. The underlying ecosystem is represented by opsgenie/opsgenie-nodejs-sdk (24+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like alerts, schedules, teams, escalation policies, notes, integrations and preserving the […]"
verification: "security_reviewed"
source: "https://github.com/opsgenie/opsgenie-nodejs-sdk"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "opsgenie/opsgenie-nodejs-sdk"
  github_stars: 24
  ase_npm_package: "opsgenie-sdk"
  npm_weekly_downloads: 5913
  license: "Apache-2.0"
---

# OpsGenie MCP Server

OpsGenie MCP Server is built around Opsgenie incident and on-call platform. The underlying ecosystem is represented by opsgenie/opsgenie-nodejs-sdk (24+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like alerts, schedules, teams, escalation policies, notes, integrations and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to opsgenie so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The implementation typically relies on alerts, schedules, teams, escalation policies, notes, integrations, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses alerts, schedules, teams, escalation policies, notes, integrations instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as alert triage, on-call auditing, and incident coordination.

Because this is exposed as an MCP skill, the tool surface is designed for agent-safe, structured calls instead of free-form shell usage. That means models can inspect schemas, call a narrow set of operations, and keep context across a longer workflow without re-implementing credentials or connection logic on every step. Key integration points include alert triage, on-call auditing, and incident coordination. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/opsgenie-mcp-server/)
