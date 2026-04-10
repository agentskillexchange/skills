---
title: "Cookiecutter Project Template Scaffolder"
description: "Generates project scaffolds using Cookiecutter templates from GitHub repositories or local directories. Automates cookiecutter.json variable prompting and post-generation hook execution."
slug: "cookiecutter-project-template-scaffolder"
category:
  - "Templates &amp; Workflows"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://github.com/cookiecutter/cookiecutter"
tool_ecosystem:
  github_repo: "cookiecutter/cookiecutter"
  github_stars: 24786
listed: true
---

# Cookiecutter Project Template Scaffolder

Generates project scaffolds using Cookiecutter templates from GitHub repositories or local directories. Automates cookiecutter.json variable prompting and post-generation hook execution.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install cookiecutter-project-template-scaffolder
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Cookiecutter Project Template Scaffolder automates project initialization using the Cookiecutter templating engine. It accepts a GitHub repository URL, a local directory path, or a Cookiecutter template alias and generates a fully scaffolded project by processing Jinja2 templates with user-provided or default context variables from cookiecutter.json. The skill handles interactive variable prompting, providing intelligent defaults based on the target project type, and validates inputs against any defined constraints. It executes pre-generation and post-generation hooks defined in the template’s hooks/ directory, supporting both shell scripts and Python scripts. The skill can chain multiple templates together for monorepo scaffolding, applying different Cookiecutter templates to subdirectories. It supports private GitHub repositories via token authentication, local template caching in ~/.cookiecutters/, and replay of previous configurations from ~/.cookiecutter_replay/. Output structure is validated against an expected file manifest when provided.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cookiecutter-project-template-scaffolder/)
