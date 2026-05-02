---
title: "Regex Pattern Test Suite Generator"
description: "Generates comprehensive test suites for regular expressions using Hypothesis property-based testing and re2 for safe evaluation. Creates positive/negative test cases, edge cases, and ReDoS vulnerability checks."
verification: "security_reviewed"
source: "https://github.com/HypothesisWorks/hypothesis"
category:
  - "Developer Tools"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "HypothesisWorks/hypothesis"
  github_stars: 8605
---

# Regex Pattern Test Suite Generator

The Regex Pattern Test Suite Generator skill automates the creation of thorough test suites for regular expressions, ensuring patterns behave correctly across edge cases and resist catastrophic backtracking. Using Hypothesis for property-based test generation, it synthesizes strings that should match and should not match based on regex analysis, covering boundary conditions that manual test creation typically misses. The re2 engine (Google RE2 via pyre2) provides a safe evaluation environment that guarantees linear-time matching, preventing ReDoS (Regular Expression Denial of Service) attacks during testing. The skill parses regex patterns into AST form to understand capture groups, lookaheads, backreferences, and quantifiers, then generates targeted test strings for each construct. For capture group patterns, it verifies that extracted groups contain expected content. Performance profiling measures matching time across input sizes to detect super-linear behavior even in patterns that pass re2 compilation. Generated test suites output in pytest format with parametrized test cases, or as JSON fixtures for use with other testing frameworks. The tool also suggests regex simplifications when it detects redundant alternations, unnecessary groups, or patterns that could use character classes instead of alternation.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/regex-pattern-test-suite-generator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/regex-pattern-test-suite-generator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/regex-pattern-test-suite-generator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/regex-pattern-test-suite-generator/)
