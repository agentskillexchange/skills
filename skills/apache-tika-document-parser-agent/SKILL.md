---
title: "Apache Tika Document Parser Agent"
description: "Extracts text and metadata from 1000+ file formats using Apache Tika server REST API. Handles PDF OCR via Tesseract integration, Office document parsing, and email archive extraction with MIME detection."
slug: "apache-tika-document-parser-agent"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/apache-tika-document-parser-agent/"
---

# Apache Tika Document Parser Agent

Extracts text and metadata from 1000+ file formats using Apache Tika server REST API. Handles PDF OCR via Tesseract integration, Office document parsing, and email archive extraction with MIME detection.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install apache-tika-document-parser-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Apache Tika Document Parser Agent provides universal document parsing through the Apache Tika REST API, supporting over 1000 file formats including PDF, DOCX, PPTX, XLSX, EML, MSG, RTF, and various image formats. It connects to a Tika server instance and handles content extraction, metadata parsing, and language detection.
For scanned PDFs and image-heavy documents, the skill activates Tika’s Tesseract OCR integration, configuring OCR parameters like DPI, page segmentation mode, and language packs. The OCR pipeline includes image preprocessing with contrast enhancement and deskewing for improved recognition accuracy.
Metadata extraction covers standard Dublin Core fields, format-specific properties (PDF author, Word revision count, EXIF data), and custom XMP metadata. The skill normalizes extracted metadata into a consistent schema regardless of source format.
Email archive processing handles recursive extraction of attachments from EML and MSG files, preserving thread relationships and attachment hierarchies. MIME type detection uses Tika’s content-based detection (magic bytes) rather than file extensions for reliable format identification.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apache-tika-document-parser-agent/)
