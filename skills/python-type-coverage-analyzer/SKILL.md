---
title: "Python Type Coverage Analyzer"
description: "Measures and improves Python type annotation coverage using mypy –html-report and pyright type completeness scoring. Identifies untyped function signatures, missing return types, and Any-typed parameters across codebases."
slug: "python-type-coverage-analyzer"
category:
  - "Code Quality &amp; Review"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/python-type-coverage-analyzer/"
listed: true
---

# Python Type Coverage Analyzer

Measures and improves Python type annotation coverage using mypy –html-report and pyright type completeness scoring. Identifies untyped function signatures, missing return types, and Any-typed parameters across codebases.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install python-type-coverage-analyzer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Python Type Coverage Analyzer skill assesses and improves type annotation completeness across Python codebases. It runs mypy with –html-report and –txt-report to generate coverage metrics, then processes pyright output in JSON mode to compute type completeness scores per module and identify specific locations where type information is missing.
The skill identifies untyped function parameters, missing return type annotations, implicit Any types from untyped third-party libraries, and overly broad Union types that could be narrowed. It leverages the mypy daemon (dmypy) for incremental analysis on large codebases and can process pyright’s reportMissing* diagnostic categories to prioritize the most impactful typing improvements.
Additional capabilities include generating type stubs (.pyi files) for untyped internal modules using stubgen, recommending typing_extensions backports for older Python versions, and creating py.typed marker files for PEP 561 compliance. The skill produces prioritized fix lists sorted by module import frequency (most-imported modules first) to maximize downstream type inference improvements, and can auto-generate TypedDict definitions from runtime JSON schema analysis.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/python-type-coverage-analyzer/)
