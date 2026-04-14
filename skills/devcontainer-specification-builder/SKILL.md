---
title: "Devcontainer Specification Builder"
description: "Generates dev container specifications with feature composition and lifecycle hooks. Uses the Dev Container Specification API, OCI feature registry, and devcontainer CLI for container-based development environments."
verification: security_reviewed
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/devcontainer-specification-builder/)
