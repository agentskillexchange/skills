---
title: "Review open pull requests against repository contribution guidelines"
description: "This entry turns GitHub Next's Contribution Check workflow into a maintainer-facing agent routine. The agent batches open pull requests, compares them to CONTRIBUTING.md, labels likely-ready submissions, comments on gaps, and produces a report issue so humans can spend review time where it matters."
verification: "security_reviewed"
source: "https://github.com/githubnext/agentics/blob/main/docs/contribution-check.md"
author: "GitHub Next"
publisher_type: "Open Source Project"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
---

# Review open pull requests against repository contribution guidelines

This entry turns GitHub Next's Contribution Check workflow into a maintainer-facing agent routine. The agent batches open pull requests, compares them to CONTRIBUTING.md, labels likely-ready submissions, comments on gaps, and produces a report issue so humans can spend review time where it matters.

## Prerequisites

GitHub CLI, the gh-aw extension, and a repository with CONTRIBUTING.md

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
gh extension install github/gh-aw && gh aw add-wizard githubnext/agentics/contribution-check
```

## Documentation

- https://github.com/githubnext/agentics/blob/main/docs/contribution-check.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/review-open-pull-requests-against-repository-contribution-guidelines/)
