---
title: "Audit Python dependency declarations for unused, missing, and transitive imports before release"
description: "Use Deptry when an agent needs to verify that a Python project's declared dependencies still match the imports the code actually uses. The agent scans the codebase, flags unused direct dependencies, missing declarations, and transitive imports that only work by accident, then turns the findings into cleanup commits or release blockers."
verification: security_reviewed
source: "https://github.com/osprey-oss/deptry"
category:
  - "Code Quality &amp; Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "osprey-oss/deptry"
  github_stars: 1359
---

# Audit Python dependency declarations for unused, missing, and transitive imports before release

Use Deptry when an agent needs to verify that a Python project's declared dependencies still match the imports the code actually uses. The agent scans the codebase, flags unused direct dependencies, missing declarations, and transitive imports that only work by accident, then turns the findings into cleanup commits or release blockers.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/audit-python-dependency-declarations-before-release
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/audit-python-dependency-declarations-before-release` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-python-dependency-declarations-before-release/)
