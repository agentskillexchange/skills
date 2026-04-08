---
title: ESLint Custom Rule Generator
description: The ESLint Custom Rule Generator skill creates production-ready ESLint
  rules from natural language descriptions of coding patterns to enforce or forbid.
  It generates complete rule modules compatible with ESLint v8 and v9 flat config,
  including meta.schema for rule options, meta.messages for configurable error messages,
  and auto-fix functions using the ESLint Fixer API. The skill uses AST pattern matching
  based on ESTree node types (as documented on AST Explorer) to construct precise
  selectors for the code patterns being targeted. It handles complex scenarios like
  tracking variable scope across function boundaries using the eslint-scope library,
  detecting patterns in JSX/TSX via @typescript-eslint/parser AST extensions, and
  analyzing import/export relationships. Generated rules include comprehensive test
  suites using ESLint RuleTester with valid and invalid code examples, edge cases
  for commented-out code and string literals, and TypeScript-specific test cases when
  applicable. The skill also generates rule documentation in the standard ESLint rule
  doc format with correct/incorrect code examples, and can create shareable ESLint
  plugin packages with proper exports and peer dependency declarations.
verification: security_reviewed
source: https://agentskillexchange.com/skills/eslint-custom-rule-generator/
category:
- Code Quality &amp; Review
framework:
- Claude Code
---

# ESLint Custom Rule Generator

The ESLint Custom Rule Generator skill creates production-ready ESLint rules from natural language descriptions of coding patterns to enforce or forbid. It generates complete rule modules compatible with ESLint v8 and v9 flat config, including meta.schema for rule options, meta.messages for configurable error messages, and auto-fix functions using the ESLint Fixer API. The skill uses AST pattern matching based on ESTree node types (as documented on AST Explorer) to construct precise selectors for the code patterns being targeted. It handles complex scenarios like tracking variable scope across function boundaries using the eslint-scope library, detecting patterns in JSX/TSX via @typescript-eslint/parser AST extensions, and analyzing import/export relationships. Generated rules include comprehensive test suites using ESLint RuleTester with valid and invalid code examples, edge cases for commented-out code and string literals, and TypeScript-specific test cases when applicable. The skill also generates rule documentation in the standard ESLint rule doc format with correct/incorrect code examples, and can create shareable ESLint plugin packages with proper exports and peer dependency declarations.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-custom-rule-generator/)
