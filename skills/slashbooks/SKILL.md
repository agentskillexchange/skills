---
name: "Slashbooks"
slug: "slashbooks"
description: "Replace QuickBooks with an AI agent you control: import bank and credit card activity, categorize and reconcile transactions, close the month, and export the files your accountant needs."
category: "Calendar, Email & Productivity"
framework: "Claude Code"
verification: listed
source: "https://github.com/giltotherescue/slashbooks"
---

# Slashbooks

Slashbooks is an open-source alternative to QuickBooks. An AI agent you control imports bank and card activity, closes the month, and creates the files your accountant needs. Instead of paying for a hosted bookkeeping SaaS plus an outsourced bookkeeper, you run the workflow yourself: point the agent at CSV or OFX exports from your bank and credit card providers, and it normalizes the transactions, applies a consistent chart of accounts, categorizes each line, flags duplicates and transfers between your own accounts, and reconciles ending balances against your statements.

When the month is closed it produces accountant-ready outputs: a categorized transaction ledger, a trial balance, and profit-and-loss and balance-sheet summaries you can hand to a CPA at tax time. Use this skill when you want month-end close, transaction categorization, reconciliation, or accountant hand-off files produced by an agent working on data you keep locally, so your financial data is never uploaded to a third-party bookkeeping vendor. Licensed Apache-2.0. Homepage: https://slashbooks.org

## Installation

### Direct repo/manual install

```bash
git clone https://github.com/giltotherescue/slashbooks.git
cp -R slashbooks ~/.agent-skills/slashbooks
```

### Claude Code / Cursor / Codex

```bash
git clone https://github.com/giltotherescue/slashbooks.git ~/.claude/skills/slashbooks
```
