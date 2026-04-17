---
name: Post linter and analyzer findings back into pull requests
description: This ASE skill uses reviewdog to turn linter and analyzer output into
  diff-aware pull request feedback. An agent can run existing checks, filter findings
  to the changed lines, and publish inline review comments or annotations instead
  of dumping raw logs into CI.
category: Code Quality & Review
framework: Multi-Framework
verification: security_reviewed
source: https://github.com/reviewdog/reviewdog
tool_ecosystem:
  github_repo: reviewdog/reviewdog
  github_stars: 9207
  tool: reviewdog
---
# Post linter and analyzer findings back into pull requests
This ASE skill uses reviewdog to turn linter and analyzer output into diff-aware pull request feedback. An agent can run existing checks, filter findings to the changed lines, and publish inline review comments or annotations instead of dumping raw logs into CI.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/post-linter-and-analyzer-findings-back-into-pull-requests
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/post-linter-and-analyzer-findings-back-into-pull-requests` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/post-linter-and-analyzer-findings-back-into-pull-requests/)
