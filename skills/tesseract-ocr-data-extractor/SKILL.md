---
title: "Tesseract OCR Data Extractor"
description: "Extracts structured data from scanned documents using Tesseract OCR engine with LSTM models. Supports table detection via OpenCV contour analysis and outputs to CSV, JSON, or Pandas DataFrames."
verification: "security_reviewed"
source: "https://github.com/tesseract-ocr/tesseract"
category:
  - "Data Extraction & Transformation"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "tesseract-ocr/tesseract"
  github_stars: 73629
---

# Tesseract OCR Data Extractor

The Tesseract OCR Data Extractor combines the Tesseract 5 LSTM OCR engine with OpenCV preprocessing for high-accuracy text extraction from scanned documents, receipts, invoices, and forms. It handles multi-language recognition with traineddata models for over 100 languages. Image preprocessing pipeline includes deskewing via Hough line transform, adaptive thresholding with Otsu method, noise reduction using morphological operations, and resolution upscaling with Lanczos interpolation. These steps significantly improve recognition accuracy on low-quality scans. Table detection uses OpenCV contour analysis to identify grid structures, separating cell boundaries through horizontal and vertical line detection with cv2.getStructuringElement kernels. Extracted table data maintains row-column relationships and exports to CSV, JSON, or Pandas DataFrames for downstream analysis. The skill supports PDF input via pdf2image conversion with Poppler, batch processing of multi-page documents, and confidence scoring per recognized word. Custom vocabulary lists and user patterns improve domain-specific accuracy for medical, legal, and financial documents. Output includes bounding box coordinates for each text region enabling overlay visualization.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/tesseract-ocr-data-extractor/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/tesseract-ocr-data-extractor
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/tesseract-ocr-data-extractor`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tesseract-ocr-data-extractor/)
