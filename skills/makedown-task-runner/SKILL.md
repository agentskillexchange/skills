---
title: Makedown Task Runner
description: The Makedown Task Runner skill turns Markdown documentation into executable
  task automation by parsing fenced code blocks annotated with task metadata. It extracts
  shell commands, Python scripts, and Node.js snippets from Markdown files, resolving
  task dependencies and executing them in the correct order. Task definitions use
  a simple annotation format within Markdown comments that specifies task name, dependencies,
  environment variables, and working directory. The skill builds a dependency graph
  and executes tasks using topological sort ordering, with parallel execution for
  independent task branches. Each task runs in an isolated environment with captured
  stdout/stderr and exit code tracking. Advanced capabilities include task parameterization
  through Jinja2 template variables in code blocks, conditional execution based on
  file glob patterns or environment checks, and incremental runs that skip tasks whose
  input files have not changed since the last execution. The skill generates a task
  index from all Markdown files in a repository, supports Makefile-style phony targets,
  and provides a watch mode that re-executes tasks when source Markdown files change.
  Integration with GitHub Actions allows using the same Markdown tasks in CI pipelines.
verification: security_reviewed
source: https://agentskillexchange.com/skills/makedown-task-runner/
category:
- Templates &amp; Workflows
framework:
- Claude Code
---

# Makedown Task Runner

The Makedown Task Runner skill turns Markdown documentation into executable task automation by parsing fenced code blocks annotated with task metadata. It extracts shell commands, Python scripts, and Node.js snippets from Markdown files, resolving task dependencies and executing them in the correct order. Task definitions use a simple annotation format within Markdown comments that specifies task name, dependencies, environment variables, and working directory. The skill builds a dependency graph and executes tasks using topological sort ordering, with parallel execution for independent task branches. Each task runs in an isolated environment with captured stdout/stderr and exit code tracking. Advanced capabilities include task parameterization through Jinja2 template variables in code blocks, conditional execution based on file glob patterns or environment checks, and incremental runs that skip tasks whose input files have not changed since the last execution. The skill generates a task index from all Markdown files in a repository, supports Makefile-style phony targets, and provides a watch mode that re-executes tasks when source Markdown files change. Integration with GitHub Actions allows using the same Markdown tasks in CI pipelines.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/makedown-task-runner/)
