---
name: "Caddy Automatic HTTPS Web Server and Reverse Proxy"
description: "Caddy is a fast, extensible web server written in Go that provides automatic HTTPS via Let's Encrypt and ZeroSSL. It supports HTTP/1.1, HTTP/2, and HTTP/3, features a simple Caddyfile configuration format, a powerful JSON API for dynamic config, and serves as a production-grade reverse proxy with zero external dependencies."
verification: security_reviewed
source: "https://github.com/caddyserver/caddy"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "caddyserver/caddy"
  github_stars: 71224
---

# Caddy Automatic HTTPS Web Server and Reverse Proxy

Caddy is an open-source, enterprise-ready web server written in Go that distinguishes itself through automatic HTTPS by default. Created by Matt Holt and maintained by the Caddy community, it automatically obtains, renews, and manages TLS certificates from Let's Encrypt and ZeroSSL for public-facing sites, and runs a fully-managed local CA for internal names and IP addresses.
Configuration
Caddy offers two configuration approaches: the Caddyfile, a human-readable format designed for simplicity (example.com { respond "Hello" }), and a native JSON configuration for full programmatic control. The JSON API allows dynamic configuration changes at runtime without server restarts, making it ideal for automation and agent-driven infrastructure management.
Core Features
The server supports HTTP/1.1, HTTP/2, and HTTP/3 simultaneously, handles Encrypted ClientHello (ECH), and scales to hundreds of thousands of sites as proven in production. Its modular architecture allows extending functionality without bloat — modules exist for rate limiting, caching, authentication, load balancing, and more. Caddy runs as a single static binary with zero external dependencies, not even libc.
Agent Skill Integration
As an agent skill, Caddy is valuable for quickly provisioning HTTPS-enabled development or staging servers, configuring reverse proxies for microservices, setting up static file serving with automatic TLS, and managing multi-site configurations. Agents can use the Caddy API to dynamically add or remove routes, inspect server state, and reload configuration. The caddy file-server command instantly serves files over HTTPS, and caddy reverse-proxy sets up a proxy in a single command.
Production Readiness
Caddy has served trillions of requests in production and managed millions of TLS certificates. It features On-Demand TLS for customer-owned domains, can coordinate with other Caddy instances in a cluster, and supports multi-issuer fallback for certificate resilience. The Apache 2.0 licensed project has an active community and regular releases.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/caddy-automatic-https-web-server-reverse-proxy/)
