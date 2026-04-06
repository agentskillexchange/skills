---
name: Tesseract OCR Document Extractor
description: Extracts structured text from scanned documents and images using Tesseract
  OCR with custom LSTM training data. Supports table detection via OpenCV contour
  analysis and PDF/A output generation.
category: "Data Extraction &amp; Transformation"
framework: ChatGPT Agents
verification: security_reviewed
source: "https://agentskillexchange.com/skills/tesseract-ocr-document-extractor/"
---
# Tesseract OCR Document Extractor

Extracts structured text from scanned documents and images using Tesseract OCR with custom LSTM training data. Supports table detection via OpenCV contour analysis and PDF/A output generation.

The Tesseract OCR Document Extractor processes scanned documents, photographs of text, and faxed PDFs using the Tesseract 5.x LSTM engine with configurable page segmentation modes (PSM). It applies OpenCV preprocessing including adaptive thresholding, deskewing, and noise reduction to maximize recognition accuracy on low-quality inputs.

Table extraction uses OpenCV contour detection and Hough line transforms to identify cell boundaries, mapping recognized text to structured row/column positions. The output supports JSON, CSV, and pandas DataFrame formats for immediate downstream processing.

Custom training data can be generated using tesstrain makefiles for domain-specific fonts and vocabularies (medical forms, legal documents, engineering drawings). The skill handles multi-language documents with automatic script detection, supports right-to-left languages including Arabic and Hebrew, and generates PDF/A compliant output with embedded text layers for archival compliance. Confidence scores per word enable automated flagging of low-certainty extractions for human review.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill tesseract-ocr-document-extractor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill tesseract-ocr-document-extractor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill tesseract-ocr-document-extractor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill tesseract-ocr-document-extractor -a codex
```

### OpenClaw

```bash
clawhub install tesseract-ocr-document-extractor
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tesseract-ocr-document-extractor/)
