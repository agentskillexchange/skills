---
title: "Datadog Monitor Configuration Agent"
description: "Creates and manages Datadog monitors using the datadog-api-client SDK. Configures metric, log, APM trace, and composite monitors with proper threshold types and notification routing."
slug: "datadog-monitor-configuration-agent-2"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/datadog-monitor-configuration-agent-2/"
listed: true
---

# Datadog Monitor Configuration Agent

Creates and manages Datadog monitors using the datadog-api-client SDK. Configures metric, log, APM trace, and composite monitors with proper threshold types and notification routing.

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
clawhub install datadog-monitor-configuration-agent-2
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Datadog Monitor Configuration Agent automates monitor lifecycle management through the datadog-api-client Python SDK. It creates metric monitors with correct threshold conditions (above, below, above-or-equal) and recovery thresholds that prevent flapping. The skill handles log monitors with proper query syntax including facet filters, pattern matching, and log pipeline processing awareness. For APM monitors, it constructs trace analytics queries targeting specific service/resource combinations with percentile-based latency thresholds. Composite monitors are built using boolean algebra across existing monitor IDs with correct operator precedence. The agent configures notification channels using @-mention syntax for Slack channels, PagerDuty services, and webhook endpoints. It manages monitor downtimes for maintenance windows, supports tag-based monitor scoping across environments, and generates Terraform datadog_monitor resources for infrastructure-as-code workflows.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-monitor-configuration-agent-2/)
