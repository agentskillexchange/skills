---
name: "Pod CrashLoop Runbook"
description: "Kubernetes-specific runbook for diagnosing and resolving CrashLoopBackOff pod states. Systematic approach to identify root cause across configuration, resource limits, health checks, and application errors."
category: "Runbooks & Diagnostics"
framework: "Custom Agents"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/pod-crashloop-runbook/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "kubernetes"  # from ase_tool_match
  github_stars: 121313  # from ase_github_stars (integer, not string)
  github_repo: "kubernetes/kubernetes"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Pod CrashLoop Runbook

Kubernetes-specific runbook for diagnosing and resolving CrashLoopBackOff pod states. Systematic approach to identify root cause across configuration, resource limits, health checks, and application errors.

## Overview

Kubernetes-specific runbook for diagnosing and resolving CrashLoopBackOff pod states. Systematic approach to identify root cause across configuration, resource limits, health checks, and application errors.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill pod-crashloop-runbook
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pod-crashloop-runbook -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pod-crashloop-runbook -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pod-crashloop-runbook -a codex
```

### OpenClaw

```bash
clawhub install pod-crashloop-runbook
```

## Source

- Marketplace: https://agentskillexchange.com/skills/pod-crashloop-runbook/
