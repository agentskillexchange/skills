---
title: "Extract invoice fields from vendor PDFs into structured records"
description: "Uses invoice2data to turn invoice PDFs into structured JSON, CSV, or XML using supplier-specific templates. This is for repeatable invoice field extraction and renaming workflows, not for full accounting system automation or generic OCR catalog listings."
verification: "security_reviewed"
source: "https://github.com/invoice-x/invoice2data"
category:
  - "Data Extraction & Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "invoice-x/invoice2data"
  github_stars: 2137
---

# Extract invoice fields from vendor PDFs into structured records

Tool used: invoice2data.


This skill is for agents that need to pull real accounting fields out of vendor invoices and hand back structured records that another system can trust. An agent can run invoice2data over one file or a folder, choose the right text extraction backend, apply built-in or custom templates, and emit normalized JSON, CSV, or XML containing fields such as invoice number, date, amount, currency, partner name, and line items when templates support them.


Invoke this instead of using the product manually when the user has recurring invoices from known suppliers and wants the extraction step automated. The agent can select or maintain supplier templates, run debug mode when a new layout appears, and slot the extracted data into downstream bookkeeping, approval, or reconciliation flows. That is much more useful than simply handing someone a PDF parser and asking them to do the rest.


The scope boundary keeps this skill-shaped. It is not an ERP, not an accounts-payable platform, and not a generic OCR or document-management listing. The job is specifically invoice field extraction from supplier documents into structured machine-readable records, using invoice2data’s template system and extraction backends.


Integration points are clear in upstream docs: OCRmyPDF, Tesseract, pdftotext, pdfminer, pdfplumber, and Google Cloud Vision can all serve as input readers; outputs can feed spreadsheets, finance pipelines, archive renaming jobs, or custom Python automations.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/extract-invoice-fields-from-vendor-pdfs-into-structured-records/)
