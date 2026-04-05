---
name: "Elementor Website Builder WordPress Visual Page Editor"
description: "Elementor is the visual drag-and-drop website builder plugin for WordPress maintained by Elementor, with more than 10 million active installs on WordPress.org. This skill is for agents that need to work with Elementor-powered pages, templates, sections, and widgets without treating the site like a generic WordPress install."
category: "WordPress &amp; CMS"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://wordpress.org/plugins/elementor/"
---
# Elementor Website Builder WordPress Visual Page Editor

Elementor is the visual drag-and-drop website builder plugin for WordPress maintained by Elementor, with more than 10 million active installs on WordPress.org. This skill is for agents that need to work with Elementor-powered pages, templates, sections, and widgets without treating the site like a generic WordPress install.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill elementor-website-builder-wordpress-visual-page-editor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill elementor-website-builder-wordpress-visual-page-editor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill elementor-website-builder-wordpress-visual-page-editor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill elementor-website-builder-wordpress-visual-page-editor -a codex
```

### OpenClaw

```bash
clawhub install elementor-website-builder-wordpress-visual-page-editor
```

## Details

Elementor Website Builder is the WordPress visual builder plugin from Elementor that lets teams design landing pages, marketing pages, theme templates, popups, and reusable sections through a widget-based editor. The upstream plugin is distributed on WordPress.org and the official Elementor site, requires WordPress 6.6+, requires PHP 7.4+, and was updated on 2026-03-30 according to the live plugin directory metadata. With more than 10 million active installs, it easily clears the adoption gate for ASE intake.

This skill is for an agent that needs to understand an Elementor-driven site before making changes. Instead of editing post content blindly, the agent can inspect whether a page is built with Elementor, identify reusable templates, reason about sections, columns, containers, global styles, and widget settings, and map requested design changes onto Elementor’s actual editing model. That matters when a site’s structure lives in Elementor data rather than in classic block markup or a custom theme file.

A strong Elementor skill should help with jobs such as updating hero sections, changing CTA blocks, replacing media, adjusting responsive layout behavior, documenting template dependencies, and preparing safe edit plans for WordPress admins. Outputs can include an implementation checklist, widget-level change notes, a template inventory, compatibility warnings for theme-builder usage, and guidance for how Elementor changes interact with WordPress themes, menus, forms, and SEO plugins. Integration points include Elementor templates, WordPress pages and posts, theme locations, reusable design systems, and any workflow where an agent needs to coordinate visual builder edits with the rest of a WordPress stack.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/elementor-website-builder-wordpress-visual-page-editor/)
