---
title: "WP Multisite Domain Mapping Agent"
description: "Manages domain mapping configurations across WordPress Multisite networks using the sunrise.php drop-in and WP-CLI's site commands. Handles SSL certificate provisioning via Certbot ACME, DNS validation through Cloudflare API, and wp_blogs table updates for custom domain routing."
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

Manages domain mapping configurations across WordPress Multisite networks using the sunrise.php drop-in and WP-CLI's site commands. Handles SSL certificate provisioning via Certbot ACME, DNS validation through Cloudflare API, and wp_blogs table updates for custom domain routing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/wp-multisite-domain-mapping-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/wp-multisite-domain-mapping-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/wp-multisite-domain-mapping-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-multisite-domain-mapping-agent/)
