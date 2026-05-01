---
title: "OWASP ZAP Automated Pen Testing Agent"
description: "Runs automated penetration tests using OWASP ZAP API with spider crawling, active scanning, and AJAX-aware testing. Generates SARIF and HTML reports with CWE-mapped findings for security review workflows."
verification: "security_reviewed"
source: "https://github.com/zaproxy/zaproxy"
category:
  - "Security & Verification"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "zaproxy/zaproxy"
  github_stars: 14991
---

# OWASP ZAP Automated Pen Testing Agent

The OWASP ZAP Automated Pen Testing Agent skill orchestrates comprehensive web application security testing using the OWASP Zed Attack Proxy through its REST API. It configures ZAP contexts defining target scope, authentication methods (form-based, token-based, OAuth), and session management strategies. The traditional spider crawls application pages while the AJAX spider handles JavaScript-rendered content using a headless browser. Passive scanning identifies low-hanging vulnerabilities like missing security headers, cookie misconfigurations, and information disclosure during crawling. Active scanning tests for injection vulnerabilities (SQL injection, XSS, command injection), authentication bypasses, and SSRF using configurable attack strength and threshold levels. Scan policies are customized to focus on vulnerability classes relevant to the target application stack. Results are deduplicated, false-positive filtered, and exported in SARIF format for GitHub Security tab integration or HTML format for human review. Each finding is mapped to CWE identifiers and includes reproduction steps and remediation guidance.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/owasp-zap-automated-pen-testing-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/owasp-zap-automated-pen-testing-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/owasp-zap-automated-pen-testing-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-automated-pen-testing-agent/)
