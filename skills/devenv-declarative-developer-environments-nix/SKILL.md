---
name: "devenv Declarative Developer Environments with Nix"
slug: "devenv-declarative-developer-environments-nix"
description: "A fast, declarative, and reproducible developer environment tool built on Nix. devenv lets teams define project dependencies, services, scripts, and language toolchains in a single configuration file, ensuring consistent environments across machines."
github_stars: 6614
verification: "security_reviewed"
source: "https://github.com/cachix/devenv"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "cachix/devenv"
  github_stars: 6614
---

# devenv Declarative Developer Environments with Nix

A fast, declarative, and reproducible developer environment tool built on Nix. devenv lets teams define project dependencies, services, scripts, and language toolchains in a single configuration file, ensuring consistent environments across machines.

## Installation

Requirements and caveats from upstream:
- **[OCI containers](https://devenv.sh/containers/)** built from your environment without Docker
- # python-app = config.languages.python.import ./python-app {};
- --option languages.python.version:string 3.10

Basic usage or getting-started notes:
- Running devenv init generates devenv.nix:
- nix
- { pkgs, lib, config, inputs, ... }:

- Source: https://github.com/cachix/devenv
- Extracted from upstream docs: https://raw.githubusercontent.com/cachix/devenv/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/devenv-declarative-developer-environments-nix/)
