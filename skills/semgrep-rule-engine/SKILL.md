---
name: Semgrep Rule Engine
description: Executes Semgrep static analysis using the semgrep CLI with custom YAML
  rule definitions. Supports taint tracking, metavariable comparisons, and pattern-not-inside
  exclusions for precise vulnerability detection.
verification: security_reviewed
source: https://agentskillexchange.com/skills/semgrep-rule-engine/
category:
- Code Quality &amp; Review
framework:
- Custom Agents
---
# Semgrep Rule Engine

The Semgrep Rule Engine agent runs the semgrep CLI to perform lightweight static analysis across codebases in 30+ languages. It loads custom YAML rule definitions that leverage Semgrep's pattern matching DSL including metavariables ($X), ellipsis operators (&#8230;), and typed metavariable comparisons for precise code pattern detection.
The agent supports advanced features like taint tracking for tracing data flow from user input (sources) to dangerous operations (sinks), enabling detection of SQL injection, XSS, and path traversal vulnerabilities. Pattern composition using pattern-either, pattern-not, and pattern-not-inside operators allows complex rule logic that reduces false positives.
For CI integration, the agent runs in differential mode (-baseline-commit) to analyze only changed code in pull requests. It categorizes findings by OWASP Top 10, CWE identifiers, and custom severity levels. Supports Semgrep Registry rules, private rule bundles, and integration with Semgrep App for centralized finding management and developer notification workflows. Output formats include SARIF for GitHub Code Scanning and JSON for custom reporting.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-rule-engine/)
