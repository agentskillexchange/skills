---
title: "Audit Python dependency declarations for unused, missing, and transitive imports before release"
slug: "audit-python-dependency-declarations-before-release"
description: "Use Deptry when an agent needs to verify that a Python project&#8217;s declared dependencies still match the imports the code actually uses. The agent scans the codebase, flags unused direct dependencies, missing declarations, and transitive imports that only work by accident, then turns the findings into cleanup commits or release blockers."
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

Use Deptry when an agent needs to verify that a Python project&#8217;s declared dependencies still match the imports the code actually uses. The agent scans the codebase, flags unused direct dependencies, missing declarations, and transitive imports that only work by accident, then turns the findings into cleanup commits or release blockers.

## Installation

1. Clone this skill into your local skills directory.
2. Review the required tools and environment variables.
3. Install dependencies with your preferred package manager or runtime.
4. Run the upstream install command from the project documentation, if needed.
5. Validate the installation and test the skill in your agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-python-dependency-declarations-before-release/)
