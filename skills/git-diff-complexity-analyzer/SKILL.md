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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-diff-complexity-analyzer/)
