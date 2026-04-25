---
title: "Apache Tika Document Parser"
description: "Extracts structured text, metadata, and embedded objects from PDFs, Office documents, and 1000+ file formats using the Apache Tika REST API. Outputs clean Markdown or JSON with XMP metadata preservation."
verification: "security_reviewed"
source: "https://github.com/apache/tika"
category:
  - "Data Extraction & Transformation"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "apache/tika"
  github_stars: 3703
---

# Apache Tika Document Parser

The Apache Tika Document Parser skill provides universal document extraction using the Apache Tika content analysis framework via its REST API. It handles over 1,000 file formats including PDF, DOCX, XLSX, PPTX, EML, MSG, HTML, and legacy formats like WPD and RTF. The skill sends documents to a Tika server instance and retrieves extracted text in multiple output formats: plain text, XHTML, or structured JSON. It preserves document metadata including XMP, Dublin Core, and format-specific properties. For PDFs, it leverages Tika’s OCR integration via Tesseract for scanned document text extraction. Advanced capabilities include recursive extraction of embedded objects (images, attachments in emails, OLE objects in Office documents), language detection using Tika’s language identifier, and content-type detection independent of file extensions. The skill supports batch processing with configurable parallelism and outputs clean Markdown suitable for LLM consumption or vector embedding pipelines.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/apache-tika-document-parser/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/apache-tika-document-parser
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/apache-tika-document-parser`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apache-tika-document-parser/)
