---
name: "Git Bisect Automator"
slug: "git-bisect-automator"
description: "Automates git bisect workflows with custom test scripts and CI pipeline integration. Uses the Git CLI and GitHub Actions API to identify regression-introducing commits across large repositories."
verification: "listed"
source: "https://git-scm.com/docs/git-bisect"
category: "Developer Tools"
framework: "Claude Code"
---

# Git Bisect Automator

Automates git bisect workflows with custom test scripts and CI pipeline integration. Uses the Git CLI and GitHub Actions API to identify regression-introducing commits across large repositories.

## Installation

Use the upstream install or setup path that matches your environment:
- $ git bisect run make # "make" builds the app
- $ git bisect run make test # "make test" builds and tests
- make || exit 125 # this skips broken builds
- make and test processes and the scripts.

Requirements and caveats from upstream:
- To use "old" and "new" instead of "good" and bad, you must run git
- does not require a checked out tree.

Basic usage or getting-started notes:
- Community
- Table of Contents
- NAME

- Source: https://git-scm.com/docs/git-bisect

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-bisect-automator/)
