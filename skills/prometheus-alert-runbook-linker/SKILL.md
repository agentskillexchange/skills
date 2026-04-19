---
title: "Prometheus Alert Runbook Linker"
description: "Prometheus Alert Runbook Linker ensures every alerting rule in your monitoring stack has an associated operational runbook for incident responders. How It Works The skill scans Prometheus alerting rules (both file-based and PrometheusRule CRDs in Kubernetes) for runbook_url annotations. It validates that linked runbooks are accessible, contain relevant content, and follows a consistent format. Key Features Scans prometheus.yml alert rules and Kubernetes PrometheusRule custom resources Validates runbook_url annotation presence and HTTP reachability for every alert Generates stub runbook templates for alerts missing documentation Cross-references alert labels with runbook metadata to detect mislinked documentation Templates Generated runbooks follow the SRE runbook format: Summary, Impact, Diagnosis Steps, Remediation Steps, and Escalation Path. Supports output to Confluence, GitBook, and Markdown in git repositories. Integrates with Grafana OnCall for runbook attachment."
source: "https://github.com/prometheus/prometheus"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
---

# Prometheus Alert Runbook Linker

Prometheus Alert Runbook Linker ensures every alerting rule in your monitoring stack has an associated operational runbook for incident responders. How It Works The skill scans Prometheus alerting rules (both file-based and PrometheusRule CRDs in Kubernetes) for runbook_url annotations. It validates that linked runbooks are accessible, contain relevant content, and follows a consistent format. Key Features Scans prometheus.yml alert rules and Kubernetes PrometheusRule custom resources Validates runbook_url annotation presence and HTTP reachability for every alert Generates stub runbook templates for alerts missing documentation Cross-references alert labels with runbook metadata to detect mislinked documentation Templates Generated runbooks follow the SRE runbook format: Summary, Impact, Diagnosis Steps, Remediation Steps, and Escalation Path. Supports output to Confluence, GitBook, and Markdown in git repositories. Integrates with Grafana OnCall for runbook attachment.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-runbook-linker/)
