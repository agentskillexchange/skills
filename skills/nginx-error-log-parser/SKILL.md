---
name: "Nginx Error Log Parser"
description: "Parses nginx error.log and access.log files using pattern matching for 5xx status codes, upstream timeouts, and SSL handshake failures. Correlates error spikes with nginx -T configuration dumps to identify misconfigured proxy_pass and keepalive settings."
category: "Developer Tools"
framework: "Cursor"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/nginx-error-log-parser/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "nginx"  # from ase_tool_match
  github_stars: 29762  # from ase_github_stars (integer, not string)
  github_repo: "nginx/nginx"  # from ase_github_repo
  license: "BSD-2-Clause"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Nginx Error Log Parser

Parses nginx error.log and access.log files using pattern matching for 5xx status codes, upstream timeouts, and SSL handshake failures. Correlates error spikes with nginx -T configuration dumps to identify misconfigured proxy_pass and keepalive settings.

## Overview

The Nginx Error Log Parser skill provides systematic web server diagnostics by analyzing nginx log files and configuration. It parses error.log entries to categorize issues by type including upstream connection failures, SSL errors, client errors, and worker-level issues. The skill processes access.log to identify 5xx response patterns, calculating error rates per upstream backend, per URI path, and per time window. It runs nginx -T to dump the effective configuration and cross-references error patterns with timeout settings, worker_connections, keepalive directives, and upstream server weights. The skill detects common misconfigurations including missing proxy_set_header Host, incorrect proxy_pass trailing slashes changing URI behavior, and buffer size mismatches causing upstream response truncation. Output includes error frequency analysis, configuration fix recommendations, and nginx reload commands.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-parser
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-parser -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-parser -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-parser -a codex
```

### OpenClaw

```bash
clawhub install nginx-error-log-parser
```

## Source

- Marketplace: https://agentskillexchange.com/skills/nginx-error-log-parser/
