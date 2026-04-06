---
name: "QuickBooks Online Invoice Reconciliation Agent"
description: "Connects to the QuickBooks Online Accounting API using OAuth 2.0 via the intuit-oauth Node.js SDK to fetch unpaid invoices and match them against bank transaction records. Discrepancies are flagged and a reconciliation report is generated as a PDF using PDFKit, then emailed via SendGrid."
category: "Data Extraction &amp; Transformation"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/quickbooks-invoice-reconciliation/"
---
# QuickBooks Online Invoice Reconciliation Agent

Connects to the QuickBooks Online Accounting API using OAuth 2.0 via the intuit-oauth Node.js SDK to fetch unpaid invoices and match them against bank transaction records. Discrepancies are flagged and a reconciliation report is generated as a PDF using PDFKit, then emailed via SendGrid.

QuickBooks Online Invoice Reconciliation Agent is built around SendGrid email delivery platform. The underlying ecosystem is represented by sendgrid/sendgrid-nodejs (3,054+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like mail/send, templates, contact lists, event webhooks, suppression groups and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to sendgrid so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Connects to the QuickBooks Online Accounting API using OAuth 2.0 via the intuit-oauth Node.js SDK to fetch unpaid invoices and match them against bank transaction records. Discrepancies are flagged and a reconciliation report is generated as a PDF using PDFKit, then emailed via SendGrid. The implementation typically relies on mail/send, templates, contact lists, event webhooks, suppression groups, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

- Accesses mail/send, templates, contact lists, event webhooks, suppression groups instead of scraping a UI, which makes runs easier to audit and retry.

- Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

- Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

- Fits into broader integration points such as transactional email, digests, notifications, and deliverability workflows.

Key integration points include transactional email, digests, notifications, and deliverability workflows. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill quickbooks-invoice-reconciliation
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill quickbooks-invoice-reconciliation -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill quickbooks-invoice-reconciliation -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill quickbooks-invoice-reconciliation -a codex
```

### OpenClaw

```bash
clawhub install quickbooks-invoice-reconciliation
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/quickbooks-invoice-reconciliation/)
