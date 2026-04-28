---
title: "Codecov Coverage Analyzer"
description: "Analyzes test coverage using the Codecov API v2 and codecov-cli uploader. Fetches per-file coverage from /api/v2/repos/{owner}/{repo}/report, computes diff coverage via /api/v2/repos/{owner}/{repo}/pulls/{pull}, and enforces configurable thresholds in CI pipelines."
verification: security_reviewed
source: "https://docs.codecov.com/docs/quick-start"
category:
  - "Code Quality & Review"
framework:
  - "Codex"
---

# Codecov Coverage Analyzer

Analyzes test coverage using the Codecov API v2 and codecov-cli uploader. Fetches per-file coverage from /api/v2/repos/{owner}/{repo}/report, computes diff coverage via /api/v2/repos/{owner}/{repo}/pulls/{pull}, and enforces configurable thresholds in CI pipelines.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/codecov-coverage-analyzer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/codecov-coverage-analyzer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/codecov-coverage-analyzer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/codecov-coverage-analyzer/)
