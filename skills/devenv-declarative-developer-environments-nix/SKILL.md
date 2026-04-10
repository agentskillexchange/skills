---
title: "devenv Declarative Developer Environments with Nix"
description: "A fast, declarative, and reproducible developer environment tool built on Nix. devenv lets teams define project dependencies, services, scripts, and language toolchains in a single configuration file, ensuring consistent environments across machines."
slug: "devenv-declarative-developer-environments-nix"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/cachix/devenv"
tool_ecosystem:
  github_repo: "cachix/devenv"
  github_stars: 6614
listed: true
---

# devenv Declarative Developer Environments with Nix

A fast, declarative, and reproducible developer environment tool built on Nix. devenv lets teams define project dependencies, services, scripts, and language toolchains in a single configuration file, ensuring consistent environments across machines.

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
clawhub install devenv-declarative-developer-environments-nix
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

devenv is an open-source tool from Cachix that makes Nix-powered developer environments accessible without requiring deep Nix expertise. It provides a high-level configuration interface (devenv.nix) where developers declare their project’s packages, language toolchains, services, scripts, pre-commit hooks, and environment variables — then activates a fully reproducible shell with everything configured.
The core workflow is simple: run devenv init to scaffold a project, edit devenv.nix to declare dependencies, and run devenv shell to enter an environment where everything is available. Unlike Docker, devenv runs natively on your machine with no container overhead, giving full access to hardware acceleration, native file system performance, and host networking.
Key features include: 50+ language integrations with built-in support for compilers, LSP servers, formatters, linters, and version selection across Python, Rust, Go, Node.js, Ruby, PHP, and more; service management via devenv up for PostgreSQL, MySQL, Redis, Elasticsearch, and other databases/services; process management for running development servers, watchers, and background tasks; pre-commit hooks with automatic git integration; and tasks for defining build steps and their dependencies.
devenv pulls from the 100,000+ package Nixpkgs repository, supporting Linux (x64, ARM64), macOS (Intel, Apple Silicon), and WSL2. Every environment is hermetic and reproducible — the same devenv.nix produces the same environment on any machine. Lock files track exact package versions, and devenv update handles controlled dependency bumps.
Installation requires only the Nix package manager. devenv itself is available via nix profile install or the cachix binary cache. The project is actively maintained with regular releases, comprehensive documentation at devenv.sh, and supports composing environments from remote configurations via --from flags for organizational sharing.
Typical use cases include onboarding new developers instantly (no manual setup), CI/CD environments that match local development exactly, polyglot projects with complex dependency graphs, and teams that need guaranteed reproducibility across macOS and Linux workstations.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/devenv-declarative-developer-environments-nix/)
