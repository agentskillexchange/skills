---
name: WordPress Theme.json Design Token Manager
description: Manages WordPress theme.json design tokens including color palettes,
  typography presets, and spacing scales. Uses the WP_Theme_JSON_Resolver class and
  wp_get_global_settings() for dynamic token resolution.
verification: security_reviewed
source: https://agentskillexchange.com/skills/wp-theme-json-design-token-manager/
category:
- WordPress &amp; CMS
framework:
- Gemini
---
# WordPress Theme.json Design Token Manager

The WordPress Theme.json Design Token Manager provides systematic control over design tokens in modern WordPress block themes. It reads and writes theme.json configurations using the WP_Theme_JSON_Resolver class, managing color palettes, font families, spacing presets, and custom CSS properties. The agent uses wp_get_global_settings() and wp_get_global_styles() to resolve merged settings across default, theme, and user layers. It supports design token versioning and migration between theme.json schema versions (v1 to v3) using WP_Theme_JSON_Schema::migrate(). The manager handles custom block style variations through the styles.blocks configuration and generates CSS custom properties via wp_get_global_stylesheet(). It validates token values against WordPress color and gradient formats, manages font face declarations through the Font Library API (wp_register_font_collection), and synchronizes tokens with Figma design files through the Figma REST API. Includes support for per-block settings overrides and appearance tools configuration.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-theme-json-design-token-manager/)
