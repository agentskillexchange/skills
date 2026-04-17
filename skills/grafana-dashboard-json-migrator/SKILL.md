---
title: "Grafana Dashboard JSON Migrator"
description: "The Grafana Dashboard JSON Migrator automates the promotion of Grafana dashboards across environments (dev, staging, production) using the Grafana HTTP API. It exports dashboards as JSON models and transforms datasource references, replacing UIDs and names to match the target environment datasource configuration. Folder structure mapping handles organizational differences between Grafana instances, creating missing folders and preserving permissions. Alert rule migration transforms Grafana Alerting (unified alerting) rule groups, updating evaluation intervals, notification policies, and contact point references. The skill handles dashboard variables (template variables) that reference datasource-specific label values, remapping them for the target environment. Library panel references are resolved and migrated independently to maintain reusability. Version history comparison between source and target identifies drift, showing which panels were modified in each environment. The skill supports Grafana Terraform provider resource generation as an alternative to API-based migration."
verification: security_reviewed
source: "https://github.com/grafana/grafana"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "grafana/grafana"
  github_stars: 73187
---

# Grafana Dashboard JSON Migrator

The Grafana Dashboard JSON Migrator automates the promotion of Grafana dashboards across environments (dev, staging, production) using the Grafana HTTP API. It exports dashboards as JSON models and transforms datasource references, replacing UIDs and names to match the target environment datasource configuration. Folder structure mapping handles organizational differences between Grafana instances, creating missing folders and preserving permissions. Alert rule migration transforms Grafana Alerting (unified alerting) rule groups, updating evaluation intervals, notification policies, and contact point references. The skill handles dashboard variables (template variables) that reference datasource-specific label values, remapping them for the target environment. Library panel references are resolved and migrated independently to maintain reusability. Version history comparison between source and target identifies drift, showing which panels were modified in each environment. The skill supports Grafana Terraform provider resource generation as an alternative to API-based migration.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/grafana-dashboard-json-migrator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/grafana-dashboard-json-migrator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-dashboard-json-migrator/)
