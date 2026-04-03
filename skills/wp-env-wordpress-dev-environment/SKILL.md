---
name: "wp-env Zero-Config WordPress Development Environment"
description: "The @wordpress/env package (wp-env) provides a zero-configuration, Docker-based local WordPress environment for developing and testing plugins and themes. A single command sets up WordPress with a test site, database, and PHP environment."
category: "WordPress & CMS"
framework: "Claude Code"
verification: "security_reviewed"
source: "https://www.npmjs.com/package/@wordpress/env"
tool_ecosystem:
  npm_package: "@wordpress/env"
  npm_weekly_downloads: 45294
---
# wp-env Zero-Config WordPress Development Environment

The @wordpress/env package (wp-env) provides a zero-configuration, Docker-based local WordPress environment for developing and testing plugins and themes. A single command sets up WordPress with a test site, database, and PHP environment.

## Overview

The `@wordpress/env` npm package, commonly known as wp-env, is the official WordPress development environment tool maintained as part of the Gutenberg project. It uses Docker to create isolated WordPress instances configured specifically for plugin and theme development, with zero manual configuration required.

Running `wp-env start` in any directory containing a WordPress plugin or theme automatically provisions a complete WordPress site with that code mounted and activated. The tool creates two parallel environments: a development site and a testing site, each with its own database. This separation allows developers to run PHPUnit tests and end-to-end tests without affecting their development data.

A skill leveraging wp-env enables agents to rapidly scaffold WordPress development environments, run automated tests against plugins, validate theme compatibility across WordPress versions, and execute WP-CLI commands within the containerized environment. The `.wp-env.json` configuration file supports specifying WordPress core version, PHP version, additional plugins (from wordpress.org, GitHub repos, or local paths), themes, port mappings, and environment variables.

Key commands include: `wp-env start` (provision environment), `wp-env stop` (shut down), `wp-env clean` (reset databases), `wp-env run` (execute commands inside containers, including WP-CLI), `wp-env destroy` (remove all data), and `wp-env logs` (view container output). The `--update` flag refreshes sources and reapplies configuration.

Integration points for agent workflows include: automated plugin testing across multiple PHP and WordPress version matrices, running PHPUnit and Playwright E2E tests in CI, validating plugin activation on clean installs, and debugging theme rendering issues in isolated environments. The tool integrates with GitHub Actions via the `@wordpress/env` npm package for CI/CD pipelines.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill wp-env-wordpress-dev-environment
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill wp-env-wordpress-dev-environment -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill wp-env-wordpress-dev-environment -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill wp-env-wordpress-dev-environment -a codex
```

### OpenClaw

```bash
clawhub install wp-env-wordpress-dev-environment
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-env-wordpress-dev-environment/)
