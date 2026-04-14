---
title: "Audit Python dependency declarations for unused, missing, and transitive imports before release"
slug: "audit-python-dependency-declarations-before-release"
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

Choose the method that fits your setup:

1. Install from Agent Skill Exchange
2. Clone or download the upstream project
3. Install with the upstream package manager
4. Add the skill to your local skills directory
5. Follow the upstream documentation for environment-specific setup

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-python-dependency-declarations-before-release/)
