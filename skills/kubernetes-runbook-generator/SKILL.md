---
title: "Kubernetes Runbook Generator"
description: "Auto-generates operational runbooks from Kubernetes cluster state using kubectl and the Kubernetes API. Produces step-by-step troubleshooting guides for common pod failure modes."
verification: "security_reviewed"
source: "https://github.com/kubernetes/kubernetes"
category:
  - "Runbooks & Diagnostics"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Runbook Generator

The Kubernetes Runbook Generator skill automatically creates operational runbooks by analyzing your Kubernetes cluster configuration and historical incident data. It connects via the Kubernetes API server using kubeconfig credentials to inspect deployments, services, and pod specifications. The skill catalogs common failure patterns including CrashLoopBackOff, OOMKilled, ImagePullBackOff, and pending pod scheduling issues. For each pattern, it generates step-by-step diagnostic procedures using kubectl commands tailored to your specific namespace and resource names. Using the Kubernetes Events API, the skill correlates recent cluster events with known remediation procedures. It integrates with Prometheus via PromQL queries to include relevant metric checks in each runbook step, such as memory usage thresholds and CPU throttling indicators. Runbooks are output in Markdown format compatible with Confluence, Notion, and GitBook. The skill supports custom templates and can incorporate organization-specific escalation procedures and contact information.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/kubernetes-runbook-generator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/kubernetes-runbook-generator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/kubernetes-runbook-generator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-runbook-generator/)
