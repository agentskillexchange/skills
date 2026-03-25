---
name: "Semgrep Rule Author"
description: "Generates custom Semgrep rules from natural language descriptions of vulnerability patterns. Uses semgrep –validate to verify rule syntax and semgrep –test to run against sample code fixtures automatically."
category: "Code Quality & Review"
framework: "OpenClaw"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/semgrep-rule-author/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "semgrep"  # from ase_tool_match
  github_stars: 14551  # from ase_github_stars (integer, not string)
  github_repo: "semgrep/semgrep"  # from ase_github_repo
  license: "LGPL-2.1"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Semgrep Rule Author

Generates custom Semgrep rules from natural language descriptions of vulnerability patterns. Uses semgrep –validate to verify rule syntax and semgrep –test to run against sample code fixtures automatically.

## Overview

Semgrep Rule Author transforms natural language descriptions of code vulnerabilities or anti-patterns into production-ready Semgrep YAML rules.

How It Works

Describe a vulnerability pattern in plain English — such as “SQL injection via string concatenation in Python Flask routes” — and the skill generates a complete Semgrep rule with pattern, pattern-not, metavariable constraints, and metadata fields.

Key Features

Supports all Semgrep pattern operators including pattern-inside, pattern-either, and metavariable-regex

Automatically runs semgrep –validate to ensure rule syntax correctness

Generates test fixtures and runs semgrep –test to verify true/false positive behavior

Outputs rules in Semgrep Registry format with proper severity, confidence, and CWE mappings

Use Cases

Ideal for security teams building custom rule packs, developers enforcing framework-specific patterns, and compliance teams mapping rules to OWASP Top 10 categories. Exports rules compatible with Semgrep Cloud Platform and semgrep-app.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill semgrep-rule-author
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill semgrep-rule-author -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill semgrep-rule-author -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill semgrep-rule-author -a codex
```

### OpenClaw

```bash
clawhub install semgrep-rule-author
```

## Source

- Marketplace: https://agentskillexchange.com/skills/semgrep-rule-author/
