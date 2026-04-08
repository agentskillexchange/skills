---
title: Devcontainer Specification Builder
description: The Devcontainer Specification Builder creates comprehensive .devcontainer/devcontainer.json
  configurations following the official Dev Container Specification. It composes development
  environments using OCI-compliant Dev Container Features from ghcr.io registries
  and custom feature repositories. The agent generates complete container configurations
  with image selection, Dockerfile composition, and Docker Compose integration for
  multi-service development stacks. It configures lifecycle hooks including onCreateCommand,
  updateContentCommand, postCreateCommand, and postStartCommand for environment initialization
  sequences. Advanced features include VS Code extension recommendation via customizations.vscode.extensions,
  port forwarding configuration with label and onAutoForward settings, and mount definitions
  for persistent volumes. The agent also supports Dev Container Templates for project-type
  presets, Feature dependency resolution with installsAfter ordering, and GitHub Codespaces
  optimization with hostRequirements for CPU, memory, and GPU specifications. Integrates
  with the devcontainer CLI for local build validation and prebuild image publishing.
verification: security_reviewed
source: https://agentskillexchange.com/skills/devcontainer-specification-builder/
category:
- Developer Tools
framework:
- Claude Agents
- Multi-Framework
---

# Devcontainer Specification Builder

The Devcontainer Specification Builder creates comprehensive .devcontainer/devcontainer.json configurations following the official Dev Container Specification. It composes development environments using OCI-compliant Dev Container Features from ghcr.io registries and custom feature repositories. The agent generates complete container configurations with image selection, Dockerfile composition, and Docker Compose integration for multi-service development stacks. It configures lifecycle hooks including onCreateCommand, updateContentCommand, postCreateCommand, and postStartCommand for environment initialization sequences. Advanced features include VS Code extension recommendation via customizations.vscode.extensions, port forwarding configuration with label and onAutoForward settings, and mount definitions for persistent volumes. The agent also supports Dev Container Templates for project-type presets, Feature dependency resolution with installsAfter ordering, and GitHub Codespaces optimization with hostRequirements for CPU, memory, and GPU specifications. Integrates with the devcontainer CLI for local build validation and prebuild image publishing.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/devcontainer-specification-builder/)
