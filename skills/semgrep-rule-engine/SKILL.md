---
name: "Semgrep Rule Engine"
description: "Executes Semgrep static analysis using the semgrep CLI with custom YAML rule definitions. Supports taint tracking, metavariable comparisons, and pattern-not-inside exclusions for precise vulnerability detection."
category: "Code Quality & Review"
framework: "Custom Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/semgrep-rule-engine/"
---
# Semgrep Rule Engine

Executes Semgrep static analysis using the semgrep CLI with custom YAML rule definitions. Supports taint tracking, metavariable comparisons, and pattern-not-inside exclusions for precise vulnerability detection.

## Overview

The Semgrep Rule Engine agent runs the semgrep CLI to perform lightweight static analysis across codebases in 30+ languages. It loads custom YAML rule definitions that leverage Semgrep’s pattern matching DSL including metavariables ($X), ellipsis operators (…), and typed metavariable comparisons for precise code pattern detection.

The agent supports advanced features like taint tracking for tracing data flow from user input (sources) to dangerous operations (sinks), enabling detection of SQL injection, XSS, and path traversal vulnerabilities. Pattern composition using pattern-either, pattern-not, and pattern-not-inside operators allows complex rule logic that reduces false positives.

For CI integration, the agent runs in differential mode (–baseline-commit) to analyze only changed code in pull requests. It categorizes findings by OWASP Top 10, CWE identifiers, and custom severity levels. Supports Semgrep Registry rules, private rule bundles, and integration with Semgrep App for centralized finding management and developer notification workflows. Output formats include SARIF for GitHub Code Scanning and JSON for custom reporting.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill semgrep-rule-engine
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill semgrep-rule-engine -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill semgrep-rule-engine -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill semgrep-rule-engine -a codex
```

### OpenClaw

```bash
clawhub install semgrep-rule-engine
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-rule-engine/)
