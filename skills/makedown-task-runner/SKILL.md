---
title: "Makedown Task Runner"
description: "Extracts executable task definitions from Markdown files and runs them as shell pipelines. Parses fenced code blocks with task metadata annotations and manages dependencies between tasks."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/makedown-task-runner/"
category:
  - "Templates &amp; Workflows"
framework:
  - "Claude Code"
---

# Makedown Task Runner

The Makedown Task Runner skill turns Markdown documentation into executable task automation by parsing fenced code blocks annotated with task metadata. It extracts shell commands, Python scripts, and Node.js snippets from Markdown files, resolving task dependencies and executing them in the correct order.

Task definitions use a simple annotation format within Markdown comments that specifies task name, dependencies, environment variables, and working directory. The skill builds a dependency graph and executes tasks using topological sort ordering, with parallel execution for independent task branches. Each task runs in an isolated environment with captured stdout/stderr and exit code tracking.

Advanced capabilities include task parameterization through Jinja2 template variables in code blocks, conditional execution based on file glob patterns or environment checks, and incremental runs that skip tasks whose input files have not changed since the last execution. The skill generates a task index from all Markdown files in a repository, supports Makefile-style phony targets, and provides a watch mode that re-executes tasks when source Markdown files change. Integration with GitHub Actions allows using the same Markdown tasks in CI pipelines.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/makedown-task-runner/)
