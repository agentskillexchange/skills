---
title: Apache Tika Content Extraction Hub
description: The Apache Tika Content Extraction Hub provides universal document parsing
  through the Apache Tika Server REST API. It extracts text, metadata, and structure
  from over 1400 file formats including PDF, Microsoft Office (DOCX, XLSX, PPTX),
  email archives (MBOX, PST), and multimedia files. The skill communicates with Tika
  Server endpoints including /tika for text extraction, /meta for metadata parsing,
  /detect/stream for MIME type detection, and /rmeta for recursive metadata extraction
  from container formats. Batch processing supports concurrent extraction with configurable
  thread pools. Advanced PDF extraction uses Tika PDFParser with OCR fallback via
  integrated Tesseract for scanned pages. Embedded document extraction recursively
  processes attachments within ZIP archives, email messages, and OLE containers, maintaining
  parent-child document relationships. Metadata extraction captures Dublin Core, XMP,
  EXIF, and format-specific properties with normalization to a common schema. The
  agent supports custom Tika configurations for parser-specific settings like OCR
  language, PDF strategy (text vs OCR vs hybrid), and maximum extraction depth. Output
  formats include plain text, XHTML, and JSON with full metadata. Language detection
  via Tika LanguageIdentifier classifies extracted content across 70+ languages.
verification: security_reviewed
source: https://agentskillexchange.com/skills/apache-tika-content-extraction-hub/
category:
- Data Extraction &amp; Transformation
framework:
- Custom Agents
---

# Apache Tika Content Extraction Hub

The Apache Tika Content Extraction Hub provides universal document parsing through the Apache Tika Server REST API. It extracts text, metadata, and structure from over 1400 file formats including PDF, Microsoft Office (DOCX, XLSX, PPTX), email archives (MBOX, PST), and multimedia files. The skill communicates with Tika Server endpoints including /tika for text extraction, /meta for metadata parsing, /detect/stream for MIME type detection, and /rmeta for recursive metadata extraction from container formats. Batch processing supports concurrent extraction with configurable thread pools. Advanced PDF extraction uses Tika PDFParser with OCR fallback via integrated Tesseract for scanned pages. Embedded document extraction recursively processes attachments within ZIP archives, email messages, and OLE containers, maintaining parent-child document relationships. Metadata extraction captures Dublin Core, XMP, EXIF, and format-specific properties with normalization to a common schema. The agent supports custom Tika configurations for parser-specific settings like OCR language, PDF strategy (text vs OCR vs hybrid), and maximum extraction depth. Output formats include plain text, XHTML, and JSON with full metadata. Language detection via Tika LanguageIdentifier classifies extracted content across 70+ languages.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apache-tika-content-extraction-hub/)
