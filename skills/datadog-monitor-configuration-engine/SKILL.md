---
name: "Datadog Monitor Configuration Engine"
description: "Interfaces with the Datadog API v2 monitors and dashboards endpoints to programmatically create and manage monitors. Uses DogStatsD protocol for custom metric submission and Datadog Terraform provider for IaC."
category: "Monitoring & Alerts"
framework: "ChatGPT Agents"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/datadog-monitor-configuration-engine/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "datadog"  # from ase_tool_match
  github_stars: 789  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 6043057  # from ase_npm_downloads
  github_repo: "DataDog/dd-trace-js"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Datadog Monitor Configuration Engine

Interfaces with the Datadog API v2 monitors and dashboards endpoints to programmatically create and manage monitors. Uses DogStatsD protocol for custom metric submission and Datadog Terraform provider for IaC.

## Overview

The Datadog Monitor Configuration Engine interfaces with the Datadog API v2 to programmatically manage monitoring infrastructure across your entire stack. It creates metric monitors, log monitors, APM trace monitors, and composite monitors through the /api/v2/monitors endpoint with proper query syntax and evaluation parameters. The agent uses the DogStatsD protocol to submit custom business metrics from application code, automatically generating corresponding monitors with appropriate thresholds. Dashboard definitions are managed as code using the Datadog dashboard API, supporting template variables and widget configurations for team-specific views. Integration with the Datadog Terraform provider enables version-controlled monitor management through HCL definitions. The engine includes anomaly detection monitor setup using the Datadog machine learning algorithms, configuring sensitivity levels and alert recovery conditions based on historical metric behavior.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill datadog-monitor-configuration-engine
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill datadog-monitor-configuration-engine -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill datadog-monitor-configuration-engine -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill datadog-monitor-configuration-engine -a codex
```

### OpenClaw

```bash
clawhub install datadog-monitor-configuration-engine
```

## Source

- Marketplace: https://agentskillexchange.com/skills/datadog-monitor-configuration-engine/
