---
name: "WP-CLI WordPress Command Line Interface"
description: "WP-CLI is the official command-line interface for WordPress, maintained as an open source project with extensive command docs and release history. It gives agents a reliable way to automate plugin, theme, database, transient, user, and multisite operations without driving the wp-admin UI."
verification: security_reviewed
source: "https://github.com/wp-cli/wp-cli"
category:
  - "WordPress &amp; CMS"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "wp-cli/wp-cli"
  github_stars: 5055
---

# WP-CLI WordPress Command Line Interface

WP-CLI is the command-line interface for WordPress and is one of the most practical tools to wrap in an agent skill when a workflow needs deterministic site administration. Instead of clicking through wp-admin, an agent can call documented commands such as wp plugin install, wp theme activate, wp option get, wp transient delete, or wp search-replace to make changes in a repeatable way. The upstream project is published at wp-cli.org and in the official GitHub repository at github.com/wp-cli/wp-cli, where the project exposes release tags, an MIT license, and active maintenance.
This skill is a strong fit for environments where WordPress access already exists over SSH, local shell, CI, or containerized hosting. It integrates naturally with PHP-based stacks, managed hosts that expose WP-CLI, deployment scripts, and operational runbooks. A typical agent flow can inspect plugin state, clear caches, update core, activate a feature plugin, or collect diagnostics by running read-only wp commands first and gated write commands second.
Because WP-CLI has a stable command taxonomy and thorough documentation on developer.wordpress.org and the WP-CLI handbook, it maps well to agent execution. The main dependencies are a working WordPress installation plus PHP 7.2.24 or later, and the recommended installation path is the official Phar download method. For WordPress operations where browser automation would be brittle or slow, WP-CLI is usually the cleaner integration point.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-cli-wordpress-command-line-interface/)
