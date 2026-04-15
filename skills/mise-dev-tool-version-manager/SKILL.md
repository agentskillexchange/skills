---
title: "Mise Dev Tool Version Manager"
description: "Use mise (mise-en-place) to manage development tool versions, environment variables, and task running from a single configuration file. Replaces asdf, nvm, pyenv, rbenv, and direnv in one tool."
verification: listed
source: "https://github.com/jdx/mise"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "jdx/mise"
  github_stars: 26298
---

# Mise Dev Tool Version Manager

Overview
mise (pronounced “meez”) is a polyglot development tool version manager written in Rust. It replaces multiple single-purpose tools — asdf for version management, nvm/pyenv/rbenv for language-specific versions, direnv for environment variables, and make for task running — with a single unified tool configured through a mise.toml file.

Unlike shim-based version managers, mise modifies the PATH directly, meaning which node returns the real binary path rather than a shim. This approach provides better compatibility with tools that inspect binary locations and eliminates the performance overhead of shim execution.

How It Works
Agents use mise to ensure consistent development environments across teams and CI/CD pipelines. A mise.toml file in the project root declares tool versions, environment variables, and tasks. Running mise install installs all specified tools, and mise activate hooks into the shell to automatically switch versions when entering project directories.

mise supports hundreds of tools through its registry, including Node.js, Python, Go, Rust, Terraform, kubectl, jq, and many more. It also supports environment variable management with .env file loading and task definitions with dependency graphs, making it a complete project environment configuration tool.

Key Features
The tool provides a task runner that supports shell commands with dependencies between tasks, parallel execution, and file watching. Environment variables can be scoped per directory, loaded from .env files, or templated. mise supports asdf plugin compatibility, meaning the existing ecosystem of asdf plugins works out of the box. With over 26,000 GitHub stars and frequent releases, mise is one of the most actively maintained developer tools available. It installs via a single curl command and supports bash, zsh, fish, and PowerShell.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/mise-dev-tool-version-manager
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/mise-dev-tool-version-manager` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mise-dev-tool-version-manager/)
