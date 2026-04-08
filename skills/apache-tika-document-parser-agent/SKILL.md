---
title: Apache Tika Document Parser Agent
description: The Apache Tika Document Parser Agent provides universal document parsing
  through the Apache Tika REST API, supporting over 1000 file formats including PDF,
  DOCX, PPTX, XLSX, EML, MSG, RTF, and various image formats. It connects to a Tika
  server instance and handles content extraction, metadata parsing, and language detection.
  For scanned PDFs and image-heavy documents, the skill activates Tika’s Tesseract
  OCR integration, configuring OCR parameters like DPI, page segmentation mode, and
  language packs. The OCR pipeline includes image preprocessing with contrast enhancement
  and deskewing for improved recognition accuracy. Metadata extraction covers standard
  Dublin Core fields, format-specific properties (PDF author, Word revision count,
  EXIF data), and custom XMP metadata. The skill normalizes extracted metadata into
  a consistent schema regardless of source format. Email archive processing handles
  recursive extraction of attachments from EML and MSG files, preserving thread relationships
  and attachment hierarchies. MIME type detection uses Tika’s content-based detection
  (magic bytes) rather than file extensions for reliable format identification.
verification: security_reviewed
source: https://agentskillexchange.com/skills/apache-tika-document-parser-agent/
category:
- Data Extraction &amp; Transformation
framework:
- Gemini
---

# Apache Tika Document Parser Agent

The Apache Tika Document Parser Agent provides universal document parsing through the Apache Tika REST API, supporting over 1000 file formats including PDF, DOCX, PPTX, XLSX, EML, MSG, RTF, and various image formats. It connects to a Tika server instance and handles content extraction, metadata parsing, and language detection. For scanned PDFs and image-heavy documents, the skill activates Tika’s Tesseract OCR integration, configuring OCR parameters like DPI, page segmentation mode, and language packs. The OCR pipeline includes image preprocessing with contrast enhancement and deskewing for improved recognition accuracy. Metadata extraction covers standard Dublin Core fields, format-specific properties (PDF author, Word revision count, EXIF data), and custom XMP metadata. The skill normalizes extracted metadata into a consistent schema regardless of source format. Email archive processing handles recursive extraction of attachments from EML and MSG files, preserving thread relationships and attachment hierarchies. MIME type detection uses Tika’s content-based detection (magic bytes) rather than file extensions for reliable format identification.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apache-tika-document-parser-agent/)
