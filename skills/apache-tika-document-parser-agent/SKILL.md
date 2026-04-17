---
title: "Apache Tika Document Parser Agent"
description: "Extracts text and metadata from 1000+ file formats using Apache Tika server REST API. Handles PDF OCR via Tesseract integration, Office document parsing, and email archive extraction with MIME detection."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/apache-tika-document-parser-agent/"
category:
  - "Data Extraction & Transformation"
framework:
  - "Gemini"
---

# Apache Tika Document Parser Agent

The Apache Tika Document Parser Agent provides universal document parsing through the Apache Tika REST API, supporting over 1000 file formats including PDF, DOCX, PPTX, XLSX, EML, MSG, RTF, and various image formats. It connects to a Tika server instance and handles content extraction, metadata parsing, and language detection.

For scanned PDFs and image-heavy documents, the skill activates Tika’s Tesseract OCR integration, configuring OCR parameters like DPI, page segmentation mode, and language packs. The OCR pipeline includes image preprocessing with contrast enhancement and deskewing for improved recognition accuracy.

Metadata extraction covers standard Dublin Core fields, format-specific properties (PDF author, Word revision count, EXIF data), and custom XMP metadata. The skill normalizes extracted metadata into a consistent schema regardless of source format.

Email archive processing handles recursive extraction of attachments from EML and MSG files, preserving thread relationships and attachment hierarchies. MIME type detection uses Tika’s content-based detection (magic bytes) rather than file extensions for reliable format identification.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/apache-tika-document-parser-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/apache-tika-document-parser-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apache-tika-document-parser-agent/)
