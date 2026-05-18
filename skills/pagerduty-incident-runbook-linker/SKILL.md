---
name: "PagerDuty Incident Runbook Linker"
slug: "pagerduty-incident-runbook-linker"
description: "Automatically links PagerDuty incidents to relevant runbooks using the PagerDuty Events API v2 and service directory. Matches incident alerts to runbook tags via Elasticsearch fuzzy queries."
github_stars: 69
verification: "listed"
source: "https://github.com/PagerDuty/pdjs"
category: "Monitoring & Alerts"
framework: "OpenClaw"
tool_ecosystem:
  github_repo: "pagerduty/pdjs"
  github_stars: 69
  npm_package: "@pagerduty/pdjs"
  npm_weekly_downloads: 1033706
---

# PagerDuty Incident Runbook Linker

Automatically links PagerDuty incidents to relevant runbooks using the PagerDuty Events API v2 and service directory. Matches incident alerts to runbook tags via Elasticsearch fuzzy queries.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-incident-runbook-linker/)
