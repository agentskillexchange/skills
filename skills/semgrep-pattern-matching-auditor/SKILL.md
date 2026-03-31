---
name: "Semgrep Pattern Matching Auditor"
description: "Leverages the Semgrep OSS engine and semgrep-rules registry to perform deep static analysis across 30+ languages. Combines taint tracking with pattern matching for OWASP Top 10 vulnerability detection."
category: "Code Quality &amp; Review"
framework: "OpenClaw"
verification: security_reviewed
source: "https://github.com/semgrep/semgrep"
tool_ecosystem:
  tool: semgrep
  github_repo: semgrep/semgrep
  github_stars: 14602
  license: LGPL-2.1
  maintained: true
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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-pattern-matching-auditor/)
