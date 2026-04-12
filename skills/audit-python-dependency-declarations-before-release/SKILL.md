---
title: "Audit Python dependency declarations for unused, missing, and transitive imports before release"
slug: "audit-python-dependency-declarations-before-release"
description: "Use Deptry when an agent needs to verify that a Python project&#8217;s declared dependencies still match the imports the code actually uses. The agent scans the codebase, flags unused direct dependencies, missing declarations, and transitive imports that only work by accident, then turns the findings into cleanup commits or release blockers."
verification: security_reviewed
source: "https://github.com/osprey-oss/deptry"
category:
  - "Code Quality &amp; Review"
tool_ecosystem:
  github_repo: "https://github.com/osprey-oss/deptry"
  github_stars: 1358
---

# Audit Python dependency declarations for unused, missing, and transitive imports before release

Use Deptry when an agent needs to verify that a Python project&#8217;s declared dependencies still match the imports the code actually uses. The agent scans the codebase, flags unused direct dependencies, missing declarations, and transitive imports that only work by accident, then turns the findings into cleanup commits or release blockers.

## Installation

Choose the setup path that fits your environment:

1. Install from the Agent Skill Exchange UI
2. Clone or download this skill into your skills directory
3. Install with your agent platform's skill manager, if supported
4. Vendor the skill into your workspace or repo
5. Copy the skill files manually for local customization

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-python-dependency-declarations-before-release/)
