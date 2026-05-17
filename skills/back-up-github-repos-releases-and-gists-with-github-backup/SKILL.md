---
name: "Back up GitHub repos releases and gists with GitHub Backup"
slug: "back-up-github-repos-releases-and-gists-with-github-backup"
description: "Use GitHub Backup when an agent needs to mirror repositories, release assets, and gists into local storage on a schedule, instead of manually exporting GitHub content repo by repo."
github_stars: 33
verification: "security_reviewed"
source: "https://github.com/SierraSoftworks/github-backup"
author: "Sierra Softworks"
publisher_type: "open_source_project"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "SierraSoftworks/github-backup"
  github_stars: 33
---

# Back up GitHub repos releases and gists with GitHub Backup

Use GitHub Backup when an agent needs to mirror repositories, release assets, and gists into local storage on a schedule, instead of manually exporting GitHub content repo by repo.

## Prerequisites

GitHub Backup binary or container image, GitHub token, local or mounted backup storage

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install the GitHub Backup binary or use the published container image, create a YAML config with your GitHub token and backup targets, then run `github-backup --config config.yaml` on demand or from a scheduler.
```

## Documentation

- https://github.com/SierraSoftworks/github-backup

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/back-up-github-repos-releases-and-gists-with-github-backup/)
