---
title: "Kubernetes Troubleshoot Analyzer"
description: "Runs diagnostic analysis on Kubernetes clusters using kubectl, k9s terminal UI data, and the Troubleshoot.sh support-bundle collector framework. Generates remediation steps for common pod scheduling, networking, and storage failures."
verification: security_reviewed
source: "https://github.com/kubernetes/kubernetes"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Troubleshoot Analyzer

The Kubernetes Troubleshoot Analyzer performs comprehensive cluster diagnostics using multiple data sources and analysis frameworks. It leverages kubectl commands for real-time cluster state inspection, parsing pod events, node conditions, and resource quota utilization to identify root causes of deployment failures.

The skill uses the Troubleshoot.sh support-bundle collector specification to gather cluster-wide diagnostics including pod logs, node resources, cluster resources, and custom collectors for application-specific health checks. Analyzers are configured to detect common failure patterns like ImagePullBackOff with registry authentication issues, CrashLoopBackOff with OOM analysis, and Pending pods with scheduler constraint violations.

Advanced diagnostics include network policy analysis using Cilium or Calico CNI-specific commands, PersistentVolumeClaim binding failures with storage class provisioner debugging, and Ingress controller configuration validation for NGINX and Istio. The analyzer generates prioritized remediation runbooks with kubectl commands, Helm value corrections, and resource manifest patches for each identified issue.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-troubleshoot-analyzer/)
