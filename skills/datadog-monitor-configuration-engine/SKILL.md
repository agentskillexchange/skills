---
title: "Datadog Monitor Configuration Engine"
description: "Interfaces with the Datadog API v2 monitors and dashboards endpoints to programmatically create and manage monitors. Uses DogStatsD protocol for custom metric submission and Datadog Terraform provider for IaC."
verification: security_reviewed
source: "https://github.com/DataDog/dd-trace-js"
category:
  - "Monitoring & Alerts"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "datadog/dd-trace-js"
  github_stars: 791
  ase_npm_package: "dd-trace"
  npm_weekly_downloads: 6596660
---

# Datadog Monitor Configuration Engine

The Datadog Monitor Configuration Engine interfaces with the Datadog API v2 to programmatically manage monitoring infrastructure across your entire stack. It creates metric monitors, log monitors, APM trace monitors, and composite monitors through the /api/v2/monitors endpoint with proper query syntax and evaluation parameters. The agent uses the DogStatsD protocol to submit custom business metrics from application code, automatically generating corresponding monitors with appropriate thresholds. Dashboard definitions are managed as code using the Datadog dashboard API, supporting template variables and widget configurations for team-specific views. Integration with the Datadog Terraform provider enables version-controlled monitor management through HCL definitions. The engine includes anomaly detection monitor setup using the Datadog machine learning algorithms, configuring sensitivity levels and alert recovery conditions based on historical metric behavior.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/datadog-monitor-configuration-engine
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/datadog-monitor-configuration-engine` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-monitor-configuration-engine/)
