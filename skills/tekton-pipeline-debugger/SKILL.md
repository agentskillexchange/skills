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

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/tekton-pipeline-debugger
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/tekton-pipeline-debugger` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tekton-pipeline-debugger/)
