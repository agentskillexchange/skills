---
title: "Complexity Trend Tracker"
description: "Tracks cyclomatic and cognitive complexity trends using lizard CLI and radon for Python analysis. Generates weekly complexity reports with git-integrated change attribution per module."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/complexity-trend-tracker-agent/"
category:
  - "Code Quality & Review"
framework:
  - "MCP"
---

# Complexity Trend Tracker

The Complexity Trend Tracker monitors code complexity metrics over time to identify areas of increasing technical debt. It combines lizard (a language-agnostic complexity analyzer) with radon for Python-specific cognitive complexity scoring, running automated analysis on each commit or on a scheduled basis.

The agent calculates cyclomatic complexity, cognitive complexity, lines of code, and parameter counts for every function and method in your codebase. It stores historical data and generates trend charts showing complexity growth per module, file, and team. Integration with git log data attributes complexity changes to specific authors and PRs.

Weekly reports highlight the top complexity offenders, newly complex functions, and modules trending toward maintenance difficulty. The agent can set configurable thresholds that trigger alerts when functions exceed complexity limits, and it suggests refactoring strategies based on the specific complexity patterns detected. Supports C, C++, Java, Python, JavaScript, TypeScript, Go, Ruby, and Rust.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/complexity-trend-tracker-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/complexity-trend-tracker-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/complexity-trend-tracker-agent/)
