---
title: "Grafana Dashboard Snapshot Exporter"
description: "Exports Grafana dashboards as shareable snapshots using the Grafana HTTP API /api/snapshots endpoint. Captures panel data at point-in-time with configurable expiration and external sharing via snapshot keys."
verification: security_reviewed
source: "https://github.com/grafana/grafana"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "grafana/grafana"
  github_stars: 73187
---

# Grafana Dashboard Snapshot Exporter

The Grafana Dashboard Snapshot Exporter creates point-in-time snapshots of Grafana dashboards for sharing and archival purposes. Using the Grafana HTTP API POST /api/snapshots endpoint, it captures the complete dashboard JSON model along with rendered panel data. The skill first retrieves the dashboard definition via GET /api/dashboards/uid/{uid}, then queries each panel’s datasource to embed actual metric values into the snapshot. For Prometheus datasources, it executes queries via the Grafana proxy endpoint /api/datasources/proxy/{id}/api/v1/query to capture current metric values. Time range configuration supports absolute ranges for historical snapshots or relative ranges for recurring export schedules. Snapshots are created with configurable expiration via the expires field (seconds until auto-deletion) and external sharing controls. The exporter generates shareable URLs using the returned snapshot key and supports both internal (organization-only) and external (public URL) sharing modes. Batch export processes multiple dashboards by folder via the /api/search endpoint with folderIds filter. Each snapshot includes dashboard variables resolved to their current values, annotation markers, and alert state indicators. Integration with cloud storage (S3, GCS) provides long-term snapshot archival beyond Grafana’s built-in retention.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-dashboard-snapshot-exporter/)
