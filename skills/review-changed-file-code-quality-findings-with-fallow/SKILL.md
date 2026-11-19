---
name: "Review changed-file code quality findings with Fallow"
slug: "review-changed-file-code-quality-findings-with-fallow"
description: "Audit a JavaScript or TypeScript change against its Git base, inspect structured findings, and return a focused merge-readiness report across code health, duplication, and unused code."
github_stars: 5376
verification: "security_reviewed"
source: "https://github.com/fallow-rs/fallow"
author: "fallow-rs maintainers"
publisher_type: "organization"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "fallow-rs/fallow"
  github_stars: 5376
  npm_package: "fallow"
  npm_weekly_downloads: 2529929
---

# Review changed-file code quality findings with Fallow

Audit a JavaScript or TypeScript change against its Git base, inspect structured findings, and return a focused merge-readiness report across code health, duplication, and unused code.

## Prerequisites

Git checkout of a JavaScript or TypeScript project; explicit base revision; Node.js >=22 and npm; fallow CLI

## Installation

Install or set up from the source-backed instructions:

In the project, run npm install --save-dev fallow. Review npx fallow recommend, then invoke npx fallow audit --base --format json --quiet. No hooks, MCP registration or automatic fixes are required.

- Source: https://github.com/fallow-rs/fallow

## Documentation

- https://fallow.tools/docs/cli/audit/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/review-changed-file-code-quality-findings-with-fallow/)
