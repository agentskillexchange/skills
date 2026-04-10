---
name: "ESLint Rule Enforcement Agent"
description: "Automates ESLint configuration and rule enforcement using the ESLint Node.js API and @typescript-eslint/parser. Generates fix suggestions and auto-corrects violations across JavaScript and TypeScript codebases."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/eslint-rule-enforcement-agent/"
category:
  - "Code Quality &amp; Review"
framework:
  - "Claude Code"
---

# ESLint Rule Enforcement Agent

The ESLint Rule Enforcement Agent skill leverages the ESLint Node.js API (new ESLint(), linter.verify(), linter.verifyAndFix()) along with @typescript-eslint/parser and @typescript-eslint/eslint-plugin to enforce coding standards across JavaScript and TypeScript projects. It supports flat config (eslint.config.js) and legacy .eslintrc formats.
The skill can initialize project configurations using eslint -init, scan entire repositories with configurable ignore patterns via .eslintignore, and apply automatic fixes using the -fix flag. It integrates with popular rule sets including eslint-config-airbnb, eslint-config-standard, and eslint-plugin-react for framework-specific linting.
Advanced features include custom rule creation using the RuleTester API, shareable config package generation, IDE integration configuration for VS Code (eslint.validate settings), and CI pipeline integration with JUnit XML report output via eslint-formatter-junit. The agent can also manage rule severity overrides, disable directives (eslint-disable comments), and generate compliance reports showing violation trends over time.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-enforcement-agent/)
