---
name: "Kubernetes Runbook Generator"
description: "Auto-generates operational runbooks from Kubernetes cluster state using kubectl and the Kubernetes API. Produces step-by-step troubleshooting guides for common pod failure modes."
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/kubernetes-runbook-generator/"
---
# Kubernetes Runbook Generator

Auto-generates operational runbooks from Kubernetes cluster state using kubectl and the Kubernetes API. Produces step-by-step troubleshooting guides for common pod failure modes.

## Overview

The Kubernetes Runbook Generator skill automatically creates operational runbooks by analyzing your Kubernetes cluster configuration and historical incident data. It connects via the Kubernetes API server using kubeconfig credentials to inspect deployments, services, and pod specifications.

The skill catalogs common failure patterns including CrashLoopBackOff, OOMKilled, ImagePullBackOff, and pending pod scheduling issues. For each pattern, it generates step-by-step diagnostic procedures using kubectl commands tailored to your specific namespace and resource names.

Using the Kubernetes Events API, the skill correlates recent cluster events with known remediation procedures. It integrates with Prometheus via PromQL queries to include relevant metric checks in each runbook step, such as memory usage thresholds and CPU throttling indicators.

Runbooks are output in Markdown format compatible with Confluence, Notion, and GitBook. The skill supports custom templates and can incorporate organization-specific escalation procedures and contact information.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill kubernetes-runbook-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill kubernetes-runbook-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill kubernetes-runbook-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill kubernetes-runbook-generator -a codex
```

### OpenClaw

```bash
clawhub install kubernetes-runbook-generator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-runbook-generator/)
