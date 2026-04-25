---
title: "PHPStan Static Analyzer Agent"
description: "Performs PHP static analysis using PHPStan CLI at rule levels 0-9 with custom extensions. Detects type errors, dead code, and PHPDoc inconsistencies in WordPress and Laravel projects."
verification: "security_reviewed"
source: "https://github.com/phpstan/phpstan"
category:
  - "Code Quality & Review"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "phpstan/phpstan"
  github_stars: 13909
---

# PHPStan Static Analyzer Agent

The PHPStan Static Analyzer Agent runs PHPStan CLI (phpstan analyse) at configurable rule levels (0-9) with custom extension support for comprehensive PHP static analysis. It detects type errors, unreachable code, incorrect PHPDoc annotations, and framework-specific issues. The agent configures phpstan.neon with project-specific settings including autoload paths, stub files for third-party dependencies, and custom rule definitions. It supports PHPStan extensions for WordPress (szepeviktor/phpstan-wordpress), Laravel (larastan), Symfony, and Doctrine ORM. For WordPress projects, the agent handles hook callback type inference, global function stubs ($wpdb, WP_Query), and template hierarchy analysis. Laravel support includes Eloquent model property inference, facade resolution, and container binding analysis through Larastan. Baseline management (phpstan analyse –generate-baseline) enables gradual adoption by ignoring existing errors while enforcing zero new errors. The agent tracks error counts per level, generates trend reports, and suggests incremental level upgrades. CI integration outputs errors in checkstyle XML or JSON format for GitHub annotations and code review comments.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/phpstan-static-analyzer-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/phpstan-static-analyzer-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/phpstan-static-analyzer-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/phpstan-static-analyzer-agent/)
