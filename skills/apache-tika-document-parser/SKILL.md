---
title: "Apache Tika Document Parser"
description: "Extracts structured text, metadata, and embedded objects from PDFs, Office documents, and 1000+ file formats using the Apache Tika REST API. Outputs clean Markdown or JSON with XMP metadata preservation."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/apache-tika-document-parser/"
category:
  - "Data Extraction & Transformation"
framework:
  - "Gemini"
---

# Apache Tika Document Parser

The Apache Tika Document Parser skill provides universal document extraction using the Apache Tika content analysis framework via its REST API. It handles over 1,000 file formats including PDF, DOCX, XLSX, PPTX, EML, MSG, HTML, and legacy formats like WPD and RTF.


The skill sends documents to a Tika server instance and retrieves extracted text in multiple output formats: plain text, XHTML, or structured JSON. It preserves document metadata including XMP, Dublin Core, and format-specific properties. For PDFs, it leverages Tika’s OCR integration via Tesseract for scanned document text extraction.


Advanced capabilities include recursive extraction of embedded objects (images, attachments in emails, OLE objects in Office documents), language detection using Tika’s language identifier, and content-type detection independent of file extensions. The skill supports batch processing with configurable parallelism and outputs clean Markdown suitable for LLM consumption or vector embedding pipelines.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apache-tika-document-parser/)
