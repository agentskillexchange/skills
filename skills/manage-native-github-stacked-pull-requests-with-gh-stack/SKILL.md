---
title: "Manage native GitHub stacked pull requests with gh-stack"
slug: "manage-native-github-stacked-pull-requests-with-gh-stack"
description: "Teach coding agents to split large changes into native GitHub stacked pull requests, keep branch layers rebased, and submit focused reviewable PR chains with the gh stack CLI."
github_stars: 401
verification: "security_reviewed"
source: "https://github.com/github/gh-stack"
author: "GitHub"
publisher_type: "first_party_open_source"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "github/gh-stack"
  github_stars: 401
---

# Manage native GitHub stacked pull requests with gh-stack

Teach coding agents to split large changes into native GitHub stacked pull requests, keep branch layers rebased, and submit focused reviewable PR chains with the gh stack CLI.

## Prerequisites

GitHub CLI 2.0+, gh-stack extension, a GitHub repository with Stacked PRs enabled, and an AI coding agent that can use repository Git commands

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install GitHub CLI 2.0+ and run gh extension install github/gh-stack. For agent-aware setup, run gh skill install github/gh-stack in environments that support GitHub CLI skills. Use only on repositories where GitHub Stacked PRs has been enabled.
```

## Documentation

- https://gh.io/stacks

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/manage-native-github-stacked-pull-requests-with-gh-stack/)
