---
name: "PHPStan Static Analyzer Agent"
description: "Performs PHP static analysis using PHPStan CLI at rule levels 0-9 with custom extensions. Detects type errors, dead code, and PHPDoc inconsistencies in WordPress and Laravel projects."
category: "Code Quality & Review"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/phpstan-static-analyzer-agent/"
---
# PHPStan Static Analyzer Agent

Performs PHP static analysis using PHPStan CLI at rule levels 0-9 with custom extensions. Detects type errors, dead code, and PHPDoc inconsistencies in WordPress and Laravel projects.

The PHPStan Static Analyzer Agent runs PHPStan CLI (phpstan analyse) at configurable rule levels (0-9) with custom extension support for comprehensive PHP static analysis. It detects type errors, unreachable code, incorrect PHPDoc annotations, and framework-specific issues.



The agent configures phpstan.neon with project-specific settings including autoload paths, stub files for third-party dependencies, and custom rule definitions. It supports PHPStan extensions for WordPress (szepeviktor/phpstan-wordpress), Laravel (larastan), Symfony, and Doctrine ORM.



For WordPress projects, the agent handles hook callback type inference, global function stubs ($wpdb, WP_Query), and template hierarchy analysis. Laravel support includes Eloquent model property inference, facade resolution, and container binding analysis through Larastan.



Baseline management (phpstan analyse –generate-baseline) enables gradual adoption by ignoring existing errors while enforcing zero new errors. The agent tracks error counts per level, generates trend reports, and suggests incremental level upgrades. CI integration outputs errors in checkstyle XML or JSON format for GitHub annotations and code review comments.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill phpstan-static-analyzer-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill phpstan-static-analyzer-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill phpstan-static-analyzer-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill phpstan-static-analyzer-agent -a codex
```

### OpenClaw

```bash
clawhub install phpstan-static-analyzer-agent
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/phpstan-static-analyzer-agent/)
