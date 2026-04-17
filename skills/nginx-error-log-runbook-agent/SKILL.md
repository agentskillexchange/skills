---
title: "Nginx Error Log Runbook Agent"
description: "Automates Nginx error diagnosis using nginx -T configuration dump, error.log pattern matching, and the Nginx Plus REST API /api/8/http/upstreams endpoint. Resolves 502 Bad Gateway, SSL handshake failures, and upstream timeout issues."
verification: security_reviewed
source: "https://github.com/nginx/nginx"
category:
  - "Runbooks & Diagnostics"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "nginx/nginx"
  github_stars: 29930
  license: "BSD-2-Clause"
---

# Nginx Error Log Runbook Agent

The Nginx Error Log Runbook Agent provides automated diagnosis and remediation guidance for common Nginx web server issues. It parses error.log files using structured pattern matching to categorize errors into upstream connectivity failures, SSL/TLS handshake errors, configuration syntax problems, and resource exhaustion conditions.

The agent uses nginx -T to dump the full resolved configuration, identifying directive conflicts across included files, misconfigured location blocks, and invalid upstream server definitions. For Nginx Plus deployments, it queries the /api/8/http/upstreams endpoint to check upstream server health status, active connection counts, and response time metrics in real-time.

For 502 Bad Gateway errors, it traces the connection path from Nginx to backend servers using the proxy_pass configuration, validates DNS resolution via dig/nslookup, and checks backend port availability with netstat and ss utilities. SSL issues are diagnosed by inspecting certificate chains with openssl s_client, checking OCSP stapling status via the Nginx OCSP responder configuration, and validating cipher suite compatibility. The agent generates step-by-step runbook procedures with exact commands for each resolution path.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/nginx-error-log-runbook-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/nginx-error-log-runbook-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nginx-error-log-runbook-agent/)
