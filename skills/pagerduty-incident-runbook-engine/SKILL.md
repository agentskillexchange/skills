---
title: "PagerDuty Incident Runbook Engine"
description: "The PagerDuty Incident Runbook Engine creates automated diagnostic workflows triggered by PagerDuty incident events. It processes PagerDuty webhook payloads via the Events API v2, extracts alert metadata, and executes diagnostic runbook steps based on the triggering service and severity level. The skill integrates with the Datadog API to fetch relevant metric snapshots, log patterns, and APM traces during incident triage. It queries AWS CloudWatch using the AWS SDK for recent alarm state changes, ECS task status, and RDS performance insights related to the incident scope. Runbook templates are parameterized with service-specific diagnostic commands including kubectl cluster status checks, database connection pool metrics via pg_stat_activity, Redis memory analysis through redis-cli info, and Elasticsearch cluster health queries. The engine generates structured incident timelines with correlated metrics, creates Confluence pages via the Atlassian REST API for post-incident documentation, and updates PagerDuty incident notes with diagnostic findings through the PagerDuty REST API."
source: "https://github.com/PagerDuty/pdjs"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
---

# PagerDuty Incident Runbook Engine

The PagerDuty Incident Runbook Engine creates automated diagnostic workflows triggered by PagerDuty incident events. It processes PagerDuty webhook payloads via the Events API v2, extracts alert metadata, and executes diagnostic runbook steps based on the triggering service and severity level. The skill integrates with the Datadog API to fetch relevant metric snapshots, log patterns, and APM traces during incident triage. It queries AWS CloudWatch using the AWS SDK for recent alarm state changes, ECS task status, and RDS performance insights related to the incident scope. Runbook templates are parameterized with service-specific diagnostic commands including kubectl cluster status checks, database connection pool metrics via pg_stat_activity, Redis memory analysis through redis-cli info, and Elasticsearch cluster health queries. The engine generates structured incident timelines with correlated metrics, creates Confluence pages via the Atlassian REST API for post-incident documentation, and updates PagerDuty incident notes with diagnostic findings through the PagerDuty REST API.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-incident-runbook-engine/)
