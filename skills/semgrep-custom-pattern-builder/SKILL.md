---
name: "Semgrep Custom Pattern Builder"
description: "Builds custom Semgrep rules using the Semgrep pattern syntax and semgrep CLI. Generates YAML rule files with metavariable patterns, taint tracking, and autofix transformations."
category: "Code Quality & Review"
framework: "Codex"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/semgrep-custom-pattern-builder/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "semgrep"  # from ase_tool_match
  github_stars: 14543  # from ase_github_stars (integer, not string)
  github_repo: "semgrep/semgrep"  # from ase_github_repo
  license: "LGPL-2.1"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Semgrep Custom Pattern Builder

Builds custom Semgrep rules using the Semgrep pattern syntax and semgrep CLI. Generates YAML rule files with metavariable patterns, taint tracking, and autofix transformations.

## Overview

The Semgrep Custom Pattern Builder creates targeted static analysis rules using the Semgrep pattern matching engine. It leverages the semgrep CLI for rule testing and the Semgrep Registry API for rule sharing and collaboration.

The skill generates YAML rule definitions with sophisticated pattern constructs including metavariable-pattern for type-constrained matching, pattern-either for multi-variant detection, pattern-inside for scope-limited scanning, and taint mode configurations for tracking data flow from sources to sinks. Each rule includes autofix patterns that provide automated remediation.

Rule development workflow includes generating test files with annotated expected findings, running semgrep –test for validation, and producing detailed rule documentation. The builder supports language-specific patterns across Python, JavaScript, TypeScript, Go, Java, and Ruby with generic pattern mode for framework-agnostic rules. It also generates Semgrep CI configurations for GitHub Actions and GitLab CI integration.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill semgrep-custom-pattern-builder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill semgrep-custom-pattern-builder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill semgrep-custom-pattern-builder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill semgrep-custom-pattern-builder -a codex
```

### OpenClaw

```bash
clawhub install semgrep-custom-pattern-builder
```

## Source

- Marketplace: https://agentskillexchange.com/skills/semgrep-custom-pattern-builder/
