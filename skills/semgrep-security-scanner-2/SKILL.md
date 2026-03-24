---
name: "Semgrep Security Scanner"
description: "Scan codebases for security vulnerabilities and anti-patterns using Semgrep OSS rules and the Semgrep CLI. Supports custom YAML rule authoring and SARIF output for CI integration."
category: "Code Quality & Review"
framework: "Claude Agents"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/semgrep-security-scanner-2/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "semgrep"  # from ase_tool_match
  github_stars: 14543  # from ase_github_stars (integer, not string)
  github_repo: "semgrep/semgrep"  # from ase_github_repo
  license: "LGPL-2.1"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Semgrep Security Scanner

Scan codebases for security vulnerabilities and anti-patterns using Semgrep OSS rules and the Semgrep CLI. Supports custom YAML rule authoring and SARIF output for CI integration.

## Overview

The Semgrep Security Scanner skill leverages the Semgrep CLI and Semgrep Registry to perform fast, pattern-based static analysis across 30+ programming languages. It uses the semgrep scan command with configurable rulesets from the Semgrep Registry (p/default, p/owasp-top-ten, p/security-audit) and supports custom rule definitions in YAML using Semgrep pattern syntax including pattern-either, pattern-inside, and metavariable-comparison operators. The skill handles monorepo scanning with path filtering via –include and –exclude flags, generates SARIF reports for GitHub Code Scanning integration, and produces JSON output for programmatic processing. It supports Semgrep App integration for diff-aware scanning in CI pipelines via –baseline-commit, manages findings with triage states (open, ignored, fixed), and can autofix certain patterns using the fix: key in custom rules. The scanner also supports secrets detection via p/secrets ruleset and supply chain analysis for dependency vulnerabilities.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill semgrep-security-scanner-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill semgrep-security-scanner-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill semgrep-security-scanner-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill semgrep-security-scanner-2 -a codex
```

### OpenClaw

```bash
clawhub install semgrep-security-scanner-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/semgrep-security-scanner-2/
