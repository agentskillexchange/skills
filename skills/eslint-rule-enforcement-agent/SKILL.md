---
name: "ESLint Rule Enforcement Agent"
description: "Automates ESLint configuration and rule enforcement using the ESLint Node.js API and @typescript-eslint/parser. Generates fix suggestions and auto-corrects violations across JavaScript and TypeScript codebases."
category: "Code Quality & Review"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/eslint-rule-enforcement-agent/"
---
# ESLint Rule Enforcement Agent

Automates ESLint configuration and rule enforcement using the ESLint Node.js API and @typescript-eslint/parser. Generates fix suggestions and auto-corrects violations across JavaScript and TypeScript codebases.

The ESLint Rule Enforcement Agent skill leverages the ESLint Node.js API (new ESLint(), linter.verify(), linter.verifyAndFix()) along with @typescript-eslint/parser and @typescript-eslint/eslint-plugin to enforce coding standards across JavaScript and TypeScript projects. It supports flat config (eslint.config.js) and legacy .eslintrc formats.



The skill can initialize project configurations using eslint –init, scan entire repositories with configurable ignore patterns via .eslintignore, and apply automatic fixes using the –fix flag. It integrates with popular rule sets including eslint-config-airbnb, eslint-config-standard, and eslint-plugin-react for framework-specific linting.



Advanced features include custom rule creation using the RuleTester API, shareable config package generation, IDE integration configuration for VS Code (eslint.validate settings), and CI pipeline integration with JUnit XML report output via eslint-formatter-junit. The agent can also manage rule severity overrides, disable directives (eslint-disable comments), and generate compliance reports showing violation trends over time.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-enforcement-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-enforcement-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-enforcement-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-enforcement-agent -a codex
```

### OpenClaw

```bash
clawhub install eslint-rule-enforcement-agent
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-enforcement-agent/)
