---
title: "Tekton Pipeline Debugger"
description: "Debugs Tekton pipeline failures by querying TaskRun and PipelineRun status via kubectl and the Tekton Results API. Extracts step container logs, identifies parameter resolution errors, and suggests workspace volume fixes."
slug: "tekton-pipeline-debugger"
category:
  - "CI/CD Integrations"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/tekton-pipeline-debugger/"
listed: true
---

# Tekton Pipeline Debugger

Debugs Tekton pipeline failures by querying TaskRun and PipelineRun status via kubectl and the Tekton Results API. Extracts step container logs, identifies parameter resolution errors, and suggests workspace volume fixes.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install tekton-pipeline-debugger
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Tekton Pipeline Debugger provides intelligent troubleshooting for failed Tekton CI/CD pipelines running on Kubernetes.
How It Works
The skill queries Kubernetes for PipelineRun and TaskRun resources, extracting status conditions, step container logs, and event histories. It correlates failures across pipeline stages to identify root causes, from parameter resolution errors to workspace volume mount issues.
Key Features
- Automatic extraction of step container logs from failed TaskRuns using kubectl logs with container selection
- Parameter resolution debugging for unbound params, missing defaults, and type mismatches
- Workspace volume troubleshooting for PVC binding failures, access mode conflicts, and storage class issues
- Integration with Tekton Results API for historical failure pattern analysis
Diagnostics
Supports Tekton Pipelines v0.50+ and Tekton Results v0.7+. Detects common issues like missing ServiceAccount permissions, image pull failures, and resource quota exhaustion. Generates fix suggestions with kubectl patch commands.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tekton-pipeline-debugger/)
