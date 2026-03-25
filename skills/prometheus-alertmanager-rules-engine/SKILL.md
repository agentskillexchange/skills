---
name: "Prometheus AlertManager Rules Engine"
description: "Generates and validates Prometheus alerting rules and AlertManager routing configurations using the Prometheus HTTP API. Implements alert grouping, inhibition rules, and silence management."
category: "Monitoring & Alerts"
framework: "Custom Agents"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/prometheus-alertmanager-rules-engine/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "prometheus"  # from ase_tool_match
  github_stars: 63289  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 5319832  # from ase_npm_downloads
  github_repo: "prometheus/prometheus"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Prometheus AlertManager Rules Engine

Generates and validates Prometheus alerting rules and AlertManager routing configurations using the Prometheus HTTP API. Implements alert grouping, inhibition rules, and silence management.

## Overview

The Prometheus AlertManager Rules Engine skill creates comprehensive alerting configurations for Prometheus monitoring stacks. It queries the Prometheus HTTP API to analyze existing metric names, label cardinality, and recording rules before generating PromQL alert expressions with appropriate thresholds and for-durations. The skill generates AlertManager routing trees with receiver configurations for Slack, PagerDuty, and email notification channels, implementing proper grouping with group_by labels and group_wait/group_interval timing. It configures inhibition rules to suppress downstream alerts when upstream dependencies are already alerting, manages silence windows through the AlertManager Silence API for planned maintenance, and validates all generated rules using the promtool check rules command syntax. The engine analyzes historical alert firing patterns via the Prometheus Alerts API to recommend threshold adjustments that reduce alert fatigue while maintaining coverage for genuine incidents.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill prometheus-alertmanager-rules-engine
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill prometheus-alertmanager-rules-engine -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill prometheus-alertmanager-rules-engine -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill prometheus-alertmanager-rules-engine -a codex
```

### OpenClaw

```bash
clawhub install prometheus-alertmanager-rules-engine
```

## Source

- Marketplace: https://agentskillexchange.com/skills/prometheus-alertmanager-rules-engine/
