---
title: "Convert dense PDFs into LLM-ready text and page-aligned markdown with olmOCR"
description: "Use olmOCR when an agent needs to turn scanned or layout-heavy documents into clean markdown or text before chunking, search, extraction, or citation workflows."
verification: listed
source: "https://github.com/allenai/olmocr"
category:
  - "Data Extraction & Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "allenai/olmocr"
  github_stars: 17135
---

# Convert dense PDFs into LLM-ready text and page-aligned markdown with olmOCR

Use olmOCR when the job is to convert PDFs or image-based documents into readable markdown or plain text with natural reading order, table handling, and header or footer cleanup. Invoke it instead of treating the original PDF as the working surface when downstream agent steps depend on clean text for retrieval, extraction, QA, or citation. The scope boundary is specific and skill-shaped: this is a document linearization and OCR preprocessing workflow, not a general document platform listing and not just a raw OCR model card.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/convert-dense-pdfs-into-llm-ready-text-and-page-aligned-markdown-with-olmocr
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/convert-dense-pdfs-into-llm-ready-text-and-page-aligned-markdown-with-olmocr` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/convert-dense-pdfs-into-llm-ready-text-and-page-aligned-markdown-with-olmocr/)
