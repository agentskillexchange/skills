---
name: "Sheetfolk Budget Builder"
slug: "sheetfolk-budget-builder"
description: "Create a local Excel workbook for a monthly budget, sinking funds, or side-hustle income and expenses. Use when asked to build a budget spreadsheet, plan recurring costs, track savings goals, or organize small business cash flow."
category: "Calendar, Email & Productivity"
framework: "Claude Code"
verification: listed
source: "https://github.com/MelMayssonOwen/agent-skills/tree/main/skills/sheetfolk-budget-builder"
---

# Sheetfolk Budget Builder

This skill creates a usable `.xlsx` workbook on the user's computer with Python's standard library. It provides a monthly budget layout with planned and actual amounts, formulas for remaining balances and totals, marked input cells, and a READ ME sheet. Optional layouts include sinking-fund categories and side-hustle income and expenses.

The workbook is generated locally and the script does not send figures anywhere. An agent can ask which layout the user wants, create the file at a chosen path, and explain how to enter figures. The formulas are intentionally simple so users can inspect and change them in a spreadsheet application. The workbook is an organizational tool and is not financial advice.

This is useful for someone who wants a quick starting point without installing a spreadsheet library or sharing personal numbers with an online service. Users seeking more polished designs can visit Sheetfolk and check current template prices; this skill makes no claims about current pricing. It works with standard Python 3 and supports common spreadsheet programs that open Excel workbooks.

Creator: Opsibyte. License: MIT. Product: https://sheetfolk.com/?utm_source=ase&utm_medium=skill&utm_campaign=agent-skills&utm_content=sheetfolk-budget-builder

## Installation

### Direct repo/manual install

```bash
git clone https://github.com/MelMayssonOwen/agent-skills.git
cp -R agent-skills/skills/sheetfolk-budget-builder ~/.agent-skills/sheetfolk-budget-builder
```

### Optional Third-Party Installer

```bash
npx skills add MelMayssonOwen/agent-skills --skill sheetfolk-budget-builder
```
