---
title: "Prometheus Alert Resolver"
description: "Resolves Prometheus alerts by querying the /api/v1/alerts and /api/v1/query_range endpoints for metric time series analysis. Executes playbook steps for common alerts like HighCPUUsage and DiskSpaceLow, validates PromQL recording rules, and silences alerts via Alertmanager /api/v2/silences."
slug: "prometheus-alert-resolver-skill"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/prometheus-alert-resolver-skill/"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Gemini"
---
# Prometheus Alert Resolver

Resolves Prometheus alerts by querying the /api/v1/alerts and /api/v1/query_range endpoints for metric time series analysis. Executes playbook steps for common alerts like HighCPUUsage and DiskSpaceLow, validates PromQL recording rules, and silences alerts via Alertmanager /api/v2/silences.

## Installation

Choose the method that fits your setup:
1. Install from the Agent Skill Exchange website
2. Clone or download the upstream source repository
3. Install via npm if the project is published there
4. Use the tool's package manager or release binaries
5. Copy the skill files into your local skills directory manually

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-resolver-skill/)
