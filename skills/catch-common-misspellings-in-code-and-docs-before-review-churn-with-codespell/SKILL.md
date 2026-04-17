---
title: "Catch common misspellings in code and docs before review churn with codespell"
description: "Run a fast typo pass across source files and documentation so common misspellings are fixed before they spread through reviews and releases."
verification: listed
source: "https://github.com/codespell-project/codespell"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "codespell-project/codespell"
  github_stars: 2356
---

# Catch common misspellings in code and docs before review churn with codespell

Use codespell when an agent needs to scan a repository for common misspellings in source files, docs, comments, and config text, then optionally apply low-risk fixes. It is well suited to cleanup passes before review, documentation refreshes, and repo-wide polish tasks where a full grammar tool would be heavier than necessary.

A user should invoke this instead of using their editor or a general writing tool normally when the job is repository-scale typo detection and remediation. The scope boundary is clear and skill-shaped: codespell only finds and fixes common misspellings in text-like project files, not broader prose editing, style coaching, or documentation platform management.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/catch-common-misspellings-in-code-and-docs-before-review-churn-with-codespell
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/catch-common-misspellings-in-code-and-docs-before-review-churn-with-codespell` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/catch-common-misspellings-in-code-and-docs-before-review-churn-with-codespell/)
