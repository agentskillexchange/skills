---
title: "Tesseract OCR Document Extractor"
description: "Extracts structured text from scanned documents and images using Tesseract OCR with custom LSTM training data. Supports table detection via OpenCV contour analysis and PDF/A output generation."
verification: "security_reviewed"
source: "https://github.com/tesseract-ocr/tesseract"
category:
  - "Data Extraction & Transformation"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "tesseract-ocr/tesseract"
  github_stars: 73614
---

# Tesseract OCR Document Extractor

The Tesseract OCR Document Extractor processes scanned documents, photographs of text, and faxed PDFs using the Tesseract 5.x LSTM engine with configurable page segmentation modes (PSM). It applies OpenCV preprocessing including adaptive thresholding, deskewing, and noise reduction to maximize recognition accuracy on low-quality inputs.

Table extraction uses OpenCV contour detection and Hough line transforms to identify cell boundaries, mapping recognized text to structured row/column positions. The output supports JSON, CSV, and pandas DataFrame formats for immediate downstream processing.

Custom training data can be generated using tesstrain makefiles for domain-specific fonts and vocabularies (medical forms, legal documents, engineering drawings). The skill handles multi-language documents with automatic script detection, supports right-to-left languages including Arabic and Hebrew, and generates PDF/A compliant output with embedded text layers for archival compliance. Confidence scores per word enable automated flagging of low-certainty extractions for human review.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/tesseract-ocr-document-extractor/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/tesseract-ocr-document-extractor
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/tesseract-ocr-document-extractor`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tesseract-ocr-document-extractor/)
