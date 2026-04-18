---
title: "Prometheus Alert Runbook Linker"
description: "Links Prometheus alerting rules to operational runbooks by parsing AlertManager configurations and PrometheusRule CRDs. Validates runbook_url annotations exist and are reachable, and generates stub runbooks for undocumented alerts."
verification: security_reviewed
source: "https://github.com/prometheus/prometheus"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
---

# Prometheus Alert Runbook Linker

Prometheus Alert Runbook Linker ensures every alerting rule in your monitoring stack has an associated operational runbook for incident responders.

How It Works The skill scans Prometheus alerting rules (both file-based and PrometheusRule CRDs in Kubernetes) for runbook_url annotations. It validates that linked runbooks are accessible, contain relevant content, and follows a consistent format.

Key Features

- Scans prometheus.yml alert rules and Kubernetes PrometheusRule custom resources

- Validates runbook_url annotation presence and HTTP reachability for every alert

- Generates stub runbook templates for alerts missing documentation

- Cross-references alert labels with runbook metadata to detect mislinked documentation

Templates Generated runbooks follow the SRE runbook format: Summary, Impact, Diagnosis Steps, Remediation Steps, and Escalation Path. Supports output to Confluence, GitBook, and Markdown in git repositories. Integrates with Grafana OnCall for runbook attachment.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/prometheus-alert-runbook-linker
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/prometheus-alert-runbook-linker` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-runbook-linker/)
