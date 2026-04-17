---
title: "WordPress Playground WebAssembly Runtime for In-Browser WordPress"
description: "WordPress Playground runs a full WordPress instance entirely in the browser using WebAssembly-compiled PHP. It enables zero-setup WordPress testing, plugin previews, and interactive demos without any server infrastructure."
verification: security_reviewed
source: "https://github.com/WordPress/wordpress-playground"
category:
  - "WordPress & CMS"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "WordPress/wordpress-playground"
  github_stars: 1926
  license: "GPL-2.0"
---

# WordPress Playground WebAssembly Runtime for In-Browser WordPress

WordPress Playground is an official WordPress project that compiles PHP to WebAssembly, enabling a complete WordPress installation to run directly in a web browser with no server required. This technology powers instant WordPress demos, plugin testing environments, and interactive learning experiences.

The @wp-playground/client npm package provides a JavaScript API for embedding WordPress Playground in any web application via iframes. Developers can programmatically install plugins, activate themes, configure WordPress settings, and execute PHP code—all from JavaScript. The blueprint system allows declarative configuration of WordPress environments with specific PHP versions, WordPress versions, plugins, and themes.

A skill built around WordPress Playground enables agents to spin up disposable WordPress instances for testing plugin compatibility, previewing theme changes, validating WP-CLI commands, and running PHPUnit tests in isolation. The CLI tool (wp-playground) supports local development with auto-reload, making it ideal for rapid iteration on WordPress projects.

Key capabilities include: running PHP 7.0 through 8.4 via WebAssembly, mounting local plugin and theme directories, executing WP-CLI commands within the sandboxed environment, networking via a service worker proxy, and persisting data across sessions using browser storage or the filesystem. The project supports both browser and Node.js runtimes.

Integration points include GitHub Actions for automated PR previews (via the wordpress-playground action), embedding in documentation sites for live code examples, and programmatic testing of WordPress plugins before deployment. The API supports steps like installPlugin, activatePlugin, login, importWxr, and arbitrary PHP execution.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/wordpress-playground-wasm-runtime
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/wordpress-playground-wasm-runtime` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wordpress-playground-wasm-runtime/)
