---
name: "MinerU PDF-to-Markdown Document Parser"
description: "Transforms complex PDFs into LLM-ready markdown and JSON using MinerU, a high-accuracy document intelligence pipeline. Extracts text, tables, formulas, and images from scientific papers, reports, and scanned documents with layout-aware parsing."
category: "Developer Tools"
framework: "Claude Code"
verification: listed  # security_reviewed or listed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/mineru-pdf-to-markdown-document-parser/"
---

# MinerU PDF-to-Markdown Document Parser

MinerU is an open-source document parsing tool developed by OpenDataLab that converts PDFs into machine-readable formats including markdown and structured JSON. Born from the pre-training pipeline of InternLM, MinerU focuses on high-fidelity extraction from complex documents including scientific literature, financial reports, and scanned pages.
The MinerU PDF-to-Markdown Document Parser skill wraps the MinerU CLI and Python API to provide agents with reliable document extraction capabilities. Given a PDF file or URL, the skill runs MinerU’s hybrid parsing backend which combines vision-language model (VLM) understanding with traditional pipeline processing. This hybrid approach extracts native text from text-based PDFs while using OCR for scanned content, supporting 109 languages for optical character recognition.
MinerU handles layout-aware parsing that preserves document structure: headers, paragraphs, lists, tables with cell-level accuracy, inline and display mathematical formulas (LaTeX output), and embedded images. The tool removes headers, footers, footnotes, and page numbers automatically, producing clean output ready for downstream LLM consumption. Cross-page table merging ensures that tables split across pages are reassembled correctly.
Output formats include markdown (optimized for LLM context windows) and structured JSON (for programmatic access to individual document elements). The skill supports GPU acceleration via CUDA, and also runs on CPU for environments without GPU access. Installation is straightforward via pip with pip install mineru[all], which installs all backend dependencies automatically.
Integration points include direct Python API usage for embedding in data pipelines, CLI usage for batch processing of document collections, and a Gradio-based web interface for interactive use. MinerU pairs well with RAG pipelines, knowledge base construction, and any workflow requiring structured extraction from PDF documents. With over 57,000 GitHub stars and active development, MinerU is one of the most widely adopted open-source document parsing tools available.


## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill mineru-pdf-to-markdown-document-parser
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill mineru-pdf-to-markdown-document-parser -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill mineru-pdf-to-markdown-document-parser -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill mineru-pdf-to-markdown-document-parser -a codex
```

### OpenClaw

```bash
clawhub install mineru-pdf-to-markdown-document-parser
```
