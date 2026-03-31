---
name: "Polaris Kubernetes Best Practices Validator"
description: "Validate Kubernetes resource configurations against best practice policies using Fairwinds Polaris. Runs as a CLI for CI/CD, a dashboard for cluster-wide audits, or a validating webhook for admission control."
category: "Code Quality &amp; Review"
framework: "Codex"
verification: security_reviewed
source: "https://github.com/FairwindsOps/polaris"
---
# Polaris Kubernetes Best Practices Validator

Validate Kubernetes resource configurations against best practice policies using Fairwinds Polaris. Runs as a CLI for CI/CD, a dashboard for cluster-wide audits, or a validating webhook for admission control.

## Overview

The Polaris Kubernetes Best Practices Validator skill uses Fairwinds Polaris, an open-source policy engine that validates and remediates Kubernetes resource configurations. Polaris ships with over 30 built-in policies covering security, reliability, and efficiency concerns, plus support for custom policies defined in JSON Schema.

Polaris operates in three modes. As a command-line tool, it scans local YAML files and Helm charts during CI/CD, catching misconfigurations before they merge into the main branch. As a dashboard, it provides a cluster-wide audit with a scored overview of every workload, highlighting which deployments, statefulsets, and jobs violate which policies. As a validating (or mutating) webhook, it intercepts kubectl apply requests and rejects or automatically fixes resources that fail danger-level checks in real time.

Built-in checks cover critical Kubernetes hygiene: containers running as root, missing resource requests and limits, privilege escalation enabled, host network or PID namespace access, missing readiness and liveness probes, pull policy not set to Always, and many more. Each check has a configurable severity level (ignore, warning, danger) and can be customized or overridden per-namespace or per-controller via annotations or a central configuration file.

The CLI produces output in JSON, YAML, pretty-printed table, or score-only formats. Exit codes reflect the audit result, making it easy to gate pull requests or deployments on passing all danger-level checks. Helm chart scanning works by rendering templates locally and validating the resulting manifests, which catches issues that only appear with specific values overrides.

Polaris is written in Go, licensed under Apache 2.0, and maintained by Fairwinds with over 3,200 GitHub stars. It integrates with the broader Fairwinds ecosystem including Goldilocks (right-sizing recommendations), Pluto (deprecated API detection), and Nova (Helm chart update checking). For teams managing Kubernetes clusters, this skill enforces configuration standards programmatically rather than relying on manual review.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill polaris-kubernetes-best-practices-validator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill polaris-kubernetes-best-practices-validator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill polaris-kubernetes-best-practices-validator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill polaris-kubernetes-best-practices-validator -a codex
```

### OpenClaw

```bash
clawhub install polaris-kubernetes-best-practices-validator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/polaris-kubernetes-best-practices-validator/)
