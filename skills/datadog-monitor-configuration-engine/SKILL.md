---
name: "Datadog Monitor Configuration Engine"
description: "Interfaces with the Datadog API v2 monitors and dashboards endpoints to programmatically create and manage monitors. Uses DogStatsD protocol for custom metric submission and Datadog Terraform provider for IaC."
category: "Monitoring &amp; Alerts"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/datadog-monitor-configuration-engine/"
---
# Datadog Monitor Configuration Engine

Interfaces with the Datadog API v2 monitors and dashboards endpoints to programmatically create and manage monitors. Uses DogStatsD protocol for custom metric submission and Datadog Terraform provider for IaC.

## Overview

The Datadog Monitor Configuration Engine interfaces with the Datadog API v2 to programmatically manage monitoring infrastructure across your entire stack. It creates metric monitors, log monitors, APM trace monitors, and composite monitors through the /api/v2/monitors endpoint with proper query syntax and evaluation parameters. The agent uses the DogStatsD protocol to submit custom business metrics from application code, automatically generating corresponding monitors with appropriate thresholds. Dashboard definitions are managed as code using the Datadog dashboard API, supporting template variables and widget configurations for team-specific views. Integration with the Datadog Terraform provider enables version-controlled monitor management through HCL definitions. The engine includes anomaly detection monitor setup using the Datadog machine learning algorithms, configuring sensitivity levels and alert recovery conditions based on historical metric behavior.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill datadog-monitor-configuration-engine
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill datadog-monitor-configuration-engine -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill datadog-monitor-configuration-engine -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill datadog-monitor-configuration-engine -a codex
```

### OpenClaw

```bash
clawhub install datadog-monitor-configuration-engine
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-monitor-configuration-engine/)
