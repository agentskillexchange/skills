---
name: "Kubernetes Pod Diagnostics"
description: "Diagnoses Kubernetes pod failures using kubectl describe, logs –previous, and the Kubernetes API /api/v1/namespaces/{ns}/events endpoints. Identifies CrashLoopBackOff root causes, OOMKilled memory analysis, and generates remediation steps with resource limit recommendations."
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
verification: security_reviewed
source: "https://github.com/kubernetes/kubernetes"
tool_ecosystem:
  tool: kubernetes
  github_stars: 121334
  github_repo: kubernetes/kubernetes
  license: Apache-2.0
  maintained: true
---
# Kubernetes Pod Diagnostics

Diagnoses Kubernetes pod failures using kubectl describe, logs –previous, and the Kubernetes API /api/v1/namespaces/{ns}/events endpoints. Identifies CrashLoopBackOff root causes, OOMKilled memory analysis, and generates remediation steps with resource limit recommendations.

## Overview

Overview

Diagnoses Kubernetes pod failures using kubectl describe, logs –previous, and the Kubernetes API /api/v1/namespaces/{ns}/events endpoints. Identifies CrashLoopBackOff root causes, OOMKilled memory analysis, and generates remediation steps with resource limit recommendations.

Key Features

Automated detection and reporting with structured output formats for downstream integrations

Configurable thresholds and rule sets that adapt to project-specific requirements and team conventions

Real-time feedback loops integrated into developer workflows for immediate actionable insights

Comprehensive logging and audit trails for compliance tracking and historical trend analysis

How It Works

Kubernetes Pod Diagnostics connects directly to your existing infrastructure through well-documented API endpoints. It authenticates using standard token-based methods (API keys, OAuth tokens, or service account credentials) and operates within your existing permission boundaries. The skill processes incoming data streams, applies configurable analysis rules, and produces structured reports that integrate with notification systems, dashboards, and issue trackers.

Requirements

Valid API credentials with appropriate read/write scopes for the target service

Network access to the relevant API endpoints from the agent runtime environment

Compatible agent framework installed and configured with the necessary SDK dependencies

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-diagnostics-skill
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-diagnostics-skill -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-diagnostics-skill -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-diagnostics-skill -a codex
```

### OpenClaw

```bash
clawhub install kubernetes-pod-diagnostics-skill
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-diagnostics-skill/)
