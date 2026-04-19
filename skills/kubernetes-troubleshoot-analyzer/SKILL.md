---
title: "Kubernetes Troubleshoot Analyzer"
description: "The Kubernetes Troubleshoot Analyzer performs comprehensive cluster diagnostics using multiple data sources and analysis frameworks. It leverages kubectl commands for real-time cluster state inspection, parsing pod events, node conditions, and resource quota utilization to identify root causes of deployment failures. The skill uses the Troubleshoot.sh support-bundle collector specification to gather cluster-wide diagnostics including pod logs, node resources, cluster resources, and custom collectors for application-specific health checks. Analyzers are configured to detect common failure patterns like ImagePullBackOff with registry authentication issues, CrashLoopBackOff with OOM analysis, and Pending pods with scheduler constraint violations. Advanced diagnostics include network policy analysis using Cilium or Calico CNI-specific commands, PersistentVolumeClaim binding failures with storage class provisioner debugging, and Ingress controller configuration validation for NGINX and Istio. The analyzer generates prioritized remediation runbooks with kubectl commands, Helm value corrections, and resource manifest patches for each identified issue."
source: "https://github.com/kubernetes/kubernetes"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Troubleshoot Analyzer

The Kubernetes Troubleshoot Analyzer performs comprehensive cluster diagnostics using multiple data sources and analysis frameworks. It leverages kubectl commands for real-time cluster state inspection, parsing pod events, node conditions, and resource quota utilization to identify root causes of deployment failures. The skill uses the Troubleshoot.sh support-bundle collector specification to gather cluster-wide diagnostics including pod logs, node resources, cluster resources, and custom collectors for application-specific health checks. Analyzers are configured to detect common failure patterns like ImagePullBackOff with registry authentication issues, CrashLoopBackOff with OOM analysis, and Pending pods with scheduler constraint violations. Advanced diagnostics include network policy analysis using Cilium or Calico CNI-specific commands, PersistentVolumeClaim binding failures with storage class provisioner debugging, and Ingress controller configuration validation for NGINX and Istio. The analyzer generates prioritized remediation runbooks with kubectl commands, Helm value corrections, and resource manifest patches for each identified issue.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-troubleshoot-analyzer/)
