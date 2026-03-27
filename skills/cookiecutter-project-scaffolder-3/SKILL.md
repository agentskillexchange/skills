---
name: "Cookiecutter Project Scaffolder"
description: "Scaffolds project templates using the Cookiecutter engine with Jinja2 templating and pre/post generation hooks. Supports conditional file inclusion, directory renaming, and cookiecutter.json variable validation with JSON Schema."
category: "Templates & Workflows"
framework: "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/cookiecutter-project-scaffolder-3/"
---

# Cookiecutter Project Scaffolder

Scaffolds project templates using the Cookiecutter engine with Jinja2 templating and pre/post generation hooks. Supports conditional file inclusion, directory renaming, and cookiecutter.json variable validation with JSON Schema.

## Overview

The Cookiecutter Project Scaffolder skill automates project template generation using the Cookiecutter engine with its Jinja2 templating system. It creates and manages template repositories with `cookiecutter.json` configuration files that define project variables, defaults, and choice prompts.

This skill generates sophisticated templates with conditional file inclusion using Jinja2 `{% if %}` blocks in directory names and filenames, enabling templates that adapt their structure based on user choices. It supports nested `cookiecutter.json` configurations for multi-component project scaffolding.

Pre and post-generation hooks are created as Python scripts in the `hooks/` directory, handling tasks like Git repository initialization, virtual environment creation, dependency installation via `pip` or `poetry`, and initial commit generation. The skill validates template variables using JSON Schema definitions.

Advanced features include template composition from multiple Cookiecutter repositories, replay file management for reproducible generation, and integration with `cruft` for keeping generated projects in sync with upstream template changes. The skill also supports private template registries and GitHub template repository conventions.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill cookiecutter-project-scaffolder-3
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill cookiecutter-project-scaffolder-3 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill cookiecutter-project-scaffolder-3 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill cookiecutter-project-scaffolder-3 -a codex
```

### OpenClaw

```bash
clawhub install cookiecutter-project-scaffolder-3
```

## Source

- Marketplace: https://agentskillexchange.com/skills/cookiecutter-project-scaffolder-3/
