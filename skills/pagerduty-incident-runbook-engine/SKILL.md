---
title: "PagerDuty Incident Runbook Engine"
description: "Generates automated incident response runbooks triggered by PagerDuty webhooks via the PagerDuty Events API v2. Integrates with Datadog API and AWS CloudWatch for diagnostic data collection during incidents."
verification: "security_reviewed"
source: "https://github.com/PagerDuty/pdjs"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
tool_ecosystem:
  license: "Apache-2.0"
---

# PagerDuty Incident Runbook Engine

The PagerDuty Incident Runbook Engine creates automated diagnostic workflows triggered by PagerDuty incident events. It processes PagerDuty webhook payloads via the Events API v2, extracts alert metadata, and executes diagnostic runbook steps based on the triggering service and severity level.

The skill integrates with the Datadog API to fetch relevant metric snapshots, log patterns, and APM traces during incident triage. It queries AWS CloudWatch using the AWS SDK for recent alarm state changes, ECS task status, and RDS performance insights related to the incident scope.

Runbook templates are parameterized with service-specific diagnostic commands including kubectl cluster status checks, database connection pool metrics via pg_stat_activity, Redis memory analysis through redis-cli info, and Elasticsearch cluster health queries. The engine generates structured incident timelines with correlated metrics, creates Confluence pages via the Atlassian REST API for post-incident documentation, and updates PagerDuty incident notes with diagnostic findings through the PagerDuty REST API.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-incident-runbook-engine/)
