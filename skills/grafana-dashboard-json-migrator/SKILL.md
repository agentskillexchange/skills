---
name: "Grafana Dashboard JSON Migrator"
description: "Migrates Grafana dashboards between instances using the Grafana HTTP API. Transforms datasource UIDs, folder structures, and alert rule references for cross-environment promotion."
category: "Monitoring & Alerts"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/grafana-dashboard-json-migrator/"
tool_ecosystem:
  tool: "grafana"
  github_stars: 72796
  github_repo: "grafana/grafana"
  license: "AGPL-3.0"
  maintained: true
---

# Grafana Dashboard JSON Migrator

Migrates Grafana dashboards between instances using the Grafana HTTP API. Transforms datasource UIDs, folder structures, and alert rule references for cross-environment promotion.

## Overview

The Grafana Dashboard JSON Migrator automates the promotion of Grafana dashboards across environments (dev, staging, production) using the Grafana HTTP API. It exports dashboards as JSON models and transforms datasource references, replacing UIDs and names to match the target environment datasource configuration. Folder structure mapping handles organizational differences between Grafana instances, creating missing folders and preserving permissions. Alert rule migration transforms Grafana Alerting (unified alerting) rule groups, updating evaluation intervals, notification policies, and contact point references. The skill handles dashboard variables (template variables) that reference datasource-specific label values, remapping them for the target environment. Library panel references are resolved and migrated independently to maintain reusability. Version history comparison between source and target identifies drift, showing which panels were modified in each environment. The skill supports Grafana Terraform provider resource generation as an alternative to API-based migration.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill grafana-dashboard-json-migrator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill grafana-dashboard-json-migrator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill grafana-dashboard-json-migrator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill grafana-dashboard-json-migrator -a codex
```

### OpenClaw

```bash
clawhub install grafana-dashboard-json-migrator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/grafana-dashboard-json-migrator/
