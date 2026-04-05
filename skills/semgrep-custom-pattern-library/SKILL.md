---
name: "Semgrep Custom Pattern Library"
description: "Builds custom Semgrep rules using the semgrep YAML rule syntax with metavariable-pattern, pattern-either, and taint-mode analysis. Generates rule packs for OWASP Top 10 detection across Python, JavaScript, and Go codebases."
category: "Code Quality &amp; Review"
framework: "Claude Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/semgrep-custom-pattern-library/"
---
# Semgrep Custom Pattern Library

Builds custom Semgrep rules using the semgrep YAML rule syntax with metavariable-pattern, pattern-either, and taint-mode analysis. Generates rule packs for OWASP Top 10 detection across Python, JavaScript, and Go codebases.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill semgrep-custom-pattern-library
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill semgrep-custom-pattern-library -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill semgrep-custom-pattern-library -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill semgrep-custom-pattern-library -a codex
```

### OpenClaw

```bash
clawhub install semgrep-custom-pattern-library
```

## Details

The Semgrep Custom Pattern Library creates targeted static analysis rules using Semgrep’s pattern matching DSL. It generates YAML rule files with sophisticated pattern combinations including pattern-either for variant matching, pattern-not for false positive suppression, and metavariable-pattern for deep structural checks.

The skill supports taint-mode analysis for tracking data flow from sources to sinks across function boundaries, enabling detection of injection vulnerabilities, SSRF, and path traversal issues. Rules are organized into packs aligned with OWASP Top 10 categories and CWE identifiers for compliance reporting.

Advanced features include autofix generation using Semgrep’s fix key for automated remediation, join rules for cross-file analysis patterns, and extract mode configurations for analyzing embedded languages like SQL in Python strings. The library integrates with Semgrep App for rule sharing and includes semgrep ci configuration for pre-commit hooks and CI pipeline integration with SARIF output for GitHub Security tab ingestion.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-custom-pattern-library/)
