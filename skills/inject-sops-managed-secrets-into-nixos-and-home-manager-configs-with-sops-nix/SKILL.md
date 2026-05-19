---
name: "Inject SOPS-managed secrets into NixOS and Home Manager configs with sops-nix"
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

Requirements and caveats from upstream:
- This will otherwise cause sops to require multiple keys (shamir secret sharing)
- The easiest way to add new machines is by using SSH host keys (this requires OpenSSH to be enabled).
- The home-manager module requires systemd/user as it runs a service called sops-nix.service rather than an activation script.

Basic usage or getting-started notes:
- There is a configuration.nix example in the [deployment step](#deploy-example) of our usage example.
- If you prefer video over the textual description below, you can also checkout this [6min tutorial](https://www.youtube.com/watch?v=G5f6GC7SnhU) by [@vimjoyer](https://github.com/vimjoyer).
- <details>

- Source: https://github.com/Mic92/sops-nix
- Extracted from upstream docs: https://raw.githubusercontent.com/Mic92/sops-nix/HEAD/README.md

## Documentation

- https://github.com/Mic92/sops-nix#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/inject-sops-managed-secrets-into-nixos-and-home-manager-configs-with-sops-nix/)
