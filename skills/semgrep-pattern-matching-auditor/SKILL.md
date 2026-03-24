---
name: "Semgrep Pattern Matching Auditor"
description: "Leverages the Semgrep OSS engine and semgrep-rules registry to perform deep static analysis across 30+ languages. Combines taint tracking with pattern matching for OWASP Top 10 vulnerability detection."
category: "Code Quality & Review"
framework: "OpenClaw"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/semgrep-pattern-matching-auditor/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "semgrep"  # from ase_tool_match
  github_stars: 14543  # from ase_github_stars (integer, not string)
  github_repo: "semgrep/semgrep"  # from ase_github_repo
  license: "LGPL-2.1"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Semgrep Pattern Matching Auditor

Leverages the Semgrep OSS engine and semgrep-rules registry to perform deep static analysis across 30+ languages. Combines taint tracking with pattern matching for OWASP Top 10 vulnerability detection.

## Overview

The Semgrep Pattern Matching Auditor uses the Semgrep open-source engine to perform comprehensive static analysis across your codebase in over 30 programming languages. It connects to the semgrep-rules community registry to pull the latest vulnerability patterns while also supporting custom rule definitions in YAML format. The agent combines Semgrep taint tracking mode with pattern matching to detect complex data flow vulnerabilities including SQL injection, XSS, SSRF, and other OWASP Top 10 issues. It integrates with the Semgrep App API for centralized findings management and policy enforcement. Results are enriched with CWE classifications, CVSS scores, and remediation guidance pulled from the Semgrep knowledge base. The auditor supports incremental scanning via git diff integration, only analyzing changed files in PRs while maintaining a full-project vulnerability baseline for trend reporting.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill semgrep-pattern-matching-auditor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill semgrep-pattern-matching-auditor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill semgrep-pattern-matching-auditor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill semgrep-pattern-matching-auditor -a codex
```

### OpenClaw

```bash
clawhub install semgrep-pattern-matching-auditor
```

## Source

- Marketplace: https://agentskillexchange.com/skills/semgrep-pattern-matching-auditor/
