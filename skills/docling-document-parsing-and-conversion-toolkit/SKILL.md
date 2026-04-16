---
title: "Docling Document Parsing and Conversion Toolkit"
description: "Docling is an open source document processing toolkit that converts PDFs, Office files, HTML, images, audio, and more into structured outputs for AI workflows. It supports local execution, OCR, and integrations with agent frameworks and retrieval pipelines."
verification: "security_reviewed"
source: "https://github.com/docling-project/docling"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "docling-project/docling"
  github_stars: 57622
---

# Docling Document Parsing and Conversion Toolkit

Docling is an open source document parsing and conversion project that focuses on preparing real-world documents for AI and automation workflows. The upstream repository and docs show support for PDF, DOCX, PPTX, XLSX, HTML, images, audio, WebVTT, LaTeX, and plain text inputs, with output options including Markdown, HTML, JSON, and DocTags. For agent use cases, that means a single tool can normalize messy source material into formats that are easier to search, summarize, chunk, and pass into downstream models.

Its job to be done is concrete: take heterogeneous files and turn them into structured, machine-usable representations without forcing every workflow to build a custom parser. Docling also exposes OCR support for scanned PDFs and images, ships a CLI for direct conversion, and documents integrations with ecosystems such as LangChain, LlamaIndex, CrewAI, and Haystack. Those integration points make it especially useful for ingestion pipelines, document QA systems, knowledge base preparation, and batch content extraction jobs where agents need more than plain text scraping.

The project has strong intake evidence. It has an official GitHub repository, live documentation, a published PyPI package, an MIT license, and recent repository activity. The maintainers also document a straightforward install path and current Python version requirements, which keeps adoption friction low for marketplace users looking for a real upstream tool rather than a speculative pattern.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docling-document-parsing-and-conversion-toolkit/)
