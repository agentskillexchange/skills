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
  license: "LGPL-2.1"
---

# Semgrep Pattern Matching Analyzer

The Semgrep Pattern Matching Analyzer creates and manages custom static analysis rules using Semgrep’s pattern matching DSL across 30+ supported languages. It leverages pattern operators (pattern, pattern-not, pattern-either, pattern-inside) and metavariable constraints (metavariable-regex, metavariable-comparison, metavariable-type) for precise vulnerability detection with low false-positive rates.


Rule development includes taint analysis mode for tracking data flow from user-controlled sources to sensitive sinks (SQL queries, file system operations, command execution). The skill generates autofix transformations that automatically remediate detected issues, supporting regex replacement and metavariable insertion for safe code transformations.


Rule bundles are organized in semgrep.yml configurations with severity levels, CWE mappings, and OWASP Top 10 classifications for compliance reporting. The analyzer integrates with Semgrep App for centralized policy management, supports .semgrepignore patterns for repository-specific exclusions, and generates SARIF output for IDE integration. Performance optimization includes rule deduplication, pattern pre-filtering, and language-specific parser selection to minimize scan times in CI environments.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-pattern-matching-analyzer/)
