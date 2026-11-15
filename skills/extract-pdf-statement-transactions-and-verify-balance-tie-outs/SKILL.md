---
name: "Extract PDF statement transactions and verify balance tie-outs"
slug: "extract-pdf-statement-transactions-and-verify-balance-tie-outs"
description: "Extract bank and card statement PDFs into CSV or XLSX, check balances and totals, and return a reconciliation report with unresolved rows."
verification: "security_reviewed"
source: "https://github.com/OneWave-AI/claude-skills/tree/main/statement-extract-and-prove"
author: "OneWave AI"
publisher_type: "organization"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
---

# Extract PDF statement transactions and verify balance tie-outs

Extract bank and card statement PDFs into CSV or XLSX, check balances and totals, and return a reconciliation report with unresolved rows.

## Prerequisites

Shell, Python 3, pdfplumber; openpyxl for XLSX; OCRmyPDF and Tesseract for scanned PDFs

## Installation

Install or set up from the source-backed instructions:

Clone https://github.com/OneWave-AI/claude-skills into a new local checkout. Preserve the complete statement-extract-and-prove directory, including SKILL.md, scripts and references. For Claude Code, copy that directory into ~/.claude/skills/statement-extract-and-prove after creating the parent and confirming that the destination does not already exist; other compatible agents can use their documented skills directory. Use a dedicated Python virtual environment and install pdfplumber; add openpyxl for XLSX output. Run the commands from the installed statement-extract-and-prove directory. For scanned documents, separately install OCRmyPDF and Tesseract with appropriate language data. Review upstream files before execution. No connection to a bank or bookkeeping service is required.

- Source: https://github.com/OneWave-AI/claude-skills/tree/main/statement-extract-and-prove

## Documentation

- https://github.com/OneWave-AI/claude-skills/blob/main/statement-extract-and-prove/SKILL.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/extract-pdf-statement-transactions-and-verify-balance-tie-outs/)
