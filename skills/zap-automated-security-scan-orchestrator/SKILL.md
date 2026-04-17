---
title: "ZAP Automated Security Scan Orchestrator"
description: "The ZAP Automated Security Scan Orchestrator manages end-to-end dynamic application security testing using OWASP ZAP through its REST API. It configures and executes multi-phase scan workflows starting with traditional and AJAX spider discovery, followed by passive analysis and targeted active scanning against discovered endpoints.\nAuthentication handling supports multiple schemes including form-based login with anti-CSRF token extraction, OAuth 2.0 bearer token injection, and session cookie management through ZAP authentication scripts. Scan policies are customizable per engagement type with tunable scanner strength and threshold settings for balancing thoroughness against scan duration.\nThe orchestrator maps findings to OWASP Top 10 categories with remediation guidance and severity ratings adjusted for application context. Output formats include HTML reports for stakeholder review, SARIF for GitHub Advanced Security integration, JUnit XML for CI pipeline quality gates, and JSON for programmatic processing. Baseline scan profiles enable regression testing in CI where new findings break the build while known accepted risks are suppressed. ZAP marketplace add-ons are managed declaratively for consistent scan capabilities across environments."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/zap-automated-security-scan-orchestrator/"
framework:
  - "Codex"
---

# ZAP Automated Security Scan Orchestrator

The ZAP Automated Security Scan Orchestrator manages end-to-end dynamic application security testing using OWASP ZAP through its REST API. It configures and executes multi-phase scan workflows starting with traditional and AJAX spider discovery, followed by passive analysis and targeted active scanning against discovered endpoints.
Authentication handling supports multiple schemes including form-based login with anti-CSRF token extraction, OAuth 2.0 bearer token injection, and session cookie management through ZAP authentication scripts. Scan policies are customizable per engagement type with tunable scanner strength and threshold settings for balancing thoroughness against scan duration.
The orchestrator maps findings to OWASP Top 10 categories with remediation guidance and severity ratings adjusted for application context. Output formats include HTML reports for stakeholder review, SARIF for GitHub Advanced Security integration, JUnit XML for CI pipeline quality gates, and JSON for programmatic processing. Baseline scan profiles enable regression testing in CI where new findings break the build while known accepted risks are suppressed. ZAP marketplace add-ons are managed declaratively for consistent scan capabilities across environments.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/zap-automated-security-scan-orchestrator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/zap-automated-security-scan-orchestrator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/zap-automated-security-scan-orchestrator/)
