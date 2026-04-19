---
title: "Kubernetes Runbook Generator"
description: "The Kubernetes Runbook Generator skill automatically creates operational runbooks by analyzing your Kubernetes cluster configuration and historical incident data. It connects via the Kubernetes API server using kubeconfig credentials to inspect deployments, services, and pod specifications. The skill catalogs common failure patterns including CrashLoopBackOff, OOMKilled, ImagePullBackOff, and pending pod scheduling issues. For each pattern, it generates step-by-step diagnostic procedures using kubectl commands tailored to your specific namespace and resource names. Using the Kubernetes Events API, the skill correlates recent cluster events with known remediation procedures. It integrates with Prometheus via PromQL queries to include relevant metric checks in each runbook step, such as memory usage thresholds and CPU throttling indicators. Runbooks are output in Markdown format compatible with Confluence, Notion, and GitBook. The skill supports custom templates and can incorporate organization-specific escalation procedures and contact information."
source: "https://github.com/kubernetes/kubernetes"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Runbook Generator

The Kubernetes Runbook Generator skill automatically creates operational runbooks by analyzing your Kubernetes cluster configuration and historical incident data. It connects via the Kubernetes API server using kubeconfig credentials to inspect deployments, services, and pod specifications. The skill catalogs common failure patterns including CrashLoopBackOff, OOMKilled, ImagePullBackOff, and pending pod scheduling issues. For each pattern, it generates step-by-step diagnostic procedures using kubectl commands tailored to your specific namespace and resource names. Using the Kubernetes Events API, the skill correlates recent cluster events with known remediation procedures. It integrates with Prometheus via PromQL queries to include relevant metric checks in each runbook step, such as memory usage thresholds and CPU throttling indicators. Runbooks are output in Markdown format compatible with Confluence, Notion, and GitBook. The skill supports custom templates and can incorporate organization-specific escalation procedures and contact information.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-runbook-generator/)
