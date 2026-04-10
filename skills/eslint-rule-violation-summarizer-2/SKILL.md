---
name: ESLint Rule Violation Summarizer
description: Runs ESLint against a JS/TS codebase, groups violations by rule and file,
  and produces a prioritized fix plan. Distinguishes auto-fixable violations from
  manual ones. Outputs Markdown for GitHub PR comments.
verification: security_reviewed
source: https://agentskillexchange.com/skills/eslint-rule-violation-summarizer-2/
category:
- Code Quality &amp; Review
framework:
- Cursor
---
# ESLint Rule Violation Summarizer

ESLint Rule Violation Summarizer is built around ESLint static analysis for JavaScript and TypeScript. The underlying ecosystem is represented by eslint/eslint (27,186+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like eslint CLI, flat config, plugins, formatters, autofix, rule metadata and preserving the operational context that matters for real tasks.
For content workflows, the skill uses eslint primitives as the system of record, so an agent can read structured inputs, apply transformations, and publish or sync output without losing metadata, IDs, or status fields. The original use case is clear: Runs ESLint against a JS/TS codebase, groups violations by rule and file, and produces a prioritized fix plan. Distinguishes auto-fixable violations from manual ones. Outputs Markdown for GitHub PR comments. The implementation typically relies on eslint CLI, flat config, plugins, formatters, autofix, rule metadata, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses eslint CLI, flat config, plugins, formatters, autofix, rule metadata instead of scraping a UI, which makes runs easier to audit and retry.
Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
Fits into broader integration points such as code review automation, style enforcement, and CI lint gates.

 Key integration points include code review automation, style enforcement, and CI lint gates. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/eslint-rule-violation-summarizer-2/)
