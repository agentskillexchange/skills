---
title: "Datadog Monitor Blueprint Generator"
description: "The Datadog Monitor Blueprint Generator skill produces comprehensive Datadog monitoring configurations through the Datadog API v2 and Terraform provider. It creates metric monitors with threshold, anomaly (using AGILE, ROBUST, or BASIC algorithms), outlier, and forecast detection methods, log monitors with facet-based query filters and multi-alert group-by dimensions, and APM trace analytics monitors for service latency P99 tracking.\nThe skill generates Terraform datadog_monitor resources with proper threshold_windows for anomaly monitors, renotify_interval configurations, and escalation_message templates with @-mention routing to team handles. It configures composite monitors using boolean algebra (a && b || !c) for complex alerting logic and produces SLO definitions via datadog_service_level_objective resources with monitor-based and metric-based SLI calculations.\nAdvanced features include dashboard JSON generation for the Datadog Dashboard API with template variables for environment switching, synthetic test configurations for HTTP and browser tests via datadog_synthetics_test resources, and log pipeline processor definitions for parsing, remapping, and enrichment. The skill also generates Datadog notebook templates for incident investigation runbooks and configures downtime schedules via the Downtimes API v2 for maintenance window management."
verification: security_reviewed
source: "https://github.com/DataDog/dd-trace-js"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "datadog/dd-trace-js"
  github_stars: 791
  ase_npm_package: "dd-trace"
  npm_weekly_downloads: 6596660
---

# Datadog Monitor Blueprint Generator

The Datadog Monitor Blueprint Generator skill produces comprehensive Datadog monitoring configurations through the Datadog API v2 and Terraform provider. It creates metric monitors with threshold, anomaly (using AGILE, ROBUST, or BASIC algorithms), outlier, and forecast detection methods, log monitors with facet-based query filters and multi-alert group-by dimensions, and APM trace analytics monitors for service latency P99 tracking.
The skill generates Terraform datadog_monitor resources with proper threshold_windows for anomaly monitors, renotify_interval configurations, and escalation_message templates with @-mention routing to team handles. It configures composite monitors using boolean algebra (a && b || !c) for complex alerting logic and produces SLO definitions via datadog_service_level_objective resources with monitor-based and metric-based SLI calculations.
Advanced features include dashboard JSON generation for the Datadog Dashboard API with template variables for environment switching, synthetic test configurations for HTTP and browser tests via datadog_synthetics_test resources, and log pipeline processor definitions for parsing, remapping, and enrichment. The skill also generates Datadog notebook templates for incident investigation runbooks and configures downtime schedules via the Downtimes API v2 for maintenance window management.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/datadog-monitor-blueprint-generator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/datadog-monitor-blueprint-generator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-monitor-blueprint-generator/)
