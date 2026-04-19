---
title: "WordPress Multisite Provisioner"
description: "WordPress Multisite Provisioner streamlines the creation and configuration of sites within a WordPress Multisite network. It uses wp_insert_site() (WordPress 5.1+) for programmatic site creation with full control over domain, path, and network assignment. The agent configures new sites via switch_to_blog() context switching, setting theme activation with switch_theme() , plugin activation lists, and site-specific options via update_option() . It supports both subdomain and subdirectory network configurations, handling SUBDOMAIN_INSTALL and DOMAIN_CURRENT_SITE constants. Includes templates for common site configurations: landing pages, blogs, WooCommerce stores, and LMS setups. Manages network-level settings via update_network_option() including upload quotas, allowed themes, and menu modules. Integrates with WP-CLI wp site create for bulk provisioning and generates Nginx/Apache rewrite rules for subdomain routing. Supports user role mapping across sites with add_user_to_blog() ."
source: "https://github.com/WordPress/WordPress"
verification: "security_reviewed"
category:
  - "WordPress &amp; CMS"
framework:
  - "ChatGPT Agents"
---

# WordPress Multisite Provisioner

WordPress Multisite Provisioner streamlines the creation and configuration of sites within a WordPress Multisite network. It uses wp_insert_site() (WordPress 5.1+) for programmatic site creation with full control over domain, path, and network assignment. The agent configures new sites via switch_to_blog() context switching, setting theme activation with switch_theme() , plugin activation lists, and site-specific options via update_option() . It supports both subdomain and subdirectory network configurations, handling SUBDOMAIN_INSTALL and DOMAIN_CURRENT_SITE constants. Includes templates for common site configurations: landing pages, blogs, WooCommerce stores, and LMS setups. Manages network-level settings via update_network_option() including upload quotas, allowed themes, and menu modules. Integrates with WP-CLI wp site create for bulk provisioning and generates Nginx/Apache rewrite rules for subdomain routing. Supports user role mapping across sites with add_user_to_blog() .

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-multisite-provisioner-agent/)
