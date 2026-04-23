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

Debugs Tekton pipeline failures by querying TaskRun and PipelineRun status via kubectl and the Tekton Results API. Extracts step container logs, identifies parameter resolution errors, and suggests workspace volume fixes.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/tekton-pipeline-debugger/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/tekton-pipeline-debugger
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/tekton-pipeline-debugger`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tekton-pipeline-debugger/)
