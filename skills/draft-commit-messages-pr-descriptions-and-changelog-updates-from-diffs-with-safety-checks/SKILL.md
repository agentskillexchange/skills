---
title: "Draft commit messages, PR descriptions, and changelog updates from diffs with safety checks"
description: "Analyze staged changes, scan for sensitive content, draft Conventional Commit messages, prepare PR text, and update changelog entries in a guarded commit-and-release communication workflow."
verification: "security_reviewed"
source: "https://github.com/psenger/ai-agent-skills/tree/main/skills/git-commit-pr-message"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "psenger/ai-agent-skills"
---

# Draft commit messages, PR descriptions, and changelog updates from diffs with safety checks

This skill helps an agent turn repository diffs into commit messages, PR summaries, and changelog-ready text while enforcing a disciplined workflow. The agent inspects staged and unstaged changes, checks branch context and recent history, performs mandatory sensitive-content scanning, asks for ticket references, drafts a Conventional Commit, and can continue into changelog and PR drafting with appropriate confirmations.

Use this when a user is ready to commit, push, open a PR, or update release notes and wants the agent to synthesize repository context into clean release communication. This is the right invocation shape when the user wants guarded, repo-aware drafting with ticket linking and secret checks rather than manually writing commit or PR text in git and GitHub.

The scope boundary is concrete: this is not a generic git, GitHub, or changelog product listing. It is a commit/PR/changelog workflow with explicit tool checks, security guardrails, confirmation points, and structured output tied to the current diff.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/draft-commit-messages-pr-descriptions-and-changelog-updates-from-diffs-with-safety-checks/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/draft-commit-messages-pr-descriptions-and-changelog-updates-from-diffs-with-safety-checks
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/draft-commit-messages-pr-descriptions-and-changelog-updates-from-diffs-with-safety-checks`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/draft-commit-messages-pr-descriptions-and-changelog-updates-from-diffs-with-safety-checks/)
