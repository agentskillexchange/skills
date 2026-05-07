---
title: "Kubernetes Pod Crash Loop Analyzer"
slug: "kubernetes-pod-crash-loop-analyzer"
description: "Diagnoses CrashLoopBackOff pods using kubectl describe, container exit code analysis, and the Kubernetes Events API. Cross-references OOMKilled signals with Prometheus container_memory_rss metrics and cAdvisor stats for root cause identification."
verification: verified
source: "https://github.com/kubernetes/kubernetes"
category: "Runbooks & Diagnostics"
framework: "Cursor"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---
# Kubernetes Pod Crash Loop Analyzer

Diagnoses CrashLoopBackOff pods using kubectl describe, container exit code analysis, and the Kubernetes Events API. Cross-references OOMKilled signals with Prometheus container_memory_rss metrics and cAdvisor stats for root cause identification.

## Installation

1. Clone this skill repository.
2. Open this skill folder.
3. Review prerequisites and setup needs.
4. Install required dependencies.
5. Run and test in your environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-crash-loop-analyzer/)
