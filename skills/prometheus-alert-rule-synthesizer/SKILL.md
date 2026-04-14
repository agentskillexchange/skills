---
title: "Prometheus Alert Rule Synthesizer"
description: "Uses the Prometheus HTTP API v1 and PromQL to auto-generate alerting rules from metric baselines. Integrates with Alertmanager API for routing configuration and PagerDuty Events API v2 for escalation."
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

# Prometheus Alert Rule Synthesizer

The Prometheus Alert Rule Synthesizer connects to your Prometheus server via the HTTP API v1 to analyze historical metric data and automatically generate intelligent alerting rules. It queries the /api/v1/query_range endpoint to establish baseline patterns for key metrics like request latency, error rates, CPU utilization, and memory consumption. Using statistical analysis on PromQL query results, it calculates dynamic thresholds that account for daily and weekly seasonality patterns. Generated alert rules include proper for-duration clauses, severity labels, and detailed annotation templates with runbook links. The agent integrates with the Alertmanager API to configure routing trees, grouping rules, and inhibition policies. It connects to PagerDuty Events API v2 for critical alert escalation and Slack Incoming Webhooks for warning-level notifications. Alert rules are output in standard Prometheus YAML format ready for deployment.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-rule-synthesizer/)
