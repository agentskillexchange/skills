---
title: "Nx Monorepo Workflow Orchestrator"
description: "Manages Nx workspace task orchestration using nx.json configuration and @nrwl/devkit executors. Automates dependency graph analysis, affected project detection, and distributed task execution via Nx Cloud."
slug: "nx-monorepo-workflow-orchestrator"
category:
  - "Templates &amp; Workflows"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://github.com/nrwl/nx"
tool_ecosystem:
  github_repo: "nrwl/nx"
  github_stars: 28496
---

# Nx Monorepo Workflow Orchestrator

Manages Nx workspace task orchestration using nx.json configuration and @nrwl/devkit executors. Automates dependency graph analysis, affected project detection, and distributed task execution via Nx Cloud.

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
clawhub install nx-monorepo-workflow-orchestrator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Nx Monorepo Workflow Orchestrator provides intelligent task management for Nx-based monorepos containing multiple applications and libraries. Using @nrwl/devkit executors and generators, it configures build, test, lint, and deploy pipelines that respect the project dependency graph. The skill analyzes nx.json and project.json configurations to determine optimal task parallelization, ensuring CPU cores are utilized efficiently during CI runs. Affected project detection uses git diff analysis to identify which projects need rebuilding after code changes, dramatically reducing CI times in large monorepos. Integration with Nx Cloud enables distributed task execution across multiple CI agents, with intelligent task distribution based on historical timing data. The orchestrator manages implicit dependencies, global configuration changes, and shared library versioning to prevent stale builds. It generates custom workspace generators using @nrwl/devkit for scaffolding new applications and libraries that conform to team standards. Cache management policies are configured to balance storage costs with rebuild frequency, using both local and remote caching strategies.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nx-monorepo-workflow-orchestrator/)
