---
name: "Monitor one pull request through CI and review with Tstack babysit-pr"
slug: "monitor-pull-request-ci-review-tstack-babysit-pr"
description: "Watch a single owned pull request, verify new review findings, fix real CI failures, and return a current readiness handoff without implicit merge permission."
verification: "security_reviewed"
source: "https://github.com/t3dotgg/tstack/tree/main/skills/babysit-pr"
author: "t3dotgg"
publisher_type: "individual"
category: "CI/CD Integrations"
framework: "Multi-Framework"
---

# Monitor one pull request through CI and review with Tstack babysit-pr

Watch a single owned pull request, verify new review findings, fix real CI failures, and return a current readiness handoff without implicit merge permission.

## Prerequisites

Git, authenticated GitHub CLI (gh), Python 3, shell access, and a skill-capable Claude Code or Codex runtime

## Installation

Install or set up from the source-backed instructions:

Clone https://github.com/t3dotgg/tstack with git clone. For Claude Code, create ~/.claude/skills with mkdir -p, then copy tstack/skills/babysit-pr and tstack/skills/leaving-pr-comments into that directory with cp -R. For Codex, use mkdir -p ~/.codex/skills and copy the same two directories there. Preserve the bundled scripts directory. Invoke by asking to monitor, watch, or babysit a specific PR; use the absolute installed babysit-pr/scripts/pr-wait path outside T3 Code. No other Tstack skills or multi-model providers are required for this scoped workflow.

- Source: https://github.com/t3dotgg/tstack/tree/main/skills/babysit-pr

## Documentation

- https://github.com/t3dotgg/tstack/blob/main/skills/babysit-pr/SKILL.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/monitor-pull-request-ci-review-tstack-babysit-pr/)
