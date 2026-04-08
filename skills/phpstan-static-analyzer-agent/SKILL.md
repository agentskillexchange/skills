---
title: PHPStan Static Analyzer Agent
description: The PHPStan Static Analyzer Agent runs PHPStan CLI (phpstan analyse)
  at configurable rule levels (0-9) with custom extension support for comprehensive
  PHP static analysis. It detects type errors, unreachable code, incorrect PHPDoc
  annotations, and framework-specific issues. The agent configures phpstan.neon with
  project-specific settings including autoload paths, stub files for third-party dependencies,
  and custom rule definitions. It supports PHPStan extensions for WordPress (szepeviktor/phpstan-wordpress),
  Laravel (larastan), Symfony, and Doctrine ORM. For WordPress projects, the agent
  handles hook callback type inference, global function stubs ($wpdb, WP_Query), and
  template hierarchy analysis. Laravel support includes Eloquent model property inference,
  facade resolution, and container binding analysis through Larastan. Baseline management
  (phpstan analyse –generate-baseline) enables gradual adoption by ignoring existing
  errors while enforcing zero new errors. The agent tracks error counts per level,
  generates trend reports, and suggests incremental level upgrades. CI integration
  outputs errors in checkstyle XML or JSON format for GitHub annotations and code
  review comments.
verification: security_reviewed
source: https://agentskillexchange.com/skills/phpstan-static-analyzer-agent/
category:
- Code Quality &amp; Review
framework:
- OpenClaw
---

# PHPStan Static Analyzer Agent

The PHPStan Static Analyzer Agent runs PHPStan CLI (phpstan analyse) at configurable rule levels (0-9) with custom extension support for comprehensive PHP static analysis. It detects type errors, unreachable code, incorrect PHPDoc annotations, and framework-specific issues. The agent configures phpstan.neon with project-specific settings including autoload paths, stub files for third-party dependencies, and custom rule definitions. It supports PHPStan extensions for WordPress (szepeviktor/phpstan-wordpress), Laravel (larastan), Symfony, and Doctrine ORM. For WordPress projects, the agent handles hook callback type inference, global function stubs ($wpdb, WP_Query), and template hierarchy analysis. Laravel support includes Eloquent model property inference, facade resolution, and container binding analysis through Larastan. Baseline management (phpstan analyse –generate-baseline) enables gradual adoption by ignoring existing errors while enforcing zero new errors. The agent tracks error counts per level, generates trend reports, and suggests incremental level upgrades. CI integration outputs errors in checkstyle XML or JSON format for GitHub annotations and code review comments.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/phpstan-static-analyzer-agent/)
