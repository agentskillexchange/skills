---
title: Grafana Dashboard Snapshot Exporter
description: The Grafana Dashboard Snapshot Exporter creates point-in-time snapshots
  of Grafana dashboards for sharing and archival purposes. Using the Grafana HTTP
  API POST /api/snapshots endpoint, it captures the complete dashboard JSON model
  along with rendered panel data. The skill first retrieves the dashboard definition
  via GET /api/dashboards/uid/{uid}, then queries each panel’s datasource to embed
  actual metric values into the snapshot. For Prometheus datasources, it executes
  queries via the Grafana proxy endpoint /api/datasources/proxy/{id}/api/v1/query
  to capture current metric values. Time range configuration supports absolute ranges
  for historical snapshots or relative ranges for recurring export schedules. Snapshots
  are created with configurable expiration via the expires field (seconds until auto-deletion)
  and external sharing controls. The exporter generates shareable URLs using the returned
  snapshot key and supports both internal (organization-only) and external (public
  URL) sharing modes. Batch export processes multiple dashboards by folder via the
  /api/search endpoint with folderIds filter. Each snapshot includes dashboard variables
  resolved to their current values, annotation markers, and alert state indicators.
  Integration with cloud storage (S3, GCS) provides long-term snapshot archival beyond
  Grafana’s built-in retention.
verification: security_reviewed
source: https://agentskillexchange.com/skills/grafana-dashboard-snapshot-exporter/
category:
- Monitoring &amp; Alerts
framework:
- Claude Code
---

# Grafana Dashboard Snapshot Exporter

The Grafana Dashboard Snapshot Exporter creates point-in-time snapshots of Grafana dashboards for sharing and archival purposes. Using the Grafana HTTP API POST /api/snapshots endpoint, it captures the complete dashboard JSON model along with rendered panel data. The skill first retrieves the dashboard definition via GET /api/dashboards/uid/{uid}, then queries each panel’s datasource to embed actual metric values into the snapshot. For Prometheus datasources, it executes queries via the Grafana proxy endpoint /api/datasources/proxy/{id}/api/v1/query to capture current metric values. Time range configuration supports absolute ranges for historical snapshots or relative ranges for recurring export schedules. Snapshots are created with configurable expiration via the expires field (seconds until auto-deletion) and external sharing controls. The exporter generates shareable URLs using the returned snapshot key and supports both internal (organization-only) and external (public URL) sharing modes. Batch export processes multiple dashboards by folder via the /api/search endpoint with folderIds filter. Each snapshot includes dashboard variables resolved to their current values, annotation markers, and alert state indicators. Integration with cloud storage (S3, GCS) provides long-term snapshot archival beyond Grafana’s built-in retention.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-dashboard-snapshot-exporter/)
