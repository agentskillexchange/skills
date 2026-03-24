---
name: "QuickBooks Online Invoice Reconciliation Agent"
description: "Connects to the QuickBooks Online Accounting API using OAuth 2.0 via the intuit-oauth Node.js SDK to fetch unpaid invoices and match them against bank transaction records. Discrepancies are flagged and a reconciliation report is generated as a PDF using PDFKit, then emailed via SendGrid."
category: "Data Extraction & Transformation"
framework: "Claude Code"
verification: listed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/quickbooks-invoice-reconciliation/"
tool_ecosystem:
  tool: "sendgrid"
  github_stars: 3054
  npm_weekly_downloads: 3287627
  github_repo: "sendgrid/sendgrid-nodejs"
  license: "MIT"
  maintained: true
---

# QuickBooks Online Invoice Reconciliation Agent

Connects to the QuickBooks Online Accounting API using OAuth 2.0 via the intuit-oauth Node.js SDK to fetch unpaid invoices and match them against bank transaction records. Discrepancies are flagged and a reconciliation report is generated as a PDF using PDFKit, then emailed via SendGrid.

## Installation

### Any Agent (npx)
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

| | |
|---|---|
| **Category** | Data Extraction & Transformation |
| **Framework** | Claude Code |
| **Verification** | 📋 Listed |
| **Tool** | [sendgrid](https://github.com/sendgrid/sendgrid-nodejs) — ⭐ 3.1k · MIT |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/quickbooks-invoice-reconciliation/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
