---
title: "Datadog Monitor Blueprint Generator"
description: "The Datadog Monitor Blueprint Generator skill produces comprehensive Datadog monitoring configurations through the Datadog API v2 and Terraform provider. It creates metric monitors with threshold, anomaly (using AGILE, ROBUST, or BASIC algorithms), outlier, and forecast detection methods, log monitors with facet-based query filters and multi-alert group-by dimensions, and APM trace analytics monitors for service latency P99 tracking. The skill generates Terraform datadog_monitor resources with proper threshold_windows for anomaly monitors, renotify_interval configurations, and escalation_message templates with @-mention routing to team handles. It configures composite monitors using boolean algebra (a &#038;&#038; b || !c) for complex alerting logic and produces SLO definitions via datadog_service_level_objective resources with monitor-based and metric-based SLI calculations. Advanced features include dashboard JSON generation for the Datadog Dashboard API with template variables for environment switching, synthetic test configurations for HTTP and browser tests via datadog_synthetics_test resources, and log pipeline processor definitions for parsing, remapping, and enrichment. The skill also generates Datadog notebook templates for incident investigation runbooks and configures downtime schedules via the Downtimes API v2 for maintenance window management."
source: "https://github.com/DataDog/dd-trace-js"
verification: "security_reviewed"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "datadog/dd-trace-js"
  github_stars: 791
  npm_package: "dd-trace"
  npm_weekly_downloads: 6596660
---

# Datadog Monitor Blueprint Generator

The Datadog Monitor Blueprint Generator skill produces comprehensive Datadog monitoring configurations through the Datadog API v2 and Terraform provider. It creates metric monitors with threshold, anomaly (using AGILE, ROBUST, or BASIC algorithms), outlier, and forecast detection methods, log monitors with facet-based query filters and multi-alert group-by dimensions, and APM trace analytics monitors for service latency P99 tracking. The skill generates Terraform datadog_monitor resources with proper threshold_windows for anomaly monitors, renotify_interval configurations, and escalation_message templates with @-mention routing to team handles. It configures composite monitors using boolean algebra (a &#038;&#038; b || !c) for complex alerting logic and produces SLO definitions via datadog_service_level_objective resources with monitor-based and metric-based SLI calculations. Advanced features include dashboard JSON generation for the Datadog Dashboard API with template variables for environment switching, synthetic test configurations for HTTP and browser tests via datadog_synthetics_test resources, and log pipeline processor definitions for parsing, remapping, and enrichment. The skill also generates Datadog notebook templates for incident investigation runbooks and configures downtime schedules via the Downtimes API v2 for maintenance window management.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-monitor-blueprint-generator/)
