---
name: "Semgrep Custom Rule Builder"
description: "Creates custom Semgrep SAST rules using the semgrep CLI and rule schema YAML format. Supports pattern-either, metavariable-regex, and taint-mode tracking for detecting framework-specific vulnerabilities in Python, Go, and JavaScript."
category: "Code Quality & Review"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/semgrep-custom-rule-builder-3/"
---
# Semgrep Custom Rule Builder

Creates custom Semgrep SAST rules using the semgrep CLI and rule schema YAML format. Supports pattern-either, metavariable-regex, and taint-mode tracking for detecting framework-specific vulnerabilities in Python, Go, and JavaScript.

## Overview

The Semgrep Custom Rule Builder skill helps security teams create precise static analysis rules using the Semgrep open-source SAST tool. It generates rules in Semgrep YAML format with proper pattern syntax, metavariable bindings, and fix suggestions.

The skill supports all Semgrep pattern operators including pattern-either for matching multiple code variants, pattern-not for exclusions, metavariable-regex for constraining captured variables, and metavariable-comparison for numeric checks. It leverages taint-mode analysis to track data flow from sources to sinks across function boundaries, essential for detecting injection vulnerabilities.

Rule generation covers common vulnerability patterns for Python (Django, Flask), Go (net/http, gin), and JavaScript (Express, React) frameworks. The skill creates rules with proper severity levels, CWE references, OWASP mappings, and actionable fix suggestions using the fix or fix-regex fields. It includes test case generation with semgrep –test compatible annotations marking expected true positives and negatives. Rules are validated against the Semgrep rule schema and tested against sample code snippets before deployment to Semgrep App or CI integration.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill semgrep-custom-rule-builder-3
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill semgrep-custom-rule-builder-3 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill semgrep-custom-rule-builder-3 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill semgrep-custom-rule-builder-3 -a codex
```

### OpenClaw

```bash
clawhub install semgrep-custom-rule-builder-3
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-custom-rule-builder-3/)
