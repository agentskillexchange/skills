---
title: "PHPStan Static Analyzer Agent"
slug: "phpstan-static-analyzer-agent"
description: "Performs PHP static analysis using PHPStan CLI at rule levels 0-9 with custom extensions. Detects type errors, dead code, and PHPDoc inconsistencies in WordPress and Laravel projects."
github_stars: 13909
verification: "security_reviewed"
source: "https://github.com/phpstan/phpstan"
author: "PHPStan"
category: "Code Quality & Review"
framework: "OpenClaw"
tool_ecosystem:
  github_repo: "phpstan/phpstan"
  github_stars: 13909
---

# PHPStan Static Analyzer Agent

Performs PHP static analysis using PHPStan CLI at rule levels 0-9 with custom extensions. Detects type errors, dead code, and PHPDoc inconsistencies in WordPress and Laravel projects.

## Prerequisites

PHP, Composer

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
composer require --dev phpstan/phpstan
```

## Documentation

- https://phpstan.org/user-guide/getting-started

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/phpstan-static-analyzer-agent/)
