---
name: "Nginx Error Log Runbook Agent"
description: "Automates Nginx error diagnosis using nginx -T configuration dump, error.log pattern matching, and the Nginx Plus REST API /api/8/http/upstreams endpoint. Resolves 502 Bad Gateway, SSL handshake failures, and upstream timeout issues."
category: "Runbooks &amp; Diagnostics"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/nginx-error-log-runbook-agent/"
---
# Nginx Error Log Runbook Agent

Automates Nginx error diagnosis using nginx -T configuration dump, error.log pattern matching, and the Nginx Plus REST API /api/8/http/upstreams endpoint. Resolves 502 Bad Gateway, SSL handshake failures, and upstream timeout issues.

## Overview

The Nginx Error Log Runbook Agent provides automated diagnosis and remediation guidance for common Nginx web server issues. It parses error.log files using structured pattern matching to categorize errors into upstream connectivity failures, SSL/TLS handshake errors, configuration syntax problems, and resource exhaustion conditions.

The agent uses nginx -T to dump the full resolved configuration, identifying directive conflicts across included files, misconfigured location blocks, and invalid upstream server definitions. For Nginx Plus deployments, it queries the /api/8/http/upstreams endpoint to check upstream server health status, active connection counts, and response time metrics in real-time.

For 502 Bad Gateway errors, it traces the connection path from Nginx to backend servers using the proxy_pass configuration, validates DNS resolution via dig/nslookup, and checks backend port availability with netstat and ss utilities. SSL issues are diagnosed by inspecting certificate chains with openssl s_client, checking OCSP stapling status via the Nginx OCSP responder configuration, and validating cipher suite compatibility. The agent generates step-by-step runbook procedures with exact commands for each resolution path.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-runbook-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-runbook-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-runbook-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-runbook-agent -a codex
```

### OpenClaw

```bash
clawhub install nginx-error-log-runbook-agent
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nginx-error-log-runbook-agent/)
