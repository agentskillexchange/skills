---
name: "Apache Tika Document Parser Agent"
description: "Extracts text and metadata from 1000+ file formats using Apache Tika server REST API. Handles PDF OCR via Tesseract integration, Office document parsing, and email archive extraction with MIME detection."
category: "Data Extraction & Transformation"
framework: "Gemini"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/apache-tika-document-parser-agent/"
---

# Apache Tika Document Parser Agent

Extracts text and metadata from 1000+ file formats using Apache Tika server REST API. Handles PDF OCR via Tesseract integration, Office document parsing, and email archive extraction with MIME detection.

## Overview

The Apache Tika Document Parser Agent provides universal document parsing through the Apache Tika REST API, supporting over 1000 file formats including PDF, DOCX, PPTX, XLSX, EML, MSG, RTF, and various image formats. It connects to a Tika server instance and handles content extraction, metadata parsing, and language detection.

For scanned PDFs and image-heavy documents, the skill activates Tika’s Tesseract OCR integration, configuring OCR parameters like DPI, page segmentation mode, and language packs. The OCR pipeline includes image preprocessing with contrast enhancement and deskewing for improved recognition accuracy.

Metadata extraction covers standard Dublin Core fields, format-specific properties (PDF author, Word revision count, EXIF data), and custom XMP metadata. The skill normalizes extracted metadata into a consistent schema regardless of source format.

Email archive processing handles recursive extraction of attachments from EML and MSG files, preserving thread relationships and attachment hierarchies. MIME type detection uses Tika’s content-based detection (magic bytes) rather than file extensions for reliable format identification.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill apache-tika-document-parser-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill apache-tika-document-parser-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill apache-tika-document-parser-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill apache-tika-document-parser-agent -a codex
```

### OpenClaw

```bash
clawhub install apache-tika-document-parser-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/apache-tika-document-parser-agent/
