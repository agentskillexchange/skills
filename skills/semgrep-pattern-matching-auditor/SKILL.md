---
title: "Semgrep Pattern Matching Auditor"
description: "Leverages the Semgrep OSS engine and semgrep-rules registry to perform deep static analysis across 30+ languages. Combines taint tracking with pattern matching for OWASP Top 10 vulnerability detection."
verification: security_reviewed
source: "https://github.com/semgrep/semgrep"
category:
  - "Code Quality & Review"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "semgrep/semgrep"
  github_stars: 14794
---

# Semgrep Pattern Matching Auditor

The Semgrep Pattern Matching Auditor uses the Semgrep open-source engine to perform comprehensive static analysis across your codebase in over 30 programming languages. It connects to the semgrep-rules community registry to pull the latest vulnerability patterns while also supporting custom rule definitions in YAML format. The agent combines Semgrep taint tracking mode with pattern matching to detect complex data flow vulnerabilities including SQL injection, XSS, SSRF, and other OWASP Top 10 issues. It integrates with the Semgrep App API for centralized findings management and policy enforcement. Results are enriched with CWE classifications, CVSS scores, and remediation guidance pulled from the Semgrep knowledge base. The auditor supports incremental scanning via git diff integration, only analyzing changed files in PRs while maintaining a full-project vulnerability baseline for trend reporting.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/semgrep-pattern-matching-auditor
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/semgrep-pattern-matching-auditor` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-pattern-matching-auditor/)
