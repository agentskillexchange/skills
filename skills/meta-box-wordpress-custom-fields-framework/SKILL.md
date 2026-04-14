---
title: "Meta Box WordPress Custom Fields and Meta Boxes Framework"
description: "Meta Box is a professional WordPress framework for creating custom fields and custom meta boxes with over 40 field types. It supports posts, pages, custom post types, taxonomies, settings pages, user profiles, and comments."
verification: security_reviewed
source: "https://github.com/wpmetabox/meta-box"
category:
  - "WordPress &amp; CMS"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "wpmetabox/meta-box"
  github_stars: 1237
---

# Meta Box WordPress Custom Fields and Meta Boxes Framework

Meta Box is a widely-used WordPress plugin and framework that enables developers and site builders to add custom fields and meta boxes to any WordPress content type. With over 40 built-in field types including text, image upload, WYSIWYG editor, file, select, checkbox, radio, date/time picker, taxonomy, user, and oEmbed, Meta Box covers virtually any data capture need.

Supported Content Types
Custom fields can be attached to posts, pages, custom post types, taxonomies (via MB Term Meta), settings pages and Customizer sections (via MB Settings Page), user profile pages (via MB User Profile), and post comments (via MB Comment Meta). This flexibility makes Meta Box suitable for building complex content architectures.

Developer Features
Meta Box uses native WordPress meta data storage and functions for performance. It supports cloneable (repeatable) fields for all field types including WYSIWYG, and repeatable field groups via the Group extension. Developers can create custom field types, and the plugin provides extensive actions and filters for customization. Meta Box integrates with Composer for dependency management.

Agent Integration
For AI agents working with WordPress, Meta Box fields are exposed through the WordPress REST API, making them accessible for content automation workflows. The plugin integrates with page builders (Elementor, Beaver Builder, Divi, Bricks, Brizy), SEO plugins (Yoast, Rank Math), and supports migration from ACF or Toolset. Meta Box Lite provides a free UI for managing fields without code. Install from WordPress.org or via Composer with composer require wpmetabox/meta-box.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/meta-box-wordpress-custom-fields-framework/)
