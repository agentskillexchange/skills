---
name: "Nginx Error Log Analyzer and Fixer"
description: "Parses Nginx error logs and access logs to diagnose 502, 504, and 413 errors. Uses GoAccess for real-time log visualization and integrates with nginx -t for configuration validation."
category: "Runbooks & Diagnostics"
framework: "Claude Agents"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/nginx-error-log-analyzer-fixer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "nginx"  # from ase_tool_match
  github_stars: 29762  # from ase_github_stars (integer, not string)
  github_repo: "nginx/nginx"  # from ase_github_repo
  license: "BSD-2-Clause"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Nginx Error Log Analyzer and Fixer

Parses Nginx error logs and access logs to diagnose 502, 504, and 413 errors. Uses GoAccess for real-time log visualization and integrates with nginx -t for configuration validation.

## Overview

This skill automates Nginx troubleshooting by parsing error logs and access logs to identify recurring issues and their root causes. It processes logs using GoAccess for real-time statistical analysis, generating reports on error rate trends, upstream timeout patterns, and client error distributions. For 502 Bad Gateway errors, it checks upstream server health, FastCGI/proxy_pass configurations, and backend service status via systemctl. For 504 Gateway Timeouts, it analyzes proxy_read_timeout and fastcgi_read_timeout settings against actual response times. The skill validates configuration changes with nginx -t before applying them, and uses nginx -T to dump the full effective configuration for analysis. It integrates with fail2ban log parsing to correlate security events with error spikes. The analyzer generates remediation scripts that adjust buffer sizes, timeout values, worker_connections, and rate limiting rules, with before/after configuration diffs for review.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-analyzer-fixer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-analyzer-fixer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-analyzer-fixer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-analyzer-fixer -a codex
```

### OpenClaw

```bash
clawhub install nginx-error-log-analyzer-fixer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/nginx-error-log-analyzer-fixer/
