---
title: "Datadog Monitor Blueprint Generator"
description: "Creates Datadog monitor definitions using the Datadog API v2 with metric, log, APM trace, and composite monitor types. Generates Terraform datadog_monitor resources with threshold and anomaly detection."
verification: "security_reviewed"
source: "https://github.com/DataDog/dd-trace-js"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Cursor"
---

# Datadog Monitor Blueprint Generator

The Datadog Monitor Blueprint Generator skill produces comprehensive Datadog monitoring configurations through the Datadog API v2 and Terraform provider. It creates metric monitors with threshold, anomaly (using AGILE, ROBUST, or BASIC algorithms), outlier, and forecast detection methods, log monitors with facet-based query filters and multi-alert group-by dimensions, and APM trace analytics monitors for service latency P99 tracking.

The skill generates Terraform datadog_monitor resources with proper threshold_windows for anomaly monitors, renotify_interval configurations, and escalation_message templates with @-mention routing to team handles. It configures composite monitors using boolean algebra (a && b || !c) for complex alerting logic and produces SLO definitions via datadog_service_level_objective resources with monitor-based and metric-based SLI calculations.

Advanced features include dashboard JSON generation for the Datadog Dashboard API with template variables for environment switching, synthetic test configurations for HTTP and browser tests via datadog_synthetics_test resources, and log pipeline processor definitions for parsing, remapping, and enrichment. The skill also generates Datadog notebook templates for incident investigation runbooks and configures downtime schedules via the Downtimes API v2 for maintenance window management.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-monitor-blueprint-generator/)
