---
title: Grafana Dashboard JSON Migrator
description: The Grafana Dashboard JSON Migrator automates the promotion of Grafana
  dashboards across environments (dev, staging, production) using the Grafana HTTP
  API. It exports dashboards as JSON models and transforms datasource references,
  replacing UIDs and names to match the target environment datasource configuration.
  Folder structure mapping handles organizational differences between Grafana instances,
  creating missing folders and preserving permissions. Alert rule migration transforms
  Grafana Alerting (unified alerting) rule groups, updating evaluation intervals,
  notification policies, and contact point references. The skill handles dashboard
  variables (template variables) that reference datasource-specific label values,
  remapping them for the target environment. Library panel references are resolved
  and migrated independently to maintain reusability. Version history comparison between
  source and target identifies drift, showing which panels were modified in each environment.
  The skill supports Grafana Terraform provider resource generation as an alternative
  to API-based migration.
verification: security_reviewed
source: https://agentskillexchange.com/skills/grafana-dashboard-json-migrator/
category:
- Monitoring &amp; Alerts
framework:
- Cursor
---

# Grafana Dashboard JSON Migrator

The Grafana Dashboard JSON Migrator automates the promotion of Grafana dashboards across environments (dev, staging, production) using the Grafana HTTP API. It exports dashboards as JSON models and transforms datasource references, replacing UIDs and names to match the target environment datasource configuration. Folder structure mapping handles organizational differences between Grafana instances, creating missing folders and preserving permissions. Alert rule migration transforms Grafana Alerting (unified alerting) rule groups, updating evaluation intervals, notification policies, and contact point references. The skill handles dashboard variables (template variables) that reference datasource-specific label values, remapping them for the target environment. Library panel references are resolved and migrated independently to maintain reusability. Version history comparison between source and target identifies drift, showing which panels were modified in each environment. The skill supports Grafana Terraform provider resource generation as an alternative to API-based migration.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-dashboard-json-migrator/)
