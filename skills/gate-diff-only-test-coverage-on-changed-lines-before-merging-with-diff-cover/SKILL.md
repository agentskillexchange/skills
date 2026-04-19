---
title: "Gate Diff Only Test Coverage On Changed Lines Before Merging With Diff Cover"
description: "diff-cover is a focused review-gate skill for checking whether newly changed lines are covered by tests, rather than judging whole-repository coverage. An agent should invoke it when a pull request needs a fast diff-only coverage decision before merge, especially in CI or review workflows where full coverage percentages hide risk on changed code. Use this instead of a general coverage dashboard when the real question is, &#8216;Did the lines we just changed get covered?&#8217; The boundary is precise: compare git diff output against Cobertura, Clover, JaCoCo, or LCov coverage reports and emit a patch-scoped result. It is not a general testing framework or product listing."
source: "https://github.com/Bachmann1234/diff_cover"
verification: "security_reviewed"
category:
  - "Code Quality &amp; Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "Bachmann1234/diff_cover"
  github_stars: 828
---

# Gate Diff Only Test Coverage On Changed Lines Before Merging With Diff Cover

diff-cover is a focused review-gate skill for checking whether newly changed lines are covered by tests, rather than judging whole-repository coverage. An agent should invoke it when a pull request needs a fast diff-only coverage decision before merge, especially in CI or review workflows where full coverage percentages hide risk on changed code. Use this instead of a general coverage dashboard when the real question is, &#8216;Did the lines we just changed get covered?&#8217; The boundary is precise: compare git diff output against Cobertura, Clover, JaCoCo, or LCov coverage reports and emit a patch-scoped result. It is not a general testing framework or product listing.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gate-diff-only-test-coverage-on-changed-lines-before-merging-with-diff-cover/)
