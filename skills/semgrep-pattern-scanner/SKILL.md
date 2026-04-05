---
name: "Semgrep Pattern Scanner"
description: "Executes Semgrep CLI with custom YAML rules and the Semgrep Registry API to detect anti-patterns, vulnerabilities, and taint tracking violations. Outputs SARIF-formatted results for GitHub Security tab integration."
category: "Code Quality &amp; Review"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/semgrep-pattern-scanner/"
---
# Semgrep Pattern Scanner

Executes Semgrep CLI with custom YAML rules and the Semgrep Registry API to detect anti-patterns, vulnerabilities, and taint tracking violations. Outputs SARIF-formatted results for GitHub Security tab integration.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill semgrep-pattern-scanner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill semgrep-pattern-scanner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill semgrep-pattern-scanner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill semgrep-pattern-scanner -a codex
```

### OpenClaw

```bash
clawhub install semgrep-pattern-scanner
```

## Details

The Semgrep Pattern Scanner leverages the Semgrep open-source static analysis engine to scan codebases for security vulnerabilities, anti-patterns, and code smells. It loads rules from the Semgrep Registry via the –config=auto flag and supports custom YAML rule definitions using pattern, pattern-either, and pattern-not-inside operators. The agent executes semgrep scan with –sarif output for direct integration with GitHub Advanced Security and the Code Scanning API. It supports taint mode analysis by defining source-sink-sanitizer rules to track dangerous data flows across function boundaries. For monorepo support, it uses –include/–exclude glob patterns and respects .semgrepignore files. The scanner handles multiple languages simultaneously including Python, JavaScript, Go, Java, and Ruby through Semgrep generic pattern syntax. Results are deduplicated across runs using fingerprinting and can be filtered by severity (ERROR, WARNING, INFO) for actionable reporting.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-pattern-scanner/)
