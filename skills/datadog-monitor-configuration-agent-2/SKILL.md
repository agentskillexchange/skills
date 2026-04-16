---
title: "Datadog Monitor Configuration Agent"
description: "Creates and manages Datadog monitors using the datadog-api-client SDK. Configures metric, log, APM trace, and composite monitors with proper threshold types and notification routing."
verification: "security_reviewed"
source: "https://github.com/DataDog/dd-trace-js"
category:
  - "Monitoring & Alerts"
framework:
  - "Claude Agents"
---

# Datadog Monitor Configuration Agent

The Datadog Monitor Configuration Agent automates monitor lifecycle management through the datadog-api-client Python SDK. It creates metric monitors with correct threshold conditions (above, below, above-or-equal) and recovery thresholds that prevent flapping. The skill handles log monitors with proper query syntax including facet filters, pattern matching, and log pipeline processing awareness. For APM monitors, it constructs trace analytics queries targeting specific service/resource combinations with percentile-based latency thresholds. Composite monitors are built using boolean algebra across existing monitor IDs with correct operator precedence. The agent configures notification channels using @-mention syntax for Slack channels, PagerDuty services, and webhook endpoints. It manages monitor downtimes for maintenance windows, supports tag-based monitor scoping across environments, and generates Terraform datadog_monitor resources for infrastructure-as-code workflows.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-monitor-configuration-agent-2/)
