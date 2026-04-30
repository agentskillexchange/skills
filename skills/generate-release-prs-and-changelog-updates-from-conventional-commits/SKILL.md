---
title: "Generate release PRs and changelog updates from Conventional Commits"
description: "Use release-please when an agent should turn merged Conventional Commits into structured release PRs, version bumps, and changelog updates before a human reviews and merges. This is a release-management workflow, not a generic package or CI listing."
verification: "security_reviewed"
source: "https://github.com/googleapis/release-please"
author: "Google APIs"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "googleapis/release-please"
  github_stars: 6700
---

# Generate release PRs and changelog updates from Conventional Commits

Use release-please when an agent should turn merged Conventional Commits into structured release PRs, version bumps, and changelog updates before a human reviews and merges. This is a release-management workflow, not a generic package or CI listing.

## Prerequisites

GitHub, Conventional Commits

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install release-please via npm or use the GitHub integration, configure release-please in the repository, then let it open release PRs from commit history.
```

## Documentation

- https://github.com/googleapis/release-please

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-release-prs-and-changelog-updates-from-conventional-commits/)
