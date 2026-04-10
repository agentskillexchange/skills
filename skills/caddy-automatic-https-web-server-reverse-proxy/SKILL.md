---
title: "Caddy Automatic HTTPS Web Server and Reverse Proxy"
description: "Caddy is a fast, extensible web server written in Go that provides automatic HTTPS via Let’s Encrypt and ZeroSSL. It supports HTTP/1.1, HTTP/2, and HTTP/3, features a simple Caddyfile configuration format, a powerful JSON API for dynamic config, and serves as a production-grade reverse proxy with zero external dependencies."
slug: "caddy-automatic-https-web-server-reverse-proxy"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/caddyserver/caddy"
tool_ecosystem:
  github_repo: "caddyserver/caddy"
  github_stars: 71224
---

# Caddy Automatic HTTPS Web Server and Reverse Proxy

Caddy is a fast, extensible web server written in Go that provides automatic HTTPS via Let’s Encrypt and ZeroSSL. It supports HTTP/1.1, HTTP/2, and HTTP/3, features a simple Caddyfile configuration format, a powerful JSON API for dynamic config, and serves as a production-grade reverse proxy with zero external dependencies.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install caddy-automatic-https-web-server-reverse-proxy
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Caddy is an open-source, enterprise-ready web server written in Go that distinguishes itself through automatic HTTPS by default. Created by Matt Holt and maintained by the Caddy community, it automatically obtains, renews, and manages TLS certificates from Let’s Encrypt and ZeroSSL for public-facing sites, and runs a fully-managed local CA for internal names and IP addresses.
Configuration
Caddy offers two configuration approaches: the Caddyfile, a human-readable format designed for simplicity (example.com { respond "Hello" }), and a native JSON configuration for full programmatic control. The JSON API allows dynamic configuration changes at runtime without server restarts, making it ideal for automation and agent-driven infrastructure management.
Core Features
The server supports HTTP/1.1, HTTP/2, and HTTP/3 simultaneously, handles Encrypted ClientHello (ECH), and scales to hundreds of thousands of sites as proven in production. Its modular architecture allows extending functionality without bloat — modules exist for rate limiting, caching, authentication, load balancing, and more. Caddy runs as a single static binary with zero external dependencies, not even libc.
Agent Skill Integration
As an agent skill, Caddy is valuable for quickly provisioning HTTPS-enabled development or staging servers, configuring reverse proxies for microservices, setting up static file serving with automatic TLS, and managing multi-site configurations. Agents can use the Caddy API to dynamically add or remove routes, inspect server state, and reload configuration. The caddy file-server command instantly serves files over HTTPS, and caddy reverse-proxy sets up a proxy in a single command.
Production Readiness
Caddy has served trillions of requests in production and managed millions of TLS certificates. It features On-Demand TLS for customer-owned domains, can coordinate with other Caddy instances in a cluster, and supports multi-issuer fallback for certificate resilience. The Apache 2.0 licensed project has an active community and regular releases.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/caddy-automatic-https-web-server-reverse-proxy/)
