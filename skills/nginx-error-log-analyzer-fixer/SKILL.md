---
name: Nginx Error Log Analyzer and Fixer
description: Parses Nginx error logs and access logs to diagnose 502, 504, and 413
  errors. Uses GoAccess for real-time log visualization and integrates with nginx
  -t for configuration validation.
verification: security_reviewed
source: https://agentskillexchange.com/skills/nginx-error-log-analyzer-fixer/
category:
- Runbooks &amp; Diagnostics
framework:
- Claude Agents
---
# Nginx Error Log Analyzer and Fixer

This skill automates Nginx troubleshooting by parsing error logs and access logs to identify recurring issues and their root causes. It processes logs using GoAccess for real-time statistical analysis, generating reports on error rate trends, upstream timeout patterns, and client error distributions. For 502 Bad Gateway errors, it checks upstream server health, FastCGI/proxy_pass configurations, and backend service status via systemctl. For 504 Gateway Timeouts, it analyzes proxy_read_timeout and fastcgi_read_timeout settings against actual response times. The skill validates configuration changes with nginx -t before applying them, and uses nginx -T to dump the full effective configuration for analysis. It integrates with fail2ban log parsing to correlate security events with error spikes. The analyzer generates remediation scripts that adjust buffer sizes, timeout values, worker_connections, and rate limiting rules, with before/after configuration diffs for review.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nginx-error-log-analyzer-fixer/)
