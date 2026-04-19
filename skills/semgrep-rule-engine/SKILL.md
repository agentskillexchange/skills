---
title: "Semgrep Rule Engine"
description: "The Semgrep Rule Engine agent runs the semgrep CLI to perform lightweight static analysis across codebases in 30+ languages. It loads custom YAML rule definitions that leverage Semgrep&#8217;s pattern matching DSL including metavariables ($X), ellipsis operators (&#8230;), and typed metavariable comparisons for precise code pattern detection. The agent supports advanced features like taint tracking for tracing data flow from user input (sources) to dangerous operations (sinks), enabling detection of SQL injection, XSS, and path traversal vulnerabilities. Pattern composition using pattern-either, pattern-not, and pattern-not-inside operators allows complex rule logic that reduces false positives. For CI integration, the agent runs in differential mode (&#8211;baseline-commit) to analyze only changed code in pull requests. It categorizes findings by OWASP Top 10, CWE identifiers, and custom severity levels. Supports Semgrep Registry rules, private rule bundles, and integration with Semgrep App for centralized finding management and developer notification workflows. Output formats include SARIF for GitHub Code Scanning and JSON for custom reporting."
source: "https://github.com/semgrep/semgrep"
verification: "security_reviewed"
category:
  - "Code Quality &amp; Review"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "semgrep/semgrep"
  github_stars: 14794
---

# Semgrep Rule Engine

The Semgrep Rule Engine agent runs the semgrep CLI to perform lightweight static analysis across codebases in 30+ languages. It loads custom YAML rule definitions that leverage Semgrep&#8217;s pattern matching DSL including metavariables ($X), ellipsis operators (&#8230;), and typed metavariable comparisons for precise code pattern detection. The agent supports advanced features like taint tracking for tracing data flow from user input (sources) to dangerous operations (sinks), enabling detection of SQL injection, XSS, and path traversal vulnerabilities. Pattern composition using pattern-either, pattern-not, and pattern-not-inside operators allows complex rule logic that reduces false positives. For CI integration, the agent runs in differential mode (&#8211;baseline-commit) to analyze only changed code in pull requests. It categorizes findings by OWASP Top 10, CWE identifiers, and custom severity levels. Supports Semgrep Registry rules, private rule bundles, and integration with Semgrep App for centralized finding management and developer notification workflows. Output formats include SARIF for GitHub Code Scanning and JSON for custom reporting.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-rule-engine/)
