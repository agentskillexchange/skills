---
title: "Validate Python Docstrings Against Function Signatures with pydoclint"
description: "Check that Python docstrings stay consistent with parameters, returns, and raised exceptions as code evolves."
verification: "listed"
source: "https://github.com/jsh9/pydoclint"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "jsh9/pydoclint"
  github_stars: 208
---

# Validate Python Docstrings Against Function Signatures with pydoclint

This skill uses pydoclint for a very specific documentation-integrity workflow. The agent compares Python docstrings to live function signatures and flags drift in parameters, return values, and documented exceptions so teams can catch stale API docs during review. Invoke it when code changes faster than its inline documentation and reviewers need a precise consistency check. Use general documentation tools when creating prose or broader style guidance. Use this skill when the real job is signature-to-docstring validation. The scope boundary is strict docstring consistency checking. It is not a broad documentation platform, generic Python linter, or package reference card.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/validate-python-docstrings-against-function-signatures-with-pydoclint/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/validate-python-docstrings-against-function-signatures-with-pydoclint
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/validate-python-docstrings-against-function-signatures-with-pydoclint`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/validate-python-docstrings-against-function-signatures-with-pydoclint/)
