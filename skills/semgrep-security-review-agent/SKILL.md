---
title: "Semgrep Security Review Agent"
description: "Performs SAST scanning using Semgrep CLI and Semgrep Registry rules. Detects OWASP Top 10 vulnerabilities, injection flaws, and insecure patterns with custom rule YAML authoring."
verification: "security_reviewed"
source: "https://github.com/semgrep/semgrep"
category:
  - "Code Quality &amp; Review"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "semgrep/semgrep"
  github_stars: 14794
  license: "LGPL-2.1"
---

# Semgrep Security Review Agent

The Semgrep Security Review Agent uses the Semgrep CLI (semgrep scan) and Semgrep Registry (r/python, r/javascript, r/java rulesets) to perform fast, accurate static application security testing. It runs lightweight pattern matching without requiring compilation or build artifacts.

The agent supports the full Semgrep rule syntax including metavariables, pattern operators (pattern-either, pattern-not, pattern-inside), and taint tracking for data flow analysis. Custom rules are authored in YAML and can target specific frameworks like Django, Flask, Express, or Spring.

OWASP Top 10 coverage includes SQL injection, XSS, SSRF, path traversal, insecure deserialization, and hardcoded secrets detection. The agent integrates with Semgrep App for centralized policy management and findings triage.

CI/CD integration supports GitHub Actions, GitLab CI, and Jenkins with SARIF output for GitHub Code Scanning alerts. Differential scanning (–baseline-ref) ensures only new issues are flagged in pull requests, reducing noise for development teams.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-security-review-agent/)
