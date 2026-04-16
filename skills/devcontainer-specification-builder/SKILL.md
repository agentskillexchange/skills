---
title: "Devcontainer Specification Builder"
description: "Generates dev container specifications with feature composition and lifecycle hooks. Uses the Dev Container Specification API, OCI feature registry, and devcontainer CLI for container-based development environments."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/devcontainer-specification-builder/"
category:
  - "Developer Tools"
framework:
  - "Claude Agents"
  - "Multi-Framework"
---

# Devcontainer Specification Builder

The Devcontainer Specification Builder creates comprehensive .devcontainer/devcontainer.json configurations following the official Dev Container Specification. It composes development environments using OCI-compliant Dev Container Features from ghcr.io registries and custom feature repositories.

The agent generates complete container configurations with image selection, Dockerfile composition, and Docker Compose integration for multi-service development stacks. It configures lifecycle hooks including onCreateCommand, updateContentCommand, postCreateCommand, and postStartCommand for environment initialization sequences.

Advanced features include VS Code extension recommendation via customizations.vscode.extensions, port forwarding configuration with label and onAutoForward settings, and mount definitions for persistent volumes. The agent also supports Dev Container Templates for project-type presets, Feature dependency resolution with installsAfter ordering, and GitHub Codespaces optimization with hostRequirements for CPU, memory, and GPU specifications. Integrates with the devcontainer CLI for local build validation and prebuild image publishing.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/devcontainer-specification-builder/)
