---
title: "WP Multisite Domain Mapping Agent"
description: "Manages domain mapping configurations across WordPress Multisite networks using the sunrise.php drop-in and WP-CLI&#8217;s site commands. Handles SSL certificate provisioning via Certbot ACME, DNS validation through Cloudflare API, and wp_blogs table updates for custom domain routing."
verification: security_reviewed
source: "https://github.com/certbot/certbot"
category:
  - "WordPress &amp; CMS"
tool_ecosystem:
  github_repo: "certbot/certbot"
  github_stars: 32972
---

# WP Multisite Domain Mapping Agent

Manages domain mapping configurations across WordPress Multisite networks using the sunrise.php drop-in and WP-CLI&#8217;s site commands. Handles SSL certificate provisioning via Certbot ACME, DNS validation through Cloudflare API, and wp_blogs table updates for custom domain routing.

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
