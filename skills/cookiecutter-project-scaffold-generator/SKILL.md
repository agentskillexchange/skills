---
name: "Cookiecutter Project Scaffold Generator"
description: "Generates project scaffolds from Cookiecutter templates with Jinja2 variable interpolation. Supports post-generation hooks, conditional file inclusion, and template composition from multiple sources."
category: "Templates & Workflows"
framework: "Codex"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/cookiecutter-project-scaffold-generator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "docker"  # from ase_tool_match
  github_stars: 71560  # from ase_github_stars (integer, not string)
  github_repo: "moby/moby"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Cookiecutter Project Scaffold Generator

Generates project scaffolds from Cookiecutter templates with Jinja2 variable interpolation. Supports post-generation hooks, conditional file inclusion, and template composition from multiple sources.

## Overview

The Cookiecutter Project Scaffold Generator skill automates new project creation using the Cookiecutter templating system with Jinja2-based variable interpolation. It manages a curated library of project templates for Python packages, FastAPI services, React applications, CLI tools, and microservice architectures. The skill handles interactive and non-interactive template rendering, supporting cookiecutter.json defaults, choice variables, and conditional file/directory inclusion based on user selections. Post-generation hooks execute setup tasks like git initialization, virtual environment creation, dependency installation, and CI/CD pipeline configuration. Template composition allows combining multiple template fragments (testing setup, Docker configuration, documentation scaffolding) into a unified project structure. The skill validates generated projects by running linters, type checkers, and test suites immediately after scaffolding to ensure templates produce working codebases.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill cookiecutter-project-scaffold-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill cookiecutter-project-scaffold-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill cookiecutter-project-scaffold-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill cookiecutter-project-scaffold-generator -a codex
```

### OpenClaw

```bash
clawhub install cookiecutter-project-scaffold-generator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/cookiecutter-project-scaffold-generator/
