---
title: "Kubernetes Pod Diagnostic Agent"
slug: "kubernetes-pod-diagnostic-agent"
description: "Diagnoses Kubernetes pod failures using kubectl and the Kubernetes API server endpoints. Analyzes CrashLoopBackOff, OOMKilled, and ImagePullBackOff states by querying /api/v1/namespaces/{ns}/pods/{pod}/log and /api/v1/events resources."
verification: security_reviewed
source: "https://github.com/kubernetes/kubernetes"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Pod Diagnostic Agent

Diagnoses Kubernetes pod failures using kubectl and the Kubernetes API server endpoints. Analyzes CrashLoopBackOff, OOMKilled, and ImagePullBackOff states by querying /api/v1/namespaces/{ns}/pods/{pod}/log and /api/v1/events resources.

## Installation

1. Clone this skill into your local skills directory.
2. Review the required tools and environment variables.
3. Install dependencies with your preferred package manager or runtime.
4. Run the upstream install command from the project documentation, if needed.
5. Validate the installation and test the skill in your agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-diagnostic-agent/)
