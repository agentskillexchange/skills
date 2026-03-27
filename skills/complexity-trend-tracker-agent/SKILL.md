---
name: "Complexity Trend Tracker"
description: "Tracks cyclomatic and cognitive complexity trends using lizard CLI and radon for Python analysis. Generates weekly complexity reports with git-integrated change attribution per module."
category: "Code Quality & Review"
framework: "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/complexity-trend-tracker-agent/"
---

# Complexity Trend Tracker

Tracks cyclomatic and cognitive complexity trends using lizard CLI and radon for Python analysis. Generates weekly complexity reports with git-integrated change attribution per module.

## Overview

The Complexity Trend Tracker monitors code complexity metrics over time to identify areas of increasing technical debt. It combines lizard (a language-agnostic complexity analyzer) with radon for Python-specific cognitive complexity scoring, running automated analysis on each commit or on a scheduled basis.

The agent calculates cyclomatic complexity, cognitive complexity, lines of code, and parameter counts for every function and method in your codebase. It stores historical data and generates trend charts showing complexity growth per module, file, and team. Integration with git log data attributes complexity changes to specific authors and PRs.

Weekly reports highlight the top complexity offenders, newly complex functions, and modules trending toward maintenance difficulty. The agent can set configurable thresholds that trigger alerts when functions exceed complexity limits, and it suggests refactoring strategies based on the specific complexity patterns detected. Supports C, C++, Java, Python, JavaScript, TypeScript, Go, Ruby, and Rust.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill complexity-trend-tracker-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill complexity-trend-tracker-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill complexity-trend-tracker-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill complexity-trend-tracker-agent -a codex
```

### OpenClaw

```bash
clawhub install complexity-trend-tracker-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/complexity-trend-tracker-agent/
