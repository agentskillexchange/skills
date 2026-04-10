---
title: "Apache Tika Document Extractor"
description: "Wraps Apache Tika Server REST API for extracting structured text from PDFs, DOCX, PPTX, and 1,200+ file formats. Outputs clean markdown with metadata preservation using Tika /rmeta/text endpoint and recursive parsing mode."
slug: "apache-tika-document-extractor"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/apache-tika-document-extractor/"
---

# Apache Tika Document Extractor

Wraps Apache Tika Server REST API for extracting structured text from PDFs, DOCX, PPTX, and 1,200+ file formats. Outputs clean markdown with metadata preservation using Tika /rmeta/text endpoint and recursive parsing mode.

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
clawhub install apache-tika-document-extractor
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Overview
This skill provides automated integration capabilities designed for production agent workflows. It handles authentication, rate limiting, and error recovery out of the box, allowing agents to focus on high-level task orchestration rather than low-level API management.
Key Features
- Automatic retry logic with exponential backoff for API rate limits
- Structured output formatting compatible with downstream agent pipelines
- Comprehensive error handling with actionable diagnostic messages
- Configurable caching layer to reduce redundant API calls
Usage
Install via the Agent Skill Exchange registry and configure with your API credentials. The skill exposes a standardized interface that works across supported agent frameworks, with framework-specific optimizations applied automatically during initialization.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apache-tika-document-extractor/)
