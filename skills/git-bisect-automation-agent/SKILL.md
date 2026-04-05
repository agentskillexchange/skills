---
name: "Git Bisect Automation Agent"
description: "Automates git bisect workflows to find regression-introducing commits using custom test scripts and the git bisect run interface. Supports containerized test execution via Docker to ensure reproducible bisect environments."
category: "Code Quality & Review"
framework: "Custom Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/git-bisect-automation-agent/"
---
# Git Bisect Automation Agent

Automates git bisect workflows to find regression-introducing commits using custom test scripts and the git bisect run interface. Supports containerized test execution via Docker to ensure reproducible bisect environments.

The Git Bisect Automation Agent skill automates the process of finding regression-introducing commits using git bisect with intelligent test script generation. It analyzes the reported regression symptoms to construct targeted test commands, then executes git bisect run with proper exit code handling (125 for skip, 1-127 for bad, 0 for good).



The skill supports containerized test execution via Docker to ensure each bisect step runs in a clean, reproducible environment with the correct dependency versions. It handles common bisect complications like commits that fail to build (automatically marking them as skip), merge commits that require special handling, and submodule version mismatches across the bisect range.



Advanced features include parallel bisect execution across multiple test dimensions (e.g., finding the commit that broke both unit tests and performance benchmarks), integration with git blame and git log –follow for file-level regression tracking, and automatic generation of revert commits or fix patches once the offending commit is identified. The skill also maintains a bisect session log with timing data for each step, helping estimate total bisect completion time for large commit ranges.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill git-bisect-automation-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill git-bisect-automation-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill git-bisect-automation-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill git-bisect-automation-agent -a codex
```

### OpenClaw

```bash
clawhub install git-bisect-automation-agent
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-bisect-automation-agent/)
