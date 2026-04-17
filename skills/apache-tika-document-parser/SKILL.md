---
title: "Apache Tika Document Parser"
description: "The Apache Tika Document Parser skill provides universal document extraction using the Apache Tika content analysis framework via its REST API. It handles over 1,000 file formats including PDF, DOCX, XLSX, PPTX, EML, MSG, HTML, and legacy formats like WPD and RTF.\nThe skill sends documents to a Tika server instance and retrieves extracted text in multiple output formats: plain text, XHTML, or structured JSON. It preserves document metadata including XMP, Dublin Core, and format-specific properties. For PDFs, it leverages Tika’s OCR integration via Tesseract for scanned document text extraction.\nAdvanced capabilities include recursive extraction of embedded objects (images, attachments in emails, OLE objects in Office documents), language detection using Tika’s language identifier, and content-type detection independent of file extensions. The skill supports batch processing with configurable parallelism and outputs clean Markdown suitable for LLM consumption or vector embedding pipelines."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/apache-tika-document-parser/"
framework:
  - "Gemini"
---

# Apache Tika Document Parser

The Apache Tika Document Parser skill provides universal document extraction using the Apache Tika content analysis framework via its REST API. It handles over 1,000 file formats including PDF, DOCX, XLSX, PPTX, EML, MSG, HTML, and legacy formats like WPD and RTF.
The skill sends documents to a Tika server instance and retrieves extracted text in multiple output formats: plain text, XHTML, or structured JSON. It preserves document metadata including XMP, Dublin Core, and format-specific properties. For PDFs, it leverages Tika’s OCR integration via Tesseract for scanned document text extraction.
Advanced capabilities include recursive extraction of embedded objects (images, attachments in emails, OLE objects in Office documents), language detection using Tika’s language identifier, and content-type detection independent of file extensions. The skill supports batch processing with configurable parallelism and outputs clean Markdown suitable for LLM consumption or vector embedding pipelines.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/apache-tika-document-parser
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/apache-tika-document-parser` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apache-tika-document-parser/)
