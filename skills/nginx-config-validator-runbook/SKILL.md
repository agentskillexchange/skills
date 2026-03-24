---
name: "Nginx Config Validator Runbook"
description: "Validates Nginx configurations using nginx -t syntax checking, the crossplane Python parser for structural analysis, and gixy security analyzer. Detects misconfigurations, SSL issues, and security vulnerabilities."
category: "Runbooks & Diagnostics"
framework: "Claude Agents"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/nginx-config-validator-runbook/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "nginx"  # from ase_tool_match
  github_stars: 29762  # from ase_github_stars (integer, not string)
  github_repo: "nginx/nginx"  # from ase_github_repo
  license: "BSD-2-Clause"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Nginx Config Validator Runbook

Validates Nginx configurations using nginx -t syntax checking, the crossplane Python parser for structural analysis, and gixy security analyzer. Detects misconfigurations, SSL issues, and security vulnerabilities.

## Overview

The Nginx Config Validator Runbook skill automates the validation and security analysis of Nginx web server configurations. It executes nginx -t for syntax validation and configuration file parsing verification before applying changes. The crossplane Python library provides programmatic parsing of Nginx configuration files into structured AST representations, enabling directive-level analysis across included files and upstream definitions. The gixy security analyzer scans configurations for common vulnerabilities including SSRF via proxy_pass misconfigurations, HTTP splitting through improper header handling, and path traversal in alias directives. The runbook validates SSL/TLS configurations checking certificate chain completeness, cipher suite strength against Mozilla recommended profiles, and OCSP stapling configuration. Performance analysis covers worker_processes optimization based on CPU cores, connection and buffer sizing, keepalive timeout tuning, and gzip compression settings. Rate limiting configurations are validated for proper zone sizing, burst allowances, and status code handling. The skill checks location block ordering for precedence issues, validates regular expression correctness in location directives, and detects conflicting server_name declarations across virtual hosts. Upstream health check configurations are verified for appropriate fail_timeout, max_fails, and backup server designations. Output includes a prioritized findings report with severity levels, specific line references, and corrective configuration snippets.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill nginx-config-validator-runbook
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill nginx-config-validator-runbook -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill nginx-config-validator-runbook -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill nginx-config-validator-runbook -a codex
```

### OpenClaw

```bash
clawhub install nginx-config-validator-runbook
```

## Source

- Marketplace: https://agentskillexchange.com/skills/nginx-config-validator-runbook/
