---
name: "ESLint Rule Enforcer Agent"
description: "Runs ESLint with custom rulesets via the ESLint Node.js API and eslint-plugin-import to enforce project-specific code standards. Parses AST violations, groups by severity, and generates fix-ready patches using eslint –fix output diffs."
category: "Code Quality &amp; Review"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/eslint-rule-enforcer-agent/"
---
# ESLint Rule Enforcer Agent

Runs ESLint with custom rulesets via the ESLint Node.js API and eslint-plugin-import to enforce project-specific code standards. Parses AST violations, groups by severity, and generates fix-ready patches using eslint –fix output diffs.

The ESLint Rule Enforcer Agent integrates directly with the ESLint Node.js API to perform deep static analysis on JavaScript and TypeScript codebases. It loads project-specific configurations from .eslintrc.json or eslint.config.mjs (flat config), applies rule overrides per directory, and leverages eslint-plugin-import for module resolution checks. The agent parses the JSON formatter output to extract violation nodes, maps them to AST locations, and groups findings by severity (error, warning, off). For auto-fixable issues, it invokes eslint –fix in dry-run mode to generate unified diff patches that can be applied via git apply. It supports custom rule authoring through the RuleContext API, enabling teams to codify domain-specific patterns. Integrates with GitHub Actions via problem matchers for inline annotations and supports caching via eslint –cache to minimize re-analysis on incremental changes.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-enforcer-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-enforcer-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-enforcer-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-enforcer-agent -a codex
```

### OpenClaw

```bash
clawhub install eslint-rule-enforcer-agent
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-enforcer-agent/)
