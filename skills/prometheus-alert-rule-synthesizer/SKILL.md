---
name: Prometheus Alert Rule Synthesizer
description: Uses the Prometheus HTTP API v1 and PromQL to auto-generate alerting
  rules from metric baselines. Integrates with Alertmanager API for routing configuration
  and PagerDuty Events API v2 for escalation.
verification: security_reviewed
source: https://agentskillexchange.com/skills/prometheus-alert-rule-synthesizer/
category:
- Monitoring &amp; Alerts
framework:
- OpenClaw
---
# Prometheus Alert Rule Synthesizer

The Prometheus Alert Rule Synthesizer connects to your Prometheus server via the HTTP API v1 to analyze historical metric data and automatically generate intelligent alerting rules. It queries the /api/v1/query_range endpoint to establish baseline patterns for key metrics like request latency, error rates, CPU utilization, and memory consumption. Using statistical analysis on PromQL query results, it calculates dynamic thresholds that account for daily and weekly seasonality patterns. Generated alert rules include proper for-duration clauses, severity labels, and detailed annotation templates with runbook links. The agent integrates with the Alertmanager API to configure routing trees, grouping rules, and inhibition policies. It connects to PagerDuty Events API v2 for critical alert escalation and Slack Incoming Webhooks for warning-level notifications. Alert rules are output in standard Prometheus YAML format ready for deployment.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-rule-synthesizer/)
