---
name: Nginx Config Linter and Tester
description: Validates nginx.conf files using the gixy static analyzer and crossplane
  parser library. Tests configuration for security misconfigs, HTTP header issues,
  and performs dry-run validation via nginx -t subprocess invocation.
verification: security_reviewed
source: https://agentskillexchange.com/skills/nginx-config-linter-tester/
category:
- Runbooks &amp; Diagnostics
framework:
- ChatGPT Agents
---
# Nginx Config Linter and Tester

The Nginx Config Linter and Tester skill provides comprehensive validation and security analysis for Nginx web server configurations. It combines multiple analysis tools for thorough configuration auditing.
The skill uses the gixy static analyzer to detect common Nginx security misconfigurations including SSRF via proxy_pass, HTTP splitting vulnerabilities, and improper alias path traversal. It parses configuration files using the crossplane Python library for structural validation.
Configuration testing includes dry-run validation via nginx -t subprocess execution, verifying syntax correctness and file reference integrity. The skill checks for missing security headers (HSTS, CSP, X-Frame-Options), improper SSL/TLS configurations, and weak cipher suite selections.
Advanced features include upstream health check configuration validation, rate limiting rule analysis, and gzip compression settings optimization. The skill generates remediation suggestions with corrected configuration snippets and links to Nginx documentation for each finding.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nginx-config-linter-tester/)
