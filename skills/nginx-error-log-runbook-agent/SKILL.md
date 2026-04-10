---
title: "Nginx Error Log Runbook Agent"
description: "Automates Nginx error diagnosis using nginx -T configuration dump, error.log pattern matching, and the Nginx Plus REST API /api/8/http/upstreams endpoint. Resolves 502 Bad Gateway, SSL handshake failures, and upstream timeout issues."
slug: "nginx-error-log-runbook-agent"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/nginx-error-log-runbook-agent/"
---

# Nginx Error Log Runbook Agent

Automates Nginx error diagnosis using nginx -T configuration dump, error.log pattern matching, and the Nginx Plus REST API /api/8/http/upstreams endpoint. Resolves 502 Bad Gateway, SSL handshake failures, and upstream timeout issues.

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
clawhub install nginx-error-log-runbook-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Nginx Error Log Runbook Agent provides automated diagnosis and remediation guidance for common Nginx web server issues. It parses error.log files using structured pattern matching to categorize errors into upstream connectivity failures, SSL/TLS handshake errors, configuration syntax problems, and resource exhaustion conditions.
The agent uses nginx -T to dump the full resolved configuration, identifying directive conflicts across included files, misconfigured location blocks, and invalid upstream server definitions. For Nginx Plus deployments, it queries the /api/8/http/upstreams endpoint to check upstream server health status, active connection counts, and response time metrics in real-time.
For 502 Bad Gateway errors, it traces the connection path from Nginx to backend servers using the proxy_pass configuration, validates DNS resolution via dig/nslookup, and checks backend port availability with netstat and ss utilities. SSL issues are diagnosed by inspecting certificate chains with openssl s_client, checking OCSP stapling status via the Nginx OCSP responder configuration, and validating cipher suite compatibility. The agent generates step-by-step runbook procedures with exact commands for each resolution path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nginx-error-log-runbook-agent/)
