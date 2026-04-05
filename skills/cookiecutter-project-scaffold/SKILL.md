---
name: "Cookiecutter Project Scaffold"
description: "Generates project boilerplate from Cookiecutter templates with Jinja2 variable injection. Supports custom hooks for post-generation linting via Ruff and pre-commit framework setup."
category: "Templates &amp; Workflows"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/cookiecutter-project-scaffold/"
---
# Cookiecutter Project Scaffold

Generates project boilerplate from Cookiecutter templates with Jinja2 variable injection. Supports custom hooks for post-generation linting via Ruff and pre-commit framework setup.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill cookiecutter-project-scaffold
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill cookiecutter-project-scaffold -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill cookiecutter-project-scaffold -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill cookiecutter-project-scaffold -a codex
```

### OpenClaw

```bash
clawhub install cookiecutter-project-scaffold
```

## Details

Generates project boilerplate from Cookiecutter templates with Jinja2 variable injection. Supports custom hooks for post-generation linting via Ruff and pre-commit framework setup.

This skill provides automated tooling for cookiecutter project scaffold workflows. It integrates directly with your development pipeline, offering configurable scanning depth, custom rule definitions, and structured output formats compatible with major CI/CD platforms. The agent handles authentication, rate limiting, and retry logic internally, so you can focus on reviewing results rather than managing infrastructure. Supports both interactive and headless operation modes with JSON and SARIF output for downstream processing. Includes built-in caching to minimize redundant API calls across sequential runs.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cookiecutter-project-scaffold/)
