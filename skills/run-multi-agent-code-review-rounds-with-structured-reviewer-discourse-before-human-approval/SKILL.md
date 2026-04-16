---
title: "Run multi-agent code review rounds with structured reviewer discourse before human approval"
description: "Use Open Code Review when an agent needs several reviewer personas to inspect a diff, debate findings, and synthesize review output before a human approves, posts, or acts on the review."
verification: "security_reviewed"
source: "https://github.com/spencermarx/open-code-review"
category:
  - "Code Quality &amp; Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "spencermarx/open-code-review"
  github_stars: 131
  ase_npm_package: "@open-code-review/cli"
  npm_weekly_downloads: 1089
---

# Run multi-agent code review rounds with structured reviewer discourse before human approval

Open Code Review gives an agent a narrow code-review workflow rather than a generic coding platform. It initializes a review project, analyzes a diff or requirements context, runs several reviewer agents in parallel, preserves their discourse, and produces structured findings plus a synthesized review that can be browsed in the dashboard or posted back to a pull request.

The scope stays tight: this is for multi-agent review rounds on code changes. It is not a generic IDE, not a broad AI coding assistant listing, and not a general CI platform card. Invoke it when the missing step is deeper review coverage and reviewer debate before human sign-off, not when the user simply wants another code editor or single-agent coding tool.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-multi-agent-code-review-rounds-with-structured-reviewer-discourse-before-human-approval/)
