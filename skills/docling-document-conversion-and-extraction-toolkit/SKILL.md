---
title: Docling Document Conversion and Extraction Toolkit
description: 'Docling is a document conversion and extraction toolkit designed to
  turn messy enterprise documents into structured data that downstream agents can
  actually use. The upstream project lives at github.com/docling-project/docling with
  an MIT license, release tags, and a high-activity commit history, and it publishes
  documentation at docling-project.github.io/docling. In practice, Docling helps an
  agent ingest PDFs, presentations, spreadsheets, HTML pages, images, and Office documents,
  then normalize them into text, markdown, JSON, or richer document representations
  that preserve layout and semantic structure. This makes it a good ASE candidate
  for data extraction and transformation workflows. An agent can use Docling before
  retrieval, summarization, indexing, or validation steps, especially when raw OCR
  or plain text extraction is not enough. The toolkit is especially useful in pipelines
  that need table preservation, section-aware parsing, or consistent chunking before
  sending content into embeddings, search indexes, or LLM prompts. Because the project
  ships as a Python package, it integrates cleanly with notebooks, ETL jobs, batch
  workers, FastAPI services, and CLI-based automation. The real install path is straightforward:
  the project docs recommend installing the docling package from pip, with Python
  3.10 or higher for current releases. For agents working across invoices, reports,
  manuals, and mixed document corpora, Docling provides a concrete, production-relevant
  job to be done: convert source files into structured machine-readable artifacts
  with better fidelity than ad hoc parsing.'
verification: security_reviewed
source: https://github.com/docling-project/docling
category:
- Data Extraction &amp; Transformation
framework:
- Multi-Framework
---

# Docling Document Conversion and Extraction Toolkit

Docling is a document conversion and extraction toolkit designed to turn messy enterprise documents into structured data that downstream agents can actually use. The upstream project lives at github.com/docling-project/docling with an MIT license, release tags, and a high-activity commit history, and it publishes documentation at docling-project.github.io/docling. In practice, Docling helps an agent ingest PDFs, presentations, spreadsheets, HTML pages, images, and Office documents, then normalize them into text, markdown, JSON, or richer document representations that preserve layout and semantic structure. This makes it a good ASE candidate for data extraction and transformation workflows. An agent can use Docling before retrieval, summarization, indexing, or validation steps, especially when raw OCR or plain text extraction is not enough. The toolkit is especially useful in pipelines that need table preservation, section-aware parsing, or consistent chunking before sending content into embeddings, search indexes, or LLM prompts. Because the project ships as a Python package, it integrates cleanly with notebooks, ETL jobs, batch workers, FastAPI services, and CLI-based automation. The real install path is straightforward: the project docs recommend installing the docling package from pip, with Python 3.10 or higher for current releases. For agents working across invoices, reports, manuals, and mixed document corpora, Docling provides a concrete, production-relevant job to be done: convert source files into structured machine-readable artifacts with better fidelity than ad hoc parsing.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docling-document-conversion-and-extraction-toolkit/)
