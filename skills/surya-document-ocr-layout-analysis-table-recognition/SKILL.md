---
title: "Surya Document OCR with Layout Analysis and Table Recognition"
description: "Surya is a document OCR toolkit by Datalab that performs OCR in 90+ languages, line-level text detection, layout analysis, reading order detection, table recognition, and LaTeX OCR. It benchmarks favorably against cloud OCR services on a wide range of document types."
verification: security_reviewed
source: "https://github.com/VikParuchuri/surya"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "vikparuchuri/surya"
  github_stars: 19530
---

# Surya Document OCR with Layout Analysis and Table Recognition

Surya is an open-source document intelligence toolkit created by Vik Paruchuri at Datalab. Named after the Hindu sun god who has universal vision, Surya provides a comprehensive suite of document understanding capabilities that go well beyond simple text extraction. The project has gained significant traction in the developer community for its accuracy that benchmarks favorably against commercial cloud OCR services.

Core Features
Surya provides six core capabilities: OCR in 90+ languages, line-level text detection in any language, layout analysis (detecting tables, images, headers, and other structural elements), reading order detection, table recognition (detecting rows and columns), and LaTeX OCR for mathematical expressions. It handles a wide variety of document types including Japanese, Chinese, Hindi, and Arabic documents, scientific papers, scanned forms, textbooks, newspaper layouts, and presentations.

Technical Architecture
Surya uses deep learning models that can run on both CPU and GPU. The toolkit is distributed as a Python package installable via pip. It includes benchmarking tools to compare against Tesseract and other OCR engines using real-world and synthetic PDFs from Common Crawl. The project measures normalized sentence similarity on a 0-1 scale for accuracy evaluation.

Agent Integration
An AI agent can use Surya to extract structured text from uploaded documents, understand document layouts before processing, detect table structures in scanned PDFs, determine reading order for complex multi-column layouts, and extract LaTeX from mathematical content. The Python API supports batch processing and can be integrated into document processing pipelines alongside tools like Marker (by the same author) for PDF-to-Markdown conversion.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/surya-document-ocr-layout-analysis-table-recognition/)
