---
title: "Convert dense PDFs into LLM-ready text and page-aligned markdown with olmOCR"
description: "Use olmOCR when the job is to convert PDFs or image-based documents into readable markdown or plain text with natural reading order, table handling, and header or footer cleanup. Invoke it instead of treating the original PDF as the working surface when downstream agent steps depend on clean text for retrieval, extraction, QA, or citation. The scope boundary is specific and skill-shaped: this is a document linearization and OCR preprocessing workflow, not a general document platform listing and not just a raw OCR model card."
source: "https://github.com/allenai/olmocr"
verification: "listed"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "allenai/olmocr"
  github_stars: 17135
---

# Convert dense PDFs into LLM-ready text and page-aligned markdown with olmOCR

Use olmOCR when the job is to convert PDFs or image-based documents into readable markdown or plain text with natural reading order, table handling, and header or footer cleanup. Invoke it instead of treating the original PDF as the working surface when downstream agent steps depend on clean text for retrieval, extraction, QA, or citation. The scope boundary is specific and skill-shaped: this is a document linearization and OCR preprocessing workflow, not a general document platform listing and not just a raw OCR model card.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/convert-dense-pdfs-into-llm-ready-text-and-page-aligned-markdown-with-olmocr/)
