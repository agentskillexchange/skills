---
title: "Address GitHub PR review comments from the current branch with gh-address-comments"
description: "Find the open PR for the current branch, gather unresolved review comments, and drive a focused comment-resolution workflow with gh-authenticated context."
verification: "listed"
source: "https://github.com/openai/skills/tree/main/skills/.curated/gh-address-comments"
category:
  - "Code Quality & Review"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "openai/skills"
  github_stars: 17293
---

# Address GitHub PR review comments from the current branch with gh-address-comments

Use gh-address-comments when the agent should find the current branch’s open PR, enumerate review threads and comments, and help work through the ones the user chooses to address. Invoke it instead of browsing GitHub manually when you want a bounded comment-handling workflow anchored to the current PR and authenticated gh context. The scope boundary is specific enough to be skill-shaped: PR comment inspection and response planning for one live review surface, not a generic GitHub tooling card.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/address-github-pr-review-comments-from-the-current-branch-with-gh-address-comments/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/address-github-pr-review-comments-from-the-current-branch-with-gh-address-comments
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/address-github-pr-review-comments-from-the-current-branch-with-gh-address-comments`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/address-github-pr-review-comments-from-the-current-branch-with-gh-address-comments/)
