---
name: "Kubernetes Troubleshoot Analyzer"
description: "Runs diagnostic analysis on Kubernetes clusters using kubectl, k9s terminal UI data, and the Troubleshoot.sh support-bundle collector framework. Generates remediation steps for common pod scheduling, networking, and storage failures."
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/kubernetes-troubleshoot-analyzer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "kubernetes"  # from ase_tool_match
  github_stars: 121313  # from ase_github_stars (integer, not string)
  github_repo: "kubernetes/kubernetes"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Kubernetes Troubleshoot Analyzer

Runs diagnostic analysis on Kubernetes clusters using kubectl, k9s terminal UI data, and the Troubleshoot.sh support-bundle collector framework. Generates remediation steps for common pod scheduling, networking, and storage failures.

## Overview

The Kubernetes Troubleshoot Analyzer performs comprehensive cluster diagnostics using multiple data sources and analysis frameworks. It leverages kubectl commands for real-time cluster state inspection, parsing pod events, node conditions, and resource quota utilization to identify root causes of deployment failures.

The skill uses the Troubleshoot.sh support-bundle collector specification to gather cluster-wide diagnostics including pod logs, node resources, cluster resources, and custom collectors for application-specific health checks. Analyzers are configured to detect common failure patterns like ImagePullBackOff with registry authentication issues, CrashLoopBackOff with OOM analysis, and Pending pods with scheduler constraint violations.

Advanced diagnostics include network policy analysis using Cilium or Calico CNI-specific commands, PersistentVolumeClaim binding failures with storage class provisioner debugging, and Ingress controller configuration validation for NGINX and Istio. The analyzer generates prioritized remediation runbooks with kubectl commands, Helm value corrections, and resource manifest patches for each identified issue.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill kubernetes-troubleshoot-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill kubernetes-troubleshoot-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill kubernetes-troubleshoot-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill kubernetes-troubleshoot-analyzer -a codex
```

### OpenClaw

```bash
clawhub install kubernetes-troubleshoot-analyzer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/kubernetes-troubleshoot-analyzer/
