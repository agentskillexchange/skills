---
name: ESLint Code Review
description: "ESLint Code Review is built around ESLint static analysis for JavaScript\
  \ and TypeScript. The underlying ecosystem is represented by eslint/eslint (27,186+\
  \ GitHub stars). It gives an agent a more technical and reliable way to work with\
  \ the tool than a thin one-line wrapper, using stable interfaces like eslint CLI,\
  \ flat config, plugins, formatters, autofix, rule […]"
category: Developer Tools
framework: Claude Code
verification: security_reviewed
source: "https://github.com/eslint/eslint"
tool_ecosystem:
  github_repo: "https://github.com/eslint/eslint"
  github_stars: 27141
  npm_package: eslint
---
# ESLint Code Review

ESLint Code Review is built around ESLint static analysis for JavaScript and TypeScript. The underlying ecosystem is represented by eslint/eslint (27,186+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like eslint CLI, flat config, plugins, formatters, autofix, rule […]

ESLint Code Review is built around ESLint static analysis for JavaScript and TypeScript. The underlying ecosystem is represented by eslint/eslint (27,186+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like eslint CLI, flat config, plugins, formatters, autofix, rule metadata and preserving the operational context that matters for real tasks.

For testing and review work, the skill wraps the normal eslint commands into a repeatable analysis loop that can produce summaries, prioritized findings, and CI-friendly output instead of a wall of raw logs. The implementation typically relies on eslint CLI, flat config, plugins, formatters, autofix, rule metadata, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

- Accesses eslint CLI, flat config, plugins, formatters, autofix, rule metadata instead of scraping a UI, which makes runs easier to audit and retry.

- Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

- Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

- Fits into broader integration points such as code review automation, style enforcement, and CI lint gates.

Key integration points include code review automation, style enforcement, and CI lint gates. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill eslint-code-review
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill eslint-code-review -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill eslint-code-review -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill eslint-code-review -a codex
```

### OpenClaw

```bash
clawhub install eslint-code-review
```


## Source

- [GitHub](https://github.com/eslint/eslint)
