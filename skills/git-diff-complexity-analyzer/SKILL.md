---
title: "Git Diff Complexity Analyzer"
description: "Analyzes git diffs using libgit2 and radon to compute cyclomatic complexity changes per function. Flags complexity regressions in pull requests with inline GitHub review comments via PyGithub."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/git-diff-complexity-analyzer/"
category:
  - "Developer Tools"
framework:
  - "MCP"
---

# Git Diff Complexity Analyzer

The Git Diff Complexity Analyzer skill provides automated code complexity analysis for git diffs, designed to catch complexity regressions before they merge. Using libgit2 for efficient diff parsing and radon for cyclomatic complexity computation, it identifies every function modified in a diff and computes before/after complexity scores. Functions that exceed configurable thresholds or show significant complexity increases are flagged with detailed explanations of which control flow additions (nested conditionals, loops, exception handlers) drove the increase. When integrated with GitHub pull requests via PyGithub, it posts inline review comments on the exact lines where complexity increased, with suggestions for refactoring patterns that could reduce complexity (extract method, replace conditional with polymorphism, introduce guard clauses). The tool supports Python, JavaScript, TypeScript, and Java through language-specific AST parsers. It maintains a complexity baseline file per repository, enabling trend tracking and team-wide complexity budgets. The skill also computes cognitive complexity (Sonar-style) alongside cyclomatic complexity, as they capture different aspects of code comprehensibility. CI integration outputs include JUnit XML reports, JSON summaries for dashboards, and configurable exit codes for quality gates.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-diff-complexity-analyzer/)
