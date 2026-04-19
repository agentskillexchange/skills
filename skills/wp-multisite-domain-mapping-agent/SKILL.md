---
title: "WP Multisite Domain Mapping Agent"
description: "WP Multisite Domain Mapping Agent handles the complete domain mapping lifecycle for WordPress Multisite installations. It configures the sunrise.php drop-in for early domain resolution, manages the wp_blogs and wp_site tables for network routing, and coordinates SSL provisioning through Certbot&#8217;s ACME protocol with DNS-01 challenges via the Cloudflare API. New domain mappings are provisioned by updating the DOMAIN_CURRENT_SITE constant context, creating DNS records through Cloudflare&#8217;s /zones/{zone_id}/dns_records endpoint, and waiting for propagation before triggering Certbot with &#8211;preferred-challenges dns-01. The agent runs WP-CLI commands like wp site create, wp option update, and wp search-replace for URL migration across the network. Health monitoring checks SSL certificate expiry dates, validates DNS resolution against expected IP addresses, and tests HTTP-to-HTTPS redirects. For subdomain-to-custom-domain transitions, it handles the wp_sitemeta updates, rewrites .htaccess or Nginx server blocks, and flushes object cache groups. Rollback capability maintains the previous DNS and WordPress configuration state for safe reversion."
source: "https://github.com/certbot/certbot"
verification: "security_reviewed"
category:
  - "WordPress &amp; CMS"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "certbot/certbot"
  github_stars: 32972
---

# WP Multisite Domain Mapping Agent

WP Multisite Domain Mapping Agent handles the complete domain mapping lifecycle for WordPress Multisite installations. It configures the sunrise.php drop-in for early domain resolution, manages the wp_blogs and wp_site tables for network routing, and coordinates SSL provisioning through Certbot&#8217;s ACME protocol with DNS-01 challenges via the Cloudflare API. New domain mappings are provisioned by updating the DOMAIN_CURRENT_SITE constant context, creating DNS records through Cloudflare&#8217;s /zones/{zone_id}/dns_records endpoint, and waiting for propagation before triggering Certbot with &#8211;preferred-challenges dns-01. The agent runs WP-CLI commands like wp site create, wp option update, and wp search-replace for URL migration across the network. Health monitoring checks SSL certificate expiry dates, validates DNS resolution against expected IP addresses, and tests HTTP-to-HTTPS redirects. For subdomain-to-custom-domain transitions, it handles the wp_sitemeta updates, rewrites .htaccess or Nginx server blocks, and flushes object cache groups. Rollback capability maintains the previous DNS and WordPress configuration state for safe reversion.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-multisite-domain-mapping-agent/)
