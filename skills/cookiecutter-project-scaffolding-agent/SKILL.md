---
name: "Cookiecutter Project Scaffolding Agent"
description: "Generates project boilerplate from Cookiecutter templates with interactive variable prompts. Supports custom Jinja2 hooks, post-generation scripts, and template composition from multiple cookiecutter.json sources for complex monorepo scaffolding."
category: "Templates & Workflows"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/cookiecutter-project-scaffolding-agent/"
---
# Cookiecutter Project Scaffolding Agent

Generates project boilerplate from Cookiecutter templates with interactive variable prompts. Supports custom Jinja2 hooks, post-generation scripts, and template composition from multiple cookiecutter.json sources for complex monorepo scaffolding.

The Cookiecutter Project Scaffolding Agent automates new project creation using the Cookiecutter templating system. It manages a curated library of project templates for various technology stacks including FastAPI backends, React frontends, Terraform modules, and Python packages conforming to PyPA standards.



Template customization flows through cookiecutter.json variable definitions with validation rules, conditional file inclusion, and computed defaults based on prior selections. Pre and post-generation hooks execute setup tasks like git initialization, virtual environment creation, dependency installation via pip or npm, and initial commit generation.



Advanced features include template composition where multiple Cookiecutter templates merge into unified project structures for monorepo setups. The agent supports private template repositories via Git SSH authentication and template version pinning through Git tags. Generated projects include pre-configured CI pipelines for GitHub Actions or GitLab CI, Docker configurations, pre-commit hook setups with black/ruff/mypy, and documentation scaffolding with MkDocs Material theme. Template updates can be replayed onto existing projects using cruft for downstream synchronization.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill cookiecutter-project-scaffolding-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill cookiecutter-project-scaffolding-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill cookiecutter-project-scaffolding-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill cookiecutter-project-scaffolding-agent -a codex
```

### OpenClaw

```bash
clawhub install cookiecutter-project-scaffolding-agent
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cookiecutter-project-scaffolding-agent/)
