---
title: "Semgrep Pattern Matching Analyzer"
description: "Writes and deploys custom Semgrep rules using pattern, pattern-either, and metavariable-regex operators for multi-language SAST scanning. Manages rule bundles in semgrep.yml with autofix transformations."
verification: "security_reviewed"
source: "https://github.com/semgrep/semgrep"
category:
  - "Code Quality & Review"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "semgrep/semgrep"
  github_stars: 14794
---

# Semgrep Pattern Matching Analyzer

The Semgrep Pattern Matching Analyzer creates and manages custom static analysis rules using Semgrep’s pattern matching DSL across 30+ supported languages. It leverages pattern operators (pattern, pattern-not, pattern-either, pattern-inside) and metavariable constraints (metavariable-regex, metavariable-comparison, metavariable-type) for precise vulnerability detection with low false-positive rates. Rule development includes taint analysis mode for tracking data flow from user-controlled sources to sensitive sinks (SQL queries, file system operations, command execution). The skill generates autofix transformations that automatically remediate detected issues, supporting regex replacement and metavariable insertion for safe code transformations. Rule bundles are organized in semgrep.yml configurations with severity levels, CWE mappings, and OWASP Top 10 classifications for compliance reporting. The analyzer integrates with Semgrep App for centralized policy management, supports .semgrepignore patterns for repository-specific exclusions, and generates SARIF output for IDE integration. Performance optimization includes rule deduplication, pattern pre-filtering, and language-specific parser selection to minimize scan times in CI environments.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/semgrep-pattern-matching-analyzer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/semgrep-pattern-matching-analyzer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/semgrep-pattern-matching-analyzer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-pattern-matching-analyzer/)
