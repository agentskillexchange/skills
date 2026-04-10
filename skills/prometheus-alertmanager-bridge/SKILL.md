---
name: Prometheus AlertManager Bridge
description: Connects to Prometheus AlertManager API to query active alerts, silences,
  and alert groups. Parses PromQL alert rules and suggests runbook actions. Integrates
  with PagerDuty escalation policies.
verification: security_reviewed
source: https://agentskillexchange.com/skills/prometheus-alertmanager-bridge/
category:
- Monitoring &amp; Alerts
framework:
- OpenClaw
---
# Prometheus AlertManager Bridge

The Prometheus AlertManager Bridge skill gives Claude direct access to your Prometheus AlertManager instance through its REST API (v2). It queries active alerts, manages silences, and retrieves alert group information for incident triage workflows.
When alerts fire, the skill retrieves full alert details including labels, annotations, generator URLs, and current status (firing, pending, resolved). It parses the underlying PromQL expressions from alert rules to explain what conditions triggered the alert in plain language.
The skill supports creating and expiring silences — useful for planned maintenance windows or acknowledged issues. It validates silence matchers against active alerts to confirm coverage. Alert group queries help identify correlated failures across services.
Integration with PagerDuty is built in: the skill reads escalation policies and on-call schedules to identify the right responder. It can acknowledge or resolve PagerDuty incidents and add notes with diagnostic findings. The skill also suggests runbook actions based on alert labels, matching against a configurable runbook directory for automated remediation steps. Designed for SRE teams managing Kubernetes clusters and microservice architectures.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-bridge/)
