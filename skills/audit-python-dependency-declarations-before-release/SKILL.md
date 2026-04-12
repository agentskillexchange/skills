---
title: "Audit Python dependency declarations for unused, missing, and transitive imports before release"
description: "Use Deptry when an agent needs to verify that a Python project's declared dependencies still match the imports the code actually uses. The agent scans the codebase, flags unused direct dependencies, missing declarations, and transitive imports that only work by accident, then turns the findings into cleanup commits or release blockers."
verification: security_reviewed
source: "https://github.com/osprey-oss/deptry"
---

# Audit Python dependency declarations for unused, missing, and transitive imports before release

Use Deptry when an agent needs to verify that a Python project's declared dependencies still match the imports the code actually uses. The agent scans the codebase, flags unused direct dependencies, missing declarations, and transitive imports that only work by accident, then turns the findings into cleanup commits or release blockers.

## Installation

Choose the path that fits your setup:

1. Clone this repository and use the skill locally.
2. Copy the skill folder into your local skills directory.
3. Add the skill as a Git submodule in your skills workspace.
4. Vendor the files into an internal skill catalog for your team.
5. Reference the upstream source and recreate the skill in your own agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-python-dependency-declarations-before-release/)
