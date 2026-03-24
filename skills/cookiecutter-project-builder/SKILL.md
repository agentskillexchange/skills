---
name: "Cookiecutter Project Builder"
description: "Creates project scaffolds from Cookiecutter templates with interactive variable resolution. Integrates with cruft for template drift detection and copier for advanced multi-template composition."
category: "Templates & Workflows"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/cookiecutter-project-builder/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "gitlab"  # from ase_tool_match
  github_stars: 24276  # from ase_github_stars (integer, not string)
  github_repo: "gitlabhq/gitlabhq"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Cookiecutter Project Builder

Creates project scaffolds from Cookiecutter templates with interactive variable resolution. Integrates with cruft for template drift detection and copier for advanced multi-template composition.

## Overview

The Cookiecutter Project Builder automates project scaffolding from community and custom Cookiecutter templates with intelligent variable resolution and post-generation hooks. It wraps the cookiecutter Python library to render Jinja2-templated project structures, supporting both local template directories and remote GitHub/GitLab repositories. For enterprise use, it integrates with cruft to detect template drift in previously generated projects, showing which files have diverged from the upstream template and offering selective update merging. The tool also supports copier as an alternative templating engine for advanced scenarios including multi-template composition, conditional file inclusion, and migration scripts between template versions. It pre-validates template variables against JSON Schema definitions in cookiecutter.json, providing autocomplete suggestions and type checking before generation begins. Post-generation hooks execute setup scripts for initializing git repositories, installing dependencies via pip/npm/cargo, creating virtual environments, and configuring pre-commit hooks. The builder maintains a local template registry for frequently used scaffolds with pinned versions and organization-specific variable defaults.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill cookiecutter-project-builder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill cookiecutter-project-builder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill cookiecutter-project-builder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill cookiecutter-project-builder -a codex
```

### OpenClaw

```bash
clawhub install cookiecutter-project-builder
```

## Source

- Marketplace: https://agentskillexchange.com/skills/cookiecutter-project-builder/
