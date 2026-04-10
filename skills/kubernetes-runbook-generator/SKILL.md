---
name: Kubernetes Runbook Generator
description: Auto-generates operational runbooks from Kubernetes cluster state using
  kubectl and the Kubernetes API. Produces step-by-step troubleshooting guides for
  common pod failure modes.
verification: security_reviewed
source: https://agentskillexchange.com/skills/kubernetes-runbook-generator/
category:
- Runbooks &amp; Diagnostics
framework:
- OpenClaw
---
# Kubernetes Runbook Generator

The Kubernetes Runbook Generator skill automatically creates operational runbooks by analyzing your Kubernetes cluster configuration and historical incident data. It connects via the Kubernetes API server using kubeconfig credentials to inspect deployments, services, and pod specifications.
The skill catalogs common failure patterns including CrashLoopBackOff, OOMKilled, ImagePullBackOff, and pending pod scheduling issues. For each pattern, it generates step-by-step diagnostic procedures using kubectl commands tailored to your specific namespace and resource names.
Using the Kubernetes Events API, the skill correlates recent cluster events with known remediation procedures. It integrates with Prometheus via PromQL queries to include relevant metric checks in each runbook step, such as memory usage thresholds and CPU throttling indicators.
Runbooks are output in Markdown format compatible with Confluence, Notion, and GitBook. The skill supports custom templates and can incorporate organization-specific escalation procedures and contact information.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-runbook-generator/)
