---
name: "Grafana Dashboard Snapshot Exporter"
description: "Exports Grafana dashboards as shareable snapshots using the Grafana HTTP API /api/snapshots endpoint. Captures panel data at point-in-time with configurable expiration and external sharing via snapshot keys."
category: "Monitoring & Alerts"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/grafana-dashboard-snapshot-exporter/"
tool_ecosystem:
  tool: "grafana"
  github_stars: 72796
  github_repo: "grafana/grafana"
  license: "AGPL-3.0"
  maintained: true
---

# Grafana Dashboard Snapshot Exporter

Exports Grafana dashboards as shareable snapshots using the Grafana HTTP API /api/snapshots endpoint. Captures panel data at point-in-time with configurable expiration and external sharing via snapshot keys.

## Overview

The Grafana Dashboard Snapshot Exporter creates point-in-time snapshots of Grafana dashboards for sharing and archival purposes. Using the Grafana HTTP API POST /api/snapshots endpoint, it captures the complete dashboard JSON model along with rendered panel data. The skill first retrieves the dashboard definition via GET /api/dashboards/uid/{uid}, then queries each panel’s datasource to embed actual metric values into the snapshot. For Prometheus datasources, it executes queries via the Grafana proxy endpoint /api/datasources/proxy/{id}/api/v1/query to capture current metric values. Time range configuration supports absolute ranges for historical snapshots or relative ranges for recurring export schedules. Snapshots are created with configurable expiration via the expires field (seconds until auto-deletion) and external sharing controls. The exporter generates shareable URLs using the returned snapshot key and supports both internal (organization-only) and external (public URL) sharing modes. Batch export processes multiple dashboards by folder via the /api/search endpoint with folderIds filter. Each snapshot includes dashboard variables resolved to their current values, annotation markers, and alert state indicators. Integration with cloud storage (S3, GCS) provides long-term snapshot archival beyond Grafana’s built-in retention.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill grafana-dashboard-snapshot-exporter
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill grafana-dashboard-snapshot-exporter -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill grafana-dashboard-snapshot-exporter -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill grafana-dashboard-snapshot-exporter -a codex
```

### OpenClaw

```bash
clawhub install grafana-dashboard-snapshot-exporter
```

## Source

- Marketplace: https://agentskillexchange.com/skills/grafana-dashboard-snapshot-exporter/
