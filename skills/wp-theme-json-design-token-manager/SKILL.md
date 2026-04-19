---
title: "WordPress Theme.json Design Token Manager"
description: "The WordPress Theme.json Design Token Manager provides systematic control over design tokens in modern WordPress block themes. It reads and writes theme.json configurations using the WP_Theme_JSON_Resolver class, managing color palettes, font families, spacing presets, and custom CSS properties. The agent uses wp_get_global_settings() and wp_get_global_styles() to resolve merged settings across default, theme, and user layers. It supports design token versioning and migration between theme.json schema versions (v1 to v3) using WP_Theme_JSON_Schema::migrate(). The manager handles custom block style variations through the styles.blocks configuration and generates CSS custom properties via wp_get_global_stylesheet(). It validates token values against WordPress color and gradient formats, manages font face declarations through the Font Library API (wp_register_font_collection), and synchronizes tokens with Figma design files through the Figma REST API. Includes support for per-block settings overrides and appearance tools configuration."
source: "https://github.com/WordPress/WordPress"
verification: "security_reviewed"
category:
  - "WordPress &amp; CMS"
framework:
  - "Gemini"
---

# WordPress Theme.json Design Token Manager

The WordPress Theme.json Design Token Manager provides systematic control over design tokens in modern WordPress block themes. It reads and writes theme.json configurations using the WP_Theme_JSON_Resolver class, managing color palettes, font families, spacing presets, and custom CSS properties. The agent uses wp_get_global_settings() and wp_get_global_styles() to resolve merged settings across default, theme, and user layers. It supports design token versioning and migration between theme.json schema versions (v1 to v3) using WP_Theme_JSON_Schema::migrate(). The manager handles custom block style variations through the styles.blocks configuration and generates CSS custom properties via wp_get_global_stylesheet(). It validates token values against WordPress color and gradient formats, manages font face declarations through the Font Library API (wp_register_font_collection), and synchronizes tokens with Figma design files through the Figma REST API. Includes support for per-block settings overrides and appearance tools configuration.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-theme-json-design-token-manager/)
