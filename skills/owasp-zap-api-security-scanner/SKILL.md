---
title: "OWASP ZAP API Security Scanner"
description: "Automates OWASP ZAP scans against REST APIs using the ZAP Python API client. Imports OpenAPI/Swagger specs for targeted scanning and generates SARIF-format reports for GitHub Security tab integration."
verification: security_reviewed
source: "https://github.com/zaproxy/zaproxy"
category:
  - "Security & Verification"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "zaproxy/zaproxy"
  github_stars: 14991
  license: "Apache-2.0"
---

# OWASP ZAP API Security Scanner

This skill automates web application and API security testing using OWASP ZAP (Zed Attack Proxy) via its Python API client. It starts ZAP in daemon mode, imports OpenAPI/Swagger specifications to discover all API endpoints, and runs targeted active and passive scans against them. The skill configures scan policies based on OWASP Top 10 categories, focusing on injection attacks, broken authentication, sensitive data exposure, and security misconfiguration. It manages ZAP contexts for authenticated scanning using session tokens or API keys, configures anti-CSRF token handling, and sets appropriate scan strength and threshold levels. Spider and AJAX Spider modules map application attack surfaces before active scanning begins. Results are exported in multiple formats including SARIF for GitHub Security tab integration, HTML for human review, and JSON for programmatic processing. The skill supports baseline scans for CI/CD pipelines with configurable fail thresholds and can compare scan results across runs to identify new vulnerabilities.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/owasp-zap-api-security-scanner
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/owasp-zap-api-security-scanner` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-api-security-scanner/)
