---
name: "Cookiecutter Project Template Scaffolder"
description: "Generates project scaffolds using Cookiecutter templates from GitHub repositories or local directories. Automates cookiecutter.json variable prompting and post-generation hook execution."
category: "Templates &amp; Workflows"
framework: "Cursor"
verification: security_reviewed
source: "https://github.com/cookiecutter/cookiecutter"
tool_ecosystem:
  github_repo: "https://github.com/cookiecutter/cookiecutter"
  github_stars: 24786
---
# Cookiecutter Project Template Scaffolder

Generates project scaffolds using Cookiecutter templates from GitHub repositories or local directories. Automates cookiecutter.json variable prompting and post-generation hook execution.

The Cookiecutter Project Template Scaffolder automates project initialization using the Cookiecutter templating engine. It accepts a GitHub repository URL, a local directory path, or a Cookiecutter template alias and generates a fully scaffolded project by processing Jinja2 templates with user-provided or default context variables from cookiecutter.json. The skill handles interactive variable prompting, providing intelligent defaults based on the target project type, and validates inputs against any defined constraints. It executes pre-generation and post-generation hooks defined in the template’s hooks/ directory, supporting both shell scripts and Python scripts. The skill can chain multiple templates together for monorepo scaffolding, applying different Cookiecutter templates to subdirectories. It supports private GitHub repositories via token authentication, local template caching in ~/.cookiecutters/, and replay of previous configurations from ~/.cookiecutter_replay/. Output structure is validated against an expected file manifest when provided.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill cookiecutter-project-template-scaffolder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill cookiecutter-project-template-scaffolder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill cookiecutter-project-template-scaffolder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill cookiecutter-project-template-scaffolder -a codex
```

### OpenClaw

```bash
clawhub install cookiecutter-project-template-scaffolder
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cookiecutter-project-template-scaffolder/)
