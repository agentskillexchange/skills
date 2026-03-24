---
name: "Prometheus Alert Rule Generator"
description: "Generates and validates Prometheus alerting rules from natural language descriptions using the Prometheus HTTP API and PromQL query engine. Supports Alertmanager routing configuration and Grafana dashboard annotation."
category: "Monitoring & Alerts"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/prometheus-alert-rule-generator-2/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "prometheus"  # from ase_tool_match
  github_stars: 63278  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 5319832  # from ase_npm_downloads
  github_repo: "prometheus/prometheus"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Prometheus Alert Rule Generator

Generates and validates Prometheus alerting rules from natural language descriptions using the Prometheus HTTP API and PromQL query engine. Supports Alertmanager routing configuration and Grafana dashboard annotation.

## Overview

The Prometheus Alert Rule Generator translates natural language alert descriptions into valid PromQL expressions and Prometheus alerting rule YAML configurations. It queries the Prometheus HTTP API to discover available metrics, labels, and recording rules, then constructs appropriate PromQL expressions with correct aggregation and threshold logic. The agent validates generated rules by executing them against the Prometheus query endpoint to ensure they return expected result types. It also generates corresponding Alertmanager routing configurations with receiver definitions for Slack, email, and webhook targets. Grafana dashboard annotations are automatically created to correlate alert windows with metric visualizations. The tool supports templating for common patterns like SLO-based alerting, rate-of-change detection, and percentile threshold monitoring. Rule files are output in standard Prometheus rule group format ready for deployment via Prometheus Operator or static configuration.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-rule-generator-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-rule-generator-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-rule-generator-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-rule-generator-2 -a codex
```

### OpenClaw

```bash
clawhub install prometheus-alert-rule-generator-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/prometheus-alert-rule-generator-2/
