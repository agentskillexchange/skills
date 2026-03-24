---
name: "Kubernetes Troubleshooting Runbook"
description: "Use this skill to systematically diagnose and resolve Kubernetes issues including pod failures, CrashLoopBackOff errors, OOMKills, and resource constraints. It guides agents through kubectl commands and diagnostic steps to identify root causes. Trigger when Kubernetes workloads are failing, pods are restarting, or cluster resources are being exhausted."
category: "Monitoring & Alerts"
framework: "Custom Agents"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/kubernetes-troubleshooting-runbook/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "kubernetes"  # from ase_tool_match
  github_stars: 121313  # from ase_github_stars (integer, not string)
  github_repo: "kubernetes/kubernetes"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Kubernetes Troubleshooting Runbook

Use this skill to systematically diagnose and resolve Kubernetes issues including pod failures, CrashLoopBackOff errors, OOMKills, and resource constraints. It guides agents through kubectl commands and diagnostic steps to identify root causes. Trigger when Kubernetes workloads are failing, pods are restarting, or cluster resources are being exhausted.

## Overview

Use this skill to systematically diagnose and resolve Kubernetes issues including pod failures, CrashLoopBackOff errors, OOMKills, and resource constraints. It guides agents through kubectl commands and diagnostic steps to identify root causes. Trigger when Kubernetes workloads are failing, pods are restarting, or cluster resources are being exhausted.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill kubernetes-troubleshooting-runbook
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill kubernetes-troubleshooting-runbook -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill kubernetes-troubleshooting-runbook -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill kubernetes-troubleshooting-runbook -a codex
```

### OpenClaw

```bash
clawhub install kubernetes-troubleshooting-runbook
```

## Source

- Marketplace: https://agentskillexchange.com/skills/kubernetes-troubleshooting-runbook/
