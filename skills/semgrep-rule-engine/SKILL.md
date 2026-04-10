---
title: "Semgrep Rule Engine"
description: "Executes Semgrep static analysis using the semgrep CLI with custom YAML rule definitions. Supports taint tracking, metavariable comparisons, and pattern-not-inside exclusions for precise vulnerability detection."
slug: "semgrep-rule-engine"
category:
  - "Code Quality &amp; Review"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/semgrep-rule-engine/"
listed: true
---

# Semgrep Rule Engine

Executes Semgrep static analysis using the semgrep CLI with custom YAML rule definitions. Supports taint tracking, metavariable comparisons, and pattern-not-inside exclusions for precise vulnerability detection.

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
clawhub install semgrep-rule-engine
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Semgrep Rule Engine agent runs the semgrep CLI to perform lightweight static analysis across codebases in 30+ languages. It loads custom YAML rule definitions that leverage Semgrep’s pattern matching DSL including metavariables ($X), ellipsis operators (…), and typed metavariable comparisons for precise code pattern detection.
The agent supports advanced features like taint tracking for tracing data flow from user input (sources) to dangerous operations (sinks), enabling detection of SQL injection, XSS, and path traversal vulnerabilities. Pattern composition using pattern-either, pattern-not, and pattern-not-inside operators allows complex rule logic that reduces false positives.
For CI integration, the agent runs in differential mode (–baseline-commit) to analyze only changed code in pull requests. It categorizes findings by OWASP Top 10, CWE identifiers, and custom severity levels. Supports Semgrep Registry rules, private rule bundles, and integration with Semgrep App for centralized finding management and developer notification workflows. Output formats include SARIF for GitHub Code Scanning and JSON for custom reporting.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-rule-engine/)
