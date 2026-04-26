---
title: "WordPress Scripts Build and Block Toolchain"
description: "@wordpress/scripts packages the default WordPress JavaScript build stack into one reusable developer dependency. It gives plugin and block developers a consistent CLI for bundling, linting, testing, packaging, and maintaining modern WordPress code without hand-assembling webpack and related tooling."
verification: "security_reviewed"
source: "https://www.npmjs.com/package/@wordpress/scripts"
category:
  - "WordPress & CMS"
framework:
  - "Multi-Framework"
tool_ecosystem:
  npm_package: "@wordpress/scripts"
  npm_weekly_downloads: 96219
---

# WordPress Scripts Build and Block Toolchain

@wordpress/scripts is the official WordPress developer tooling package for modern JavaScript and block development. It ships as an npm package and exposes the wp-scripts CLI so teams can standardize build, lint, format, test, and packaging tasks across plugins, themes, and block projects. Instead of wiring together webpack, Babel, Jest, ESLint, and auxiliary configuration by hand, a project installs one dependency and inherits the conventions maintained by the WordPress project.

In practice, this makes it useful for jobs like compiling block editor assets, watching local source files during development, linting JavaScript and CSS, running unit and end-to-end tests, generating plugin ZIP archives, and keeping WordPress package versions aligned. The package README documents common commands such as wp-scripts build, wp-scripts start, wp-scripts lint-js, wp-scripts test-e2e, and wp-scripts plugin-zip. It also supports block metadata workflows, including generation of a blocks manifest that can improve plugin registration performance.

For ASE, this maps cleanly to repeatable WordPress engineering workflows. A skill built around @wordpress/scripts can scaffold or modernize build pipelines, add package.json scripts to an existing repository, debug block build issues, standardize CI commands, or prepare a distributable plugin ZIP. Integration points include npm-based projects, Gutenberg block repos, WordPress plugin monorepos, and CI environments that need reproducible build commands.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/wordpress-scripts-build-and-block-toolchain/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/wordpress-scripts-build-and-block-toolchain
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/wordpress-scripts-build-and-block-toolchain`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wordpress-scripts-build-and-block-toolchain/)
