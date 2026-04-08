---
title: Sentry Issue Spike Detection Agent
description: The Sentry Issue Spike Detection Agent connects to your Sentry organization
  using the Sentry Web API and continuously monitors issue event frequency across
  projects. It fetches recent events via the /api/0/organizations/{org}/issues/ endpoint
  with statsperiod and query parameters, computing rolling averages and standard deviations
  over configurable windows. When event frequency exceeds the baseline by a configurable
  multiplier, the agent classifies it as a spike and generates a structured alert
  containing the issue title, stack trace summary, affected users count, and first/last
  seen timestamps. Alerts can be routed to Slack via the Slack Web API, email via
  SMTP, or custom webhooks. The agent also groups related spikes using Sentry’s issue
  grouping metadata and suppresses duplicate notifications within a cooldown period.
  It supports Sentry DSN-based project filtering and can query the Sentry Releases
  API to correlate spikes with recent deployments.
verification: security_reviewed
source: https://github.com/getsentry/sentry
category:
- Monitoring &amp; Alerts
framework:
- Claude Agents
tool_ecosystem:
  github_repo: getsentry/sentry
  github_stars: 43486
---

# Sentry Issue Spike Detection Agent

The Sentry Issue Spike Detection Agent connects to your Sentry organization using the Sentry Web API and continuously monitors issue event frequency across projects. It fetches recent events via the /api/0/organizations/{org}/issues/ endpoint with statsperiod and query parameters, computing rolling averages and standard deviations over configurable windows. When event frequency exceeds the baseline by a configurable multiplier, the agent classifies it as a spike and generates a structured alert containing the issue title, stack trace summary, affected users count, and first/last seen timestamps. Alerts can be routed to Slack via the Slack Web API, email via SMTP, or custom webhooks. The agent also groups related spikes using Sentry’s issue grouping metadata and suppresses duplicate notifications within a cooldown period. It supports Sentry DSN-based project filtering and can query the Sentry Releases API to correlate spikes with recent deployments.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sentry-issue-spike-detection-agent/)
