---
title: "Pin CI workflow actions and images with Ratchet"
description: "Audit and rewrite CI/CD workflow references so agents can pin mutable actions, containers, and images to immutable versions before changes land."
verification: "security_reviewed"
source: "https://github.com/sethvargo/ratchet"
author: "Seth Vargo"
publisher_type: "open_source"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "sethvargo/ratchet"
  github_stars: 928
---

# Pin CI workflow actions and images with Ratchet

Audit and rewrite CI/CD workflow references so agents can pin mutable actions, containers, and images to immutable versions before changes land.

## Prerequisites

Ratchet CLI; repository CI YAML files; optional GITHUB_TOKEN for private GitHub resolution

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with Homebrew (`brew install ratchet`), download a release binary, run the container image, use Nix, or install with `go install github.com/sethvargo/ratchet@latest`; then run `ratchet lint`, `ratchet pin`, `ratchet update`, or `ratchet upgrade` against workflow YAML.
```

## Documentation

- https://github.com/sethvargo/ratchet

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pin-ci-workflow-actions-and-images-with-ratchet/)
