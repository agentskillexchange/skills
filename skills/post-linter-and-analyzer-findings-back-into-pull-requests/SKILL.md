---
title: "Post linter and analyzer findings back into pull requests"
description: "This ASE skill uses reviewdog to turn linter and analyzer output into diff-aware pull request feedback. An agent can run existing checks, filter findings to the changed lines, and publish inline review comments or annotations instead of dumping raw logs into CI."
verification: security_reviewed
source: "https://github.com/reviewdog/reviewdog"
tool_ecosystem:
  github_repo: "reviewdog/reviewdog"
  github_stars: 9204
---

# Post linter and analyzer findings back into pull requests

This ASE skill uses reviewdog to turn linter and analyzer output into diff-aware pull request feedback. An agent can run existing checks, filter findings to the changed lines, and publish inline review comments or annotations instead of dumping raw logs into CI.

## Installation

Choose the path that fits your setup:

1. Clone this repository and use the skill locally.
2. Copy the skill folder into your local skills directory.
3. Add the skill as a Git submodule in your skills workspace.
4. Vendor the files into an internal skill catalog for your team.
5. Reference the upstream source and recreate the skill in your own agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/post-linter-and-analyzer-findings-back-into-pull-requests/)
