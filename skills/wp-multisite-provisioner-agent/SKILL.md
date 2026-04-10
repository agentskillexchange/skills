---
title: "WordPress Multisite Provisioner"
description: "Automates WordPress Multisite network site creation using wp_insert_site() and the Sites REST API. Configures per-site themes, plugins, and options via switch_to_blog() with subdomain or subdirectory routing."
slug: "wp-multisite-provisioner-agent"
category:
  - "WordPress &amp; CMS"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/wp-multisite-provisioner-agent/"
---

# WordPress Multisite Provisioner

Automates WordPress Multisite network site creation using wp_insert_site() and the Sites REST API. Configures per-site themes, plugins, and options via switch_to_blog() with subdomain or subdirectory routing.

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
clawhub install wp-multisite-provisioner-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

WordPress Multisite Provisioner streamlines the creation and configuration of sites within a WordPress Multisite network. It uses wp_insert_site() (WordPress 5.1+) for programmatic site creation with full control over domain, path, and network assignment.
The agent configures new sites via switch_to_blog() context switching, setting theme activation with switch_theme(), plugin activation lists, and site-specific options via update_option(). It supports both subdomain and subdirectory network configurations, handling SUBDOMAIN_INSTALL and DOMAIN_CURRENT_SITE constants.
Includes templates for common site configurations: landing pages, blogs, WooCommerce stores, and LMS setups. Manages network-level settings via update_network_option() including upload quotas, allowed themes, and menu modules. Integrates with WP-CLI wp site create for bulk provisioning and generates Nginx/Apache rewrite rules for subdomain routing. Supports user role mapping across sites with add_user_to_blog().

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-multisite-provisioner-agent/)
