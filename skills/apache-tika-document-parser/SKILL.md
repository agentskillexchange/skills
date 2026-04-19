---
title: "Apache Tika Document Parser"
description: "The Apache Tika Document Parser skill provides universal document extraction using the Apache Tika content analysis framework via its REST API. It handles over 1,000 file formats including PDF, DOCX, XLSX, PPTX, EML, MSG, HTML, and legacy formats like WPD and RTF. The skill sends documents to a Tika server instance and retrieves extracted text in multiple output formats: plain text, XHTML, or structured JSON. It preserves document metadata including XMP, Dublin Core, and format-specific properties. For PDFs, it leverages Tika&#8217;s OCR integration via Tesseract for scanned document text extraction. Advanced capabilities include recursive extraction of embedded objects (images, attachments in emails, OLE objects in Office documents), language detection using Tika&#8217;s language identifier, and content-type detection independent of file extensions. The skill supports batch processing with configurable parallelism and outputs clean Markdown suitable for LLM consumption or vector embedding pipelines."
source: "https://github.com/apache/tika"
verification: "security_reviewed"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "apache/tika"
  github_stars: 3703
---

# Apache Tika Document Parser

The Apache Tika Document Parser skill provides universal document extraction using the Apache Tika content analysis framework via its REST API. It handles over 1,000 file formats including PDF, DOCX, XLSX, PPTX, EML, MSG, HTML, and legacy formats like WPD and RTF. The skill sends documents to a Tika server instance and retrieves extracted text in multiple output formats: plain text, XHTML, or structured JSON. It preserves document metadata including XMP, Dublin Core, and format-specific properties. For PDFs, it leverages Tika&#8217;s OCR integration via Tesseract for scanned document text extraction. Advanced capabilities include recursive extraction of embedded objects (images, attachments in emails, OLE objects in Office documents), language detection using Tika&#8217;s language identifier, and content-type detection independent of file extensions. The skill supports batch processing with configurable parallelism and outputs clean Markdown suitable for LLM consumption or vector embedding pipelines.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apache-tika-document-parser/)
