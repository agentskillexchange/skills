---
name: "Nginx Error Log Pattern Analyzer"
description: "Parses Nginx error logs using configurable regex patterns and the GoAccess real-time log analyzer API. Clusters recurring 502/504 errors and correlates with upstream health check failures."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/nginx-error-log-pattern-analyzer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "nginx"  # from ase_tool_match
  github_stars: 29762  # from ase_github_stars (integer, not string)
  github_repo: "nginx/nginx"  # from ase_github_repo
  license: "BSD-2-Clause"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
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

- Marketplace: https://agentskillexchange.com/skills/nginx-error-log-pattern-analyzer/
