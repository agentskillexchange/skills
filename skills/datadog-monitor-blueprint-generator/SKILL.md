---
name: Datadog Monitor Blueprint Generator
description: Creates Datadog monitor definitions using the Datadog API v2 with metric,
  log, APM trace, and composite monitor types. Generates Terraform datadog_monitor
  resources with threshold and anomaly detection.
verification: security_reviewed
source: https://agentskillexchange.com/skills/datadog-monitor-blueprint-generator/
category:
- Monitoring &amp; Alerts
framework:
- Cursor
---
# Datadog Monitor Blueprint Generator

The Datadog Monitor Blueprint Generator skill produces comprehensive Datadog monitoring configurations through the Datadog API v2 and Terraform provider. It creates metric monitors with threshold, anomaly (using AGILE, ROBUST, or BASIC algorithms), outlier, and forecast detection methods, log monitors with facet-based query filters and multi-alert group-by dimensions, and APM trace analytics monitors for service latency P99 tracking.
The skill generates Terraform datadog_monitor resources with proper threshold_windows for anomaly monitors, renotify_interval configurations, and escalation_message templates with @-mention routing to team handles. It configures composite monitors using boolean algebra (a && b || !c) for complex alerting logic and produces SLO definitions via datadog_service_level_objective resources with monitor-based and metric-based SLI calculations.
Advanced features include dashboard JSON generation for the Datadog Dashboard API with template variables for environment switching, synthetic test configurations for HTTP and browser tests via datadog_synthetics_test resources, and log pipeline processor definitions for parsing, remapping, and enrichment. The skill also generates Datadog notebook templates for incident investigation runbooks and configures downtime schedules via the Downtimes API v2 for maintenance window management.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-monitor-blueprint-generator/)
