---
name: "WordOps High-Performance WordPress Server Stack Manager"
description: "WordOps is an open-source CLI tool that installs and manages a complete high-performance WordPress server stack with Nginx, PHP, MariaDB, and Redis in a few keystrokes. It handles site creation, SSL certificates via Let’s Encrypt, server hardening, and cache configuration for optimal WordPress performance."
category: "WordPress & CMS"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/WordOps/WordOps"
---
# WordOps High-Performance WordPress Server Stack Manager

WordOps is an open-source CLI tool that installs and manages a complete high-performance WordPress server stack with Nginx, PHP, MariaDB, and Redis in a few keystrokes. It handles site creation, SSL certificates via Let’s Encrypt, server hardening, and cache configuration for optimal WordPress performance.

## Overview

WordOps is a Python-based command-line tool for installing and managing complete WordPress hosting stacks on Ubuntu and Debian servers. With a single installation command, WordOps sets up a production-ready environment including a custom-built Nginx with HTTP/3 QUIC and Brotli support, multiple PHP versions (7.4 through 8.4), MariaDB 11.4 LTS, and Redis 7.0 for object caching.

The tool dramatically simplifies WordPress server administration. Creating a new WordPress site with full SSL and caching is as simple as running `sudo wo site create example.com --wp --letsencrypt`. WordOps handles Nginx virtual host configuration, PHP-FPM pool setup, database creation, WordPress installation, and Let’s Encrypt certificate provisioning — all automatically. It supports domain, subdomain, and wildcard SSL certificates with DNS API integration for automated renewal.

WordOps provides multiple cache backend options including Nginx fastcgi_cache, Redis full-page cache, and wp-super-cache integration. Each cache strategy comes with pre-optimized Nginx configurations that include strict security directives for WordPress — blocking access to sensitive files, preventing PHP execution in upload directories, and enforcing proper headers. The tool achieves Grade A+ SSL ratings on Qualys SSL Labs out of the box.

Installation is straightforward: `wget -qO wo wops.cc && sudo bash wo`. The tool includes a web-based dashboard for monitoring server status, resource usage, and site health. It also supports migration from EasyEngine v3, making it a natural upgrade path for existing WordPress hosting setups.

For agent skills focused on WordPress infrastructure management, WordOps provides the automation layer needed to provision, configure, and maintain WordPress servers programmatically. An agent can use WordOps to create staging environments, manage SSL certificates, switch cache backends, update PHP versions, and monitor server health — all through clean CLI commands that integrate naturally into automated DevOps workflows. With over 1,500 GitHub stars and regular release cycles, WordOps is actively maintained and widely used in production WordPress hosting.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill wordops-high-performance-wordpress-server-stack
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill wordops-high-performance-wordpress-server-stack -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill wordops-high-performance-wordpress-server-stack -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill wordops-high-performance-wordpress-server-stack -a codex
```

### OpenClaw

```bash
clawhub install wordops-high-performance-wordpress-server-stack
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wordops-high-performance-wordpress-server-stack/)
