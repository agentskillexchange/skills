---
name: "ESLint Rule Violation Summarizer"
description: "Runs ESLint against a JS/TS codebase, groups violations by rule and file, and produces a prioritized fix plan. Distinguishes auto-fixable violations from manual ones. Outputs Markdown for GitHub PR comments."
category: "Code Quality &amp; Review"
framework: "Cursor"
verification: security_reviewed
source: "https://github.com/eslint/eslint"
tool_ecosystem:
  tool: eslint
  github_repo: eslint/eslint
  github_stars: 27153
  license: MIT
  maintained: true
---
# ESLint Rule Violation Summarizer

Runs ESLint against a JS/TS codebase, groups violations by rule and file, and produces a prioritized fix plan. Distinguishes auto-fixable violations from manual ones. Outputs Markdown for GitHub PR comments.

## Overview

ESLint Rule Violation Summarizer is built around ESLint static analysis for JavaScript and TypeScript. The underlying ecosystem is represented by eslint/eslint (27,186+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like eslint CLI, flat config, plugins, formatters, autofix, rule metadata and preserving the operational context that matters for real tasks.

For content workflows, the skill uses eslint primitives as the system of record, so an agent can read structured inputs, apply transformations, and publish or sync output without losing metadata, IDs, or status fields. The original use case is clear: Runs ESLint against a JS/TS codebase, groups violations by rule and file, and produces a prioritized fix plan. Distinguishes auto-fixable violations from manual ones. Outputs Markdown for GitHub PR comments. The implementation typically relies on eslint CLI, flat config, plugins, formatters, autofix, rule metadata, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses eslint CLI, flat config, plugins, formatters, autofix, rule metadata instead of scraping a UI, which makes runs easier to audit and retry.
Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
Fits into broader integration points such as code review automation, style enforcement, and CI lint gates.

 Key integration points include code review automation, style enforcement, and CI lint gates. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-violation-summarizer-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-violation-summarizer-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-violation-summarizer-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill eslint-rule-violation-summarizer-2 -a codex
```

### OpenClaw

```bash
clawhub install eslint-rule-violation-summarizer-2
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-violation-summarizer-2/)
