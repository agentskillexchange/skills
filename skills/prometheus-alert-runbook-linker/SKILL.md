---
name: Prometheus Alert Runbook Linker
description: Links Prometheus alerting rules to operational runbooks by parsing AlertManager configurations and PrometheusRule CRDs. Validates runbook_url annotations exist and are reachable, and generates stub runbooks for undocumented alerts.
category: Runbooks &amp; Diagnostics
framework: Any Agent
verification: security_reviewed
rating: 4.0
reviews: 82
source: https://agentskillexchange.com/skill/prometheus-alert-runbook-linker/
---

# Prometheus Alert Runbook Linker

Links Prometheus alerting rules to operational runbooks by parsing AlertManager configurations and PrometheusRule CRDs. Validates runbook_url annotations exist and are reachable, and generates stub runbooks for undocumented alerts.

## Overview

Links Prometheus alerting rules to operational runbooks by parsing AlertManager configurations and PrometheusRule CRDs. Validates runbook_url annotations exist and are reachable, and generates stub runbooks for undocumented alerts.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-runbook-linker
```

### OpenClaw

```bash
clawhub install prometheus-alert-runbook-linker
```

### Claude Code

```bash
claude mcp add prometheus-alert-runbook-linker
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/prometheus-alert-runbook-linker/) for detailed installation instructions.

## Verification

- **Status**: security_reviewed
- **Category**: Runbooks &amp; Diagnostics
- **Framework**: Any Agent
- **Rating**: 4.0/5 (82 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/prometheus-alert-runbook-linker/)
