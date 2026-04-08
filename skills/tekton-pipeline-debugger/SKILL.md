---
title: Tekton Pipeline Debugger
description: Tekton Pipeline Debugger provides intelligent troubleshooting for failed
  Tekton CI/CD pipelines running on Kubernetes. How It Works The skill queries Kubernetes
  for PipelineRun and TaskRun resources, extracting status conditions, step container
  logs, and event histories. It correlates failures across pipeline stages to identify
  root causes, from parameter resolution errors to workspace volume mount issues.
  Key Features Automatic extraction of step container logs from failed TaskRuns using
  kubectl logs with container selection Parameter resolution debugging for unbound
  params, missing defaults, and type mismatches Workspace volume troubleshooting for
  PVC binding failures, access mode conflicts, and storage class issues Integration
  with Tekton Results API for historical failure pattern analysis Diagnostics Supports
  Tekton Pipelines v0.50+ and Tekton Results v0.7+. Detects common issues like missing
  ServiceAccount permissions, image pull failures, and resource quota exhaustion.
  Generates fix suggestions with kubectl patch commands.
verification: security_reviewed
source: https://agentskillexchange.com/skills/tekton-pipeline-debugger/
category:
- CI/CD Integrations
framework:
- Custom Agents
---

# Tekton Pipeline Debugger

Tekton Pipeline Debugger provides intelligent troubleshooting for failed Tekton CI/CD pipelines running on Kubernetes. How It Works The skill queries Kubernetes for PipelineRun and TaskRun resources, extracting status conditions, step container logs, and event histories. It correlates failures across pipeline stages to identify root causes, from parameter resolution errors to workspace volume mount issues. Key Features Automatic extraction of step container logs from failed TaskRuns using kubectl logs with container selection Parameter resolution debugging for unbound params, missing defaults, and type mismatches Workspace volume troubleshooting for PVC binding failures, access mode conflicts, and storage class issues Integration with Tekton Results API for historical failure pattern analysis Diagnostics Supports Tekton Pipelines v0.50+ and Tekton Results v0.7+. Detects common issues like missing ServiceAccount permissions, image pull failures, and resource quota exhaustion. Generates fix suggestions with kubectl patch commands.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tekton-pipeline-debugger/)
