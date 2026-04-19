---
title: "Mise Dev Tool Version Manager"
description: "Overview mise (pronounced &#8220;meez&#8221;) is a polyglot development tool version manager written in Rust. It replaces multiple single-purpose tools — asdf for version management, nvm/pyenv/rbenv for language-specific versions, direnv for environment variables, and make for task running — with a single unified tool configured through a mise.toml file. Unlike shim-based version managers, mise modifies the PATH directly, meaning which node returns the real binary path rather than a shim. This approach provides better compatibility with tools that inspect binary locations and eliminates the performance overhead of shim execution. How It Works Agents use mise to ensure consistent development environments across teams and CI/CD pipelines. A mise.toml file in the project root declares tool versions, environment variables, and tasks. Running mise install installs all specified tools, and mise activate hooks into the shell to automatically switch versions when entering project directories. mise supports hundreds of tools through its registry, including Node.js, Python, Go, Rust, Terraform, kubectl, jq, and many more. It also supports environment variable management with .env file loading and task definitions with dependency graphs, making it a complete project environment configuration tool. Key Features The tool provides a task runner that supports shell commands with dependencies between tasks, parallel execution, and file watching. Environment variables can be scoped per directory, loaded from .env files, or templated. mise supports asdf plugin compatibility, meaning the existing ecosystem of asdf plugins works out of the box. With over 26,000 GitHub stars and frequent releases, mise is one of the most actively maintained developer tools available. It installs via a single curl command and supports bash, zsh, fish, and PowerShell."
source: "https://github.com/jdx/mise"
verification: "listed"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "jdx/mise"
  github_stars: 26298
---

# Mise Dev Tool Version Manager

Overview mise (pronounced &#8220;meez&#8221;) is a polyglot development tool version manager written in Rust. It replaces multiple single-purpose tools — asdf for version management, nvm/pyenv/rbenv for language-specific versions, direnv for environment variables, and make for task running — with a single unified tool configured through a mise.toml file. Unlike shim-based version managers, mise modifies the PATH directly, meaning which node returns the real binary path rather than a shim. This approach provides better compatibility with tools that inspect binary locations and eliminates the performance overhead of shim execution. How It Works Agents use mise to ensure consistent development environments across teams and CI/CD pipelines. A mise.toml file in the project root declares tool versions, environment variables, and tasks. Running mise install installs all specified tools, and mise activate hooks into the shell to automatically switch versions when entering project directories. mise supports hundreds of tools through its registry, including Node.js, Python, Go, Rust, Terraform, kubectl, jq, and many more. It also supports environment variable management with .env file loading and task definitions with dependency graphs, making it a complete project environment configuration tool. Key Features The tool provides a task runner that supports shell commands with dependencies between tasks, parallel execution, and file watching. Environment variables can be scoped per directory, loaded from .env files, or templated. mise supports asdf plugin compatibility, meaning the existing ecosystem of asdf plugins works out of the box. With over 26,000 GitHub stars and frequent releases, mise is one of the most actively maintained developer tools available. It installs via a single curl command and supports bash, zsh, fish, and PowerShell.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mise-dev-tool-version-manager/)
