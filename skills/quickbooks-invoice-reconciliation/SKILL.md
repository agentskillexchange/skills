---
name: "QuickBooks Online Invoice Reconciliation Agent"
description: "Connects to the QuickBooks Online Accounting API using OAuth 2.0 via the intuit-oauth Node.js SDK to fetch unpaid invoices and match them against bank transaction records. Discrepancies are flagged and a reconciliation report is generated as a PDF using PDFKit, then emailed via SendGrid."
category: "Data Extraction & Transformation"
framework: "Claude Code"
verification: verified_metadata
rating: 4.5
reviews: 8
creator: "Nathan Brooks"
creator_handle: "@nbrooks"
creator_verified: false
source: "https://agentskillexchange.com/skills/quickbooks-invoice-reconciliation/"
---
# QuickBooks Online Invoice Reconciliation Agent

Connects to the QuickBooks Online Accounting API using OAuth 2.0 via the intuit-oauth Node.js SDK to fetch unpaid invoices and match them against bank transaction records. Discrepancies are flagged and a reconciliation report is generated as a PDF using PDFKit, then emailed via SendGrid.

## Installation

### Any agent (npx skills)

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

### OpenClaw

```bash
clawhub install quickbooks-invoice-reconciliation
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill quickbooks-invoice-reconciliation -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Data Extraction & Transformation |
| Framework | Claude Code |
| Verification | Verified Metadata |
| Rating | 4.5/5 (8 reviews) |

## Creator

**Nathan Brooks**
- Profile: [@nbrooks](https://agentskillexchange.com/browse-skills/?creator=nbrooks)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/quickbooks-invoice-reconciliation/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
