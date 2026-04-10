---
title: "Grafana Dashboard Snapshot Exporter"
description: "Exports Grafana dashboards as shareable snapshots using the Grafana HTTP API /api/snapshots endpoint. Captures panel data at point-in-time with configurable expiration and external sharing via snapshot keys."
slug: "grafana-dashboard-snapshot-exporter"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/grafana-dashboard-snapshot-exporter/"
---

# Grafana Dashboard Snapshot Exporter

Exports Grafana dashboards as shareable snapshots using the Grafana HTTP API /api/snapshots endpoint. Captures panel data at point-in-time with configurable expiration and external sharing via snapshot keys.

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
clawhub install grafana-dashboard-snapshot-exporter
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Grafana Dashboard Snapshot Exporter creates point-in-time snapshots of Grafana dashboards for sharing and archival purposes. Using the Grafana HTTP API POST /api/snapshots endpoint, it captures the complete dashboard JSON model along with rendered panel data. The skill first retrieves the dashboard definition via GET /api/dashboards/uid/{uid}, then queries each panel’s datasource to embed actual metric values into the snapshot. For Prometheus datasources, it executes queries via the Grafana proxy endpoint /api/datasources/proxy/{id}/api/v1/query to capture current metric values. Time range configuration supports absolute ranges for historical snapshots or relative ranges for recurring export schedules. Snapshots are created with configurable expiration via the expires field (seconds until auto-deletion) and external sharing controls. The exporter generates shareable URLs using the returned snapshot key and supports both internal (organization-only) and external (public URL) sharing modes. Batch export processes multiple dashboards by folder via the /api/search endpoint with folderIds filter. Each snapshot includes dashboard variables resolved to their current values, annotation markers, and alert state indicators. Integration with cloud storage (S3, GCS) provides long-term snapshot archival beyond Grafana’s built-in retention.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-dashboard-snapshot-exporter/)
