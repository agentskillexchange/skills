---
title: "Cookiecutter Project Scaffolder"
description: "Scaffolds project templates using the Cookiecutter engine with Jinja2 templating and pre/post generation hooks. Supports conditional file inclusion, directory renaming, and cookiecutter.json variable validation with JSON Schema."
verification: "security_reviewed"
source: "https://github.com/cookiecutter/cookiecutter"
category:
  - "Templates & Workflows"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "cookiecutter/cookiecutter"
  github_stars: 24818
---

# Cookiecutter Project Scaffolder

The Cookiecutter Project Scaffolder skill automates project template generation using the Cookiecutter engine with its Jinja2 templating system. It creates and manages template repositories with cookiecutter.json configuration files that define project variables, defaults, and choice prompts. This skill generates sophisticated templates with conditional file inclusion using Jinja2 {% if %} blocks in directory names and filenames, enabling templates that adapt their structure based on user choices. It supports nested cookiecutter.json configurations for multi-component project scaffolding. Pre and post-generation hooks are created as Python scripts in the hooks/ directory, handling tasks like Git repository initialization, virtual environment creation, dependency installation via pip or poetry, and initial commit generation. The skill validates template variables using JSON Schema definitions. Advanced features include template composition from multiple Cookiecutter repositories, replay file management for reproducible generation, and integration with cruft for keeping generated projects in sync with upstream template changes. The skill also supports private template registries and GitHub template repository conventions.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/cookiecutter-project-scaffolder-3/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/cookiecutter-project-scaffolder-3
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/cookiecutter-project-scaffolder-3`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cookiecutter-project-scaffolder-3/)
