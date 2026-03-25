---
name: "Tesseract OCR Data Extractor"
description: "Extracts structured data from scanned documents using Tesseract OCR engine with LSTM models. Supports table detection via OpenCV contour analysis and outputs to CSV, JSON, or Pandas DataFrames."
category: "Data Extraction & Transformation"
framework: "Gemini"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/tesseract-ocr-data-extractor/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "pandas"  # from ase_tool_match
  github_stars: 48239  # from ase_github_stars (integer, not string)
  github_repo: "pandas-dev/pandas"  # from ase_github_repo
  license: "BSD-3-Clause"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Tesseract OCR Data Extractor

Extracts structured data from scanned documents using Tesseract OCR engine with LSTM models. Supports table detection via OpenCV contour analysis and outputs to CSV, JSON, or Pandas DataFrames.

## Overview

The Tesseract OCR Data Extractor combines the Tesseract 5 LSTM OCR engine with OpenCV preprocessing for high-accuracy text extraction from scanned documents, receipts, invoices, and forms. It handles multi-language recognition with traineddata models for over 100 languages.

Image preprocessing pipeline includes deskewing via Hough line transform, adaptive thresholding with Otsu method, noise reduction using morphological operations, and resolution upscaling with Lanczos interpolation. These steps significantly improve recognition accuracy on low-quality scans.

Table detection uses OpenCV contour analysis to identify grid structures, separating cell boundaries through horizontal and vertical line detection with cv2.getStructuringElement kernels. Extracted table data maintains row-column relationships and exports to CSV, JSON, or Pandas DataFrames for downstream analysis.

The skill supports PDF input via pdf2image conversion with Poppler, batch processing of multi-page documents, and confidence scoring per recognized word. Custom vocabulary lists and user patterns improve domain-specific accuracy for medical, legal, and financial documents. Output includes bounding box coordinates for each text region enabling overlay visualization.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill tesseract-ocr-data-extractor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill tesseract-ocr-data-extractor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill tesseract-ocr-data-extractor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill tesseract-ocr-data-extractor -a codex
```

### OpenClaw

```bash
clawhub install tesseract-ocr-data-extractor
```

## Source

- Marketplace: https://agentskillexchange.com/skills/tesseract-ocr-data-extractor/
