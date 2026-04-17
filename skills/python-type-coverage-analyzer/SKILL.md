---
title: "Python Type Coverage Analyzer"
description: "The Python Type Coverage Analyzer skill assesses and improves type annotation completeness across Python codebases. It runs mypy with –html-report and –txt-report to generate coverage metrics, then processes pyright output in JSON mode to compute type completeness scores per module and identify specific locations where type information is missing.\nThe skill identifies untyped function parameters, missing return type annotations, implicit Any types from untyped third-party libraries, and overly broad Union types that could be narrowed. It leverages the mypy daemon (dmypy) for incremental analysis on large codebases and can process pyright’s reportMissing* diagnostic categories to prioritize the most impactful typing improvements.\nAdditional capabilities include generating type stubs (.pyi files) for untyped internal modules using stubgen, recommending typing_extensions backports for older Python versions, and creating py.typed marker files for PEP 561 compliance. The skill produces prioritized fix lists sorted by module import frequency (most-imported modules first) to maximize downstream type inference improvements, and can auto-generate TypedDict definitions from runtime JSON schema analysis."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/python-type-coverage-analyzer/"
framework:
  - "Gemini"
---

# Python Type Coverage Analyzer

The Python Type Coverage Analyzer skill assesses and improves type annotation completeness across Python codebases. It runs mypy with –html-report and –txt-report to generate coverage metrics, then processes pyright output in JSON mode to compute type completeness scores per module and identify specific locations where type information is missing.
The skill identifies untyped function parameters, missing return type annotations, implicit Any types from untyped third-party libraries, and overly broad Union types that could be narrowed. It leverages the mypy daemon (dmypy) for incremental analysis on large codebases and can process pyright’s reportMissing* diagnostic categories to prioritize the most impactful typing improvements.
Additional capabilities include generating type stubs (.pyi files) for untyped internal modules using stubgen, recommending typing_extensions backports for older Python versions, and creating py.typed marker files for PEP 561 compliance. The skill produces prioritized fix lists sorted by module import frequency (most-imported modules first) to maximize downstream type inference improvements, and can auto-generate TypedDict definitions from runtime JSON schema analysis.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/python-type-coverage-analyzer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/python-type-coverage-analyzer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/python-type-coverage-analyzer/)
