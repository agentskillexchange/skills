---
title: Complexity Trend Tracker
description: The Complexity Trend Tracker monitors code complexity metrics over time
  to identify areas of increasing technical debt. It combines lizard (a language-agnostic
  complexity analyzer) with radon for Python-specific cognitive complexity scoring,
  running automated analysis on each commit or on a scheduled basis. The agent calculates
  cyclomatic complexity, cognitive complexity, lines of code, and parameter counts
  for every function and method in your codebase. It stores historical data and generates
  trend charts showing complexity growth per module, file, and team. Integration with
  git log data attributes complexity changes to specific authors and PRs. Weekly reports
  highlight the top complexity offenders, newly complex functions, and modules trending
  toward maintenance difficulty. The agent can set configurable thresholds that trigger
  alerts when functions exceed complexity limits, and it suggests refactoring strategies
  based on the specific complexity patterns detected. Supports C, C++, Java, Python,
  JavaScript, TypeScript, Go, Ruby, and Rust.
verification: security_reviewed
source: https://agentskillexchange.com/skills/complexity-trend-tracker-agent/
category:
- Code Quality &amp; Review
framework:
- MCP
---

# Complexity Trend Tracker

The Complexity Trend Tracker monitors code complexity metrics over time to identify areas of increasing technical debt. It combines lizard (a language-agnostic complexity analyzer) with radon for Python-specific cognitive complexity scoring, running automated analysis on each commit or on a scheduled basis. The agent calculates cyclomatic complexity, cognitive complexity, lines of code, and parameter counts for every function and method in your codebase. It stores historical data and generates trend charts showing complexity growth per module, file, and team. Integration with git log data attributes complexity changes to specific authors and PRs. Weekly reports highlight the top complexity offenders, newly complex functions, and modules trending toward maintenance difficulty. The agent can set configurable thresholds that trigger alerts when functions exceed complexity limits, and it suggests refactoring strategies based on the specific complexity patterns detected. Supports C, C++, Java, Python, JavaScript, TypeScript, Go, Ruby, and Rust.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/complexity-trend-tracker-agent/)
