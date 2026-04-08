---
title: Prometheus AlertManager Bridge
description: 'The Prometheus AlertManager Bridge skill gives Claude direct access
  to your Prometheus AlertManager instance through its REST API (v2). It queries active
  alerts, manages silences, and retrieves alert group information for incident triage
  workflows. When alerts fire, the skill retrieves full alert details including labels,
  annotations, generator URLs, and current status (firing, pending, resolved). It
  parses the underlying PromQL expressions from alert rules to explain what conditions
  triggered the alert in plain language. The skill supports creating and expiring
  silences — useful for planned maintenance windows or acknowledged issues. It validates
  silence matchers against active alerts to confirm coverage. Alert group queries
  help identify correlated failures across services. Integration with PagerDuty is
  built in: the skill reads escalation policies and on-call schedules to identify
  the right responder. It can acknowledge or resolve PagerDuty incidents and add notes
  with diagnostic findings. The skill also suggests runbook actions based on alert
  labels, matching against a configurable runbook directory for automated remediation
  steps. Designed for SRE teams managing Kubernetes clusters and microservice architectures.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/prometheus-alertmanager-bridge/
category:
- Monitoring &amp; Alerts
framework:
- OpenClaw
---

# Prometheus AlertManager Bridge

The Prometheus AlertManager Bridge skill gives Claude direct access to your Prometheus AlertManager instance through its REST API (v2). It queries active alerts, manages silences, and retrieves alert group information for incident triage workflows. When alerts fire, the skill retrieves full alert details including labels, annotations, generator URLs, and current status (firing, pending, resolved). It parses the underlying PromQL expressions from alert rules to explain what conditions triggered the alert in plain language. The skill supports creating and expiring silences — useful for planned maintenance windows or acknowledged issues. It validates silence matchers against active alerts to confirm coverage. Alert group queries help identify correlated failures across services. Integration with PagerDuty is built in: the skill reads escalation policies and on-call schedules to identify the right responder. It can acknowledge or resolve PagerDuty incidents and add notes with diagnostic findings. The skill also suggests runbook actions based on alert labels, matching against a configurable runbook directory for automated remediation steps. Designed for SRE teams managing Kubernetes clusters and microservice architectures.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-bridge/)
