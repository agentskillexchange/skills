---
title: "OWASP ZAP API Security Scanner"
description: "Automates OWASP ZAP scans against REST APIs using the ZAP Python API client. Imports OpenAPI/Swagger specs for targeted scanning and generates SARIF-format reports for GitHub Security tab integration."
verification: security_reviewed
source: "https://github.com/zaproxy/zaproxy"
category:
  - "Security &amp; Verification"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "zaproxy/zaproxy"
  github_stars: 14991
---

# OWASP ZAP API Security Scanner

This skill automates web application and API security testing using OWASP ZAP (Zed Attack Proxy) via its Python API client. It starts ZAP in daemon mode, imports OpenAPI/Swagger specifications to discover all API endpoints, and runs targeted active and passive scans against them. The skill configures scan policies based on OWASP Top 10 categories, focusing on injection attacks, broken authentication, sensitive data exposure, and security misconfiguration. It manages ZAP contexts for authenticated scanning using session tokens or API keys, configures anti-CSRF token handling, and sets appropriate scan strength and threshold levels. Spider and AJAX Spider modules map application attack surfaces before active scanning begins. Results are exported in multiple formats including SARIF for GitHub Security tab integration, HTML for human review, and JSON for programmatic processing. The skill supports baseline scans for CI/CD pipelines with configurable fail thresholds and can compare scan results across runs to identify new vulnerabilities.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-api-security-scanner/)
