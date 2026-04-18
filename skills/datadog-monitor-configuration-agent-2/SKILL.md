---
title: "Datadog Monitor Configuration Agent"
description: "Creates and manages Datadog monitors using the datadog-api-client SDK. Configures metric, log, APM trace, and composite monitors with proper threshold types and notification routing."
verification: security_reviewed
source: "https://github.com/DataDog/dd-trace-js"
category:
  - "Monitoring & Alerts"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "datadog/dd-trace-js"
  github_stars: 791
  ase_npm_package: "dd-trace"
  npm_weekly_downloads: 6596660
---

# Datadog Monitor Configuration Agent

The Datadog Monitor Configuration Agent automates monitor lifecycle management through the datadog-api-client Python SDK. It creates metric monitors with correct threshold conditions (above, below, above-or-equal) and recovery thresholds that prevent flapping. The skill handles log monitors with proper query syntax including facet filters, pattern matching, and log pipeline processing awareness. For APM monitors, it constructs trace analytics queries targeting specific service/resource combinations with percentile-based latency thresholds. Composite monitors are built using boolean algebra across existing monitor IDs with correct operator precedence. The agent configures notification channels using @-mention syntax for Slack channels, PagerDuty services, and webhook endpoints. It manages monitor downtimes for maintenance windows, supports tag-based monitor scoping across environments, and generates Terraform datadog_monitor resources for infrastructure-as-code workflows.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/datadog-monitor-configuration-agent-2
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/datadog-monitor-configuration-agent-2` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-monitor-configuration-agent-2/)
