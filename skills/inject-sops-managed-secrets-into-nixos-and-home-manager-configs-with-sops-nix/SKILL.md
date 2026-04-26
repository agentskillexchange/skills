---
title: "Inject SOPS-managed secrets into NixOS and Home Manager configs with sops-nix"
description: "Materialize age or PGP encrypted SOPS secrets inside declarative NixOS and Home Manager systems during activation without hand-copying values."
verification: "listed"
source: "https://github.com/Mic92/sops-nix"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "Mic92/sops-nix"
  github_stars: 2771
---

# Inject SOPS-managed secrets into NixOS and Home Manager configs with sops-nix

Use sops-nix when an agent needs to wire encrypted SOPS secrets into NixOS or Home Manager configurations so they are decrypted and materialized at activation time. A user should invoke this instead of using SOPS by itself when the job is declarative Nix secret integration and deployment, not generic secret file editing or encryption. The scope boundary is clear and skill-shaped: NixOS and Home Manager secret injection from SOPS-managed inputs, not a general secret management product card.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/inject-sops-managed-secrets-into-nixos-and-home-manager-configs-with-sops-nix/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/inject-sops-managed-secrets-into-nixos-and-home-manager-configs-with-sops-nix
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/inject-sops-managed-secrets-into-nixos-and-home-manager-configs-with-sops-nix`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/inject-sops-managed-secrets-into-nixos-and-home-manager-configs-with-sops-nix/)
