---
name: "WordPress Theme.json Design Token Manager"
description: "Manages WordPress theme.json design tokens including color palettes, typography presets, and spacing scales. Uses the WP_Theme_JSON_Resolver class and wp_get_global_settings() for dynamic token resolution."
category: "WordPress & CMS"
framework: "Gemini"
verification: security_reviewed
source: "https://github.com/WordPress/WordPress"
tool_ecosystem:
  tool: wordpress
  github_stars: 20976
  github_repo: WordPress/WordPress
  maintained: true
---

# WordPress Theme.json Design Token Manager

Manages WordPress theme.json design tokens including color palettes, typography presets, and spacing scales. Uses the WP_Theme_JSON_Resolver class and wp_get_global_settings() for dynamic token resolution.

## Overview

The WordPress Theme.json Design Token Manager provides systematic control over design tokens in modern WordPress block themes. It reads and writes theme.json configurations using the WP_Theme_JSON_Resolver class, managing color palettes, font families, spacing presets, and custom CSS properties. The agent uses wp_get_global_settings() and wp_get_global_styles() to resolve merged settings across default, theme, and user layers. It supports design token versioning and migration between theme.json schema versions (v1 to v3) using WP_Theme_JSON_Schema::migrate(). The manager handles custom block style variations through the styles.blocks configuration and generates CSS custom properties via wp_get_global_stylesheet(). It validates token values against WordPress color and gradient formats, manages font face declarations through the Font Library API (wp_register_font_collection), and synchronizes tokens with Figma design files through the Figma REST API. Includes support for per-block settings overrides and appearance tools configuration.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill wp-theme-json-design-token-manager
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill wp-theme-json-design-token-manager -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill wp-theme-json-design-token-manager -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill wp-theme-json-design-token-manager -a codex
```

### OpenClaw

```bash
clawhub install wp-theme-json-design-token-manager
```

## Source

- Marketplace: https://agentskillexchange.com/skills/wp-theme-json-design-token-manager/
