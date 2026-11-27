---
name: "Gate Coding Changes with Cezar Browser Tests and Bounded Repair Retries"
slug: "gate-coding-changes-cezar-browser-tests-bounded-retries"
description: "Run a worktree-local implementation and test loop that returns browser failure evidence to the coding agent, retries test failures within a limit, and stops on infrastructure errors."
github_stars: 1111
verification: "security_reviewed"
source: "https://github.com/open-mercato/cezar"
author: "Patryk Lewczuk / Open Mercato"
publisher_type: "open_source"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "open-mercato/cezar"
  github_stars: 1111
  npm_package: "@open-mercato/cezar"
  npm_weekly_downloads: 82913
---

# Gate Coding Changes with Cezar Browser Tests and Bounded Repair Retries

Run a worktree-local implementation and test loop that returns browser failure evidence to the coding agent, retries test failures within a limit, and stops on infrastructure errors.

## Prerequisites

Node.js >=20; Git; supported authenticated coding-agent CLI; project-pinned TesterArmy e2e and browser; optional provider API key for agentic test steps

## Installation

Install or set up from the source-backed instructions:

From the target repository run npx cezar-run@0.20.0. Use Settings → project → External integrations → Test frameworks → TesterArmy e2e → Set up e2e; review and commit or merge the generated configuration before launching implement-and-e2e. Install repository-pinned dependencies in each task worktree. Configure browser/model prerequisites and check-only secrets using the upstream guide. No installation was executed during verification.

- Source: https://github.com/open-mercato/cezar

## Documentation

- https://github.com/open-mercato/cezar/blob/b5309b02c004eee0c8b14bbcd69cf65786b55421/docs/e2e-verification.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gate-coding-changes-cezar-browser-tests-bounded-retries/)
