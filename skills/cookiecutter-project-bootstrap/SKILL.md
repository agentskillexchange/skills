---
name: "Cookiecutter Project Bootstrap"
description: "Bootstraps new projects from Cookiecutter templates with variable substitution and post-generation hooks. Supports remote template repositories via the cookiecutter CLI and Jinja2 rendering engine."
category: "Templates & Workflows"
framework: "MCP-compatible"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/cookiecutter-project-bootstrap/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "gitlab"  # from ase_tool_match
  github_stars: 24276  # from ase_github_stars (integer, not string)
  github_repo: "gitlabhq/gitlabhq"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Cookiecutter Project Bootstrap

Bootstraps new projects from Cookiecutter templates with variable substitution and post-generation hooks. Supports remote template repositories via the cookiecutter CLI and Jinja2 rendering engine.

## Overview

The Cookiecutter Project Bootstrap skill automates new project creation using Cookiecutter templates. It processes cookiecutter.json configuration files for variable prompting and uses the Jinja2 rendering engine for template file generation with variable substitution.

The skill supports template sourcing from local directories, Git repositories (GitHub, GitLab, Bitbucket), and zip archives. It handles nested template directories, conditional file generation using Jinja2 conditionals, and post-generation hooks for automated setup tasks like git init, virtual environment creation, and dependency installation.

Advanced features include template replay from ~/.cookiecutter_replay for reproducible project creation, custom template extensions via cookiecutter extensions API, and integration with pre-commit hooks for immediate code quality enforcement. The skill validates generated project structure against configurable rules and runs post-gen test suites.

Configuration supports default values via ~/.cookiecutterrc, abbreviation expansion for frequently used templates, and batch project generation from YAML manifest files.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill cookiecutter-project-bootstrap
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill cookiecutter-project-bootstrap -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill cookiecutter-project-bootstrap -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill cookiecutter-project-bootstrap -a codex
```

### OpenClaw

```bash
clawhub install cookiecutter-project-bootstrap
```

## Source

- Marketplace: https://agentskillexchange.com/skills/cookiecutter-project-bootstrap/
