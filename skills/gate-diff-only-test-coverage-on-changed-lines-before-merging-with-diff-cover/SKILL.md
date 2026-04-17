---
title: "Gate Diff Only Test Coverage On Changed Lines Before Merging With Diff Cover"
description: "Compare coverage reports against a git diff so an agent can flag newly changed lines that still lack tests before merge."
verification: listed
source: "https://github.com/Bachmann1234/diff_cover"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "Bachmann1234/diff_cover"
  github_stars: 828
---

# Gate Diff Only Test Coverage On Changed Lines Before Merging With Diff Cover

diff-cover is a focused review-gate skill for checking whether newly changed lines are covered by tests, rather than judging whole-repository coverage. An agent should invoke it when a pull request needs a fast diff-only coverage decision before merge, especially in CI or review workflows where full coverage percentages hide risk on changed code.

Use this instead of a general coverage dashboard when the real question is, ‘Did the lines we just changed get covered?’ The boundary is precise: compare git diff output against Cobertura, Clover, JaCoCo, or LCov coverage reports and emit a patch-scoped result. It is not a general testing framework or product listing.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/gate-diff-only-test-coverage-on-changed-lines-before-merging-with-diff-cover
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/gate-diff-only-test-coverage-on-changed-lines-before-merging-with-diff-cover` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gate-diff-only-test-coverage-on-changed-lines-before-merging-with-diff-cover/)
