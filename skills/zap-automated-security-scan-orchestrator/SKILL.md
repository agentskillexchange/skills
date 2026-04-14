---
title: "ZAP Automated Security Scan Orchestrator"
description: "Orchestrates OWASP ZAP security scans via the ZAP API with automated spider, active scanner, and authentication sequence configuration. Generates compliance reports mapped to OWASP Top 10 and exports findings in SARIF and JUnit XML formats."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/zap-automated-security-scan-orchestrator/"
category:
  - "Security &amp; Verification"
framework:
  - "Codex"
---

# ZAP Automated Security Scan Orchestrator

The ZAP Automated Security Scan Orchestrator manages end-to-end dynamic application security testing using OWASP ZAP through its REST API. It configures and executes multi-phase scan workflows starting with traditional and AJAX spider discovery, followed by passive analysis and targeted active scanning against discovered endpoints.

Authentication handling supports multiple schemes including form-based login with anti-CSRF token extraction, OAuth 2.0 bearer token injection, and session cookie management through ZAP authentication scripts. Scan policies are customizable per engagement type with tunable scanner strength and threshold settings for balancing thoroughness against scan duration.

The orchestrator maps findings to OWASP Top 10 categories with remediation guidance and severity ratings adjusted for application context. Output formats include HTML reports for stakeholder review, SARIF for GitHub Advanced Security integration, JUnit XML for CI pipeline quality gates, and JSON for programmatic processing. Baseline scan profiles enable regression testing in CI where new findings break the build while known accepted risks are suppressed. ZAP marketplace add-ons are managed declaratively for consistent scan capabilities across environments.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/zap-automated-security-scan-orchestrator/)
