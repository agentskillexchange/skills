---
title: "OWASP ZAP Automated Pen Testing Agent"
description: "Runs automated penetration tests using OWASP ZAP API with spider crawling, active scanning, and AJAX-aware testing. Generates SARIF and HTML reports with CWE-mapped findings for security review workflows."
slug: "owasp-zap-automated-pen-testing-agent"
category:
  - "Security &amp; Verification"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/owasp-zap-automated-pen-testing-agent/"
listed: true
---

# OWASP ZAP Automated Pen Testing Agent

Runs automated penetration tests using OWASP ZAP API with spider crawling, active scanning, and AJAX-aware testing. Generates SARIF and HTML reports with CWE-mapped findings for security review workflows.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install owasp-zap-automated-pen-testing-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The OWASP ZAP Automated Pen Testing Agent skill orchestrates comprehensive web application security testing using the OWASP Zed Attack Proxy through its REST API. It configures ZAP contexts defining target scope, authentication methods (form-based, token-based, OAuth), and session management strategies. The traditional spider crawls application pages while the AJAX spider handles JavaScript-rendered content using a headless browser. Passive scanning identifies low-hanging vulnerabilities like missing security headers, cookie misconfigurations, and information disclosure during crawling. Active scanning tests for injection vulnerabilities (SQL injection, XSS, command injection), authentication bypasses, and SSRF using configurable attack strength and threshold levels. Scan policies are customized to focus on vulnerability classes relevant to the target application stack. Results are deduplicated, false-positive filtered, and exported in SARIF format for GitHub Security tab integration or HTML format for human review. Each finding is mapped to CWE identifiers and includes reproduction steps and remediation guidance.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-automated-pen-testing-agent/)
