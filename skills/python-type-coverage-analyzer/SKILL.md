---
title: "Python Type Coverage Analyzer"
description: "The Python Type Coverage Analyzer skill assesses and improves type annotation completeness across Python codebases. It runs mypy with &#8211;html-report and &#8211;txt-report to generate coverage metrics, then processes pyright output in JSON mode to compute type completeness scores per module and identify specific locations where type information is missing. The skill identifies untyped function parameters, missing return type annotations, implicit Any types from untyped third-party libraries, and overly broad Union types that could be narrowed. It leverages the mypy daemon (dmypy) for incremental analysis on large codebases and can process pyright&#8217;s reportMissing* diagnostic categories to prioritize the most impactful typing improvements. Additional capabilities include generating type stubs (.pyi files) for untyped internal modules using stubgen, recommending typing_extensions backports for older Python versions, and creating py.typed marker files for PEP 561 compliance. The skill produces prioritized fix lists sorted by module import frequency (most-imported modules first) to maximize downstream type inference improvements, and can auto-generate TypedDict definitions from runtime JSON schema analysis."
source: "https://agentskillexchange.com/skills/python-type-coverage-analyzer/"
verification: "security_reviewed"
category:
  - "Code Quality &amp; Review"
framework:
  - "Gemini"
---

# Python Type Coverage Analyzer

The Python Type Coverage Analyzer skill assesses and improves type annotation completeness across Python codebases. It runs mypy with &#8211;html-report and &#8211;txt-report to generate coverage metrics, then processes pyright output in JSON mode to compute type completeness scores per module and identify specific locations where type information is missing. The skill identifies untyped function parameters, missing return type annotations, implicit Any types from untyped third-party libraries, and overly broad Union types that could be narrowed. It leverages the mypy daemon (dmypy) for incremental analysis on large codebases and can process pyright&#8217;s reportMissing* diagnostic categories to prioritize the most impactful typing improvements. Additional capabilities include generating type stubs (.pyi files) for untyped internal modules using stubgen, recommending typing_extensions backports for older Python versions, and creating py.typed marker files for PEP 561 compliance. The skill produces prioritized fix lists sorted by module import frequency (most-imported modules first) to maximize downstream type inference improvements, and can auto-generate TypedDict definitions from runtime JSON schema analysis.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/python-type-coverage-analyzer/)
