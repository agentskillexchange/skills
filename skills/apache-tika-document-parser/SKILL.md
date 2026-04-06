---
name: Apache Tika Document Parser
description: Extracts structured text, metadata, and embedded objects from PDFs, Office
  documents, and 1000+ file formats using the Apache Tika REST API. Outputs clean
  Markdown or JSON with XMP metadata preservation.
category: "Data Extraction &amp; Transformation"
framework: Gemini
verification: security_reviewed
source: "https://agentskillexchange.com/skills/apache-tika-document-parser/"
---
# Apache Tika Document Parser

Extracts structured text, metadata, and embedded objects from PDFs, Office documents, and 1000+ file formats using the Apache Tika REST API. Outputs clean Markdown or JSON with XMP metadata preservation.

The Apache Tika Document Parser skill provides universal document extraction using the Apache Tika content analysis framework via its REST API. It handles over 1,000 file formats including PDF, DOCX, XLSX, PPTX, EML, MSG, HTML, and legacy formats like WPD and RTF.

The skill sends documents to a Tika server instance and retrieves extracted text in multiple output formats: plain text, XHTML, or structured JSON. It preserves document metadata including XMP, Dublin Core, and format-specific properties. For PDFs, it leverages Tika’s OCR integration via Tesseract for scanned document text extraction.

Advanced capabilities include recursive extraction of embedded objects (images, attachments in emails, OLE objects in Office documents), language detection using Tika’s language identifier, and content-type detection independent of file extensions. The skill supports batch processing with configurable parallelism and outputs clean Markdown suitable for LLM consumption or vector embedding pipelines.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill apache-tika-document-parser
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill apache-tika-document-parser -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill apache-tika-document-parser -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill apache-tika-document-parser -a codex
```

### OpenClaw

```bash
clawhub install apache-tika-document-parser
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apache-tika-document-parser/)
