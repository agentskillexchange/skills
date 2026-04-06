---
name: Grafana Dashboard JSON Assembler
description: Assembles Grafana dashboard JSON models using panel types like timeseries,
  stat, table, and heatmap. Configures datasource references, template variables,
  and annotation queries for operational dashboards.
category: "Monitoring &amp; Alerts"
framework: Cursor
verification: security_reviewed
source: "https://agentskillexchange.com/skills/grafana-dashboard-json-assembler/"
---
# Grafana Dashboard JSON Assembler

Assembles Grafana dashboard JSON models using panel types like timeseries, stat, table, and heatmap. Configures datasource references, template variables, and annotation queries for operational dashboards.

The Grafana Dashboard JSON Assembler constructs complete dashboard models following the Grafana JSON schema specification. It generates panel configurations for all major visualization types including timeseries with multiple y-axes, stat panels with value mappings and thresholds, table panels with field overrides and column filtering, and heatmap panels with bucket aggregation. The skill handles datasource provisioning references using UID-based selectors compatible with Grafana provisioning workflows. Template variables are configured with proper query types—label_values for Prometheus, tag queries for InfluxDB, and dimension values for CloudWatch. Row-based layouts use gridPos calculations for responsive panel positioning. Annotation queries overlay deployment events and alert state changes on time-series panels. The assembler supports library panel references for reusable components, dashboard links for drill-down navigation, and JSON-based provisioning compatible with Kubernetes ConfigMap mounting.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill grafana-dashboard-json-assembler
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill grafana-dashboard-json-assembler -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill grafana-dashboard-json-assembler -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill grafana-dashboard-json-assembler -a codex
```

### OpenClaw

```bash
clawhub install grafana-dashboard-json-assembler
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-dashboard-json-assembler/)
