---
title: "Complexity Trend Tracker"
description: "The Complexity Trend Tracker monitors code complexity metrics over time to identify areas of increasing technical debt. It combines lizard (a language-agnostic complexity analyzer) with radon for Python-specific cognitive complexity scoring, running automated analysis on each commit or on a scheduled basis. The agent calculates cyclomatic complexity, cognitive complexity, lines of code, and parameter counts for every function and method in your codebase. It stores historical data and generates trend charts showing complexity growth per module, file, and team. Integration with git log data attributes complexity changes to specific authors and PRs. Weekly reports highlight the top complexity offenders, newly complex functions, and modules trending toward maintenance difficulty. The agent can set configurable thresholds that trigger alerts when functions exceed complexity limits, and it suggests refactoring strategies based on the specific complexity patterns detected. Supports C, C++, Java, Python, JavaScript, TypeScript, Go, Ruby, and Rust."
source: "https://agentskillexchange.com/skills/complexity-trend-tracker-agent/"
verification: "security_reviewed"
category:
  - "Code Quality &amp; Review"
framework:
  - "MCP"
---

# Complexity Trend Tracker

The Complexity Trend Tracker monitors code complexity metrics over time to identify areas of increasing technical debt. It combines lizard (a language-agnostic complexity analyzer) with radon for Python-specific cognitive complexity scoring, running automated analysis on each commit or on a scheduled basis. The agent calculates cyclomatic complexity, cognitive complexity, lines of code, and parameter counts for every function and method in your codebase. It stores historical data and generates trend charts showing complexity growth per module, file, and team. Integration with git log data attributes complexity changes to specific authors and PRs. Weekly reports highlight the top complexity offenders, newly complex functions, and modules trending toward maintenance difficulty. The agent can set configurable thresholds that trigger alerts when functions exceed complexity limits, and it suggests refactoring strategies based on the specific complexity patterns detected. Supports C, C++, Java, Python, JavaScript, TypeScript, Go, Ruby, and Rust.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/complexity-trend-tracker-agent/)
