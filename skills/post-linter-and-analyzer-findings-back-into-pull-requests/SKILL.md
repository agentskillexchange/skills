---
title: "Post linter and analyzer findings back into pull requests"
slug: "post-linter-and-analyzer-findings-back-into-pull-requests"
description: "This ASE skill uses reviewdog to turn linter and analyzer output into diff-aware pull request feedback. An agent can run existing checks, filter findings to the changed lines, and publish inline review comments or annotations instead of dumping raw logs into CI."
github_stars: 9207
verification: "security_reviewed"
source: "https://github.com/reviewdog/reviewdog"
author: "reviewdog"
publisher_type: "Open Source Project"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "reviewdog/reviewdog"
  github_stars: 9207
---

# Post linter and analyzer findings back into pull requests

This ASE skill uses reviewdog to turn linter and analyzer output into diff-aware pull request feedback. An agent can run existing checks, filter findings to the changed lines, and publish inline review comments or annotations instead of dumping raw logs into CI.

## Prerequisites

One or more linters or analyzers that emit machine-readable diagnostics, plus local git diff or CI pull request context

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
brew install reviewdog/tap/reviewdog
```

## Documentation

- https://github.com/reviewdog/reviewdog/blob/master/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/post-linter-and-analyzer-findings-back-into-pull-requests/)
