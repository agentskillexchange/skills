---
name: "Nginx Config Linter and Tester"
description: "Validates nginx.conf files using the gixy static analyzer and crossplane parser library. Tests configuration for security misconfigs, HTTP header issues, and performs dry-run validation via nginx -t subprocess invocation."
category: "Runbooks &amp; Diagnostics"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://github.com/nginx/nginx"
tool_ecosystem:
  tool: nginx
  github_repo: nginx/nginx
  github_stars: 29767
  license: BSD-2-Clause
  maintained: true
---
# Nginx Config Linter and Tester

Validates nginx.conf files using the gixy static analyzer and crossplane parser library. Tests configuration for security misconfigs, HTTP header issues, and performs dry-run validation via nginx -t subprocess invocation.

## Overview

The Nginx Config Linter and Tester skill provides comprehensive validation and security analysis for Nginx web server configurations. It combines multiple analysis tools for thorough configuration auditing.

The skill uses the gixy static analyzer to detect common Nginx security misconfigurations including SSRF via proxy_pass, HTTP splitting vulnerabilities, and improper alias path traversal. It parses configuration files using the crossplane Python library for structural validation.

Configuration testing includes dry-run validation via nginx -t subprocess execution, verifying syntax correctness and file reference integrity. The skill checks for missing security headers (HSTS, CSP, X-Frame-Options), improper SSL/TLS configurations, and weak cipher suite selections.

Advanced features include upstream health check configuration validation, rate limiting rule analysis, and gzip compression settings optimization. The skill generates remediation suggestions with corrected configuration snippets and links to Nginx documentation for each finding.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill nginx-config-linter-tester
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill nginx-config-linter-tester -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill nginx-config-linter-tester -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill nginx-config-linter-tester -a codex
```

### OpenClaw

```bash
clawhub install nginx-config-linter-tester
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nginx-config-linter-tester/)
