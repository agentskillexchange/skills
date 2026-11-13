---
name: "Build and validate one Enferno admin feature"
slug: "build-validate-one-enferno-admin-feature"
description: "Implement one scoped admin feature using Enferno’s upstream agent skill, then review its migration, authorization, CSRF behavior and test evidence."
github_stars: 571
verification: "security_reviewed"
source: "https://github.com/level09/enferno"
author: "level09"
publisher_type: "community"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "level09/enferno"
  github_stars: 571
---

# Build and validate one Enferno admin feature

Implement one scoped admin feature using Enferno’s upstream agent skill, then review its migration, authorization, CSRF behavior and test evidence.

## Prerequisites

Coding agent with terminal/filesystem access; Python 3.11+; uv; Enferno development checkout; disposable database; browser for UI validation

## Installation

Install or set up from the source-backed instructions:

Use a disposable source checkout at the documented commit. Read AGENTS.md and .agents/skills/enferno-dev/SKILL.md. For a fresh development project follow ./setup.sh, uv run flask create-db and uv run flask install. Existing projects need their own setup and migration review. Do not initialize or upgrade production databases through this workflow. Source commit: 346661754b179be425ed62488bd2650620094468.

- Source: https://github.com/level09/enferno

## Documentation

- https://github.com/level09/enferno/blob/346661754b179be425ed62488bd2650620094468/.agents/skills/enferno-dev/SKILL.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/build-validate-one-enferno-admin-feature/)
