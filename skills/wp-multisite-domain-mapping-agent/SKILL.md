---
title: "WP Multisite Domain Mapping Agent"
slug: "wp-multisite-domain-mapping-agent"
description: "Manages domain mapping configurations across WordPress Multisite networks using the sunrise.php drop-in and WP-CLI's site commands. Handles SSL certificate provisioning via Certbot ACME, DNS validation through Cloudflare API, and wp_blogs table updates for custom domain routing."
category:
  - "WordPress &amp; CMS"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://github.com/certbot/certbot"
tool_ecosystem:
  github_repo: "certbot/certbot"
  github_stars: 32959
---

# WP Multisite Domain Mapping Agent

Manages domain mapping configurations across WordPress Multisite networks using the sunrise.php drop-in and WP-CLI's site commands. Handles SSL certificate provisioning via Certbot ACME, DNS validation through Cloudflare API, and wp_blogs table updates for custom domain routing.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange catalog in your compatible client.
2. Clone or download this repository and copy the skill folder into your local skills directory.
3. Add it as a git submodule inside your skills collection.
4. Use a package or automation workflow that syncs skills from this repository.
5. Install directly from the original upstream project if you prefer to track source releases.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-multisite-domain-mapping-agent/)
