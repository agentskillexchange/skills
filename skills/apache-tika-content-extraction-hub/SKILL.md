---
title: "Apache Tika Content Extraction Hub"
description: "Extracts text and metadata from 1400+ file formats via Apache Tika Server REST API. Handles PDF, DOCX, PPTX, email archives, and embedded document extraction with MIME type detection."
verification: "security_reviewed"
source: "https://github.com/apache/tika"
category:
  - "Data Extraction & Transformation"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "apache/tika"
  github_stars: 3703
---

# Apache Tika Content Extraction Hub

The Apache Tika Content Extraction Hub provides universal document parsing through the Apache Tika Server REST API. It extracts text, metadata, and structure from over 1400 file formats including PDF, Microsoft Office (DOCX, XLSX, PPTX), email archives (MBOX, PST), and multimedia files. The skill communicates with Tika Server endpoints including /tika for text extraction, /meta for metadata parsing, /detect/stream for MIME type detection, and /rmeta for recursive metadata extraction from container formats. Batch processing supports concurrent extraction with configurable thread pools. Advanced PDF extraction uses Tika PDFParser with OCR fallback via integrated Tesseract for scanned pages. Embedded document extraction recursively processes attachments within ZIP archives, email messages, and OLE containers, maintaining parent-child document relationships. Metadata extraction captures Dublin Core, XMP, EXIF, and format-specific properties with normalization to a common schema. The agent supports custom Tika configurations for parser-specific settings like OCR language, PDF strategy (text vs OCR vs hybrid), and maximum extraction depth. Output formats include plain text, XHTML, and JSON with full metadata. Language detection via Tika LanguageIdentifier classifies extracted content across 70+ languages.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/apache-tika-content-extraction-hub/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/apache-tika-content-extraction-hub
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/apache-tika-content-extraction-hub`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apache-tika-content-extraction-hub/)
