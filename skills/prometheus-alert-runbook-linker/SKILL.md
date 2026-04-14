---
title: "Prometheus Alert Runbook Linker"
description: "Links Prometheus alerting rules to operational runbooks by parsing AlertManager configurations and PrometheusRule CRDs. Validates runbook_url annotations exist and are reachable, and generates stub runbooks for undocumented alerts."
verification: security_reviewed
source: "https://github.com/prometheus/prometheus"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-runbook-linker/)
