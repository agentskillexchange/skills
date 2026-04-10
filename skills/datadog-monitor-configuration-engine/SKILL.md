---
name: "Datadog Monitor Configuration Engine"
description: "Interfaces with the Datadog API v2 monitors and dashboards endpoints to programmatically create and manage monitors. Uses DogStatsD protocol for custom metric submission and Datadog Terraform provider for IaC."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/datadog-monitor-configuration-engine/"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "ChatGPT Agents"
---

# Datadog Monitor Configuration Engine

The Datadog Monitor Configuration Engine interfaces with the Datadog API v2 to programmatically manage monitoring infrastructure across your entire stack. It creates metric monitors, log monitors, APM trace monitors, and composite monitors through the /api/v2/monitors endpoint with proper query syntax and evaluation parameters. The agent uses the DogStatsD protocol to submit custom business metrics from application code, automatically generating corresponding monitors with appropriate thresholds. Dashboard definitions are managed as code using the Datadog dashboard API, supporting template variables and widget configurations for team-specific views. Integration with the Datadog Terraform provider enables version-controlled monitor management through HCL definitions. The engine includes anomaly detection monitor setup using the Datadog machine learning algorithms, configuring sensitivity levels and alert recovery conditions based on historical metric behavior.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-monitor-configuration-engine/)
