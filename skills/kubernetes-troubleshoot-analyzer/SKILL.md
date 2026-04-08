---
title: Kubernetes Troubleshoot Analyzer
description: The Kubernetes Troubleshoot Analyzer performs comprehensive cluster diagnostics
  using multiple data sources and analysis frameworks. It leverages kubectl commands
  for real-time cluster state inspection, parsing pod events, node conditions, and
  resource quota utilization to identify root causes of deployment failures. The skill
  uses the Troubleshoot.sh support-bundle collector specification to gather cluster-wide
  diagnostics including pod logs, node resources, cluster resources, and custom collectors
  for application-specific health checks. Analyzers are configured to detect common
  failure patterns like ImagePullBackOff with registry authentication issues, CrashLoopBackOff
  with OOM analysis, and Pending pods with scheduler constraint violations. Advanced
  diagnostics include network policy analysis using Cilium or Calico CNI-specific
  commands, PersistentVolumeClaim binding failures with storage class provisioner
  debugging, and Ingress controller configuration validation for NGINX and Istio.
  The analyzer generates prioritized remediation runbooks with kubectl commands, Helm
  value corrections, and resource manifest patches for each identified issue.
verification: security_reviewed
source: https://agentskillexchange.com/skills/kubernetes-troubleshoot-analyzer/
category:
- Runbooks &amp; Diagnostics
framework:
- ChatGPT Agents
---

# Kubernetes Troubleshoot Analyzer

The Kubernetes Troubleshoot Analyzer performs comprehensive cluster diagnostics using multiple data sources and analysis frameworks. It leverages kubectl commands for real-time cluster state inspection, parsing pod events, node conditions, and resource quota utilization to identify root causes of deployment failures. The skill uses the Troubleshoot.sh support-bundle collector specification to gather cluster-wide diagnostics including pod logs, node resources, cluster resources, and custom collectors for application-specific health checks. Analyzers are configured to detect common failure patterns like ImagePullBackOff with registry authentication issues, CrashLoopBackOff with OOM analysis, and Pending pods with scheduler constraint violations. Advanced diagnostics include network policy analysis using Cilium or Calico CNI-specific commands, PersistentVolumeClaim binding failures with storage class provisioner debugging, and Ingress controller configuration validation for NGINX and Istio. The analyzer generates prioritized remediation runbooks with kubectl commands, Helm value corrections, and resource manifest patches for each identified issue.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-troubleshoot-analyzer/)
