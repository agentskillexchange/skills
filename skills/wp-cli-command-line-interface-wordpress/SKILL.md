---
name: WP-CLI Command-Line Interface for WordPress
description: Builds repeatable WordPress maintenance and content workflows around
  WP-CLI, the official command-line interface for WordPress. Useful for plugin management,
  database tasks, user administration, search-replace operations, and scripted publishing
  without living inside wp-admin.
category: "WordPress &amp; CMS"
framework: Multi-Framework
verification: security_reviewed
source: "https://github.com/wp-cli/wp-cli"
tool_ecosystem:
  github_repo: "https://github.com/wp-cli/wp-cli"
  github_stars: 5044
  license: MIT
---
# WP-CLI Command-Line Interface for WordPress

Builds repeatable WordPress maintenance and content workflows around WP-CLI, the official command-line interface for WordPress. Useful for plugin management, database tasks, user administration, search-replace operations, and scripted publishing without living inside wp-admin.

WP-CLI Command-Line Interface for WordPress is a practical skill for people who need to operate WordPress sites faster and more consistently than the admin dashboard allows. It is anchored to the real WP-CLI project and its command surface, including commands such as wp plugin list, wp post list, wp option get, wp user create, wp search-replace, wp cron event run, and wp db export. That makes it valuable for administrators, maintainers, and agents that need to inspect or change site state from a shell, over SSH, or inside a deployment pipeline.

The skill teaches an agent how to translate a site task into the right WP-CLI subcommands, flags, and safety checks. It can help enumerate content, export structured data, update plugins, flush caches, inspect rewrite rules, or run targeted maintenance against a staging site before touching production. Because WP-CLI exposes WordPress internals directly, the workflow is much more deterministic than clicking through wp-admin screens one by one.

Outputs usually include tabular command results, JSON formatted records, database exports, generated users, changed options, or audit evidence captured from the terminal. Integration points include shell automation, CI jobs, cron tasks, SSH-based remote maintenance, and plugin/theme development workflows where command-line verification is faster than browser testing. Use this skill when the job is operational WordPress control through a documented CLI rather than generic CMS advice.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill wp-cli-command-line-interface-wordpress
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill wp-cli-command-line-interface-wordpress -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill wp-cli-command-line-interface-wordpress -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill wp-cli-command-line-interface-wordpress -a codex
```

### OpenClaw

```bash
clawhub install wp-cli-command-line-interface-wordpress
```


## Source

- [GitHub](https://github.com/wp-cli/wp-cli)
