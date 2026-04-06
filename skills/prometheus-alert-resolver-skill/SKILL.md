---
title: "Prometheus Alert Resolver"
description: "Resolves Prometheus alerts by querying the /api/v1/alerts and /api/v1/query_range endpoints for metric time series analysis. Executes playbook steps for common alerts like HighCPUUsage and DiskSpaceLow, validates PromQL recording rules, and silences alerts via Alertmanager /api/v2/silences."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/prometheus-alert-resolver-skill/"
category: ["Runbooks &amp; Diagnostics"]
framework: ["Gemini"]
---

# Prometheus Alert Resolver

Resolves Prometheus alerts by querying the /api/v1/alerts and /api/v1/query_range endpoints for metric time series analysis. Executes playbook steps for common alerts like HighCPUUsage and DiskSpaceLow, validates PromQL recording rules, and silences alerts via Alertmanager /api/v2/silences.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI.
2. Add it through your agent or assistant skill manager.
3. Clone or copy this skill into your local skills directory.
4. Install with a package manager if the upstream project provides one.
5. Follow the upstream project documentation for manual setup.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-resolver-skill/)
