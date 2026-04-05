---
name: "Semgrep Pattern Matching Analyzer"
description: "Writes and deploys custom Semgrep rules using pattern, pattern-either, and metavariable-regex operators for multi-language SAST scanning. Manages rule bundles in semgrep.yml with autofix transformations."
category: "Code Quality &amp; Review"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/semgrep-pattern-matching-analyzer/"
---
# Semgrep Pattern Matching Analyzer

Writes and deploys custom Semgrep rules using pattern, pattern-either, and metavariable-regex operators for multi-language SAST scanning. Manages rule bundles in semgrep.yml with autofix transformations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill semgrep-pattern-matching-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill semgrep-pattern-matching-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill semgrep-pattern-matching-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill semgrep-pattern-matching-analyzer -a codex
```

### OpenClaw

```bash
clawhub install semgrep-pattern-matching-analyzer
```

## Details

The Semgrep Pattern Matching Analyzer creates and manages custom static analysis rules using Semgrep’s pattern matching DSL across 30+ supported languages. It leverages pattern operators (pattern, pattern-not, pattern-either, pattern-inside) and metavariable constraints (metavariable-regex, metavariable-comparison, metavariable-type) for precise vulnerability detection with low false-positive rates.

Rule development includes taint analysis mode for tracking data flow from user-controlled sources to sensitive sinks (SQL queries, file system operations, command execution). The skill generates autofix transformations that automatically remediate detected issues, supporting regex replacement and metavariable insertion for safe code transformations.

Rule bundles are organized in semgrep.yml configurations with severity levels, CWE mappings, and OWASP Top 10 classifications for compliance reporting. The analyzer integrates with Semgrep App for centralized policy management, supports .semgrepignore patterns for repository-specific exclusions, and generates SARIF output for IDE integration. Performance optimization includes rule deduplication, pattern pre-filtering, and language-specific parser selection to minimize scan times in CI environments.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-pattern-matching-analyzer/)
