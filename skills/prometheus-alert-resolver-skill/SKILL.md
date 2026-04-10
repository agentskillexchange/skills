---
title: "Prometheus Alert Resolver"
description: "Resolves Prometheus alerts by querying the /api/v1/alerts and /api/v1/query_range endpoints for metric time series analysis. Executes playbook steps for common alerts like HighCPUUsage and DiskSpaceLow, validates PromQL recording rules, and silences alerts via Alertmanager /api/v2/silences."
slug: "prometheus-alert-resolver-skill"
category:
  - "Runbooks &amp; Diagnostics"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/prometheus-alert-resolver-skill/"
---

# Prometheus Alert Resolver

Resolves Prometheus alerts by querying the /api/v1/alerts and /api/v1/query_range endpoints for metric time series analysis. Executes playbook steps for common alerts like HighCPUUsage and DiskSpaceLow, validates PromQL recording rules, and silences alerts via Alertmanager /api/v2/silences.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install prometheus-alert-resolver-skill
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-resolver-skill/)
