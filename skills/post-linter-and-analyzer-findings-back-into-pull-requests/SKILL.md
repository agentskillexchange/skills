---
title: "Post linter and analyzer findings back into pull requests"
description: "This ASE skill uses reviewdog to turn linter and analyzer output into diff-aware pull request feedback. An agent can run existing checks, filter findings to the changed lines, and publish inline review comments or annotations instead of dumping raw logs into CI."
verification: "security_reviewed"
source: "https://github.com/reviewdog/reviewdog"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "reviewdog/reviewdog"
  github_stars: 9207
---

# Post linter and analyzer findings back into pull requests

This ASE skill is built around reviewdog, the open source automation tool from the reviewdog project for routing lint and analysis results into code review surfaces. The agent behavior is narrow and useful: run one or more existing analyzers, collect their findings, map them to the current diff, and post them back into a pull request as inline comments, annotations, or status checks. That makes the entry skill-shaped instead of a plain tool card, because the job is not “use reviewdog” in the abstract. The job is to take already-generated diagnostics and deliver them to the exact review context where a human or agent is deciding whether to merge. Invoke this when an agent has modified code, opened or reviewed a pull request, or is coordinating CI checks and wants actionable feedback in the review itself. reviewdog supports multiple input formats, including errorformat-style diagnostics, Checkstyle, SARIF, and reviewdog’s own diagnostic format, so it works well as the feedback layer on top of linters, type checkers, security scanners, and custom analyzers. It can report locally against git diff output or inside GitHub Actions, GitLab CI, Bitbucket, and other automation contexts. The scope boundary matters. This skill does not replace the linter, the test runner, or the hosting platform. It only handles diff-aware review reporting and suggestion delivery. Integration points include GitHub Actions reporters, GitLab merge request reporters, local git diff filtering, and any analyzer that can emit machine-readable results. If you need inline review feedback rather than another wall of CI text, this is the right job for an agent to invoke.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/post-linter-and-analyzer-findings-back-into-pull-requests/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/post-linter-and-analyzer-findings-back-into-pull-requests
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/post-linter-and-analyzer-findings-back-into-pull-requests`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/post-linter-and-analyzer-findings-back-into-pull-requests/)
