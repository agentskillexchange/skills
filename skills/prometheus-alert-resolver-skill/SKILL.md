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

Choose the installation path that fits your setup:

1. Install from Agent Skill Exchange in the OpenClaw UI.
2. Copy the skill folder into your local skills directory.
3. Add it to your shared workspace skills collection.
4. Install it through a compatible agent skill manager.
5. Clone or download the upstream source and wire it into your agent runtime.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-resolver-skill/)
