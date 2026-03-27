---
name: "Apache Tika Document Extractor"
description: "Wraps Apache Tika Server REST API for extracting structured text from PDFs, DOCX, PPTX, and 1,200+ file formats. Outputs clean markdown with metadata preservation using Tika /rmeta/text endpoint and recursive parsing mode."
category: "Data Extraction & Transformation"
framework: "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/apache-tika-document-extractor/"
---

# Apache Tika Document Extractor

Wraps Apache Tika Server REST API for extracting structured text from PDFs, DOCX, PPTX, and 1,200+ file formats. Outputs clean markdown with metadata preservation using Tika /rmeta/text endpoint and recursive parsing mode.

## Overview

Wraps Apache Tika Server REST API for extracting structured text from PDFs, DOCX, PPTX, and 1,200+ file formats. Outputs clean markdown with metadata preservation using Tika /rmeta/text endpoint and recursive parsing mode.

Overview

This skill provides automated integration capabilities designed for production agent workflows. It handles authentication, rate limiting, and error recovery out of the box, allowing agents to focus on high-level task orchestration rather than low-level API management.

Key Features

Automatic retry logic with exponential backoff for API rate limits

Structured output formatting compatible with downstream agent pipelines

Comprehensive error handling with actionable diagnostic messages

Configurable caching layer to reduce redundant API calls

Usage

Install via the Agent Skill Exchange registry and configure with your API credentials. The skill exposes a standardized interface that works across supported agent frameworks, with framework-specific optimizations applied automatically during initialization.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill apache-tika-document-extractor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill apache-tika-document-extractor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill apache-tika-document-extractor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill apache-tika-document-extractor -a codex
```

### OpenClaw

```bash
clawhub install apache-tika-document-extractor
```

## Source

- Marketplace: https://agentskillexchange.com/skills/apache-tika-document-extractor/
