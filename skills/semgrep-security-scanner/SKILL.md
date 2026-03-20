---
name: Semgrep Security Scanner
description: Runs Semgrep static analysis with custom and community rulesets via the Semgrep CLI and Semgrep App API. Detects OWASP Top 10 vulnerabilities and generates fix suggestions.
category: Code Quality & Review
framework: Codex
verification: verified_metadata
rating: 4.8
reviews: 32
source: https://agentskillexchange.com/skill/semgrep-security-scanner/
---

# Semgrep Security Scanner

Runs Semgrep static analysis with custom and community rulesets via the Semgrep CLI and Semgrep App API. Detects OWASP Top 10 vulnerabilities and generates fix suggestions.

## Overview

The Semgrep Security Scanner agent performs comprehensive static application security testing (SAST) using Semgrep’s pattern-based analysis engine. It runs scans via the Semgrep CLI with curated community and custom rulesets, targeting OWASP Top 10 vulnerability categories across multiple programming languages.
The agent configures Semgrep rulesets appropriate for your technology stack, selecting from the Semgrep Registry categories including injection prevention, authentication flaws, cryptographic misuse, and insecure deserialization patterns. It supports custom rule authoring using Semgrep’s pattern syntax for organization-specific security policies and coding standards.
Scan results are enriched with contextual information using the Semgrep App API, including vulnerability descriptions, CWE mappings, and confidence scores. For each finding, the agent generates specific fix suggestions with code examples, prioritized by severity and exploitability. It tracks findings across scans using the Semgrep App dashboard API, identifying new vulnerabilities introduced in recent changes versus existing technical debt. Integration with CI pipelines enables blocking merges that introduce high-severity findings.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill semgrep-security-scanner
```

### OpenClaw

```bash
openclaw install semgrep-security-scanner
```

### Manual

Download this `SKILL.md` file and place it in your agent's skills directory.

## Metadata

| Field | Value |
|-------|-------|
| Category | Code Quality & Review |
| Framework | Codex |
| Verification | Verified Metadata |
| Rating | ⭐⭐⭐⭐ 4.8/5.0 (32 reviews) |

---

*Published on [Agent Skill Exchange](https://agentskillexchange.com/skill/semgrep-security-scanner/)*
