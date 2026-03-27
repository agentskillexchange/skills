---
name: "Datadog Monitor Blueprint Generator"
description: "Creates Datadog monitor definitions using the Datadog API v2 with metric, log, APM trace, and composite monitor types. Generates Terraform datadog_monitor resources with threshold and anomaly detection."
category: "Monitoring & Alerts"
framework: "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/datadog-monitor-blueprint-generator/"
tool_ecosystem:
  tool: datadog
  github_stars: 789
  npm_weekly_downloads: 6043057
  github_repo: DataDog/dd-trace-js
  maintained: true
---

# Datadog Monitor Blueprint Generator

Creates Datadog monitor definitions using the Datadog API v2 with metric, log, APM trace, and composite monitor types. Generates Terraform datadog_monitor resources with threshold and anomaly detection.

## Overview

The Datadog Monitor Blueprint Generator skill produces comprehensive Datadog monitoring configurations through the Datadog API v2 and Terraform provider. It creates metric monitors with threshold, anomaly (using AGILE, ROBUST, or BASIC algorithms), outlier, and forecast detection methods, log monitors with facet-based query filters and multi-alert group-by dimensions, and APM trace analytics monitors for service latency P99 tracking.

The skill generates Terraform datadog_monitor resources with proper threshold_windows for anomaly monitors, renotify_interval configurations, and escalation_message templates with @-mention routing to team handles. It configures composite monitors using boolean algebra (a && b || !c) for complex alerting logic and produces SLO definitions via datadog_service_level_objective resources with monitor-based and metric-based SLI calculations.

Advanced features include dashboard JSON generation for the Datadog Dashboard API with template variables for environment switching, synthetic test configurations for HTTP and browser tests via datadog_synthetics_test resources, and log pipeline processor definitions for parsing, remapping, and enrichment. The skill also generates Datadog notebook templates for incident investigation runbooks and configures downtime schedules via the Downtimes API v2 for maintenance window management.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill datadog-monitor-blueprint-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill datadog-monitor-blueprint-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill datadog-monitor-blueprint-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill datadog-monitor-blueprint-generator -a codex
```

### OpenClaw

```bash
clawhub install datadog-monitor-blueprint-generator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/datadog-monitor-blueprint-generator/
