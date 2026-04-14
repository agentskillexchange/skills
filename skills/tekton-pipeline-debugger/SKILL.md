---
title: "Tekton Pipeline Debugger"
description: "Debugs Tekton pipeline failures by querying TaskRun and PipelineRun status via kubectl and the Tekton Results API. Extracts step container logs, identifies parameter resolution errors, and suggests workspace volume fixes."
verification: security_reviewed
source: "https://github.com/tektoncd/pipeline"
category:
  - "CI/CD Integrations"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "tektoncd/pipeline"
  github_stars: 8936
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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tekton-pipeline-debugger/)
