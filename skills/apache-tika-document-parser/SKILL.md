---
title: Apache Tika Document Parser
description: 'The Apache Tika Document Parser skill provides universal document extraction
  using the Apache Tika content analysis framework via its REST API. It handles over
  1,000 file formats including PDF, DOCX, XLSX, PPTX, EML, MSG, HTML, and legacy formats
  like WPD and RTF. The skill sends documents to a Tika server instance and retrieves
  extracted text in multiple output formats: plain text, XHTML, or structured JSON.
  It preserves document metadata including XMP, Dublin Core, and format-specific properties.
  For PDFs, it leverages Tika’s OCR integration via Tesseract for scanned document
  text extraction. Advanced capabilities include recursive extraction of embedded
  objects (images, attachments in emails, OLE objects in Office documents), language
  detection using Tika’s language identifier, and content-type detection independent
  of file extensions. The skill supports batch processing with configurable parallelism
  and outputs clean Markdown suitable for LLM consumption or vector embedding pipelines.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/apache-tika-document-parser/
category:
- Data Extraction &amp; Transformation
framework:
- Gemini
---

# Apache Tika Document Parser

The Apache Tika Document Parser skill provides universal document extraction using the Apache Tika content analysis framework via its REST API. It handles over 1,000 file formats including PDF, DOCX, XLSX, PPTX, EML, MSG, HTML, and legacy formats like WPD and RTF. The skill sends documents to a Tika server instance and retrieves extracted text in multiple output formats: plain text, XHTML, or structured JSON. It preserves document metadata including XMP, Dublin Core, and format-specific properties. For PDFs, it leverages Tika’s OCR integration via Tesseract for scanned document text extraction. Advanced capabilities include recursive extraction of embedded objects (images, attachments in emails, OLE objects in Office documents), language detection using Tika’s language identifier, and content-type detection independent of file extensions. The skill supports batch processing with configurable parallelism and outputs clean Markdown suitable for LLM consumption or vector embedding pipelines.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apache-tika-document-parser/)
