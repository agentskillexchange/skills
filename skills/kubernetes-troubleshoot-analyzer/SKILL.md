---
name: "Kubernetes Troubleshoot Analyzer"
description: "Runs diagnostic analysis on Kubernetes clusters using kubectl, k9s terminal UI data, and the Troubleshoot.sh support-bundle collector framework. Generates remediation steps for common pod scheduling, networking, and storage failures."
category: "Runbooks &amp; Diagnostics"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/kubernetes-troubleshoot-analyzer/"
---
# Kubernetes Troubleshoot Analyzer

Runs diagnostic analysis on Kubernetes clusters using kubectl, k9s terminal UI data, and the Troubleshoot.sh support-bundle collector framework. Generates remediation steps for common pod scheduling, networking, and storage failures.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-troubleshoot-analyzer/)
