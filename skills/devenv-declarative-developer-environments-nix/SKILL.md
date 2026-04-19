---
title: "devenv Declarative Developer Environments with Nix"
description: "devenv is an open-source tool from Cachix that makes Nix-powered developer environments accessible without requiring deep Nix expertise. It provides a high-level configuration interface (devenv.nix) where developers declare their project&#8217;s packages, language toolchains, services, scripts, pre-commit hooks, and environment variables — then activates a fully reproducible shell with everything configured. The core workflow is simple: run devenv init to scaffold a project, edit devenv.nix to declare dependencies, and run devenv shell to enter an environment where everything is available. Unlike Docker, devenv runs natively on your machine with no container overhead, giving full access to hardware acceleration, native file system performance, and host networking. Key features include: 50+ language integrations with built-in support for compilers, LSP servers, formatters, linters, and version selection across Python, Rust, Go, Node.js, Ruby, PHP, and more; service management via devenv up for PostgreSQL, MySQL, Redis, Elasticsearch, and other databases/services; process management for running development servers, watchers, and background tasks; pre-commit hooks with automatic git integration; and tasks for defining build steps and their dependencies. devenv pulls from the 100,000+ package Nixpkgs repository, supporting Linux (x64, ARM64), macOS (Intel, Apple Silicon), and WSL2. Every environment is hermetic and reproducible — the same devenv.nix produces the same environment on any machine. Lock files track exact package versions, and devenv update handles controlled dependency bumps. Installation requires only the Nix package manager. devenv itself is available via nix profile install or the cachix binary cache. The project is actively maintained with regular releases, comprehensive documentation at devenv.sh, and supports composing environments from remote configurations via --from flags for organizational sharing. Typical use cases include onboarding new developers instantly (no manual setup), CI/CD environments that match local development exactly, polyglot projects with complex dependency graphs, and teams that need guaranteed reproducibility across macOS and Linux workstations."
source: "https://github.com/cachix/devenv"
verification: "security_reviewed"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "cachix/devenv"
  github_stars: 6614
---

# devenv Declarative Developer Environments with Nix

devenv is an open-source tool from Cachix that makes Nix-powered developer environments accessible without requiring deep Nix expertise. It provides a high-level configuration interface (devenv.nix) where developers declare their project&#8217;s packages, language toolchains, services, scripts, pre-commit hooks, and environment variables — then activates a fully reproducible shell with everything configured. The core workflow is simple: run devenv init to scaffold a project, edit devenv.nix to declare dependencies, and run devenv shell to enter an environment where everything is available. Unlike Docker, devenv runs natively on your machine with no container overhead, giving full access to hardware acceleration, native file system performance, and host networking. Key features include: 50+ language integrations with built-in support for compilers, LSP servers, formatters, linters, and version selection across Python, Rust, Go, Node.js, Ruby, PHP, and more; service management via devenv up for PostgreSQL, MySQL, Redis, Elasticsearch, and other databases/services; process management for running development servers, watchers, and background tasks; pre-commit hooks with automatic git integration; and tasks for defining build steps and their dependencies. devenv pulls from the 100,000+ package Nixpkgs repository, supporting Linux (x64, ARM64), macOS (Intel, Apple Silicon), and WSL2. Every environment is hermetic and reproducible — the same devenv.nix produces the same environment on any machine. Lock files track exact package versions, and devenv update handles controlled dependency bumps. Installation requires only the Nix package manager. devenv itself is available via nix profile install or the cachix binary cache. The project is actively maintained with regular releases, comprehensive documentation at devenv.sh, and supports composing environments from remote configurations via --from flags for organizational sharing. Typical use cases include onboarding new developers instantly (no manual setup), CI/CD environments that match local development exactly, polyglot projects with complex dependency graphs, and teams that need guaranteed reproducibility across macOS and Linux workstations.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/devenv-declarative-developer-environments-nix/)
