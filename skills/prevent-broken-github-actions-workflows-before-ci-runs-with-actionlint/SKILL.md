---
title: "Prevent broken GitHub Actions workflows before CI runs with actionlint"
description: "Use actionlint when an agent needs to inspect GitHub Actions workflow files before a push or pull request lands. The skill checks syntax, expressions, action inputs, runner labels, cron patterns, and a few security footguns so the agent can stop bad workflow changes before CI burns time."
verification: security_reviewed
source: "https://github.com/rhysd/actionlint"
category:
  - "Code Quality &amp; Review"
framework:
  - "Multi-Framework"
---

# Prevent broken GitHub Actions workflows before CI runs with actionlint

This ASE entry is built around actionlint, the open source static checker for GitHub Actions workflow files maintained at rhysd/actionlint. The agent behavior is narrow and concrete: scan one repository’s workflow YAML, explain what is broken, and block or repair bad workflow edits before they hit GitHub Actions. That is the job-to-be-done. The agent is not acting as a general CI platform, a generic linter catalog, or a framework listing. It is using actionlint specifically to catch invalid keys, broken expressions, wrong action inputs, risky inline-script patterns, runner-label mistakes, dependency graph errors, and cron syntax problems inside workflow files.

Invoke this skill when a user is changing .github/workflows/*.yml, reviewing a pull request that touched workflow automation, or trying to understand why a workflow definition is obviously wrong before GitHub even starts a run. It is especially useful in repository maintenance, release automation, reusable workflow authoring, and pre-merge review loops where an agent can lint, summarize failures, and propose exact YAML fixes. actionlint also integrates shellcheck and pyflakes checks for inline scripts, which gives the agent a stronger review pass than plain YAML validation.

The scope boundary matters. This is not “GitHub Actions” as a product card, and it is not a generic Go CLI listing. The skill is bounded to preflight validation of workflow definitions. Integration points are local repository checkouts, pre-commit hooks, CI guard jobs, reviewdog pipelines, and editor or PR review automation. Upstream evidence is strong: the official GitHub repo exists, tagged releases are available, the MIT license is published, installation and usage docs are maintained in the repo, and the project shows recent maintenance and broad adoption.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prevent-broken-github-actions-workflows-before-ci-runs-with-actionlint/)
