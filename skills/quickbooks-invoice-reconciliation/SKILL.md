---
title: "QuickBooks Online Invoice Reconciliation Agent"
description: "Connects to the QuickBooks Online Accounting API using OAuth 2.0 via the intuit-oauth Node.js SDK to fetch unpaid invoices and match them against bank transaction records. Discrepancies are flagged and a reconciliation report is generated as a PDF using PDFKit, then emailed via SendGrid."
verification: "security_reviewed"
source: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/most-commonly-used/invoice"
category:
  - "Data Extraction & Transformation"
framework:
  - "Claude Code"
---

# QuickBooks Online Invoice Reconciliation Agent

Connects to the QuickBooks Online Accounting API using OAuth 2.0 via the intuit-oauth Node.js SDK to fetch unpaid invoices and match them against bank transaction records. Discrepancies are flagged and a reconciliation report is generated as a PDF using PDFKit, then emailed via SendGrid.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/quickbooks-invoice-reconciliation/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/quickbooks-invoice-reconciliation
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/quickbooks-invoice-reconciliation`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/quickbooks-invoice-reconciliation/)
