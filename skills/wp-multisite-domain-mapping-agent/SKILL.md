---
title: "WP Multisite Domain Mapping Agent"
slug: "wp-multisite-domain-mapping-agent"
verification: "security_reviewed"
description: "Manages domain mapping configurations across WordPress Multisite networks using the sunrise.php drop-in and WP-CLI’s site commands. Handles SSL certificate provisioning via Certbot ACME, DNS validation through Cloudflare API, and wp_blogs table updates for custom domain routing."
category:
  - "WordPress &amp; CMS"
framework:
  - "Custom Agents"
source: "https://github.com/certbot/certbot"
tool_ecosystem:
  github_repo: "certbot/certbot"
  github_stars: 32959
---

# WP Multisite Domain Mapping Agent

Manages domain mapping configurations across WordPress Multisite networks using the sunrise.php drop-in and WP-CLI’s site commands. Handles SSL certificate provisioning via Certbot ACME, DNS validation through Cloudflare API, and wp_blogs table updates for custom domain routing.

## Installation

Choose the setup path that fits your environment:

1. Clone or download this skill into your local skills workspace.
2. Install it with ClawHub if it is available there.
3. Copy the folder into your OpenClaw or AgentSkills directory manually.
4. Add it as a git submodule if you manage skills as pinned dependencies.
5. Vendor it directly into a project repo when you need a fixed internal copy.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-multisite-domain-mapping-agent/)
