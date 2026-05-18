---
name: "PagerDuty Incident Runbook Engine"
slug: "pagerduty-incident-runbook-engine"
description: "Generates automated incident response runbooks triggered by PagerDuty webhooks via the PagerDuty Events API v2. Integrates with Datadog API and AWS CloudWatch for diagnostic data collection during incidents."
github_stars: 69
verification: "listed"
source: "https://github.com/PagerDuty/pdjs"
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
tool_ecosystem:
  github_repo: "pagerduty/pdjs"
  github_stars: 69
  npm_package: "@pagerduty/pdjs"
  npm_weekly_downloads: 1033706
---

# PagerDuty Incident Runbook Engine

Generates automated incident response runbooks triggered by PagerDuty webhooks via the PagerDuty Events API v2. Integrates with Datadog API and AWS CloudWatch for diagnostic data collection during incidents.

## Installation

Use the upstream install or setup path that matches your environment:
- npm install --save @pagerduty/pdjs

Requirements and caveats from upstream:
- Supports Node and Browser environments
- Some endpoints require the setting of extra headers such as a From header.

Basic usage or getting-started notes:
- bash
- ### REST API
- REST API calls can be done using the convenience methods or by passing in a url or endpoint.

- Source: https://github.com/PagerDuty/pdjs
- Extracted from upstream docs: https://raw.githubusercontent.com/PagerDuty/pdjs/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-incident-runbook-engine/)
