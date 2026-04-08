---
title: wp-env Zero-Config WordPress Development Environment
description: 'The @wordpress/env npm package, commonly known as wp-env, is the official
  WordPress development environment tool maintained as part of the Gutenberg project.
  It uses Docker to create isolated WordPress instances configured specifically for
  plugin and theme development, with zero manual configuration required. Running wp-env
  start in any directory containing a WordPress plugin or theme automatically provisions
  a complete WordPress site with that code mounted and activated. The tool creates
  two parallel environments: a development site and a testing site, each with its
  own database. This separation allows developers to run PHPUnit tests and end-to-end
  tests without affecting their development data. A skill leveraging wp-env enables
  agents to rapidly scaffold WordPress development environments, run automated tests
  against plugins, validate theme compatibility across WordPress versions, and execute
  WP-CLI commands within the containerized environment. The .wp-env.json configuration
  file supports specifying WordPress core version, PHP version, additional plugins
  (from wordpress.org, GitHub repos, or local paths), themes, port mappings, and environment
  variables. Key commands include: wp-env start (provision environment), wp-env stop
  (shut down), wp-env clean (reset databases), wp-env run (execute commands inside
  containers, including WP-CLI), wp-env destroy (remove all data), and wp-env logs
  (view container output). The --update flag refreshes sources and reapplies configuration.
  Integration points for agent workflows include: automated plugin testing across
  multiple PHP and WordPress version matrices, running PHPUnit and Playwright E2E
  tests in CI, validating plugin activation on clean installs, and debugging theme
  rendering issues in isolated environments. The tool integrates with GitHub Actions
  via the @wordpress/env npm package for CI/CD pipelines.'
verification: security_reviewed
source: https://www.npmjs.com/package/@wordpress/env
category:
- WordPress &amp; CMS
framework:
- Claude Code
tool_ecosystem:
  npm_package: '@wordpress/env'
  npm_weekly_downloads: 46753
---

# wp-env Zero-Config WordPress Development Environment

The @wordpress/env npm package, commonly known as wp-env, is the official WordPress development environment tool maintained as part of the Gutenberg project. It uses Docker to create isolated WordPress instances configured specifically for plugin and theme development, with zero manual configuration required. Running wp-env start in any directory containing a WordPress plugin or theme automatically provisions a complete WordPress site with that code mounted and activated. The tool creates two parallel environments: a development site and a testing site, each with its own database. This separation allows developers to run PHPUnit tests and end-to-end tests without affecting their development data. A skill leveraging wp-env enables agents to rapidly scaffold WordPress development environments, run automated tests against plugins, validate theme compatibility across WordPress versions, and execute WP-CLI commands within the containerized environment. The .wp-env.json configuration file supports specifying WordPress core version, PHP version, additional plugins (from wordpress.org, GitHub repos, or local paths), themes, port mappings, and environment variables. Key commands include: wp-env start (provision environment), wp-env stop (shut down), wp-env clean (reset databases), wp-env run (execute commands inside containers, including WP-CLI), wp-env destroy (remove all data), and wp-env logs (view container output). The --update flag refreshes sources and reapplies configuration. Integration points for agent workflows include: automated plugin testing across multiple PHP and WordPress version matrices, running PHPUnit and Playwright E2E tests in CI, validating plugin activation on clean installs, and debugging theme rendering issues in isolated environments. The tool integrates with GitHub Actions via the @wordpress/env npm package for CI/CD pipelines.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-env-wordpress-dev-environment/)
