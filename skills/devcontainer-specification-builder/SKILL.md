---
title: "Devcontainer Specification Builder"
description: "Generates dev container specifications with feature composition and lifecycle hooks. Uses the Dev Container Specification API, OCI feature registry, and devcontainer CLI for container-based development environments."
slug: "devcontainer-specification-builder"
category:
  - "Developer Tools"
framework:
  - "Claude Agents"
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/devcontainer-specification-builder/"
listed: true
---

# Devcontainer Specification Builder

Generates dev container specifications with feature composition and lifecycle hooks. Uses the Dev Container Specification API, OCI feature registry, and devcontainer CLI for container-based development environments.

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
clawhub install devcontainer-specification-builder
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Devcontainer Specification Builder creates comprehensive .devcontainer/devcontainer.json configurations following the official Dev Container Specification. It composes development environments using OCI-compliant Dev Container Features from ghcr.io registries and custom feature repositories.
The agent generates complete container configurations with image selection, Dockerfile composition, and Docker Compose integration for multi-service development stacks. It configures lifecycle hooks including onCreateCommand, updateContentCommand, postCreateCommand, and postStartCommand for environment initialization sequences.
Advanced features include VS Code extension recommendation via customizations.vscode.extensions, port forwarding configuration with label and onAutoForward settings, and mount definitions for persistent volumes. The agent also supports Dev Container Templates for project-type presets, Feature dependency resolution with installsAfter ordering, and GitHub Codespaces optimization with hostRequirements for CPU, memory, and GPU specifications. Integrates with the devcontainer CLI for local build validation and prebuild image publishing.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/devcontainer-specification-builder/)
