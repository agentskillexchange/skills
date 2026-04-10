---
title: "Prometheus AlertManager Bridge"
description: "Connects to Prometheus AlertManager API to query active alerts, silences, and alert groups. Parses PromQL alert rules and suggests runbook actions. Integrates with PagerDuty escalation policies."
slug: "prometheus-alertmanager-bridge"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/prometheus-alertmanager-bridge/"
---

# Prometheus AlertManager Bridge

Connects to Prometheus AlertManager API to query active alerts, silences, and alert groups. Parses PromQL alert rules and suggests runbook actions. Integrates with PagerDuty escalation policies.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install prometheus-alertmanager-bridge
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Prometheus AlertManager Bridge skill gives Claude direct access to your Prometheus AlertManager instance through its REST API (v2). It queries active alerts, manages silences, and retrieves alert group information for incident triage workflows.
When alerts fire, the skill retrieves full alert details including labels, annotations, generator URLs, and current status (firing, pending, resolved). It parses the underlying PromQL expressions from alert rules to explain what conditions triggered the alert in plain language.
The skill supports creating and expiring silences — useful for planned maintenance windows or acknowledged issues. It validates silence matchers against active alerts to confirm coverage. Alert group queries help identify correlated failures across services.
Integration with PagerDuty is built in: the skill reads escalation policies and on-call schedules to identify the right responder. It can acknowledge or resolve PagerDuty incidents and add notes with diagnostic findings. The skill also suggests runbook actions based on alert labels, matching against a configurable runbook directory for automated remediation steps. Designed for SRE teams managing Kubernetes clusters and microservice architectures.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-bridge/)
