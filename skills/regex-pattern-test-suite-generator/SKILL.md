---
title: "Regex Pattern Test Suite Generator"
description: "Generates comprehensive test suites for regular expressions using Hypothesis property-based testing and re2 for safe evaluation. Creates positive/negative test cases, edge cases, and ReDoS vulnerability checks."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/regex-pattern-test-suite-generator/"
category:
  - "Developer Tools"
framework:
  - "Cursor"
---

# Regex Pattern Test Suite Generator

The Regex Pattern Test Suite Generator skill automates the creation of thorough test suites for regular expressions, ensuring patterns behave correctly across edge cases and resist catastrophic backtracking. Using Hypothesis for property-based test generation, it synthesizes strings that should match and should not match based on regex analysis, covering boundary conditions that manual test creation typically misses. The re2 engine (Google RE2 via pyre2) provides a safe evaluation environment that guarantees linear-time matching, preventing ReDoS (Regular Expression Denial of Service) attacks during testing. The skill parses regex patterns into AST form to understand capture groups, lookaheads, backreferences, and quantifiers, then generates targeted test strings for each construct. For capture group patterns, it verifies that extracted groups contain expected content. Performance profiling measures matching time across input sizes to detect super-linear behavior even in patterns that pass re2 compilation. Generated test suites output in pytest format with parametrized test cases, or as JSON fixtures for use with other testing frameworks. The tool also suggests regex simplifications when it detects redundant alternations, unnecessary groups, or patterns that could use character classes instead of alternation.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/regex-pattern-test-suite-generator/)
