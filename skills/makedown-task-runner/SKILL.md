---
title: "Makedown Task Runner"
description: "The Makedown Task Runner skill turns Markdown documentation into executable task automation by parsing fenced code blocks annotated with task metadata. It extracts shell commands, Python scripts, and Node.js snippets from Markdown files, resolving task dependencies and executing them in the correct order. Task definitions use a simple annotation format within Markdown comments that specifies task name, dependencies, environment variables, and working directory. The skill builds a dependency graph and executes tasks using topological sort ordering, with parallel execution for independent task branches. Each task runs in an isolated environment with captured stdout/stderr and exit code tracking. Advanced capabilities include task parameterization through Jinja2 template variables in code blocks, conditional execution based on file glob patterns or environment checks, and incremental runs that skip tasks whose input files have not changed since the last execution. The skill generates a task index from all Markdown files in a repository, supports Makefile-style phony targets, and provides a watch mode that re-executes tasks when source Markdown files change. Integration with GitHub Actions allows using the same Markdown tasks in CI pipelines."
source: "https://agentskillexchange.com/skills/makedown-task-runner/"
verification: "security_reviewed"
category:
  - "Templates &amp; Workflows"
framework:
  - "Claude Code"
---

# Makedown Task Runner

The Makedown Task Runner skill turns Markdown documentation into executable task automation by parsing fenced code blocks annotated with task metadata. It extracts shell commands, Python scripts, and Node.js snippets from Markdown files, resolving task dependencies and executing them in the correct order. Task definitions use a simple annotation format within Markdown comments that specifies task name, dependencies, environment variables, and working directory. The skill builds a dependency graph and executes tasks using topological sort ordering, with parallel execution for independent task branches. Each task runs in an isolated environment with captured stdout/stderr and exit code tracking. Advanced capabilities include task parameterization through Jinja2 template variables in code blocks, conditional execution based on file glob patterns or environment checks, and incremental runs that skip tasks whose input files have not changed since the last execution. The skill generates a task index from all Markdown files in a repository, supports Makefile-style phony targets, and provides a watch mode that re-executes tasks when source Markdown files change. Integration with GitHub Actions allows using the same Markdown tasks in CI pipelines.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/makedown-task-runner/)
