---
name: "QuickBooks Online Invoice Reconciliation Agent"
slug: "quickbooks-invoice-reconciliation"
description: "Connects to the QuickBooks Online Accounting API using OAuth 2.0 via the intuit-oauth Node.js SDK to fetch unpaid invoices and match them against bank transaction records. Discrepancies are flagged and a reconciliation report is generated as a PDF using PDFKit, then emailed via SendGrid."
verification: "security_reviewed"
source: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/most-commonly-used/invoice"
author: "Intuit"
category: "Data Extraction & Transformation"
framework: "Claude Code"
---

# QuickBooks Online Invoice Reconciliation Agent

Connects to the QuickBooks Online Accounting API using OAuth 2.0 via the intuit-oauth Node.js SDK to fetch unpaid invoices and match them against bank transaction records. Discrepancies are flagged and a reconciliation report is generated as a PDF using PDFKit, then emailed via SendGrid.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Documentation

- https://developer.intuit.com/app/developer/qbo/docs/api/accounting/most-commonly-used/invoice

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/quickbooks-invoice-reconciliation/)
