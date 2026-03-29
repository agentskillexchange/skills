---
name: "Semgrep Custom Pattern Generator"
description: "Generates Semgrep SAST rules from vulnerability descriptions using the Semgrep CLI and semgrep-rules YAML schema. Supports metavariable patterns, taint tracking, and join rules for cross-function analysis."
category: "Code Quality & Review"
framework: "MCP"
verification: security_reviewed
source: "https://github.com/semgrep/semgrep"
tool_ecosystem:
  tool: semgrep
  github_stars: 14551
  github_repo: semgrep/semgrep
  license: LGPL-2.1
  maintained: true
---
# Semgrep Custom Pattern Generator

Generates Semgrep SAST rules from vulnerability descriptions using the Semgrep CLI and semgrep-rules YAML schema. Supports metavariable patterns, taint tracking, and join rules for cross-function analysis.

## Overview

The Semgrep Custom Pattern Generator skill creates custom static analysis rules for security and code quality scanning. It translates vulnerability descriptions or insecure code patterns into Semgrep rule definitions using the official semgrep-rules YAML schema.

The skill supports the full range of Semgrep pattern operators including pattern, pattern-not, pattern-inside, pattern-either, and metavariable-pattern for complex matching logic. For security-focused rules, it generates taint-mode rules with proper source, sink, and sanitizer definitions that track data flow across function boundaries.

Advanced rule features are supported including join rules for cross-file analysis using the semgrep join mode, pattern-regex for matching string literals and comments, and metavariable-comparison for numeric constraint checking. Each rule includes proper metadata following the semgrep-rule-schema with cwe, owasp, confidence, and impact fields.

Validation is performed using the semgrep –validate flag against the generated YAML, and the skill runs semgrep –test against provided test fixtures to verify true positives and false negative handling. Rules are organized into rulesets compatible with the Semgrep Registry publishing format, ready for use with semgrep ci in your CI pipeline.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill semgrep-custom-pattern-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill semgrep-custom-pattern-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill semgrep-custom-pattern-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill semgrep-custom-pattern-generator -a codex
```

### OpenClaw

```bash
clawhub install semgrep-custom-pattern-generator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-custom-pattern-generator/)
