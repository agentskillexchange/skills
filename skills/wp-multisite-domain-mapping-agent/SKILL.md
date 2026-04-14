---
title: "WP Multisite Domain Mapping Agent"
description: "Manages domain mapping configurations across WordPress Multisite networks using the sunrise.php drop-in and WP-CLI&#8217;s site commands. Handles SSL certificate provisioning via Certbot ACME, DNS validation through Cloudflare API, and wp_blogs table updates for custom domain routing."
verification: "security_reviewed"
source: "https://github.com/certbot/certbot"
category:
  - "WordPress & CMS"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "certbot/certbot"
  github_stars: 32972
---
# WP Multisite Domain Mapping Agent

Manages domain mapping configurations across WordPress Multisite networks using the sunrise.php drop-in and WP-CLI&#8217;s site commands. Handles SSL certificate provisioning via Certbot ACME, DNS validation through Cloudflare API, and wp_blogs table updates for custom domain routing.

## Installation

You can install this skill in a few common ways:

1. Browse and install from Agent Skill Exchange in the UI if your client supports it.
2. Install from a local skill folder by copying it into your skills directory.
3. Add it as a git submodule or vendor it into your shared skills repo.
4. Fetch it with your preferred skill or package workflow if the upstream project publishes one.
5. Follow the upstream project documentation for manual setup and dependencies.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-multisite-domain-mapping-agent/)
