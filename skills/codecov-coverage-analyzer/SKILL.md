---
name: Codecov Coverage Analyzer
description: Analyzes test coverage using the Codecov API v2 and codecov-cli uploader.
  Fetches per-file coverage from /api/v2/repos/{owner}/{repo}/report, computes diff
  coverage via /api/v2/repos/{owner}/{repo}/pulls/{pull}, and enforces configurable
  thresholds in CI pipelines.
category: Code Quality & Review
framework: Codex
verification: security_reviewed
source: https://agentskillexchange.com/skills/codecov-coverage-analyzer/
---
# Codecov Coverage Analyzer
Analyzes test coverage using the Codecov API v2 and codecov-cli uploader. Fetches per-file coverage from /api/v2/repos/{owner}/{repo}/report, computes diff coverage via /api/v2/repos/{owner}/{repo}/pulls/{pull}, and enforces configurable thresholds in CI pipelines.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/codecov-coverage-analyzer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/codecov-coverage-analyzer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/codecov-coverage-analyzer/)
