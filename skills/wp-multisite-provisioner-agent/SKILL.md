---
name: "WordPress Multisite Provisioner"
description: "Automates WordPress Multisite network site creation using wp_insert_site() and the Sites REST API. Configures per-site themes, plugins, and options via switch_to_blog() with subdomain or subdirectory routing."
category: "WordPress &amp; CMS"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/wp-multisite-provisioner-agent/"
---
# WordPress Multisite Provisioner

Automates WordPress Multisite network site creation using wp_insert_site() and the Sites REST API. Configures per-site themes, plugins, and options via switch_to_blog() with subdomain or subdirectory routing.

## Overview

WordPress Multisite Provisioner streamlines the creation and configuration of sites within a WordPress Multisite network. It uses wp_insert_site() (WordPress 5.1+) for programmatic site creation with full control over domain, path, and network assignment.

The agent configures new sites via switch_to_blog() context switching, setting theme activation with switch_theme(), plugin activation lists, and site-specific options via update_option(). It supports both subdomain and subdirectory network configurations, handling SUBDOMAIN_INSTALL and DOMAIN_CURRENT_SITE constants.

Includes templates for common site configurations: landing pages, blogs, WooCommerce stores, and LMS setups. Manages network-level settings via update_network_option() including upload quotas, allowed themes, and menu modules. Integrates with WP-CLI wp site create for bulk provisioning and generates Nginx/Apache rewrite rules for subdomain routing. Supports user role mapping across sites with add_user_to_blog().

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill wp-multisite-provisioner-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill wp-multisite-provisioner-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill wp-multisite-provisioner-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill wp-multisite-provisioner-agent -a codex
```

### OpenClaw

```bash
clawhub install wp-multisite-provisioner-agent
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-multisite-provisioner-agent/)
