---
title: "Prometheus AlertManager Bridge"
description: "Connects to Prometheus AlertManager API to query active alerts, silences, and alert groups. Parses PromQL alert rules and suggests runbook actions. Integrates with PagerDuty escalation policies."
verification: security_reviewed
source: "https://github.com/prometheus/prometheus"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
---

# Prometheus AlertManager Bridge

The Prometheus AlertManager Bridge skill gives Claude direct access to your Prometheus AlertManager instance through its REST API (v2). It queries active alerts, manages silences, and retrieves alert group information for incident triage workflows.

When alerts fire, the skill retrieves full alert details including labels, annotations, generator URLs, and current status (firing, pending, resolved). It parses the underlying PromQL expressions from alert rules to explain what conditions triggered the alert in plain language.

The skill supports creating and expiring silences — useful for planned maintenance windows or acknowledged issues. It validates silence matchers against active alerts to confirm coverage. Alert group queries help identify correlated failures across services.

Integration with PagerDuty is built in: the skill reads escalation policies and on-call schedules to identify the right responder. It can acknowledge or resolve PagerDuty incidents and add notes with diagnostic findings. The skill also suggests runbook actions based on alert labels, matching against a configurable runbook directory for automated remediation steps. Designed for SRE teams managing Kubernetes clusters and microservice architectures.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-bridge/)
