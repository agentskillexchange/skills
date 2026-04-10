---
name: PagerDuty Incident Runbook
description: Responds to PagerDuty incidents via the PagerDuty Events API v2 and REST
  API. Automatically executes diagnostic runbooks based on service and alert routing
  keys, and posts resolution notes back to the incident timeline.
verification: security_reviewed
source: https://agentskillexchange.com/skills/pagerduty-incident-runbook/
category:
- Runbooks &amp; Diagnostics
framework:
- OpenClaw
---
# PagerDuty Incident Runbook

The PagerDuty Incident Runbook agent integrates with PagerDuty via the Events API v2 and REST API (/incidents, /services, /escalation_policies) to automate incident response workflows. When triggered by a PagerDuty webhook, it identifies the affected service and matches it to a pre-configured diagnostic runbook.
The agent executes runbook steps sequentially: gathering system metrics, checking service health endpoints, querying log aggregation APIs (Elasticsearch, Datadog), and running connectivity tests. Each step's output is captured and posted as a timeline note on the PagerDuty incident via POST /incidents/{id}/notes.
For known failure patterns, the agent can escalate to automated remediation: restarting services via SSH, scaling infrastructure through cloud provider APIs, or toggling feature flags. It respects escalation policies and notifies on-call engineers when automated remediation fails. Supports custom severity mappings, maintenance window awareness, and integration with Statuspage for public communication during outages.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-incident-runbook/)
