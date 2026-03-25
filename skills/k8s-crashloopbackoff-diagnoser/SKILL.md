---
name: "Kubernetes CrashLoopBackOff Diagnoser"
description: "Diagnoses CrashLoopBackOff pods using kubectl and the Kubernetes API. Inspects container logs, exit codes, OOMKilled events, and liveness probe configurations to generate actionable remediation steps."
category: "Runbooks & Diagnostics"
framework: "Codex"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/k8s-crashloopbackoff-diagnoser/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "kubernetes"  # from ase_tool_match
  github_stars: 121334  # from ase_github_stars (integer, not string)
  github_repo: "kubernetes/kubernetes"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Kubernetes CrashLoopBackOff Diagnoser

Diagnoses CrashLoopBackOff pods using kubectl and the Kubernetes API. Inspects container logs, exit codes, OOMKilled events, and liveness probe configurations to generate actionable remediation steps.

## Overview

The Kubernetes CrashLoopBackOff Diagnoser skill automates root cause analysis for pods stuck in CrashLoopBackOff state. Using kubectl and direct Kubernetes API calls to the /api/v1/namespaces/{ns}/pods/{pod}/log endpoint, it systematically inspects container logs, exit codes, and pod events to identify the underlying failure.

The diagnosis workflow begins by listing all pods with status.containerStatuses[].state.waiting.reason=CrashLoopBackOff using the Kubernetes List API with field selectors. For each affected pod, it retrieves the last N log lines from each container, checks for OOMKilled termination reasons via the container lastState.terminated.reason field, and inspects liveness and readiness probe configurations.

The skill correlates exit codes with known failure patterns: exit code 137 maps to OOMKilled or SIGKILL, exit code 1 to application errors, and exit code 127 to missing binaries. It also checks resource requests and limits against node allocatable resources, validates environment variable references to ConfigMaps and Secrets, and verifies volume mount paths exist. Output includes a structured diagnosis with confidence levels and specific remediation steps.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill k8s-crashloopbackoff-diagnoser
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill k8s-crashloopbackoff-diagnoser -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill k8s-crashloopbackoff-diagnoser -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill k8s-crashloopbackoff-diagnoser -a codex
```

### OpenClaw

```bash
clawhub install k8s-crashloopbackoff-diagnoser
```

## Source

- Marketplace: https://agentskillexchange.com/skills/k8s-crashloopbackoff-diagnoser/
