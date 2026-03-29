---
name: "Devcontainer Specification Builder"
description: "Generates dev container specifications with feature composition and lifecycle hooks. Uses the Dev Container Specification API, OCI feature registry, and devcontainer CLI for container-based development environments."
category: "Developer Tools"
framework: "Claude Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/devcontainer-specification-builder/"
tool_ecosystem:
  tool: docker
  github_stars: 71560
  github_repo: moby/moby
  license: Apache-2.0
  maintained: true
---
# Devcontainer Specification Builder

Generates dev container specifications with feature composition and lifecycle hooks. Uses the Dev Container Specification API, OCI feature registry, and devcontainer CLI for container-based development environments.

## Overview

The Devcontainer Specification Builder creates comprehensive .devcontainer/devcontainer.json configurations following the official Dev Container Specification. It composes development environments using OCI-compliant Dev Container Features from ghcr.io registries and custom feature repositories.

The agent generates complete container configurations with image selection, Dockerfile composition, and Docker Compose integration for multi-service development stacks. It configures lifecycle hooks including onCreateCommand, updateContentCommand, postCreateCommand, and postStartCommand for environment initialization sequences.

Advanced features include VS Code extension recommendation via customizations.vscode.extensions, port forwarding configuration with label and onAutoForward settings, and mount definitions for persistent volumes. The agent also supports Dev Container Templates for project-type presets, Feature dependency resolution with installsAfter ordering, and GitHub Codespaces optimization with hostRequirements for CPU, memory, and GPU specifications. Integrates with the devcontainer CLI for local build validation and prebuild image publishing.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill devcontainer-specification-builder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill devcontainer-specification-builder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill devcontainer-specification-builder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill devcontainer-specification-builder -a codex
```

### OpenClaw

```bash
clawhub install devcontainer-specification-builder
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/devcontainer-specification-builder/)
