---
title: "WordPress Theme.json Design Token Manager"
description: "Manages WordPress theme.json design tokens including color palettes, typography presets, and spacing scales. Uses the WP_Theme_JSON_Resolver class and wp_get_global_settings() for dynamic token resolution."
slug: "wp-theme-json-design-token-manager"
category:
  - "WordPress &amp; CMS"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/wp-theme-json-design-token-manager/"
listed: true
---

# WordPress Theme.json Design Token Manager

Manages WordPress theme.json design tokens including color palettes, typography presets, and spacing scales. Uses the WP_Theme_JSON_Resolver class and wp_get_global_settings() for dynamic token resolution.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install wp-theme-json-design-token-manager
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The WordPress Theme.json Design Token Manager provides systematic control over design tokens in modern WordPress block themes. It reads and writes theme.json configurations using the WP_Theme_JSON_Resolver class, managing color palettes, font families, spacing presets, and custom CSS properties. The agent uses wp_get_global_settings() and wp_get_global_styles() to resolve merged settings across default, theme, and user layers. It supports design token versioning and migration between theme.json schema versions (v1 to v3) using WP_Theme_JSON_Schema::migrate(). The manager handles custom block style variations through the styles.blocks configuration and generates CSS custom properties via wp_get_global_stylesheet(). It validates token values against WordPress color and gradient formats, manages font face declarations through the Font Library API (wp_register_font_collection), and synchronizes tokens with Figma design files through the Figma REST API. Includes support for per-block settings overrides and appearance tools configuration.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-theme-json-design-token-manager/)
