---
name: "ESLint Rule Auditor"
description: "Audits ESLint configurations using @eslint/eslintrc and @eslint/js flat config APIs. Detects conflicting rules, deprecated configs, and generates migration paths from eslintrc to eslint.config.js flat config format."
category: "Code Quality & Review"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/eslint-rule-auditor-3/"
---
# ESLint Rule Auditor

Audits ESLint configurations using @eslint/eslintrc and @eslint/js flat config APIs. Detects conflicting rules, deprecated configs, and generates migration paths from eslintrc to eslint.config.js flat config format.

The ESLint Rule Auditor skill performs comprehensive analysis of ESLint configurations across JavaScript and TypeScript projects. It parses both legacy eslintrc and modern flat config formats using @eslint/eslintrc and @eslint/js APIs to build a complete picture of active rules, overrides, and plugin interactions.



The skill detects common configuration issues including conflicting rules between extends chains, deprecated rule usage flagged by eslint –print-config, overlapping plugin rules from @typescript-eslint/eslint-plugin and eslint-plugin-import, and misconfigured parser options. It evaluates rule severity distributions and identifies overly permissive configurations that may miss code quality issues.



For projects still using legacy eslintrc format, the auditor generates detailed migration plans to eslint.config.js flat config, mapping each extends entry to its equivalent flat config import and converting overrides patterns to the new glob-based configuration arrays. It also benchmarks rule execution times using TIMING=1 environment variable to identify slow rules impacting CI performance, and suggests equivalent faster alternatives where available.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-auditor-3
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-auditor-3 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-auditor-3 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-auditor-3 -a codex
```

### OpenClaw

```bash
clawhub install eslint-rule-auditor-3
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-auditor-3/)
