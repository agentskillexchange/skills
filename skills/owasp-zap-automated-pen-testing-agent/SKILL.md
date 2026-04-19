---
title: "OWASP ZAP Automated Pen Testing Agent"
description: "The OWASP ZAP Automated Pen Testing Agent skill orchestrates comprehensive web application security testing using the OWASP Zed Attack Proxy through its REST API. It configures ZAP contexts defining target scope, authentication methods (form-based, token-based, OAuth), and session management strategies. The traditional spider crawls application pages while the AJAX spider handles JavaScript-rendered content using a headless browser. Passive scanning identifies low-hanging vulnerabilities like missing security headers, cookie misconfigurations, and information disclosure during crawling. Active scanning tests for injection vulnerabilities (SQL injection, XSS, command injection), authentication bypasses, and SSRF using configurable attack strength and threshold levels. Scan policies are customized to focus on vulnerability classes relevant to the target application stack. Results are deduplicated, false-positive filtered, and exported in SARIF format for GitHub Security tab integration or HTML format for human review. Each finding is mapped to CWE identifiers and includes reproduction steps and remediation guidance."
source: "https://github.com/zaproxy/zaproxy"
verification: "security_reviewed"
category:
  - "Security &amp; Verification"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "zaproxy/zaproxy"
  github_stars: 14991
---

# OWASP ZAP Automated Pen Testing Agent

The OWASP ZAP Automated Pen Testing Agent skill orchestrates comprehensive web application security testing using the OWASP Zed Attack Proxy through its REST API. It configures ZAP contexts defining target scope, authentication methods (form-based, token-based, OAuth), and session management strategies. The traditional spider crawls application pages while the AJAX spider handles JavaScript-rendered content using a headless browser. Passive scanning identifies low-hanging vulnerabilities like missing security headers, cookie misconfigurations, and information disclosure during crawling. Active scanning tests for injection vulnerabilities (SQL injection, XSS, command injection), authentication bypasses, and SSRF using configurable attack strength and threshold levels. Scan policies are customized to focus on vulnerability classes relevant to the target application stack. Results are deduplicated, false-positive filtered, and exported in SARIF format for GitHub Security tab integration or HTML format for human review. Each finding is mapped to CWE identifiers and includes reproduction steps and remediation guidance.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-automated-pen-testing-agent/)
