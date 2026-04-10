---
title: "Semgrep Pattern Scanner"
description: "Executes Semgrep CLI with custom YAML rules and the Semgrep Registry API to detect anti-patterns, vulnerabilities, and taint tracking violations. Outputs SARIF-formatted results for GitHub Security tab integration."
slug: "semgrep-pattern-scanner"
category:
  - "Code Quality &amp; Review"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/semgrep-pattern-scanner/"
---

# Semgrep Pattern Scanner

Executes Semgrep CLI with custom YAML rules and the Semgrep Registry API to detect anti-patterns, vulnerabilities, and taint tracking violations. Outputs SARIF-formatted results for GitHub Security tab integration.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install semgrep-pattern-scanner
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Semgrep Pattern Scanner leverages the Semgrep open-source static analysis engine to scan codebases for security vulnerabilities, anti-patterns, and code smells. It loads rules from the Semgrep Registry via the –config=auto flag and supports custom YAML rule definitions using pattern, pattern-either, and pattern-not-inside operators. The agent executes semgrep scan with –sarif output for direct integration with GitHub Advanced Security and the Code Scanning API. It supports taint mode analysis by defining source-sink-sanitizer rules to track dangerous data flows across function boundaries. For monorepo support, it uses –include/–exclude glob patterns and respects .semgrepignore files. The scanner handles multiple languages simultaneously including Python, JavaScript, Go, Java, and Ruby through Semgrep generic pattern syntax. Results are deduplicated across runs using fingerprinting and can be filtered by severity (ERROR, WARNING, INFO) for actionable reporting.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-pattern-scanner/)
