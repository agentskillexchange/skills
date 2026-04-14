---
title: "Semgrep Pattern Scanner"
description: "Executes Semgrep CLI with custom YAML rules and the Semgrep Registry API to detect anti-patterns, vulnerabilities, and taint tracking violations. Outputs SARIF-formatted results for GitHub Security tab integration."
verification: security_reviewed
source: "https://github.com/semgrep/semgrep"
category:
  - "Code Quality &amp; Review"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "semgrep/semgrep"
  github_stars: 14794
---

# Semgrep Pattern Scanner

The Semgrep Pattern Scanner leverages the Semgrep open-source static analysis engine to scan codebases for security vulnerabilities, anti-patterns, and code smells. It loads rules from the Semgrep Registry via the –config=auto flag and supports custom YAML rule definitions using pattern, pattern-either, and pattern-not-inside operators. The agent executes semgrep scan with –sarif output for direct integration with GitHub Advanced Security and the Code Scanning API. It supports taint mode analysis by defining source-sink-sanitizer rules to track dangerous data flows across function boundaries. For monorepo support, it uses –include/–exclude glob patterns and respects .semgrepignore files. The scanner handles multiple languages simultaneously including Python, JavaScript, Go, Java, and Ruby through Semgrep generic pattern syntax. Results are deduplicated across runs using fingerprinting and can be filtered by severity (ERROR, WARNING, INFO) for actionable reporting.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/semgrep-pattern-scanner/)
