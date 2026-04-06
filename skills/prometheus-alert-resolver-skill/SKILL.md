---
title: "Prometheus Alert Resolver"
slug: "prometheus-alert-resolver-skill"
description: "Resolves Prometheus alerts by querying the /api/v1/alerts and /api/v1/query_range endpoints for metric time series analysis. Executes playbook steps for common alerts like HighCPUUsage and DiskSpaceLow, validates PromQL recording rules, and silences alerts via Alertmanager /api/v2/silences."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/prometheus-alert-resolver-skill/"
category: "Runbooks &amp; Diagnostics"
framework: "Gemini"
---

# Prometheus Alert Resolver

Resolves Prometheus alerts by querying the /api/v1/alerts and /api/v1/query_range endpoints for metric time series analysis. Executes playbook steps for common alerts like HighCPUUsage and DiskSpaceLow, validates PromQL recording rules, and silences alerts via Alertmanager /api/v2/silences.

## Installation

Choose whichever method fits your setup:

1. Browse and install from Agent Skill Exchange.
2. Clone or download the upstream project manually.
3. Use the project package manager or installer if available.
4. Copy the skill into your local skills directory.
5. Follow the upstream documentation for environment-specific setup.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-resolver-skill/)
