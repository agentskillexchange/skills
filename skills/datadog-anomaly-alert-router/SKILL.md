---
title: "Datadog Anomaly Alert Router"
description: "Routes Datadog anomaly detection alerts to appropriate response channels using the Datadog Events API v2 and Monitors API. Applies severity-based escalation rules with PagerDuty and Slack webhook integration."
verification: security_reviewed
source: "https://github.com/DataDog/dd-trace-js"
category:
  - "Monitoring & Alerts"
framework:
  - "MCP"
---

# Datadog Anomaly Alert Router

Routes Datadog anomaly detection alerts to appropriate response channels using the Datadog Events API v2 and Monitors API. Applies severity-based escalation rules with PagerDuty and Slack webhook integration.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/datadog-anomaly-alert-router
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/datadog-anomaly-alert-router` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-anomaly-alert-router/)
