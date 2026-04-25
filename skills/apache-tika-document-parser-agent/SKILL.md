---
title: "Apache Tika Document Parser Agent"
description: "Extracts text and metadata from 1000+ file formats using Apache Tika server REST API. Handles PDF OCR via Tesseract integration, Office document parsing, and email archive extraction with MIME detection."
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

# Apache Tika Document Parser Agent

The Apache Tika Document Parser Agent provides universal document parsing through the Apache Tika REST API, supporting over 1000 file formats including PDF, DOCX, PPTX, XLSX, EML, MSG, RTF, and various image formats. It connects to a Tika server instance and handles content extraction, metadata parsing, and language detection.

For scanned PDFs and image-heavy documents, the skill activates Tika’s Tesseract OCR integration, configuring OCR parameters like DPI, page segmentation mode, and language packs. The OCR pipeline includes image preprocessing with contrast enhancement and deskewing for improved recognition accuracy.

Metadata extraction covers standard Dublin Core fields, format-specific properties (PDF author, Word revision count, EXIF data), and custom XMP metadata. The skill normalizes extracted metadata into a consistent schema regardless of source format.

Email archive processing handles recursive extraction of attachments from EML and MSG files, preserving thread relationships and attachment hierarchies. MIME type detection uses Tika’s content-based detection (magic bytes) rather than file extensions for reliable format identification.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/apache-tika-document-parser-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/apache-tika-document-parser-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/apache-tika-document-parser-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apache-tika-document-parser-agent/)
