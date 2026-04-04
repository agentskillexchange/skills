---
name: "WP Multisite Domain Mapping Agent"
category: "WordPress & CMS"
verification: "security_reviewed"
source: "https://github.com/certbot/certbot"
tool_ecosystem:
  github_repo: "certbot/certbot"
  github_stars: 32959
---

# WP Multisite Domain Mapping Agent

Manages domain mapping configurations across WordPress Multisite networks using the sunrise.php drop-in and WP-CLI’s site commands. Handles SSL certificate provisioning via Certbot ACME, DNS validation through Cloudflare API, and wp_blogs table updates for custom domain routing.

## Installation

Install this skill using one of the following methods:

```bash
# ClawHub CLI
clawhub install wp-multisite-domain-mapping-agent

# OpenClaw CLI
openclaw skills install wp-multisite-domain-mapping-agent

# Chat command
/skill install wp-multisite-domain-mapping-agent

# Direct download
curl -L https://agentskillexchange.com/skills/wp-multisite-domain-mapping-agent/download -o wp-multisite-domain-mapping-agent.zip

# Git clone this repo and copy the skill folder
cp -r skills/wp-multisite-domain-mapping-agent ~/.openclaw/workspace/skills/
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-multisite-domain-mapping-agent/)
