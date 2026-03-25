---
name: "Datadog Monitor Configuration Agent"
description: "Creates and manages Datadog monitors using the datadog-api-client SDK. Configures metric, log, APM trace, and composite monitors with proper threshold types and notification routing."
category: "Monitoring & Alerts"
framework: "Claude Agents"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/datadog-monitor-configuration-agent-2/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "datadog"  # from ase_tool_match
  github_stars: 787  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 6043057  # from ase_npm_downloads
  github_repo: "DataDog/dd-trace-js"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Datadog Monitor Configuration Agent

Creates and manages Datadog monitors using the datadog-api-client SDK. Configures metric, log, APM trace, and composite monitors with proper threshold types and notification routing.

## Overview

The Datadog Monitor Configuration Agent automates monitor lifecycle management through the datadog-api-client Python SDK. It creates metric monitors with correct threshold conditions (above, below, above-or-equal) and recovery thresholds that prevent flapping. The skill handles log monitors with proper query syntax including facet filters, pattern matching, and log pipeline processing awareness. For APM monitors, it constructs trace analytics queries targeting specific service/resource combinations with percentile-based latency thresholds. Composite monitors are built using boolean algebra across existing monitor IDs with correct operator precedence. The agent configures notification channels using @-mention syntax for Slack channels, PagerDuty services, and webhook endpoints. It manages monitor downtimes for maintenance windows, supports tag-based monitor scoping across environments, and generates Terraform datadog_monitor resources for infrastructure-as-code workflows.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill datadog-monitor-configuration-agent-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill datadog-monitor-configuration-agent-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill datadog-monitor-configuration-agent-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill datadog-monitor-configuration-agent-2 -a codex
```

### OpenClaw

```bash
clawhub install datadog-monitor-configuration-agent-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/datadog-monitor-configuration-agent-2/
