---
title: "Prometheus Alert Rule Synthesizer"
description: "Uses the Prometheus HTTP API v1 and PromQL to auto-generate alerting rules from metric baselines. Integrates with Alertmanager API for routing configuration and PagerDuty Events API v2 for escalation."
verification: "security_reviewed"
source: "https://github.com/prometheus/prometheus"
category:
  - "Monitoring & Alerts"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
  license: "Apache-2.0"
---

# Prometheus Alert Rule Synthesizer

The Prometheus Alert Rule Synthesizer connects to your Prometheus server via the HTTP API v1 to analyze historical metric data and automatically generate intelligent alerting rules. It queries the /api/v1/query_range endpoint to establish baseline patterns for key metrics like request latency, error rates, CPU utilization, and memory consumption. Using statistical analysis on PromQL query results, it calculates dynamic thresholds that account for daily and weekly seasonality patterns. Generated alert rules include proper for-duration clauses, severity labels, and detailed annotation templates with runbook links. The agent integrates with the Alertmanager API to configure routing trees, grouping rules, and inhibition policies. It connects to PagerDuty Events API v2 for critical alert escalation and Slack Incoming Webhooks for warning-level notifications. Alert rules are output in standard Prometheus YAML format ready for deployment.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-rule-synthesizer/)
