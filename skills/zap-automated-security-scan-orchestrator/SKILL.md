---
name: "ZAP Automated Security Scan Orchestrator"
description: "Orchestrates OWASP ZAP security scans via the ZAP API with automated spider, active scanner, and authentication sequence configuration. Generates compliance reports mapped to OWASP Top 10 and exports findings in SARIF and JUnit XML formats."
category: "Security &amp; Verification"
framework: "Codex"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/zap-automated-security-scan-orchestrator/"
---
# ZAP Automated Security Scan Orchestrator

Orchestrates OWASP ZAP security scans via the ZAP API with automated spider, active scanner, and authentication sequence configuration. Generates compliance reports mapped to OWASP Top 10 and exports findings in SARIF and JUnit XML formats.

## Overview

The ZAP Automated Security Scan Orchestrator manages end-to-end dynamic application security testing using OWASP ZAP through its REST API. It configures and executes multi-phase scan workflows starting with traditional and AJAX spider discovery, followed by passive analysis and targeted active scanning against discovered endpoints.

Authentication handling supports multiple schemes including form-based login with anti-CSRF token extraction, OAuth 2.0 bearer token injection, and session cookie management through ZAP authentication scripts. Scan policies are customizable per engagement type with tunable scanner strength and threshold settings for balancing thoroughness against scan duration.

The orchestrator maps findings to OWASP Top 10 categories with remediation guidance and severity ratings adjusted for application context. Output formats include HTML reports for stakeholder review, SARIF for GitHub Advanced Security integration, JUnit XML for CI pipeline quality gates, and JSON for programmatic processing. Baseline scan profiles enable regression testing in CI where new findings break the build while known accepted risks are suppressed. ZAP marketplace add-ons are managed declaratively for consistent scan capabilities across environments.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill zap-automated-security-scan-orchestrator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill zap-automated-security-scan-orchestrator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill zap-automated-security-scan-orchestrator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill zap-automated-security-scan-orchestrator -a codex
```

### OpenClaw

```bash
clawhub install zap-automated-security-scan-orchestrator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/zap-automated-security-scan-orchestrator/)
