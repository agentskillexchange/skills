---
title: "WordPress Multisite Provisioner"
description: "Automates WordPress Multisite network site creation using wp_insert_site() and the Sites REST API. Configures per-site themes, plugins, and options via switch_to_blog() with subdomain or subdirectory routing."
verification: security_reviewed
source: "https://github.com/WordPress/WordPress"
category:
  - "WordPress &amp; CMS"
framework:
  - "ChatGPT Agents"
---

# WordPress Multisite Provisioner

WordPress Multisite Provisioner streamlines the creation and configuration of sites within a WordPress Multisite network. It uses wp_insert_site() (WordPress 5.1+) for programmatic site creation with full control over domain, path, and network assignment.

The agent configures new sites via switch_to_blog() context switching, setting theme activation with switch_theme(), plugin activation lists, and site-specific options via update_option(). It supports both subdomain and subdirectory network configurations, handling SUBDOMAIN_INSTALL and DOMAIN_CURRENT_SITE constants.

Includes templates for common site configurations: landing pages, blogs, WooCommerce stores, and LMS setups. Manages network-level settings via update_network_option() including upload quotas, allowed themes, and menu modules. Integrates with WP-CLI wp site create for bulk provisioning and generates Nginx/Apache rewrite rules for subdomain routing. Supports user role mapping across sites with add_user_to_blog().

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-multisite-provisioner-agent/)
