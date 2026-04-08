---
title: Polaris Kubernetes Best Practices Validator
description: 'The Polaris Kubernetes Best Practices Validator skill uses Fairwinds
  Polaris , an open-source policy engine that validates and remediates Kubernetes
  resource configurations. Polaris ships with over 30 built-in policies covering security,
  reliability, and efficiency concerns, plus support for custom policies defined in
  JSON Schema. Polaris operates in three modes. As a command-line tool, it scans local
  YAML files and Helm charts during CI/CD, catching misconfigurations before they
  merge into the main branch. As a dashboard, it provides a cluster-wide audit with
  a scored overview of every workload, highlighting which deployments, statefulsets,
  and jobs violate which policies. As a validating (or mutating) webhook, it intercepts
  kubectl apply requests and rejects or automatically fixes resources that fail danger-level
  checks in real time. Built-in checks cover critical Kubernetes hygiene: containers
  running as root, missing resource requests and limits, privilege escalation enabled,
  host network or PID namespace access, missing readiness and liveness probes, pull
  policy not set to Always, and many more. Each check has a configurable severity
  level (ignore, warning, danger) and can be customized or overridden per-namespace
  or per-controller via annotations or a central configuration file. The CLI produces
  output in JSON, YAML, pretty-printed table, or score-only formats. Exit codes reflect
  the audit result, making it easy to gate pull requests or deployments on passing
  all danger-level checks. Helm chart scanning works by rendering templates locally
  and validating the resulting manifests, which catches issues that only appear with
  specific values overrides. Polaris is written in Go, licensed under Apache 2.0,
  and maintained by Fairwinds with over 3,200 GitHub stars. It integrates with the
  broader Fairwinds ecosystem including Goldilocks (right-sizing recommendations),
  Pluto (deprecated API detection), and Nova (Helm chart update checking). For teams
  managing Kubernetes clusters, this skill enforces configuration standards programmatically
  rather than relying on manual review.'
verification: security_reviewed
source: https://github.com/FairwindsOps/polaris
category:
- Code Quality &amp; Review
framework:
- Codex
tool_ecosystem:
  github_repo: FairwindsOps/polaris
  github_stars: 3355
---

# Polaris Kubernetes Best Practices Validator

The Polaris Kubernetes Best Practices Validator skill uses Fairwinds Polaris , an open-source policy engine that validates and remediates Kubernetes resource configurations. Polaris ships with over 30 built-in policies covering security, reliability, and efficiency concerns, plus support for custom policies defined in JSON Schema. Polaris operates in three modes. As a command-line tool, it scans local YAML files and Helm charts during CI/CD, catching misconfigurations before they merge into the main branch. As a dashboard, it provides a cluster-wide audit with a scored overview of every workload, highlighting which deployments, statefulsets, and jobs violate which policies. As a validating (or mutating) webhook, it intercepts kubectl apply requests and rejects or automatically fixes resources that fail danger-level checks in real time. Built-in checks cover critical Kubernetes hygiene: containers running as root, missing resource requests and limits, privilege escalation enabled, host network or PID namespace access, missing readiness and liveness probes, pull policy not set to Always, and many more. Each check has a configurable severity level (ignore, warning, danger) and can be customized or overridden per-namespace or per-controller via annotations or a central configuration file. The CLI produces output in JSON, YAML, pretty-printed table, or score-only formats. Exit codes reflect the audit result, making it easy to gate pull requests or deployments on passing all danger-level checks. Helm chart scanning works by rendering templates locally and validating the resulting manifests, which catches issues that only appear with specific values overrides. Polaris is written in Go, licensed under Apache 2.0, and maintained by Fairwinds with over 3,200 GitHub stars. It integrates with the broader Fairwinds ecosystem including Goldilocks (right-sizing recommendations), Pluto (deprecated API detection), and Nova (Helm chart update checking). For teams managing Kubernetes clusters, this skill enforces configuration standards programmatically rather than relying on manual review.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/polaris-kubernetes-best-practices-validator/)
