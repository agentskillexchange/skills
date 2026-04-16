---
title: "Tesseract OCR Data Extractor"
description: "Extracts structured data from scanned documents using Tesseract OCR engine with LSTM models. Supports table detection via OpenCV contour analysis and outputs to CSV, JSON, or Pandas DataFrames."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/tesseract-ocr-data-extractor/"
category:
  - "Data Extraction & Transformation"
framework:
  - "Gemini"
---

# Tesseract OCR Data Extractor

The Tesseract OCR Data Extractor combines the Tesseract 5 LSTM OCR engine with OpenCV preprocessing for high-accuracy text extraction from scanned documents, receipts, invoices, and forms. It handles multi-language recognition with traineddata models for over 100 languages.


Image preprocessing pipeline includes deskewing via Hough line transform, adaptive thresholding with Otsu method, noise reduction using morphological operations, and resolution upscaling with Lanczos interpolation. These steps significantly improve recognition accuracy on low-quality scans.


Table detection uses OpenCV contour analysis to identify grid structures, separating cell boundaries through horizontal and vertical line detection with cv2.getStructuringElement kernels. Extracted table data maintains row-column relationships and exports to CSV, JSON, or Pandas DataFrames for downstream analysis.


The skill supports PDF input via pdf2image conversion with Poppler, batch processing of multi-page documents, and confidence scoring per recognized word. Custom vocabulary lists and user patterns improve domain-specific accuracy for medical, legal, and financial documents. Output includes bounding box coordinates for each text region enabling overlay visualization.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tesseract-ocr-data-extractor/)
