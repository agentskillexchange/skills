---
title: "Semgrep Custom Pattern Library"
description: "Builds custom Semgrep rules using the semgrep YAML rule syntax with metavariable-pattern, pattern-either, and taint-mode analysis. Generates rule packs for OWASP Top 10 detection across Python, JavaScript, and Go codebases."
verification: security_reviewed
source: "https://github.com/semgrep/semgrep"
category:
  - "Code Quality & Review"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "semgrep/semgrep"
  github_stars: 14794
  license: "LGPL-2.1"
---

# Semgrep Custom Pattern Library

The Semgrep Custom Pattern Library creates targeted static analysis rules using Semgrep’s pattern matching DSL. It generates YAML rule files with sophisticated pattern combinations including pattern-either for variant matching, pattern-not for false positive suppression, and metavariable-pattern for deep structural checks.

The skill supports taint-mode analysis for tracking data flow from sources to sinks across function boundaries, enabling detection of injection vulnerabilities, SSRF, and path traversal issues. Rules are organized into packs aligned with OWASP Top 10 categories and CWE identifiers for compliance reporting.

Advanced features include autofix generation using Semgrep’s fix key for automated remediation, join rules for cross-file analysis patterns, and extract mode configurations for analyzing embedded languages like SQL in Python strings. The library integrates with Semgrep App for rule sharing and includes semgrep ci configuration for pre-commit hooks and CI pipeline integration with SARIF output for GitHub Security tab ingestion.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/semgrep-custom-pattern-library
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/semgrep-custom-pattern-library` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-custom-pattern-library/)
