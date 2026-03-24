---
name: "QuickBooks Online Invoice Reconciliation Agent"
description: "Connects to the QuickBooks Online Accounting API using OAuth 2.0 via the intuit-oauth Node.js SDK to fetch unpaid invoices and match them against bank transaction records. Discrepancies are flagged and a reconciliation report is generated as a PDF using PDFKit, then emailed via SendGrid."
category: "Data Extraction & Transformation"
framework: "Claude Code"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/quickbooks-invoice-reconciliation/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "sendgrid"  # from ase_tool_match
  github_stars: 3054  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 3287627  # from ase_npm_downloads
  github_repo: "sendgrid/sendgrid-nodejs"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# QuickBooks Online Invoice Reconciliation Agent

Connects to the QuickBooks Online Accounting API using OAuth 2.0 via the intuit-oauth Node.js SDK to fetch unpaid invoices and match them against bank transaction records. Discrepancies are flagged and a reconciliation report is generated as a PDF using PDFKit, then emailed via SendGrid.

## Overview

Connects to the QuickBooks Online Accounting API using OAuth 2.0 via the intuit-oauth Node.js SDK to fetch unpaid invoices and match them against bank transaction records. Discrepancies are flagged and a reconciliation report is generated as a PDF using PDFKit, then emailed via SendGrid.

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

- Marketplace: https://agentskillexchange.com/skills/quickbooks-invoice-reconciliation/
