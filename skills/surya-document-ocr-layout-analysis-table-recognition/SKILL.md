---
title: "Surya Document OCR with Layout Analysis and Table Recognition"
description: "Surya is a document OCR toolkit by Datalab that performs OCR in 90+ languages, line-level text detection, layout analysis, reading order detection, table recognition, and LaTeX OCR. It benchmarks favorably against cloud OCR services on a wide range of document types."
slug: "surya-document-ocr-layout-analysis-table-recognition"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://github.com/VikParuchuri/surya"
listed: true
---

# Surya Document OCR with Layout Analysis and Table Recognition

Surya is a document OCR toolkit by Datalab that performs OCR in 90+ languages, line-level text detection, layout analysis, reading order detection, table recognition, and LaTeX OCR. It benchmarks favorably against cloud OCR services on a wide range of document types.

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
clawhub install surya-document-ocr-layout-analysis-table-recognition
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Surya is an open-source document intelligence toolkit created by Vik Paruchuri at Datalab. Named after the Hindu sun god who has universal vision, Surya provides a comprehensive suite of document understanding capabilities that go well beyond simple text extraction. The project has gained significant traction in the developer community for its accuracy that benchmarks favorably against commercial cloud OCR services.
Core Features
Surya provides six core capabilities: OCR in 90+ languages, line-level text detection in any language, layout analysis (detecting tables, images, headers, and other structural elements), reading order detection, table recognition (detecting rows and columns), and LaTeX OCR for mathematical expressions. It handles a wide variety of document types including Japanese, Chinese, Hindi, and Arabic documents, scientific papers, scanned forms, textbooks, newspaper layouts, and presentations.
Technical Architecture
Surya uses deep learning models that can run on both CPU and GPU. The toolkit is distributed as a Python package installable via pip. It includes benchmarking tools to compare against Tesseract and other OCR engines using real-world and synthetic PDFs from Common Crawl. The project measures normalized sentence similarity on a 0-1 scale for accuracy evaluation.
Agent Integration
An AI agent can use Surya to extract structured text from uploaded documents, understand document layouts before processing, detect table structures in scanned PDFs, determine reading order for complex multi-column layouts, and extract LaTeX from mathematical content. The Python API supports batch processing and can be integrated into document processing pipelines alongside tools like Marker (by the same author) for PDF-to-Markdown conversion.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/surya-document-ocr-layout-analysis-table-recognition/)
