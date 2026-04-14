---
title: "Python Type Coverage Analyzer"
description: "Measures and improves Python type annotation coverage using mypy –html-report and pyright type completeness scoring. Identifies untyped function signatures, missing return types, and Any-typed parameters across codebases."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/python-type-coverage-analyzer/"
category:
  - "Code Quality &amp; Review"
framework:
  - "Gemini"
---

# Python Type Coverage Analyzer

The Python Type Coverage Analyzer skill assesses and improves type annotation completeness across Python codebases. It runs mypy with –html-report and –txt-report to generate coverage metrics, then processes pyright output in JSON mode to compute type completeness scores per module and identify specific locations where type information is missing.

The skill identifies untyped function parameters, missing return type annotations, implicit Any types from untyped third-party libraries, and overly broad Union types that could be narrowed. It leverages the mypy daemon (dmypy) for incremental analysis on large codebases and can process pyright’s reportMissing* diagnostic categories to prioritize the most impactful typing improvements.

Additional capabilities include generating type stubs (.pyi files) for untyped internal modules using stubgen, recommending typing_extensions backports for older Python versions, and creating py.typed marker files for PEP 561 compliance. The skill produces prioritized fix lists sorted by module import frequency (most-imported modules first) to maximize downstream type inference improvements, and can auto-generate TypedDict definitions from runtime JSON schema analysis.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/python-type-coverage-analyzer/)
