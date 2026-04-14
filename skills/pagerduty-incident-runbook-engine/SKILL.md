---
title: "PagerDuty Incident Runbook Engine"
description: "Generates automated incident response runbooks triggered by PagerDuty webhooks via the PagerDuty Events API v2. Integrates with Datadog API and AWS CloudWatch for diagnostic data collection during incidents."
verification: security_reviewed
source: "https://github.com/PagerDuty/pdjs"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "pagerduty/pdjs"
  github_stars: 69
---

# PagerDuty Incident Runbook Engine

The PagerDuty Incident Runbook Engine creates automated diagnostic workflows triggered by PagerDuty incident events. It processes PagerDuty webhook payloads via the Events API v2, extracts alert metadata, and executes diagnostic runbook steps based on the triggering service and severity level.

The skill integrates with the Datadog API to fetch relevant metric snapshots, log patterns, and APM traces during incident triage. It queries AWS CloudWatch using the AWS SDK for recent alarm state changes, ECS task status, and RDS performance insights related to the incident scope.

Runbook templates are parameterized with service-specific diagnostic commands including kubectl cluster status checks, database connection pool metrics via pg_stat_activity, Redis memory analysis through redis-cli info, and Elasticsearch cluster health queries. The engine generates structured incident timelines with correlated metrics, creates Confluence pages via the Atlassian REST API for post-incident documentation, and updates PagerDuty incident notes with diagnostic findings through the PagerDuty REST API.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-incident-runbook-engine/)
