---
title: "WP Multisite Domain Mapping Agent"
description: "Manages domain mapping configurations across WordPress Multisite networks using the sunrise.php drop-in and WP-CLI’s site commands. Handles SSL certificate provisioning via Certbot ACME, DNS validation through Cloudflare API, and wp_blogs table updates for custom domain routing."
verification: security_reviewed
source: "https://github.com/certbot/certbot"
category:
  - "WordPress &amp; CMS"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "certbot/certbot"
  github_stars: 32972
---

# WP Multisite Domain Mapping Agent

WP Multisite Domain Mapping Agent handles the complete domain mapping lifecycle for WordPress Multisite installations. It configures the sunrise.php drop-in for early domain resolution, manages the wp_blogs and wp_site tables for network routing, and coordinates SSL provisioning through Certbot’s ACME protocol with DNS-01 challenges via the Cloudflare API.

New domain mappings are provisioned by updating the DOMAIN_CURRENT_SITE constant context, creating DNS records through Cloudflare’s /zones/{zone_id}/dns_records endpoint, and waiting for propagation before triggering Certbot with –preferred-challenges dns-01. The agent runs WP-CLI commands like wp site create, wp option update, and wp search-replace for URL migration across the network.

Health monitoring checks SSL certificate expiry dates, validates DNS resolution against expected IP addresses, and tests HTTP-to-HTTPS redirects. For subdomain-to-custom-domain transitions, it handles the wp_sitemeta updates, rewrites .htaccess or Nginx server blocks, and flushes object cache groups. Rollback capability maintains the previous DNS and WordPress configuration state for safe reversion.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-multisite-domain-mapping-agent/)
