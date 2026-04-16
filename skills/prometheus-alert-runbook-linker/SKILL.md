---
title: "Prometheus Alert Runbook Linker"
description: "Links Prometheus alerting rules to operational runbooks by parsing AlertManager configurations and PrometheusRule CRDs. Validates runbook_url annotations exist and are reachable, and generates stub runbooks for undocumented alerts."
verification: "security_reviewed"
source: "https://github.com/prometheus/prometheus"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
  license: "Apache-2.0"
---

# Prometheus Alert Runbook Linker

Prometheus Alert Runbook Linker ensures every alerting rule in your monitoring stack has an associated operational runbook for incident responders.

How It Works

The skill scans Prometheus alerting rules (both file-based and PrometheusRule CRDs in Kubernetes) for runbook_url annotations. It validates that linked runbooks are accessible, contain relevant content, and follows a consistent format.

Key Features

Scans prometheus.yml alert rules and Kubernetes PrometheusRule custom resources

Validates runbook_url annotation presence and HTTP reachability for every alert

Generates stub runbook templates for alerts missing documentation

Cross-references alert labels with runbook metadata to detect mislinked documentation

Templates

Generated runbooks follow the SRE runbook format: Summary, Impact, Diagnosis Steps, Remediation Steps, and Escalation Path. Supports output to Confluence, GitBook, and Markdown in git repositories. Integrates with Grafana OnCall for runbook attachment.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-runbook-linker/)
