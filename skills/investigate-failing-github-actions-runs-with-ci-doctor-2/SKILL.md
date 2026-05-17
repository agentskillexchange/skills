---
name: "Investigate failing GitHub Actions runs with CI Doctor"
slug: "investigate-failing-github-actions-runs-with-ci-doctor-2"
description: "Use GitHub Next's CI Doctor workflow to watch GitHub Actions runs, pull failure logs, trace recurring patterns, and open investigation issues with concrete next steps. This is for agents acting as CI failure investigators, not for listing GitHub Agentic Workflows as a product."
verification: "security_reviewed"
source: "https://github.com/githubnext/agentics/blob/main/docs/ci-doctor.md"
author: "GitHub Next"
publisher_type: "Open source project"
category: "CI/CD Integrations"
framework: "Multi-Framework"
---

# Investigate failing GitHub Actions runs with CI Doctor

Use GitHub Next's CI Doctor workflow to watch GitHub Actions runs, pull failure logs, trace recurring patterns, and open investigation issues with concrete next steps. This is for agents acting as CI failure investigators, not for listing GitHub Agentic Workflows as a product.

## Prerequisites

GitHub, GitHub Actions, gh, GitHub Agentic Workflows extension, AI provider token supported by gh-aw

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install gh-aw with gh extension install github/gh-aw, then add githubnext/agentics/ci-doctor to your repository and compile the workflow.
```

## Documentation

- https://raw.githubusercontent.com/githubnext/agentics/main/docs/ci-doctor.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/investigate-failing-github-actions-runs-with-ci-doctor-2/)
