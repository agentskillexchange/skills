---
title: "Git Diff Complexity Analyzer"
description: "Analyzes git diffs using libgit2 and radon to compute cyclomatic complexity changes per function. Flags complexity regressions in pull requests with inline GitHub review comments via PyGithub."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/git-diff-complexity-analyzer/"
category:
  - "Developer Tools"
framework:
  - "MCP"
---

# Git Diff Complexity Analyzer

The Git Diff Complexity Analyzer skill provides automated code complexity analysis for git diffs, designed to catch complexity regressions before they merge. Using libgit2 for efficient diff parsing and radon for cyclomatic complexity computation, it identifies every function modified in a diff and computes before/after complexity scores. Functions that exceed configurable thresholds or show significant complexity increases are flagged with detailed explanations of which control flow additions (nested conditionals, loops, exception handlers) drove the increase. When integrated with GitHub pull requests via PyGithub, it posts inline review comments on the exact lines where complexity increased, with suggestions for refactoring patterns that could reduce complexity (extract method, replace conditional with polymorphism, introduce guard clauses). The tool supports Python, JavaScript, TypeScript, and Java through language-specific AST parsers. It maintains a complexity baseline file per repository, enabling trend tracking and team-wide complexity budgets. The skill also computes cognitive complexity (Sonar-style) alongside cyclomatic complexity, as they capture different aspects of code comprehensibility. CI integration outputs include JUnit XML reports, JSON summaries for dashboards, and configurable exit codes for quality gates.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/git-diff-complexity-analyzer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/git-diff-complexity-analyzer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-diff-complexity-analyzer/)
