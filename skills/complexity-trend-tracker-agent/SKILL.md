---
title: "Complexity Trend Tracker"
description: "Tracks cyclomatic and cognitive complexity trends using lizard CLI and radon for Python analysis. Generates weekly complexity reports with git-integrated change attribution per module."
slug: "complexity-trend-tracker-agent"
category:
  - "Code Quality &amp; Review"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/complexity-trend-tracker-agent/"
---

# Complexity Trend Tracker

Tracks cyclomatic and cognitive complexity trends using lizard CLI and radon for Python analysis. Generates weekly complexity reports with git-integrated change attribution per module.

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
clawhub install complexity-trend-tracker-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Complexity Trend Tracker monitors code complexity metrics over time to identify areas of increasing technical debt. It combines lizard (a language-agnostic complexity analyzer) with radon for Python-specific cognitive complexity scoring, running automated analysis on each commit or on a scheduled basis.
The agent calculates cyclomatic complexity, cognitive complexity, lines of code, and parameter counts for every function and method in your codebase. It stores historical data and generates trend charts showing complexity growth per module, file, and team. Integration with git log data attributes complexity changes to specific authors and PRs.
Weekly reports highlight the top complexity offenders, newly complex functions, and modules trending toward maintenance difficulty. The agent can set configurable thresholds that trigger alerts when functions exceed complexity limits, and it suggests refactoring strategies based on the specific complexity patterns detected. Supports C, C++, Java, Python, JavaScript, TypeScript, Go, Ruby, and Rust.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/complexity-trend-tracker-agent/)
