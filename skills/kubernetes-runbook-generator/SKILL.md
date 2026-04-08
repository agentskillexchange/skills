---
title: Kubernetes Runbook Generator
description: The Kubernetes Runbook Generator skill automatically creates operational
  runbooks by analyzing your Kubernetes cluster configuration and historical incident
  data. It connects via the Kubernetes API server using kubeconfig credentials to
  inspect deployments, services, and pod specifications. The skill catalogs common
  failure patterns including CrashLoopBackOff, OOMKilled, ImagePullBackOff, and pending
  pod scheduling issues. For each pattern, it generates step-by-step diagnostic procedures
  using kubectl commands tailored to your specific namespace and resource names. Using
  the Kubernetes Events API, the skill correlates recent cluster events with known
  remediation procedures. It integrates with Prometheus via PromQL queries to include
  relevant metric checks in each runbook step, such as memory usage thresholds and
  CPU throttling indicators. Runbooks are output in Markdown format compatible with
  Confluence, Notion, and GitBook. The skill supports custom templates and can incorporate
  organization-specific escalation procedures and contact information.
verification: security_reviewed
source: https://agentskillexchange.com/skills/kubernetes-runbook-generator/
category:
- Runbooks &amp; Diagnostics
framework:
- OpenClaw
---

# Kubernetes Runbook Generator

The Kubernetes Runbook Generator skill automatically creates operational runbooks by analyzing your Kubernetes cluster configuration and historical incident data. It connects via the Kubernetes API server using kubeconfig credentials to inspect deployments, services, and pod specifications. The skill catalogs common failure patterns including CrashLoopBackOff, OOMKilled, ImagePullBackOff, and pending pod scheduling issues. For each pattern, it generates step-by-step diagnostic procedures using kubectl commands tailored to your specific namespace and resource names. Using the Kubernetes Events API, the skill correlates recent cluster events with known remediation procedures. It integrates with Prometheus via PromQL queries to include relevant metric checks in each runbook step, such as memory usage thresholds and CPU throttling indicators. Runbooks are output in Markdown format compatible with Confluence, Notion, and GitBook. The skill supports custom templates and can incorporate organization-specific escalation procedures and contact information.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-runbook-generator/)
