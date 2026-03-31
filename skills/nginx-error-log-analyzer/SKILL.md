---
name: "Nginx Error Log Analyzer"
description: "Parses and diagnoses Nginx error logs and access logs using pattern matching against known error signatures. Integrates with the Nginx Plus REST API /api/8/ endpoints for real-time upstream health, connection metrics, and SSL certificate expiration monitoring."
category: "Runbooks &amp; Diagnostics"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/nginx-error-log-analyzer/"
---
# Nginx Error Log Analyzer

Parses and diagnoses Nginx error logs and access logs using pattern matching against known error signatures. Integrates with the Nginx Plus REST API /api/8/ endpoints for real-time upstream health, connection metrics, and SSL certificate expiration monitoring.

## Overview

The Nginx Error Log Analyzer skill provides automated diagnosis of web server issues by parsing Nginx error logs, access logs, and real-time metrics. It uses structured log parsing to identify error patterns and correlates them with known Nginx failure modes and misconfigurations.

The skill processes standard Nginx error log format and custom log_format definitions, categorizing errors into connection failures (upstream timeouts, connection refused), SSL/TLS errors (certificate chain issues, protocol mismatches), configuration errors (duplicate location blocks, invalid upstream references), and client errors (413 Request Entity Too Large, 499 Client Closed Request).

For Nginx Plus deployments, it queries the REST API at /api/8/ including /api/8/http/upstreams for backend health status, /api/8/connections for active connection metrics, /api/8/ssl for handshake statistics, and /api/8/http/server_zones for per-virtual-host request rates. The skill generates diagnostic runbooks with specific configuration fixes, including optimized proxy_buffer_size settings, upstream keepalive connection tuning, worker_connections calculations based on traffic patterns, and rate limiting configurations using the limit_req module. It also checks SSL certificate expiration dates and recommends Let's Encrypt renewal commands.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-analyzer -a codex
```

### OpenClaw

```bash
clawhub install nginx-error-log-analyzer
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nginx-error-log-analyzer/)
