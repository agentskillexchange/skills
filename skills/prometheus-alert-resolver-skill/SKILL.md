---
name: "prometheus-alert-resolver-skill"
description: "Resolves Prometheus alerts by querying the /api/v1/alerts and /api/v1/query_range endpoints for metric time series analysis. Executes playbook steps for common alerts like HighCPUUsage and DiskSpaceLow, validates PromQL recording rules, and silences alerts via Alertmanager /api/v2/silences."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/prometheus-alert-resolver-skill/"
---

# Prometheus Alert Resolver

Resolves Prometheus alerts by querying the /api/v1/alerts and /api/v1/query_range endpoints for metric time series analysis. Executes playbook steps for common alerts like HighCPUUsage and DiskSpaceLow, validates PromQL recording rules, and silences alerts via Alertmanager /api/v2/silences.

## Installation

You can install this skill using one of these common methods:

1. **ClawHub** — install from the marketplace if available.
2. **Git clone** — clone the skill folder into your local skills directory.
3. **Download ZIP** — download and extract the skill files manually.
4. **Copy files** — copy the skill directory into your agent skills path.
5. **Package manager / upstream installer** — use the original project installer if the source provides one.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-resolver-skill/)
