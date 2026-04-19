---
title: "Datadog Monitor Configuration Engine"
description: "The Datadog Monitor Configuration Engine interfaces with the Datadog API v2 to programmatically manage monitoring infrastructure across your entire stack. It creates metric monitors, log monitors, APM trace monitors, and composite monitors through the /api/v2/monitors endpoint with proper query syntax and evaluation parameters. The agent uses the DogStatsD protocol to submit custom business metrics from application code, automatically generating corresponding monitors with appropriate thresholds. Dashboard definitions are managed as code using the Datadog dashboard API, supporting template variables and widget configurations for team-specific views. Integration with the Datadog Terraform provider enables version-controlled monitor management through HCL definitions. The engine includes anomaly detection monitor setup using the Datadog machine learning algorithms, configuring sensitivity levels and alert recovery conditions based on historical metric behavior."
source: "https://github.com/DataDog/dd-trace-js"
verification: "security_reviewed"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  npm_package: "dd-trace"
---

# Datadog Monitor Configuration Engine

The Datadog Monitor Configuration Engine interfaces with the Datadog API v2 to programmatically manage monitoring infrastructure across your entire stack. It creates metric monitors, log monitors, APM trace monitors, and composite monitors through the /api/v2/monitors endpoint with proper query syntax and evaluation parameters. The agent uses the DogStatsD protocol to submit custom business metrics from application code, automatically generating corresponding monitors with appropriate thresholds. Dashboard definitions are managed as code using the Datadog dashboard API, supporting template variables and widget configurations for team-specific views. Integration with the Datadog Terraform provider enables version-controlled monitor management through HCL definitions. The engine includes anomaly detection monitor setup using the Datadog machine learning algorithms, configuring sensitivity levels and alert recovery conditions based on historical metric behavior.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-monitor-configuration-engine/)
