---
title: Prometheus Alert Runbook Linker
description: 'Prometheus Alert Runbook Linker ensures every alerting rule in your
  monitoring stack has an associated operational runbook for incident responders.
  How It Works The skill scans Prometheus alerting rules (both file-based and PrometheusRule
  CRDs in Kubernetes) for runbook_url annotations. It validates that linked runbooks
  are accessible, contain relevant content, and follows a consistent format. Key Features
  Scans prometheus.yml alert rules and Kubernetes PrometheusRule custom resources
  Validates runbook_url annotation presence and HTTP reachability for every alert
  Generates stub runbook templates for alerts missing documentation Cross-references
  alert labels with runbook metadata to detect mislinked documentation Templates Generated
  runbooks follow the SRE runbook format: Summary, Impact, Diagnosis Steps, Remediation
  Steps, and Escalation Path. Supports output to Confluence, GitBook, and Markdown
  in git repositories. Integrates with Grafana OnCall for runbook attachment.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/prometheus-alert-runbook-linker/
category:
- Runbooks &amp; Diagnostics
framework:
- Gemini
---

# Prometheus Alert Runbook Linker

Prometheus Alert Runbook Linker ensures every alerting rule in your monitoring stack has an associated operational runbook for incident responders. How It Works The skill scans Prometheus alerting rules (both file-based and PrometheusRule CRDs in Kubernetes) for runbook_url annotations. It validates that linked runbooks are accessible, contain relevant content, and follows a consistent format. Key Features Scans prometheus.yml alert rules and Kubernetes PrometheusRule custom resources Validates runbook_url annotation presence and HTTP reachability for every alert Generates stub runbook templates for alerts missing documentation Cross-references alert labels with runbook metadata to detect mislinked documentation Templates Generated runbooks follow the SRE runbook format: Summary, Impact, Diagnosis Steps, Remediation Steps, and Escalation Path. Supports output to Confluence, GitBook, and Markdown in git repositories. Integrates with Grafana OnCall for runbook attachment.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-runbook-linker/)
