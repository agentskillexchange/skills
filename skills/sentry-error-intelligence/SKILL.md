---
title: Sentry Error Intelligence
description: The Sentry Error Intelligence skill transforms raw error data into actionable
  insights for AI agent workflows. It connects to the Sentry API v0, querying /api/0/organizations/{org}/issues/
  with Sentry Query Language (SQL) filters to identify trending errors, regressions,
  and new issue spikes across projects. Stack trace analysis uses Sentry enhanced
  event data from the /api/0/issues/{issue_id}/events/latest/ endpoint, parsing frame-level
  information including source context, variable values, and breadcrumb trails. The
  skill implements custom fingerprinting rules via the /api/0/projects/{org}/{project}/grouping-configs/
  endpoint to improve issue deduplication accuracy. Auto-assignment leverages GitHub
  CODEOWNERS files parsed through the GitHub Contents API, matching error source file
  paths to responsible teams. The skill creates GitHub issues for persistent errors
  via the Issues API v3, including Sentry event links, affected user counts, and frequency
  charts generated from the Sentry Stats API (/api/0/organizations/{org}/stats_v2/).
  Release health monitoring tracks crash-free session rates through the Sessions API,
  triggering rollback recommendations when rates drop below configurable thresholds.
verification: security_reviewed
source: https://agentskillexchange.com/skills/sentry-error-intelligence/
category:
- Monitoring &amp; Alerts
framework:
- Claude Code
---

# Sentry Error Intelligence

The Sentry Error Intelligence skill transforms raw error data into actionable insights for AI agent workflows. It connects to the Sentry API v0, querying /api/0/organizations/{org}/issues/ with Sentry Query Language (SQL) filters to identify trending errors, regressions, and new issue spikes across projects. Stack trace analysis uses Sentry enhanced event data from the /api/0/issues/{issue_id}/events/latest/ endpoint, parsing frame-level information including source context, variable values, and breadcrumb trails. The skill implements custom fingerprinting rules via the /api/0/projects/{org}/{project}/grouping-configs/ endpoint to improve issue deduplication accuracy. Auto-assignment leverages GitHub CODEOWNERS files parsed through the GitHub Contents API, matching error source file paths to responsible teams. The skill creates GitHub issues for persistent errors via the Issues API v3, including Sentry event links, affected user counts, and frequency charts generated from the Sentry Stats API (/api/0/organizations/{org}/stats_v2/). Release health monitoring tracks crash-free session rates through the Sessions API, triggering rollback recommendations when rates drop below configurable thresholds.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sentry-error-intelligence/)
