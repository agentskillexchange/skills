---
title: "Complexity Trend Tracker"
description: "Tracks cyclomatic and cognitive complexity trends using lizard CLI and radon for Python analysis. Generates weekly complexity reports with git-integrated change attribution per module."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/complexity-trend-tracker-agent/"
category:
  - "Code Quality &amp; Review"
framework:
  - "MCP"
---

# Complexity Trend Tracker

The Complexity Trend Tracker monitors code complexity metrics over time to identify areas of increasing technical debt. It combines lizard (a language-agnostic complexity analyzer) with radon for Python-specific cognitive complexity scoring, running automated analysis on each commit or on a scheduled basis.

The agent calculates cyclomatic complexity, cognitive complexity, lines of code, and parameter counts for every function and method in your codebase. It stores historical data and generates trend charts showing complexity growth per module, file, and team. Integration with git log data attributes complexity changes to specific authors and PRs.

Weekly reports highlight the top complexity offenders, newly complex functions, and modules trending toward maintenance difficulty. The agent can set configurable thresholds that trigger alerts when functions exceed complexity limits, and it suggests refactoring strategies based on the specific complexity patterns detected. Supports C, C++, Java, Python, JavaScript, TypeScript, Go, Ruby, and Rust.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/complexity-trend-tracker-agent/)
