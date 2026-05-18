---
name: "PagerDuty On-Call Escalation Checker"
slug: "pagerduty-on-call-escalation-checker-2"
description: "Queries PagerDuty to show who is currently on-call for each escalation policy, surfaces unacknowledged incidents, and identifies schedule coverage gaps for the next 7 days. Useful for handoff checks and pre-weekend coverage audits. Read-only skill."
github_stars: 69
verification: "listed"
source: "https://github.com/PagerDuty/pdjs"
category: "Runbooks & Diagnostics"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "pagerduty/pdjs"
  github_stars: 69
  npm_package: "@pagerduty/pdjs"
  npm_weekly_downloads: 1025138
---

# PagerDuty On-Call Escalation Checker

Queries PagerDuty to show who is currently on-call for each escalation policy, surfaces unacknowledged incidents, and identifies schedule coverage gaps for the next 7 days. Useful for handoff checks and pre-weekend coverage audits. Read-only skill.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-on-call-escalation-checker-2/)
