---
title: "Semgrep Security Review Agent"
description: "Performs SAST scanning using Semgrep CLI and Semgrep Registry rules. Detects OWASP Top 10 vulnerabilities, injection flaws, and insecure patterns with custom rule YAML authoring."
slug: "semgrep-security-review-agent"
category:
  - "Code Quality &amp; Review"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/semgrep-security-review-agent/"
---

# Semgrep Security Review Agent

Performs SAST scanning using Semgrep CLI and Semgrep Registry rules. Detects OWASP Top 10 vulnerabilities, injection flaws, and insecure patterns with custom rule YAML authoring.

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
clawhub install semgrep-security-review-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Semgrep Security Review Agent uses the Semgrep CLI (semgrep scan) and Semgrep Registry (r/python, r/javascript, r/java rulesets) to perform fast, accurate static application security testing. It runs lightweight pattern matching without requiring compilation or build artifacts.
The agent supports the full Semgrep rule syntax including metavariables, pattern operators (pattern-either, pattern-not, pattern-inside), and taint tracking for data flow analysis. Custom rules are authored in YAML and can target specific frameworks like Django, Flask, Express, or Spring.
OWASP Top 10 coverage includes SQL injection, XSS, SSRF, path traversal, insecure deserialization, and hardcoded secrets detection. The agent integrates with Semgrep App for centralized policy management and findings triage.
CI/CD integration supports GitHub Actions, GitLab CI, and Jenkins with SARIF output for GitHub Code Scanning alerts. Differential scanning (–baseline-ref) ensures only new issues are flagged in pull requests, reducing noise for development teams.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-security-review-agent/)
