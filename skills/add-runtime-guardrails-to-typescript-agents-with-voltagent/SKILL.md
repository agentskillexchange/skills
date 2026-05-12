---
title: "Add runtime guardrails to TypeScript agents with VoltAgent"
slug: "add-runtime-guardrails-to-typescript-agents-with-voltagent"
description: "Use VoltAgent to intercept, validate, and enforce input/output policies in TypeScript agent workflows."
verification: "listed"
source: "https://github.com/VoltAgent/voltagent"
category: "Security & Verification"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "VoltAgent/voltagent"
  github_stars: 8647
---

# Add runtime guardrails to TypeScript agents with VoltAgent

Use VoltAgent to intercept, validate, and enforce input/output policies in TypeScript agent workflows.

Operator workflow: identify the risky interaction boundary, add VoltAgent guardrail checks to the agent runtime, wire the agent tools/model provider, test expected allow/block behavior, and monitor the workflow in development or operations.

## Prerequisites

- Node.js / TypeScript
- VoltAgent packages (`@voltagent/*`)
- Target model provider credentials

## Setup

Install the required VoltAgent packages for the agent project and follow the guardrails documentation:

```
npm install @voltagent/core
```

## Documentation

- https://voltagent.dev/docs/guardrails/overview/
- https://voltagent.dev/docs/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/add-runtime-guardrails-to-typescript-agents-with-voltagent/)
