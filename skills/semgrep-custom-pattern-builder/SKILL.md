---
name: "Semgrep Custom Pattern Builder"
description: "Builds custom Semgrep rules using the Semgrep pattern syntax and semgrep CLI. Generates YAML rule files with metavariable patterns, taint tracking, and autofix transformations."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/semgrep-custom-pattern-builder/"
category:
  - "Code Quality &amp; Review"
framework:
  - "Codex"
---

# Semgrep Custom Pattern Builder

The Semgrep Custom Pattern Builder creates targeted static analysis rules using the Semgrep pattern matching engine. It leverages the semgrep CLI for rule testing and the Semgrep Registry API for rule sharing and collaboration.
The skill generates YAML rule definitions with sophisticated pattern constructs including metavariable-pattern for type-constrained matching, pattern-either for multi-variant detection, pattern-inside for scope-limited scanning, and taint mode configurations for tracking data flow from sources to sinks. Each rule includes autofix patterns that provide automated remediation.
Rule development workflow includes generating test files with annotated expected findings, running semgrep -test for validation, and producing detailed rule documentation. The builder supports language-specific patterns across Python, JavaScript, TypeScript, Go, Java, and Ruby with generic pattern mode for framework-agnostic rules. It also generates Semgrep CI configurations for GitHub Actions and GitLab CI integration.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-custom-pattern-builder/)
