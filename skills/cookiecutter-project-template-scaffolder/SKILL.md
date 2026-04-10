---
name: "Cookiecutter Project Template Scaffolder"
description: "Generates project scaffolds using Cookiecutter templates from GitHub repositories or local directories. Automates cookiecutter.json variable prompting and post-generation hook execution."
verification: security_reviewed
source: "https://github.com/cookiecutter/cookiecutter"
category:
  - "Templates &amp; Workflows"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "cookiecutter/cookiecutter"
  github_stars: 24786
---

# Cookiecutter Project Template Scaffolder

The Cookiecutter Project Template Scaffolder automates project initialization using the Cookiecutter templating engine. It accepts a GitHub repository URL, a local directory path, or a Cookiecutter template alias and generates a fully scaffolded project by processing Jinja2 templates with user-provided or default context variables from cookiecutter.json. The skill handles interactive variable prompting, providing intelligent defaults based on the target project type, and validates inputs against any defined constraints. It executes pre-generation and post-generation hooks defined in the template's hooks/ directory, supporting both shell scripts and Python scripts. The skill can chain multiple templates together for monorepo scaffolding, applying different Cookiecutter templates to subdirectories. It supports private GitHub repositories via token authentication, local template caching in ~/.cookiecutters/, and replay of previous configurations from ~/.cookiecutter_replay/. Output structure is validated against an expected file manifest when provided.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cookiecutter-project-template-scaffolder/)
