---
name: "GraphQL Introspection Schema Change Reporter"
description: "Compares two GraphQL introspection results and reports breaking, dangerous, and additive changes across types, fields, arguments, enums, and directives. It helps teams monitor API evolution before a frontend build, SDK release, or agent workflow starts failing silently."
category: "Library & API Reference"
framework: "OpenClaw"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/graphql-introspection-schema-change-reporter-20260324/"
---

# GraphQL Introspection Schema Change Reporter

Compares two GraphQL introspection results and reports breaking, dangerous, and additive changes across types, fields, arguments, enums, and directives. It helps teams monitor API evolution before a frontend build, SDK release, or agent workflow starts failing silently.

## Overview

This skill monitors the evolution of a **GraphQL** API by diffing two introspection snapshots and summarizing what actually changed. Instead of scanning raw JSON manually, it classifies additions, removals, type mutations, enum value shifts, argument changes, and deprecations in a way that matters to clients. That is especially useful when a schema is shared across web apps, mobile apps, automation agents, and generated SDKs. A field disappearing from a type or changing nullability can break far more than one UI, so the skill turns schema drift into a readable technical report.

The workflow can use the standard introspection query, a GraphQL endpoint behind auth, or a schema file checked into git. It then builds a diff summary and tags each change as additive, dangerous, or breaking, similar to GraphQL Inspector. Outputs can include Markdown reports for pull requests, JSON for CI/CD gates, and a smaller changelog focused on impacted operations or fragments. Integration points include Apollo Client, Relay, urql, GraphQL Code Generator, GitHub Actions, and Slack or webhook notifications when a schema change crosses a policy threshold. Teams can use it before releasing a new backend, regenerating TypeScript types, or updating cached query documents. The result is a lightweight schema governance layer that keeps GraphQL contracts visible and actionable.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill graphql-introspection-schema-change-reporter-20260324
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill graphql-introspection-schema-change-reporter-20260324 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill graphql-introspection-schema-change-reporter-20260324 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill graphql-introspection-schema-change-reporter-20260324 -a codex
```

### OpenClaw

```bash
clawhub install graphql-introspection-schema-change-reporter-20260324
```

## Source

- Marketplace: https://agentskillexchange.com/skills/graphql-introspection-schema-change-reporter-20260324/
