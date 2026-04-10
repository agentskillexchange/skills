---
name: "PagerDuty Incident Runbook Engine"
description: "Generates automated incident response runbooks triggered by PagerDuty webhooks via the PagerDuty Events API v2. Integrates with Datadog API and AWS CloudWatch for diagnostic data collection during incidents."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/pagerduty-incident-runbook-engine/"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
---

# PagerDuty Incident Runbook Engine

The PagerDuty Incident Runbook Engine creates automated diagnostic workflows triggered by PagerDuty incident events. It processes PagerDuty webhook payloads via the Events API v2, extracts alert metadata, and executes diagnostic runbook steps based on the triggering service and severity level.
The skill integrates with the Datadog API to fetch relevant metric snapshots, log patterns, and APM traces during incident triage. It queries AWS CloudWatch using the AWS SDK for recent alarm state changes, ECS task status, and RDS performance insights related to the incident scope.
Runbook templates are parameterized with service-specific diagnostic commands including kubectl cluster status checks, database connection pool metrics via pg_stat_activity, Redis memory analysis through redis-cli info, and Elasticsearch cluster health queries. The engine generates structured incident timelines with correlated metrics, creates Confluence pages via the Atlassian REST API for post-incident documentation, and updates PagerDuty incident notes with diagnostic findings through the PagerDuty REST API.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-incident-runbook-engine/)
