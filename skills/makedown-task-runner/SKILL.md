---
name: "Makedown Task Runner"
description: "Extracts executable task definitions from Markdown files and runs them as shell pipelines. Parses fenced code blocks with task metadata annotations and manages dependencies between tasks."
category: "Templates & Workflows"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/makedown-task-runner/"
---
# Makedown Task Runner

Extracts executable task definitions from Markdown files and runs them as shell pipelines. Parses fenced code blocks with task metadata annotations and manages dependencies between tasks.

The Makedown Task Runner skill turns Markdown documentation into executable task automation by parsing fenced code blocks annotated with task metadata. It extracts shell commands, Python scripts, and Node.js snippets from Markdown files, resolving task dependencies and executing them in the correct order.



Task definitions use a simple annotation format within Markdown comments that specifies task name, dependencies, environment variables, and working directory. The skill builds a dependency graph and executes tasks using topological sort ordering, with parallel execution for independent task branches. Each task runs in an isolated environment with captured stdout/stderr and exit code tracking.



Advanced capabilities include task parameterization through Jinja2 template variables in code blocks, conditional execution based on file glob patterns or environment checks, and incremental runs that skip tasks whose input files have not changed since the last execution. The skill generates a task index from all Markdown files in a repository, supports Makefile-style phony targets, and provides a watch mode that re-executes tasks when source Markdown files change. Integration with GitHub Actions allows using the same Markdown tasks in CI pipelines.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill makedown-task-runner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill makedown-task-runner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill makedown-task-runner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill makedown-task-runner -a codex
```

### OpenClaw

```bash
clawhub install makedown-task-runner
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/makedown-task-runner/)
