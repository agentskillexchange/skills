---
name: "Nx Monorepo Workflow Orchestrator"
description: "Manages Nx workspace task orchestration using nx.json configuration and @nrwl/devkit executors. Automates dependency graph analysis, affected project detection, and distributed task execution via Nx Cloud."
category: "Templates & Workflows"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/nx-monorepo-workflow-orchestrator/"
---
# Nx Monorepo Workflow Orchestrator

Manages Nx workspace task orchestration using nx.json configuration and @nrwl/devkit executors. Automates dependency graph analysis, affected project detection, and distributed task execution via Nx Cloud.

## Overview

The Nx Monorepo Workflow Orchestrator provides intelligent task management for Nx-based monorepos containing multiple applications and libraries. Using @nrwl/devkit executors and generators, it configures build, test, lint, and deploy pipelines that respect the project dependency graph. The skill analyzes nx.json and project.json configurations to determine optimal task parallelization, ensuring CPU cores are utilized efficiently during CI runs. Affected project detection uses git diff analysis to identify which projects need rebuilding after code changes, dramatically reducing CI times in large monorepos. Integration with Nx Cloud enables distributed task execution across multiple CI agents, with intelligent task distribution based on historical timing data. The orchestrator manages implicit dependencies, global configuration changes, and shared library versioning to prevent stale builds. It generates custom workspace generators using @nrwl/devkit for scaffolding new applications and libraries that conform to team standards. Cache management policies are configured to balance storage costs with rebuild frequency, using both local and remote caching strategies.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill nx-monorepo-workflow-orchestrator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill nx-monorepo-workflow-orchestrator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill nx-monorepo-workflow-orchestrator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill nx-monorepo-workflow-orchestrator -a codex
```

### OpenClaw

```bash
clawhub install nx-monorepo-workflow-orchestrator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nx-monorepo-workflow-orchestrator/)
