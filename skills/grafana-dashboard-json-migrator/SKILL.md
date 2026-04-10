---
title: "Grafana Dashboard JSON Migrator"
description: "Migrates Grafana dashboards between instances using the Grafana HTTP API. Transforms datasource UIDs, folder structures, and alert rule references for cross-environment promotion."
slug: "grafana-dashboard-json-migrator"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/grafana-dashboard-json-migrator/"
listed: true
---

# Grafana Dashboard JSON Migrator

Migrates Grafana dashboards between instances using the Grafana HTTP API. Transforms datasource UIDs, folder structures, and alert rule references for cross-environment promotion.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install grafana-dashboard-json-migrator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Grafana Dashboard JSON Migrator automates the promotion of Grafana dashboards across environments (dev, staging, production) using the Grafana HTTP API. It exports dashboards as JSON models and transforms datasource references, replacing UIDs and names to match the target environment datasource configuration. Folder structure mapping handles organizational differences between Grafana instances, creating missing folders and preserving permissions. Alert rule migration transforms Grafana Alerting (unified alerting) rule groups, updating evaluation intervals, notification policies, and contact point references. The skill handles dashboard variables (template variables) that reference datasource-specific label values, remapping them for the target environment. Library panel references are resolved and migrated independently to maintain reusability. Version history comparison between source and target identifies drift, showing which panels were modified in each environment. The skill supports Grafana Terraform provider resource generation as an alternative to API-based migration.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-dashboard-json-migrator/)
