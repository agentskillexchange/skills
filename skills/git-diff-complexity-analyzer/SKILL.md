---
title: "Git Diff Complexity Analyzer"
description: "The Git Diff Complexity Analyzer skill provides automated code complexity analysis for git diffs, designed to catch complexity regressions before they merge. Using libgit2 for efficient diff parsing and radon for cyclomatic complexity computation, it identifies every function modified in a diff and computes before/after complexity scores. Functions that exceed configurable thresholds or show significant complexity increases are flagged with detailed explanations of which control flow additions (nested conditionals, loops, exception handlers) drove the increase. When integrated with GitHub pull requests via PyGithub, it posts inline review comments on the exact lines where complexity increased, with suggestions for refactoring patterns that could reduce complexity (extract method, replace conditional with polymorphism, introduce guard clauses). The tool supports Python, JavaScript, TypeScript, and Java through language-specific AST parsers. It maintains a complexity baseline file per repository, enabling trend tracking and team-wide complexity budgets. The skill also computes cognitive complexity (Sonar-style) alongside cyclomatic complexity, as they capture different aspects of code comprehensibility. CI integration outputs include JUnit XML reports, JSON summaries for dashboards, and configurable exit codes for quality gates."
source: "https://agentskillexchange.com/skills/git-diff-complexity-analyzer/"
verification: "security_reviewed"
category:
  - "Developer Tools"
framework:
  - "MCP"
---

# Git Diff Complexity Analyzer

The Git Diff Complexity Analyzer skill provides automated code complexity analysis for git diffs, designed to catch complexity regressions before they merge. Using libgit2 for efficient diff parsing and radon for cyclomatic complexity computation, it identifies every function modified in a diff and computes before/after complexity scores. Functions that exceed configurable thresholds or show significant complexity increases are flagged with detailed explanations of which control flow additions (nested conditionals, loops, exception handlers) drove the increase. When integrated with GitHub pull requests via PyGithub, it posts inline review comments on the exact lines where complexity increased, with suggestions for refactoring patterns that could reduce complexity (extract method, replace conditional with polymorphism, introduce guard clauses). The tool supports Python, JavaScript, TypeScript, and Java through language-specific AST parsers. It maintains a complexity baseline file per repository, enabling trend tracking and team-wide complexity budgets. The skill also computes cognitive complexity (Sonar-style) alongside cyclomatic complexity, as they capture different aspects of code comprehensibility. CI integration outputs include JUnit XML reports, JSON summaries for dashboards, and configurable exit codes for quality gates.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-diff-complexity-analyzer/)
