---
name: "Tekton Pipeline Debugger"
description: "Debugs Tekton pipeline failures by querying TaskRun and PipelineRun status via kubectl and the Tekton Results API. Extracts step container logs, identifies parameter resolution errors, and suggests workspace volume fixes."
category: "CI/CD Integrations"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/tektoncd/pipeline"
tool_ecosystem:
  tool: tekton
  github_stars: 8923
  github_repo: tektoncd/pipeline
  license: Apache-2.0
  maintained: true
---
# Tekton Pipeline Debugger

Debugs Tekton pipeline failures by querying TaskRun and PipelineRun status via kubectl and the Tekton Results API. Extracts step container logs, identifies parameter resolution errors, and suggests workspace volume fixes.

## Overview

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

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-debugger
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-debugger -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-debugger -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill tekton-pipeline-debugger -a codex
```

### OpenClaw

```bash
clawhub install tekton-pipeline-debugger
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tekton-pipeline-debugger/)
