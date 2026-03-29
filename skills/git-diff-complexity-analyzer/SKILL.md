---
name: "Git Diff Complexity Analyzer"
description: "Analyzes git diffs using libgit2 and radon to compute cyclomatic complexity changes per function. Flags complexity regressions in pull requests with inline GitHub review comments via PyGithub."
category: "Developer Tools"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/git-diff-complexity-analyzer/"
---
# Git Diff Complexity Analyzer

Analyzes git diffs using libgit2 and radon to compute cyclomatic complexity changes per function. Flags complexity regressions in pull requests with inline GitHub review comments via PyGithub.

## Overview

The Git Diff Complexity Analyzer skill provides automated code complexity analysis for git diffs, designed to catch complexity regressions before they merge. Using libgit2 for efficient diff parsing and radon for cyclomatic complexity computation, it identifies every function modified in a diff and computes before/after complexity scores. Functions that exceed configurable thresholds or show significant complexity increases are flagged with detailed explanations of which control flow additions (nested conditionals, loops, exception handlers) drove the increase. When integrated with GitHub pull requests via PyGithub, it posts inline review comments on the exact lines where complexity increased, with suggestions for refactoring patterns that could reduce complexity (extract method, replace conditional with polymorphism, introduce guard clauses). The tool supports Python, JavaScript, TypeScript, and Java through language-specific AST parsers. It maintains a complexity baseline file per repository, enabling trend tracking and team-wide complexity budgets. The skill also computes cognitive complexity (Sonar-style) alongside cyclomatic complexity, as they capture different aspects of code comprehensibility. CI integration outputs include JUnit XML reports, JSON summaries for dashboards, and configurable exit codes for quality gates.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill git-diff-complexity-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill git-diff-complexity-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill git-diff-complexity-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill git-diff-complexity-analyzer -a codex
```

### OpenClaw

```bash
clawhub install git-diff-complexity-analyzer
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-diff-complexity-analyzer/)
