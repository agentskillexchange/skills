---
title: "ESLint Rule Violation Summarizer"
description: "Runs ESLint against a JS/TS codebase, groups violations by rule and file, and produces a prioritized fix plan. Distinguishes auto-fixable violations from manual ones. Outputs Markdown for GitHub PR comments."
slug: "eslint-rule-violation-summarizer-2"
category:
  - "Code Quality &amp; Review"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/eslint-rule-violation-summarizer-2/"
---

# ESLint Rule Violation Summarizer

Runs ESLint against a JS/TS codebase, groups violations by rule and file, and produces a prioritized fix plan. Distinguishes auto-fixable violations from manual ones. Outputs Markdown for GitHub PR comments.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install eslint-rule-violation-summarizer-2
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

ESLint Rule Violation Summarizer is built around ESLint static analysis for JavaScript and TypeScript. The underlying ecosystem is represented by eslint/eslint (27,186+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like eslint CLI, flat config, plugins, formatters, autofix, rule metadata and preserving the operational context that matters for real tasks.
For content workflows, the skill uses eslint primitives as the system of record, so an agent can read structured inputs, apply transformations, and publish or sync output without losing metadata, IDs, or status fields. The original use case is clear: Runs ESLint against a JS/TS codebase, groups violations by rule and file, and produces a prioritized fix plan. Distinguishes auto-fixable violations from manual ones. Outputs Markdown for GitHub PR comments. The implementation typically relies on eslint CLI, flat config, plugins, formatters, autofix, rule metadata, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.
- Accesses eslint CLI, flat config, plugins, formatters, autofix, rule metadata instead of scraping a UI, which makes runs easier to audit and retry.
- Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
- Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
- Fits into broader integration points such as code review automation, style enforcement, and CI lint gates.
Key integration points include code review automation, style enforcement, and CI lint gates. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-violation-summarizer-2/)
