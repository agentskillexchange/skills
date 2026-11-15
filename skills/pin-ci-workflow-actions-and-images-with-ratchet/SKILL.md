---
name: "Pin CI workflow actions and images with Ratchet"
slug: "pin-ci-workflow-actions-and-images-with-ratchet"
description: "Audit and rewrite CI/CD workflow references so agents can pin mutable actions, containers, and images to immutable versions before changes land."
github_stars: 928
verification: "security_reviewed"
source: "https://github.com/sethvargo/ratchet"
author: "Seth Vargo"
publisher_type: "open_source"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "sethvargo/ratchet"
  github_stars: 928
---

# Pin CI workflow actions and images with Ratchet

Audit and rewrite CI/CD workflow references so agents can pin mutable actions, containers, and images to immutable versions before changes land.

## Prerequisites

Ratchet CLI; repository CI YAML files; optional GITHUB_TOKEN for private GitHub resolution

## Installation

Use the upstream install or setup path that matches your environment:
- Cargo, Go modules, NPM, Pip, or Yarn, but for CI/CD workflows. Ratchet supports:
- Docker tags are mutable. This poses a substantial security and reliability risk.
- brew install ratchet
- go install github.com/sethvargo/ratchet@latest

Requirements and caveats from upstream:
- Compiled from source yourself. Note this option is not supported.
- container or Docker-based references.

Basic usage or getting-started notes:
- There are a few options for installing ratchet:
- Via homebrew:
- sh

- Source: https://github.com/sethvargo/ratchet
- Extracted from upstream docs: https://raw.githubusercontent.com/sethvargo/ratchet/HEAD/README.md

## Documentation

- https://github.com/sethvargo/ratchet

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pin-ci-workflow-actions-and-images-with-ratchet/)
