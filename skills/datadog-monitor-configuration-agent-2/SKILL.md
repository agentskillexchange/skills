---
title: "Datadog Monitor Configuration Agent"
description: "The Datadog Monitor Configuration Agent automates monitor lifecycle management through the datadog-api-client Python SDK. It creates metric monitors with correct threshold conditions (above, below, above-or-equal) and recovery thresholds that prevent flapping. The skill handles log monitors with proper query syntax including facet filters, pattern matching, and log pipeline processing awareness. For APM monitors, it constructs trace analytics queries targeting specific service/resource combinations with percentile-based latency thresholds. Composite monitors are built using boolean algebra across existing monitor IDs with correct operator precedence. The agent configures notification channels using @-mention syntax for Slack channels, PagerDuty services, and webhook endpoints. It manages monitor downtimes for maintenance windows, supports tag-based monitor scoping across environments, and generates Terraform datadog_monitor resources for infrastructure-as-code workflows."
source: "https://github.com/DataDog/dd-trace-js"
verification: "security_reviewed"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "datadog/dd-trace-js"
  github_stars: 791
  npm_package: "dd-trace"
  npm_weekly_downloads: 6596660
---

# Datadog Monitor Configuration Agent

The Datadog Monitor Configuration Agent automates monitor lifecycle management through the datadog-api-client Python SDK. It creates metric monitors with correct threshold conditions (above, below, above-or-equal) and recovery thresholds that prevent flapping. The skill handles log monitors with proper query syntax including facet filters, pattern matching, and log pipeline processing awareness. For APM monitors, it constructs trace analytics queries targeting specific service/resource combinations with percentile-based latency thresholds. Composite monitors are built using boolean algebra across existing monitor IDs with correct operator precedence. The agent configures notification channels using @-mention syntax for Slack channels, PagerDuty services, and webhook endpoints. It manages monitor downtimes for maintenance windows, supports tag-based monitor scoping across environments, and generates Terraform datadog_monitor resources for infrastructure-as-code workflows.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-monitor-configuration-agent-2/)
