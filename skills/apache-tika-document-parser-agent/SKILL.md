---
title: "Apache Tika Document Parser Agent"
description: "The Apache Tika Document Parser Agent provides universal document parsing through the Apache Tika REST API, supporting over 1000 file formats including PDF, DOCX, PPTX, XLSX, EML, MSG, RTF, and various image formats. It connects to a Tika server instance and handles content extraction, metadata parsing, and language detection. For scanned PDFs and image-heavy documents, the skill activates Tika&#8217;s Tesseract OCR integration, configuring OCR parameters like DPI, page segmentation mode, and language packs. The OCR pipeline includes image preprocessing with contrast enhancement and deskewing for improved recognition accuracy. Metadata extraction covers standard Dublin Core fields, format-specific properties (PDF author, Word revision count, EXIF data), and custom XMP metadata. The skill normalizes extracted metadata into a consistent schema regardless of source format. Email archive processing handles recursive extraction of attachments from EML and MSG files, preserving thread relationships and attachment hierarchies. MIME type detection uses Tika&#8217;s content-based detection (magic bytes) rather than file extensions for reliable format identification."
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

# Apache Tika Document Parser Agent

The Apache Tika Document Parser Agent provides universal document parsing through the Apache Tika REST API, supporting over 1000 file formats including PDF, DOCX, PPTX, XLSX, EML, MSG, RTF, and various image formats. It connects to a Tika server instance and handles content extraction, metadata parsing, and language detection. For scanned PDFs and image-heavy documents, the skill activates Tika&#8217;s Tesseract OCR integration, configuring OCR parameters like DPI, page segmentation mode, and language packs. The OCR pipeline includes image preprocessing with contrast enhancement and deskewing for improved recognition accuracy. Metadata extraction covers standard Dublin Core fields, format-specific properties (PDF author, Word revision count, EXIF data), and custom XMP metadata. The skill normalizes extracted metadata into a consistent schema regardless of source format. Email archive processing handles recursive extraction of attachments from EML and MSG files, preserving thread relationships and attachment hierarchies. MIME type detection uses Tika&#8217;s content-based detection (magic bytes) rather than file extensions for reliable format identification.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apache-tika-document-parser-agent/)
