---
title: "Semgrep Security Review Agent"
description: "The Semgrep Security Review Agent uses the Semgrep CLI (semgrep scan) and Semgrep Registry (r/python, r/javascript, r/java rulesets) to perform fast, accurate static application security testing. It runs lightweight pattern matching without requiring compilation or build artifacts.\nThe agent supports the full Semgrep rule syntax including metavariables, pattern operators (pattern-either, pattern-not, pattern-inside), and taint tracking for data flow analysis. Custom rules are authored in YAML and can target specific frameworks like Django, Flask, Express, or Spring.\nOWASP Top 10 coverage includes SQL injection, XSS, SSRF, path traversal, insecure deserialization, and hardcoded secrets detection. The agent integrates with Semgrep App for centralized policy management and findings triage.\nCI/CD integration supports GitHub Actions, GitLab CI, and Jenkins with SARIF output for GitHub Code Scanning alerts. Differential scanning (–baseline-ref) ensures only new issues are flagged in pull requests, reducing noise for development teams."
verification: security_reviewed
source: "https://github.com/semgrep/semgrep"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "semgrep/semgrep"
  github_stars: 14794
---

# Semgrep Security Review Agent

The Semgrep Security Review Agent uses the Semgrep CLI (semgrep scan) and Semgrep Registry (r/python, r/javascript, r/java rulesets) to perform fast, accurate static application security testing. It runs lightweight pattern matching without requiring compilation or build artifacts.
The agent supports the full Semgrep rule syntax including metavariables, pattern operators (pattern-either, pattern-not, pattern-inside), and taint tracking for data flow analysis. Custom rules are authored in YAML and can target specific frameworks like Django, Flask, Express, or Spring.
OWASP Top 10 coverage includes SQL injection, XSS, SSRF, path traversal, insecure deserialization, and hardcoded secrets detection. The agent integrates with Semgrep App for centralized policy management and findings triage.
CI/CD integration supports GitHub Actions, GitLab CI, and Jenkins with SARIF output for GitHub Code Scanning alerts. Differential scanning (–baseline-ref) ensures only new issues are flagged in pull requests, reducing noise for development teams.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/semgrep-security-review-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/semgrep-security-review-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-security-review-agent/)
