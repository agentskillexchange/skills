---
name: "Nx Monorepo Workflow Orchestrator"
description: "Manages Nx workspace task orchestration using nx.json configuration and @nrwl/devkit executors. Automates dependency graph analysis, affected project detection, and distributed task execution via Nx Cloud."
verification: security_reviewed
source: "https://github.com/nrwl/nx"
category:
  - "Templates &amp; Workflows"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "nrwl/nx"
  github_stars: 28496
---

# Nx Monorepo Workflow Orchestrator

The Nx Monorepo Workflow Orchestrator provides intelligent task management for Nx-based monorepos containing multiple applications and libraries. Using @nrwl/devkit executors and generators, it configures build, test, lint, and deploy pipelines that respect the project dependency graph. The skill analyzes nx.json and project.json configurations to determine optimal task parallelization, ensuring CPU cores are utilized efficiently during CI runs. Affected project detection uses git diff analysis to identify which projects need rebuilding after code changes, dramatically reducing CI times in large monorepos. Integration with Nx Cloud enables distributed task execution across multiple CI agents, with intelligent task distribution based on historical timing data. The orchestrator manages implicit dependencies, global configuration changes, and shared library versioning to prevent stale builds. It generates custom workspace generators using @nrwl/devkit for scaffolding new applications and libraries that conform to team standards. Cache management policies are configured to balance storage costs with rebuild frequency, using both local and remote caching strategies.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nx-monorepo-workflow-orchestrator/)
