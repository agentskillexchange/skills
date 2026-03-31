---
name: "Prometheus Alert Runbook Linker"
description: "Links Prometheus alerting rules to operational runbooks by parsing AlertManager configurations and PrometheusRule CRDs. Validates runbook_url annotations exist and are reachable, and generates stub runbooks for undocumented alerts."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/prometheus-alert-runbook-linker/"
---
# Prometheus Alert Runbook Linker

Links Prometheus alerting rules to operational runbooks by parsing AlertManager configurations and PrometheusRule CRDs. Validates runbook_url annotations exist and are reachable, and generates stub runbooks for undocumented alerts.

## Overview

Prometheus Alert Runbook Linker ensures every alerting rule in your monitoring stack has an associated operational runbook for incident responders.

How It Works

The skill scans Prometheus alerting rules (both file-based and PrometheusRule CRDs in Kubernetes) for runbook_url annotations. It validates that linked runbooks are accessible, contain relevant content, and follows a consistent format.

Key Features

- Scans prometheus.yml alert rules and Kubernetes PrometheusRule custom resources

- Validates runbook_url annotation presence and HTTP reachability for every alert

- Generates stub runbook templates for alerts missing documentation

- Cross-references alert labels with runbook metadata to detect mislinked documentation

Templates

Generated runbooks follow the SRE runbook format: Summary, Impact, Diagnosis Steps, Remediation Steps, and Escalation Path. Supports output to Confluence, GitBook, and Markdown in git repositories. Integrates with Grafana OnCall for runbook attachment.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-runbook-linker
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-runbook-linker -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-runbook-linker -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-runbook-linker -a codex
```

### OpenClaw

```bash
clawhub install prometheus-alert-runbook-linker
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-runbook-linker/)
