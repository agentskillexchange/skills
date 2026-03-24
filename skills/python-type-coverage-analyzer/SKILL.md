---
name: "Python Type Coverage Analyzer"
description: "Measures and improves Python type annotation coverage using mypy –html-report and pyright type completeness scoring. Identifies untyped function signatures, missing return types, and Any-typed parameters across codebases."
category: "Code Quality & Review"
framework: "Gemini"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/python-type-coverage-analyzer/"
---

# Python Type Coverage Analyzer

Measures and improves Python type annotation coverage using mypy –html-report and pyright type completeness scoring. Identifies untyped function signatures, missing return types, and Any-typed parameters across codebases.

## Overview

The Python Type Coverage Analyzer skill assesses and improves type annotation completeness across Python codebases. It runs mypy with –html-report and –txt-report to generate coverage metrics, then processes pyright output in JSON mode to compute type completeness scores per module and identify specific locations where type information is missing.

The skill identifies untyped function parameters, missing return type annotations, implicit Any types from untyped third-party libraries, and overly broad Union types that could be narrowed. It leverages the mypy daemon (dmypy) for incremental analysis on large codebases and can process pyright’s reportMissing* diagnostic categories to prioritize the most impactful typing improvements.

Additional capabilities include generating type stubs (.pyi files) for untyped internal modules using stubgen, recommending typing_extensions backports for older Python versions, and creating py.typed marker files for PEP 561 compliance. The skill produces prioritized fix lists sorted by module import frequency (most-imported modules first) to maximize downstream type inference improvements, and can auto-generate TypedDict definitions from runtime JSON schema analysis.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill python-type-coverage-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill python-type-coverage-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill python-type-coverage-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill python-type-coverage-analyzer -a codex
```

### OpenClaw

```bash
clawhub install python-type-coverage-analyzer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/python-type-coverage-analyzer/
