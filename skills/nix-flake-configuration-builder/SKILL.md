---
name: "Nix Flake Configuration Builder"
description: "Generates reproducible Nix flake configurations with devShell environments and package overlays. Uses the Nix Flakes API, nixpkgs lib functions, and flake-utils for cross-platform builds."
category: "Developer Tools"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/nix-flake-configuration-builder/"
---
# Nix Flake Configuration Builder

Generates reproducible Nix flake configurations with devShell environments and package overlays. Uses the Nix Flakes API, nixpkgs lib functions, and flake-utils for cross-platform builds.

## Overview

The Nix Flake Configuration Builder creates fully reproducible development environments and package definitions using the Nix Flakes system. It generates flake.nix files with properly structured inputs, outputs, and overlay definitions using the nixpkgs.lib utility functions.

The agent supports devShell creation with automatic dependency detection, leveraging pkgs.mkShell and shellHook configuration for project-specific environment setup. It generates flake-utils eachDefaultSystem mappings for cross-platform compatibility across x86_64-linux, aarch64-linux, and x86_64-darwin targets.

Key features include overlay composition using nixpkgs.overlays for package customization, NixOS module generation with options and config attribute sets, and home-manager integration for user-level configuration. The agent also configures binary cache settings via nix.conf substituters and trusted-public-keys, and generates CI-ready configurations with cachix push integration for build artifact sharing.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill nix-flake-configuration-builder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill nix-flake-configuration-builder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill nix-flake-configuration-builder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill nix-flake-configuration-builder -a codex
```

### OpenClaw

```bash
clawhub install nix-flake-configuration-builder
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nix-flake-configuration-builder/)
