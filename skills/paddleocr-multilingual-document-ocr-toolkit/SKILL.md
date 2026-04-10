---
name: PaddleOCR Multilingual Document OCR and Structured Data Toolkit
description: PaddleOCR is a powerful, lightweight OCR toolkit developed by Baidu that
  converts documents and images into structured, AI-friendly data like JSON and Markdown.
  It supports 100+ languages with industry-leading accuracy, bridging the gap between
  images/PDFs and LLMs.
verification: security_reviewed
source: https://github.com/PaddlePaddle/PaddleOCR
category:
- Data Extraction &amp; Transformation
framework:
- Multi-Framework
tool_ecosystem:
  license: Apache-2.0
---
# PaddleOCR Multilingual Document OCR and Structured Data Toolkit

PaddleOCR is an open-source, production-grade Optical Character Recognition toolkit developed by Baidu as part of the PaddlePaddle ecosystem. With over 60,000 GitHub stars, it has become the premier solution for developers building intelligent document applications in the AI era. The toolkit converts PDFs, scanned documents, and images into structured data formats including JSON and Markdown, making them ready for downstream AI and LLM processing.
Core Capabilities
PaddleOCR 3.0 includes several specialized pipelines. PP-OCRv5 provides universal scene text recognition supporting five text types (Simplified Chinese, Traditional Chinese, English, Japanese, and Pinyin) with a 13% accuracy improvement over previous versions. PP-StructureV3 handles complex document parsing, intelligently converting PDFs and document images into Markdown and JSON while preserving original layout and hierarchical structure. PP-ChatOCRv4 integrates with large language models for intelligent information extraction from documents.
Integration and Deployment
PaddleOCR provides an MCP server for integration with AI agent applications like Claude Desktop. It supports three working modes: local Python library, cloud service, and self-hosted service. The toolkit can be invoked via stdio for local services and Streamable HTTP for remote services. It is deeply integrated into leading projects like MinerU, RAGFlow, pathway, and cherry-studio.
Agent Integration
An AI coding agent can use PaddleOCR to extract text and structure from uploaded documents, parse tables from scanned PDFs, convert image-based documents into editable text, and feed structured document data into RAG pipelines. The Python API makes it straightforward to integrate into any automation workflow, and the MCP server enables direct use from AI assistants.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/paddleocr-multilingual-document-ocr-toolkit/)
