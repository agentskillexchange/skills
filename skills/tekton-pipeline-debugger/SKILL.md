---
name: Tekton Pipeline Debugger
description: Debugs Tekton pipeline failures by querying TaskRun and PipelineRun status
  via kubectl and the Tekton Results API. Extracts step container logs, identifies
  parameter resolution errors, and suggests workspace volume fixes.
verification: security_reviewed
source: https://agentskillexchange.com/skills/tekton-pipeline-debugger/
category:
- CI/CD Integrations
framework:
- Custom Agents
---
# Tekton Pipeline Debugger

Tekton Pipeline Debugger provides intelligent troubleshooting for failed Tekton CI/CD pipelines running on Kubernetes.
How It Works
The skill queries Kubernetes for PipelineRun and TaskRun resources, extracting status conditions, step container logs, and event histories. It correlates failures across pipeline stages to identify root causes, from parameter resolution errors to workspace volume mount issues.
Key Features

Automatic extraction of step container logs from failed TaskRuns using kubectl logs with container selection
Parameter resolution debugging for unbound params, missing defaults, and type mismatches
Workspace volume troubleshooting for PVC binding failures, access mode conflicts, and storage class issues
Integration with Tekton Results API for historical failure pattern analysis

Diagnostics
Supports Tekton Pipelines v0.50+ and Tekton Results v0.7+. Detects common issues like missing ServiceAccount permissions, image pull failures, and resource quota exhaustion. Generates fix suggestions with kubectl patch commands.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tekton-pipeline-debugger/)
