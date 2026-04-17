---
name: Tekton Pipeline Resource Optimizer
description: Analyzes Tekton Pipeline and Task resource definitions using the Tekton
  Results API. Recommends CPU/memory request adjustments based on historical TaskRun
  metrics from Prometheus.
category: CI/CD Integrations
framework: Cursor
verification: security_reviewed
source: https://github.com/tektoncd/pipeline
tool_ecosystem:
  github_repo: tektoncd/pipeline
  github_stars: 8936
  tool: pipeline
  license: Apache-2.0
  maintained: true
---
# Tekton Pipeline Resource Optimizer
Analyzes Tekton Pipeline and Task resource definitions using the Tekton Results API. Recommends CPU/memory request adjustments based on historical TaskRun metrics from Prometheus.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/tekton-pipeline-resource-optimizer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/tekton-pipeline-resource-optimizer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tekton-pipeline-resource-optimizer/)
