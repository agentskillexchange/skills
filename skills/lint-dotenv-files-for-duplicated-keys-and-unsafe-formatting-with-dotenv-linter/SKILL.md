---
title: "Lint .env files for duplicated keys and unsafe formatting with dotenv-linter"
description: "Check dotenv files for duplicated keys, malformed values, and formatting mistakes before they break local runs or secret handoffs."
verification: "security_reviewed"
source: "https://github.com/dotenv-linter/dotenv-linter"
author: "dotenv-linter"
publisher_type: "organization"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "dotenv-linter/dotenv-linter"
  github_stars: 2068
---

# Lint .env files for duplicated keys and unsafe formatting with dotenv-linter

Check dotenv files for duplicated keys, malformed values, and formatting mistakes before they break local runs or secret handoffs.

## Prerequisites

The dotenv-linter CLI or binary and a repository containing dotenv files to check.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install a release binary or build with cargo install dotenv-linter, then run dotenv-linter against the repository root or specific .env files. Use the documented check, fix, and diff flows to review problems before committing changes.
```

## Documentation

- https://dotenv-linter.readthedocs.io/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-dotenv-files-for-duplicated-keys-and-unsafe-formatting-with-dotenv-linter/)
