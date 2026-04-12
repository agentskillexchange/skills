---
title: "Prometheus Alert Resolver"
description: "Resolves Prometheus alerts by querying the /api/v1/alerts and /api/v1/query_range endpoints for metric time series analysis. Executes playbook steps for common alerts like HighCPUUsage and DiskSpaceLow, validates PromQL recording rules, and silences alerts via Alertmanager /api/v2/silences."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/prometheus-alert-resolver-skill/"
---

# Prometheus Alert Resolver

Resolves Prometheus alerts by querying the /api/v1/alerts and /api/v1/query_range endpoints for metric time series analysis. Executes playbook steps for common alerts like HighCPUUsage and DiskSpaceLow, validates PromQL recording rules, and silences alerts via Alertmanager /api/v2/silences.

## Installation

Choose the path that fits your setup:

1. Clone this repository and use the skill locally.
2. Copy the skill folder into your local skills directory.
3. Add the skill as a Git submodule in your skills workspace.
4. Vendor the files into an internal skill catalog for your team.
5. Reference the upstream source and recreate the skill in your own agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-resolver-skill/)
