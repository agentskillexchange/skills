---
name: "Run multi-agent code review rounds with structured reviewer discourse before human approval"
slug: "run-multi-agent-code-review-rounds-with-structured-reviewer-discourse-before-human-approval"
description: "Use Open Code Review when an agent needs several reviewer personas to inspect a diff, debate findings, and synthesize review output before a human approves, posts, or acts on the review."
github_stars: 131
verification: "security_reviewed"
source: "https://github.com/spencermarx/open-code-review"
author: "Spencer Marx"
publisher_type: "individual"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "spencermarx/open-code-review"
  github_stars: 131
  npm_package: "@open-code-review/cli"
  npm_weekly_downloads: 1089
---

# Run multi-agent code review rounds with structured reviewer discourse before human approval

Use Open Code Review when an agent needs several reviewer personas to inspect a diff, debate findings, and synthesize review output before a human approves, posts, or acts on the review.

## Prerequisites

Node.js 20+, Git, and a supported AI coding assistant such as Claude Code, Cursor, Windsurf, or another OCR-supported tool. GitHub CLI auth is also needed if you want to post reviews back to pull requests.

## Installation

Requirements and caveats from upstream:
- **Prerequisites**: GitHub CLI (gh) installed and authenticated, open PR on current branch.

Basic usage or getting-started notes:
- The dashboard is the recommended way to run reviews, browse results, and manage your workflow. Launch it with ocr dashboard.
- ### Run reviews and maps
- <img src="assets/ocr-tool-example-translated-human-review.png" alt="Human-voice review posted to GitHub PR" width="700" />

- Source: https://github.com/spencermarx/open-code-review
- Extracted from upstream docs: https://raw.githubusercontent.com/spencermarx/open-code-review/HEAD/README.md

## Documentation

- https://github.com/spencermarx/open-code-review#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-multi-agent-code-review-rounds-with-structured-reviewer-discourse-before-human-approval/)
