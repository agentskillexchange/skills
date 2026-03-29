---
name: "DocuSign Contract Auto-Sender with Conditional Logic"
description: "Uses the DocuSign eSignature REST API SDK to programmatically create envelope definitions with conditional routing rules based on contract value thresholds. Signers are resolved from a Salesforce SOQL query via the JSForce SDK, and envelope status updates are tracked via DocuSign Connect webhooks."
category: "Security & Verification"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/docusign-contract-auto-sender/"
tool_ecosystem:
  tool: salesforce
  github_stars: 1452
  npm_weekly_downloads: 804753
  github_repo: jsforce/jsforce
  license: MIT
  maintained: true
---
# DocuSign Contract Auto-Sender with Conditional Logic

Uses the DocuSign eSignature REST API SDK to programmatically create envelope definitions with conditional routing rules based on contract value thresholds. Signers are resolved from a Salesforce SOQL query via the JSForce SDK, and envelope status updates are tracked via DocuSign Connect webhooks.

## Overview

**DocuSign Contract Auto-Sender with Conditional Logic** is built around Salesforce CRM platform. The underlying ecosystem is represented by `jsforce/jsforce` (1,452+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like SOQL, REST API, objects, workflows, envelopes, records, sync and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to salesforce so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Uses the DocuSign eSignature REST API SDK to programmatically create envelope definitions with conditional routing rules based on contract value thresholds. Signers are resolved from a Salesforce SOQL query via the JSForce SDK, and envelope status updates are tracked via DocuSign Connect webhooks. The implementation typically relies on SOQL, REST API, objects, workflows, envelopes, records, sync, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses SOQL, REST API, objects, workflows, envelopes, records, sync instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as CRM integration, contract routing, and sales operations automation.

Key integration points include CRM integration, contract routing, and sales operations automation. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill docusign-contract-auto-sender
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill docusign-contract-auto-sender -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill docusign-contract-auto-sender -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill docusign-contract-auto-sender -a codex
```

### OpenClaw

```bash
clawhub install docusign-contract-auto-sender
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docusign-contract-auto-sender/)
