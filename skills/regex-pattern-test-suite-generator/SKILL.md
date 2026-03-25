---
name: "Regex Pattern Test Suite Generator"
description: "Generates comprehensive test suites for regular expressions using Hypothesis property-based testing and re2 for safe evaluation. Creates positive/negative test cases, edge cases, and ReDoS vulnerability checks."
category: "Developer Tools"
framework: "Cursor"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/regex-pattern-test-suite-generator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "pytest"  # from ase_tool_match
  github_stars: 13718  # from ase_github_stars (integer, not string)
  github_repo: "pytest-dev/pytest"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Regex Pattern Test Suite Generator

Generates comprehensive test suites for regular expressions using Hypothesis property-based testing and re2 for safe evaluation. Creates positive/negative test cases, edge cases, and ReDoS vulnerability checks.

## Overview

The Regex Pattern Test Suite Generator skill automates the creation of thorough test suites for regular expressions, ensuring patterns behave correctly across edge cases and resist catastrophic backtracking. Using Hypothesis for property-based test generation, it synthesizes strings that should match and should not match based on regex analysis, covering boundary conditions that manual test creation typically misses. The re2 engine (Google RE2 via pyre2) provides a safe evaluation environment that guarantees linear-time matching, preventing ReDoS (Regular Expression Denial of Service) attacks during testing. The skill parses regex patterns into AST form to understand capture groups, lookaheads, backreferences, and quantifiers, then generates targeted test strings for each construct. For capture group patterns, it verifies that extracted groups contain expected content. Performance profiling measures matching time across input sizes to detect super-linear behavior even in patterns that pass re2 compilation. Generated test suites output in pytest format with parametrized test cases, or as JSON fixtures for use with other testing frameworks. The tool also suggests regex simplifications when it detects redundant alternations, unnecessary groups, or patterns that could use character classes instead of alternation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill regex-pattern-test-suite-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill regex-pattern-test-suite-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill regex-pattern-test-suite-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill regex-pattern-test-suite-generator -a codex
```

### OpenClaw

```bash
clawhub install regex-pattern-test-suite-generator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/regex-pattern-test-suite-generator/
