---
title: "Inject SOPS-managed secrets into NixOS and Home Manager configs with sops-nix"
slug: "inject-sops-managed-secrets-into-nixos-and-home-manager-configs-with-sops-nix"
description: "Materialize age or PGP encrypted SOPS secrets inside declarative NixOS and Home Manager systems during activation without hand-copying values."
github_stars: 2771
verification: "security_reviewed"
source: "https://github.com/Mic92/sops-nix"
author: "Mic92"
publisher_type: "individual"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "Mic92/sops-nix"
  github_stars: 2771
---

# Inject SOPS-managed secrets into NixOS and Home Manager configs with sops-nix

Materialize age or PGP encrypted SOPS secrets inside declarative NixOS and Home Manager systems during activation without hand-copying values.

## Prerequisites

NixOS or Home Manager configuration, sops-nix module, SOPS-encrypted secret files, age or PGP keys, Nix build and activation access

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Add sops-nix to the target NixOS or Home Manager configuration per the upstream module instructions, configure SOPS and the decryption keys, then define the secrets to materialize during activation or user environment setup.
```

## Documentation

- https://github.com/Mic92/sops-nix#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/inject-sops-managed-secrets-into-nixos-and-home-manager-configs-with-sops-nix/)
