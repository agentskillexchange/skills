---
name: "Rewrite Git history to purge secrets, binaries, or accidental paths before sharing a repo"
slug: "rewrite-git-history-to-purge-secrets-binaries-or-accidental-paths-before-sharing-a-repo"
description: "Use git-filter-repo when an agent needs to surgically rewrite repository history after a leaked secret, a huge binary commit, or a bad subtree split. The agent analyzes the problem, builds the rewrite command, and leaves a clean follow-up checklist for force-push, clone reset, and downstream cleanup."
github_stars: 12127
verification: "listed"
source: "https://github.com/newren/git-filter-repo"
publisher_type: "individual_maintainer"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "newren/git-filter-repo"
  github_stars: 12127
---

# Rewrite Git history to purge secrets, binaries, or accidental paths before sharing a repo

Use git-filter-repo when an agent needs to surgically rewrite repository history after a leaked secret, a huge binary commit, or a bad subtree split. The agent analyzes the problem, builds the rewrite command, and leaves a clean follow-up checklist for force-push, clone reset, and downstream cleanup.

## Prerequisites

git >= 2.36.0, python3 >= 3.6

## Installation

Use the upstream install or setup path that matches your environment:
- git clone file://$(pwd) newcopy

Requirements and caveats from upstream:
- [Prerequisites](#prerequisites)
- filter-repo requires:
- is all contained in a single-file python script named

Basic usage or getting-started notes:
- [Simple example, with comparisons](#simple-example-with-comparisons)
- git >= 2.36.0
- python3 >= 3.6

- Source: https://github.com/newren/git-filter-repo
- Extracted from upstream docs: https://raw.githubusercontent.com/newren/git-filter-repo/HEAD/README.md

## Documentation

- https://github.com/newren/git-filter-repo

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rewrite-git-history-to-purge-secrets-binaries-or-accidental-paths-before-sharing-a-repo/)
