---
name: "Nginx Error Log Pattern Analyzer"
description: "Parses Nginx error logs using configurable regex patterns and the GoAccess real-time log analyzer API. Clusters recurring 502/504 errors and correlates with upstream health check failures."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: security_reviewed
source: "https://github.com/nginx/nginx"
tool_ecosystem:
  tool: nginx
  github_stars: 29767
  github_repo: nginx/nginx
  license: BSD-2-Clause
  maintained: true
---
# Nginx Error Log Pattern Analyzer

Parses Nginx error logs using configurable regex patterns and the GoAccess real-time log analyzer API. Clusters recurring 502/504 errors and correlates with upstream health check failures.

## Overview

The Nginx Error Log Pattern Analyzer processes Nginx error log files using configurable regex patterns to extract structured data from error entries. It integrates with the GoAccess real-time web log analyzer API for live dashboard generation and historical trend analysis. The skill clusters recurring error patterns, with special focus on 502 Bad Gateway and 504 Gateway Timeout errors, correlating them with upstream server health check failures and connection timeouts. It parses upstream response times from access logs to identify degrading backend services before they trigger errors. The analyzer supports log rotation detection, compressed log file reading (.gz), and multi-server log aggregation via rsyslog or Filebeat inputs. Output includes frequency heatmaps by hour, top offending upstreams, client IP analysis for potential abuse patterns, and recommended Nginx configuration tuning parameters for proxy_read_timeout, proxy_connect_timeout, and keepalive settings.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-pattern-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-pattern-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-pattern-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-pattern-analyzer -a codex
```

### OpenClaw

```bash
clawhub install nginx-error-log-pattern-analyzer
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nginx-error-log-pattern-analyzer/)
