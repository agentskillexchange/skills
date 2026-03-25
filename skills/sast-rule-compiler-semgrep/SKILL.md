---
name: "SAST Rule Compiler for Semgrep"
description: "Compiles and validates custom Semgrep SAST rules using the semgrep-core engine. Tests pattern matching against sample codebases and generates rule performance benchmarks with p/ci rulesets."
category: "Security & Verification"
framework: "Codex"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/sast-rule-compiler-semgrep/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "semgrep"  # from ase_tool_match
  github_stars: 14543  # from ase_github_stars (integer, not string)
  github_repo: "semgrep/semgrep"  # from ase_github_repo
  license: "LGPL-2.1"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# SAST Rule Compiler for Semgrep

Compiles and validates custom Semgrep SAST rules using the semgrep-core engine. Tests pattern matching against sample codebases and generates rule performance benchmarks with p/ci rulesets.

## Overview

The SAST Rule Compiler for Semgrep skill streamlines the creation and validation of custom Static Application Security Testing rules for the Semgrep engine. It provides an interactive workflow for writing pattern, pattern-either, pattern-not, and taint-mode rules with immediate feedback against test codebases.

The skill validates rule YAML syntax against the Semgrep rule schema, checks metavariable bindings for consistency, and runs pattern compilation through semgrep-core to catch regex errors and unsupported language features. It includes a benchmark mode that profiles rule performance against large codebases, identifying rules that exceed scan-time budgets.

For teams using Semgrep App, the skill can push rules to custom rule packs and validate them against the p/ci, p/security-audit, and p/owasp-top-ten rulesets to avoid conflicts. It supports all 30+ languages in Semgrep’s grammar registry and can generate autofix patterns using the fix: directive. Output includes rule coverage reports showing which CWE IDs are addressed and gap analysis against OWASP benchmarks.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sast-rule-compiler-semgrep
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sast-rule-compiler-semgrep -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sast-rule-compiler-semgrep -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sast-rule-compiler-semgrep -a codex
```

### OpenClaw

```bash
clawhub install sast-rule-compiler-semgrep
```

## Source

- Marketplace: https://agentskillexchange.com/skills/sast-rule-compiler-semgrep/
