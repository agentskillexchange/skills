---
name: "devenv Declarative Developer Environments with Nix"
description: "A fast, declarative, and reproducible developer environment tool built on Nix. devenv lets teams define project dependencies, services, scripts, and language toolchains in a single configuration file, ensuring consistent environments across machines."
category: "Developer Tools"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/cachix/devenv"
tool_ecosystem:
  tool: devenv
  github_repo: cachix/devenv
  github_stars: 6614
---
# devenv Declarative Developer Environments with Nix

A fast, declarative, and reproducible developer environment tool built on Nix. devenv lets teams define project dependencies, services, scripts, and language toolchains in a single configuration file, ensuring consistent environments across machines.

## Overview

devenv is an open-source tool from Cachix that makes Nix-powered developer environments accessible without requiring deep Nix expertise. It provides a high-level configuration interface (devenv.nix) where developers declare their project’s packages, language toolchains, services, scripts, pre-commit hooks, and environment variables — then activates a fully reproducible shell with everything configured.

The core workflow is simple: run `devenv init` to scaffold a project, edit `devenv.nix` to declare dependencies, and run `devenv shell` to enter an environment where everything is available. Unlike Docker, devenv runs natively on your machine with no container overhead, giving full access to hardware acceleration, native file system performance, and host networking.

Key features include: 50+ language integrations with built-in support for compilers, LSP servers, formatters, linters, and version selection across Python, Rust, Go, Node.js, Ruby, PHP, and more; service management via `devenv up` for PostgreSQL, MySQL, Redis, Elasticsearch, and other databases/services; process management for running development servers, watchers, and background tasks; pre-commit hooks with automatic git integration; and tasks for defining build steps and their dependencies.

devenv pulls from the 100,000+ package Nixpkgs repository, supporting Linux (x64, ARM64), macOS (Intel, Apple Silicon), and WSL2. Every environment is hermetic and reproducible — the same devenv.nix produces the same environment on any machine. Lock files track exact package versions, and `devenv update` handles controlled dependency bumps.

Installation requires only the Nix package manager. devenv itself is available via `nix profile install` or the cachix binary cache. The project is actively maintained with regular releases, comprehensive documentation at devenv.sh, and supports composing environments from remote configurations via `--from` flags for organizational sharing.

Typical use cases include onboarding new developers instantly (no manual setup), CI/CD environments that match local development exactly, polyglot projects with complex dependency graphs, and teams that need guaranteed reproducibility across macOS and Linux workstations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill devenv-declarative-developer-environments-nix
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill devenv-declarative-developer-environments-nix -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill devenv-declarative-developer-environments-nix -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill devenv-declarative-developer-environments-nix -a codex
```

### OpenClaw

```bash
clawhub install devenv-declarative-developer-environments-nix
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/devenv-declarative-developer-environments-nix/)
