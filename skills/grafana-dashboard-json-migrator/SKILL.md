---
title: "Grafana Dashboard JSON Migrator"
description: "The Grafana Dashboard JSON Migrator automates the promotion of Grafana dashboards across environments (dev, staging, production) using the Grafana HTTP API. It exports dashboards as JSON models and transforms datasource references, replacing UIDs and names to match the target environment datasource configuration. Folder structure mapping handles organizational differences between Grafana instances, creating missing folders and preserving permissions. Alert rule migration transforms Grafana Alerting (unified alerting) rule groups, updating evaluation intervals, notification policies, and contact point references. The skill handles dashboard variables (template variables) that reference datasource-specific label values, remapping them for the target environment. Library panel references are resolved and migrated independently to maintain reusability. Version history comparison between source and target identifies drift, showing which panels were modified in each environment. The skill supports Grafana Terraform provider resource generation as an alternative to API-based migration."
source: "https://github.com/grafana/grafana"
verification: "security_reviewed"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "grafana/grafana"
  github_stars: 73187
---

# Grafana Dashboard JSON Migrator

The Grafana Dashboard JSON Migrator automates the promotion of Grafana dashboards across environments (dev, staging, production) using the Grafana HTTP API. It exports dashboards as JSON models and transforms datasource references, replacing UIDs and names to match the target environment datasource configuration. Folder structure mapping handles organizational differences between Grafana instances, creating missing folders and preserving permissions. Alert rule migration transforms Grafana Alerting (unified alerting) rule groups, updating evaluation intervals, notification policies, and contact point references. The skill handles dashboard variables (template variables) that reference datasource-specific label values, remapping them for the target environment. Library panel references are resolved and migrated independently to maintain reusability. Version history comparison between source and target identifies drift, showing which panels were modified in each environment. The skill supports Grafana Terraform provider resource generation as an alternative to API-based migration.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-dashboard-json-migrator/)
