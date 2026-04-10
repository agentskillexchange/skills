---
name: Semgrep Pattern Matching Auditor
description: Leverages the Semgrep OSS engine and semgrep-rules registry to perform
  deep static analysis across 30+ languages. Combines taint tracking with pattern
  matching for OWASP Top 10 vulnerability detection.
verification: security_reviewed
source: https://agentskillexchange.com/skills/semgrep-pattern-matching-auditor/
category:
- Code Quality &amp; Review
framework:
- OpenClaw
---
# Semgrep Pattern Matching Auditor

The Semgrep Pattern Matching Auditor uses the Semgrep open-source engine to perform comprehensive static analysis across your codebase in over 30 programming languages. It connects to the semgrep-rules community registry to pull the latest vulnerability patterns while also supporting custom rule definitions in YAML format. The agent combines Semgrep taint tracking mode with pattern matching to detect complex data flow vulnerabilities including SQL injection, XSS, SSRF, and other OWASP Top 10 issues. It integrates with the Semgrep App API for centralized findings management and policy enforcement. Results are enriched with CWE classifications, CVSS scores, and remediation guidance pulled from the Semgrep knowledge base. The auditor supports incremental scanning via git diff integration, only analyzing changed files in PRs while maintaining a full-project vulnerability baseline for trend reporting.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-pattern-matching-auditor/)
