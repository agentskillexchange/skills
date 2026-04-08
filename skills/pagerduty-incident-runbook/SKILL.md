---
title: PagerDuty Incident Runbook
description: 'The PagerDuty Incident Runbook agent integrates with PagerDuty via the
  Events API v2 and REST API (/incidents, /services, /escalation_policies) to automate
  incident response workflows. When triggered by a PagerDuty webhook, it identifies
  the affected service and matches it to a pre-configured diagnostic runbook. The
  agent executes runbook steps sequentially: gathering system metrics, checking service
  health endpoints, querying log aggregation APIs (Elasticsearch, Datadog), and running
  connectivity tests. Each step’s output is captured and posted as a timeline note
  on the PagerDuty incident via POST /incidents/{id}/notes. For known failure patterns,
  the agent can escalate to automated remediation: restarting services via SSH, scaling
  infrastructure through cloud provider APIs, or toggling feature flags. It respects
  escalation policies and notifies on-call engineers when automated remediation fails.
  Supports custom severity mappings, maintenance window awareness, and integration
  with Statuspage for public communication during outages.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/pagerduty-incident-runbook/
category:
- Runbooks &amp; Diagnostics
framework:
- OpenClaw
---

# PagerDuty Incident Runbook

The PagerDuty Incident Runbook agent integrates with PagerDuty via the Events API v2 and REST API (/incidents, /services, /escalation_policies) to automate incident response workflows. When triggered by a PagerDuty webhook, it identifies the affected service and matches it to a pre-configured diagnostic runbook. The agent executes runbook steps sequentially: gathering system metrics, checking service health endpoints, querying log aggregation APIs (Elasticsearch, Datadog), and running connectivity tests. Each step’s output is captured and posted as a timeline note on the PagerDuty incident via POST /incidents/{id}/notes. For known failure patterns, the agent can escalate to automated remediation: restarting services via SSH, scaling infrastructure through cloud provider APIs, or toggling feature flags. It respects escalation policies and notifies on-call engineers when automated remediation fails. Supports custom severity mappings, maintenance window awareness, and integration with Statuspage for public communication during outages.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pagerduty-incident-runbook/)
