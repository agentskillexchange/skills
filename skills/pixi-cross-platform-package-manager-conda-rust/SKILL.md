---
name: "Pixi Cross-Platform Package Manager Built on Conda"
description: "A blazing-fast, cross-platform package manager and workflow tool written in Rust. Pixi builds on the Conda ecosystem to provide reproducible, multi-language dependency management with a Cargo-like developer experience for Python, C++, R, and more."
category: "Developer Tools"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/pixi-cross-platform-package-manager-conda-rust/"
---

# Pixi Cross-Platform Package Manager Built on Conda

A blazing-fast, cross-platform package manager and workflow tool written in Rust. Pixi builds on the Conda ecosystem to provide reproducible, multi-language dependency management with a Cargo-like developer experience for Python, C++, R, and more.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill pixi-cross-platform-package-manager-conda-rust
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pixi-cross-platform-package-manager-conda-rust -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pixi-cross-platform-package-manager-conda-rust -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pixi-cross-platform-package-manager-conda-rust -a codex
```

### OpenClaw

```bash
clawhub install pixi-cross-platform-package-manager-conda-rust
```

## Overview

Pixi is a modern package manager from prefix.dev, written entirely in Rust, that brings the reproducibility of the Conda ecosystem together with the ergonomics of tools like Cargo and npm. It manages project dependencies, virtual environments, and task execution across Python, C++, R, CUDA, and other languages through a single pixi.toml configuration file.

The core commands mirror familiar workflows: pixi init creates a new project, pixi add numpy adds a dependency, pixi install locks and installs all dependencies, and pixi run executes tasks in the project environment. Every project gets an automatically maintained lock file (pixi.lock) that pins exact package versions and hashes for full reproducibility.

Key differentiators include: multi-language support for Python, C++, R, Fortran, CUDA, and system libraries from the conda-forge repository containing 30,000+ packages; cross-platform environments with native support for Linux, macOS (Intel and Apple Silicon), and Windows without containers; PyPI integration allowing mixed conda and pip dependencies in the same project; and global tool installation via pixi global install for system-wide CLI tools.

Built on the rattler library, Pixi achieves fast dependency resolution through a SAT solver and parallel downloads. It supports conda channels, PyPI indices, and custom package repositories.
