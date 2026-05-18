---
name: "Regex Pattern Test Suite Generator"
slug: "regex-pattern-test-suite-generator"
description: "Generates comprehensive test suites for regular expressions using Hypothesis property-based testing and re2 for safe evaluation. Creates positive/negative test cases, edge cases, and ReDoS vulnerability checks."
github_stars: 8605
verification: "listed"
source: "https://github.com/HypothesisWorks/hypothesis"
author: "HypothesisWorks"
category: "Developer Tools"
framework: "Cursor"
tool_ecosystem:
  github_repo: "HypothesisWorks/hypothesis"
  github_stars: 8605
---

# Regex Pattern Test Suite Generator

Generates comprehensive test suites for regular expressions using Hypothesis property-based testing and re2 for safe evaluation. Creates positive/negative test cases, edge cases, and ReDoS vulnerability checks.

## Installation

Use the upstream install or setup path that matches your environment:
- pip install hypothesis

Requirements and caveats from upstream:
- Hypothesis is the property-based testing library for Python. With Hypothesis, you write tests which should pass for all inputs in whatever range you describe, and let Hypothesis randomly choose which of those inputs t...
- python

Basic usage or getting-started notes:
- This randomized testing can catch bugs and edge cases that you didn't think of and wouldn't have found. In addition, when Hypothesis does find a bug, it doesn't just report any failing example — it reports the simples...
- fails with the simplest possible failing example:
- Falsifying example: test_matches_builtin(ls=[0, 0])

- Source: https://github.com/HypothesisWorks/hypothesis
- Extracted from upstream docs: https://raw.githubusercontent.com/HypothesisWorks/hypothesis/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/regex-pattern-test-suite-generator/)
