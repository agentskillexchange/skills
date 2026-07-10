---
title: "Generate structured release notes from merged pull requests between two refs with Copilot Release Notes"
description: "Compare two tags, branches, or SHAs and turn merged pull requests into reviewable markdown and JSON release notes for a release workflow."
verification: "security_reviewed"
source: "https://github.com/github/copilot-release-notes"
author: "GitHub"
publisher_type: "organization"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "github/copilot-release-notes"
  github_stars: 2
---

# Generate structured release notes from merged pull requests between two refs with Copilot Release Notes

Compare two tags, branches, or SHAs and turn merged pull requests into reviewable markdown and JSON release notes for a release workflow.

## Prerequisites

GitHub Actions runner, checked-out git history for the compared refs, GitHub Copilot license, fine-grained PAT with Copilot Requests read permission

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Add the documented action to a GitHub Actions workflow, provide base-ref and head-ref, configure the COPILOT_GITHUB_TOKEN secret, then consume the generated markdown or JSON outputs in the release pipeline.
```

## Documentation

- https://github.com/github/copilot-release-notes

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-structured-release-notes-from-merged-pull-requests-between-two-refs-with-copilot-release-notes/)
