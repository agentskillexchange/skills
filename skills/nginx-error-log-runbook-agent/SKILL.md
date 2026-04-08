---
title: Nginx Error Log Runbook Agent
description: The Nginx Error Log Runbook Agent provides automated diagnosis and remediation
  guidance for common Nginx web server issues. It parses error.log files using structured
  pattern matching to categorize errors into upstream connectivity failures, SSL/TLS
  handshake errors, configuration syntax problems, and resource exhaustion conditions.
  The agent uses nginx -T to dump the full resolved configuration, identifying directive
  conflicts across included files, misconfigured location blocks, and invalid upstream
  server definitions. For Nginx Plus deployments, it queries the /api/8/http/upstreams
  endpoint to check upstream server health status, active connection counts, and response
  time metrics in real-time. For 502 Bad Gateway errors, it traces the connection
  path from Nginx to backend servers using the proxy_pass configuration, validates
  DNS resolution via dig/nslookup, and checks backend port availability with netstat
  and ss utilities. SSL issues are diagnosed by inspecting certificate chains with
  openssl s_client, checking OCSP stapling status via the Nginx OCSP responder configuration,
  and validating cipher suite compatibility. The agent generates step-by-step runbook
  procedures with exact commands for each resolution path.
verification: security_reviewed
source: https://agentskillexchange.com/skills/nginx-error-log-runbook-agent/
category:
- Runbooks &amp; Diagnostics
framework:
- ChatGPT Agents
---

# Nginx Error Log Runbook Agent

The Nginx Error Log Runbook Agent provides automated diagnosis and remediation guidance for common Nginx web server issues. It parses error.log files using structured pattern matching to categorize errors into upstream connectivity failures, SSL/TLS handshake errors, configuration syntax problems, and resource exhaustion conditions. The agent uses nginx -T to dump the full resolved configuration, identifying directive conflicts across included files, misconfigured location blocks, and invalid upstream server definitions. For Nginx Plus deployments, it queries the /api/8/http/upstreams endpoint to check upstream server health status, active connection counts, and response time metrics in real-time. For 502 Bad Gateway errors, it traces the connection path from Nginx to backend servers using the proxy_pass configuration, validates DNS resolution via dig/nslookup, and checks backend port availability with netstat and ss utilities. SSL issues are diagnosed by inspecting certificate chains with openssl s_client, checking OCSP stapling status via the Nginx OCSP responder configuration, and validating cipher suite compatibility. The agent generates step-by-step runbook procedures with exact commands for each resolution path.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nginx-error-log-runbook-agent/)
