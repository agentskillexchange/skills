---
title: "ZAP Automated Security Scan Orchestrator"
description: "Orchestrates OWASP ZAP security scans via the ZAP API with automated spider, active scanner, and authentication sequence configuration. Generates compliance reports mapped to OWASP Top 10 and exports findings in SARIF and JUnit XML formats."
slug: "zap-automated-security-scan-orchestrator"
category:
  - "Security &amp; Verification"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/zap-automated-security-scan-orchestrator/"
---

# ZAP Automated Security Scan Orchestrator

Orchestrates OWASP ZAP security scans via the ZAP API with automated spider, active scanner, and authentication sequence configuration. Generates compliance reports mapped to OWASP Top 10 and exports findings in SARIF and JUnit XML formats.

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
clawhub install zap-automated-security-scan-orchestrator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The ZAP Automated Security Scan Orchestrator manages end-to-end dynamic application security testing using OWASP ZAP through its REST API. It configures and executes multi-phase scan workflows starting with traditional and AJAX spider discovery, followed by passive analysis and targeted active scanning against discovered endpoints.
Authentication handling supports multiple schemes including form-based login with anti-CSRF token extraction, OAuth 2.0 bearer token injection, and session cookie management through ZAP authentication scripts. Scan policies are customizable per engagement type with tunable scanner strength and threshold settings for balancing thoroughness against scan duration.
The orchestrator maps findings to OWASP Top 10 categories with remediation guidance and severity ratings adjusted for application context. Output formats include HTML reports for stakeholder review, SARIF for GitHub Advanced Security integration, JUnit XML for CI pipeline quality gates, and JSON for programmatic processing. Baseline scan profiles enable regression testing in CI where new findings break the build while known accepted risks are suppressed. ZAP marketplace add-ons are managed declaratively for consistent scan capabilities across environments.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/zap-automated-security-scan-orchestrator/)
