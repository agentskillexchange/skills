---
name: "OWASP ZAP Automated Pen Testing Agent"
description: "Runs automated penetration tests using OWASP ZAP API with spider crawling, active scanning, and AJAX-aware testing. Generates SARIF and HTML reports with CWE-mapped findings for security review workflows."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/owasp-zap-automated-pen-testing-agent/"
category:
  - "Security &amp; Verification"
framework:
  - "ChatGPT Agents"
---

# OWASP ZAP Automated Pen Testing Agent

The OWASP ZAP Automated Pen Testing Agent skill orchestrates comprehensive web application security testing using the OWASP Zed Attack Proxy through its REST API. It configures ZAP contexts defining target scope, authentication methods (form-based, token-based, OAuth), and session management strategies. The traditional spider crawls application pages while the AJAX spider handles JavaScript-rendered content using a headless browser. Passive scanning identifies low-hanging vulnerabilities like missing security headers, cookie misconfigurations, and information disclosure during crawling. Active scanning tests for injection vulnerabilities (SQL injection, XSS, command injection), authentication bypasses, and SSRF using configurable attack strength and threshold levels. Scan policies are customized to focus on vulnerability classes relevant to the target application stack. Results are deduplicated, false-positive filtered, and exported in SARIF format for GitHub Security tab integration or HTML format for human review. Each finding is mapped to CWE identifiers and includes reproduction steps and remediation guidance.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/owasp-zap-automated-pen-testing-agent/)
