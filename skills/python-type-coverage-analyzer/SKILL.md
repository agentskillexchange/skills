---
title: Python Type Coverage Analyzer
description: The Python Type Coverage Analyzer skill assesses and improves type annotation
  completeness across Python codebases. It runs mypy with –html-report and –txt-report
  to generate coverage metrics, then processes pyright output in JSON mode to compute
  type completeness scores per module and identify specific locations where type information
  is missing. The skill identifies untyped function parameters, missing return type
  annotations, implicit Any types from untyped third-party libraries, and overly broad
  Union types that could be narrowed. It leverages the mypy daemon (dmypy) for incremental
  analysis on large codebases and can process pyright’s reportMissing* diagnostic
  categories to prioritize the most impactful typing improvements. Additional capabilities
  include generating type stubs (.pyi files) for untyped internal modules using stubgen,
  recommending typing_extensions backports for older Python versions, and creating
  py.typed marker files for PEP 561 compliance. The skill produces prioritized fix
  lists sorted by module import frequency (most-imported modules first) to maximize
  downstream type inference improvements, and can auto-generate TypedDict definitions
  from runtime JSON schema analysis.
verification: security_reviewed
source: https://agentskillexchange.com/skills/python-type-coverage-analyzer/
category:
- Code Quality &amp; Review
framework:
- Gemini
---

# Python Type Coverage Analyzer

The Python Type Coverage Analyzer skill assesses and improves type annotation completeness across Python codebases. It runs mypy with –html-report and –txt-report to generate coverage metrics, then processes pyright output in JSON mode to compute type completeness scores per module and identify specific locations where type information is missing. The skill identifies untyped function parameters, missing return type annotations, implicit Any types from untyped third-party libraries, and overly broad Union types that could be narrowed. It leverages the mypy daemon (dmypy) for incremental analysis on large codebases and can process pyright’s reportMissing* diagnostic categories to prioritize the most impactful typing improvements. Additional capabilities include generating type stubs (.pyi files) for untyped internal modules using stubgen, recommending typing_extensions backports for older Python versions, and creating py.typed marker files for PEP 561 compliance. The skill produces prioritized fix lists sorted by module import frequency (most-imported modules first) to maximize downstream type inference improvements, and can auto-generate TypedDict definitions from runtime JSON schema analysis.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/python-type-coverage-analyzer/)
