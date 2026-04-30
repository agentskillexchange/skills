---
title: "Run multi-agent code review rounds with structured reviewer discourse before human approval"
description: "Use Open Code Review when an agent needs several reviewer personas to inspect a diff, debate findings, and synthesize review output before a human approves, posts, or acts on the review."
verification: "security_reviewed"
source: "https://github.com/spencermarx/open-code-review"
author: "Spencer Marx"
publisher_type: "individual"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
<p>Install the CLI with <code>npm install -g @open-code-review/cli</code>, run <code>ocr init</code> inside the target repository, then open <code>ocr dashboard</code> or invoke the review from your coding assistant with <code>/ocr:review</code> or <code>/ocr-review</code>. Use <code>ocr progress</code> to watch live execution and connect <code>gh</code> if you want OCR to post findings to pull requests.</p>
```

## Documentation

- https://github.com/spencermarx/open-code-review#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-multi-agent-code-review-rounds-with-structured-reviewer-discourse-before-human-approval/)
