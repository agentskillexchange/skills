---
name: "Manage native GitHub stacked pull requests with gh-stack"
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

Requirements and caveats from upstream:
- Requires the [GitHub CLI](https://cli.github.com/) (gh) v2.0+.
- | -n, --numbered | Use auto-incrementing numbered branch names (requires --prefix) |
- Creates a new branch at the current HEAD, adds it to the top of the stack, and checks it out. Must be run while on the topmost branch of a stack. If no branch name is given, prompts for one.

Basic usage or getting-started notes:
- sh
- gh extension install github/gh-stack
- ## AI agent integration

- Source: https://github.com/github/gh-stack
- Extracted from upstream docs: https://raw.githubusercontent.com/github/gh-stack/HEAD/README.md

## Documentation

- https://gh.io/stacks

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/manage-native-github-stacked-pull-requests-with-gh-stack/)
