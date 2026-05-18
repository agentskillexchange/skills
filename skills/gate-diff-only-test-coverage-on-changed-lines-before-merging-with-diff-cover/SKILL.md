---
name: "Gate Diff Only Test Coverage On Changed Lines Before Merging With Diff Cover"
slug: "gate-diff-only-test-coverage-on-changed-lines-before-merging-with-diff-cover"
description: "Compare coverage reports against a git diff so an agent can flag newly changed lines that still lack tests before merge."
github_stars: 828
verification: "security_reviewed"
source: "https://github.com/Bachmann1234/diff_cover"
author: "Matthias Bachmann and contributors"
publisher_type: "Open Source"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "Bachmann1234/diff_cover"
  github_stars: 828
---

# Gate Diff Only Test Coverage On Changed Lines Before Merging With Diff Cover

Compare coverage reports against a git diff so an agent can flag newly changed lines that still lack tests before merge.

## Prerequisites

Git, supported XML or LCov coverage report, Python 3, pip

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
pip install diff-cover
```

## Documentation

- https://github.com/Bachmann1234/diff_cover

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gate-diff-only-test-coverage-on-changed-lines-before-merging-with-diff-cover/)
