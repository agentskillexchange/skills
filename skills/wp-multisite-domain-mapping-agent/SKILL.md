---
title: WP Multisite Domain Mapping Agent
description: WP Multisite Domain Mapping Agent handles the complete domain mapping
  lifecycle for WordPress Multisite installations. It configures the sunrise.php drop-in
  for early domain resolution, manages the wp_blogs and wp_site tables for network
  routing, and coordinates SSL provisioning through Certbot’s ACME protocol with DNS-01
  challenges via the Cloudflare API. New domain mappings are provisioned by updating
  the DOMAIN_CURRENT_SITE constant context, creating DNS records through Cloudflare’s
  /zones/{zone_id}/dns_records endpoint, and waiting for propagation before triggering
  Certbot with –preferred-challenges dns-01. The agent runs WP-CLI commands like wp
  site create, wp option update, and wp search-replace for URL migration across the
  network. Health monitoring checks SSL certificate expiry dates, validates DNS resolution
  against expected IP addresses, and tests HTTP-to-HTTPS redirects. For subdomain-to-custom-domain
  transitions, it handles the wp_sitemeta updates, rewrites .htaccess or Nginx server
  blocks, and flushes object cache groups. Rollback capability maintains the previous
  DNS and WordPress configuration state for safe reversion.
verification: security_reviewed
source: https://github.com/certbot/certbot
category:
- WordPress &amp; CMS
framework:
- Custom Agents
tool_ecosystem:
  github_repo: certbot/certbot
  github_stars: 32959
---

# WP Multisite Domain Mapping Agent

WP Multisite Domain Mapping Agent handles the complete domain mapping lifecycle for WordPress Multisite installations. It configures the sunrise.php drop-in for early domain resolution, manages the wp_blogs and wp_site tables for network routing, and coordinates SSL provisioning through Certbot’s ACME protocol with DNS-01 challenges via the Cloudflare API. New domain mappings are provisioned by updating the DOMAIN_CURRENT_SITE constant context, creating DNS records through Cloudflare’s /zones/{zone_id}/dns_records endpoint, and waiting for propagation before triggering Certbot with –preferred-challenges dns-01. The agent runs WP-CLI commands like wp site create, wp option update, and wp search-replace for URL migration across the network. Health monitoring checks SSL certificate expiry dates, validates DNS resolution against expected IP addresses, and tests HTTP-to-HTTPS redirects. For subdomain-to-custom-domain transitions, it handles the wp_sitemeta updates, rewrites .htaccess or Nginx server blocks, and flushes object cache groups. Rollback capability maintains the previous DNS and WordPress configuration state for safe reversion.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-multisite-domain-mapping-agent/)
