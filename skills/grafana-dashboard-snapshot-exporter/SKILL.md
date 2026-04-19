---
title: "Grafana Dashboard Snapshot Exporter"
description: "The Grafana Dashboard Snapshot Exporter creates point-in-time snapshots of Grafana dashboards for sharing and archival purposes. Using the Grafana HTTP API POST /api/snapshots endpoint, it captures the complete dashboard JSON model along with rendered panel data. The skill first retrieves the dashboard definition via GET /api/dashboards/uid/{uid}, then queries each panel&#8217;s datasource to embed actual metric values into the snapshot. For Prometheus datasources, it executes queries via the Grafana proxy endpoint /api/datasources/proxy/{id}/api/v1/query to capture current metric values. Time range configuration supports absolute ranges for historical snapshots or relative ranges for recurring export schedules. Snapshots are created with configurable expiration via the expires field (seconds until auto-deletion) and external sharing controls. The exporter generates shareable URLs using the returned snapshot key and supports both internal (organization-only) and external (public URL) sharing modes. Batch export processes multiple dashboards by folder via the /api/search endpoint with folderIds filter. Each snapshot includes dashboard variables resolved to their current values, annotation markers, and alert state indicators. Integration with cloud storage (S3, GCS) provides long-term snapshot archival beyond Grafana&#8217;s built-in retention."
source: "https://github.com/grafana/grafana"
verification: "security_reviewed"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "grafana/grafana"
  github_stars: 73187
---

# Grafana Dashboard Snapshot Exporter

The Grafana Dashboard Snapshot Exporter creates point-in-time snapshots of Grafana dashboards for sharing and archival purposes. Using the Grafana HTTP API POST /api/snapshots endpoint, it captures the complete dashboard JSON model along with rendered panel data. The skill first retrieves the dashboard definition via GET /api/dashboards/uid/{uid}, then queries each panel&#8217;s datasource to embed actual metric values into the snapshot. For Prometheus datasources, it executes queries via the Grafana proxy endpoint /api/datasources/proxy/{id}/api/v1/query to capture current metric values. Time range configuration supports absolute ranges for historical snapshots or relative ranges for recurring export schedules. Snapshots are created with configurable expiration via the expires field (seconds until auto-deletion) and external sharing controls. The exporter generates shareable URLs using the returned snapshot key and supports both internal (organization-only) and external (public URL) sharing modes. Batch export processes multiple dashboards by folder via the /api/search endpoint with folderIds filter. Each snapshot includes dashboard variables resolved to their current values, annotation markers, and alert state indicators. Integration with cloud storage (S3, GCS) provides long-term snapshot archival beyond Grafana&#8217;s built-in retention.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-dashboard-snapshot-exporter/)
