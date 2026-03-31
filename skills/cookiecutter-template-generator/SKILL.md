---
name: "Cookiecutter Template Generator"
description: "Generates project scaffolding using the Cookiecutter CLI with Jinja2 templating. Supports custom template registries, post-generation hooks via Python scripts, and integration with the GitHub template repository API."
category: "Templates &amp; Workflows"
framework: "Codex"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/cookiecutter-template-generator/"
---
# Cookiecutter Template Generator

Generates project scaffolding using the Cookiecutter CLI with Jinja2 templating. Supports custom template registries, post-generation hooks via Python scripts, and integration with the GitHub template repository API.

## Overview

The Cookiecutter Template Generator skill automates project scaffolding using the Cookiecutter CLI and Jinja2 template engine. It creates production-ready project structures from configurable templates, handling variable substitution, conditional file generation, and directory structure customization.

The skill supports pulling templates from GitHub repositories, local directories, and custom registries. It manages cookiecutter.json configurations with typed prompts, default values, and choice variables. Post-generation hooks execute Python or shell scripts for tasks like git initialization, virtual environment setup, and dependency installation.

Advanced features include template composition from multiple sources, conditional directory inclusion based on user choices, and automatic integration with CI/CD configuration generation. The skill can also create new Cookiecutter templates from existing projects, extracting patterns and generating Jinja2 variables for reusable scaffolding.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill cookiecutter-template-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill cookiecutter-template-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill cookiecutter-template-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill cookiecutter-template-generator -a codex
```

### OpenClaw

```bash
clawhub install cookiecutter-template-generator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cookiecutter-template-generator/)
