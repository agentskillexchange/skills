---
title: "Enforce architectural import boundaries in Python codebases with Import Linter"
description: "Check whether a Python codebase still respects declared layered, independence, or forbidden import contracts."
verification: listed
source: "https://github.com/seddonym/import-linter"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "seddonym/import-linter"
  github_stars: 995
---

# Enforce architectural import boundaries in Python codebases with Import Linter

Use Import Linter when an agent needs to guard a Python architecture against gradual boundary erosion. The agent defines contracts such as layered dependencies, forbidden imports, or independence rules, runs the checker, and turns violations into review comments or cleanup tasks. Invoke this instead of using the product normally when the job is architecture verification inside an existing codebase, not generic linting or package management. The scope boundary is clear: import-graph contract enforcement for Python projects.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/enforce-architectural-import-boundaries-in-python-codebases-with-import-linter
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/enforce-architectural-import-boundaries-in-python-codebases-with-import-linter` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/enforce-architectural-import-boundaries-in-python-codebases-with-import-linter/)
