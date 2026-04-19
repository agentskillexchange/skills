---
title: "Devcontainer Specification Builder"
description: "The Devcontainer Specification Builder creates comprehensive .devcontainer/devcontainer.json configurations following the official Dev Container Specification. It composes development environments using OCI-compliant Dev Container Features from ghcr.io registries and custom feature repositories. The agent generates complete container configurations with image selection, Dockerfile composition, and Docker Compose integration for multi-service development stacks. It configures lifecycle hooks including onCreateCommand, updateContentCommand, postCreateCommand, and postStartCommand for environment initialization sequences. Advanced features include VS Code extension recommendation via customizations.vscode.extensions, port forwarding configuration with label and onAutoForward settings, and mount definitions for persistent volumes. The agent also supports Dev Container Templates for project-type presets, Feature dependency resolution with installsAfter ordering, and GitHub Codespaces optimization with hostRequirements for CPU, memory, and GPU specifications. Integrates with the devcontainer CLI for local build validation and prebuild image publishing."
source: "https://agentskillexchange.com/skills/devcontainer-specification-builder/"
verification: "security_reviewed"
category:
  - "Developer Tools"
framework:
  - "Claude Agents"
  - "Multi-Framework"
---

# Devcontainer Specification Builder

The Devcontainer Specification Builder creates comprehensive .devcontainer/devcontainer.json configurations following the official Dev Container Specification. It composes development environments using OCI-compliant Dev Container Features from ghcr.io registries and custom feature repositories. The agent generates complete container configurations with image selection, Dockerfile composition, and Docker Compose integration for multi-service development stacks. It configures lifecycle hooks including onCreateCommand, updateContentCommand, postCreateCommand, and postStartCommand for environment initialization sequences. Advanced features include VS Code extension recommendation via customizations.vscode.extensions, port forwarding configuration with label and onAutoForward settings, and mount definitions for persistent volumes. The agent also supports Dev Container Templates for project-type presets, Feature dependency resolution with installsAfter ordering, and GitHub Codespaces optimization with hostRequirements for CPU, memory, and GPU specifications. Integrates with the devcontainer CLI for local build validation and prebuild image publishing.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/devcontainer-specification-builder/)
