---
title: Semgrep Security Review Agent
description: The Semgrep Security Review Agent uses the Semgrep CLI (semgrep scan)
  and Semgrep Registry (r/python, r/javascript, r/java rulesets) to perform fast,
  accurate static application security testing. It runs lightweight pattern matching
  without requiring compilation or build artifacts. The agent supports the full Semgrep
  rule syntax including metavariables, pattern operators (pattern-either, pattern-not,
  pattern-inside), and taint tracking for data flow analysis. Custom rules are authored
  in YAML and can target specific frameworks like Django, Flask, Express, or Spring.
  OWASP Top 10 coverage includes SQL injection, XSS, SSRF, path traversal, insecure
  deserialization, and hardcoded secrets detection. The agent integrates with Semgrep
  App for centralized policy management and findings triage. CI/CD integration supports
  GitHub Actions, GitLab CI, and Jenkins with SARIF output for GitHub Code Scanning
  alerts. Differential scanning (–baseline-ref) ensures only new issues are flagged
  in pull requests, reducing noise for development teams.
verification: security_reviewed
source: https://agentskillexchange.com/skills/semgrep-security-review-agent/
category:
- Code Quality &amp; Review
framework:
- Claude Agents
---

# Semgrep Security Review Agent

The Semgrep Security Review Agent uses the Semgrep CLI (semgrep scan) and Semgrep Registry (r/python, r/javascript, r/java rulesets) to perform fast, accurate static application security testing. It runs lightweight pattern matching without requiring compilation or build artifacts. The agent supports the full Semgrep rule syntax including metavariables, pattern operators (pattern-either, pattern-not, pattern-inside), and taint tracking for data flow analysis. Custom rules are authored in YAML and can target specific frameworks like Django, Flask, Express, or Spring. OWASP Top 10 coverage includes SQL injection, XSS, SSRF, path traversal, insecure deserialization, and hardcoded secrets detection. The agent integrates with Semgrep App for centralized policy management and findings triage. CI/CD integration supports GitHub Actions, GitLab CI, and Jenkins with SARIF output for GitHub Code Scanning alerts. Differential scanning (–baseline-ref) ensures only new issues are flagged in pull requests, reducing noise for development teams.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-security-review-agent/)
