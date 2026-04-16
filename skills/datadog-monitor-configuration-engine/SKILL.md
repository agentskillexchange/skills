---
title: "Datadog Monitor Configuration Engine"
description: "Interfaces with the Datadog API v2 monitors and dashboards endpoints to programmatically create and manage monitors. Uses DogStatsD protocol for custom metric submission and Datadog Terraform provider for IaC."
verification: "security_reviewed"
source: "https://github.com/DataDog/dd-trace-js"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "ChatGPT Agents"
---

# Datadog Monitor Configuration Engine

The Datadog Monitor Configuration Engine interfaces with the Datadog API v2 to programmatically manage monitoring infrastructure across your entire stack. It creates metric monitors, log monitors, APM trace monitors, and composite monitors through the /api/v2/monitors endpoint with proper query syntax and evaluation parameters. The agent uses the DogStatsD protocol to submit custom business metrics from application code, automatically generating corresponding monitors with appropriate thresholds. Dashboard definitions are managed as code using the Datadog dashboard API, supporting template variables and widget configurations for team-specific views. Integration with the Datadog Terraform provider enables version-controlled monitor management through HCL definitions. The engine includes anomaly detection monitor setup using the Datadog machine learning algorithms, configuring sensitivity levels and alert recovery conditions based on historical metric behavior.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-monitor-configuration-engine/)
