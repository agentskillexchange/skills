---
title: "Tesseract OCR Document Extractor"
description: "Extracts structured text from scanned documents and images using Tesseract OCR with custom LSTM training data. Supports table detection via OpenCV contour analysis and PDF/A output generation."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/tesseract-ocr-document-extractor/"
category:
  - "Data Extraction & Transformation"
framework:
  - "ChatGPT Agents"
---

# Tesseract OCR Document Extractor

The Tesseract OCR Document Extractor processes scanned documents, photographs of text, and faxed PDFs using the Tesseract 5.x LSTM engine with configurable page segmentation modes (PSM). It applies OpenCV preprocessing including adaptive thresholding, deskewing, and noise reduction to maximize recognition accuracy on low-quality inputs.


Table extraction uses OpenCV contour detection and Hough line transforms to identify cell boundaries, mapping recognized text to structured row/column positions. The output supports JSON, CSV, and pandas DataFrame formats for immediate downstream processing.


Custom training data can be generated using tesstrain makefiles for domain-specific fonts and vocabularies (medical forms, legal documents, engineering drawings). The skill handles multi-language documents with automatic script detection, supports right-to-left languages including Arabic and Hebrew, and generates PDF/A compliant output with embedded text layers for archival compliance. Confidence scores per word enable automated flagging of low-certainty extractions for human review.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tesseract-ocr-document-extractor/)
